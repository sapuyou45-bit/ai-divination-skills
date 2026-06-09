# Release Notes

## v0.7.0 - Bazi (Four Pillars) + Client Configs

This release adds the bazi (八字 / Four Pillars) divination skill and ships ready-to-paste MCP client configs for the four most common hosts.

### What's New

- **Bazi skill** — `ai-divination bazi --datetime <ISO 8601>` returns the four pillars (年/月/日/时), each with 天干 + 地支, element, polarity, and 纳音, plus the day master and a Five Elements tally. The model never invents a pillar — it interprets the JSON.
- **`bazi.cast` MCP tool** — drop-in for Claude Desktop, Codex, Cursor, Continue, or any MCP host. Five tools total now.
- **Client setup docs** — `docs/clients/{claude-desktop,codex,cursor,continue}.md` with one-click JSON snippets, install steps, and example calls for each of the five tools.
- **Demo image** — README now opens with a terminal-style demo so visitors see what the tools do at a glance.

### Why

Bazi was the last classical system on the v0.x roadmap. With the per-client config pages, "how do I actually use this in Claude Desktop / Codex?" now has a one-screen answer in every supported language.

### Notes

- The bazi skill needs `lunar-python`; install with `pip install 'ai-divination-skills[lunar]'`.
- Without an exact birth hour the hour pillar is unreliable; the skill surfaces this limitation in its template and refuses to fabricate one.
- Closes #11.

## v0.6.2 - MCP Registry listing

This release prepares the project for publication on the official MCP Server Registry (https://registry.modelcontextprotocol.io/).

### What's New

- `server.json` describing the package as a stdio MCP server backed by PyPI.
- `mcp-name: io.github.sapuyou45-bit/ai-divination-skills` ownership token added to README.md, README.zh-CN.md, README.ja.md so PyPI mirrors the marker and the registry can verify ownership automatically.

### Why

Once published, MCP clients (Claude Desktop, Codex, Cursor, etc.) can discover and install this server through the official registry without scraping awesome lists.

## v0.6.1 - Discovery and SEO

This release helps people who don't already know about the project actually find it.

### What's New

- README badges for PyPI version and monthly downloads (all three languages).
- README.zh-CN.md and README.ja.md now also have the "Use it from Claude Desktop / Codex / any MCP host" section.
- GitHub repository description updated to lead with "MCP server + Python CLI" so MCP search results pick it up.
- GitHub repository topics expanded with `mcp`, `mcp-server`, `model-context-protocol`, `claude`, `claude-desktop`, `anthropic`.
- README and docs site install snippets now lead with `pip install ai-divination-skills` instead of `pip install .`.

## v0.6.0 - MCP server for Claude Desktop, Codex, and other MCP hosts

This release adds first-party support for the [Model Context Protocol](https://modelcontextprotocol.io/). Any MCP-aware host can mount `ai-divination-skills` with one config line and get four audited divination tools.

### What's New

- **`ai-divination-mcp` console script** — zero-dependency JSON-RPC 2.0 server over stdio.
- **4 MCP tools** — `tarot.draw`, `iching.cast`, `xiaoliuren.cast`, `interpretation_template`. Each tool routes through the audited local script; the host never invents the draw.
- **Claude Desktop snippet** — paste 4 lines into `claude_desktop_config.json`, restart, ask "draw three tarot cards for my decision".
- **Test coverage** — 12 new tests (61 total) for protocol handshake, tools/list, tools/call for every tool, JSON-RPC error mapping, invalid-JSON recovery, and the full stdio loop.
- **Closes issue #13**.

### Install

```bash
pip install ai-divination-skills
```

Then in `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{ "mcpServers": { "divination": { "command": "ai-divination-mcp" } } }
```

Restart Claude Desktop.

## v0.5.4 - Final Ops Hardening

This release closes the remaining operational gaps that don't require user credentials.

### What's New

- **Safety / Ethics Concern issue template** — structured form for non-sensitive safety reports, with a header directing sensitive ones to the private vulnerability flow.
- **Copilot instructions** — `.github/copilot-instructions.md` tells AI tools the project's non-negotiable rules (never invent draws, system entropy by default, no telemetry, safety boundaries, schema + test expectations).
- **Dependabot grouping** — pip and Actions each consolidate into a single monthly PR.
- **Repo governance** — main now permits squash-merge only, auto-merge on, update-branch on, delete-branch-on-merge on; Wiki and Projects turned off for a solo maintainer; Dependabot security updates and automated security fixes enabled.

## v0.5.3 - Security Scanning, Link Hygiene, Docs Polish

This release does not change skill logic. It adds two new CI workflows and finishes the multi-host adapter story in user-facing docs.

### What's New

- **CodeQL** — static analysis on every push, PR, and weekly schedule. Findings land in the Security tab.
- **Link check** — `lychee` runs on every markdown change and weekly to catch dead links across README, docs site, and reference files.
- **Docs / Translation issue template** — explicit form for typos, missing examples, broken links, and translation gaps.
- **Per-host adapters surfaced in README** — table covering OpenAI / Claude / Gemini / Cursor adapters with how each is invoked.
- **Community section** in the English README pointing at Releases, Roadmap, Discussions, `good first issue` / `new-skill` labels, and the security policy.
- **Status badges** now appear in the Simplified Chinese and Japanese READMEs as well.

## v0.5.2 - Multi-agent Adapters and Branch Protection

This release ships the skills to more agent runtimes and tightens the merge gate on `main`.

### What's New

- **Claude / Gemini / Cursor adapters** — each of `tarot`, `iching`, `xiaoliuren` now ships `agents/claude.yaml`, `agents/gemini.yaml`, and `agents/cursor.mdc` in addition to the existing OpenAI metadata. Every adapter routes through the same audited `ai-divination <skill>` CLI, so no host can let the model invent a draw.
- **ROADMAP.md** — public list of what is in flight, what is next, and the explicit non-goals.
- **Branch protection on main** — linear history, no force-pushes, no deletions, required conversation resolution, four-version CI gate (`unittest (3.9|3.10|3.11|3.12)`).
- **Test coverage** — `tests/test_agent_adapters.py` adds 5 tests (49 total) that check adapter presence, CLI routing, frontmatter, and a "no invented draws" lint.

## v0.5.1 - Community Operations

This release does not change skill logic. It makes the repo easier to contribute to and ship from.

### What's New

- **Issue and PR templates**: bug report, feature request, new-skill proposal forms; PR template enforces the `shared/methodology.md` checklist.
- **Community files**: `CODEOWNERS`, `FUNDING.yml`, and `dependabot.yml` (pip + GitHub Actions, monthly).
- **Release workflow**: tagged pushes (`v*`) build sdist + wheel and attach them to an auto-generated GitHub Release.
- **CI matrix**: tests now run on Python 3.9 / 3.10 / 3.11 / 3.12 with a CLI smoke test for all three skills.
- **Social preview**: 1280×640 image checked in under `.github/social-preview-1280x640.png`.
- **Discussions enabled**: linked from the issue template chooser.

## v0.5.0 - Skill Spec Hardening

This release makes the repository stronger as an Agent skill collection, not just as a Python package.

### What's New

- **Standalone skill scripts**: copied single-skill folders now run without requiring the top-level Python package.
- **Skill frontmatter hardening**: descriptions now use `Use when...` trigger wording and avoid workflow summaries.
- **Usage boundaries**: every skill has explicit `When to Use` and `When Not to Use` sections.
- **OpenAI metadata polish**: every skill now has brand color plus small and large SVG icons.
- **Skill contract tests**: coverage checks frontmatter, referenced files, metadata assets, and single-folder script execution.
- **Dev extra**: `.[dev]` includes build, twine, and PyYAML for package and skill validation work.

## v0.4.0 - Installable Package Runtime

This release makes the CLI work from a normal package install, not only from an editable checkout.

### What's New

- **Packaged runtime**: tarot, I Ching, and Xiao Liu Ren logic now lives in importable `ai_divination_skills` modules.
- **Package-only CLI**: `ai-divination` no longer depends on top-level `skills/` files being present after installation.
- **Python API**: callers can import `draw`, `cast`, and `cast_numbers` directly.
- **Packaged templates**: interpretation templates are bundled inside the package for installed CLI use.
- **Compatibility wrappers**: existing `skills/*/scripts/*.py` paths still work and delegate to the package modules.
- **Install tests**: coverage checks package-only CLI execution and importable APIs.

## v0.3.0 - Unified CLI and Agent Interpretation Templates

This release makes the toolkit easier for agents and humans to call consistently.

### What's New

- **Unified CLI**: `ai-divination tarot`, `ai-divination iching`, and `ai-divination xiaoliuren` route to the existing audited scripts.
- **Install entry point**: `pip install -e .` exposes the `ai-divination` command for local development and agent workflows.
- **Agent templates**: `ai-divination template tarot` prints the shared interpretation protocol plus the skill-specific template.
- **Interpretation boundary**: shared and per-skill templates explicitly state that AI interprets generated results and must not invent, redraw, or recast.
- **Docs and tests**: README examples and unit tests cover the CLI and interpretation templates.

## v0.2.0 - Traditional Rigor and Auditable Randomness

This release separates the divination process from AI interpretation more strictly.

### What's New

- **Methodology**: project-level rules for randomness, traditional sources, reproducibility, and limits.
- **Tarot**: explicit Fisher-Yates shuffle with deck size, draw count, drawn indices, and RNG mode metadata.
- **I Ching**: auditable three-coin lines, digital yarrow probability mode, and a compatibility warning for `random`.
- **Xiao Liu Ren**: optional `lunar-time` mode via `lunar_python`, stronger Gregorian fallback warning, and leap-month rejection.
- **Schemas**: JSON schema files for all three script outputs.
- **CI**: GitHub Actions runs the unittest suite on push and pull requests.

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
