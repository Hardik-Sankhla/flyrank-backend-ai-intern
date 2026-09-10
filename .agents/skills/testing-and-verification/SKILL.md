---
name: testing-and-verification
description: Discover the correct test commands, run targeted tests first, report verification honestly.
---

# Testing and Verification Skill

## Objective
Guide the agent on how to verify its changes in this repository.

## Instructions
1. **Current State**: There are currently no formal unit tests (`pytest`).
2. **Manual Verification**: Verify changes by executing the relevant script via `uv run`. For FastAPI apps, run the dev server and verify endpoints via curl or interactive docs.
3. **Honest Reporting**: Never claim a task is complete without verification. If tests are absent, explicitly state that manual verification was performed or that the changes are untested and require human review.
