# Use `ai-divination-skills` in Cursor

Cursor supports MCP servers from its Settings → Features → MCP panel, or directly via `~/.cursor/mcp.json`.

## 1. Install

```bash
pip install 'ai-divination-skills[lunar]'
```

## 2. Configure

Edit `~/.cursor/mcp.json` (create if missing):

```json
{
  "mcpServers": {
    "divination": {
      "command": "ai-divination-mcp"
    }
  }
}
```

Reload Cursor. The MCP panel should show `divination` with five tools.

## 3. Tools

| Tool                      | What it does                                                  |
|---------------------------|---------------------------------------------------------------|
| `tarot.draw`              | Audited Fisher-Yates tarot draw                               |
| `iching.cast`             | I Ching cast — coins, yarrow, or manual lines                 |
| `xiaoliuren.cast`         | Xiao Liu Ren (小六壬) cast                                    |
| `bazi.cast`               | Bazi / Four Pillars (八字) from a Gregorian birth datetime    |
| `interpretation_template` | The hard-rules template the model must follow before reading  |

## 4. Example chat prompts

- "Draw three tarot cards on whether I should refactor `auth.py` this sprint."
- "Cast an I Ching (yarrow) on the v2 launch decision."
- "Read my bazi: 1990-05-20 14:30."

## 5. Per-skill Cursor rules

Each skill ships a `.mdc` rule file at `skills/<skill>/agents/cursor.mdc`. Drop them into your project's `.cursor/rules/` folder to scope the divination workflow to a specific repo.
