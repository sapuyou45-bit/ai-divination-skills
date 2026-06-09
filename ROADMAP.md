# Roadmap

Live, opinion-driven list of where this project is going next. Each item is tracked as a GitHub issue — pick one, leave a comment, and open a PR.

## Now (v0.5.x — operations)

- [x] Community templates, dependabot, release workflow, social preview (v0.5.1)
- [x] Multi-agent adapters: `claude.yaml`, `gemini.yaml`, `cursor.mdc` for tarot / I Ching / Xiao Liu Ren (v0.5.2 — issue [#12](https://github.com/sapuyou45-bit/ai-divination-skills/issues/12))
- [ ] Optional PyPI publish from the release workflow (waits on `PYPI_API_TOKEN` secret — see `docs/maintainer/release-and-pypi.md`)
- [ ] Custom social preview image uploaded (manual one-time step — see `docs/maintainer/social-preview.md`)

## Next (v0.6 — depth)

- [ ] **Bazi (四柱八字)** — new deterministic divination skill, issue [#11](https://github.com/sapuyou45-bit/ai-divination-skills/issues/11)
- [ ] **Tarot deepening** — Celtic Cross, Relationship Cross, Year Wheel spreads; reversal-semantics layer
- [ ] **MCP server** wrapping the three skills so Claude Desktop / Codex can mount them in one config line — issue [#13](https://github.com/sapuyou45-bit/ai-divination-skills/issues/13)

## Later (v0.7+)

- [ ] Web playground (static, runs `pyodide`-shipped CLI in the browser)
- [ ] Additional language READMEs (Spanish, Portuguese)
- [ ] Optional "lots" / "runes" / "sortes" skill family with shared schema

## Non-goals

- Generating divination results inside the model. Scripts (or user-provided physical casts) generate the result. The agent only interprets.
- Medical, legal, financial, emergency, or crisis advice. The shared safety policy refuses those.
- Bundling copyrighted deck art, card text, or long-form traditional source material.

## How to influence the roadmap

- Comment on an open issue with a use case or a methodology source.
- Open a new issue with the "🔮 New Divination Skill Proposal" template.
- Open a discussion in the [Ideas](https://github.com/sapuyou45-bit/ai-divination-skills/discussions/categories/ideas) category.
