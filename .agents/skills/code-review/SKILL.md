---
name: code-review
description: Review diffs for regressions, edge cases, security problems, architectural violations, and complexity.
---

# Code Review Skill

## Objective
Provide rigorous code review standards for the repository.

## Instructions
1. **Review Diffs**: Always generate and review a diff of proposed changes against the current branch.
2. **Key Areas to Check**:
   - **Regressions**: Ensure existing functionality (especially in assignments) is not broken.
   - **Complexity**: Keep solutions simple and minimal.
   - **Architecture**: Ensure the code aligns with `docs/ARCHITECTURE.md`.
3. **Avoid Large Rewrites**: Favor small, incremental changes over sweeping refactors.
