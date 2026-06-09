# Use `ai-divination-skills` in Continue (VS Code / JetBrains)

[Continue](https://continue.dev/) supports MCP servers via its `~/.continue/config.json` (or `config.yaml`).

## 1. Install

```bash
pip install 'ai-divination-skills[lunar]'
```

## 2. Configure

Add this entry to `~/.continue/config.json` under `experimental.modelContextProtocolServers`:

```json
{
  "experimental": {
    "modelContextProtocolServers": [
      {
        "transport": {
          "type": "stdio",
          "command": "ai-divination-mcp"
        }
      }
    ]
  }
}
```

Reload the Continue window. Five new tools become available to the chat.

## 3. Tools

- `tarot.draw`
- `iching.cast`
- `xiaoliuren.cast`
- `bazi.cast`
- `interpretation_template`

## 4. Example prompts

- "Use the divination tools to draw a three-card tarot reading for whether I should accept the offer."
- "Cast an I Ching with yarrow on the launch."
- "Read my bazi: born 1990-05-20 14:30 local time."

## 5. Troubleshooting

- **`command not found`** → make sure Continue can see your Python env. Use the absolute path from `which ai-divination-mcp`.
- **Tools missing** → reload the Continue window after editing `config.json`.
