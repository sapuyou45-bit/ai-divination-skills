"""Unified CLI for ai-divination-skills."""

from __future__ import annotations

import sys
from importlib import resources

from ai_divination_skills import iching, tarot, xiaoliuren


COMMANDS = {
    "tarot": tarot.main,
    "iching": iching.main,
    "xiaoliuren": xiaoliuren.main,
}

TEMPLATE_NAMES = {"shared", "tarot", "iching", "xiaoliuren"}


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


def template_text(name: str) -> str:
    return resources.files("ai_divination_skills.templates").joinpath(f"{name}.md").read_text(encoding="utf-8")


def print_template(args: list[str]) -> int:
    if len(args) != 1 or args[0] not in TEMPLATE_NAMES:
        print("Usage: ai-divination template [shared|tarot|iching|xiaoliuren]", file=sys.stderr)
        return 2

    template_name = args[0]
    shared_text = template_text("shared")
    if template_name == "shared":
        print(shared_text)
        return 0

    skill_text = template_text(template_name)
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
    if command in COMMANDS:
        return COMMANDS[command](command_args)

    print(f"Unknown command: {command}", file=sys.stderr)
    print_usage()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
