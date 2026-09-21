# UG_COSEAT_08 Project Hub

Technical coordination and shared project records for **Portfolio Rescue & Resilient AI Integration**, undertaken in COS40005 Computing Technology Project A during Semester 2, 2026.

## Project details

| Field | Details |
|---|---|
| Unit | COS40005 Computing Technology Project A |
| Project | UG_COSEAT_08 |
| Semester | Semester 2, 2026 |
| Supervisor | Dr Naveed Ali |
| Client representative | Md Shaik Said |
| Current phase | Sprint 1 ConnectMyTask delivery and investigation |
| Current status | On 2026-09-10 the client technical contact clarified the initial countries, provider KYC, dynamic currency/payment direction, mobile investigation, and ConnectMyTask-first sequence; the payout reversal defect must be fixed before production, while remaining per-country, payout-process, CuponZ, environment, and acceptance details are pending |

## Purpose

This private GitHub repository is the complete shared, versioned record for meeting records, confirmed requirements, decisions, risks, contribution evidence, and project working practices. Jira is the operational delivery board, while Confluence provides a readable navigation and collaboration hub.

The repository does not contain client application source code. The client granted access to its GitHub organisation on 2026-08-20 and all twelve repositories were cloned and verified; the consolidated evidence is recorded in the [repository state summary](discovery/2026-08-20-repository-state.md). On 2026-08-25, the client prioritised ConnectMyTask and CuponZ. On 2026-09-03, the supervisor reviewed a ConnectMyTask-first Sprint Zero plan and confirmed that one assessment submission must contain a complete separate project plan for each product. On 2026-09-10, Ishtiaq Ahmad Anan accepted the ConnectMyTask-first sequence and clarified the initial ConnectMyTask Sprint 1 direction; remaining client and acceptance details stay explicit under `UGC08-3`.

## Team

- Prattay Banik
- Mohita Mittal
- Cong Huan Nguyen
- Unna Nusen
- Le Bao Tran Pham
- Md Mudabbirul Islam Saad

See [TEAM.md](TEAM.md) for the working team register.

## Current priorities

1. Follow up privately on exposed credentials and verify authorised rotation/remediation without opening, using, or reproducing any values.
2. Convert the 2026-09-10 ConnectMyTask country, provider-KYC, dynamic-currency, payment, and mobile-investigation direction into measurable reviewed backlog criteria.
3. Reproduce and fix the declined-withdrawal balance-reversal/atomicity defect with synthetic non-production tests and independent review before any production release.
4. Obtain the promised confirmation of the provider-payout process and the remaining requester-KYC, per-country gateway/forms, and mobile implementation decisions.
5. Complete the agreed ConnectMyTask increment first, then review the CuponZ improvement list and replatforming proposal without overcommitting the semester capacity.
6. Finalise the Jira board structure, preserve actual work dates for the cross-product sprint report, and assign the mobile investigation and reviewers.
7. Obtain approved development-VPS and non-production configuration access through secure channels and define the minimum acceptance/readiness evidence.
8. Keep `UGC08-3` blocked only for the unresolved details and convert confirmed outcomes into the official sprint backlog without expanding them.
9. Retain approximately 12.5 hours of attributable technical and non-technical evidence per member each week, obtain the five missing Atlassian email addresses, and finalise reviewer responsibilities.

## Project records

- [Project intake and client questions](PROJECT_INTAKE.md)
- [Requirements register](REQUIREMENTS.md)
- [Decision log](DECISIONS.md)
- [Risk register](RISKS.md)
- [Team register](TEAM.md)
- [Meeting register](MEETINGS.md)
- [Contribution workflow](CONTRIBUTING.md)
- [Security guidance](SECURITY.md)
- [AI usage log](AI_USAGE_LOG.md)
- [Agent knowledge base](knowledge-base/README.md)
- [Agent instructions](AGENTS.md)

## Connected tools

- [Jira UGC08 backlog](https://ugcoseat08.atlassian.net/jira/software/projects/UGC08/boards/1/backlog) — operational work tracking.
- [Confluence project hub](https://ugcoseat08.atlassian.net/wiki/spaces/UGC08/pages/65838/UG_COSEAT_08+Project+Hub) — navigation and collaboration.
- [GitHub project hub](https://github.com/ug-coseat-08/ug-coseat-08-project-hub) — canonical versioned records.

## Working workflow

1. Record a clear task with an expected result and acceptance criteria.
2. Nominate one primary owner and a separate reviewer where practical.
3. Create a short-lived branch from the latest `main`, using the Jira key where available.
4. Make a focused change using descriptive commits.
5. Open a pull request and link the task.
6. Provide test results, screenshots, notes, or other relevant evidence.
7. Address review findings and confirm the acceptance criteria.
8. Merge only after the required checks and review are complete.
9. Delete the merged branch and update related records.

Detailed technical choices remain provisional until the client reviews the proposed ConnectMyTask and CuponZ improvements and the team records the accepted architecture and acceptance evidence.
