---
name: ug-coseat-08-project
description: Maintains the UG_COSEAT_08 project hub consistently across GitHub, Jira, and Confluence. Use when recording meetings, requirements, decisions, risks, team details, research or assessment evidence, AI use, Jira-linked work, repository operations, or Semester 1 2027 handover planning.
---

# UG_COSEAT_08 Project Maintenance

## Quick start

1. Read `AGENTS.md`.
2. Read `knowledge-base/CURRENT_STATE.md` and `knowledge-base/project.json`.
3. Read `knowledge-base/PLAYBOOKS.md`, then the authoritative root record for the task.
4. Make the smallest evidence-backed change that keeps related records consistent.
5. Run `python .agents/skills/ug-coseat-08-project/scripts/validate_project_hub.py`.

All paths are relative to the repository root.

## Choose the correct record

- Project identity and entry questions: `PROJECT_INTAKE.md`
- People, ownership, and verified identities: `TEAM.md`
- Confirmed or provisional needs: `REQUIREMENTS.md`
- Accepted choices and rationale: `DECISIONS.md`
- Threats, mitigations, owners, and status: `RISKS.md`
- Meeting standards and indexes: `MEETINGS.md`
- Supervisor/group/client evidence: `meeting-minutes/`
- Contribution and review rules: `CONTRIBUTING.md`
- Security and data handling: `SECURITY.md`
- AI disclosure evidence: `AI_USAGE_LOG.md`
- Current summary and service map: `knowledge-base/`

See `knowledge-base/REPOSITORY_MAP.md` for cross-update rules and `knowledge-base/WAYS_OF_WORKING.md` for the operating model.

## Standard workflow

1. Classify each input as confirmed fact, decision, proposal, provisional assumption, action, risk, or unknown.
2. Capture who supplied it, when, and where the evidence lives.
3. Update the authoritative record first; update summaries and indexes second.
4. Link affected Jira keys using `UGC08-N` when they exist.
5. Check downstream effects on requirements, decisions, risks, meetings, ownership, and milestones.
6. Review for unsupported claims, misattribution, secrets, and protected material.
7. Add or update the AI disclosure when AI materially shaped the output.
8. Run the validator and review the diff.

## Guardrails

- Do not resolve `UGC08-3` without dated client evidence.
- Do not convert `UGC08-17` into implementation scope without approval and evidence.
- Do not infer work contribution from authorship, attendance, Git history, or task assignment alone.
- Do not commit raw audio/video, transcripts, credentials, private client data, or protected course content.
- Do not overwrite uncertainty. Use explicit status labels and retain the source of truth.
- Do not copy large canonical records into Confluence or the knowledge base; link and summarize them.

## Maintenance freshness

When a material fact changes:

1. Update the canonical root record.
2. Update `knowledge-base/CURRENT_STATE.md` and `knowledge-base/project.json` if the fact is represented there.
3. Set their review date to the actual review date.
4. Add the evidence link, meeting record, decision ID, or Jira key.

Warnings from the validator may represent intentional unknowns. Keep them visible until evidence resolves them.
