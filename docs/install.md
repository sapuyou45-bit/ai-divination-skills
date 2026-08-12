# Install AI Divination Skills

## For Humans

Paste this into your AI agent:

```text
Install AI Divination Skills for this agent: https://raw.githubusercontent.com/sapuyou45-bit/oraclebone/main/docs/install.md
```

中文：

```text
请帮我安装 AI Divination Skills：https://raw.githubusercontent.com/sapuyou45-bit/oraclebone/main/docs/install.md
```

The agent should read this file, choose the right skill directory, install the three skill folders, and verify the scripts.

## For AI Agents

You are installing filesystem-based skills for the current agent. These skills are intentionally simple: copy the skill folders, then call their local scripts when the user asks for a reading.

### Boundaries

- Do not use `sudo`.
- Do not modify shell profiles such as `.bashrc`, `.zshrc`, or `.profile`.
- Do not install Python packages during the base skill install.
- Do not upload files or send data to external services.
- Do not write outside the selected skills directory except for a temporary clone/download directory.
- Do not overwrite unrelated user files.
- If the target skill directory is unclear, ask the user before installing.

### Target directory

Prefer these directories in order:

1. `$AI_SKILLS_DIR` if it is set.
2. `~/.claude/skills` for Claude-style local agents.
3. `~/.codex/skills` for Codex-style local agents.
4. A user-provided custom skill directory.

The default installer target is:

```text
~/.claude/skills
```

### One-command install

```bash
curl -fsSL https://raw.githubusercontent.com/sapuyou45-bit/oraclebone/main/install.sh | bash
```

### Install to a custom skill directory

```bash
export AI_SKILLS_DIR="$HOME/.codex/skills"
curl -fsSL https://raw.githubusercontent.com/sapuyou45-bit/oraclebone/main/install.sh | bash
```

or, from a local checkout:

```bash
AI_SKILLS_DIR="$HOME/.claude/skills" bash install.sh
```

### Transparent manual install

Use this when the user does not want `curl | bash`:

```bash
git clone https://github.com/sapuyou45-bit/oraclebone.git
mkdir -p "$HOME/.claude/skills"
cp -R oraclebone/skills/tarot "$HOME/.claude/skills/tarot"
cp -R oraclebone/skills/iching "$HOME/.claude/skills/iching"
cp -R oraclebone/skills/xiaoliuren "$HOME/.claude/skills/xiaoliuren"
```

### Dry run

Preview the target directory and skill list without changing files:

```bash
curl -fsSL https://raw.githubusercontent.com/sapuyou45-bit/oraclebone/main/install.sh | bash -s -- --dry-run
```

### Update

To update an existing install, run the same installer again. Existing `tarot`, `iching`, and `xiaoliuren` folders are backed up under `<skills-dir>/.ai-divination-backups/<timestamp>/` before replacement.

### Verify

After installing to the default Claude-style directory, run:

```bash
python3 "$HOME/.claude/skills/tarot/scripts/draw.py" --deck major --spread single --seed demo
python3 "$HOME/.claude/skills/iching/scripts/cast.py" --method coins --seed demo
python3 "$HOME/.claude/skills/xiaoliuren/scripts/cast.py" --method numbers --month 3 --day 12 --hour 7
```

If using a custom directory, replace `$HOME/.claude/skills` with the selected directory.

## Installed Skills

| Skill | Trigger examples | Script |
| --- | --- | --- |
| `tarot` | tarot, card pull, card reading, 塔罗 | `scripts/draw.py` |
| `iching` | I Ching, Yi Jing, 易经, 周易, hexagram | `scripts/cast.py` |
| `xiaoliuren` | Xiao Liu Ren, 小六壬, quick timing reflection | `scripts/cast.py` |

## After Install: Invocation Protocol

When the user asks for a reading:

1. Select the matching installed skill by its `SKILL.md` description.
2. Read the selected skill's `SKILL.md`.
3. Run the skill script from inside that skill directory unless the user provided a physical draw/cast result.
4. Use the JSON output as the only divination result.
5. Interpret symbolically and practically.
6. Do not claim deterministic prediction.
7. Do not use readings as medical, legal, financial, emergency, or crisis advice.

Do not invent cards, hexagrams, line values, or Xiao Liu Ren positions. The script or the user's physical input provides the result; the AI only interprets it.
