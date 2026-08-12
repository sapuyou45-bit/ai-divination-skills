#!/usr/bin/env python3
"""Verify all declared version strings match across the repository.

Checks that ``project.version`` in pyproject.toml, ``__version__`` in
oraclebone/__init__.py, ``version`` in server.json, and the
``version`` field in every skills/*/agents/gemini.yaml all agree.

Run in CI so a release bump can never drift out of sync again.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def version_from_pyproject() -> str:
    text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    match = re.search(r"(?m)^version\s*=\s*[\"']([^\"']+)[\"']", text)
    if not match:
        raise SystemExit("ERROR: version not found in pyproject.toml")
    return match.group(1)


def version_from_init() -> str:
    text = (ROOT / "oraclebone" / "__init__.py").read_text(encoding="utf-8")
    match = re.search(r"__version__\s*=\s*[\"']([^\"']+)[\"']", text)
    if not match:
        raise SystemExit("ERROR: __version__ not found in oraclebone/__init__.py")
    return match.group(1)


def version_from_server_json() -> str:
    data = json.loads((ROOT / "server.json").read_text(encoding="utf-8"))
    return str(data["version"])


def version_from_gemini_yamls() -> dict[str, str]:
    versions: dict[str, str] = {}
    for yaml_path in sorted((ROOT / "skills").glob("*/agents/gemini.yaml")):
        text = yaml_path.read_text(encoding="utf-8")
        match = re.search(r"(?m)^version\s*:\s*[\"']?([^\"'\s#]+)", text)
        if not match:
            raise SystemExit(f"ERROR: version not found in {yaml_path}")
        versions[yaml_path.relative_to(ROOT).as_posix()] = match.group(1)
    return versions


def main() -> int:
    sources: dict[str, str] = {
        "pyproject.toml": version_from_pyproject(),
        "oraclebone/__init__.py": version_from_init(),
        "server.json": version_from_server_json(),
    }
    sources.update(version_from_gemini_yamls())

    expected = next(iter(sources.values()))
    failures = [f"{name}={ver}" for name, ver in sources.items() if ver != expected]

    for name, ver in sources.items():
        print(f"{name}: {ver}")

    if failures:
        print(f"\nERROR: version mismatch. Expected {expected} everywhere, got:")
        for failure in failures:
            print(f"  {failure}")
        return 1

    print(f"\nOK: all versions match at {expected}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
