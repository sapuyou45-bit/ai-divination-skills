"""Unified CLI for oraclebone."""

from __future__ import annotations

import sys
from importlib import resources

from oraclebone import bazi, iching, tarot, xiaoliuren


COMMANDS = {
    "tarot": tarot.main,
    "iching": iching.main,
    "xiaoliuren": xiaoliuren.main,
    "bazi": bazi.main,
}

TEMPLATE_NAMES = {"shared", "tarot", "iching", "xiaoliuren", "bazi"}


def print_usage() -> None:
    print(
        """oraclebone — the bone cracks, the model reads

Usage:
  oraclebone tarot [draw options]
  oraclebone iching [cast options]
  oraclebone xiaoliuren [cast options]
  oraclebone bazi --datetime <ISO 8601>
  oraclebone template [shared|tarot|iching|xiaoliuren|bazi]

Examples:
  oraclebone tarot --deck major --spread three-card
  oraclebone iching --method yarrow
  oraclebone xiaoliuren --method numbers --month 3 --day 12 --hour 7
  oraclebone bazi --datetime 1990-05-20T14:30:00
  oraclebone template bazi
"""
    )


def template_text(name: str) -> str:
    return resources.files("oraclebone.templates").joinpath(f"{name}.md").read_text(encoding="utf-8")


def print_template(args: list[str]) -> int:
    if len(args) != 1 or args[0] not in TEMPLATE_NAMES:
        print("Usage: oraclebone template [shared|tarot|iching|xiaoliuren|bazi]", file=sys.stderr)
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


def main_legacy(argv: list[str] | None = None) -> int:
    print(
        "Warning: 'ai-divination' is deprecated. The project is now Oraclebone — "
        "use the 'oraclebone' command (package: pip install oraclebone).",
        file=sys.stderr,
    )
    return main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
