import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_scripts import ROOT


class PackagedInstallTests(unittest.TestCase):
    def test_ci_builds_and_smoke_tests_wheel(self):
        workflow = (ROOT / ".github" / "workflows" / "tests.yml").read_text(encoding="utf-8")

        self.assertIn('python-version: ["3.9", "3.10", "3.11", "3.12"]', workflow)
        self.assertIn('pip install -e ".[dev]"', workflow)
        self.assertIn("python3 -m unittest discover -s tests", workflow)
        self.assertIn("python3 -m build", workflow)
        self.assertIn("ai-divination tarot", workflow)
        self.assertIn("ai-divination template tarot", workflow)

    def test_cli_runs_from_package_without_repo_layout(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            package_root = Path(temp_dir) / "oraclebone"
            shutil.copytree(ROOT / "oraclebone", package_root)
            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "oraclebone.cli",
                    "tarot",
                    "--deck",
                    "major",
                    "--spread",
                    "single",
                    "--seed",
                    "package-only",
                ],
                cwd=temp_dir,
                env={**os.environ, "PYTHONPATH": temp_dir},
                check=True,
                capture_output=True,
                text=True,
            )

        result = json.loads(completed.stdout)
        self.assertEqual(result["system"], "tarot")
        self.assertEqual(result["shuffle_algorithm"], "fisher-yates")
        self.assertEqual(result["rng_mode"], "seeded-demo")

    def test_package_exposes_core_api_functions(self):
        from oraclebone.iching import cast
        from oraclebone.tarot import draw
        from oraclebone.xiaoliuren import cast_numbers

        tarot = draw("major", "single", False, "api")
        iching = cast("yarrow", "api", None)
        xiaoliuren = cast_numbers(3, 12, 7)

        self.assertEqual(tarot["system"], "tarot")
        self.assertEqual(iching["system"], "iching")
        self.assertEqual(xiaoliuren["system"], "xiaoliuren")

    def test_package_includes_interpretation_templates(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            package_root = Path(temp_dir) / "oraclebone"
            shutil.copytree(ROOT / "oraclebone", package_root)
            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "oraclebone.cli",
                    "template",
                    "iching",
                ],
                cwd=temp_dir,
                env={**os.environ, "PYTHONPATH": temp_dir},
                check=True,
                capture_output=True,
                text=True,
            )

        self.assertIn("AI interprets", completed.stdout)
        self.assertIn("I Ching Interpretation Template", completed.stdout)
        self.assertIn("Do not invent", completed.stdout)


if __name__ == "__main__":
    unittest.main()
