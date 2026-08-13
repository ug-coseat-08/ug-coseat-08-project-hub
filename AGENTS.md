# UG_COSEAT_08 Agent Guide

## Purpose

This repository is the project operations and evidence hub for UG_COSEAT_08. It currently contains project records, not the client's application source code. Keep it accurate enough that a new team member or agent can understand the project without relying on private chat history.

## Required skill

For any project maintenance task, read and follow `.agents/skills/ug-coseat-08-project/SKILL.md` first. Use its knowledge-base routing and validator before declaring work complete.

## Fact and authority order

When records disagree, use this order and document the conflict instead of silently choosing:

1. The team's latest explicit instruction for the current task.
2. Dated, attributable client or supervisor evidence.
3. Accepted entries in `DECISIONS.md` and confirmed entries in `REQUIREMENTS.md`.
4. Dated meeting minutes and Jira history.
5. `RISKS.md`, `PROJECT_INTAKE.md`, and `TEAM.md`.
6. Summaries in `knowledge-base/` and Confluence.

The root Markdown files are canonical project records. Jira is the operational work tracker. Confluence is the navigation and collaboration layer. GitHub is the durable versioned record.

## Knowledge routing

- Start with `knowledge-base/CURRENT_STATE.md` and `knowledge-base/project.json`.
- Use `knowledge-base/REPOSITORY_MAP.md` to find the authoritative file.
- Use `knowledge-base/WAYS_OF_WORKING.md` for team workflow and quality rules.
- Use `knowledge-base/PLAYBOOKS.md` for repeatable maintenance procedures.
- Read the relevant root record before changing any summary.

## Non-negotiable guardrails

- Do not invent client scope, architecture, deadlines, acceptance criteria, meeting attendance, decisions, or contribution evidence.
- Treat `UGC08-3` as the client-scope gate until documented client discovery resolves it.
- Treat `UGC08-17` as a Semester 1 2027 planning placeholder, not approved implementation scope.
- Preserve named attribution and distinguish `Confirmed`, `Provisional`, `Proposed`, `Pending`, and `TBD`.
- Never commit credentials, private client data, raw meeting recordings, transcripts, or protected course material.
- Use Jira issue keys in branches, commits, pull requests, and related records where available.
- Use ISO dates (`YYYY-MM-DD`) in the Australia/Sydney timezone.
- Log material AI assistance in `AI_USAGE_LOG.md`; human owners must review, modify as needed, understand, and verify the output.

## Completion checklist

Before finishing a maintenance change:

1. Update the canonical record before its summaries or indexes.
2. Add source/evidence and status where a fact is not yet confirmed.
3. Cross-update linked decisions, risks, requirements, meetings, or Jira references.
4. Check links and avoid duplicating authoritative content unnecessarily.
5. Run `python .agents/skills/ug-coseat-08-project/scripts/validate_project_hub.py`.
6. Review `git diff` for attribution, secrets, unsupported claims, and unrelated edits.
