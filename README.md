# AI Divination Skills

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

Direct, practical divination skills for AI agents.

`ai-divination-skills` is an open-source skill collection for tarot, I Ching, Xiao Liu Ren, and other symbolic systems. It is designed for agent workflows where the random draw or cast is produced by a local script, and the AI agent interprets the result with clear safety boundaries.

This project treats divination as symbolic reasoning and reflection, not deterministic prediction.

## Methodological Rigor

The core rule is simple: scripts or user-provided physical casts generate the divination result; AI interprets that result and does not generate the divination result.

This is not scientific proof of divination efficacy. It is a stricter workflow for symbolic reasoning:

- real readings use system randomness by default
- seeded mode is only for tests and reproducible demos
- traditional methods and limitations are documented per skill
- outputs include enough JSON metadata to audit the method
- approximate modes emit warnings instead of pretending to be traditional

## Multilingual Docs

The project includes a GitHub Pages-ready docs site with in-page language switching:

- [English](https://sapuyou45-bit.github.io/ai-divination-skills/?lang=en)
- [简体中文](https://sapuyou45-bit.github.io/ai-divination-skills/?lang=zh)
- [日本語](https://sapuyou45-bit.github.io/ai-divination-skills/?lang=ja)

Local preview:

```bash
python3 -m http.server 8000 -d docs
```

Published site:

```text
https://sapuyou45-bit.github.io/ai-divination-skills/
```

## Included Skills

| Skill | What it does | Script |
|---|---|---|
| `tarot` | Draws tarot cards for reflection, decisions, creative blocks, and project reframing. | `skills/tarot/scripts/draw.py` |
| `iching` | Casts six-line I Ching hexagrams with primary and resulting hexagrams. | `skills/iching/scripts/cast.py` |
| `xiaoliuren` | Casts Xiao Liu Ren from lunar-style numbers or a Gregorian time fallback. | `skills/xiaoliuren/scripts/cast.py` |

## Why This Exists

Most AI divination prompts let the model invent the result. This project separates the two jobs:

1. Scripts produce the card draw, hexagram, or position.
2. The AI agent interprets the generated result.

That makes readings easier to test, reproduce, audit, and reuse across agents.

## Quick Start

Run any script directly:

```bash
python3 skills/tarot/scripts/draw.py --deck major --spread three-card --reversals
python3 skills/iching/scripts/cast.py --method coins
python3 skills/iching/scripts/cast.py --method yarrow
python3 skills/xiaoliuren/scripts/cast.py --method numbers --month 3 --day 12 --hour 7
```

Use a seed for reproducible demos:

```bash
python3 skills/tarot/scripts/draw.py --spread decision --seed demo
python3 skills/iching/scripts/cast.py --method yarrow --seed demo
```

All scripts output JSON.

## Install as Agent Skills

Copy the skill folders you want into your agent's skill directory:

```bash
cp -R skills/tarot ~/.codex/skills/tarot
cp -R skills/iching ~/.codex/skills/iching
cp -R skills/xiaoliuren ~/.codex/skills/xiaoliuren
```

Each skill is self-contained:

```text
skills/name/
  SKILL.md
  agents/openai.yaml
  scripts/
  references/
```

Install individual folders, not the entire repository, when you only want one skill.

## Agent Behavior

Each skill instructs the agent to:

- generate or accept a concrete draw/cast result
- read concise reference material only when needed
- interpret with the shared response contract
- avoid certainty, fatalism, and professional advice

Shared guidance lives in:

- `shared/methodology.md`
- `shared/response-contract.md`
- `shared/randomness-protocol.md`
- `shared/safety-policy.md`
- `shared/interpretation-style.md`

## Examples

- `examples/tarot-decision.md`
- `examples/iching-strategy.md`
- `examples/xiaoliuren-daily.md`

## Safety Boundaries

These skills are not for medical, legal, financial, or crisis guidance.

Good readings should:

- frame the result as symbolic reflection
- connect claims to the generated result
- preserve user agency
- offer small, reversible next steps
- state uncertainty clearly

See `ETHICS.md` for the full project stance.

## Development

No runtime dependencies are required beyond Python 3.

Run tests:

```bash
python3 -m unittest discover -s tests
```

Current coverage checks:

- tarot spread output
- I Ching cast structure and manual lines
- Xiao Liu Ren number and time fallback behavior

## Roadmap

Near-term:

- Add richer reference material for each MVP skill.
- Add more example readings.
- Add a simple installer script.
- Add optional Chinese-language docs.

Later:

- `meihua`
- `liuyao`
- `runes`
- `numerology`
- `astrology`

## License

MIT
