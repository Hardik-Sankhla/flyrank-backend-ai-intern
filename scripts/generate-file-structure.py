import os
from pathlib import Path

# ============================================================
# Configuration
# ============================================================

# Target the parent directory of the script since it's located in scripts/
root = Path(__file__).parent.parent.resolve()

# ============================================================
# Repository structure
# ============================================================

DIRECTORIES = [
    "assignments/FL-01-workflow-audit/claude-project",
    "assignments/FL-01-workflow-audit/evidence/screenshots",

    "assignments/FL-02-prompting/evidence",

    "assignments/FL-03/evidence",

    "assignments/FL-04-automation/prompts",
    "assignments/FL-04-automation/workflow",
    "assignments/FL-04-automation/evidence",

    "projects",
    "resources",
    "scripts",
]

# ============================================================
# Initial files
# ============================================================

FILES = {

    "README.md": """# FlyRank AI Internship

Personal repository for documenting my FlyRank AI internship,
assignments, experiments, workflows, and projects.

## Repository Structure

```text
assignments/
    FL-01-workflow-audit/
    FL-02-prompting/
    FL-03/
    FL-04-automation/

projects/
resources/
```

## Assignments

|Assignment|Topic|Status|
|---|---|---|
|FL-01|AI Workflow Audit|In Progress|
|FL-02|Prompting Fundamentals|Not Started|
|FL-03|TBD|Not Started|
|FL-04|Ship an Automation Workflow|Not Started|

## Purpose

This repository is intended to document the actual work,  
experiments, decisions, evidence, and learnings produced  
during the internship.

> Private information, credentials, API keys, private datasets,  
> and confidential company information should never be committed.  
""",

    ".gitignore": """# Python

__pycache__/
*.py[cod]
*.pyo
*.pyd
.venv/
venv/
env/

# Environment / secrets

.env
.env.*
*.key
*.pem

# IDE

.vscode/
.idea/

# OS

.DS_Store
Thumbs.db

# Temporary files

*.tmp
*.log

# Jupyter

.ipynb_checkpoints/

# Generated/private data

data/private/
data/raw/
secrets/
credentials/

# Screenshots that may contain sensitive information

# Uncomment if needed:

# evidence/private/
""",

    "assignments/FL-01-workflow-audit/README.md": """# FL-01 — AI Workflow Audit

## Objective

Map recurring tasks from my real work, study, and AI  
engineering activities and identify where AI should be  
used, reviewed, collaborated with, automated, or avoided.

## Deliverables

- Workflow Audit
- Claude Project Configuration
- Evidence screenshots in `evidence/screenshots/`

## Three Target Tasks

1. AI/ML Technical Research
2. AI/Backend Debugging
3. Technical Workflow Automation

## Evidence

Screenshots and supporting evidence should be placed in:

```text
evidence/screenshots/
```

## Submission

The final FlyRank submission can reference this directory  
or the repository's corresponding public URL.  
""",

    "assignments/FL-01-workflow-audit/workflow-audit.md": """# FL-01 — AI Workflow Audit

**Name:** Hardik Sankhla  
**Track:** General AI Fluency  
**Assignment:** FL-01 — AI Workflow Audit

---

## 1. Introduction

This audit maps recurring tasks from my actual workflow,  
including AI engineering, technical research, backend  
development, infrastructure work, automation, studying,  
outreach, and career-related activities.

The purpose is to identify where AI should remain under  
direct human control, where AI can collaborate with me,  
where AI can perform delegated work with review, and  
where a workflow can reasonably be automated.

---

## 2. Recurring Tasks

|#|Real Task|Classification|Rationale|
|---|---|---|---|
|1|Debug Python/FastAPI/AI project errors|Collaborate with AI|AI can analyze logs and suggest fixes, but I need to understand and verify the root cause.|
|2|Research unfamiliar AI/ML concepts|Collaborate with AI|AI can accelerate exploration and explanation, while I verify important technical claims.|
|3|Design architecture for an AI system|Just me|AI can critique alternatives, but the core architectural decisions depend on my goals and constraints.|
|4|Read and understand technical papers|Collaborate with AI|AI can explain difficult sections and terminology while I develop and verify the understanding.|
|5|Build and modify AI models/inference pipelines|Collaborate with AI|AI can assist implementation and debugging, but the resulting system must be tested and validated.|
|6|Maintain local AI/agent infrastructure|Collaborate with AI|AI is useful for troubleshooting Termux, Linux, Docker, runtimes, and dependencies, but changes require verification.|
|7|Develop personal automation workflows|Delegate to AI with review|AI can generate scripts and workflow logic, but I need to review safety, correctness, and failure handling.|
|8|Analyze LinkedIn/outreach data|Fully automate|Structured conversation data can be cleaned, classified, clustered, and summarized automatically, with human review for important cases.|
|9|Write/revise LinkedIn outreach messages|Delegate to AI with review|AI can create personalized drafts, while I verify accuracy and decide what should actually be sent.|
|10|Prepare internship/job applications|Delegate to AI with review|AI can tailor applications, but factual claims and final positioning must remain under my control.|
|11|Study GATE DA concepts|Collaborate with AI|AI can teach concepts, create examples, and test understanding, but learning cannot be delegated completely.|
|12|Solve GATE DA problems|Just me|Independent problem solving is the actual skill being developed, so outsourcing the solution would reduce the value of the activity.|
|13|Decide which technical project to build|Just me|AI can brainstorm, but project selection depends on my goals, interests, resources, and constraints.|
|14|Write technical documentation/repository manuals|Delegate to AI with review|AI can transform notes and implementation details into documentation, but the final documentation must reflect the real system.|
|15|Explore unfamiliar technologies/tools|Collaborate with AI|AI can rapidly compare and explain tools, while I determine whether they work for my actual environment.|

---

## 3. Three Target Tasks

### Target Task 1 — AI/ML Technical Research

**Description**

Investigate an unfamiliar AI/ML research question and produce  
a technically grounded answer.

**Done well means:**

- The question is clearly defined.
- Established research is separated from speculation.
- Relevant approaches, papers, or systems are identified.
- The underlying mechanism is explained.
- Limitations and unresolved problems are identified.
- Important claims are supported by reliable sources.
- The final answer directly addresses the original question.

---

### Target Task 2 — AI/Backend Debugging

**Description**

Diagnose and resolve failures in my AI development  
environments and backend systems.

**Done well means:**

- The actual root cause is identified.
- The difference between symptoms and causes is explained.
- The smallest reasonable fix is proposed.
- Unnecessary system changes are avoided.
- The fix is tested.
- The reason the fix works is documented.
- Preventive measures are identified when appropriate.

---

### Target Task 3 — Technical Workflow Automation

**Description**

Convert repetitive technical or data-processing workflows  
into reliable automated pipelines.

**Done well means:**

- Expected inputs are handled automatically.
- Outputs have a predictable structure.
- Errors are detected rather than silently ignored.
- Important decisions remain reviewable.
- The workflow can be safely rerun.
- Performance or quality can be measured.
- The workflow produces a meaningful reduction in manual work.

---

## 4. Initial Success Criteria

The workflow audit is successful if:

- At least 10 recurring tasks are identified.
- Tasks represent my actual activities rather than generic examples.
- Every task has a classification.
- Every classification has a concrete rationale.
- At least two tasks remain intentionally human-only.
- Three reusable target tasks are clearly defined.
- Each target task has measurable quality criteria.

---

## 5. Reflection

The main observation from this audit is that AI is most useful  
to me when it acts as a collaborator rather than simply replacing  
the work.

For technical research and engineering, I benefit from using AI  
to accelerate exploration, debugging, implementation, and  
comparison while retaining responsibility for verification and  
decision-making.

For repetitive structured workflows, however, greater automation  
is appropriate when the inputs, outputs, and failure conditions  
can be clearly defined.

The three target tasks therefore represent three important forms  
of AI collaboration:

1. Research and reasoning
2. Technical diagnosis
3. Workflow automation  
""",
    
    "assignments/FL-01-workflow-audit/claude-project/instructions.md": """# Claude Project Instructions
    
## About Me

I am Hardik Sankhla, a Data Science / AI-focused software  
developer and researcher.

My work frequently involves:

- AI/ML research
- LLMs and generative AI
- Backend engineering
- Python and FastAPI
- AI inference pipelines
- Linux and infrastructure
- Docker
- AI agents and automation
- Data processing
- Technical experimentation
- GATE DA preparation
- Career and technical projects

## How I Want AI To Work With Me

Act as a technical collaborator rather than blindly completing  
tasks.

Priorities:

1. Accuracy over confidence.
2. Explain important reasoning and tradeoffs.
3. Clearly distinguish facts from assumptions.
4. Do not invent papers, benchmarks, APIs, or technical claims.
5. For debugging, identify the root cause before proposing fixes.
6. Prefer minimal, reversible changes.
7. When researching, distinguish established research from speculation.
8. When writing code, consider the actual environment and constraints.
9. Challenge my assumptions when evidence suggests they are wrong.
10. Ask for missing technical context when it materially affects the answer.

## Current Target Tasks

### 1. AI/ML Technical Research

Help investigate research questions and produce evidence-grounded  
technical conclusions.

### 2. AI/Backend Debugging

Help diagnose root causes, propose fixes, and verify solutions  
for real development environments.

### 3. Technical Workflow Automation

Help identify repetitive workflows that can be automated and  
design reliable implementations with appropriate human review.  
""",

    "assignments/FL-02-prompting/README.md": """# FL-02 — Prompting Fundamentals

**Status:** Not Started

This directory will contain prompts, experiments, outputs,  
comparisons, and conclusions from FL-02.

## Files

- `prompts.md` — prompts tested during the assignment
- `results.md` — observed outputs and analysis
- `evidence/` — screenshots or supporting evidence  
""",
    
    "assignments/FL-02-prompting/prompts.md": """# FL-02 Prompts
    
> Add prompts and iterations here as the assignment progresses.

## Experiment 1

### Task

TODO

### Prompt — Version 1

TODO

### Prompt — Improved Version

TODO

### Observations

TODO  
""",

    "assignments/FL-02-prompting/results.md": """# FL-02 Results

## Experiment 1

### Objective

TODO

### Result

TODO

### What Improved?

TODO

### What Did Not Improve?

TODO

### Final Prompt

TODO  
""",

    "assignments/FL-03/README.md": """# FL-03

**Status:** Not Started

Document the assignment objective, experiments, results,  
evidence, and final reflection here.  
""",

    "assignments/FL-04-automation/README.md": """# FL-04 — Ship an Automation Workflow

**Status:** Not Started

## Objective

Document an actual workflow that can be improved through  
automation.

## Structure

- `prompts/` — prompts used during development
- `workflow/` — implementation and workflow definitions
- `evidence/` — screenshots and proof of execution

## Workflow

TODO

## Before Automation

TODO

## After Automation

TODO

## Results

TODO

## Limitations

TODO  
""",

    "projects/README.md": """# Projects

Supporting projects related to the internship.

Do not include confidential company code or private data.  
""",

    "resources/README.md": """# Resources

Useful references, notes, documentation, and learning  
resources used during the internship.  
""",  
}

# ============================================================
# Generator
# ============================================================

def create_repo():  
    print(f"Creating repository structure: {root.resolve()}")

    # Create directories
    for directory in DIRECTORIES:
        path = root / directory
        path.mkdir(parents=True, exist_ok=True)

    # Create files without overwriting existing work
    created = 0
    skipped = 0

    for relative_path, content in FILES.items():
        path = root / relative_path

        path.parent.mkdir(parents=True, exist_ok=True)

        if path.exists():
            print(f"[SKIP]   {path}")
            skipped += 1
            continue

        path.write_text(content.strip() + "\\n", encoding="utf-8")
        print(f"[CREATE] {path}")
        created += 1

    print("\\n" + "=" * 60)
    print("Repository created successfully")
    print("=" * 60)
    print(f"Location : {root.resolve()}")
    print(f"Created  : {created} files")
    print(f"Skipped  : {skipped} existing files")

if __name__ == "__main__":  
    create_repo()
