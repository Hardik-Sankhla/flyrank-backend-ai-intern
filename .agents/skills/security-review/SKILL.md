---
name: security-review
description: Detect secrets, unsafe subprocess usage, insecure configuration, injection risks.
---

# Security Review Skill

## Objective
Prevent security vulnerabilities and secrets leakage in the repository.

## Instructions
1. **Secret Scanning**: Never expose actual secret values (API keys, passwords, tokens). Use placeholder variables or `.env` files (which must be `.gitignore`d).
2. **Subprocesses**: Avoid unsafe `subprocess` usage with `shell=True` unless strictly sanitized.
3. **Injection**: Ensure API inputs (e.g., in FastAPI endpoints) are properly validated using Pydantic to prevent injection risks.
