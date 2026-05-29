# Release Notes

## v0.5.0 - Skill Spec Hardening

This release makes the repository stronger as an Agent skill collection, not just as a Python package.

### What's New

- **Standalone skill scripts**: copied single-skill folders now run without requiring the top-level Python package.
- **Skill frontmatter hardening**: descriptions now use `Use when...` trigger wording and avoid workflow summaries.
- **Usage boundaries**: every skill has explicit `When to Use` and `When Not to Use` sections.
- **OpenAI metadata polish**: every skill now has brand color plus small and large SVG icons.
- **Skill contract tests**: coverage checks frontmatter, referenced files, metadata assets, and single-folder script execution.
- **Dev extra**: `.[dev]` includes build, twine, and PyYAML for package and skill validation work.

## v0.4.0 - Installable Package Runtime

This release makes the CLI work from a normal package install, not only from an editable checkout.

### What's New

- **Packaged runtime**: tarot, I Ching, and Xiao Liu Ren logic now lives in importable `ai_divination_skills` modules.
- **Package-only CLI**: `ai-divination` no longer depends on top-level `skills/` files being present after installation.
- **Python API**: callers can import `draw`, `cast`, and `cast_numbers` directly.
- **Packaged templates**: interpretation templates are bundled inside the package for installed CLI use.
- **Compatibility wrappers**: existing `skills/*/scripts/*.py` paths still work and delegate to the package modules.
- **Install tests**: coverage checks package-only CLI execution and importable APIs.

## v0.3.0 - Unified CLI and Agent Interpretation Templates

This release makes the toolkit easier for agents and humans to call consistently.

### What's New

- **Unified CLI**: `ai-divination tarot`, `ai-divination iching`, and `ai-divination xiaoliuren` route to the existing audited scripts.
- **Install entry point**: `pip install -e .` exposes the `ai-divination` command for local development and agent workflows.
- **Agent templates**: `ai-divination template tarot` prints the shared interpretation protocol plus the skill-specific template.
- **Interpretation boundary**: shared and per-skill templates explicitly state that AI interprets generated results and must not invent, redraw, or recast.
- **Docs and tests**: README examples and unit tests cover the CLI and interpretation templates.

## v0.2.0 - Traditional Rigor and Auditable Randomness

This release separates the divination process from AI interpretation more strictly.

### What's New

- **Methodology**: project-level rules for randomness, traditional sources, reproducibility, and limits.
- **Tarot**: explicit Fisher-Yates shuffle with deck size, draw count, drawn indices, and RNG mode metadata.
- **I Ching**: auditable three-coin lines, digital yarrow probability mode, and a compatibility warning for `random`.
- **Xiao Liu Ren**: optional `lunar-time` mode via `lunar_python`, stronger Gregorian fallback warning, and leap-month rejection.
- **Schemas**: JSON schema files for all three script outputs.
- **CI**: GitHub Actions runs the unittest suite on push and pull requests.

## v0.1.2 - Clickable Language Switchers

This release makes language switching work like common multilingual open-source repositories.

### What's New

- **README language links**: English, Simplified Chinese, and Japanese README files link to each other.
- **Localized README files**: added `README.zh-CN.md` and `README.ja.md`.
- **Shareable docs languages**: the GitHub Pages language switcher now uses links such as `?lang=zh` and `?lang=ja`.
- **Docs UI fix**: language controls are real anchors while still switching content without leaving the page.

## v0.1.1 - Multilingual Docs Site

This release adds a GitHub Pages-ready documentation site with in-page language switching.

### What's New

- **Multilingual page**: English, Simplified Chinese, and Japanese copy.
- **Language switching**: page-level buttons switch visible content without leaving the page.
- **GitHub Pages support**: static files live in `docs/` and can be published from the `main` branch.
- **Visual docs landing page**: a lightweight canvas scene gives the project a clearer first impression.
- **Docs tests**: coverage checks that the language switcher and published docs URL are present.

### Page URL

```text
https://sapuyou45-bit.github.io/ai-divination-skills/
```

## v0.1.0 - Initial Public Release

`ai-divination-skills` starts as a small, practical toolkit for AI agents that need concrete divination results before interpretation.

### What's Included

- **Tarot skill**: draw single-card, three-card, decision, creative, and project spreads.
- **I Ching skill**: cast six-line hexagrams with primary and resulting hexagram output.
- **Xiao Liu Ren skill**: cast from lunar-style numbers or a lightweight Gregorian time fallback.
- **Shared interpretation protocol**: response format, randomness rules, safety boundaries, and tone guidance.
- **Examples**: sample readings for a decision, strategic change, and daily focus.
- **Tests**: standard-library unit tests for all three MVP scripts.

### Design Choices

- Scripts emit JSON so agents can reason from a concrete result.
- Random draws support seeded mode for reproducible demos.
- The MVP is offline by default and uses only Python standard library.
- Divination is framed as symbolic reflection, not deterministic prediction.

### Known Limitations

- Xiao Liu Ren does not calculate the Chinese lunar calendar yet. For traditional accuracy, pass lunar month, lunar day, and hour index manually.
- Tarot reference material is intentionally concise in this first release.
- The collection currently includes three skills. More systems are planned after the core structure settles.

### Try It

```bash
python3 skills/tarot/scripts/draw.py --deck major --spread three-card --reversals
python3 skills/iching/scripts/cast.py --method coins
python3 skills/xiaoliuren/scripts/cast.py --method numbers --month 3 --day 12 --hour 7
```
