# Ways of Working

## One project, three connected tools

- **Jira** owns executable work: priority, assignee, status, sprint, blockers, and due dates.
- **GitHub** owns versioned project records, code when available, branches, reviews, and evidence of change.
- **Confluence** provides a readable hub, onboarding, agendas, and links. It should summarize and link to canonical GitHub records rather than fork them.

Use the Jira key everywhere a delivery item crosses tools. For example: branch `docs/UGC08-12-client-minutes`, commit `UGC08-12 record client decisions`, pull request `[UGC08-12] Record client discovery`, and a Confluence link labelled `UGC08-12`.

## Work lifecycle

Jira workflow: `Ready` → `In Progress` → `In Review` → `Done`. Use `Blocked` when the assignee cannot make meaningful progress without external input or a prerequisite.

### Definition of Ready

A normal delivery item is ready when it has:

- a clear outcome and owner;
- evidence or source context;
- explicit boundaries and dependencies;
- acceptance checks that a reviewer can evaluate; and
- no unresolved client-scope assumption hidden as fact.

Discovery tasks may instead be ready with a precise question and required evidence. Implementation dependent on client scope is not ready while `UGC08-3` is blocked.

### Definition of Done

Work is done when:

- the stated outcome and acceptance checks are satisfied;
- the change is reviewed by a human other than the author where practical;
- evidence or verification is recorded;
- related requirements, decisions, risks, meetings, and Jira state are consistent;
- no credentials, private data, protected course material, raw recordings, or transcripts are committed; and
- material AI assistance is disclosed and human-verified.

## GitHub collaboration

Use short-lived, focused branches and pull requests. Keep unrelated edits separate. Link the Jira key, explain why the change is needed, include verification evidence, and request a human review. Every contributor uses their own verified identity. Never infer contribution percentages or authorship for someone else.

## Meetings and evidence

Use one concise minutes standard for supervisor, group, and client meetings. Record date, attendees, absentees, agenda, important discussion, decisions, and actions with owners and dates where agreed. Prepare and file the reviewed Markdown record by Sunday. Raw media and transcripts remain local-only.

Meeting discussion is not automatically a decision or requirement. Promote it into `DECISIONS.md` or `REQUIREMENTS.md` only when the evidence supports that classification.

## Review and contribution evidence

Evidence should be contemporaneous and attributable: pull requests, reviewed documents, meeting actions, Jira history, commits, or other verifiable artefacts. Task assignment is not proof of completion, attendance is not proof of contribution, and Git history alone may not capture non-code work.

## AI use

Before material AI use, ensure the intended use is consistent with supervisor/client expectations. Log the tool, date, purpose, meaningful prompt or method, how the team modified the output, how it was verified, the responsible student, and confirmation status. The responsible student must understand and be able to defend the final work.

## Security and data handling

Use least privilege. Do not commit secrets, `.env` files, client datasets, personally identifying information, or protected course content. Do not test a client system without explicit authorisation and an agreed scope. If sensitive material is exposed, stop sharing it, preserve evidence safely, notify the appropriate owner, and follow `SECURITY.md`.

## Semester 1 2027 handover

Current work may improve documentation, maintainability, reproducibility, and a future backlog. It must not manufacture Semester 1 2027 requirements. `UGC08-17` remains a planning placeholder until scope, owner, timing, and approval evidence exist.
