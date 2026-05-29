"""Unified CLI for ai-divination-skills."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SCRIPT_COMMANDS = {
    "tarot": ROOT / "skills" / "tarot" / "scripts" / "draw.py",
    "iching": ROOT / "skills" / "iching" / "scripts" / "cast.py",
    "xiaoliuren": ROOT / "skills" / "xiaoliuren" / "scripts" / "cast.py",
}

TEMPLATE_FILES = {
    "shared": ROOT / "shared" / "interpretation-protocol.md",
    "tarot": ROOT / "skills" / "tarot" / "references" / "interpretation-template.md",
    "iching": ROOT / "skills" / "iching" / "references" / "interpretation-template.md",
    "xiaoliuren": ROOT / "skills" / "xiaoliuren" / "references" / "interpretation-template.md",
}


def print_usage() -> None:
    print(
        """ai-divination

Usage:
  ai-divination tarot [draw options]
  ai-divination iching [cast options]
  ai-divination xiaoliuren [cast options]
  ai-divination template [shared|tarot|iching|xiaoliuren]

Examples:
  ai-divination tarot --deck major --spread three-card
  ai-divination iching --method yarrow
  ai-divination xiaoliuren --method numbers --month 3 --day 12 --hour 7
  ai-divination template tarot
"""
    )


def run_script(command: str, args: list[str]) -> int:
    script = SCRIPT_COMMANDS[command]
    if not script.exists():
        print(f"Script not found for {command}: {script}", file=sys.stderr)
        return 1
    completed = subprocess.run([sys.executable, str(script), *args], cwd=ROOT)
    return completed.returncode


def print_template(args: list[str]) -> int:
    if len(args) != 1 or args[0] not in TEMPLATE_FILES:
        print("Usage: ai-divination template [shared|tarot|iching|xiaoliuren]", file=sys.stderr)
        return 2

    template_name = args[0]
    shared_text = TEMPLATE_FILES["shared"].read_text(encoding="utf-8")
    if template_name == "shared":
        print(shared_text)
        return 0

    skill_text = TEMPLATE_FILES[template_name].read_text(encoding="utf-8")
    print(shared_text.rstrip())
    print()
    print("---")
    print()
    print(skill_text)
    return 0


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] in {"-h", "--help"}:
        print_usage()
        return 0

    command = args[0]
    command_args = args[1:]
    if command == "template":
        return print_template(command_args)
    if command in SCRIPT_COMMANDS:
        return run_script(command, command_args)

    print(f"Unknown command: {command}", file=sys.stderr)
    print_usage()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
