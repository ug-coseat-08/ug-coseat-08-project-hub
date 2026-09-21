# Current Project State

**Reviewed:** 2026-09-21
**Timezone:** Australia/Sydney
**Confidence:** Evidence-backed summary; unresolved items remain explicit.

## Project snapshot

- **Project:** UG_COSEAT_08 — Portfolio Rescue & Resilient AI Integration
- **Unit:** COS40005, Semester 2 2026
- **Current phase:** Sprint 1 ConnectMyTask delivery and investigation
- **Supervisor:** Dr Naveed Ali
- **Client representative:** Md Shaik Said
- **Delivery direction:** Complete an approved ConnectMyTask increment first, then move to CuponZ; use evidence-backed development, independent testing, defect correction, and an approved deployment lifecycle.
- **Scope status:** All twelve organisation repositories were accessed and verified on 2026-08-20. ConnectMyTask and CuponZ remain the Semester 2 priorities. On 2026-09-10 the client technical contact clarified the initial ConnectMyTask countries, provider KYC, dynamic currency/payment direction, Sprint 1 mobile investigation, and ConnectMyTask-first sequence. Payout-process confirmation, requester KYC, the remaining per-country matrix, detailed CuponZ scope, development access, and minimum acceptance/readiness evidence remain pending.

At the first client meeting on 2026-08-13, the client directed the team to begin discovery across four applications: algorithmic trading, lead-generation coupons, property-portfolio calculations, and an Airtasker-like task marketplace. On 2026-08-20 the team received and verified access to all twelve repositories in the client's GitHub organisation; every repository was cloned, installed, and tested, and the consolidated evidence is recorded in the [repository state summary](../discovery/2026-08-20-repository-state.md). The proposed mapping is coupons ("CuponZ") to five repositories, the ConnectMyTask marketplace to three, PropCalc to one, and trading to `Project-B`, which currently exists only as a zip archive containing files that look like real credentials.

At the second client meeting on 2026-08-25, Md Shaik Said selected ConnectMyTask and CuponZ as the current semester priorities because they are comparatively mature and were previously deployed. PropCalc and Project-B were deferred from the current semester priority. The client authorised the team to propose replacing CuponZ's legacy stack while preserving its approved lead-generation functionality, and directed ConnectMyTask toward international use with country-appropriate forms, currencies, and payment options. Sprint 1 is for development on both applications; Sprint 2 is for cross-executed functional testing, defect correction, and readiness evidence, followed by a production go/no-go decision. `UGC08-3` remains blocked until the precise improvement list, repository boundary, acceptance evidence, and client/supervisor minimum outcome are confirmed.

At the 2026-08-27 supervisor meeting, Dr Naveed Ali directed the team to begin work by the following week and to maintain separate Jira boards and GitHub project workspaces for ConnectMyTask and CuponZ. The team then adopted a provisional sequential working plan: all six members will begin with ConnectMyTask and move together to CuponZ. This is a planning choice, not approved product scope or contribution evidence; week targets and backlog contents remain subject to estimates, client review, and `UGC08-3`. The team needs one team plan, while the supervisor is awaiting unit-convener guidance on whether the two products require one combined project plan or two separate plans.

At the 2026-09-03 supervisor meeting, Dr Naveed Ali relayed the unit convener's guidance that multiple products may be managed in either one clearly partitioned Jira board or separate boards, while each sprint still has one combined report. Work before Week 7 should remain in the backlog or Sprint Zero; the official sprints run in Weeks 7–9 and 10–12. The supervisor reviewed the team's ConnectMyTask-first sequence and its three provisional work pairs, with ConnectMyTask targeted for the end of the term break before the team concentrates on CuponZ. One team and project-plan submission is required, containing a complete separate project-plan section for each product. These planning clarifications do not resolve the client-scope gate: supported countries, mobile scope, accepted improvements, measurable criteria, and minimum outcomes remain pending.

At the 2026-09-10 client meeting, Ishtiaq Ahmad Anan said the team's proposal aligned with the client's requirements and accepted the ConnectMyTask-first sequence. Bangladesh is the first market, followed by India, Pakistan, Sri Lanka, and Australia. Providers require KYC using national identification and professional certification where applicable; requester KYC remains unresolved. Static currency conversion should become dynamic, SSLCommerz should serve Bangladesh, and international gateways such as PayPal or Google Pay require a final country matrix. Sprint 1 should focus on ConnectMyTask KYC, currency/payment, and a bounded run/test/investigation of the existing mobile application. The team also identified a declined-withdrawal defect that does not restore the provider balance; Ishtiaq required that production-impacting issue to be solved before release. The detailed payout process, mobile implementation subset, CuponZ backlog, environments, and acceptance evidence keep `UGC08-3` partially blocked.

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

- `UGC08-3`: client-scope gate; partially clarified on 2026-09-10, but still blocked for payout-process confirmation, requester KYC, remaining per-country configuration, mobile implementation scope, CuponZ detail, environments, and measurable acceptance evidence.
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
2. Convert the 2026-09-10 ConnectMyTask country, provider-KYC, dynamic-currency, payment, and mobile-investigation direction into measurable reviewed backlog criteria.
3. Reproduce and fix the declined-withdrawal balance-reversal/atomicity defect with synthetic non-production evidence and independent review before production readiness approval (RISK-011).
4. Follow up Ishtiaq Ahmad Anan's promised email and confirm the provider-payout process, requester KYC, allowed documents/verification method, country-specific forms/compliance, and gateways for India, Pakistan, Sri Lanka, and Australia.
5. Assign and complete the bounded mobile run/test/investigation; treat any implementation beyond the reviewed findings as pending scope.
6. Continue the named ConnectMyTask pairs against reviewed backlog items, record attributable evidence, and complete ConnectMyTask before moving the team to CuponZ.
7. Review the CuponZ improvement list and architecture options, then select a feasible accepted subset without promising an unestimated replatforming.
8. Finalise the Jira board structure, preserve actual work dates for the cross-product sprint report, and name ticket reviewers.
9. Obtain approved development-VPS and non-production configuration access through a secure channel; document the deployment boundary and end-of-Sprint-2 go/no-go evidence.
10. Keep `UGC08-3` blocked for the remaining details while converting only the confirmed 2026-09-10 outcomes into delivery work.
11. Retain approximately 12.5 hours of contemporaneous technical and non-technical evidence per member each week; obtain the five missing Atlassian email addresses.
12. Keep `UGC08-17` as planning-only until Semester 1 2027 scope and ownership are approved.
