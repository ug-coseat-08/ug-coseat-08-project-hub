# Client Meeting Minutes — Week 4

| Field | Details |
|---|---|
| Date and time | 2026-08-25, approximately 20:34–21:07 AEST |
| Channel | Online client meeting (Zoom) |
| Attendees | Md Shaik Said (client representative); Ishtiaq Ahmad Anan (client developer); Prattay Banik; Mohita Mittal; Cong Huan Nguyen; Unna Nusen; Le Bao Tran Pham; Md Mudabbirul Islam Saad |
| Absent | No project-team members absent |

## Agenda

Semester priorities, initial audit findings, expected outcomes for CuponZ and ConnectMyTask, technology and environment direction, sprint sequencing, testing, deployment, and immediate actions.

## Key discussion

- The team explained that the supervisor recommended concentrating the semester's two sprints on two applications so they can be developed, tested, and prepared properly. Md Shaik Said prioritised ConnectMyTask and CuponZ because both are comparatively mature and have previously been deployed. PropCalc and Project-B remain part of the wider portfolio but are deferred from the current semester priority.
- Ishtiaq Ahmad Anan confirmed that environment configuration for ConnectMyTask and CuponZ is available. The client asked the team to begin work on the two priority applications immediately and send its proposed improvements and requirements for client and developer review rather than wait for a separate requirements meeting.
- CuponZ is a Bangladesh-focused lead-generation platform, not a conventional online shop. A customer provides contact details to obtain a coupon, and the shop owner receives the lead for later marketing. The client identified problems with subscription tiers, shop-owner access to lead details, administrator functions, and digital-marketing integration. The team still needs to verify the current behaviour and send a precise improvement list.
- The client described CuponZ's current stack and file structure as legacy and difficult to maintain. He authorised the team to propose a substantial technology-stack or architecture change, provided the approved product functionality is preserved and the proposed change is sent for review.
- ConnectMyTask was described as the more complete and robust application. It has previously been deployed, but the team and client discussed remaining audit concerns, including KYC and payment behaviour. The intended direction is an international marketplace whose forms, currency, and payment options can vary by country; SSLCommerz for Bangladesh and Stripe for Australia were discussed as examples, while the exact supported markets and gateways still require confirmation.
- The client wants both priority applications prepared for real customers, not treated only as assessment demonstrations. Sprint 1 should focus on development for both applications. Sprint 2 should focus on functional testing, defect correction, and readiness evidence. A developer should write functional test cases and another team member should execute them.
- The client expects to provide development-VPS access within one to two weeks or by the end of the next sprint. Production deployment is not automatic: the client, developer, and team will make a go/no-go decision after Sprint 2 based on readiness. Either the team or Ishtiaq may then perform the authorised production deployment.
- The team summarised its application audits and offered to send the consolidated audit document after the meeting. The client acknowledged the reported Project-B credential-exposure concern; credential rotation or remediation was not confirmed in the meeting.

## Decisions and agreements

- Prioritise ConnectMyTask and CuponZ for the two Semester 2 sprints; defer PropCalc and Project-B from the current semester priority.
- Preserve CuponZ's lead-generation purpose and approved functionality, while allowing the team to propose replacement of its legacy technology stack and architecture.
- Use Sprint 1 for development on both priority applications and Sprint 2 for cross-executed functional testing, defect correction, and readiness assessment.
- Make the production go/no-go decision after Sprint 2; development deployment and testing must happen first.
- Design ConnectMyTask toward international use with country-appropriate forms, currencies, and payment options; the detailed market and gateway requirements remain to be confirmed.

## Actions

| Action | Owner | Due or status |
|---|---|---|
| Send the consolidated audit document and a precise proposed improvement list for ConnectMyTask and CuponZ. | Mohita Mittal and project team | As soon as possible after the meeting |
| Review the proposed improvements, add any missing requirements, and confirm the accepted work. | Md Shaik Said and Ishtiaq Ahmad Anan | After receiving the team's list |
| Provide or reconfirm approved environment configuration, the existing development instance, and necessary access through a secure private channel. | Ishtiaq Ahmad Anan | As soon as possible |
| Verify CuponZ in the customer, shop-owner, and administrator roles and refine its proposed modernisation scope. | Project team, with Ishtiaq's support | Before committing the detailed Sprint 1 backlog |
| Begin reversible development within the confirmed ConnectMyTask and CuponZ product directions while the detailed improvement list is reviewed. | Project team | Sprint 1 |
| Write functional test cases for each implemented change and assign a different member to execute them. | Each developer and paired tester | Sprint 2 |
| Provide development-VPS access for deployment and testing. | Md Shaik Said and Ishtiaq Ahmad Anan | Within one to two weeks / by the end of Sprint 1, as stated in the meeting |
| Review readiness evidence and make a production go/no-go decision. | Client, Ishtiaq Ahmad Anan, and project team | End of Sprint 2 |
| Send concise PropCalc findings for future-semester planning. | Unna Nusen | After the meeting; no date agreed |

## Source note

These draft minutes were prepared from the 33-minute screen recording and an AI-generated timestamped transcript. The recording did not consistently capture locally spoken contributions during several presentation sections, so detailed inaudible statements were not reconstructed. All attendees must review the wording, attribution, and actions before the record is treated as final.
