- **Hierarchical** Architecture to follow same pattern while still allowing FL-02/03/04 to become much more detailed.
## 1. Main repository — `README.md`

This should be the **front page someone sees when they open your GitHub repository**.

___
# FlyRank Backend AI Engineering Internship

> **Intern:** Hardik Sankhla  
> **Program:** FlyRank AI Internship  
> **Track:** Backend AI Engineering  
> **Repository:** Internship Work, Experiments, Assignments & Technical Evidence  
> **Status:** In Progress

---

## About This Repository

This repository documents my work throughout the FlyRank AI internship.

Rather than using this repository only as a place to store assignment submissions, I am using it as a structured record of:

- assignments
- technical experiments
- AI-assisted workflows
- backend engineering work
- AI/ML research
- automation workflows
- prompts and prompt experiments
- implementation decisions
- results and evaluations
- evidence
- reflections and lessons learned

The goal is to preserve not only **what I built**, but also **how I approached the problem, where AI helped, where human judgment was required, and what I learned from the process**.

---

# Internship Progress

| Area                           | Status         |
| ------------------------------ | -------------- |
| Onboarding                     | ✅ Complete     |
| Profile                        | ✅ Complete     |
| FL-01 — AI Workflow Audit      | 🟡 In Progress |
| FL-02 — Prompting Fundamentals | ⬜ Not Started  |
| FL-03                          | ⬜ Not Started  |
| FL-04 — Automation Workflow    | ⬜ Not Started  |
| Main Track Assignments         | 🟡 In Progress |
| Capstone                       | ⬜ Not Started  |

> Status symbols: ✅ Complete · 🟡 In Progress · ⬜ Not Started

---

# Repository Structure

```text
flyrank-backend-ai-intern/
│
├── assignments/
│   │
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
│   ├── FL-03/
│   │   ├── README.md
│   │   └── evidence/
│   │
│   └── FL-04-automation/
│       ├── README.md
│       ├── prompts/
│       ├── workflow/
│       └── evidence/
│
├── projects/
│   └── README.md
│
├── resources/
│   └── README.md
│
├── scripts/
│   └── generate-file-structure.py
│
└── README.md
```

---

# Assignment Index

## General AI Fluency

|Assignment|Description|Status|
|---|---|---|
|[FL-01 — AI Workflow Audit](https://chatgpt.com/c/assignments/FL-01-workflow-audit/)|Map my real workflows and identify where AI should collaborate, delegate, or automate|🟡 In Progress|
|[FL-02 — Prompting Fundamentals](https://chatgpt.com/c/assignments/FL-02-prompting/)|Improve AI interaction on real tasks|⬜ Not Started|
|[FL-03](https://chatgpt.com/c/assignments/FL-03/)|TBD|⬜ Not Started|
|[FL-04 — Ship an Automation Workflow](https://chatgpt.com/c/assignments/FL-04-automation/)|Turn a real workflow into a working automation|⬜ Not Started|

---

# My Three Core AI Workflows

The three workflows identified during FL-01 are:

### 1. AI/ML Technical Research

Investigating unfamiliar AI/ML questions and turning research  
into technically grounded conclusions.

**Example areas:**

- model adaptation
- LLMs
- post-training
- inference
- agents
- AI architectures
- emerging research

---

### 2. AI/Backend Debugging

Using AI as a technical collaborator when diagnosing real  
engineering problems.

**Example areas:**

- Python
- FastAPI
- model loading
- inference pipelines
- Docker
- Linux
- Termux
- dependencies
- databases
- GPU/runtime issues

---

### 3. Technical Workflow Automation

Identifying repetitive workflows and converting them into  
reliable automated systems.

**Example areas:**

- data processing
- outreach analysis
- LLM pipelines
- classification
- automation
- agent workflows
- repository tooling

---

# How I Work With AI

My objective is not to use AI for everything.

I use different levels of AI involvement depending on the task:

```text
                    HUMAN CONTROL
                         │
          ┌──────────────┼──────────────┐
          │              │              │
       Just Me       Collaborate     Delegate
          │              │              │
          │              │              │
       Decisions     Research       Repetitive
       Learning      Debugging      Work
       Judgment      Design         Drafting
          │              │              │
          └──────────────┼──────────────┘
                         │
                    Automation
```

Important decisions, independent learning, and final  
responsibility remain with me.

---

# Evidence Philosophy

For each assignment, I aim to document four things:

### 1. Context : What problem was I trying to solve?
### 2. Process: How did I approach it?

### 3. Result: What did I actually produce?

### 4. Reflection: What worked, what failed, and what did I learn?

This makes the repository a record of the process rather than  
just a collection of final answers.

---

# Repository Conventions

Each assignment should generally contain:

```text
README.md
    ↓
Assignment overview

main deliverable
    ↓
Actual completed work

evidence/
    ↓
Screenshots / supporting proof

experiments/
    ↓
Trials and iterations when necessary

results/
    ↓
Outputs and evaluation when necessary

reflection.md
    ↓
Lessons learned when useful
```

Not every assignment needs every folder.

The structure should grow according to the actual requirements  
of the assignment rather than creating unnecessary files.

---

# Security & Privacy

This repository must not contain:

- API keys
- passwords
- access tokens
- private credentials
- private datasets
- personal authentication information
- confidential company information
- proprietary material that cannot be publicly shared

Sensitive information should be replaced with:

```text
[REDACTED]
```

or with synthetic/example data.

---

# Progress Log

## August 2026

### 2026-08-09

- Created the internship repository structure.
- Started FL-01 workflow audit.
- Identified three reusable AI workflows.
- Began documenting AI collaboration patterns.

---

# Final Internship Outcome

At the end of the internship this repository should provide a  
single view of:

1. What I worked on.
2. What I built.
3. How I used AI.
4. How I evaluated AI output.
5. Which workflows I automated.
6. What technical problems I encountered.
7. How I solved them.
8. What I learned.
9. What I would improve next.

---

## Author

**Hardik Sankhla**

Data Science / AI  
Backend AI Engineering · LLMs · AI Systems · Automation

# 2. Generic assignment `README.md`

This is the template I'd use **inside every assignment folder**.

The key is that you don't have to redesign the README every time.

# FL-XX — Assignment Title

> **Track:** [Track name]  
> **Week:** [Week number]  
> **Status:** 🟡 In Progress  
> **Started:** [YYYY-MM-DD]  
> **Completed:** [YYYY-MM-DD]

---

## 1. Assignment Overview

### Objective

[What is this assignment asking me to accomplish?]

### Why This Matters

[Why is this task relevant to my work or AI workflow?]

### Assignment Requirements

- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

---

# 2. My Real-World Context

Describe the actual situation in which I applied this  
assignment.

### Problem

[What problem/task was I actually working on?]

### Existing Workflow

```
[Current workflow]

Input
  ↓
Step 1
  ↓
Step 2
  ↓
Step 3
  ↓
Output
```

### Constraints

- [Constraint]
- [Constraint]
- [Constraint]

---

# 3. Approach

Explain how I approached the assignment.

### Initial Approach

[Describe the first approach.]

### AI's Role

[Explain what AI was responsible for.]

### My Role

[Explain what I personally decided, verified, implemented,  
or evaluated.]

---

# 4. Implementation / Work

[Put the actual work here or link to the relevant files.]

## Relevant Files

|File|Purpose|
|---|---|
|`[file](./file)`|Description|
|`[file](./file)`|Description|

---

# 5. Experiments / Iterations

If applicable, document how the approach changed.

## Experiment 1

### Hypothesis

[What did I expect?]

### Method

[What did I try?]

### Result

[What happened?]

### Learning

[What did I learn?]

---

## Experiment 2

### Hypothesis

[What changed from Experiment 1?]

### Method

[What did I try?]

### Result

[What happened?]

### Learning

[What did I learn?]

---

# 6. Results

## What Worked

- [Result]
- [Result]
- [Result]

## What Did Not Work

- [Failure]
- [Failure]

## Final Result

[Describe the final outcome.]

---

# 7. Evaluation

### Success Criteria

|   |   |   |
|---|---|---|
|Criterion|Result|Evidence|
|[Criterion]|✅ / ❌ / Partial|[Link]|
|[Criterion]|✅ / ❌ / Partial|[Link]|
|[Criterion]|✅ / ❌ / Partial|[Link]|

---

# 8. Evidence

Supporting evidence is stored in:

```
evidence/
```

### Screenshots

- [Screenshot description](./evidence/example.png)

### Other Evidence

- [Link / artifact]
- [Link / artifact]

---

# 9. What AI Did

Document the actual contribution of AI.

### AI helped with

- [Example]
- [Example]
- [Example]

### AI output that required correction

[Describe any incorrect, incomplete, or misleading AI output.]

### Human verification

[Explain how I verified the final result.]

---

# 10. Reflection

### What Worked Well?

[Reflection]

### What Was Difficult?

[Reflection]

### What Would I Do Differently?

[Reflection]

### What Did I Learn?

[Reflection]

---

# 11. Final Deliverable

The final submission is:

- [Main deliverable](./deliverable.md)
- [Evidence](./evidence/)
- [Supporting files](./)

---

# Status

**Assignment:** [Complete / In Progress / Not Started]

**Submission:** [Submitted / Not Submitted]

**Last Updated:** [YYYY-MM-DD]

---

# 3. A better template for your **FL-01 README**

FL-01 is slightly different because it is an audit rather than a coding project.

I'd therefore use a specialized README rather than forcing the generic template onto it.

# FL-01 — AI Workflow Audit

> **Track:** General AI Fluency  
> **Week:** 1  
> **Status:** 🟡 In Progress  
> **Owner:** Hardik Sankhla

---

## Objective

Map recurring tasks from my actual week across:

- AI engineering
- backend development
- technical research
- infrastructure
- automation
- studying
- outreach
- career development

The objective is to determine where AI should be used,  
where human review is required, and where automation is  
appropriate.

---

# Deliverables

|Deliverable|Location|Status|
|---|---|---|
|Workflow Audit|`[workflow-audit.md](./workflow-audit.md)`|🟡|
|Claude Project Instructions|`[claude-project/instructions.md](./claude-project/instructions.md)`|🟡|
|Evidence|`[evidence/](./evidence/)`|🟡|

---

# Workflow Audit

The complete workflow audit is available here:

[**→ Read Workflow Audit**](./workflow-audit.md)

---

# Three Target Tasks

These are the three tasks selected for reuse in subsequent  
AI Fluency assignments.

## 1. AI/ML Technical Research

Investigate unfamiliar AI/ML questions and produce  
evidence-grounded conclusions.

**Success means:**

- clear problem definition
- evidence-backed claims
- distinction between research and speculation
- technical explanation
- limitations identified
- direct answer to the original question

---

## 2. AI/Backend Debugging

Diagnose and resolve failures in real AI/backend  
development environments.

**Success means:**

- root cause identified
- symptom separated from cause
- minimal fix
- fix verified
- reasoning documented
- prevention considered

---

## 3. Technical Workflow Automation

Convert repetitive technical/data workflows into reliable  
automation.

**Success means:**

- predictable inputs
- predictable outputs
- error handling
- rerunnable workflow
- measurable quality
- reduced manual work

---

# AI Collaboration Model

The audit identified four useful levels of AI involvement:

|   |   |
|---|---|
|Level|Meaning|
|**Just Me**|AI should not perform the core task|
|**Collaborate**|AI and I work together|
|**Delegate + Review**|AI performs the task but I verify the result|
|**Automate**|The workflow can execute with limited human intervention|

---

# Evidence

Evidence for this assignment is stored under:

```
evidence/
└── screenshots/
```

Examples:

- configured Claude Project
- workflow examples
- relevant outputs

---

# Connection to Future Assignments

This assignment establishes the three real workflows that  
will be reused later:

```
FL-01
Workflow identification
       │
       ▼
FL-02
Prompt improvement
       │
       ▼
FL-03
AI collaboration improvement
       │
       ▼
FL-04
Workflow automation
```

The purpose is therefore not only to complete FL-01, but to  
create a foundation for the following assignments.

---

# Reflection

The most important observation from this audit is that AI  
should not automatically replace every task.

For research and engineering, AI is most valuable as a  
collaborator that accelerates exploration, debugging,  
implementation, and evaluation.

For repetitive structured workflows, automation becomes  
appropriate when the process and failure conditions can be  
defined clearly.

---

# Submission

**Final deliverable:** `[workflow-audit.md](./workflow-audit.md)`

**Evidence:** `[evidence/](./evidence/)`

**Claude Project:** `[claude-project/](./claude-project/)`

**Status:** 🟡 Ready for final review

---

## 4. How I want you to grow the repo

Don't create 50 empty files now.

Start with:

```
flyrank-backend-ai-intern/
│
├── README.md                         ← master dashboard
│
├── assignments/
│   │
│   ├── FL-01-workflow-audit/
│   │   ├── README.md                ← assignment dashboard
│   │   ├── workflow-audit.md        ← actual submission
│   │   ├── claude-project/
│   │   └── evidence/
│   │
│   ├── FL-02-prompting/
│   │   └── README.md
│   │
│   ├── FL-03/
│   │   └── README.md
│   │
│   └── FL-04-automation/
│       └── README.md
│
├── projects/
│   └── README.md
│
├── resources/
│   └── README.md
│
└── scripts/
    └── generate-file-structure.py
```

Then **grow each assignment only when you actually do the work**.

For example, FL-04 might eventually become:

```
FL-04-automation/
│
├── README.md
│
├── problem.md
├── before.md
├── after.md
│
├── prompts/
│   ├── research-prompt.md
│   ├── implementation-prompt.md
│   └── evaluation-prompt.md
│
├── workflow/
│   ├── README.md
│   ├── workflow.json
│   └── src/
│
├── results/
│   ├── evaluation.md
│   └── metrics.md
│
├── evidence/
│   └── screenshots/
│
└── reflection.md
```

That gives you a **progressive structure** rather than prematurely inventing a giant repository.