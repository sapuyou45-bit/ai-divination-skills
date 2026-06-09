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


SKILLS = {
    "tarot": {
        "script": ("scripts", "draw.py"),
        "args": ["--deck", "major", "--spread", "single", "--seed", "standalone"],
    },
    "iching": {
        "script": ("scripts", "cast.py"),
        "args": ["--method", "yarrow", "--seed", "standalone"],
    },
    "xiaoliuren": {
        "script": ("scripts", "cast.py"),
        "args": ["--method", "numbers", "--month", "3", "--day", "12", "--hour", "7"],
    },
    "bazi": {
        "script": ("scripts", "cast.py"),
        "args": ["--datetime", "1990-05-20T14:30:00"],
    },
}


def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise AssertionError(f"{path} missing YAML frontmatter")
    fields = {}
    for line in match.group(1).splitlines():
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields, text


class SkillContractTests(unittest.TestCase):
    def test_skill_frontmatter_uses_trigger_only_descriptions(self):
        for skill in SKILLS:
            fields, _ = parse_frontmatter(ROOT / "skills" / skill / "SKILL.md")

            self.assertEqual(fields["name"], skill)
            self.assertTrue(fields["description"].startswith("Use when"), skill)
            self.assertLessEqual(len(fields["description"]), 500)
            self.assertNotIn("Run `", fields["description"])

    def test_skill_docs_have_usage_boundaries_and_reference_navigation(self):
        for skill in SKILLS:
            _, text = parse_frontmatter(ROOT / "skills" / skill / "SKILL.md")

            self.assertIn("## When to Use", text)
            self.assertIn("## When Not to Use", text)
            self.assertIn("references/interpretation-template.md", text)
            self.assertIn("Do not", text)

    def test_referenced_files_exist(self):
        for skill in SKILLS:
            skill_dir = ROOT / "skills" / skill
            _, text = parse_frontmatter(skill_dir / "SKILL.md")
            for reference in re.findall(r"`(references/[^`]+\.md)`", text):
                self.assertTrue((skill_dir / reference).exists(), f"{skill} references missing file {reference}")

    def test_openai_metadata_has_prompt_and_assets(self):
        for skill in SKILLS:
            metadata = (ROOT / "skills" / skill / "agents" / "openai.yaml").read_text(encoding="utf-8")

            self.assertIn(f"Use ${skill}", metadata)
            self.assertIn("brand_color:", metadata)
            icon_paths = re.findall(r'icon_(?:small|large): "([^"]+)"', metadata)
            self.assertEqual(len(icon_paths), 2, skill)
            for icon_path in icon_paths:
                self.assertTrue((ROOT / "skills" / skill / icon_path).exists(), f"{skill} missing {icon_path}")

    def test_skill_script_runs_when_single_skill_folder_is_copied(self):
        try:
            import lunar_python  # noqa: F401
            have_lunar = True
        except ImportError:
            have_lunar = False
        for skill, config in SKILLS.items():
            if skill == "bazi" and not have_lunar:
                continue
            with self.subTest(skill=skill):
                with tempfile.TemporaryDirectory() as temp_dir:
                    copied = Path(temp_dir) / skill
                    shutil.copytree(ROOT / "skills" / skill, copied)
                    script = copied.joinpath(*config["script"])
                    env = os.environ.copy()
                    env.pop("PYTHONPATH", None)
                    completed = subprocess.run(
                        [sys.executable, str(script), *config["args"]],
                        cwd=temp_dir,
                        env=env,
                        check=True,
                        capture_output=True,
                        text=True,
                    )

                result = json.loads(completed.stdout)
                self.assertEqual(result["system"], skill)


if __name__ == "__main__":
    unittest.main()
