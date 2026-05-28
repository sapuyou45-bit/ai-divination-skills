import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def assert_script_exists(testcase, path):
    testcase.assertTrue(path.exists(), f"{path.relative_to(ROOT)} should exist")
    return path


def run_json(*args):
    completed = subprocess.run(
        [sys.executable, *map(str, args)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


class TarotDrawTests(unittest.TestCase):
    def test_three_card_draw_returns_unique_positioned_cards(self):
        script = assert_script_exists(self, ROOT / "skills" / "tarot" / "scripts" / "draw.py")

        result = run_json(
            script,
            "--deck",
            "major",
            "--spread",
            "three-card",
            "--seed",
            "demo",
            "--reversals",
        )

        self.assertEqual(result["system"], "tarot")
        self.assertEqual(result["deck"], "major")
        self.assertEqual(result["spread"], "three-card")
        self.assertEqual([card["position"] for card in result["cards"]], ["Situation", "Obstacle", "Guidance"])
        self.assertEqual(len({card["name"] for card in result["cards"]}), 3)
        self.assertTrue(all("reversed" in card for card in result["cards"]))

    def test_decision_spread_has_clear_options(self):
        script = assert_script_exists(self, ROOT / "skills" / "tarot" / "scripts" / "draw.py")
        result = run_json(script, "--spread", "decision", "--seed", "choice")

        self.assertEqual([card["position"] for card in result["cards"]], ["Option A", "Option B", "Hidden factor", "Advice"])


class IChingCastTests(unittest.TestCase):
    def test_seeded_cast_returns_six_lines_and_hexagrams(self):
        script = assert_script_exists(self, ROOT / "skills" / "iching" / "scripts" / "cast.py")

        result = run_json(script, "--method", "random", "--seed", "demo")

        self.assertEqual(result["system"], "iching")
        self.assertEqual(len(result["lines"]), 6)
        self.assertTrue(all(line["value"] in [6, 7, 8, 9] for line in result["lines"]))
        self.assertIn("number", result["primary_hexagram"])
        self.assertIn("name", result["primary_hexagram"])
        self.assertIn("binary", result["primary_hexagram"])
        self.assertEqual(len(result["primary_hexagram"]["binary"]), 6)
        self.assertIn("changing_lines", result)
        self.assertIn("resulting_hexagram", result)

    def test_manual_line_values_are_accepted(self):
        script = assert_script_exists(self, ROOT / "skills" / "iching" / "scripts" / "cast.py")
        result = run_json(script, "--method", "manual", "--lines", "6,7,8,9,7,8")

        self.assertEqual([line["value"] for line in result["lines"]], [6, 7, 8, 9, 7, 8])
        self.assertEqual(result["changing_lines"], [1, 4])


class XiaoLiuRenCastTests(unittest.TestCase):
    def test_number_cast_returns_position_and_inputs(self):
        script = assert_script_exists(self, ROOT / "skills" / "xiaoliuren" / "scripts" / "cast.py")

        result = run_json(script, "--method", "numbers", "--month", "3", "--day", "12", "--hour", "7")

        self.assertEqual(result["system"], "xiaoliuren")
        self.assertEqual(result["inputs"], {"month": 3, "day": 12, "hour": 7})
        self.assertEqual(result["position"]["index"], 3)
        self.assertEqual(result["position"]["name_en"], "Swift Joy")
        self.assertIn("keywords", result["position"])

    def test_time_cast_accepts_explicit_datetime(self):
        script = assert_script_exists(self, ROOT / "skills" / "xiaoliuren" / "scripts" / "cast.py")
        result = run_json(script, "--method", "time", "--datetime", "2026-05-29T14:30:00")

        self.assertEqual(result["inputs"]["hour"], 8)
        self.assertIn(result["position"]["index"], [1, 2, 3, 4, 5, 6])

    def test_time_cast_handles_gregorian_day_31_fallback(self):
        script = assert_script_exists(self, ROOT / "skills" / "xiaoliuren" / "scripts" / "cast.py")
        result = run_json(script, "--method", "time", "--datetime", "2026-05-31T10:00:00")

        self.assertEqual(result["inputs"]["day"], 30)
        self.assertIn("calendar_note", result)


if __name__ == "__main__":
    unittest.main()
