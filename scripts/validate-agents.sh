#!/usr/bin/env bash
# validate-agents.sh
# Verifies the Antigravity agent configuration in the repository.

set -e

echo "Validating Antigravity Agent Configuration..."

# 1. Check directories
for dir in .agents/rules .agents/skills .agents/agents; do
    if [ ! -d "$dir" ]; then
        echo "❌ Missing directory: $dir"
        exit 1
    fi
done
echo "✅ Directory structure is valid."

# 2. Check for Master Rule
if [ ! -f ".agents/rules/flyrank-engineering.md" ]; then
    echo "❌ Missing Master Rule: .agents/rules/flyrank-engineering.md"
    exit 1
fi
echo "✅ Master Rule exists."

# 3. Check Skills Frontmatter
shopt -s nullglob
for skill in .agents/skills/*/SKILL.md; do
    if ! head -n 1 "$skill" | grep -q "^---"; then
        echo "❌ Missing YAML frontmatter in $skill"
        exit 1
    fi
done
echo "✅ Skills YAML frontmatter is valid."

# 4. Check documentation
for doc in docs/REPOSITORY_MAP.md docs/ARCHITECTURE.md docs/AGENT_GUIDE.md; do
    if [ ! -f "$doc" ]; then
        echo "❌ Missing documentation: $doc"
        exit 1
    fi
done
echo "✅ Repository documentation exists."

echo "🎉 All Antigravity configurations are valid!"
