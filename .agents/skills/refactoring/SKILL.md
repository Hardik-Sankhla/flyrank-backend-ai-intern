---
name: refactoring
description: Require dependency/reference analysis before moving or deleting code. Preserve behavior.
---

# Refactoring Skill

## Objective
Ensure refactoring is safe, minimal, and preserves existing behavior.

## Instructions
1. **Reference Analysis**: Use `grep_search` to find all references and imports of a file, class, or function before moving or renaming it.
2. **Preserve Behavior**: Do not alter business logic or assignment outcomes during a structural refactor.
3. **Incremental Approach**: Propose refactoring in small, atomic commits rather than massive pull requests.
