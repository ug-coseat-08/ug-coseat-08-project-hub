# Project Intake

Use this register during client and supervisor discussions. Record confirmed information separately from assumptions and link supporting evidence where available.

## Desired outcome and scope

| Question | Current answer | Status | Source or evidence |
|---|---|---|---|
| What outcome should be demonstrated at the end of Semester 2? | Supervisor: an agreed alpha release. Client: progress four initial existing applications through modernisation, testing, defect correction, and deployment toward production use. | Confirmed directions; one realistic semester outcome still needs joint agreement | [Week 1 supervisor meeting](meeting-minutes/supervisor/2026-08-07-supervisor-meeting.md); [first client meeting](meeting-minutes/client/2026-08-13-client-meeting.md) |
| What is the minimum acceptable alpha release? | The client advised small, complete, high-quality increments rather than broad feature work; the exact per-application minimum is not agreed. | Open—requires client and supervisor alignment | [First client meeting](meeting-minutes/client/2026-08-13-client-meeting.md) |
| Is the team reviewing applications, completing applications, or both? | Both: understand and run existing applications, identify gaps, modernise approved areas, test, fix defects, establish the delivery lifecycle, and deploy through an approved process. | Confirmed high-level direction; per-application scope pending | [First client meeting](meeting-minutes/client/2026-08-13-client-meeting.md) |
| Which application or workflow has the highest priority? | Four initial application categories were described, but their order and exact scope were not prioritised. | Open | [First client meeting](meeting-minutes/client/2026-08-13-client-meeting.md) |
| What is explicitly out of scope? | No formal exclusions were approved. Large feature commitments were discouraged, and the additional four future applications are not current approved scope. | Partially confirmed | [First client meeting](meeting-minutes/client/2026-08-13-client-meeting.md) |

## Application and repository inventory

| Application or service | Purpose | Repository owner/location | Current status | Technology | Local setup | Known problems | Access required |
|---|---|---|---|---|---|---|---|
| Algorithmic-trading platform (exact product name TBD) | Allow a user to configure an algorithm for automated trading. | Client-owned GitHub organisation/repository; exact location TBD | Existing; production maturity TBD | TBD | Pending access | Gap and test inventory pending | Team GitHub identifiers to be added by client/developer |
| Lead-generation coupon platform (exact product name TBD) | Capture customer contact details through coupon offers for small-business lead generation. | Client-owned GitHub organisation/repository; exact location TBD | Existing; production maturity TBD | TBD | Pending access | Gap and test inventory pending | Team GitHub identifiers to be added by client/developer |
| Property-portfolio calculator (exact product name TBD) | Combine online data with a user's property profile to project asset value and cash flow. | Client-owned GitHub organisation/repository; exact location TBD | Existing; production maturity TBD | TBD | Pending access | Gap and test inventory pending | Team GitHub identifiers to be added by client/developer |
| Task marketplace, described as Airtasker-like (exact product name TBD) | Connect users through a task/service marketplace; detailed journeys TBD. | Client-owned GitHub organisation/repository; exact location TBD | Existing; production maturity TBD | TBD | Pending access | Gap and test inventory pending | Team GitHub identifiers to be added by client/developer |

The client referred to a wider portfolio, but clearly directed the team to begin with the four applications above. Other applications may be considered only after the first four are completed, so they are not part of the current working set.

## Data, infrastructure, and operations

| Topic | Questions to confirm | Current answer |
|---|---|---|
| Databases and storage | What data stores exist? Who owns them? Is representative test data available? | TBD |
| External services | Which third-party services, APIs, or integrations are required? | TBD |
| Hosting | Where are development, staging, and production environments hosted? | Client described a development virtual machine and a separate production environment; exact hosts and access are TBD. |
| Deployment | How are releases currently built, approved, deployed, verified, and rolled back? | CI/CD to development is preferred, followed by integration testing and controlled production deployment. Direct production access is undecided; client developer may deploy. Rollback and approval evidence remain TBD. |
| Configuration | How are secrets and environment-specific settings managed? | TBD |
| Testing | What automated and manual tests currently exist? | Team must write test cases, use another member to execute them where practical, track/fix defects, and run integration tests. Existing coverage and tooling are TBD. |
| Performance | What traffic, response-time, concurrency, and availability expectations apply? | TBD |
| Security and privacy | What client, user, data, access, and regulatory restrictions apply? | TBD |
| Documentation | What setup, architecture, support, and handover material already exists? | Some technical-design or user-guide material may exist; Ishtiaq Ahmad Anan will provide documentation or demonstrations after access. Completeness is TBD. |

## User journeys and acceptance

| Journey or capability | Intended user | Current behaviour | Expected behaviour | Priority | Acceptance evidence |
|---|---|---|---|---|---|
| Configure automated trading | Trading-platform user; exact persona TBD | Existing behaviour and maturity TBD | User can configure an algorithm and the platform can execute the intended workflow safely; detailed criteria TBD | TBD | Client-approved functional, test, and deployment evidence |
| Obtain an offer and provide a lead | Small-business customer/prospect; exact persona TBD | Existing behaviour and maturity TBD | User supplies contact details to receive an offer; privacy and consent requirements TBD | TBD | Client-approved journey and data-handling evidence |
| Review a property portfolio projection | Property owner/investor; exact persona TBD | Existing behaviour and maturity TBD | User profile combines relevant online data to show asset-value and cash-flow projections; calculation criteria TBD | TBD | Client-approved calculation and test evidence |
| Use a task marketplace | Service requester/provider; exact personas TBD | Existing behaviour and maturity TBD | Detailed marketplace journey TBD after repository review | TBD | Client-approved journey and test evidence |

## Remaining client-discovery questions

1. What are the names and repository locations of the four applications, and what documentation, services, data, and environments will the team receive?
2. For each application, who are the users, what are the main gaps, and which small improvements have the highest priority?
3. What realistic result should be completed this semester, and how will the client's production goal fit the university's alpha-release and sprint structure?
4. What security, privacy, testing, performance, deployment, rollback, monitoring, and support constraints must the team follow?
5. Who will act as Product Owner, approve the work, and authorise each production release?
6. When will the first fortnightly meeting with Ishtiaq Ahmad Anan occur, and what should its initial agenda cover?
