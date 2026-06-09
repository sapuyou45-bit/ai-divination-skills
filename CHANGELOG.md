# Changelog

All notable changes to this project are documented here.
For human-readable release announcements, see `RELEASE_NOTES.md` and [GitHub Releases](https://github.com/sapuyou45-bit/ai-divination-skills/releases).

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[Unreleased]: https://github.com/sapuyou45-bit/ai-divination-skills/compare/v0.5.1...HEAD
[0.5.1]: https://github.com/sapuyou45-bit/ai-divination-skills/compare/v0.5.0...v0.5.1
[0.5.0]: https://github.com/sapuyou45-bit/ai-divination-skills/releases/tag/v0.5.0
