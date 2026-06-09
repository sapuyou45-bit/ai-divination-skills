---
name: bazi
description: Use when the user asks for bazi, 八字, Four Pillars, BaZi, Chinese astrology birth chart, 生辰八字, 命盘, day master, or interpretation from a Gregorian birth date and time.
---

# Bazi (八字 / Four Pillars)

Bazi maps a Gregorian birth instant to four pillars (年柱/月柱/日柱/时柱) of Heavenly Stem + Earthly Branch, then derives Five Elements (五行), NaYin (纳音), and the Chinese zodiac (生肖). It is a symbolic life-pattern lens, not a deterministic forecast.

## When to Use

- The user asks for bazi, 八字, Four Pillars, BaZi, 生辰八字, 命盘, or day master analysis.
- The user provides a Gregorian birth date **and** an exact birth time.
- The user wants symbolic reflection on personality patterns, element balance, or life themes.

## When Not to Use

- The request needs medical, legal, financial, emergency, or crisis advice.
- The user wants a guaranteed prediction or precise life forecast.
- The user cannot supply an exact birth hour — say so and refuse to overstate precision.
- The user asks the agent to invent pillars, stems, branches, wuxing, or shen sha.

## Workflow

1. Confirm the user has a Gregorian birth date and an exact birth time (hour matters).
2. Run `scripts/cast.py --datetime <ISO 8601>` to produce the chart JSON.
3. Read `references/interpretation-template.md` before writing the interpretation.
4. Read `references/pillars.md` for stem/branch/element reference.
5. Read `references/sources.md` when method rigor or engine limits matter.
6. Interpret using the shared response contract:
   - Result
   - Symbolic Reading
   - Situation Mapping
   - Hidden Variables
   - Actionable Guidance
   - Boundaries

## Commands

```bash
python3 scripts/cast.py --datetime 1990-05-20T14:30:00
python3 scripts/cast.py --datetime 2000-01-01T00:00:00
```

## Rules

- Do not invent stems, branches, wuxing, or NaYin. Only cite values returned by the script.
- Do not pretend to read da yun (大运), liu nian (流年), or shen sha (神煞) — they are not in the output.
- Do not skip the birth-hour requirement; an unknown hour invalidates the hour pillar.
- Keep readings practical and grounded; do not override professional advice or the user's agency.
