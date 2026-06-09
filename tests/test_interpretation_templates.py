import unittest

from test_scripts import ROOT


class InterpretationTemplateTests(unittest.TestCase):
    def test_shared_interpretation_protocol_exists_and_sets_boundary(self):
        path = ROOT / "shared" / "interpretation-protocol.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")

        self.assertIn("AI interprets", text)
        self.assertIn("does not generate the divination result", text)
        self.assertIn("Do not invent", text)
        self.assertIn("Generated Result", text)

    def test_each_skill_has_interpretation_template(self):
        for skill in ["tarot", "iching", "xiaoliuren", "bazi"]:
            path = ROOT / "skills" / skill / "references" / "interpretation-template.md"
            self.assertTrue(path.exists(), f"{skill} should have an interpretation template")
            text = path.read_text(encoding="utf-8")
            self.assertIn("Input JSON", text)
            self.assertIn("Do not invent", text)
            self.assertIn("Do not redraw", text)

    def test_readme_documents_unified_cli(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("ai-divination tarot", readme)
        self.assertIn("ai-divination template tarot", readme)
        self.assertIn("pip install -e .", readme)


if __name__ == "__main__":
    unittest.main()
