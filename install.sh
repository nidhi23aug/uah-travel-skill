#!/usr/bin/env bash
# Install the UAH travel skill for Claude Code.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
dest="$HOME/.claude/skills/uah-travel-authorization"

mkdir -p "$HOME/.claude/skills"
rm -rf "$dest"
cp -R "$here/skills/uah-travel-authorization" "$dest"
echo "Skill installed to $dest"

if [ ! -x "$HOME/.venvs/uah-ta/bin/python" ]; then
  python3 -m venv "$HOME/.venvs/uah-ta"
fi
"$HOME/.venvs/uah-ta/bin/pip" install --quiet --disable-pip-version-check --upgrade reportlab pypdf
echo "PDF tools ready in ~/.venvs/uah-ta"
echo "Start Claude Code with: claude --chrome"
