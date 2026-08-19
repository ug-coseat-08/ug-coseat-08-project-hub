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
| Algorithmic-trading platform (likely `Project-B`; product name TBD) | Allow a user to configure an algorithm for automated trading. | [ug-coseat-08/Project-B](https://github.com/ug-coseat-08/Project-B) | Existing as a zip archive of a Flask trading tool; not a working repository | Python/Flask (from archive inspection); no tests or CI observed | Not runnable until the archive is extracted and secrets are removed | Archive contains files that look like real credentials; no README, history, or CI | Access received 2026-08-20 |
| Lead-generation coupon platform ("CuponZ") | Capture customer contact details through coupon offers for small-business lead generation. | [backend](https://github.com/ug-coseat-08/backend), [frontend](https://github.com/ug-coseat-08/frontend), [mobile-app](https://github.com/ug-coseat-08/mobile-app), [coupon-scraper](https://github.com/ug-coseat-08/coupon-scraper), [deploy](https://github.com/ug-coseat-08/deploy) | Existing; mixed maturity | Fastify + MySQL/MariaDB (`backend`); Vite React SSR (`frontend`); Expo SDK 54 (`mobile-app`); Python CLI (`coupon-scraper`); VitePress (`deploy`) | All five cloned and verified 2026-08-20; `backend` needs Linux-oriented services (memcache, MariaDB) and `pnpm install --ignore-scripts` on Windows/Node 24 | `backend`: 13 failing tests, no CI, committed sample private key. `frontend`: thin test coverage, mixed lockfiles. `mobile-app`: FileSystem runtime bug, no tests. `deploy`: docs build broken by a dead link | Access received 2026-08-20 |
| Property-portfolio calculator ("PropCalc") | Combine online data with a user's property profile to project asset value and cash flow. | [ug-coseat-08/propcalc](https://github.com/ug-coseat-08/propcalc) | Existing; production build currently broken | Flask + MongoDB backend; Next.js 15 + TypeScript frontend | Cloned and verified 2026-08-20; backend compiles; frontend build fails | Empty `add-property/page.tsx` fails the build; committed `node_modules` and `.env`; zero tests | Access received 2026-08-20 |
| Task marketplace ("ConnectMyTask", described as Airtasker-like) | Connect users through a task/service marketplace; detailed journeys TBD. | [ConnectMyTask](https://github.com/ug-coseat-08/ConnectMyTask), [Web-connectmytask](https://github.com/ug-coseat-08/Web-connectmytask), [Mobile-connectmytask](https://github.com/ug-coseat-08/Mobile-connectmytask) | Existing; strongest portfolio area | Express + MongoDB + Docker (`ConnectMyTask`); React CRA (`Web-connectmytask`); Flutter (`Mobile-connectmytask`) | All three cloned and verified 2026-08-20; backend and web run their full test suites | `Mobile-connectmytask`: boilerplate test fails and dependency pins block current Flutter; web has minor hygiene issues | Access received 2026-08-20 |

The client referred to a wider portfolio, but clearly directed the team to begin with the four applications above. Other applications may be considered only after the first four are completed, so they are not part of the current working set.

All twelve organisation repositories, including the team's own project hub and two apparently unused repositories (`Project-B`, `create-debug-test`), were cloned, installed, and tested on 2026-08-20. The consolidated result and the per-repository evidence are recorded in the [repository state summary](discovery/2026-08-20-repository-state.md). The application-to-repository mapping above is **proposed** from repository contents; it is not yet client-confirmed and must be verified with Ishtiaq Ahmad Anan before per-application scope is agreed.

## Data, infrastructure, and operations

| Topic | Questions to confirm | Current answer |
|---|---|---|
| Databases and storage | What data stores exist? Who owns them? Is representative test data available? | TBD |
| External services | Which third-party services, APIs, or integrations are required? | TBD |
| Hosting | Where are development, staging, and production environments hosted? | Client described a development virtual machine and a separate production environment; exact hosts and access are TBD. |
| Deployment | How are releases currently built, approved, deployed, verified, and rolled back? | CI/CD to development is preferred, followed by integration testing and controlled production deployment. Direct production access is undecided; client developer may deploy. Rollback and approval evidence remain TBD. |
| Configuration | How are secrets and environment-specific settings managed? | TBD |
| Testing | What automated and manual tests currently exist? | Existing coverage was inventoried on 2026-08-20: strong for the ConnectMyTask backend and web (361 passing tests, green CI), partial for the coupon backend, and absent for `propcalc`, `mobile-app`, and the Flutter app. The team must still write test cases, have another member execute them where practical, track/fix defects, and run integration tests. |
| Performance | What traffic, response-time, concurrency, and availability expectations apply? | TBD |
| Security and privacy | What client, user, data, access, and regulatory restrictions apply? | TBD |
| Documentation | What setup, architecture, support, and handover material already exists? | Per-repository READMEs were inventoried on 2026-08-20 and vary from thorough (`ConnectMyTask`) to absent (`Project-B`). Additional client documentation or demonstrations from Ishtiaq Ahmad Anan are still expected. |

## User journeys and acceptance

| Journey or capability | Intended user | Current behaviour | Expected behaviour | Priority | Acceptance evidence |
|---|---|---|---|---|---|
| Configure automated trading | Trading-platform user; exact persona TBD | Existing behaviour and maturity TBD | User can configure an algorithm and the platform can execute the intended workflow safely; detailed criteria TBD | TBD | Client-approved functional, test, and deployment evidence |
| Obtain an offer and provide a lead | Small-business customer/prospect; exact persona TBD | Existing behaviour and maturity TBD | User supplies contact details to receive an offer; privacy and consent requirements TBD | TBD | Client-approved journey and data-handling evidence |
| Review a property portfolio projection | Property owner/investor; exact persona TBD | Existing behaviour and maturity TBD | User profile combines relevant online data to show asset-value and cash-flow projections; calculation criteria TBD | TBD | Client-approved calculation and test evidence |
| Use a task marketplace | Service requester/provider; exact personas TBD | Existing behaviour and maturity TBD | Detailed marketplace journey TBD after repository review | TBD | Client-approved journey and test evidence |

## Remaining client-discovery questions

1. Confirm the proposed application-to-repository mapping, especially that trading means `Project-B`, whether all five coupon repositories are in scope, and what should happen to `Project-B` and `create-debug-test`.
2. For each application, who are the users, what are the main gaps, and which small improvements have the highest priority?
3. What realistic result should be completed this semester, and how will the client's production goal fit the university's alpha-release and sprint structure?
4. Which environments and services will the team receive beyond repository access (development VM, databases, third-party services), and what security, privacy, testing, performance, deployment, rollback, monitoring, and support constraints apply?
5. Who will act as Product Owner, approve the work, and authorise each production release?
6. When will the first fortnightly meeting with Ishtiaq Ahmad Anan occur, and what should its initial agenda cover? The team proposed Tuesday, 25 August 2026 at 8:30 PM.
