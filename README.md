# AI Divination Skills

Practical divination skills for AI agents: tarot, I Ching, Xiao Liu Ren, and more.

This project treats divination systems as symbolic reasoning and reflection tools, not deterministic prediction engines. The scripts produce the draw or cast. The AI agent interprets the result with clear boundaries.

## MVP Skills

- `tarot`: card draws for reflection, decisions, creative blocks, and project reframing.
- `iching`: six-line I Ching casts with primary and resulting hexagrams.
- `xiaoliuren`: lightweight Xiao Liu Ren casts from lunar numbers or a Gregorian time fallback.

## Design Principles

- Direct skill names. Users should know what a skill does from its folder name.
- Randomness is externalized. Agents do not choose cards, lines, or positions by intuition.
- JSON first. Scripts emit machine-readable data for reliable agent workflows.
- Offline by default. The MVP has no network calls and uses only Python standard library.
- Bounded interpretation. No medical, legal, financial, or crisis advice.
- Modular structure. Each system can be installed and used independently.

## Repository Layout

```text
skills/
  tarot/
    SKILL.md
    scripts/draw.py
    references/
  iching/
    SKILL.md
    scripts/cast.py
    references/
  xiaoliuren/
    SKILL.md
    scripts/cast.py
    references/
shared/
  response-contract.md
  safety-policy.md
  randomness-protocol.md
  interpretation-style.md
examples/
tests/
```

## Quick Try

```bash
python3 skills/tarot/scripts/draw.py --deck major --spread three-card --reversals
python3 skills/iching/scripts/cast.py --method coins
python3 skills/xiaoliuren/scripts/cast.py --method numbers --month 3 --day 12 --hour 7
```

For reproducible demos and tests, pass `--seed` where supported:

```bash
python3 skills/tarot/scripts/draw.py --spread decision --seed demo
python3 skills/iching/scripts/cast.py --method random --seed demo
```

## Install as Skills

Copy the skill folders you want into your agent's skill directory, for example:

```bash
cp -R skills/tarot ~/.codex/skills/tarot
cp -R skills/iching ~/.codex/skills/iching
cp -R skills/xiaoliuren ~/.codex/skills/xiaoliuren
```

Use only the individual skill folder when installing a single skill. The root docs and shared protocol are for maintainers and contributors.

## Development

Run the standard-library test suite:

```bash
python3 -m unittest discover -s tests
```

## Status

This is an initial scaffold. The first goal is a small, reliable core rather than a large collection of half-finished systems.
