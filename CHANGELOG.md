# Changelog

All notable changes to this project are documented here.
For human-readable release announcements, see `RELEASE_NOTES.md` and [GitHub Releases](https://github.com/sapuyou45-bit/ai-divination-skills/releases).

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.5.4] - 2026-06-09

### Added
- Safety / Ethics Concern issue template (`.github/ISSUE_TEMPLATE/safety_concern.yml`) with structured repro fields.
- `.github/ISSUE_TEMPLATE/config.yml` updated: direct link to GitHub private vulnerability reporting.
- `.github/copilot-instructions.md`: explicit project shape + non-negotiable rules for AI code generators.
- Dependabot grouping: GitHub Actions and pip updates each create a single monthly PR instead of several.
- `.github/PULL_REQUEST_TEMPLATE.md` now referenced from root; UI picker shows it.

### Changed
- Repo settings hardened: squash-merge only (no merge commit, no rebase), auto-merge enabled, update-branch enabled, delete-branch-on-merge.
- Wiki and Projects disabled (no content; solo repo).
- Dependabot security updates enabled, automated security fixes enabled (were off).
- Secret scanning validity checks and non-provider patterns remain off (opt-in by GitHub).


## [0.5.3] - 2026-06-09

### Added
- CodeQL static-analysis workflow (`.github/workflows/codeql.yml`) on push, PR, and weekly cron.
- Markdown link-check workflow (`.github/workflows/link-check.yml`) on markdown PRs and weekly cron, using lychee.
- "📚 Docs / Translation" issue template (`.github/ISSUE_TEMPLATE/docs.yml`).
- README now documents the four per-host adapters (OpenAI / Claude / Gemini / Cursor) and links to Discussions, Roadmap, Security.
- Simplified Chinese and Japanese READMEs now also show the same status badges as the English README.


## [0.5.2] - 2026-06-09

### Added
- Per-skill Claude (`claude.yaml`), Gemini (`gemini.yaml`), and Cursor (`cursor.mdc`) adapters for tarot / I Ching / Xiao Liu Ren. Every adapter routes through the existing audited CLI so the agent never invents a draw.
- `ROADMAP.md` linking the open issues that drive the next releases.
- New `tests/test_agent_adapters.py` (5 tests, 49 total) covering presence, CLI routing, frontmatter, and a "no invented draws" lint.

### Changed
- `main` branch is now protected: linear history, no force-pushes, no deletions, required conversation resolution, and all four `unittest (3.9|3.10|3.11|3.12)` checks must pass before merge.


## [0.5.1] - 2026-06-09

### Added
- Issue templates (bug, feature, new-skill) and PR template with methodology checklist.
- `CODEOWNERS`, `FUNDING.yml`, and `dependabot.yml` (pip + GitHub Actions, monthly).
- Tag-triggered release workflow that builds sdist + wheel and attaches them to a generated GitHub Release.
- CI matrix on Python 3.9 / 3.10 / 3.11 / 3.12 with a CLI smoke test for tarot / iching / xiaoliuren.
- Social preview image (`.github/social-preview-1280x640.png`).
- GitHub Discussions enabled and linked from the issue chooser.

### Changed
- `actions/checkout` → v6, `actions/setup-python` → v6, `actions/upload-artifact` → v7, `softprops/action-gh-release` → v3.

## [0.5.0] - Skill Spec Hardening

See `RELEASE_NOTES.md`.

## [0.4.0] - Installable Package Runtime

See `RELEASE_NOTES.md`.

## [0.3.0] - Unified CLI and Agent Interpretation Templates

See `RELEASE_NOTES.md`.

## [0.2.0] and earlier

See `RELEASE_NOTES.md` and `git log`.

[Unreleased]: https://github.com/sapuyou45-bit/ai-divination-skills/compare/v0.5.4...HEAD
[0.5.4]: https://github.com/sapuyou45-bit/ai-divination-skills/compare/v0.5.3...v0.5.4
[0.5.3]: https://github.com/sapuyou45-bit/ai-divination-skills/compare/v0.5.2...v0.5.3
[0.5.2]: https://github.com/sapuyou45-bit/ai-divination-skills/compare/v0.5.1...v0.5.2
[0.5.1]: https://github.com/sapuyou45-bit/ai-divination-skills/compare/v0.5.0...v0.5.1
[0.5.0]: https://github.com/sapuyou45-bit/ai-divination-skills/releases/tag/v0.5.0
