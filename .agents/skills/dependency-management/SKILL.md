---
name: dependency-management
description: Respect uv/pyproject.toml/uv.lock. Avoid dependency duplication.
---

# Dependency Management Skill

## Objective
Manage project dependencies safely and effectively using `uv`.

## Instructions
1. **Tooling**: Always use `uv` for managing dependencies. Do not use `pip install` directly if it bypasses `pyproject.toml`.
2. **Audit Before Adding**: Check if an existing dependency already solves the problem before adding a new one.
3. **Lockfile Rule**: Never manually edit `uv.lock`. Let `uv` manage it.
