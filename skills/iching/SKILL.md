---
name: iching
description: Use when the user asks for I Ching, Yi Jing, Zhouyi, 易经, 周易, hexagrams, coin casting, yarrow-style casting, change analysis, or interpretation of user-provided line values.
---

# I Ching

I Ching readings analyze change, timing, tension, and response. They are not deterministic commands.

## When to Use

- The user asks for I Ching, Yi Jing, Zhouyi, 易经, 周易, hexagrams, coins, or yarrow.
- The user wants symbolic reflection on timing, change, tension, strategy, or response.
- The user provides six bottom-to-top line values and wants an interpretation.

## When Not to Use

- The request needs medical, legal, financial, emergency, or crisis advice.
- The user wants a guaranteed prediction or deterministic command.
- The user asks the agent to invent line values or recast for a nicer result.

## Workflow

1. Clarify the question if it is vague or high-stakes.
2. Run `scripts/cast.py` unless the user provides six line values.
3. Read `references/casting-methods.md` when the casting method matters.
4. Read `references/interpretation-template.md` before writing the interpretation.
5. Read `references/sources.md` when method rigor or adjacent systems matter.
6. Read `references/hexagrams.md` for the primary and resulting hexagram.
7. Interpret using the shared response contract:
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
