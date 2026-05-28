import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class DocsSiteTests(unittest.TestCase):
    def test_docs_site_has_three_language_switcher_links(self):
        html = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")

        self.assertIn('data-lang="en"', html)
        self.assertIn('data-lang="zh"', html)
        self.assertIn('data-lang="ja"', html)
        self.assertIn('href="?lang=en"', html)
        self.assertIn('href="?lang=zh"', html)
        self.assertIn('href="?lang=ja"', html)
        self.assertIn('aria-label="Language selector"', html)

    def test_translation_dictionary_contains_required_languages(self):
        js = (ROOT / "docs" / "app.js").read_text(encoding="utf-8")

        self.assertRegex(js, re.compile(r"const translations = \{.*\ben:", re.S))
        self.assertRegex(js, re.compile(r"const translations = \{.*\bzh:", re.S))
        self.assertRegex(js, re.compile(r"const translations = \{.*\bja:", re.S))
        self.assertIn("给 AI agent 使用的开源技能", js)
        self.assertIn("AI agent のためのオープンソース skill", js)

    def test_readme_points_to_published_pages_url(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("https://sapuyou45-bit.github.io/ai-divination-skills/", readme)

    def test_readme_language_switcher_links_to_localized_readmes(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("[English](README.md)", readme)
        self.assertIn("[简体中文](README.zh-CN.md)", readme)
        self.assertIn("[日本語](README.ja.md)", readme)
        self.assertTrue((ROOT / "README.zh-CN.md").exists())
        self.assertTrue((ROOT / "README.ja.md").exists())


if __name__ == "__main__":
    unittest.main()
