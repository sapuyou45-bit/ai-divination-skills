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
