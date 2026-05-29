---
name: xiaoliuren
description: Use when the user asks for Xiao Liu Ren, 小六壬, xiaoliuren, quick symbolic timing reflection, daily guidance, folk-style yes/no reflection, or interpretation from lunar month/day/hour inputs.
---

# Xiao Liu Ren

Xiao Liu Ren is used here as a lightweight symbolic timing tool. It should not be framed as certainty.

## When to Use

- The user asks for Xiao Liu Ren, 小六壬, or xiaoliuren.
- The user wants lightweight symbolic timing reflection or quick daily guidance.
- The user provides lunar month, lunar day, and Chinese hour index.

## When Not to Use

- The request needs medical, legal, financial, emergency, or crisis advice.
- The user expects a traditional lunar cast but cannot provide lunar inputs and `lunar_python` is unavailable.
- The user asks the agent to invent lunar dates, hour branches, or positions.

## Workflow

1. Prefer user-provided lunar month, lunar day, and Chinese hour index when available.
2. Use `--method lunar-time` only when `lunar_python` is installed and the user gives a datetime.
3. If the user asks for a quick current-time cast without lunar support, run the Gregorian fallback and disclose its warning.
4. Read `references/interpretation-template.md` before writing the interpretation.
5. Read `references/sources.md` when method rigor matters.
6. Read `references/positions.md` for the resulting position.
7. Read `references/lunar-time.md` if the user asks about inputs or hour conversion.
8. Interpret using the shared response contract:
   - Result
   - Symbolic Reading
   - Situation Mapping
   - Hidden Variables
   - Actionable Guidance
   - Boundaries

## Commands

```bash
python3 scripts/cast.py --method numbers --month 3 --day 12 --hour 7
python3 scripts/cast.py --method lunar-time --datetime 2026-05-29T14:30:00
python3 scripts/cast.py --method time
python3 scripts/cast.py --method time --datetime 2026-05-29T14:30:00
```

## Rules

- Do not pretend Gregorian fallback is a traditional lunar calculation.
- Reject leap lunar months unless the user provides explicit `numbers` input.
- Do not invent lunar dates if the user needs traditional accuracy.
- Keep readings short and practical.
- Do not use the result to override professional advice or user agency.
