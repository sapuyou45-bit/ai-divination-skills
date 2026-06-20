import os
import re
import subprocess
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

    def test_docs_site_static_default_is_chinese(self):
        html = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")

        self.assertIn('<html lang="zh-CN">', html)
        self.assertIn("<title>AI 占卜 Skills</title>", html)
        self.assertIn("给 AI agent 使用的直接、实用占卜技能集", html)
        self.assertIn('data-lang="zh" aria-pressed="true"', html)
        self.assertIn("直接、可验证的占卜工具", html)

    def test_docs_site_default_language_falls_back_to_chinese(self):
        js = (ROOT / "docs" / "app.js").read_text(encoding="utf-8")

        self.assertNotIn("navigator.language", js)
        self.assertRegex(js, re.compile(r"function preferredLanguage\(\).*return \"zh\";", re.S))

    def test_docs_site_local_assets_exist_and_are_non_empty(self):
        html = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")

        for asset in ["styles.css", "app.js"]:
            with self.subTest(asset=asset):
                self.assertIn(f'./{asset}', html)
                path = ROOT / "docs" / asset
                self.assertTrue(path.exists(), f"{asset} should exist")
                self.assertGreater(path.stat().st_size, 0, f"{asset} should not be empty")

    def test_docs_stylesheet_contains_core_layout_and_accessibility_rules(self):
        css = (ROOT / "docs" / "styles.css").read_text(encoding="utf-8")

        for selector in [".site-header", ".hero", ".skill-grid"]:
            with self.subTest(selector=selector):
                self.assertIn(selector, css)
        self.assertIn(":focus-visible", css)
        self.assertIn("prefers-reduced-motion", css)
        self.assertIn("scroll-behavior: auto", css)

    def test_canvas_animation_respects_reduced_motion(self):
        js = (ROOT / "docs" / "app.js").read_text(encoding="utf-8")

        self.assertIn("prefers-reduced-motion: reduce", js)
        self.assertIn("prefersReducedMotion", js)
        self.assertIn("if (!prefersReducedMotion)", js)

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

    def test_readmes_point_agents_to_remote_install_runbook(self):
        install_url = "https://raw.githubusercontent.com/sapuyou45-bit/ai-divination-skills/main/docs/install.md"
        for path in [ROOT / "README.md", ROOT / "README.zh-CN.md", ROOT / "README.ja.md"]:
            readme = path.read_text(encoding="utf-8")
            with self.subTest(path=path.name):
                self.assertIn(install_url, readme)
                self.assertIn("install.sh", readme)
                self.assertIn("AI_SKILLS_DIR", readme)

    def test_install_runbook_is_agent_facing_and_bounded(self):
        runbook = (ROOT / "docs" / "install.md").read_text(encoding="utf-8")

        self.assertIn("For Humans", runbook)
        self.assertIn("For AI Agents", runbook)
        self.assertIn("~/.claude/skills", runbook)
        self.assertIn("AI_SKILLS_DIR", runbook)
        self.assertIn("Do not use `sudo`", runbook)
        self.assertIn("Do not install Python packages", runbook)
        for skill in ["tarot", "iching", "xiaoliuren"]:
            self.assertIn(skill, runbook)

    def test_install_script_is_minimal_and_skill_only(self):
        installer = (ROOT / "install.sh").read_text(encoding="utf-8")

        self.assertIn("AI_SKILLS_DIR", installer)
        self.assertIn("--dry-run", installer)
        self.assertIn("Refusing unsafe AI_SKILLS_DIR", installer)
        self.assertIn(".ai-divination-backups", installer)
        self.assertIn("verified tarot, iching, xiaoliuren", installer)
        for skill in ["tarot", "iching", "xiaoliuren"]:
            self.assertIn(skill, installer)
        for forbidden in ["sudo", "pip install", ".bashrc", ".zshrc", ".profile"]:
            self.assertNotIn(forbidden, installer)

    def test_install_script_rejects_obviously_unsafe_targets(self):
        installer = ROOT / "install.sh"

        for target in ["/", ".", str(Path.home())]:
            with self.subTest(target=target):
                completed = subprocess.run(
                    ["bash", str(installer), "--dry-run"],
                    env={**os.environ, "AI_SKILLS_DIR": target},
                    check=False,
                    capture_output=True,
                    text=True,
                )
                self.assertNotEqual(completed.returncode, 0)
                self.assertIn("Refusing unsafe AI_SKILLS_DIR", completed.stderr + completed.stdout)

    def test_docs_site_surfaces_one_line_agent_install(self):
        html = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
        js = (ROOT / "docs" / "app.js").read_text(encoding="utf-8")

        self.assertIn("docs/install.md", html)
        self.assertIn("install.sh", html)
        self.assertIn("AI_SKILLS_DIR", html)
        self.assertIn("Paste one line into your AI agent", js)

    def test_readme_language_switcher_links_to_localized_readmes(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("[English](README.md)", readme)
        self.assertIn("[简体中文](README.zh-CN.md)", readme)
        self.assertIn("[日本語](README.ja.md)", readme)
        self.assertTrue((ROOT / "README.zh-CN.md").exists())
        self.assertTrue((ROOT / "README.ja.md").exists())

    def test_readmes_do_not_repeat_docs_language_switcher(self):
        for path in [ROOT / "README.md", ROOT / "README.zh-CN.md", ROOT / "README.ja.md"]:
            readme = path.read_text(encoding="utf-8")
            with self.subTest(path=path.name):
                self.assertNotIn("?lang=en", readme)
                self.assertNotIn("?lang=zh", readme)
                self.assertNotIn("?lang=ja", readme)

    def test_readmes_use_emoji_section_headings(self):
        for path in [ROOT / "README.md", ROOT / "README.zh-CN.md", ROOT / "README.ja.md"]:
            readme = path.read_text(encoding="utf-8")
            with self.subTest(path=path.name):
                for heading in ["## ✨", "## 🧭", "## 🚀", "## 🧩", "## 🛡️", "## 🗺️", "## 📄"]:
                    self.assertIn(heading, readme)


if __name__ == "__main__":
    unittest.main()
