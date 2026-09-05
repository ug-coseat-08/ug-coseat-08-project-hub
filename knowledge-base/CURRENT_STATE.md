# Current Project State

**Reviewed:** 2026-09-05
**Timezone:** Australia/Sydney
**Confidence:** Evidence-backed summary; unresolved items remain explicit.

## Project snapshot

- **Project:** UG_COSEAT_08 — Portfolio Rescue & Resilient AI Integration
- **Unit:** COS40005, Semester 2 2026
- **Current phase:** Sprint Zero planning and ConnectMyTask pre-sprint work
- **Supervisor:** Dr Naveed Ali
- **Client representative:** Md Shaik Said
- **Delivery direction:** Rescue and modernise an initial set of existing client web applications through local setup, gap analysis, small approved development, testing, defect correction, and an approved deployment lifecycle.
- **Scope status:** All twelve organisation repositories were accessed and verified on 2026-08-20. On 2026-08-25 the client prioritised ConnectMyTask and CuponZ for the two Semester 2 sprints, with Sprint 1 for development and Sprint 2 for testing and readiness assessment. The exact repository mapping, accepted improvement list, minimum alpha/readiness evidence, development access, and operational controls remain pending.

At the first client meeting on 2026-08-13, the client directed the team to begin discovery across four applications: algorithmic trading, lead-generation coupons, property-portfolio calculations, and an Airtasker-like task marketplace. On 2026-08-20 the team received and verified access to all twelve repositories in the client's GitHub organisation; every repository was cloned, installed, and tested, and the consolidated evidence is recorded in the [repository state summary](../discovery/2026-08-20-repository-state.md). The proposed mapping is coupons ("CuponZ") to five repositories, the ConnectMyTask marketplace to three, PropCalc to one, and trading to `Project-B`, which currently exists only as a zip archive containing files that look like real credentials.

At the second client meeting on 2026-08-25, Md Shaik Said selected ConnectMyTask and CuponZ as the current semester priorities because they are comparatively mature and were previously deployed. PropCalc and Project-B were deferred from the current semester priority. The client authorised the team to propose replacing CuponZ's legacy stack while preserving its approved lead-generation functionality, and directed ConnectMyTask toward international use with country-appropriate forms, currencies, and payment options. Sprint 1 is for development on both applications; Sprint 2 is for cross-executed functional testing, defect correction, and readiness evidence, followed by a production go/no-go decision. `UGC08-3` remains blocked until the precise improvement list, repository boundary, acceptance evidence, and client/supervisor minimum outcome are confirmed.

At the 2026-08-27 supervisor meeting, Dr Naveed Ali directed the team to begin work by the following week and to maintain separate Jira boards and GitHub project workspaces for ConnectMyTask and CuponZ. The team then adopted a provisional sequential working plan: all six members will begin with ConnectMyTask and move together to CuponZ. This is a planning choice, not approved product scope or contribution evidence; week targets and backlog contents remain subject to estimates, client review, and `UGC08-3`. The team needs one team plan, while the supervisor is awaiting unit-convener guidance on whether the two products require one combined project plan or two separate plans.

At the 2026-09-03 supervisor meeting, Dr Naveed Ali relayed the unit convener's guidance that multiple products may be managed in either one clearly partitioned Jira board or separate boards, while each sprint still has one combined report. Work before Week 7 should remain in the backlog or Sprint Zero; the official sprints run in Weeks 7–9 and 10–12. The supervisor reviewed the team's ConnectMyTask-first sequence and its three provisional work pairs, with ConnectMyTask targeted for the end of the term break before the team concentrates on CuponZ. One team and project-plan submission is required, containing a complete separate project-plan section for each product. These planning clarifications do not resolve the client-scope gate: supported countries, mobile scope, accepted improvements, measurable criteria, and minimum outcomes remain pending.

## Team and verified GitHub identities

| Team member | GitHub username | Current ownership note |
|---|---|---|
| Prattay Banik | `prattaybanik03` | ConnectMyTask country/currency and payments/payouts pair with Saad; ticket allocation provisional |
| Mohita Mittal | `mohitamittal` | Initial Scrum Master; ConnectMyTask Direct Hire and Reviews pair with Unna |
| Cong Huan Nguyen | `CongHuann` | ConnectMyTask registration/login and KYC/identity pair with Le |
| Unna Nusen | `unninna` | ConnectMyTask Direct Hire and Reviews pair with Mohita |
| Le Bao Tran Pham | `plebaotrn` | ConnectMyTask registration/login and KYC/identity pair with Cong |
| Md Mudabbirul Islam Saad | `MudabbirulSaad` | Meeting-minutes records; ConnectMyTask country/currency and payments/payouts pair with Prattay |

Mohita Mittal is the initial Scrum Master. DEC-016 provides the ConnectMyTask-first sequence and the 2026-09-03 meeting records three provisional pairs, but ticket-level owners, reviewers, and CuponZ workstreams remain pending. Stated interests, attendance, and assignment are not completion evidence.

## Connected project services

| Service | Role | Location or status |
|---|---|---|
| GitHub | Canonical versioned project record | [ug-coseat-08-project-hub](https://github.com/ug-coseat-08/ug-coseat-08-project-hub), private, default branch `main`; client repositories at [github.com/ug-coseat-08](https://github.com/orgs/ug-coseat-08/repositories), access verified 2026-08-20 |
| Jira | Operational backlog, ownership, status, and delivery flow | [Current UGC08 backlog](https://ugcoseat08.atlassian.net/jira/software/projects/UGC08/boards/1/backlog); ConnectMyTask backlog shown on 2026-09-03; unit permits either one clearly partitioned board or separate boards, with final structure pending |
| Confluence | Human-readable navigation and collaboration hub | [UG_COSEAT_08 Project Hub](https://ugcoseat08.atlassian.net/wiki/spaces/UGC08/pages/65838/UG_COSEAT_08+Project+Hub) |
| Canvas | Unit requirements, assessment briefs, policy, and submission | Access-controlled university source; do not copy protected content into this repository |

GitHub for Atlassian is installed and restricted to the project repository; its history backfill has completed. Five teammates' Atlassian email addresses are still unavailable, so Jira/Confluence access and assignment cannot yet be completed for everyone.

## Delivery structure

Jira workflow: `Ready` → `In Progress` → `In Review` → `Blocked` → `Done`.

- `UGC08-3`: client-scope gate; still blocked pending review of the detailed ConnectMyTask/CuponZ improvement list, repository boundary, and acceptance evidence.
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

1. Follow up privately on the exposed credentials in `Project-B`, `propcalc`, `backend`, and reachable ConnectMyTask history; the client acknowledged the Project-B concern on 2026-08-25, but rotation and remediation remain unverified (RISK-009).
2. Send Md Shaik Said and Ishtiaq Ahmad Anan the consolidated audit and a precise proposed improvement list for ConnectMyTask and CuponZ; record the wording and their review.
3. Confirm the accepted repository boundary, CuponZ replatforming scope, ConnectMyTask country/payment matrix, detailed acceptance evidence, and the minimum outcome shared with the supervisor.
4. Finalise whether Jira uses one partitioned board or separate boards; keep pre-sprint work in the backlog/Sprint Zero, preserve actual work dates, and prepare the single cross-product sprint-report evidence path.
5. Continue the named ConnectMyTask pairs against reviewed backlog items and record attributable technical, review, and non-technical evidence for each member.
6. Follow up the client email, confirm the next meeting, and resolve ConnectMyTask country, currency, KYC, payment-provider, and mobile-application scope plus the expected sprint demonstrations.
7. Complete one team and project-plan submission with full, separate ConnectMyTask and CuponZ plan sections and address the supervisor's Week 5 feedback.
8. Obtain approved development-VPS and non-production configuration access through a secure channel; document the deployment boundary and end-of-Sprint-2 go/no-go evidence.
9. Keep `UGC08-3` blocked until the detailed scope and acceptance evidence are sufficient; convert only reviewed outcomes into the official sprint backlog.
10. Retain attributable submission evidence for each individual research report; the 2026-09-03 meeting does not confirm all six submissions.
11. Obtain the five missing Atlassian email addresses and finish team access/assignment.
12. Keep `UGC08-17` as planning-only until Semester 1 2027 scope and ownership are approved.
