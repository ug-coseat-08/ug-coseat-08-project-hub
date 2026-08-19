# UG_COSEAT_08 Knowledge Base

This folder gives people and agents a compact, maintained view of the project. It is an index and operating aid, not a replacement for the canonical records in the repository root.

## Start here

- [Current state](CURRENT_STATE.md) — what is known now, what is blocked, and where the connected services live.
- [Repository map](REPOSITORY_MAP.md) — which file owns each kind of information and what else changes with it.
- [Ways of working](WAYS_OF_WORKING.md) — the team's Jira, GitHub, Confluence, review, meeting, AI, and security conventions.
- [Playbooks](PLAYBOOKS.md) — repeatable procedures for common maintenance tasks.
- [Machine-readable project context](project.json) — stable facts that tools can validate or consume.

## Knowledge rules

1. Root project records remain authoritative; this folder summarizes and routes.
2. Every material claim needs a source, owner, date, or explicit uncertainty status.
3. `Confirmed`, `Provisional`, `Proposed`, `Pending`, and `TBD` are different states and must not be collapsed.
4. Dated client and supervisor evidence outranks undated summaries.
5. GitHub stores the durable versioned record, Jira tracks execution, and Confluence provides a readable project hub.

## Freshness protocol

When a canonical fact changes, update the matching knowledge-base summary in the same pull request. Change the `Reviewed` date only after checking the whole affected section, not for cosmetic edits. Run the project-hub validator before review.
