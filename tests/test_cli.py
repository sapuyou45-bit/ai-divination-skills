import json
import subprocess
import sys
import unittest

from test_scripts import ROOT


def run_cli(*args, check=True):
    return subprocess.run(
        [sys.executable, "-m", "ai_divination_skills.cli", *args],
        cwd=ROOT,
        check=check,
        capture_output=True,
        text=True,
    )


class UnifiedCliTests(unittest.TestCase):
    def test_tarot_command_delegates_to_tarot_draw(self):
        completed = run_cli("tarot", "--deck", "major", "--spread", "single", "--seed", "cli")
        result = json.loads(completed.stdout)

        self.assertEqual(result["system"], "tarot")
        self.assertEqual(result["deck"], "major")
        self.assertEqual(result["spread"], "single")
        self.assertEqual(result["rng_mode"], "seeded-demo")

    def test_iching_command_delegates_to_yarrow_cast(self):
        completed = run_cli("iching", "--method", "yarrow", "--seed", "cli")
        result = json.loads(completed.stdout)

        self.assertEqual(result["system"], "iching")
        self.assertEqual(result["method"], "yarrow")
        self.assertEqual(result["line_probabilities"], {"6": "1/16", "7": "5/16", "8": "7/16", "9": "3/16"})

    def test_xiaoliuren_command_delegates_to_number_cast(self):
        completed = run_cli("xiaoliuren", "--method", "numbers", "--month", "3", "--day", "12", "--hour", "7")
        result = json.loads(completed.stdout)

        self.assertEqual(result["system"], "xiaoliuren")
        self.assertEqual(result["method"], "numbers")
        self.assertEqual(result["position"]["name_en"], "Swift Joy")

    def test_template_command_prints_agent_interpretation_protocol(self):
        completed = run_cli("template", "tarot")

        self.assertIn("AI interprets", completed.stdout)
        self.assertIn("Do not invent", completed.stdout)
        self.assertIn("tarot", completed.stdout.lower())


if __name__ == "__main__":
    unittest.main()
