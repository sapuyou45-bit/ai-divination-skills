import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def assert_script_exists(testcase, path):
    testcase.assertTrue(path.exists(), f"{path.relative_to(ROOT)} should exist")
    return path


def run_json(*args, env=None):
    command_env = os.environ.copy()
    if env:
        command_env.update(env)
    completed = subprocess.run(
        [sys.executable, *map(str, args)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        env=command_env,
    )
    return json.loads(completed.stdout)


def run_text(*args, env=None, check=True):
    command_env = os.environ.copy()
    if env:
        command_env.update(env)
    return subprocess.run(
        [sys.executable, *map(str, args)],
        cwd=ROOT,
        check=check,
        capture_output=True,
        text=True,
        env=command_env,
    )


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
        self.assertEqual(result["shuffle_algorithm"], "fisher-yates")
        self.assertEqual(result["deck_size"], 22)
        self.assertEqual(result["draw_count"], 3)
        self.assertEqual(result["rng_mode"], "seeded-demo")
        self.assertEqual(len(result["drawn_indices"]), 3)
        self.assertEqual([card["position"] for card in result["cards"]], ["Situation", "Obstacle", "Guidance"])
        self.assertEqual(len({card["name"] for card in result["cards"]}), 3)
        self.assertTrue(all("reversed" in card for card in result["cards"]))

    def test_decision_spread_has_clear_options(self):
        script = assert_script_exists(self, ROOT / "skills" / "tarot" / "scripts" / "draw.py")
        result = run_json(script, "--spread", "decision", "--seed", "choice")

        self.assertEqual([card["position"] for card in result["cards"]], ["Option A", "Option B", "Hidden factor", "Advice"])

    def test_full_deck_reports_seventy_eight_cards(self):
        script = assert_script_exists(self, ROOT / "skills" / "tarot" / "scripts" / "draw.py")
        result = run_json(script, "--deck", "full", "--spread", "single", "--seed", "full")

        self.assertEqual(result["deck_size"], 78)
        self.assertEqual(result["draw_count"], 1)
        self.assertEqual(len(result["drawn_indices"]), 1)


class IChingCastTests(unittest.TestCase):
    def test_seeded_cast_returns_six_lines_and_hexagrams(self):
        script = assert_script_exists(self, ROOT / "skills" / "iching" / "scripts" / "cast.py")

        result = run_json(script, "--method", "coins", "--seed", "demo")

        self.assertEqual(result["system"], "iching")
        self.assertEqual(result["method"], "coins")
        self.assertEqual(len(result["lines"]), 6)
        self.assertTrue(all(line["value"] in [6, 7, 8, 9] for line in result["lines"]))
        self.assertTrue(all(len(line["coin_tosses"]) == 3 for line in result["lines"]))
        self.assertTrue(all(len(line["coin_values"]) == 3 for line in result["lines"]))
        self.assertEqual(result["line_probabilities"], {"6": "1/8", "7": "3/8", "8": "3/8", "9": "1/8"})
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

    def test_yarrow_method_uses_yarrow_probability_table(self):
        script = assert_script_exists(self, ROOT / "skills" / "iching" / "scripts" / "cast.py")
        result = run_json(script, "--method", "yarrow", "--seed", "demo")

        self.assertEqual(result["method"], "yarrow")
        self.assertEqual(result["method_details"]["probability_model"], "digital-yarrow-equivalent")
        self.assertEqual(result["line_probabilities"], {"6": "1/16", "7": "5/16", "8": "7/16", "9": "3/16"})
        self.assertTrue(all(line["value"] in [6, 7, 8, 9] for line in result["lines"]))

    def test_random_method_is_compatibility_alias_with_warning(self):
        script = assert_script_exists(self, ROOT / "skills" / "iching" / "scripts" / "cast.py")
        result = run_json(script, "--method", "random", "--seed", "demo")

        self.assertEqual(result["method"], "coins")
        self.assertEqual(result["requested_method"], "random")
        self.assertIn("warning", result)
        self.assertIn("Use --method coins or --method yarrow", result["warning"])


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
        self.assertEqual(result["accuracy"], "gregorian-fallback")
        self.assertIn("not a traditional lunar calculation", result["warning"])

    def test_time_cast_handles_gregorian_day_31_fallback(self):
        script = assert_script_exists(self, ROOT / "skills" / "xiaoliuren" / "scripts" / "cast.py")
        result = run_json(script, "--method", "time", "--datetime", "2026-05-31T10:00:00")

        self.assertEqual(result["inputs"]["day"], 30)
        self.assertIn("calendar_note", result)

    def test_lunar_time_requires_optional_dependency(self):
        script = assert_script_exists(self, ROOT / "skills" / "xiaoliuren" / "scripts" / "cast.py")
        completed = run_text(
            script,
            "--method",
            "lunar-time",
            "--datetime",
            "2026-05-29T14:30:00",
            env={"AI_DIVINATION_DISABLE_LUNAR_PYTHON": "1"},
            check=False,
        )

        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("lunar_python is required", completed.stderr + completed.stdout)

    def test_lunar_time_converts_known_date_with_lunar_python_api(self):
        script = assert_script_exists(self, ROOT / "skills" / "xiaoliuren" / "scripts" / "cast.py")
        with tempfile.TemporaryDirectory() as temp_dir:
            fake_module = Path(temp_dir) / "lunar_python.py"
            fake_module.write_text(
                """
class FakeLunar:
    def getMonth(self):
        return 4
    def getDay(self):
        return 13
    def getMonthInChinese(self):
        return "四月"
    def getDayInChinese(self):
        return "十三"

class FakeSolar:
    def getLunar(self):
        return FakeLunar()

class Solar:
    @staticmethod
    def fromYmdHms(year, month, day, hour, minute, second):
        return FakeSolar()
""",
                encoding="utf-8",
            )
            result = run_json(
                script,
                "--method",
                "lunar-time",
                "--datetime",
                "2026-05-29T14:30:00",
                env={"PYTHONPATH": temp_dir},
            )

        self.assertEqual(result["method"], "lunar-time")
        self.assertEqual(result["inputs"], {"month": 4, "day": 13, "hour": 8})
        self.assertEqual(result["lunar_date"]["month_chinese"], "四月")
        self.assertEqual(result["accuracy"], "traditional-lunar-calendar")

    def test_lunar_time_rejects_leap_month(self):
        script = assert_script_exists(self, ROOT / "skills" / "xiaoliuren" / "scripts" / "cast.py")
        with tempfile.TemporaryDirectory() as temp_dir:
            fake_module = Path(temp_dir) / "lunar_python.py"
            fake_module.write_text(
                """
class FakeLunar:
    def getMonth(self):
        return -4
    def getDay(self):
        return 13
    def getMonthInChinese(self):
        return "闰四月"
    def getDayInChinese(self):
        return "十三"

class FakeSolar:
    def getLunar(self):
        return FakeLunar()

class Solar:
    @staticmethod
    def fromYmdHms(year, month, day, hour, minute, second):
        return FakeSolar()
""",
                encoding="utf-8",
            )
            completed = run_text(
                script,
                "--method",
                "lunar-time",
                "--datetime",
                "2026-05-29T14:30:00",
                env={"PYTHONPATH": temp_dir},
                check=False,
            )

        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("Leap lunar month", completed.stderr + completed.stdout)


if __name__ == "__main__":
    unittest.main()
