# Maintenance Playbooks

These procedures keep the project hub coherent. In every playbook, separate facts from proposals and record the evidence source.

## Record a meeting

1. Create a dated Markdown file in the correct `meeting-minutes/` folder using the established naming pattern.
2. Record date, purpose, attendees, absentees, agenda, important discussion, decisions, and actions.
3. Preserve exact attribution and mark unclear statements as unresolved.
4. Add the record to the matching index in `MEETINGS.md`.
5. Promote accepted choices to `DECISIONS.md`, needs to `REQUIREMENTS.md`, exposures to `RISKS.md`, and owned actions to Jira.
6. Keep source audio/video and transcripts local and untracked.

## Complete first client discovery

1. Start from the unanswered questions in `PROJECT_INTAKE.md` and blocker `UGC08-3`.
2. Confirm application inventory, repositories, environments, access, stakeholders, problems, priorities, constraints, acceptance evidence, and authorised testing boundaries.
3. Record concise client minutes and named decisions/actions.
4. Update intake, requirements, decisions, risks, and the current-state summary with explicit evidence.
5. Resolve or reframe `UGC08-3` only to the extent supported by the meeting.
6. Break approved outcomes into ready Jira work; leave unapproved ideas provisional.

## Add or change a requirement

1. Assign the next repository requirement ID using the existing format.
2. State the need in testable language and label its status.
3. Record source, date, owner/stakeholder, rationale, and acceptance evidence where known.
4. Link the source meeting and delivery Jira item.
5. Check for affected decisions and risks.

## Record a decision

1. Confirm that a choice was actually accepted by an authorised person or team process.
2. Add the next decision ID, date, status, context, choice, rationale, consequences, and evidence.
3. Link affected requirements, risks, meetings, and Jira work.
4. Supersede old decisions explicitly; never silently rewrite history.

## Add or update a risk

1. Describe cause, uncertain event, and impact rather than only the symptom.
2. Record likelihood, impact, mitigation, contingency, owner, and status.
3. Create or link a Jira action when mitigation requires work.
4. Review after relevant meetings, decisions, or delivery changes.

## Make a repository change

1. Locate the authority using `REPOSITORY_MAP.md`.
2. Use a short-lived Jira-keyed branch where available.
3. Change the canonical record first and keep the diff focused.
4. Update summaries only where the canonical change affects them.
5. Run the project validator and any task-specific checks.
6. Open a linked pull request with evidence and a human reviewer.

## Maintain Jira and Confluence

1. Jira holds execution state; Confluence holds navigation and readable summaries.
2. Link Jira items to the relevant GitHub record or pull request.
3. Update Confluence when navigation, onboarding, or a shared summary changes.
4. Do not copy an entire canonical record into Confluence.
5. Check team access after membership changes; never invent missing email addresses.

## Prepare an assessment milestone

1. Recheck the due date and brief in Canvas.
2. Create Jira work early enough for human review and submission contingency.
3. Gather attributable evidence throughout the period.
4. Validate citations, contribution claims, AI disclosure, format, and submission ownership.
5. Do not store protected Canvas material in the repository.

## Plan Semester 1 2027 handover

1. Use `UGC08-17` as the planning container.
2. Capture only evidence-backed carry-over: known debt, unresolved decisions, setup guidance, operational risks, and reproducible verification steps.
3. Label proposed future work as proposed and include its source.
4. Do not assign future students or promise implementation without approval.

## Validate the project hub

Run:

```powershell
python .agents/skills/ug-coseat-08-project/scripts/validate_project_hub.py
git diff --check
git status --short
```

Fix errors. Review warnings and retain them when they accurately describe an unresolved project condition.
