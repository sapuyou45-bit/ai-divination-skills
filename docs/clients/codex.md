# Use `ai-divination-skills` in Codex (OpenAI Codex CLI)

The Codex CLI supports MCP servers via its config file.

## 1. Install

```bash
pip install 'ai-divination-skills[lunar]'
```

## 2. Configure

Add the server to `~/.codex/config.toml`:

```toml
[mcp_servers.divination]
command = "ai-divination-mcp"
```

Restart `codex` (or open a new session).

## 3. Five tools become available

- `tarot.draw`
- `iching.cast`
- `xiaoliuren.cast`
- `bazi.cast`
- `interpretation_template`

## 4. Example prompts

- "Use the divination MCP to draw a three-card tarot reading on whether I should refactor the auth layer this week."
- "Cast an I Ching (yarrow) on the launch decision."
- "Read my bazi: born 1990-05-20 14:30."

The agent will run the audited tool, then call `interpretation_template` to fetch the strict response contract before interpreting.

## 5. Troubleshooting

- **`command not found`** → check `which ai-divination-mcp` and use the absolute path in `command`.
- **Lunar tools fail** → install with `pip install 'ai-divination-skills[lunar]'`.
- **Tools missing after edit** → restart the codex session.
