# Dockerfile for ai-divination-skills MCP server (for Glama / generic MCP hosts)
# Builds a tiny image that exposes `ai-divination-mcp` over stdio (JSON-RPC 2.0).
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

COPY pyproject.toml README.md LICENSE ./
COPY ai_divination_skills ./ai_divination_skills

RUN pip install --upgrade pip && pip install .

# MCP servers communicate over stdio. The default entrypoint is the stdio server.
ENTRYPOINT ["ai-divination-mcp"]
