Tasks that are _genuinely mine_ are: we have a very unusual mix of AI engineering, research, GATE preparation, automation, internship work, Linux/infra work, projects, and outreach.
## FL-01 workflow audit - our real-life workflow audit

| #   | Task you actually do                                   | Classification                | Why                                                                                                                                                                                                             |
| --- | ------------------------------------------------------ | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Debug Python/FastAPI/AI project errors**             | 🤝 Collaborate with AI        | You can give AI the traceback, code and environment, but you need to understand and verify the fix rather than blindly applying it.                                                                             |
| 2   | **Research an unfamiliar AI/ML concept**               | 🤝 Collaborate with AI        | You regularly investigate things like model adaptation, post-training, agents, inference, RAG alternatives, etc. AI can accelerate exploration, but you need to judge whether the research is actually correct. |
| 3   | **Design architecture for an AI system**               | 👤 Just me                    | AI can critique architectures, but the actual architectural decisions—tradeoffs, constraints, what you are _really_ trying to build—are yours.                                                                  |
| 4   | **Read and understand technical papers**               | 🤝 Collaborate with AI        | AI can explain equations, sections and terminology, while you verify the paper and develop your own understanding.                                                                                              |
| 5   | **Build/modify AI models and inference pipelines**     | 🤝 Collaborate with AI        | AI is useful for implementation, debugging and optimization, but you must test whether the resulting pipeline actually works.                                                                                   |
| 6   | **Work on your local AI/agent infrastructure**         | 🤝 Collaborate with AI        | Things like Termux, Ubuntu/PRoot, Docker, model runtimes, storage and services involve lots of troubleshooting where AI is useful—but the final environment has to be validated by you.                         |
| 7   | **Develop personal automation workflows**              | ⚙️ Delegate to AI with review | AI can generate scripts/workflows, but you should review permissions, logic and failure cases before allowing automation to run.                                                                                |
| 8   | **Analyze your LinkedIn/outreach data**                | 🤖 Fully automate             | Your large outreach dataset already contains structured information that can be classified, clustered and summarized automatically. Human intervention is mainly needed for exceptions/hot leads.               |
| 9   | **Write/revise LinkedIn outreach messages**            | 🤖 Delegate to AI with review | AI can produce personalized drafts from lead/company context, but you should review the final message before sending.                                                                                           |
| 10  | **Prepare internship/job applications**                | 🤖 Delegate to AI with review | AI can tailor CV bullets, cover letters and messages to a specific role, while you verify factual accuracy and decide what you actually want to claim.                                                          |
| 11  | **Study GATE DA concepts**                             | 🤝 Collaborate with AI        | AI can teach, generate examples and test your understanding, but the learning itself cannot be outsourced.                                                                                                      |
| 12  | **Solve GATE DA problems**                             | 👤 Just me                    | The point is to develop your own problem-solving ability. AI solving everything for you would defeat the purpose.                                                                                               |
| 13  | **Plan what technical project to build next**          | 👤 Just me                    | AI can brainstorm, but your project choices depend on your own interests, career direction, available hardware and long-term goals.                                                                             |
| 14  | **Write technical documentation / repository manuals** | 🤖 Delegate to AI with review | AI can turn your commands, architecture and notes into documentation, while you verify that it accurately represents the actual repository.                                                                     |
| 15  | **Explore new technologies/tools**                     | 🤝 Collaborate with AI        | AI can rapidly compare tools and explain unfamiliar technologies, while you test whether they actually solve your particular problem.                                                                           |

**Note:** These are the **15 genuinely personal tasks**, I've actually been doing with AI projects, infrastructure, outreach, research and studying. Importantly, you've got **three “Just me” tasks**, The assignment specifically asks for at least two tasks honestly classified as “just me.”
### What I'd recommend for you 

```
flyrank-ai-internship/
│
├── README.md
│
├── assignments/
│   ├── FL-01-workflow-audit/
│   │   ├── README.md
│   │   ├── workflow-audit.md
│   │   ├── claude-project/
│   │   │   └── instructions.md
│   │   └── evidence/
│   │       └── screenshots/
│   │
│   ├── FL-02-prompting/
│   │   ├── README.md
│   │   ├── prompts.md
│   │   ├── results.md
│   │   └── evidence/
│   │
│   ├── FL-03-...
│   │
│   └── FL-04-automation/
│       ├── README.md
│       ├── workflow/
│       ├── prompts/
│       └── evidence/
│
├── projects/
│   └── ...
│
└── resources/
    └── ...
```

## For **FL-01 specifically**

I'd make the main deliverable:

```
assignments/
└── FL-01-workflow-audit/
    ├── README.md
    ├── workflow-audit.md
    └── evidence/
        ├── claude-project.png
        └── ...
```

### `workflow-audit.md`

This should contain the **actual 1–2 page submission**:

1. Brief introduction
2. Your 15 real tasks
3. Classification + rationale
4. Your 3 selected target tasks
5. “Done well” success definitions
6. Short conclusion

### `README.md`

Make this the **landing page for FL-01**:

```
# FL-01 — AI Workflow Audit

## Objective

Map recurring tasks from my real work, study, and
AI engineering activities and identify where AI should
be used, reviewed, collaborated with, or avoided.

## Deliverables

- [Workflow Audit](./workflow-audit.md)
- [Claude Project Configuration](./claude-project/instructions.md)
- Evidence screenshots

## Three Target Tasks

1. AI/ML Technical Research
2. AI/Backend Debugging
3. Technical Workflow Automation
```

Then the GitHub link you submit is simply the FL-01 folder/repo URL.

---

## Why I prefer a repo for **you**

Because you're not doing just one assignment.

You're going to accumulate:

**FL-01 → FL-02 → FL-03 → FL-04 → other assignments → capstone**

And several of your assignments are likely to involve **actual code, prompts, experiments, screenshots, automation workflows and results**.

A repo lets you preserve the evolution:

```
FL-01
  ↓
"I identified my workflow"

FL-02
  ↓
"I improved how I prompt AI"

FL-03
  ↓
"I improved the collaboration"

FL-04
  ↓
"I actually automated the workflow"
```

That makes the internship repository potentially useful **after the internship too**—as a portfolio showing how you actually use AI, rather than merely a folder of certificates.

### One important thing

Don't put **private internship information, private datasets, API keys, credentials, personal emails, internal links, or confidential company material** in a public repository.

For example, your LinkedIn outreach dataset should **not** simply be uploaded because it contains real conversations. Put sanitized/sample data or documentation of the workflow instead.

---

### My recommendation

**Use GitHub + Markdown as the master repository.**

Then for the FlyRank submission:

> **Public GitHub repo → `assignments/FL-01-workflow-audit/` → `README.md`**

And if you want to be extra safe, also upload the rendered **PDF** of the workflow audit to FlyRank. Their portal accepts either a valid public link or an uploaded file.

So you effectively have:

**GitHub = source of truth**  
**PDF = clean formal submission**  
**Screenshots = evidence**

That's the setup I'd use for your entire internship.

Today 2:50 AM

generate a python code so i can generate these files and structure correctly

Absolutely. Since you want to build this as a **long-term FlyRank internship repository**, here's a Python generator that creates the structure cleanly and avoids overwriting existing work.

It will create:

```
flyrank-ai-internship/
├── README.md
├── assignments/
│   ├── FL-01-workflow-audit/
│   │   ├── README.md
│   │   ├── workflow-audit.md
│   │   ├── claude-project/
│   │   │   └── instructions.md
│   │   └── evidence/
│   │       └── screenshots/
│   ├── FL-02-prompting/
│   │   ├── README.md
│   │   ├── prompts.md
│   │   ├── results.md
│   │   └── evidence/
│   ├── FL-03/
│   │   ├── README.md
│   │   └── evidence/
│   └── FL-04-automation/
│       ├── README.md
│       ├── prompts/
│       ├── workflow/
│       └── evidence/
├── projects/
├── resources/
└── .gitignore
```

I also made the generator **idempotent**: if you run it again, it won't destroy files you've already written.

````
from pathlib import Path


# ============================================================
# Configuration
# ============================================================

REPO_NAME = "flyrank-ai-internship"


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
````

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
> """,

```
".gitignore": """# Python
```

**pycache**/  
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

```
"assignments/FL-01-workflow-audit/README.md": """# FL-01 — AI Workflow Audit
```

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

```
evidence/screenshots/
```

## Submission

The final FlyRank submission can reference this directory  
or the repository's corresponding public URL.  
""",

```
"assignments/FL-01-workflow-audit/workflow-audit.md": """# FL-01 — AI Workflow Audit
```

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

```
"assignments/FL-02-prompting/README.md": """# FL-02 — Prompting Fundamentals
```

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

```
"assignments/FL-02-prompting/results.md": """# FL-02 Results
```

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

```
"assignments/FL-03/README.md": """# FL-03
```

**Status:** Not Started

Document the assignment objective, experiments, results,  
evidence, and final reflection here.  
""",

```
"assignments/FL-04-automation/README.md": """# FL-04 — Ship an Automation Workflow
```

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

```
"projects/README.md": """# Projects
```

Supporting projects related to the internship.

Do not include confidential company code or private data.  
""",

```
"resources/README.md": """# Resources
```

Useful references, notes, documentation, and learning  
resources used during the internship.  
""",  
}

# ============================================================

# Generator

# ============================================================

def create_repo():  
root = Path(REPO_NAME)

```
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

    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"[CREATE] {path}")
    created += 1

print("\n" + "=" * 60)
print("Repository created successfully")
print("=" * 60)
print(f"Location : {root.resolve()}")
print(f"Created  : {created} files")
print(f"Skipped  : {skipped} existing files")
print()
print("Next steps:")
print(f"  cd {REPO_NAME}")
print("  git init")
print("  git add .")
print('  git commit -m "Initialize FlyRank internship repository"')
print("  git branch -M main")
print("  git remote add origin <YOUR_GITHUB_REPO_URL>")
print("  git push -u origin main")
```

if **name** == "**main**":  
create_repo()

````

### Run it

Save it as:

```text
create_flyrank_repo.py
````

Then:

```
python create_flyrank_repo.py
```

It will create the complete repository in the **current directory**.

Then:

```
cd flyrank-ai-internship
git init
git add .
git commit -m "Initialize FlyRank internship repository"
```

After you create the GitHub repository:

```
git branch -M main
git remote add origin YOUR_REPO_URL
git push -u origin main
```

One thing I'd **strongly recommend**: don't treat this generated content as permanently final. The FL-01 instructions specifically say the tasks should be genuinely yours, so before submission we should refine the 15 rows with your _actual_ recurring activities and concrete examples rather than making the repository look artificially polished.

/home/hardik-sankhla/Desktop/flyrank-backend-ai-intern/scripts/generate-file-structure.py generate code for this

Yes — since the script itself is at:

```
/home/hardik-sankhla/Desktop/flyrank-backend-ai-intern/scripts/generate-file-structure.py
```

use this version. It creates the repository **inside the existing FlyRank project**, rather than creating another `flyrank-ai-internship` directory wherever you happen to run the script.

````
from pathlib import Path


# ============================================================
# Project Configuration
# ============================================================

# This script lives in:
# /home/hardik-sankhla/Desktop/flyrank-backend-ai-intern/scripts/
#
# Therefore the repository root is the parent of "scripts".

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent


# ============================================================
# Repository Structure
# ============================================================

DIRECTORIES = [
    # FL-01
    "assignments/FL-01-workflow-audit/claude-project",
    "assignments/FL-01-workflow-audit/evidence/screenshots",

    # FL-02
    "assignments/FL-02-prompting/evidence",

    # FL-03
    "assignments/FL-03/evidence",

    # FL-04
    "assignments/FL-04-automation/prompts",
    "assignments/FL-04-automation/workflow",
    "assignments/FL-04-automation/evidence",

    # Supporting material
    "projects",
    "resources",
]


# ============================================================
# Files
# ============================================================

FILES = {

    # --------------------------------------------------------
    # Root README
    # --------------------------------------------------------

    "README.md": """# FlyRank Backend AI Engineering Internship

Repository for documenting my FlyRank internship work,
assignments, experiments, technical implementations,
AI workflows, automation, and supporting evidence.

## Repository Structure

```text
flyrank-backend-ai-intern/
│
├── assignments/
│   ├── FL-01-workflow-audit/
│   ├── FL-02-prompting/
│   ├── FL-03/
│   └── FL-04-automation/
│
├── projects/
├── resources/
├── scripts/
│   └── generate-file-structure.py
│
└── README.md
````

## Assignment Status

|Assignment|Topic|Status|
|---|---|---|
|FL-01|AI Workflow Audit|In Progress|
|FL-02|Prompting Fundamentals|Not Started|
|FL-03|TBD|Not Started|
|FL-04|Ship an Automation Workflow|Not Started|

## Purpose

This repository documents the actual work completed during  
the internship, including:

- workflow audits
- prompts and prompt experiments
- AI-assisted development
- technical research
- backend engineering
- automation workflows
- experiments
- results
- evidence
- reflections and learnings

## Important

Do not commit:

- API keys
- passwords
- credentials
- private datasets
- private conversations
- confidential company information
- proprietary source code  
    """,
    
    # --------------------------------------------------------
    
    # Gitignore
    
    # --------------------------------------------------------
    
    ".gitignore": """# ============================================================
    

# Python

# ============================================================

**pycache**/  
*.py[cod]  
*.pyo  
*.pyd

.venv/  
venv/  
env/

# ============================================================

# Environment / Secrets

# ============================================================

.env  
.env.*  
*.key  
*.pem  
credentials/  
secrets/

# ============================================================

# IDE

# ============================================================

.vscode/  
.idea/

# ============================================================

# OS

# ============================================================

.DS_Store  
Thumbs.db

# ============================================================

# Logs / Temporary

# ============================================================

*.log  
*.tmp

# ============================================================

# Jupyter

# ============================================================

.ipynb_checkpoints/

# ============================================================

# Private / Raw Data

# ============================================================

data/raw/  
data/private/  
private/  
""",

```
# ========================================================
# FL-01
# ========================================================

"assignments/FL-01-workflow-audit/README.md": """# FL-01 — AI Workflow Audit
```

## Objective

Map recurring tasks from my real work, study, technical  
projects, AI engineering activities, and automation work.

The goal is to identify where AI should:

- remain under direct human control
- collaborate with me
- perform delegated work with review
- be fully automated

## Deliverables

- Workflow Audit
- Claude Project Instructions
- Evidence screenshots in `evidence/screenshots/`

## Three Target Tasks

1. AI/ML Technical Research
2. AI/Backend Debugging
3. Technical Workflow Automation

## Evidence

Supporting screenshots and evidence should be placed in:

```
evidence/screenshots/
```

## Submission

The assignment can be submitted through the FlyRank portal  
using the repository link and/or an exported document.  
""",

```
"assignments/FL-01-workflow-audit/workflow-audit.md": """# FL-01 — AI Workflow Audit
```

**Name:** Hardik Sankhla  
**Track:** General AI Fluency  
**Assignment:** FL-01 — AI Workflow Audit

---

## 1. Introduction

This audit maps recurring tasks from my actual workflow,  
including AI engineering, backend development, technical  
research, infrastructure work, automation, studying,  
outreach, and career-related activities.

The purpose is to understand where AI provides useful  
leverage, where human review is necessary, and where  
automation is appropriate.

---

## 2. Recurring Tasks

|#|Real Task|Classification|Rationale|
|---|---|---|---|
|1|Debug Python/FastAPI/AI project errors|Collaborate with AI|AI can analyze logs and suggest fixes, but I need to understand and verify the root cause.|
|2|Research unfamiliar AI/ML concepts|Collaborate with AI|AI can accelerate exploration and explanation, while important claims need verification.|
|3|Design architecture for an AI system|Just me|AI can critique alternatives, but the core architectural decisions depend on my goals and constraints.|
|4|Read and understand technical papers|Collaborate with AI|AI can explain difficult sections while I develop and verify my understanding.|
|5|Build and modify AI models/inference pipelines|Collaborate with AI|AI can assist implementation and debugging, but the resulting system must be tested.|
|6|Maintain local AI/agent infrastructure|Collaborate with AI|AI can assist with Linux, Termux, Docker, runtimes, and dependency problems, but changes require verification.|
|7|Develop personal automation workflows|Delegate to AI with review|AI can generate workflow logic and scripts, but I need to review correctness and failure cases.|
|8|Analyze LinkedIn/outreach data|Fully automate|Structured data can be cleaned, classified, clustered, and summarized automatically, with human review for important cases.|
|9|Write and revise outreach messages|Delegate to AI with review|AI can create personalized drafts, while I verify accuracy before sending.|
|10|Prepare internship/job applications|Delegate to AI with review|AI can tailor applications, but factual claims and final positioning remain my responsibility.|
|11|Study GATE DA concepts|Collaborate with AI|AI can teach concepts and generate practice material, but the learning itself cannot be delegated.|
|12|Solve GATE DA problems independently|Just me|Independent problem solving is the skill being developed.|
|13|Decide which technical project to build|Just me|AI can brainstorm, but project selection depends on my own goals and constraints.|
|14|Write technical documentation|Delegate to AI with review|AI can transform technical notes into documentation, while I verify accuracy.|
|15|Explore unfamiliar technologies|Collaborate with AI|AI can explain and compare technologies, while I test whether they work in my environment.|

---

## 3. Three Target Tasks

### Target Task 1 — AI/ML Technical Research

Investigate an unfamiliar AI/ML research question and produce  
a technically grounded answer.

#### Done Well Means

- The question is clearly defined.
- Established research is separated from speculation.
- Relevant approaches, papers, or systems are identified.
- The underlying mechanisms are explained.
- Limitations and unresolved problems are identified.
- Important claims are supported by reliable sources.
- The final answer directly addresses the original question.

---

### Target Task 2 — AI/Backend Debugging

Diagnose and resolve failures in my AI development  
environments and backend systems.

#### Done Well Means

- The root cause is identified.
- Symptoms are separated from causes.
- The smallest reasonable fix is proposed.
- Unnecessary system changes are avoided.
- The fix is tested.
- The reason the fix works is documented.
- Preventive measures are identified where appropriate.

---

### Target Task 3 — Technical Workflow Automation

Convert repetitive technical or data-processing workflows  
into reliable automated pipelines.

#### Done Well Means

- Expected inputs are handled automatically.
- Outputs have a predictable structure.
- Errors are detected rather than silently ignored.
- Important decisions remain reviewable.
- The workflow can be safely rerun.
- Performance or quality can be measured.
- Manual effort is meaningfully reduced.

---

## 4. Success Criteria

The workflow audit is successful if:

- At least 10 recurring tasks are identified.
- Tasks represent my actual activities.
- Every task has a classification.
- Every classification has a rationale.
- At least two tasks are intentionally marked "Just me".
- Three reusable target tasks are defined.
- Each target task has measurable quality criteria.

---

## 5. Reflection

The main observation from this audit is that AI is most useful  
to me when it acts as a collaborator rather than simply  
replacing the work.

For technical research and engineering, AI can accelerate  
exploration, debugging, implementation, and comparison while  
I retain responsibility for verification and decision-making.

For repetitive structured workflows, greater automation is  
appropriate when inputs, outputs, and failure conditions can  
be clearly defined.

The three target tasks therefore represent three forms of  
AI collaboration:

1. Research and reasoning
2. Technical diagnosis
3. Workflow automation  
    """,
    
    "assignments/FL-01-workflow-audit/claude-project/instructions.md": """# Claude Project Instructions
    

## About Me

I am Hardik Sankhla, a Data Science / AI-focused developer  
and technical researcher.

My work involves:

- AI/ML research
- LLMs and generative AI
- Backend engineering
- Python and FastAPI
- AI inference pipelines
- Linux and infrastructure
- Docker
- AI agents
- Automation
- Data processing
- Technical experimentation
- GATE DA preparation
- Technical projects

## How AI Should Work With Me

Act as a technical collaborator rather than blindly  
completing tasks.

### Priorities

1. Accuracy over confidence.
2. Explain important reasoning and tradeoffs.
3. Clearly distinguish facts from assumptions.
4. Never invent papers, benchmarks, APIs, or technical claims.
5. For debugging, identify the root cause before proposing fixes.
6. Prefer minimal and reversible changes.
7. For research, distinguish established research from speculation.
8. Consider my actual environment and constraints.
9. Challenge incorrect assumptions when evidence supports doing so.
10. Ask for missing technical context when it materially affects the answer.

## Current Target Tasks

### 1. AI/ML Technical Research

Investigate research questions and produce evidence-grounded  
technical conclusions.

### 2. AI/Backend Debugging

Diagnose root causes, propose fixes, and verify solutions  
for real development environments.

### 3. Technical Workflow Automation

Identify repetitive workflows and design reliable automation  
with appropriate human review.  
""",

```
# ========================================================
# FL-02
# ========================================================

"assignments/FL-02-prompting/README.md": """# FL-02 — Prompting Fundamentals
```

**Status:** Not Started

This directory contains prompts, iterations, outputs,  
comparisons, and conclusions from FL-02.

## Files

- `prompts.md`
- `results.md`
- `evidence/`  
    """,
    
    "assignments/FL-02-prompting/prompts.md": """# FL-02 — Prompt Experiments
    

> Add real prompts and iterations here.

## Experiment 1

### Task

TODO

### Initial Prompt

TODO

### Improved Prompt

TODO

### Why It Was Improved

TODO  
""",

```
"assignments/FL-02-prompting/results.md": """# FL-02 — Results
```

## Experiment 1

### Objective

TODO

### Initial Result

TODO

### Improved Result

TODO

### What Improved?

TODO

### What Did Not Improve?

TODO

### Final Prompt

TODO  
""",

```
# ========================================================
# FL-03
# ========================================================

"assignments/FL-03/README.md": """# FL-03
```

**Status:** Not Started

Document:

- assignment objective
- task
- approach
- experiments
- results
- evidence
- reflection
- final conclusions  
    """,
    
    # ========================================================
    
    # FL-04
    
    # ========================================================
    
    "assignments/FL-04-automation/README.md": """# FL-04 — Ship an Automation Workflow
    

**Status:** Not Started

## Objective

Document and implement a real workflow that benefits from  
automation.

## Structure

### prompts/

Prompts used during development.

### workflow/

Automation implementation and configuration.

### evidence/

Screenshots and execution evidence.

## Workflow

TODO

## Before Automation

TODO

## After Automation

TODO

## Results

TODO

## Failure Handling

TODO

## Limitations

TODO

## Reflection

TODO  
""",

```
# ========================================================
# Projects
# ========================================================

"projects/README.md": """# Projects
```

Supporting projects related to the internship.

Only include projects that are appropriate for public  
documentation.

Do not include confidential company code or private data.  
""",

```
# ========================================================
# Resources
# ========================================================

"resources/README.md": """# Resources
```

Useful references, technical documentation, research papers,  
notes, and learning resources used during the internship.  
""",  
}

# ============================================================

# Helper Functions

# ============================================================

def create_directories():  
"""Create all required directories."""

```
print("\nCreating directories...\n")

for directory in DIRECTORIES:
    path = REPO_ROOT / directory

    path.mkdir(
        parents=True,
        exist_ok=True,
    )

    print(f"[DIR]    {path.relative_to(REPO_ROOT)}")
```

def create_files():  
"""Create files without overwriting existing work."""

```
print("\nCreating files...\n")

created = 0
skipped = 0

for relative_path, content in FILES.items():

    path = REPO_ROOT / relative_path

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    # IMPORTANT:
    # Never overwrite existing files.
    if path.exists():
        print(f"[SKIP]   {relative_path}")
        skipped += 1
        continue

    path.write_text(
        content.rstrip() + "\n",
        encoding="utf-8",
    )

    print(f"[CREATE] {relative_path}")
    created += 1

return created, skipped
```

def print_summary(created, skipped):  
"""Print final repository information."""

```
print("\n")
print("=" * 70)
print("FLYRANK REPOSITORY STRUCTURE CREATED")
print("=" * 70)

print(f"\nRepository:")
print(f"  {REPO_ROOT}")

print(f"\nFiles created : {created}")
print(f"Files skipped : {skipped}")

print("\nNext steps:")
print()
print("  cd", REPO_ROOT)
print()
print("  git status")
print("  git add .")
print('  git commit -m "Initialize FlyRank internship documentation"')
print()
print("Then connect your GitHub repository:")
print()
print("  git remote add origin <YOUR_GITHUB_REPO_URL>")
print("  git branch -M main")
print("  git push -u origin main")
print()
```

# ============================================================

# Main

# ============================================================

def main():

```
print("=" * 70)
print("FlyRank Internship Repository Generator")
print("=" * 70)

print(f"\nScript location:")
print(f"  {Path(__file__).resolve()}")

print(f"\nRepository root:")
print(f"  {REPO_ROOT}")

create_directories()

created, skipped = create_files()

print_summary(created, skipped)
```

if **name** == "**main**":  
main()

````

### Your exact setup

Because the script is already here:

```text
/home/hardik-sankhla/Desktop/flyrank-backend-ai-intern/
└── scripts/
    └── generate-file-structure.py
````

run:

```
cd /home/hardik-sankhla/Desktop/flyrank-backend-ai-intern

python3 scripts/generate-file-structure.py
```

It will detect the script's location automatically and create everything relative to:

```
/home/hardik-sankhla/Desktop/flyrank-backend-ai-intern/
```

So **it won't accidentally create another repository somewhere else**.

Also, I intentionally made it **non-destructive**: if you already have a `README.md`, `.gitignore`, or assignment files in that repo, the generator prints `[SKIP]` and leaves them untouched.


The assignment explicitly allows **Word/Google Doc/notes/PDF/etc.**, and says you can upload a file or provide a public link.

### What I'd recommend for you

Use a repo like:

```
flyrank-ai-internship/
│
├── README.md
│
├── assignments/
│   ├── FL-01-workflow-audit/
│   │   ├── README.md
│   │   ├── workflow-audit.md
│   │   ├── claude-project/
│   │   │   └── instructions.md
│   │   └── evidence/
│   │       └── screenshots/
│   │
│   ├── FL-02-prompting/
│   │   ├── README.md
│   │   ├── prompts.md
│   │   ├── results.md
│   │   └── evidence/
│   │
│   ├── FL-03-...
│   │
│   └── FL-04-automation/
│       ├── README.md
│       ├── workflow/
│       ├── prompts/
│       └── evidence/
│
├── projects/
│   └── ...
│
└── resources/
    └── ...
```

## For **FL-01 specifically**

I'd make the main deliverable:

```
assignments/
└── FL-01-workflow-audit/
    ├── README.md
    ├── workflow-audit.md
    └── evidence/
        ├── claude-project.png
        └── ...
```

### `workflow-audit.md`

This should contain the **actual 1–2 page submission**:

1. Brief introduction
2. Your 15 real tasks
3. Classification + rationale
4. Your 3 selected target tasks
5. “Done well” success definitions
6. Short conclusion

That's much cleaner than a `.txt` file.

### `README.md`

Make this the **landing page for FL-01**:

```
# FL-01 — AI Workflow Audit

## Objective

Map recurring tasks from my real work, study, and
AI engineering activities and identify where AI should
be used, reviewed, collaborated with, or avoided.

## Deliverables

- [Workflow Audit](./workflow-audit.md)
- [Claude Project Configuration](./claude-project/instructions.md)
- Evidence screenshots

## Three Target Tasks

1. AI/ML Technical Research
2. AI/Backend Debugging
3. Technical Workflow Automation
```

Then the GitHub link you submit is simply the FL-01 folder/repo URL.

---

## Why I prefer a repo for **you**

Because you're not doing just one assignment.

You're going to accumulate:

**FL-01 → FL-02 → FL-03 → FL-04 → other assignments → capstone**

And several of your assignments are likely to involve **actual code, prompts, experiments, screenshots, automation workflows and results**.

A repo lets you preserve the evolution:

```
FL-01
  ↓
"I identified my workflow"

FL-02
  ↓
"I improved how I prompt AI"

FL-03
  ↓
"I improved the collaboration"

FL-04
  ↓
"I actually automated the workflow"
```

That makes the internship repository potentially useful **after the internship too**—as a portfolio showing how you actually use AI, rather than merely a folder of certificates.

### One important thing

Don't put **private internship information, private datasets, API keys, credentials, personal emails, internal links, or confidential company material** in a public repository.

For example, your LinkedIn outreach dataset should **not** simply be uploaded because it contains real conversations. Put sanitized/sample data or documentation of the workflow instead.

---

### My recommendation

**Use GitHub + Markdown as the master repository.**

Then for the FlyRank submission:

> **Public GitHub repo → `assignments/FL-01-workflow-audit/` → `README.md`**

And if you want to be extra safe, also upload the rendered **PDF** of the workflow audit to FlyRank. Their portal accepts either a valid public link or an uploaded file.

So you effectively have:

**GitHub = source of truth**  
**PDF = clean formal submission**  
**Screenshots = evidence**

That's the setup I'd use for your entire internship.

Today 2:50 AM

generate a python code so i can generate these files and structure correctly

Absolutely. Since you want to build this as a **long-term FlyRank internship repository**, here's a Python generator that creates the structure cleanly and avoids overwriting existing work.

It will create:

```
flyrank-ai-internship/
├── README.md
├── assignments/
│   ├── FL-01-workflow-audit/
│   │   ├── README.md
│   │   ├── workflow-audit.md
│   │   ├── claude-project/
│   │   │   └── instructions.md
│   │   └── evidence/
│   │       └── screenshots/
│   ├── FL-02-prompting/
│   │   ├── README.md
│   │   ├── prompts.md
│   │   ├── results.md
│   │   └── evidence/
│   ├── FL-03/
│   │   ├── README.md
│   │   └── evidence/
│   └── FL-04-automation/
│       ├── README.md
│       ├── prompts/
│       ├── workflow/
│       └── evidence/
├── projects/
├── resources/
└── .gitignore
```

I also made the generator **idempotent**: if you run it again, it won't destroy files you've already written.

````
from pathlib import Path


# ============================================================
# Configuration
# ============================================================

REPO_NAME = "flyrank-ai-internship"


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
````

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
> """,

```
".gitignore": """# Python
```

**pycache**/  
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

```
"assignments/FL-01-workflow-audit/README.md": """# FL-01 — AI Workflow Audit
```

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

```
evidence/screenshots/
```

## Submission

The final FlyRank submission can reference this directory  
or the repository's corresponding public URL.  
""",

```
"assignments/FL-01-workflow-audit/workflow-audit.md": """# FL-01 — AI Workflow Audit
```

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

```
"assignments/FL-02-prompting/README.md": """# FL-02 — Prompting Fundamentals
```

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

```
"assignments/FL-02-prompting/results.md": """# FL-02 Results
```

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

```
"assignments/FL-03/README.md": """# FL-03
```

**Status:** Not Started

Document the assignment objective, experiments, results,  
evidence, and final reflection here.  
""",

```
"assignments/FL-04-automation/README.md": """# FL-04 — Ship an Automation Workflow
```

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

```
"projects/README.md": """# Projects
```

Supporting projects related to the internship.

Do not include confidential company code or private data.  
""",

```
"resources/README.md": """# Resources
```

Useful references, notes, documentation, and learning  
resources used during the internship.  
""",  
}

# ============================================================

# Generator

# ============================================================

def create_repo():  
root = Path(REPO_NAME)

```
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

    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"[CREATE] {path}")
    created += 1

print("\n" + "=" * 60)
print("Repository created successfully")
print("=" * 60)
print(f"Location : {root.resolve()}")
print(f"Created  : {created} files")
print(f"Skipped  : {skipped} existing files")
print()
print("Next steps:")
print(f"  cd {REPO_NAME}")
print("  git init")
print("  git add .")
print('  git commit -m "Initialize FlyRank internship repository"')
print("  git branch -M main")
print("  git remote add origin <YOUR_GITHUB_REPO_URL>")
print("  git push -u origin main")
```

if **name** == "**main**":  
create_repo()

````

### Run it

Save it as:

```text
create_flyrank_repo.py
````

Then:

```
python create_flyrank_repo.py
```

It will create the complete repository in the **current directory**.

Then:

```
cd flyrank-ai-internship
git init
git add .
git commit -m "Initialize FlyRank internship repository"
```

After you create the GitHub repository:

```
git branch -M main
git remote add origin YOUR_REPO_URL
git push -u origin main
```

One thing I'd **strongly recommend**: don't treat this generated content as permanently final. The FL-01 instructions specifically say the tasks should be genuinely yours, so before submission we should refine the 15 rows with your _actual_ recurring activities and concrete examples rather than making the repository look artificially polished.

/home/hardik-sankhla/Desktop/flyrank-backend-ai-intern/scripts/generate-file-structure.py generate code for this

Yes — since the script itself is at:

```
/home/hardik-sankhla/Desktop/flyrank-backend-ai-intern/scripts/generate-file-structure.py
```

use this version. It creates the repository **inside the existing FlyRank project**, rather than creating another `flyrank-ai-internship` directory wherever you happen to run the script.

````
from pathlib import Path


# ============================================================
# Project Configuration
# ============================================================

# This script lives in:
# /home/hardik-sankhla/Desktop/flyrank-backend-ai-intern/scripts/
#
# Therefore the repository root is the parent of "scripts".

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent


# ============================================================
# Repository Structure
# ============================================================

DIRECTORIES = [
    # FL-01
    "assignments/FL-01-workflow-audit/claude-project",
    "assignments/FL-01-workflow-audit/evidence/screenshots",

    # FL-02
    "assignments/FL-02-prompting/evidence",

    # FL-03
    "assignments/FL-03/evidence",

    # FL-04
    "assignments/FL-04-automation/prompts",
    "assignments/FL-04-automation/workflow",
    "assignments/FL-04-automation/evidence",

    # Supporting material
    "projects",
    "resources",
]


# ============================================================
# Files
# ============================================================

FILES = {

    # --------------------------------------------------------
    # Root README
    # --------------------------------------------------------

    "README.md": """# FlyRank Backend AI Engineering Internship

Repository for documenting my FlyRank internship work,
assignments, experiments, technical implementations,
AI workflows, automation, and supporting evidence.

## Repository Structure

```text
flyrank-backend-ai-intern/
│
├── assignments/
│   ├── FL-01-workflow-audit/
│   ├── FL-02-prompting/
│   ├── FL-03/
│   └── FL-04-automation/
│
├── projects/
├── resources/
├── scripts/
│   └── generate-file-structure.py
│
└── README.md
````

## Assignment Status

|Assignment|Topic|Status|
|---|---|---|
|FL-01|AI Workflow Audit|In Progress|
|FL-02|Prompting Fundamentals|Not Started|
|FL-03|TBD|Not Started|
|FL-04|Ship an Automation Workflow|Not Started|

## Purpose

This repository documents the actual work completed during  
the internship, including:

- workflow audits
- prompts and prompt experiments
- AI-assisted development
- technical research
- backend engineering
- automation workflows
- experiments
- results
- evidence
- reflections and learnings

## Important

Do not commit:

- API keys
- passwords
- credentials
- private datasets
- private conversations
- confidential company information
- proprietary source code  
    """,
    
    # --------------------------------------------------------
    
    # Gitignore
    
    # --------------------------------------------------------
    
    ".gitignore": """# ============================================================
    

# Python

# ============================================================

**pycache**/  
*.py[cod]  
*.pyo  
*.pyd

.venv/  
venv/  
env/

# ============================================================

# Environment / Secrets

# ============================================================

.env  
.env.*  
*.key  
*.pem  
credentials/  
secrets/

# ============================================================

# IDE

# ============================================================

.vscode/  
.idea/

# ============================================================

# OS

# ============================================================

.DS_Store  
Thumbs.db

# ============================================================

# Logs / Temporary

# ============================================================

*.log  
*.tmp

# ============================================================

# Jupyter

# ============================================================

.ipynb_checkpoints/

# ============================================================

# Private / Raw Data

# ============================================================

data/raw/  
data/private/  
private/  
""",

```
# ========================================================
# FL-01
# ========================================================

"assignments/FL-01-workflow-audit/README.md": """# FL-01 — AI Workflow Audit
```

## Objective

Map recurring tasks from my real work, study, technical  
projects, AI engineering activities, and automation work.

The goal is to identify where AI should:

- remain under direct human control
- collaborate with me
- perform delegated work with review
- be fully automated

## Deliverables

- Workflow Audit
- Claude Project Instructions
- Evidence screenshots in `evidence/screenshots/`

## Three Target Tasks

1. AI/ML Technical Research
2. AI/Backend Debugging
3. Technical Workflow Automation

## Evidence

Supporting screenshots and evidence should be placed in:

```
evidence/screenshots/
```

## Submission

The assignment can be submitted through the FlyRank portal  
using the repository link and/or an exported document.  
""",

```
"assignments/FL-01-workflow-audit/workflow-audit.md": """# FL-01 — AI Workflow Audit
```

**Name:** Hardik Sankhla  
**Track:** General AI Fluency  
**Assignment:** FL-01 — AI Workflow Audit

---

## 1. Introduction

This audit maps recurring tasks from my actual workflow,  
including AI engineering, backend development, technical  
research, infrastructure work, automation, studying,  
outreach, and career-related activities.

The purpose is to understand where AI provides useful  
leverage, where human review is necessary, and where  
automation is appropriate.

---

## 2. Recurring Tasks

|#|Real Task|Classification|Rationale|
|---|---|---|---|
|1|Debug Python/FastAPI/AI project errors|Collaborate with AI|AI can analyze logs and suggest fixes, but I need to understand and verify the root cause.|
|2|Research unfamiliar AI/ML concepts|Collaborate with AI|AI can accelerate exploration and explanation, while important claims need verification.|
|3|Design architecture for an AI system|Just me|AI can critique alternatives, but the core architectural decisions depend on my goals and constraints.|
|4|Read and understand technical papers|Collaborate with AI|AI can explain difficult sections while I develop and verify my understanding.|
|5|Build and modify AI models/inference pipelines|Collaborate with AI|AI can assist implementation and debugging, but the resulting system must be tested.|
|6|Maintain local AI/agent infrastructure|Collaborate with AI|AI can assist with Linux, Termux, Docker, runtimes, and dependency problems, but changes require verification.|
|7|Develop personal automation workflows|Delegate to AI with review|AI can generate workflow logic and scripts, but I need to review correctness and failure cases.|
|8|Analyze LinkedIn/outreach data|Fully automate|Structured data can be cleaned, classified, clustered, and summarized automatically, with human review for important cases.|
|9|Write and revise outreach messages|Delegate to AI with review|AI can create personalized drafts, while I verify accuracy before sending.|
|10|Prepare internship/job applications|Delegate to AI with review|AI can tailor applications, but factual claims and final positioning remain my responsibility.|
|11|Study GATE DA concepts|Collaborate with AI|AI can teach concepts and generate practice material, but the learning itself cannot be delegated.|
|12|Solve GATE DA problems independently|Just me|Independent problem solving is the skill being developed.|
|13|Decide which technical project to build|Just me|AI can brainstorm, but project selection depends on my own goals and constraints.|
|14|Write technical documentation|Delegate to AI with review|AI can transform technical notes into documentation, while I verify accuracy.|
|15|Explore unfamiliar technologies|Collaborate with AI|AI can explain and compare technologies, while I test whether they work in my environment.|

---

## 3. Three Target Tasks

### Target Task 1 — AI/ML Technical Research

Investigate an unfamiliar AI/ML research question and produce  
a technically grounded answer.

#### Done Well Means

- The question is clearly defined.
- Established research is separated from speculation.
- Relevant approaches, papers, or systems are identified.
- The underlying mechanisms are explained.
- Limitations and unresolved problems are identified.
- Important claims are supported by reliable sources.
- The final answer directly addresses the original question.

---

### Target Task 2 — AI/Backend Debugging

Diagnose and resolve failures in my AI development  
environments and backend systems.

#### Done Well Means

- The root cause is identified.
- Symptoms are separated from causes.
- The smallest reasonable fix is proposed.
- Unnecessary system changes are avoided.
- The fix is tested.
- The reason the fix works is documented.
- Preventive measures are identified where appropriate.

---

### Target Task 3 — Technical Workflow Automation

Convert repetitive technical or data-processing workflows  
into reliable automated pipelines.

#### Done Well Means

- Expected inputs are handled automatically.
- Outputs have a predictable structure.
- Errors are detected rather than silently ignored.
- Important decisions remain reviewable.
- The workflow can be safely rerun.
- Performance or quality can be measured.
- Manual effort is meaningfully reduced.

---

## 4. Success Criteria

The workflow audit is successful if:

- At least 10 recurring tasks are identified.
- Tasks represent my actual activities.
- Every task has a classification.
- Every classification has a rationale.
- At least two tasks are intentionally marked "Just me".
- Three reusable target tasks are defined.
- Each target task has measurable quality criteria.

---

## 5. Reflection

The main observation from this audit is that AI is most useful  
to me when it acts as a collaborator rather than simply  
replacing the work.

For technical research and engineering, AI can accelerate  
exploration, debugging, implementation, and comparison while  
I retain responsibility for verification and decision-making.

For repetitive structured workflows, greater automation is  
appropriate when inputs, outputs, and failure conditions can  
be clearly defined.

The three target tasks therefore represent three forms of  
AI collaboration:

1. Research and reasoning
2. Technical diagnosis
3. Workflow automation  
    """,
    
    "assignments/FL-01-workflow-audit/claude-project/instructions.md": """# Claude Project Instructions
    

## About Me

I am Hardik Sankhla, a Data Science / AI-focused developer  
and technical researcher.

My work involves:

- AI/ML research
- LLMs and generative AI
- Backend engineering
- Python and FastAPI
- AI inference pipelines
- Linux and infrastructure
- Docker
- AI agents
- Automation
- Data processing
- Technical experimentation
- GATE DA preparation
- Technical projects

## How AI Should Work With Me

Act as a technical collaborator rather than blindly  
completing tasks.

### Priorities

1. Accuracy over confidence.
2. Explain important reasoning and tradeoffs.
3. Clearly distinguish facts from assumptions.
4. Never invent papers, benchmarks, APIs, or technical claims.
5. For debugging, identify the root cause before proposing fixes.
6. Prefer minimal and reversible changes.
7. For research, distinguish established research from speculation.
8. Consider my actual environment and constraints.
9. Challenge incorrect assumptions when evidence supports doing so.
10. Ask for missing technical context when it materially affects the answer.

## Current Target Tasks

### 1. AI/ML Technical Research

Investigate research questions and produce evidence-grounded  
technical conclusions.

### 2. AI/Backend Debugging

Diagnose root causes, propose fixes, and verify solutions  
for real development environments.

### 3. Technical Workflow Automation

Identify repetitive workflows and design reliable automation  
with appropriate human review.  
""",

```
# ========================================================
# FL-02
# ========================================================

"assignments/FL-02-prompting/README.md": """# FL-02 — Prompting Fundamentals
```

**Status:** Not Started

This directory contains prompts, iterations, outputs,  
comparisons, and conclusions from FL-02.

## Files

- `prompts.md`
- `results.md`
- `evidence/`  
    """,
    
    "assignments/FL-02-prompting/prompts.md": """# FL-02 — Prompt Experiments
    

> Add real prompts and iterations here.

## Experiment 1

### Task

TODO

### Initial Prompt

TODO

### Improved Prompt

TODO

### Why It Was Improved

TODO  
""",

```
"assignments/FL-02-prompting/results.md": """# FL-02 — Results
```

## Experiment 1

### Objective

TODO

### Initial Result

TODO

### Improved Result

TODO

### What Improved?

TODO

### What Did Not Improve?

TODO

### Final Prompt

TODO  
""",

```
# ========================================================
# FL-03
# ========================================================

"assignments/FL-03/README.md": """# FL-03
```

**Status:** Not Started

Document:

- assignment objective
- task
- approach
- experiments
- results
- evidence
- reflection
- final conclusions  
    """,
    
    # ========================================================
    
    # FL-04
    
    # ========================================================
    
    "assignments/FL-04-automation/README.md": """# FL-04 — Ship an Automation Workflow
    

**Status:** Not Started

## Objective

Document and implement a real workflow that benefits from  
automation.

## Structure

### prompts/

Prompts used during development.

### workflow/

Automation implementation and configuration.

### evidence/

Screenshots and execution evidence.

## Workflow

TODO

## Before Automation

TODO

## After Automation

TODO

## Results

TODO

## Failure Handling

TODO

## Limitations

TODO

## Reflection

TODO  
""",

```
# ========================================================
# Projects
# ========================================================

"projects/README.md": """# Projects
```

Supporting projects related to the internship.

Only include projects that are appropriate for public  
documentation.

Do not include confidential company code or private data.  
""",

```
# ========================================================
# Resources
# ========================================================

"resources/README.md": """# Resources
```

Useful references, technical documentation, research papers,  
notes, and learning resources used during the internship.  
""",  
}

# ============================================================

# Helper Functions

# ============================================================

def create_directories():  
"""Create all required directories."""

```
print("\nCreating directories...\n")

for directory in DIRECTORIES:
    path = REPO_ROOT / directory

    path.mkdir(
        parents=True,
        exist_ok=True,
    )

    print(f"[DIR]    {path.relative_to(REPO_ROOT)}")
```

def create_files():  
"""Create files without overwriting existing work."""

```
print("\nCreating files...\n")

created = 0
skipped = 0

for relative_path, content in FILES.items():

    path = REPO_ROOT / relative_path

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    # IMPORTANT:
    # Never overwrite existing files.
    if path.exists():
        print(f"[SKIP]   {relative_path}")
        skipped += 1
        continue

    path.write_text(
        content.rstrip() + "\n",
        encoding="utf-8",
    )

    print(f"[CREATE] {relative_path}")
    created += 1

return created, skipped
```

def print_summary(created, skipped):  
"""Print final repository information."""

```
print("\n")
print("=" * 70)
print("FLYRANK REPOSITORY STRUCTURE CREATED")
print("=" * 70)

print(f"\nRepository:")
print(f"  {REPO_ROOT}")

print(f"\nFiles created : {created}")
print(f"Files skipped : {skipped}")

print("\nNext steps:")
print()
print("  cd", REPO_ROOT)
print()
print("  git status")
print("  git add .")
print('  git commit -m "Initialize FlyRank internship documentation"')
print()
print("Then connect your GitHub repository:")
print()
print("  git remote add origin <YOUR_GITHUB_REPO_URL>")
print("  git branch -M main")
print("  git push -u origin main")
print()
```

# ============================================================

# Main

# ============================================================

def main():

```
print("=" * 70)
print("FlyRank Internship Repository Generator")
print("=" * 70)

print(f"\nScript location:")
print(f"  {Path(__file__).resolve()}")

print(f"\nRepository root:")
print(f"  {REPO_ROOT}")

create_directories()

created, skipped = create_files()

print_summary(created, skipped)
```

if **name** == "**main**":  
main()

````

### Your exact setup

Because the script is already here:

```text
/home/hardik-sankhla/Desktop/flyrank-backend-ai-intern/
└── scripts/
    └── generate-file-structure.py
````

run:

```
cd /home/hardik-sankhla/Desktop/flyrank-backend-ai-intern

python3 scripts/generate-file-structure.py
```

It will detect the script's location automatically and create everything relative to:

```
/home/hardik-sankhla/Desktop/flyrank-backend-ai-intern/
```

So **it won't accidentally create another repository somewhere else**.

Also, I intentionally made it **non-destructive**: if you already have a `README.md`, `.gitignore`, or assignment files in that repo, the generator prints `[SKIP]` and leaves them untouched.