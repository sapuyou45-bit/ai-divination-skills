---
name: iching
description: Cast and interpret I Ching hexagrams for AI agent readings, symbolic decision reflection, change analysis, or when the user asks for I Ching, Yi Jing, Zhouyi, hexagrams, coins, or 易经/周易.
---

# I Ching

I Ching readings analyze change, timing, tension, and response. They are not deterministic commands.

## Workflow

1. Clarify the question if it is vague or high-stakes.
2. Run `scripts/cast.py` unless the user provides six line values.
3. Read `references/casting-methods.md` when the casting method matters.
4. Read `references/sources.md` when method rigor or adjacent systems matter.
5. Read `references/hexagrams.md` for the primary and resulting hexagram.
6. Interpret using the shared response contract:
   - Result
   - Symbolic Reading
   - Situation Mapping
   - Hidden Variables
   - Actionable Guidance
   - Boundaries

## Commands

```bash
python3 scripts/cast.py --method coins
python3 scripts/cast.py --method yarrow
python3 scripts/cast.py --method manual --lines 6,7,8,9,7,8
```

Line order is bottom-to-top.

## Rules

- Do not invent line values or hexagrams.
- For real readings, prefer `coins`, `yarrow`, or `manual`; `random` is only a compatibility alias.
- Do not recast to get a more convenient answer.
- Treat changing lines as areas of active transition, not guaranteed events.
- If the question is medical, legal, financial, or crisis-related, switch to reflective support and recommend qualified help.
