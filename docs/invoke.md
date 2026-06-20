# Invoke AI Divination Skills

This guide tells AI agents how to use the installed skills after setup.

## Core Rule

Do not invent divination results. A script or user-provided physical draw/cast produces the result; the AI interprets that concrete result.

## General Invocation Protocol

1. Select the matching installed skill by its `SKILL.md` description.
2. Read the selected skill's `SKILL.md`.
3. Run the skill script from inside the skill directory unless the user already provided a physical result.
4. Treat the script's JSON output as the only divination result.
5. Read the skill's interpretation template and concise references only when needed.
6. Interpret symbolically and practically.
7. Preserve user agency and avoid deterministic prediction.
8. Do not give medical, legal, financial, emergency, or crisis advice as a reading.

## Tarot

Use when the user asks for tarot, a card pull, symbolic reframing, decision reflection, creative blocks, or project reflection.

Typical command from inside the installed `tarot` skill directory:

```bash
python3 scripts/draw.py --deck major --spread single
```

Other useful commands:

```bash
python3 scripts/draw.py --deck major --spread three-card --reversals
python3 scripts/draw.py --deck full --spread decision --reversals
python3 scripts/draw.py --spread project --seed demo
```

Use `--seed` only for tests or reproducible demos, not real readings unless the user explicitly asks for a reproducible demo.

## I Ching

Use when the user asks for I Ching, Yi Jing, Zhouyi, 易经, 周易, hexagrams, coin casting, yarrow-style casting, change analysis, or manual line interpretation.

Typical command from inside the installed `iching` skill directory:

```bash
python3 scripts/cast.py --method coins
```

Other useful commands:

```bash
python3 scripts/cast.py --method yarrow
python3 scripts/cast.py --method manual --lines 6,7,8,9,7,8
```

Line order is bottom-to-top. Do not invent line values or recast for a nicer answer.

## Xiao Liu Ren

Use when the user asks for Xiao Liu Ren, 小六壬, quick symbolic timing reflection, daily guidance, or lunar month/day/hour inputs.

Prefer user-provided lunar-style numbers:

```bash
python3 scripts/cast.py --method numbers --month 3 --day 12 --hour 7
```

If `lunar_python` is installed and the user provides a datetime:

```bash
python3 scripts/cast.py --method lunar-time --datetime 2026-05-29T14:30:00
```

For quick fallback only, with disclosure:

```bash
python3 scripts/cast.py --method time
```

Do not pretend Gregorian fallback is a traditional lunar calculation. Keep readings short and practical.

## Response Shape

Use the shared response contract unless the user asks for a shorter answer:

- Result
- Symbolic Reading
- Situation Mapping
- Hidden Variables
- Actionable Guidance
- Boundaries

If the user asks for a very short reading, compress the same structure into a few concise paragraphs.
