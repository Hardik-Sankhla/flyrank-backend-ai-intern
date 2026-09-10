# Repository Map

**Status**: Baseline Bootstrap Map
**Last Updated**: September 2026

## 1. Application / Package
- **Actual Python package**: Currently, there is no canonical `src/` or `app/` package. The repository is primarily an educational/internship tracker.
- **Dependencies**: Managed by `uv` (`pyproject.toml` and `uv.lock`). The main dependency is `fastapi[standard]`.
- **Executable entry points**:
  - `assignments/main.py`: A simple, in-memory to-do list FastAPI application (educational demo).
  - `scripts/generate-file-structure.py`: A Python script for generating directory trees (utility script).

## 2. Directories & Components
- **`assignments/`**: Contains internship assignments (e.g., FL-01 to FL-04, BE-01, BE-02) and related documentation, prompts, and code.
- **`projects/`**: Intended for larger projects, currently empty or just containing a README.
- **`resources/`**: Contains shared resources, currently empty or just containing a README.
- **`scripts/`**: Contains utility scripts, notably `generate-file-structure.py`.
- **`docs/`**: Generated documentation (Architecture, Map, Development, Testing, Agent Guide).
- **`.agents/`**: Antigravity agent configuration (rules, skills, agents, plugins).

## 3. Code Classifications
- **Production-like code**: **None.** There is no live production code here yet.
- **Experimental / Educational code**: `assignments/main.py`, assignments content.
- **Documentation**: `README.md`, `Repository Architecture.md`, `AGENTS.md`, and all `.md` files in `assignments/`.
- **Generated / Ignore Files**: `.venv`, `__pycache__`.

## 4. Environment & Execution
- **Execution**: The FastAPI app in `assignments/main.py` can be executed using `fastapi dev assignments/main.py` or `uv run uvicorn assignments.main:app`.
- **Testing**: No formal test suite (`pytest` etc.) has been identified yet.
- **Formatting/Linting**: Not formally configured (no `ruff.toml` or pre-commit hooks found yet).
- **Type Checking**: Not formally configured.
- **External Services**: None currently required by `assignments/main.py`.
- **Environment Variables**: No `.env` requirements have been discovered for the current codebase.

## 5. Dead / Unused Code
- Historical assignments may be considered "dead" for production purposes, but are kept as historical artifacts.

## Summary (Verified vs Inferred)
- **VERIFIED FACT**: The repository uses `uv` for dependencies. It contains a FastAPI demo in `assignments/main.py`. It is structured to track internship progress.
- **INFERRED INFORMATION**: The repository is meant to be a monorepo for the intern's assignments, potentially transitioning into real project work later.
- **UNKNOWN / NEEDS VALIDATION**: Whether a canonical application package (`src/flyrank`) will be created in the future.
