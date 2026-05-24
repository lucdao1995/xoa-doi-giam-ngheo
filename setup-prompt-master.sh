#!/bin/bash
# Setup script: Cài prompt-master cho Claude Code
# Chạy: bash setup-prompt-master.sh

set -e

echo "=== Cài đặt Prompt Master cho dự án Xoá Đói Giảm Nghèo ==="

# 1. Copy skill vào ~/.claude/skills/
SKILL_SRC=".claude/skills/prompt-master"
SKILL_DEST="$HOME/.claude/skills/prompt-master"

if [ -d "$SKILL_DEST" ]; then
  echo "⚠  Prompt Master đã tồn tại ở $SKILL_DEST"
  echo "   Muốn ghi đè không? (y/N): "
  read -r overwrite
  if [ "$overwrite" = "y" ] || [ "$overwrite" = "Y" ]; then
    cp -r "$SKILL_SRC" "$SKILL_DEST"
    echo "✓ Đã ghi đè"
  fi
else
  mkdir -p "$HOME/.claude/skills"
  cp -r "$SKILL_SRC" "$SKILL_DEST"
  echo "✓ Đã copy skill vào $SKILL_DEST"
fi

# 2. Copy rules
RULE_SRC=".claude/rules/project-rules.md"
RULE_DEST="$HOME/.claude/rules/project-rules.md"

mkdir -p "$HOME/.claude/rules"
cp "$RULE_SRC" "$RULE_DEST"
echo "✓ Đã copy rules vào $RULE_DEST"

# 3. Thông báo
echo ""
echo "=== Hoàn tất! ==="
echo ""
echo "📌 Cách dùng Prompt Master:"
echo "   Trong Claude, nói tự nhiên như:"
echo '     "Write me a prompt for Claude Code to add a new chapter"'
echo '     "I need a prompt for Cursor to fix the navigation"'
echo ""
echo "📌 Hoặc dùng lệnh:"
echo "     /prompt-master I want to add chapter 31 to the Hugo site"
echo ""
echo "📌 Project-specific templates:"
echo "   prompt-templates/translate-chapter.md"
echo "   prompt-templates/hugo-add-chapter.md"
echo "   prompt-templates/deploy-workflow.md"
