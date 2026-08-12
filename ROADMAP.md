# Roadmap

Live, opinion-driven list of where this project is going next. Each item is tracked as a GitHub issue — pick one, leave a comment, and open a PR.

## Done recently

- [x] Community templates, dependabot, release workflow, social preview (v0.5.1)
- [x] Multi-agent adapters: `claude.yaml`, `gemini.yaml`, `cursor.mdc` (v0.5.2 — issue [#12](https://github.com/sapuyou45-bit/ai-divination-skills/issues/12))
- [x] **MCP server** wrapping the skills (v0.6.0, closed issue [#13](https://github.com/sapuyou45-bit/ai-divination-skills/issues/13))
- [x] MCP Registry publish (`server.json` + `mcp-name` token, v0.6.2)
- [x] **Bazi (四柱八字)** skill + per-client config docs (v0.7.0 — issue [#11](https://github.com/sapuyou45-bit/ai-divination-skills/issues/11))
- [x] Xiao Liu Ren traditional-count fix + MCP 2025-06-18 upgrade (spec-compliant tool names, `outputSchema` / `structuredContent`) (v0.7.1)

## Now (v0.8 — data layer)

- [ ] **Card/hexagram meaning data in JSON output** — tarot upright/reversed keywords and I Ching judgment/line texts, so the model interprets audited data instead of memory
- [ ] **Bazi timezone + true solar time** — `timezone` parameter and optional longitude correction; dayun (大运) cycles
- [ ] MCP `resources` / `prompts` — expose `shared/*.md` and interpretation templates as protocol-native capabilities
- [ ] **Tarot deepening** — Celtic Cross, Relationship Cross, Year Wheel spreads; reversal-semantics layer
- [ ] Custom social preview image uploaded (manual one-time step — see `docs/maintainer/social-preview.md`)

## Next (v0.9 — transport & reach)

- [ ] Streamable-HTTP transport + a hosted public endpoint (zero-install clients)
- [ ] Optional QRNG backend (ANU / drand) alongside local `SystemRandom` — audited randomness, upgraded
- [ ] English-community distribution: awesome-list PRs, dev.to / HN / Reddit write-ups on the "audited randomness" approach

## Later (v1.0+)

- [ ] Web playground (static, runs `pyodide`-shipped CLI in the browser)
- [ ] Additional language READMEs (Spanish, Portuguese)
- [ ] Optional "lots" / "runes" / "sortes" skill family with shared schema
- [ ] New systems by community vote (Zi Wei Dou Shu, Liu Yao) — one at a time

## Non-goals

- Generating divination results inside the model. Scripts (or user-provided physical casts) generate the result. The agent only interprets.
- Medical, legal, financial, emergency, or crisis advice. The shared safety policy refuses those.
- Bundling copyrighted deck art, card text, or long-form traditional source material.

## How to influence the roadmap

- Comment on an open issue with a use case or a methodology source.
- Open a new issue with the "🔮 New Divination Skill Proposal" template.
- Open a discussion in the [Ideas](https://github.com/sapuyou45-bit/ai-divination-skills/discussions/categories/ideas) category.
