#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${AI_SKILLS_DIR:-$HOME/.claude/skills}"
REPO_URL="${AI_DIVINATION_REPO_URL:-https://github.com/sapuyou45-bit/ai-divination-skills.git}"
DRY_RUN=0

if [ "${1:-}" = "--dry-run" ]; then
  DRY_RUN=1
fi

case "$TARGET_DIR" in
  ""|"/"|"."|"$HOME")
    printf 'Refusing unsafe AI_SKILLS_DIR: %s\n' "$TARGET_DIR" >&2
    printf 'Use a dedicated agent skills directory, for example: %s/.claude/skills\n' "$HOME" >&2
    exit 1
    ;;
esac

printf 'Target skills directory: %s\n' "$TARGET_DIR"
printf 'Skills to install: tarot, iching, xiaoliuren, bazi\n'

if [ "$DRY_RUN" = "1" ]; then
  printf 'Dry run only. No files changed.\n'
  exit 0
fi

mkdir -p "$TARGET_DIR"

tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT

git clone --depth 1 "$REPO_URL" "$tmp_dir/repo"

backup_root="$TARGET_DIR/.ai-divination-backups/$(date +%Y%m%d-%H%M%S)"
backup_created=0

for skill in tarot iching xiaoliuren bazi; do
  if [ -e "$TARGET_DIR/$skill" ]; then
    mkdir -p "$backup_root"
    mv "$TARGET_DIR/$skill" "$backup_root/$skill"
    backup_created=1
    printf 'backed up existing %s to %s\n' "$skill" "$backup_root/$skill"
  fi
  cp -R "$tmp_dir/repo/skills/$skill" "$TARGET_DIR/$skill"
  printf 'installed %s\n' "$skill"
done

if command -v python3 >/dev/null 2>&1; then
  python3 "$TARGET_DIR/tarot/scripts/draw.py" --deck major --spread single --seed demo >/dev/null
  python3 "$TARGET_DIR/iching/scripts/cast.py" --method coins --seed demo >/dev/null
  python3 "$TARGET_DIR/xiaoliuren/scripts/cast.py" --method numbers --month 3 --day 12 --hour 7 >/dev/null
  printf 'verified tarot, iching, xiaoliuren\n'
else
  printf 'python3 not found; skipping script verification\n'
fi

printf '\nAI Divination Skills installed to:\n%s\n' "$TARGET_DIR"
if [ "$backup_created" = "1" ]; then
  printf 'Previous skill folders were backed up under:\n%s\n' "$backup_root"
fi
printf 'Ask your agent to use tarot, iching, xiaoliuren, or bazi when you want a symbolic reading.\n'
