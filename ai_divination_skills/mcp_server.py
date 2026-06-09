"""Model Context Protocol server exposing the ai-divination-skills toolkit.

This implements a minimal subset of MCP 2024-11-05 (initialize, tools/list,
tools/call) over JSON-RPC 2.0 on stdio with no third-party dependencies. It is
designed to be mounted by Claude Desktop, Codex, Continue, or any other MCP host.

Run as a CLI:

    ai-divination-mcp

Or in claude_desktop_config.json:

    {
      "mcpServers": {
        "divination": { "command": "ai-divination-mcp" }
      }
    }

All draws are still produced by the audited local scripts; the host never invents
a draw. Seeded mode is reserved for tests and reproducible demos.
"""

from __future__ import annotations

import json
import sys
from typing import Any, Callable, Dict

from ai_divination_skills import __version__, bazi, iching, tarot, xiaoliuren
from ai_divination_skills.cli import template_text, TEMPLATE_NAMES


PROTOCOL_VERSION = "2024-11-05"
SERVER_NAME = "ai-divination-skills"


def _ok(result: Any) -> Dict[str, Any]:
    return {"content": [{"type": "text", "text": json.dumps(result, ensure_ascii=False, indent=2)}]}


def _ok_text(text: str) -> Dict[str, Any]:
    return {"content": [{"type": "text", "text": text}]}


def tool_tarot_draw(args: Dict[str, Any]) -> Dict[str, Any]:
    return _ok(
        tarot.draw(
            deck_name=args.get("deck", "major"),
            spread_name=args.get("spread", "three-card"),
            reversals=bool(args.get("reversals", False)),
            seed=args.get("seed"),
        )
    )


def tool_iching_cast(args: Dict[str, Any]) -> Dict[str, Any]:
    return _ok(
        iching.cast(
            method=args.get("method", "yarrow"),
            seed=args.get("seed"),
            manual_lines=args.get("manual_lines"),
        )
    )


def tool_xiaoliuren_cast(args: Dict[str, Any]) -> Dict[str, Any]:
    method = args.get("method", "numbers")
    if method == "numbers":
        return _ok(
            xiaoliuren.cast_numbers(
                month=int(args["month"]),
                day=int(args["day"]),
                hour=int(args["hour"]),
            )
        )
    if method == "time":
        return _ok(xiaoliuren.cast_time(args.get("datetime")))
    if method == "lunar_time":
        return _ok(xiaoliuren.cast_lunar_time(args.get("datetime")))
    raise ValueError(f"Unknown xiaoliuren method: {method}")




def tool_bazi_cast(args: Dict[str, Any]) -> Dict[str, Any]:
    return _ok(bazi.cast(raw_datetime=args.get("datetime")))


def tool_interpretation_template(args: Dict[str, Any]) -> Dict[str, Any]:
    name = args.get("skill", "shared")
    if name not in TEMPLATE_NAMES:
        raise ValueError(f"Unknown template: {name}. Use one of {sorted(TEMPLATE_NAMES)}.")
    shared = template_text("shared")
    if name == "shared":
        return _ok_text(shared)
    skill_text = template_text(name)
    return _ok_text(f"{shared.rstrip()}\n\n---\n\n{skill_text}")


TOOLS = [
    {
        "name": "tarot.draw",
        "description": (
            "Draw tarot cards with audited Fisher-Yates shuffle. "
            "The host MUST NOT invent the draw. Omit `seed` for real readings; "
            "seeded mode is for tests and reproducible demos only."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "deck": {
                    "type": "string",
                    "enum": ["major", "full"],
                    "default": "major",
                    "description": "Major arcana only (22 cards) or full 78-card deck.",
                },
                "spread": {
                    "type": "string",
                    "enum": ["single", "three-card", "decision"],
                    "default": "three-card",
                },
                "reversals": {"type": "boolean", "default": False},
                "seed": {"type": "string", "description": "Optional. Test/demo only."},
            },
        },
        "_call": tool_tarot_draw,
    },
    {
        "name": "iching.cast",
        "description": (
            "Cast an I Ching hexagram. The host MUST NOT invent the cast. "
            "Use method=coins, yarrow, or manual (with manual_lines)."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "method": {"type": "string", "enum": ["coins", "yarrow", "manual"], "default": "yarrow"},
                "seed": {"type": "string", "description": "Optional. Test/demo only."},
                "manual_lines": {
                    "type": "string",
                    "description": "Required when method=manual. Six comma-separated line values 6/7/8/9.",
                },
            },
        },
        "_call": tool_iching_cast,
    },
    {
        "name": "xiaoliuren.cast",
        "description": (
            "Cast Xiao Liu Ren (\u5c0f\u516d\u58ec). The host MUST NOT invent the cast. "
            "method=numbers needs month/day/hour, method=time and method=lunar_time take an ISO datetime "
            "(lunar_time requires the optional lunar-python dependency)."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "method": {
                    "type": "string",
                    "enum": ["numbers", "time", "lunar_time"],
                    "default": "numbers",
                },
                "month": {"type": "integer", "minimum": 1, "maximum": 12},
                "day": {"type": "integer", "minimum": 1, "maximum": 31},
                "hour": {"type": "integer", "minimum": 0, "maximum": 23},
                "datetime": {"type": "string", "description": "ISO 8601 datetime for method=time or lunar_time."},
            },
        },
        "_call": tool_xiaoliuren_cast,
    },
    {
        "name": "bazi.cast",
        "description": (
            "Cast a Bazi (\u516b\u5b57 / Four Pillars) chart from a Gregorian birth datetime. "
            "The host MUST NOT invent pillars, stems, branches, or wuxing. "
            "Requires the optional lunar-python dependency."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "datetime": {
                    "type": "string",
                    "description": "Gregorian ISO 8601 birth datetime, e.g. 1990-05-20T14:30:00. The hour pillar requires an exact birth time.",
                },
            },
            "required": ["datetime"],
        },
        "_call": tool_bazi_cast,
    },
    {
        "name": "interpretation_template",
        "description": "Return the interpretation template (shared + per-skill) that the host should follow before writing an interpretation.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "skill": {
                    "type": "string",
                    "enum": sorted(TEMPLATE_NAMES),
                    "default": "shared",
                },
            },
        },
        "_call": tool_interpretation_template,
    },
]


TOOL_REGISTRY: Dict[str, Callable[[Dict[str, Any]], Dict[str, Any]]] = {
    t["name"]: t["_call"] for t in TOOLS
}


def _tools_public() -> list:
    return [{k: v for k, v in t.items() if not k.startswith("_")} for t in TOOLS]


def handle(request: Dict[str, Any]) -> Dict[str, Any] | None:
    method = request.get("method")
    req_id = request.get("id")
    params = request.get("params") or {}

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": SERVER_NAME, "version": __version__},
                "instructions": (
                    "This server exposes audited divination scripts. "
                    "Never invent a draw or cast. Run a tool, then interpret the JSON output "
                    "using interpretation_template(skill=...)."
                ),
            },
        }

    if method == "notifications/initialized":
        return None

    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": _tools_public()}}

    if method == "tools/call":
        name = params.get("name")
        arguments = params.get("arguments") or {}
        if name not in TOOL_REGISTRY:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32601, "message": f"Unknown tool: {name}"},
            }
        try:
            result = TOOL_REGISTRY[name](arguments)
            return {"jsonrpc": "2.0", "id": req_id, "result": result}
        except Exception as exc:  # noqa: BLE001 - protocol-level error wrap
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "isError": True,
                    "content": [{"type": "text", "text": f"{type(exc).__name__}: {exc}"}],
                },
            }

    if method in {"ping"}:
        return {"jsonrpc": "2.0", "id": req_id, "result": {}}

    if req_id is None:
        return None

    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": -32601, "message": f"Method not found: {method}"},
    }


def serve(stdin=None, stdout=None) -> int:
    stdin = stdin or sys.stdin
    stdout = stdout or sys.stdout
    for raw in stdin:
        line = raw.strip()
        if not line:
            continue
        try:
            request = json.loads(line)
        except json.JSONDecodeError as exc:
            error = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": f"Parse error: {exc}"},
            }
            stdout.write(json.dumps(error) + "\n")
            stdout.flush()
            continue
        response = handle(request)
        if response is None:
            continue
        stdout.write(json.dumps(response, ensure_ascii=False) + "\n")
        stdout.flush()
    return 0


def main(argv=None) -> int:
    return serve()


if __name__ == "__main__":
    raise SystemExit(main())
