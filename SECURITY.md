# Security and Responsible Handling

## Scope

This repository stores project coordination records. Client application source code must remain in its authorised repository unless the client explicitly approves another location.

## Do not commit

- Passwords, tokens, API keys, private keys, or credentials.
- Personal information or confidential client information.
- Production data or unapproved datasets.
- Raw meeting recordings or transcripts without explicit approval.
- Environment files containing real values.
- Protected course material or licensed documents.

Use redacted examples and documented environment-variable names where configuration guidance is required.

## Reporting a concern

Do not disclose a suspected vulnerability or exposed secret in a public issue. Notify the repository owner and the relevant client or supervisor contact privately, identify the affected system and evidence, and avoid unnecessary access or exploitation.

If a credential is exposed, treat it as compromised: stop further sharing, revoke or rotate it through the authorised owner, remove it from current content and history using a reviewed procedure, and document the incident without repeating the secret.

## Application work

Before security testing, confirm the authorised systems, accounts, environments, test methods, data, and time window. Do not test production systems or third-party services without explicit written permission.
