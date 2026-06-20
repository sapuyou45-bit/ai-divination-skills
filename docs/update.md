# Update AI Divination Skills

## For Humans

Paste this into your AI agent:

```text
Update AI Divination Skills for this agent: https://raw.githubusercontent.com/sapuyou45-bit/ai-divination-skills/main/docs/update.md
```

中文：

```text
请帮我更新 AI Divination Skills：https://raw.githubusercontent.com/sapuyou45-bit/ai-divination-skills/main/docs/update.md
```

## For AI Agents

You are updating filesystem-based skills that were previously installed from this repository.

### Boundaries

Follow the same boundaries as `docs/install.md`:

- Do not use `sudo`.
- Do not modify shell profiles.
- Do not install Python packages during the base update.
- Do not upload files or send data to external services.
- Do not overwrite unrelated user files.
- If the target skill directory is unclear, ask the user before updating.

### Target directory

Use the same skill directory as the current install. Prefer:

1. `$AI_SKILLS_DIR` if set.
2. `~/.claude/skills` for Claude-style local agents.
3. `~/.codex/skills` for Codex-style local agents.
4. A user-provided custom skill directory.

### Update command

Default Claude-style update:

```bash
curl -fsSL https://raw.githubusercontent.com/sapuyou45-bit/ai-divination-skills/main/install.sh | bash
```

Custom target:

```bash
export AI_SKILLS_DIR="$HOME/.codex/skills"
curl -fsSL https://raw.githubusercontent.com/sapuyou45-bit/ai-divination-skills/main/install.sh | bash
```

The installer replaces `tarot`, `iching`, and `xiaoliuren` with the latest repository versions. Existing skill folders are backed up under:

```text
<skills-dir>/.ai-divination-backups/<timestamp>/
```

### Dry run

```bash
curl -fsSL https://raw.githubusercontent.com/sapuyou45-bit/ai-divination-skills/main/install.sh | bash -s -- --dry-run
```

### Verify

After updating, verify the three scripts:

```bash
python3 "$HOME/.claude/skills/tarot/scripts/draw.py" --deck major --spread single --seed demo
python3 "$HOME/.claude/skills/iching/scripts/cast.py" --method coins --seed demo
python3 "$HOME/.claude/skills/xiaoliuren/scripts/cast.py" --method numbers --month 3 --day 12 --hour 7
```

If using a custom directory, replace `$HOME/.claude/skills` with the selected directory.

### Report back to the user

Tell the user:

- which skill directory was updated
- whether existing skill folders were backed up
- whether tarot, iching, and xiaoliuren verification passed
- how to ask for a reading next
