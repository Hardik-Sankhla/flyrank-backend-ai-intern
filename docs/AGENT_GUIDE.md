# Antigravity Agent Guide

Welcome to the `flyrank-backend-ai-intern` repository. If you are an AI agent operating in this repository, this document provides your operational context.

## Where should an agent start?
- Start by reading `docs/REPOSITORY_MAP.md` and `.agents/rules/flyrank-engineering.md`.
- Read this `AGENT_GUIDE.md` for execution context.

## Which files are authoritative?
- `pyproject.toml` and `uv.lock` are the absolute authorities on Python dependencies and the Python environment.
- `/mnt/Storage/Career/engineering` is the source of truth for reusable capabilities outside of this local workspace.
- For local agent behavior, `.agents/rules/flyrank-engineering.md` is authoritative.

## Where is application code?
- Currently, there is no monolithic application code. It resides as experimental scripts (e.g., `assignments/main.py` and `scripts/generate-file-structure.py`).

## Where are tests?
- There are no tests currently. Wait for Phase D (Testing normalization).

## How should dependencies be changed?
- Use the `uv` tool (e.g., `uv add <package>`).
- Do NOT manually edit `uv.lock` or `pyproject.toml` unless strictly necessary.

## How should code be validated?
- Ensure the FastAPI app runs without errors using `uv run fastapi dev assignments/main.py`.
- If new validation tools (e.g., `ruff`, `pytest`) are added, run them after every change.

## Which directories are experimental?
- `assignments/` contains historical and experimental work.

## Which directories should not be modified casually?
- `.agents/` controls your own operating environment. Modify it only intentionally.
- `assignments/` should have its behavior preserved as it documents educational progress.

## How should an agent approach a new feature?
1. Inspect the repo to see if similar features exist.
2. Create an Implementation Plan.
3. Use `uv run` to verify the execution of the new feature.
4. Create localized tests.

## How should an agent approach a bug?
1. Inspect the stack trace.
2. Search the codebase for the offending file/line.
3. Make minimal, localized changes.
4. Verify the fix manually.

## How should an agent approach refactoring?
1. Require dependency/reference analysis before moving or deleting code.
2. Preserve behavior.
3. Prefer incremental refactoring.

## Safe vs. Unsafe Operations

**SAFE TO AUTO-EXECUTE**:
* read-only inspection
* git diff/status
* tests
* formatting
* static analysis
* local searches

**REQUIRE REVIEW** (Always wait for user confirmation or explicit requests):
* `rm` / delete of substantial files
* moving/renaming important files
* dependency installation/removal
* database mutations
* git reset / checkout / force operations
* network/API mutations
* credential-related operations
* deployment
* git push
