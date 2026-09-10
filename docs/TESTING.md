# Testing Strategy

**Status**: Initial Setup

## Current State

As of the agent bootstrap phase, there is no formal test suite (e.g., `pytest`) or automated CI configured for this repository. 

Previously, test result artifacts (`python_test_results.txt`) were generated and committed manually, but have since been cleaned up.

## Future Testing Architecture (Phase D)

Once the application structure is normalized, testing will follow these principles:

1. **Test Runner**: `pytest` will be the standard test runner.
2. **Execution**: Tests will be executed via `uv run pytest`.
3. **Location**: Tests should reside in a `tests/` directory at the root or adjacent to the `src/` modules.
4. **Scope**: Include Unit Tests, Integration Tests for APIs, and assignment-validation tests.

To manually verify the FastAPI app currently:
- Start the server: `uv run fastapi dev assignments/main.py`
- Open the interactive docs: `http://localhost:8000/docs`
