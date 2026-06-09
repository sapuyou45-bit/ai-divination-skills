import json
import subprocess
import sys
import unittest

from ai_divination_skills import bazi


try:
    bazi.load_solar()
    HAVE_LUNAR = True
except ImportError:
    HAVE_LUNAR = False


@unittest.skipUnless(HAVE_LUNAR, "lunar-python not installed")
class BaziCastTests(unittest.TestCase):
    """The bazi engine is a thin wrapper over lunar-python.

    These tests pin the canonical 1990-05-20 14:30 chart so any future
    refactor (or accidental engine swap) is caught immediately.
    """

    def test_canonical_chart_1990_05_20(self):
        result = bazi.cast("1990-05-20T14:30:00")

        self.assertEqual(result["system"], "bazi")
        self.assertEqual(result["engine"], "lunar-python")
        self.assertEqual(result["shengxiao"]["char"], "马")
        self.assertEqual(result["shengxiao"]["english"], "Horse")

        self.assertEqual(result["pillars"]["year"]["ganzhi"], "庚午")
        self.assertEqual(result["pillars"]["month"]["ganzhi"], "辛巳")
        self.assertEqual(result["pillars"]["day"]["ganzhi"], "乙酉")
        self.assertEqual(result["pillars"]["hour"]["ganzhi"], "癸未")

        self.assertEqual(result["day_master"]["element"], "wood")
        self.assertEqual(result["day_master"]["polarity"], "yin")

        tally = result["five_elements_tally"]
        self.assertEqual(sum(tally.values()), 8)
        self.assertEqual(tally["metal"], 3)
        self.assertEqual(tally["fire"], 2)

    def test_pillar_elements_match_stem_branch_lookup(self):
        result = bazi.cast("2000-01-01T00:00:00")

        for pillar in result["pillars"].values():
            self.assertIn(pillar["stem"]["element"], {"wood", "fire", "earth", "metal", "water"})
            self.assertIn(pillar["branch"]["element"], {"wood", "fire", "earth", "metal", "water"})
            self.assertIn(pillar["stem"]["polarity"], {"yin", "yang"})

    def test_missing_datetime_raises(self):
        with self.assertRaises(ValueError):
            bazi.cast(None)

    def test_notes_warn_about_hour_pillar(self):
        result = bazi.cast("1990-05-20T14:30:00")
        joined = " ".join(result["notes"]).lower()
        self.assertIn("hour", joined)
        self.assertIn("invent", joined)


@unittest.skipUnless(HAVE_LUNAR, "lunar-python not installed")
class BaziCliTests(unittest.TestCase):
    def test_cli_subcommand(self):
        completed = subprocess.run(
            [sys.executable, "-m", "ai_divination_skills.cli", "bazi",
             "--datetime", "1990-05-20T14:30:00"],
            check=True, capture_output=True, text=True,
        )
        result = json.loads(completed.stdout)
        self.assertEqual(result["pillars"]["day"]["ganzhi"], "乙酉")

    def test_cli_missing_datetime_exits_nonzero(self):
        completed = subprocess.run(
            [sys.executable, "-m", "ai_divination_skills.cli", "bazi"],
            capture_output=True, text=True,
        )
        self.assertNotEqual(completed.returncode, 0)

    def test_template_bazi_is_available(self):
        completed = subprocess.run(
            [sys.executable, "-m", "ai_divination_skills.cli", "template", "bazi"],
            check=True, capture_output=True, text=True,
        )
        self.assertIn("Bazi", completed.stdout)
        self.assertIn("day_master", completed.stdout)


@unittest.skipUnless(HAVE_LUNAR, "lunar-python not installed")
class BaziMcpTests(unittest.TestCase):
    def test_mcp_tool_registered(self):
        from ai_divination_skills import mcp_server
        names = [t["name"] for t in mcp_server.TOOLS]
        self.assertIn("bazi.cast", names)

    def test_mcp_call_returns_chart(self):
        from ai_divination_skills import mcp_server
        resp = mcp_server.handle({
            "jsonrpc": "2.0", "id": 1, "method": "tools/call",
            "params": {"name": "bazi.cast",
                       "arguments": {"datetime": "1990-05-20T14:30:00"}},
        })
        text = resp["result"]["content"][0]["text"]
        payload = json.loads(text)
        self.assertEqual(payload["pillars"]["year"]["ganzhi"], "庚午")


if __name__ == "__main__":
    unittest.main()
