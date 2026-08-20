# AI Coding Exam Skills

[![Validate Skills](https://github.com/ranxi2001/ai-coding-exam-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/ranxi2001/ai-coding-exam-skills/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/release/ranxi2001/ai-coding-exam-skills)](https://github.com/ranxi2001/ai-coding-exam-skills/releases)
[![License](https://img.shields.io/github/license/ranxi2001/ai-coding-exam-skills)](LICENSE)
[![Stars](https://img.shields.io/github/stars/ranxi2001/ai-coding-exam-skills?style=flat)](https://github.com/ranxi2001/ai-coding-exam-skills/stargazers)

**Open-source skills for AI-assisted coding exams and project-based technical assessments.**

[中文 README](README.md) · [Latest Release](https://github.com/ranxi2001/ai-coding-exam-skills/releases/latest) · [Issues](https://github.com/ranxi2001/ai-coding-exam-skills/issues)

AI Coding Exam Skills turns a long assessment README into a controlled engineering workflow: lock the contract, create SDD artifacts, plan a minimal vertical slice, guide a weaker coding model one prompt at a time, attack the implementation with tests, and close with minimal fixes, regression checks, and a final delivery audit.

> Use this project only where AI assistance is explicitly permitted. It does not provide official company question banks, hidden test cases, or internal scoring rules.

## Why

AI coding assessments measure more than code generation:

- Extracting exact acceptance criteria from a requirements document
- Making scope and architecture trade-offs under a time limit
- Keeping a coding model aligned with field, state, API, and error contracts
- Designing boundary tests that attack the current implementation
- Repairing failures from real logs without breaking passing behavior
- Preserving stable checkpoints and explaining engineering decisions

## What's Included

### `prompt-solving`

The only released skill in the current version. It supports three operating modes:

| Mode | Use it when |
| --- | --- |
| **Direct** | The agent can access the task repository and edit/verify code directly |
| **Relay** | You operate a weaker coding model in another window and need one copy-ready prompt per round |
| **Analysis** | You want to distill a task, solution, failure modes, tests, and prompts without editing code |

Included reference patterns cover:

- Multi-client state-machine and order systems
- Web data-cleaning pipelines
- Batch LLM inference consoles
- Heterogeneous Excel billing parsers
- In-memory governance, budget, and idempotency services
- Security auditing and minimal vulnerability repairs

## Core Workflow

```text
Read the task
    -> Lock the exact contract
    -> Create SDD artifacts
    -> Plan a minimal vertical slice
    -> Implement one verifiable block
    -> Generate adversarial tests
    -> Apply the smallest valid fix
    -> Run regression checks
    -> Save a stable checkpoint
    -> Audit the final delivery
```

Core principles: **spec first, one objective per round, separate tests from implementation, prefer evidence, and keep delivery reversible.**

## Quick Start

```bash
git clone https://github.com/ranxi2001/ai-coding-exam-skills.git
cd ai-coding-exam-skills
```

Install for Codex at user scope:

```bash
cp -R skills/prompt-solving ~/.codex/skills/prompt-solving
```

Install for Claude Code at user scope:

```bash
cp -R skills/prompt-solving ~/.claude/skills/prompt-solving
```

You can also place `skills/prompt-solving` in the project-level skill directory supported by your coding tool.

## Use It

Explicit invocation:

```text
Use $prompt-solving to analyze this AI Coding exam task and guide the coding model through implementation, testing, and correction.
```

Relay mode keeps every round in a copy-friendly format:

```text
Current phase:
Observed evidence:
Likely mistake or risk:
Prompt to send next:
[one copy-ready prompt]
Expected proof:
Rollback condition:
```

## Repository Map

```text
ai-coding-exam-skills/
├── skills/
│   └── prompt-solving/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       └── references/
├── references/              # Research notes and source records
├── scripts/                 # Local repository checks
└── .github/workflows/       # CI validation
```

## Validate Locally

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_skills.py
```

CI also runs the official Skill validator and repository reference checks on every push and pull request.

## Roadmap

- [x] `prompt-solving` v0.1.0
- [ ] More distilled engineering question patterns
- [ ] Reusable task-spec and test-case templates
- [ ] `mock-coding-exam` project for local practice
- [ ] Optional strong-model Judge and trajectory scoring

The mock-exam project and Judge are intentionally out of scope for the current release so the solving workflow can stabilize independently from execution and scoring infrastructure.

## Contributing

Contributions of public task patterns, weak-model failure cases, prompt templates, boundary tests, and documentation improvements are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) first. Do not submit confidential question text, hidden answers, personal information, tokens, or secrets, and do not present personal reports as official company policy.

## License

[MIT](LICENSE) © 2026 ranxi2001

