---
name: architecture-analysis
description: Analyze module boundaries, dependencies, responsibilities, coupling, and architectural drift.
---

# Architecture Analysis Skill

## Objective
Help agents reason about the repository's structural boundaries.

## Instructions
1. **Assess Boundaries**: Recognize the difference between isolated assignment directories and shared resources.
2. **Architectural Drift**: Identify when actual code contradicts the documented architecture (e.g., `docs/ARCHITECTURE.md`).
3. **Propose Changes**: When the architecture needs to be normalized (e.g., moving to a `src/` layout), present a detailed structural plan before moving files.
