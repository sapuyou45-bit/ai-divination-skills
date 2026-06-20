import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_scripts import ROOT


class PackagedInstallTests(unittest.TestCase):
    def test_version_metadata_is_consistent(self):
        pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
        package_init = (ROOT / "ai_divination_skills" / "__init__.py").read_text(encoding="utf-8")
        setup_py = (ROOT / "setup.py").read_text(encoding="utf-8")

        pyproject_version = re.search(r'^version = "([^"]+)"', pyproject, re.MULTILINE).group(1)
        package_version = re.search(r'^__version__ = "([^"]+)"', package_init, re.MULTILINE).group(1)
        setup_version = re.search(r'version="([^"]+)"', setup_py).group(1)

        self.assertEqual(pyproject_version, package_version)
        self.assertEqual(pyproject_version, setup_version)

    def test_ci_builds_and_smoke_tests_wheel(self):
        workflow = (ROOT / ".github" / "workflows" / "tests.yml").read_text(encoding="utf-8")

        self.assertIn('python-version: ["3.9", "3.10", "3.11", "3.12"]', workflow)
        self.assertIn('python -m pip install -e ".[dev]"', workflow)
        self.assertIn("python3 -m unittest discover -s tests", workflow)
        self.assertIn("python -m build", workflow)
        self.assertIn("ai-divination tarot", workflow)
        self.assertIn("ai-divination template tarot", workflow)

    def test_cli_runs_from_package_without_repo_layout(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            package_root = Path(temp_dir) / "ai_divination_skills"
            shutil.copytree(ROOT / "ai_divination_skills", package_root)
            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "ai_divination_skills.cli",
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
        from ai_divination_skills.iching import cast
        from ai_divination_skills.tarot import draw
        from ai_divination_skills.xiaoliuren import cast_numbers

        tarot = draw("major", "single", False, "api")
        iching = cast("yarrow", "api", None)
        xiaoliuren = cast_numbers(3, 12, 7)

        self.assertEqual(tarot["system"], "tarot")
        self.assertEqual(iching["system"], "iching")
        self.assertEqual(xiaoliuren["system"], "xiaoliuren")

    def test_package_includes_interpretation_templates(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            package_root = Path(temp_dir) / "ai_divination_skills"
            shutil.copytree(ROOT / "ai_divination_skills", package_root)
            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "ai_divination_skills.cli",
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
