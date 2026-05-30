import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class MethodologyDocsTests(unittest.TestCase):
    def test_shared_methodology_defines_ai_interpretation_boundary(self):
        text = (ROOT / "shared" / "methodology.md").read_text(encoding="utf-8")

        self.assertIn("AI interprets", text)
        self.assertIn("does not generate the divination result", text)
        self.assertIn("not scientific proof", text)

    def test_each_skill_has_sources_reference(self):
        for skill in ["tarot", "iching", "xiaoliuren"]:
            path = ROOT / "skills" / skill / "references" / "sources.md"
            self.assertTrue(path.exists(), f"{skill} should have references/sources.md")
            text = path.read_text(encoding="utf-8")
            self.assertIn("Adopted", text)
            self.assertIn("Not adopted", text)

    def test_readme_mentions_methodological_rigor(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("## 🧭 Methodological Rigor", readme)
        self.assertIn("AI interprets", readme)

    def test_docs_site_mentions_interpretation_boundary(self):
        app = (ROOT / "docs" / "app.js").read_text(encoding="utf-8")

        self.assertIn("AI only interprets", app)
        self.assertIn("system randomness", app)

    def test_ci_runs_unittest_discovery(self):
        workflow = (ROOT / ".github" / "workflows" / "tests.yml").read_text(encoding="utf-8")

        self.assertIn("python3 -m unittest discover -s tests", workflow)


if __name__ == "__main__":
    unittest.main()
