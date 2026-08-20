# Current Project State

**Reviewed:** 2026-08-20
**Timezone:** Australia/Sydney
**Confidence:** Evidence-backed summary; unresolved items remain explicit.

## Project snapshot

- **Project:** UG_COSEAT_08 — Portfolio Rescue & Resilient AI Integration
- **Unit:** COS40005, Semester 2 2026
- **Current phase:** Repository discovery and local verification
- **Supervisor:** Dr Naveed Ali
- **Client representative:** Md Shaik Said
- **Delivery direction:** Rescue and modernise an initial set of existing client web applications through local setup, gap analysis, small approved development, testing, defect correction, and an approved deployment lifecycle.
- **Scope status:** All twelve organisation repositories were accessed and verified on 2026-08-20. The four application categories now map to specific repositories, but the mapping is proposed rather than client-confirmed, and priorities, per-application scope, production authority, and acceptance criteria are not yet agreed.

At the first client meeting on 2026-08-13, the client directed the team to begin with four applications: algorithmic trading, lead-generation coupons, property-portfolio calculations, and an Airtasker-like task marketplace. Other applications were mentioned for later, but they are not part of the current working set. On 2026-08-20 the team received and verified access to all twelve repositories in the client's GitHub organisation; every repository was cloned, installed, and tested, and the consolidated evidence is recorded in the [repository state summary](../discovery/2026-08-20-repository-state.md). The proposed mapping is coupons ("CuponZ") to five repositories, the ConnectMyTask marketplace to three, PropCalc to one, and trading to `Project-B`, which currently exists only as a zip archive containing files that look like real credentials. `UGC08-3` remains blocked until the client confirms the mapping and per-application priorities, acceptance criteria, and a realistic semester scope are agreed.

## Team and verified GitHub identities

| Team member | GitHub username | Current ownership note |
|---|---|---|
| Prattay Banik | `prattaybanik03` | Workstream allocation provisional |
| Mohita Mittal | `mohitamittal` | Workstream allocation provisional |
| Cong Huan Nguyen | `CongHuann` | Workstream allocation provisional |
| Unna Nusen | `unninna` | Workstream allocation provisional |
| Le Bao Tran Pham | `plebaotrn` | Workstream allocation provisional |
| Md Mudabbirul Islam Saad | `MudabbirulSaad` | Prepares meeting-minutes records |

Mohita Mittal is the initial Scrum Master. Technical workstreams remain provisional until repository discovery establishes the actual work; stated interests are not assignments or contribution evidence.

## Connected project services

| Service | Role | Location or status |
|---|---|---|
| GitHub | Canonical versioned project record | [ug-coseat-08-project-hub](https://github.com/ug-coseat-08/ug-coseat-08-project-hub), private, default branch `main`; client repositories at [github.com/ug-coseat-08](https://github.com/orgs/ug-coseat-08/repositories), access verified 2026-08-20 |
| Jira | Operational backlog, ownership, status, and delivery flow | [UGC08 backlog](https://ugcoseat08.atlassian.net/jira/software/projects/UGC08/boards/1/backlog) |
| Confluence | Human-readable navigation and collaboration hub | [UG_COSEAT_08 Project Hub](https://ugcoseat08.atlassian.net/wiki/spaces/UGC08/pages/65838/UG_COSEAT_08+Project+Hub) |
| Canvas | Unit requirements, assessment briefs, policy, and submission | Access-controlled university source; do not copy protected content into this repository |

GitHub for Atlassian is installed and restricted to the project repository; its history backfill has completed. Five teammates' Atlassian email addresses are still unavailable, so Jira/Confluence access and assignment cannot yet be completed for everyone.

## Delivery structure

Jira workflow: `Ready` → `In Progress` → `In Review` → `Blocked` → `Done`.

- `UGC08-3`: client-scope gate; currently blocked pending client discovery.
- `UGC08-17`: Semester 1 2027 planning placeholder Feature; due 2027-03-01; it carries no approved implementation scope.
- Preparation, Sprint 1, and Sprint 2 milestone work exists in Jira.
- An Alpha release is a high-level target only; its content and acceptance criteria are unconfirmed.

## Known academic milestones

| Milestone | Due date |
|---|---|
| Research Report | 2026-08-30 |
| Final Team & Project Plan | 2026-09-13 |
| Preparation Contribution Summary | 2026-09-13 |
| Sprint 1 Report & Contribution Summary | 2026-10-11 |
| Sprint 2 Report & Contribution Summary | 2026-11-01 |
| Video presentation and peer review | 2026-11-08 |

Dates should be rechecked against Canvas before submission because Canvas remains authoritative for assessment details.

## Immediate priorities and blockers

1. Privately report the exposed credentials found in `Project-B`, `propcalc`, and `backend` to Md Shaik Said and Ishtiaq Ahmad Anan through Mohita, treating them as compromised and never opening, using, or reproducing the values (RISK-009).
2. Send the client the local-setup milestone update now that repository access and verification are complete, and record the wording actually sent.
3. Hold the proposed client meeting on Tuesday, 25 August 2026 at 8:30 PM and confirm the application-to-repository mapping, per-application priorities, environments, and acceptance evidence.
4. Keep `UGC08-3` blocked until the client confirms priorities and acceptance criteria; convert the candidate improvements identified in the state reports into agreed work only then.
5. Complete the six individual research reports by 2026-08-30; the supervisor offered feedback on questions or draft sections.
6. Obtain the five missing Atlassian email addresses and finish team access/assignment.
7. Keep `UGC08-17` as planning-only until Semester 1 2027 scope and ownership are approved.
