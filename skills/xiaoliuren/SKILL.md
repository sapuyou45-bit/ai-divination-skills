---
name: xiaoliuren
description: Cast Xiao Liu Ren for lightweight AI agent divination, quick timing reflection, daily guidance, yes/no-style folk questions, or when the user asks for 小六壬 or xiaoliuren.
---

# Xiao Liu Ren

Xiao Liu Ren is used here as a lightweight symbolic timing tool. It should not be framed as certainty.

## Workflow

1. Prefer user-provided lunar month, lunar day, and Chinese hour index when available.
2. If the user asks for a quick current-time cast, run the time fallback and disclose its calendar note.
3. Read `references/positions.md` for the resulting position.
4. Read `references/lunar-time.md` if the user asks about inputs or hour conversion.
5. Interpret using the shared response contract:
   - Result
   - Symbolic Reading
   - Situation Mapping
   - Hidden Variables
   - Actionable Guidance
   - Boundaries

## Commands

```bash
python3 scripts/cast.py --method numbers --month 3 --day 12 --hour 7
python3 scripts/cast.py --method time
python3 scripts/cast.py --method time --datetime 2026-05-29T14:30:00
```

## Rules

- Do not pretend Gregorian fallback is a traditional lunar calculation.
- Do not invent lunar dates if the user needs traditional accuracy.
- Keep readings short and practical.
- Do not use the result to override professional advice or user agency.
