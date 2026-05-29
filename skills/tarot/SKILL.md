---
name: tarot
description: Use when the user asks for tarot, a card pull, a card reading, symbolic reframing, decision reflection, creative blocks, project reflection, or interpretation of a user-provided tarot draw.
---

# Tarot

Tarot is used here as a symbolic reflection tool, not a prediction engine.

## When to Use

- The user asks for tarot, a card pull, or a card reading.
- The user wants symbolic reflection for a decision, creative block, project review, or personal question.
- The user provides physical tarot cards and wants an interpretation.

## When Not to Use

- The request needs medical, legal, financial, emergency, or crisis advice.
- The user wants a deterministic prediction or certainty about future events.
- The user asks the agent to choose cards without a script or physical draw.

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
