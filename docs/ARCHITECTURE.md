# Repository Architecture

**Status**: Verified / Bootstrap State
**Last Updated**: September 2026

## Overview

This repository is primarily structured as an **internship tracker and educational sandbox** rather than a traditional production monorepo. It contains experiments, assignments, and AI-assisted workflows.

## Verified Structure

### Dependencies
- Handled by `uv`, utilizing `pyproject.toml` and `uv.lock`.
- Current primary dependency: `fastapi[standard]`.

### Executable Components
- `assignments/main.py`: A simple, in-memory to-do list FastAPI application (educational demo).
- `scripts/generate-file-structure.py`: A utility Python script for generating directory trees.

## Historical Intent vs. Current State

The original `Repository Architecture.md` detailed a highly structured hierarchical architecture (e.g., FL-01, FL-02, FL-03, FL-04 tracks). While some of these directories exist under `assignments/`, the core application is currently limited to demo apps rather than a unified production system.

### Contradictions
- The original architecture document may imply a unified application structure, but the actual code consists of isolated scripts and assignments.
- There is no canonical `src/flyrank` or `app/` directory yet.

## Data Flow
- `assignments/main.py` uses an in-memory data store for tasks (no external database configured).

## Next Architectural Steps (Phase C / Roadmap)
- Transitioning from an assignment-based repository to a structured software package.
- Establishing a `src/` layout.
- Introducing a real persistence layer if required.
