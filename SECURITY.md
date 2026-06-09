# Security Policy

## Supported Versions

The latest minor version on the `main` branch is supported. Older tagged releases are not backported.

| Version | Supported          |
| ------- | ------------------ |
| 0.5.x   | ✅                 |
| < 0.5   | ❌                 |

The shipped scripts are local-only and use the Python standard library plus optional `lunar-python` for Xiao Liu Ren's `time` mode.

## Reporting a Vulnerability

For **non-sensitive** issues (e.g. dependency hardening, packaging mistakes), open a public issue with the `safety` label.

For **sensitive** issues (anything that could harm a user if disclosed before a fix), please **do not** open a public issue. Use GitHub's private vulnerability reporting:

1. Go to https://github.com/sapuyou45-bit/ai-divination-skills/security/advisories/new.
2. Describe the impact, the affected version(s), and a minimal reproduction.
3. The maintainer aims to acknowledge within 7 days and ship a fix or mitigation within 30 days for high-severity reports.

If GitHub private reporting is unavailable to you, open a minimal public issue asking for a private contact and the maintainer will respond.

## Project Expectations

These are the contracts every shipped skill must respect:

- No hidden network calls.
- No reading unrelated user files.
- No shelling out from scripts unless explicitly documented.
- No telemetry.
- No secret handling.
- Optional dependencies (currently only `lunar-python`) are documented in `pyproject.toml` under `[project.optional-dependencies]`.

## Reviewing Third-party Skills

Before installing third-party contributed skills, inspect any scripts they ask the agent to run. The project's PR template enforces a methodology checklist (see `shared/methodology.md`) but third-party forks bypass that gate.
