---
name: tarot
description: Draw and interpret tarot cards for AI agent readings, symbolic reframing, decisions, creative blocks, project reflection, or when the user asks for tarot, a card pull, or a card reading.
---

# Tarot

Tarot is used here as a symbolic reflection tool, not a prediction engine.

## Workflow

1. Clarify the user's question if needed.
2. Choose a spread from `references/spreads.md`.
3. Run `scripts/draw.py` unless the user provides a physical draw.
4. Read `references/interpretation-template.md` before writing the interpretation.
5. Read `references/sources.md` when method or licensing rigor matters.
6. Read `references/cards.md` for concise card and suit meanings.
7. Interpret using the shared response contract:
   - Result
   - Symbolic Reading
   - Situation Mapping
   - Hidden Variables
   - Actionable Guidance
   - Boundaries

## Commands

```bash
python3 scripts/draw.py --deck major --spread single
python3 scripts/draw.py --deck major --spread three-card --reversals
python3 scripts/draw.py --deck full --spread decision --reversals
python3 scripts/draw.py --spread project --seed demo
```

Use `--seed` only for tests and reproducible demos, not real readings.

## Rules

- Do not choose cards yourself.
- Do not use seeded mode for real readings unless the user explicitly wants a reproducible demo.
- Do not redraw because the first result is inconvenient.
- Do not claim certainty about future events.
- Do not answer medical, legal, financial, or crisis questions as a tarot verdict.
- If script execution is unavailable, ask the user to provide a physical draw or say the draw cannot be performed.
