# Copilot / AI assistant instructions for this repository

Read `AGENTS.md` first, then this file.

## Project shape

- Python package `ai_divination_skills` exposes the CLI `ai-divination`.
- Per-skill skill folders live under `skills/<skill>/` and each ships:
  - `SKILL.md` (trigger description + workflow)
  - `agents/openai.yaml`, `agents/claude.yaml`, `agents/gemini.yaml`, `agents/cursor.mdc`
  - `scripts/` (delegates to the package; standalone fallback when copied as a folder)
  - `references/` (sources, interpretation template, cards/hexagrams reference)
- Shared cross-skill policies live in `shared/`.
- JSON output schemas live in `schemas/`.

## Non-negotiable rules when writing code

1. **Never let the model generate the divination result.** Every code path that produces a draw / hexagram / position must go through the audited script. Adapters re-export the CLI; they do not call out to a model.
2. **Randomness uses system entropy by default.** Seeded mode is reserved for tests and reproducible demos and must be documented as such in any new surface.
3. **No hidden network calls, no shelling out, no telemetry, no secret handling.** Per `SECURITY.md`.
4. **Safety boundaries:** refuse medical / legal / financial / emergency / crisis advice. See `shared/safety-policy.md`.
5. **JSON outputs need a matching schema in `schemas/` and a unit test.**
6. **Python 3.9–3.12 compatibility** (use `from __future__ import annotations` for new modules).

## Workflow expectations

- Tests must pass: `python3 -m unittest discover -s tests` (49 tests today, all four CI matrix versions).
- New behaviour must come with tests under `tests/`.
- Update `CHANGELOG.md` `[Unreleased]` for every user-facing change.
- Update `RELEASE_NOTES.md` once during the release-cutting PR.
- PRs use the checklist in `.github/PULL_REQUEST_TEMPLATE.md`.

## Releasing

Maintainer-only. See `docs/maintainer/release-and-pypi.md`. Tag `vX.Y.Z` → release workflow attaches sdist+wheel, and publishes to PyPI when `PYPI_API_TOKEN` secret is set.
