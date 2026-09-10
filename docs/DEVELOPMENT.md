# Development Guide

## Environment Setup

This project uses `uv` for lightning-fast dependency management.

### Initializing the environment

Ensure you have `uv` installed. Then sync dependencies:

```bash
uv sync
```

This will create a `.venv` virtual environment and install the required dependencies (such as `fastapi`).

## Running the Demo App

To run the sample FastAPI application:

```bash
uv run fastapi dev assignments/main.py
```
or 
```bash
uv run uvicorn assignments.main:app --reload
```

## Adding Dependencies

To add a new dependency to the project:

```bash
uv add <package-name>
```

To add a development dependency:

```bash
uv add --dev <package-name>
```

## Code Formatting and Linting

Currently, there are no strict formatting or linting tools (like `ruff` or `black`) configured. Once they are introduced, this section will be updated.
