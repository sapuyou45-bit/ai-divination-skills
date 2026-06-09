# Use `ai-divination-skills` in Claude Desktop

Claude Desktop discovers MCP servers via `claude_desktop_config.json`.

## 1. Install

```bash
pip install 'ai-divination-skills[lunar]'
```

The `[lunar]` extra is required for the bazi (八字) and Xiao Liu Ren lunar-time tools.

## 2. Edit your config

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "divination": {
      "command": "ai-divination-mcp"
    }
  }
}
```

Restart Claude Desktop. The "Search and tools" indicator should now list the `divination` server with five tools.

## 3. Available tools

| Tool                      | What it does                                                  |
|---------------------------|---------------------------------------------------------------|
| `tarot.draw`              | Audited Fisher-Yates tarot draw (major or full deck)          |
| `iching.cast`             | I Ching cast — coins, yarrow, or manual lines                 |
| `xiaoliuren.cast`         | Xiao Liu Ren (小六壬) — numbers, time, or lunar-time          |
| `bazi.cast`               | Bazi / Four Pillars (八字) from a Gregorian birth datetime    |
| `interpretation_template` | The hard-rules template the model must follow before reading  |

## 4. Example prompts

- "Draw three tarot cards for whether I should accept this job."
- "Cast an I Ching with the yarrow method on whether to push the launch."
- "小六壬：现在是不是给老板发消息的好时机？"
- "Read my bazi: born 1990-05-20 at 14:30 local time."

The model will call the appropriate tool, then read `interpretation_template` and write the interpretation. It **never** invents a draw or chart.

## 5. Troubleshooting

- **"command not found: ai-divination-mcp"** → make sure your Claude Desktop is using a Python env that has the package installed. If you installed with `pipx`, point `command` at the full path printed by `which ai-divination-mcp`.
- **Bazi or lunar-time fails** → install the optional dep: `pip install 'ai-divination-skills[lunar]'`.
- **No tools show up** → fully quit Claude Desktop (Cmd-Q on macOS) and reopen; the config is read at launch only.
