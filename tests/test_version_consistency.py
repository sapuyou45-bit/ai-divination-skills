import json
import re
import unittest
from pathlib import Path

from test_scripts import ROOT


def version_from_pyproject():
    text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    match = re.search(r"(?m)^version\s*=\s*[\"']([^\"']+)[\"']", text)
    return match.group(1) if match else None


def version_from_init():
    text = (ROOT / "oraclebone" / "__init__.py").read_text(encoding="utf-8")
    match = re.search(r"__version__\s*=\s*[\"']([^\"']+)[\"']", text)
    return match.group(1) if match else None


def version_from_server_json():
    data = json.loads((ROOT / "server.json").read_text(encoding="utf-8"))
    return str(data["version"])


class VersionConsistencyTests(unittest.TestCase):
    def test_core_version_sources_agree(self):
        sources = [
            version_from_pyproject(),
            version_from_init(),
            version_from_server_json(),
        ]
        for source in sources:
            self.assertIsNotNone(source, "version source returned None")
        self.assertEqual(len(set(sources)), 1, f"core versions differ: {sources}")

    def test_every_gemini_adapter_matches_package_version(self):
        expected = version_from_pyproject()
        for yaml_path in (ROOT / "skills").glob("*/agents/gemini.yaml"):
            text = yaml_path.read_text(encoding="utf-8")
            match = re.search(r"(?m)^version\s*:\s*[\"']?([^\"'\s#]+)", text)
            self.assertIsNotNone(match, f"version missing in {yaml_path}")
            self.assertEqual(
                match.group(1),
                expected,
                f"{yaml_path} version {match.group(1)} != {expected}",
            )

    def test_check_script_succeeds(self):
        import subprocess
        import sys

        completed = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check_version_consistency.py")],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0)
        self.assertIn("OK: all versions match", completed.stdout)


if __name__ == "__main__":
    unittest.main()
