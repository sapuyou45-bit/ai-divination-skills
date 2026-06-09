"""Tests for the per-host agent adapters in skills/*/agents/."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ["tarot", "iching", "xiaoliuren", "bazi"]
ADAPTERS = ["openai.yaml", "claude.yaml", "gemini.yaml", "cursor.mdc"]

CLI = {
    "tarot": "ai-divination tarot",
    "iching": "ai-divination iching",
    "xiaoliuren": "ai-divination xiaoliuren",
    "bazi": "ai-divination bazi",
}


class AgentAdapterTests(unittest.TestCase):
    def test_every_skill_ships_every_adapter(self):
        for skill in SKILLS:
            for adapter in ADAPTERS:
                path = ROOT / "skills" / skill / "agents" / adapter
                self.assertTrue(
                    path.exists(),
                    f"missing adapter {adapter} for {skill}",
                )
                text = path.read_text(encoding="utf-8")
                self.assertGreater(len(text), 40, f"{path} looks empty")

    def test_claude_adapter_routes_through_cli(self):
        for skill in SKILLS:
            text = (ROOT / "skills" / skill / "agents" / "claude.yaml").read_text(
                encoding="utf-8"
            )
            self.assertIn(f"name: {skill}", text)
            self.assertIn(CLI[skill], text)
            self.assertIn("You do NOT generate the draw", text)

    def test_gemini_adapter_routes_through_cli(self):
        for skill in SKILLS:
            text = (ROOT / "skills" / skill / "agents" / "gemini.yaml").read_text(
                encoding="utf-8"
            )
            self.assertIn(f"name: ai-divination-{skill}", text)
            self.assertIn('command: "ai-divination"', text)
            self.assertIn(f'args: ["{skill}"]', text)
            self.assertIn("shared/safety-policy.md", text)

    def test_cursor_adapter_has_frontmatter_and_cli(self):
        for skill in SKILLS:
            text = (ROOT / "skills" / skill / "agents" / "cursor.mdc").read_text(
                encoding="utf-8"
            )
            self.assertTrue(text.startswith("---\n"), f"{skill} missing frontmatter")
            self.assertIn("alwaysApply: false", text)
            self.assertIn(CLI[skill], text)
            self.assertIn("Never invent", text)

    def test_no_adapter_invites_model_generated_draws(self):
        forbidden = [
            "you may invent",
            "make up a draw",
            "fabricate the result",
            "generate the cast yourself",
        ]
        for skill in SKILLS:
            for adapter in ADAPTERS:
                text = (
                    ROOT / "skills" / skill / "agents" / adapter
                ).read_text(encoding="utf-8").lower()
                for needle in forbidden:
                    self.assertNotIn(needle, text, f"{skill}/{adapter} contains forbidden hint: {needle}")


if __name__ == "__main__":
    unittest.main()
