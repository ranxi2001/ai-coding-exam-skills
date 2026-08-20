---
name: prompt-solving
description: Solve AI-assisted coding exams and project-based technical assessments from a README, specification, starter repository, or failure log. Use when Codex must extract exact acceptance contracts, create SDD artifacts, plan a minimal vertical slice, produce staged prompts for a weak coding model, identify model mistakes, generate adversarial tests, correct failures with minimal patches, manage checkpoints, or complete a final delivery audit. Use only where AI assistance is permitted. Do not use for algorithm-only LeetCode problems or for building mock-exam/Judge infrastructure.
---

# Prompt Solving

Turn a long engineering prompt into a controlled, test-backed delivery. Treat the exam README as authoritative and the coding model as an unreliable implementer that needs narrow instructions and objective feedback.

## Select An Operating Mode

- **Direct mode**: Inspect and edit the provided repository, run tests, and complete the task.
- **Relay mode**: Guide a weaker coding model. Produce one copy-ready prompt per round, inspect its response or logs, then issue the next prompt.
- **Analysis mode**: Distill a question, expected solution, failure modes, prompts, and tests without changing code.

State the selected mode. If the user gives a repository, prefer direct mode. If the user is operating a separate exam model, prefer relay mode.

## Load References Selectively

- Read [references/weak-model-prompts.md](references/weak-model-prompts.md) when generating or correcting prompts for another coding model.
- Read [references/question-patterns.md](references/question-patterns.md) when the task resembles a state-machine service, data-cleaning pipeline, batch LLM tool, bill parser, governance service, or security repair.
- Read [references/sdd.md](references/sdd.md) when creating or reviewing `spec.md`, `design.md`, and `tasks.md`.
- Read [references/exam-techniques.md](references/exam-techniques.md) when planning time, checkpoints, context resets, or final submission.
- Read [references/security-repair.md](references/security-repair.md) only for vulnerability auditing or repair tasks.

Do not load every reference by default.

## Run The Exam Workflow

### 1. Preserve The Starting State

Inspect the repository, existing instructions, tests, and version status before editing. Do not overwrite starter fixtures or unrelated user changes. Record the allowed language, entrypoint, start command, port, dependency restrictions, network availability, protected files, time limit, and required deliverables.

If Git is available and exam rules permit it, identify the current baseline and create checkpoints only after verified milestones. If Git is unavailable, use the IDE snapshot facility or copy only the few files being changed.

### 2. Audit Requirements Before Coding

Extract four explicit lists:

1. **Environment**: runtime, entrypoint, commands, ports, paths, dependencies, network, protected files.
2. **Contract**: methods, routes, parameter locations, field names, types, enum spelling, status/exit codes, output files.
3. **Rules**: states, permissions, ordering, precision, idempotency, deadlines, failure side effects.
4. **Acceptance**: one executable proof for each required behavior.

Separate confirmed requirements, ambiguities, assumptions, non-goals, and optional bonuses. Never silently replace an unknown with a conventional default.

### 3. Establish SDD Artifacts

For a non-trivial task, create or maintain:

- `spec.md`: goal, non-goals, exact contract, rules, boundaries, acceptance criteria.
- `design.md`: minimal architecture, data model, state machine, interfaces, failure handling.
- `tasks.md`: vertical, independently testable work items ordered by dependency and value.

Keep these files short enough to reread during the exam. Update them only when the requirement understanding changes; do not rewrite them to justify an accidental implementation.

### 4. Plan A Minimal Vertical Slice

Choose the smallest path that proves the system can start, accept input, execute one core rule, and produce the required output. Defer optional UI polish, speculative abstractions, production infrastructure, and unrequested features.

For every work item define:

- exact scope and permitted files;
- contracts that must remain unchanged;
- success and failure behavior;
- verification command;
- rollback point.

### 5. Control The Coding Model

In relay mode, issue one prompt at a time. Each prompt must contain:

- one main objective;
- exact source-of-truth requirement excerpts;
- allowed and forbidden files;
- literal names and values that cannot change;
- explicit non-goals;
- a concrete command or test proving completion;
- a requirement to show real output.

Ask the model to restate its intended files and constraints before a risky change. Prefer choices and bounded tasks over open-ended architecture questions. Never ask it to “finish the whole project.”

### 6. Verify Each Functional Block

After the minimal slice works, require normal-path and failure-path tests. Then ask the model to attack the current implementation with tests derived line by line from the specification.

Keep diagnostic integrity:

- say “write tests only; do not modify business code”;
- do not weaken assertions to fit the implementation;
- do not change tests and implementation in the same diagnostic step;
- cover invalid input, boundaries, repeated actions, terminal states, exact output contracts, and failure-without-side-effects;
- run the new test, related boundary tests, and existing regression tests.

### 7. Correct Failures Minimally

Use the complete command, failure output, relevant requirement, and current diff. Identify expected behavior, actual behavior, root cause, and the smallest valid change before editing or issuing a repair prompt.

Protect already passing behavior. Reject broad rewrites, dependency upgrades, interface renaming, and unrelated cleanup during correction. After a fix, run in this order:

1. the originally failing test;
2. related boundary tests;
3. the full regression suite.

If regressions increase or the main flow breaks, stop stacking patches and return to the latest verified checkpoint. If three consecutive attempts add no new evidence, start a clean context using only the specification, stable state, reproduction command, and full failure output.

### 8. Audit The Exact Contract

Independently compare the implementation with the requirement for entrypoints, commands, routes, parameter positions, field names, casing, types, enum values, status codes, exit codes, stdout/stderr, empty values, paths, and output filenames.

Business logic that returns the wrong field shape is still incorrect. Fix confirmed mismatches only, then rerun contract and regression tests.

### 9. Close The Submission

Reserve meaningful time for acceptance. From a clean start:

1. run the specified install and start commands;
2. execute one real end-to-end core flow;
3. run all available tests and required static checks;
4. inspect secrets, debug output, temporary files, and unintended changes;
5. map every required item to actual evidence;
6. report completed items, missing items, commands and results, known risks, run instructions, and deliverables.

Do not claim success without observed output. Do not invent completed features.

## Format Relay Responses

When guiding a weak model, return:

```text
Current phase:
Observed evidence:
Likely mistake or risk:
Prompt to send next:
[one copy-ready prompt]
Expected proof:
Rollback condition:
```

Do not bury the next prompt inside a long explanation. Make it usable under exam time pressure.

## Protect Scoring Priorities

Prefer, in order: starts correctly, exact contract, complete core flow, boundary correctness, regression safety, code quality, optional polish. When behind schedule, remove optional scope rather than removing validation of core behavior.

