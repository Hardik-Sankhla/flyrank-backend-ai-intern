# FlyRank Engineering Contract

## Core Principles

1. **Treat this repository as a real software project.**
2. **Inspect before editing**: Always explore the repository (e.g., read the Map, Architecture, and search code) before modifying files.
3. **Prefer minimal, reversible changes**: Do not introduce sweeping changes without explicit instructions.
4. **Never silently delete functionality.**
5. **Never move files without understanding references/imports.**
6. **Preserve working behavior** unless the task explicitly requires behavior changes.
7. **Use existing project tooling** instead of introducing competing tooling.
8. **uv Authority**: Use `uv` as the Python environment, dependency, and package-management authority (verified by `pyproject.toml`).
9. **Respect pyproject.toml and uv.lock**: Do not bypass them.
10. **Never manually modify uv.lock** unless explicitly required by the package manager.
11. **Run relevant tests** after changes.
12. **Run formatting/lint/type checks** when configured (e.g., `ruff`, `mypy`).
13. **Never claim a task is complete without verification.**
14. **Reporting**: Clearly report:
    - files changed
    - commands executed
    - tests executed
    - failures
    - remaining risks
15. **Never invent API behavior, credentials, environment variables, database schemas, or external service behavior.**
16. **Never commit secrets.**
17. **Never expose environment-variable values.**
18. **Prefer small changes over large rewrites.**
19. **Architecture**: Before architectural changes, explain the current architecture and proposed target architecture.
20. **Uncertainty**: When uncertain, inspect the repository rather than guessing.

## Workflow Phases

Agents should explicitly distinguish between the following phases of work:

- **Exploration**: Inspecting the repository, reading docs, searching code, understanding the problem space without making changes.
- **Planning**: Outlining proposed changes, architecture updates, or refactoring plans, seeking user approval if significant.
- **Implementation**: Making the agreed-upon minimal changes, following project conventions and tooling (`uv`).
- **Verification**: Running tests, formatting, linting, or manually verifying the changes work as intended.
- **Cleanup/Refactoring**: Only performed when explicitly requested, doing localized, behavior-preserving transformations.
