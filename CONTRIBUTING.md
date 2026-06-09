# Contributing

Contributions are welcome when they make the skills more accurate, safer, clearer, or easier for agents to use.

## Contribution Rules

- Keep skill names direct and short.
- Keep each `SKILL.md` concise. Put detailed reference material in `references/`.
- Scripts must be deterministic under a seed when they use randomness.
- Scripts should emit JSON by default.
- New scripts should include tests.
- Do not add network calls without a clear reason and documentation.
- Do not include proprietary deck text, copyrighted card art, or copied long-form source material.

## Adding a New Skill

New skill folders should follow this shape:

```text
skills/name/
  SKILL.md
  agents/openai.yaml
  scripts/
  references/
```

The skill should explain:

- When the agent should use it.
- What script or input produces the result.
- What reference files to read.
- What output structure to follow.
- What safety boundaries apply.

## Local development

```bash
git clone https://github.com/sapuyou45-bit/ai-divination-skills.git
cd ai-divination-skills
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
python3 -m unittest discover -s tests
ai-divination tarot --spread three-card --seed demo
```

Supported Python versions: 3.9, 3.10, 3.11, 3.12 (see CI matrix in `.github/workflows/tests.yml`).

## Pull request flow

1. Fork or branch.
2. Write code + tests. Add or update schemas under `schemas/` for any new script output.
3. Run `python3 -m unittest discover -s tests` until it passes.
4. Update `README*.md`, `docs/`, `CHANGELOG.md`, and `RELEASE_NOTES.md` where relevant.
5. Open a PR using the template — the methodology checklist must be ticked before merge.
6. CI must pass on all four Python versions. Dependabot keeps Action versions fresh — please rebase rather than re-fight.

## Releasing

Maintainer-only. See `docs/maintainer/release-and-pypi.md`.
