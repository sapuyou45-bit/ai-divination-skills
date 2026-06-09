## Summary

<!-- What does this PR change, and why? Reference any related issue. -->

## Type of change

- [ ] New skill / new divination system
- [ ] New spread or casting method for an existing skill
- [ ] CLI / packaging change
- [ ] Documentation, examples, or translations
- [ ] Bug fix
- [ ] Refactor / chore

## Methodology checklist

The project rule is: **scripts (or user-provided physical casts) generate the result; AI interprets that result.** Confirm the following before merge:

- [ ] No code path lets the AI invent, redraw, or recast the divination result.
- [ ] Randomness uses system entropy by default; seeded mode is documented as test / demo only.
- [ ] New methods cite traditional sources or clearly mark themselves as approximate with a warning.
- [ ] JSON output includes enough metadata to audit the method (e.g. RNG mode, seed, inputs).
- [ ] Safety boundaries from `shared/safety-policy.md` are respected (no medical / legal / financial / crisis advice).

## Quality checklist

- [ ] `python3 -m unittest discover -s tests` passes locally.
- [ ] New behaviour is covered by unit tests.
- [ ] Schemas under `schemas/` are updated (or added) for any new script output.
- [ ] User-facing docs (`README.md`, `README.zh-CN.md`, `README.ja.md`, `docs/`) are updated where relevant.
- [ ] `RELEASE_NOTES.md` has a draft entry for the next release.
