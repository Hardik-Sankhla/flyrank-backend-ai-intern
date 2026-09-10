---
name: python-development
description: Follow this project's Python conventions, respect pyproject.toml, and use uv where applicable.
---

# Python Development Skill

## Objective
Ensure all Python development adheres to the project's standards using `uv`.

## Instructions
1. **Dependency Management**: Use `uv add <package>` to add dependencies. Never edit `uv.lock` manually.
2. **Execution**: Execute all Python code through `uv run` to ensure it runs within the managed `.venv`.
   - Example: `uv run fastapi dev assignments/main.py`
3. **Adherence to Architecture**: Do not arbitrarily create `src/` or `app/` directories until Phase C (Architecture Normalization) is initiated. Place experimental code in the appropriate `assignments/` or `scripts/` directories as currently modeled.
