# Repository Map

Use this map to update one authoritative record and then its necessary dependants, rather than duplicating facts across the repository.

## Canonical project records

| Path | Owns | Update when | Common cross-updates |
|---|---|---|---|
| `README.md` | Project entry point and navigation | Priorities, tools, or repository structure materially change | `CURRENT_STATE.md`, relevant canonical record |
| `PROJECT_INTAKE.md` | Initial project context and unanswered discovery questions | Client context or intake answers become attributable | `REQUIREMENTS.md`, `RISKS.md`, meeting minutes |
| `TEAM.md` | Membership, identities, ownership, and role status | A person, verified identity, or agreed ownership changes | Jira assignment/access, `CURRENT_STATE.md` |
| `REQUIREMENTS.md` | Confirmed and provisional project needs | A requirement is discovered, changed, accepted, or rejected | Source minutes, Jira delivery item, decision/risk |
| `DECISIONS.md` | Accepted choices, rationale, and consequences | The team accepts, supersedes, or reverses a material choice | Requirement/risk, Jira item, relevant minutes |
| `RISKS.md` | Risk statement, impact, likelihood, mitigation, owner, and status | Exposure or mitigation materially changes | Jira action, decision, meeting evidence |
| `MEETINGS.md` | Meeting standard and minutes indexes | A meeting record is added or the standard changes | Matching folder record, actions in Jira |
| `meeting-minutes/supervisor/` | Dated supervisor evidence | A supervisor meeting is verified | `MEETINGS.md`, decisions/actions/risks |
| `meeting-minutes/group/` | Dated internal team evidence | A group meeting is verified | `MEETINGS.md`, Jira ownership/actions |
| `meeting-minutes/client/` | Dated client discovery and approval evidence | A client meeting is verified | `MEETINGS.md`, intake, requirements, decisions, risks, Jira gate |
| `CONTRIBUTING.md` | Branch, commit, pull request, review, and evidence rules | The collaboration workflow changes | PR/issue templates, `WAYS_OF_WORKING.md` |
| `SECURITY.md` | Credential, private-data, testing, and incident rules | Security constraints or reporting paths change | Risks, contribution guidance |
| `AI_USAGE_LOG.md` | Evidence of material AI assistance and human verification | AI materially shapes a deliverable or project record | The affected deliverable and its reviewer evidence |

## Agent and knowledge infrastructure

| Path | Purpose |
|---|---|
| `AGENTS.md` | Repository-wide instructions and authority hierarchy for agents |
| `.agents/skills/ug-coseat-08-project/SKILL.md` | Reusable maintenance workflow for this project |
| `.agents/skills/ug-coseat-08-project/scripts/validate_project_hub.py` | Deterministic checks for structure, links, identifiers, machine context, and sensitive tracked files |
| `knowledge-base/CURRENT_STATE.md` | Reviewed, concise status summary |
| `knowledge-base/project.json` | Machine-readable stable context |
| `knowledge-base/WAYS_OF_WORKING.md` | Team operating model |
| `knowledge-base/PLAYBOOKS.md` | Procedures for common project events |

## GitHub workflow support

- `.github/PULL_REQUEST_TEMPLATE.md` prompts for Jira linkage, evidence, testing, and reviewer checks.
- `.github/ISSUE_TEMPLATE/project-task.yml` captures repository-side project tasks where a GitHub issue is useful.
- `.github/ISSUE_TEMPLATE/bug-report.yml` captures reproducible problems.
- `.github/ISSUE_TEMPLATE/config.yml` controls issue-template behaviour.

Jira owns operational delivery status. GitHub issues are optional technical collaboration records and should link back to the Jira key instead of creating a competing backlog.

## Local-only evidence

Raw recordings and transcripts may exist locally for preparing verified minutes, but must stay ignored and untracked. Only concise, reviewed Markdown minutes belong in Git. Never move protected Canvas material into the repository merely to make it available to an agent.
