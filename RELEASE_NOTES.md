# Release Notes

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
