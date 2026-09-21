# Client Meeting Minutes — Week 6

| Field | Details |
|---|---|
| Date and time | 2026-09-10, approximately 16:04–16:26 AEST |
| Channel | Online client meeting (Zoom) |
| Attendees | Ishtiaq Ahmad Anan; Mohita Mittal; Cong Huan Nguyen; Unna Nusen; Le Bao Tran Pham; Md Mudabbirul Islam Saad |
| Absent | Prattay Banik; Md Shaik Said was not present |

## Agenda

Review of the team's ConnectMyTask proposal and clarification questions, Sprint 1 scope, supported countries, KYC, currency and payments, provider payouts, the mobile application, the ConnectMyTask-first sequence, and the client agreement.

## Key discussion

- Ishtiaq Ahmad Anan said he had reviewed the team's proposal and considered it aligned with the client's requirements. He had not yet confirmed every detail with Md Shaik Said and undertook to provide further answers by email.
- The initial ConnectMyTask market priority is Bangladesh first, followed by India, Pakistan, Sri Lanka, and Australia. Country-specific forms and compliance details were not fully defined in the meeting.
- KYC is required for service providers/task doers. The expected evidence includes a national identity document and, for a person offering a professional service, relevant professional certification. Optional requester/user verification and its documents were discussed but not confirmed as required scope.
- The existing fixed/static currency conversion should be replaced with dynamic conversion so international transactions can use current rates.
- SSLCommerz should support Bangladesh. International payment options such as PayPal and Google Pay were discussed for other markets, while the exact gateway for each non-Bangladesh country remains to be confirmed.
- Ishtiaq described the current provider-payout flow as accumulated provider credit followed by a withdrawal request and administrator approval. He would ask Md Shaik Said whether that flow should remain or change.
- The team raised a payout defect in which a declined withdrawal does not restore the provider's balance, breaking the expected atomic financial transition. Ishtiaq treated this as a serious issue that must be corrected before production and asked the team to ensure the reported ConnectMyTask issues are addressed.
- For Sprint 1, Ishtiaq asked the team to focus on ConnectMyTask KYC, currency conversion, and payment work. The existing mobile application should also be run, tested, and investigated so the team can report what works and what improvements are needed; this was an investigation commitment, not approval for an unspecified mobile rewrite.
- The team reported its three ConnectMyTask work pairs: registration/login and KYC; Direct Hire, provider profiles, and reviews; and payments/payouts. No member was working on the mobile application at that point, and the team said it would begin the mobile investigation the following week.
- The team explained that CuponZ had been investigated but remained more complex because of its technologies and proposed architecture work. The team intended to complete the agreed ConnectMyTask deliverables first and then move to CuponZ; Ishtiaq accepted that sequence.
- The team planned to email the client agreement for Md Shaik Said to complete. Ishtiaq said he would discuss it and the remaining proposal questions with Md Shaik Said.

## Decisions and agreements

- Use Bangladesh as the first ConnectMyTask market, followed by India, Pakistan, Sri Lanka, and Australia.
- Require provider KYC using a national identity document and professional certification where applicable; keep requester/user KYC and its document rules pending further confirmation.
- Replace static currency conversion with dynamic conversion.
- Use SSLCommerz for Bangladesh and investigate suitable international gateways, including PayPal and Google Pay, for the other accepted markets.
- Prioritise ConnectMyTask KYC, currency, and payment work in Sprint 1, together with a bounded run/test/investigation of the existing mobile application.
- Continue the ConnectMyTask-first delivery sequence and move to CuponZ after the agreed ConnectMyTask work.
- Correct the declined-withdrawal balance-reversal/atomicity defect before any production release.

## Actions

| Action | Owner | Due or status |
|---|---|---|
| Confirm with Md Shaik Said whether the existing provider-credit, withdrawal-request, and administrator-approval flow should remain or change, then reply by email. | Ishtiaq Ahmad Anan | Intended on 2026-09-10; confirmation not recorded in this meeting |
| Convert the confirmed KYC, dynamic-currency, payment, and market directions into reviewed ConnectMyTask backlog acceptance criteria. | Project team | Sprint 1 |
| Reproduce and correct the declined-withdrawal balance-reversal/atomicity defect using non-production evidence and independent review. | Payments/payouts pair with project-team review | Before production readiness approval |
| Run and investigate the existing ConnectMyTask mobile application and document what works, what fails, and the improvements requiring review. | Project team; owner to be assigned | Sprint 1 |
| Continue the agreed ConnectMyTask work first, then prepare the reviewed CuponZ scope and architecture decision. | Project team | ConnectMyTask first; CuponZ follows |
| Check the ConnectMyTask issue list that the team reported as already sent. | Ishtiaq Ahmad Anan | As soon as possible |
| Email the client agreement for Md Shaik Said to complete and follow up if no response is received. | Mohita Mittal / project team | As soon as possible |
| Discuss the proposal, any further requirements, and the client agreement with Md Shaik Said and respond to the team. | Ishtiaq Ahmad Anan | As soon as possible |

## Source note

These draft minutes were prepared from the 21-minute 56-second screen recording, a CUDA-accelerated timestamped transcript, Zoom captions, and sampled attendance frames. Six participants were visible: Ishtiaq Ahmad Anan and five team members; Prattay Banik and Md Shaik Said were not present in the recorded meeting. Overlapping and locally captured speech caused several unreliable automated-transcript passages, so only statements supported by clear audio or captions were retained. All attendees should review the wording, attribution, decisions, and actions before the record is treated as final.
