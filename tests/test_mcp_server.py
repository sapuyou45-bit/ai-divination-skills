"""Tests for the MCP server."""

import io
import json
import unittest

from ai_divination_skills import mcp_server


class HandleTests(unittest.TestCase):
    def test_initialize_returns_capabilities(self):
        resp = mcp_server.handle({"jsonrpc": "2.0", "id": 1, "method": "initialize"})
        self.assertEqual(resp["id"], 1)
        result = resp["result"]
        self.assertEqual(result["protocolVersion"], mcp_server.PROTOCOL_VERSION)
        self.assertEqual(result["serverInfo"]["name"], mcp_server.SERVER_NAME)
        self.assertIn("Never invent", result["instructions"])
        self.assertIn("tools", result["capabilities"])

    def test_tools_list_returns_all_four_tools(self):
        resp = mcp_server.handle({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
        tools = resp["result"]["tools"]
        names = [t["name"] for t in tools]
        self.assertEqual(
            sorted(names),
            sorted(["tarot.draw", "iching.cast", "xiaoliuren.cast", "interpretation_template"]),
        )
        for tool in tools:
            self.assertIn("description", tool)
            self.assertIn("inputSchema", tool)
            self.assertNotIn("_call", tool)

    def test_tarot_draw_via_tools_call(self):
        resp = mcp_server.handle({
            "jsonrpc": "2.0", "id": 3, "method": "tools/call",
            "params": {"name": "tarot.draw", "arguments": {"spread": "single", "seed": "demo"}},
        })
        text = resp["result"]["content"][0]["text"]
        data = json.loads(text)
        self.assertEqual(data["system"], "tarot")
        self.assertEqual(data["spread"], "single")
        self.assertEqual(data["rng_mode"], "seeded-demo")

    def test_iching_cast_via_tools_call(self):
        resp = mcp_server.handle({
            "jsonrpc": "2.0", "id": 4, "method": "tools/call",
            "params": {"name": "iching.cast", "arguments": {"method": "yarrow", "seed": "demo"}},
        })
        data = json.loads(resp["result"]["content"][0]["text"])
        self.assertEqual(data["system"], "iching")
        self.assertEqual(data["method"], "yarrow")

    def test_xiaoliuren_cast_numbers_via_tools_call(self):
        resp = mcp_server.handle({
            "jsonrpc": "2.0", "id": 5, "method": "tools/call",
            "params": {"name": "xiaoliuren.cast", "arguments": {"method": "numbers", "month": 3, "day": 12, "hour": 7}},
        })
        data = json.loads(resp["result"]["content"][0]["text"])
        self.assertEqual(data["system"], "xiaoliuren")

    def test_interpretation_template_combines_shared_and_skill(self):
        resp = mcp_server.handle({
            "jsonrpc": "2.0", "id": 6, "method": "tools/call",
            "params": {"name": "interpretation_template", "arguments": {"skill": "tarot"}},
        })
        text = resp["result"]["content"][0]["text"]
        self.assertIn("Interpretation Protocol", text)
        self.assertIn("---", text)

    def test_unknown_tool_returns_error_content(self):
        resp = mcp_server.handle({
            "jsonrpc": "2.0", "id": 7, "method": "tools/call",
            "params": {"name": "bogus", "arguments": {}},
        })
        self.assertEqual(resp["error"]["code"], -32601)

    def test_invalid_tool_args_returned_as_isError(self):
        resp = mcp_server.handle({
            "jsonrpc": "2.0", "id": 8, "method": "tools/call",
            "params": {"name": "xiaoliuren.cast", "arguments": {"method": "numbers"}},
        })
        result = resp["result"]
        self.assertTrue(result.get("isError"))
        self.assertIn("KeyError", result["content"][0]["text"])

    def test_unknown_method_returns_jsonrpc_error(self):
        resp = mcp_server.handle({"jsonrpc": "2.0", "id": 9, "method": "no_such_method"})
        self.assertEqual(resp["error"]["code"], -32601)

    def test_initialized_notification_returns_none(self):
        resp = mcp_server.handle({"jsonrpc": "2.0", "method": "notifications/initialized"})
        self.assertIsNone(resp)


class ServeStdioTests(unittest.TestCase):
    def test_serve_full_handshake_over_stdio(self):
        requests = [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize"},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
            {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
             "params": {"name": "iching.cast", "arguments": {"method": "yarrow", "seed": "demo"}}},
        ]
        stdin = io.StringIO("\n".join(json.dumps(r) for r in requests) + "\n")
        stdout = io.StringIO()
        rc = mcp_server.serve(stdin=stdin, stdout=stdout)
        self.assertEqual(rc, 0)
        responses = [json.loads(line) for line in stdout.getvalue().splitlines() if line.strip()]
        # 3 responses (the notification has no reply)
        self.assertEqual(len(responses), 3)
        self.assertEqual(responses[0]["id"], 1)
        self.assertEqual(responses[1]["id"], 2)
        self.assertEqual(responses[2]["id"], 3)

    def test_serve_handles_invalid_json(self):
        stdin = io.StringIO('not-json\n{"jsonrpc":"2.0","id":1,"method":"initialize"}\n')
        stdout = io.StringIO()
        mcp_server.serve(stdin=stdin, stdout=stdout)
        responses = [json.loads(line) for line in stdout.getvalue().splitlines() if line.strip()]
        self.assertEqual(len(responses), 2)
        self.assertEqual(responses[0]["error"]["code"], -32700)
        self.assertEqual(responses[1]["id"], 1)


if __name__ == "__main__":
    unittest.main()
