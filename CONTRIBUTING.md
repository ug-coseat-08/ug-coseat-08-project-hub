# Contributing

## Before starting work

1. Confirm that the task is within the agreed project scope.
2. Define the objective, owner, expected result, acceptance criteria, dependencies, and required evidence.
3. Update local `main` before creating a branch.

## Branches

Use one short-lived branch for each coherent change:

- `feat/UGC08-<number>-<description>`
- `fix/UGC08-<number>-<description>`
- `docs/UGC08-<number>-<description>`
- `test/UGC08-<number>-<description>`
- `research/UGC08-<number>-<description>`
- `chore/UGC08-<number>-<description>`

Do not use permanent personal branches, a permanent `develop` branch, or shared branches that obscure ownership.

## Commits

- Commit through your own Git identity.
- Start the subject with the Jira key where one exists, for example `UGC08-12 record client decisions`.
- Use short, descriptive messages that explain the completed change.
- Keep unrelated work in separate commits and pull requests.
- Never rewrite another student's authorship or fabricate contribution history.

## Pull requests

- Start the title with the Jira key, for example `[UGC08-12] Record client discovery`.
- Link the Jira work item and any supporting GitHub issue.
- Explain what changed and why.
- State the affected application or project record.
- Include commands run and their results.
- Attach screenshots, output, or other evidence where useful.
- Describe security, privacy, configuration, migration, fallback, and recovery effects where relevant.
- Identify known limitations and documentation changes.
- Request a human reviewer who is not the author.
- Respond to findings and keep the original author responsible for corrections.

Draft pull requests are welcome for early visibility but are not ready for final approval or merge.

## Review and merge

Reviewers should check requirements, behaviour, regressions, security, tests, failure handling, integration effects, and documentation. Formatting and deterministic mechanical checks should be handled by tooling where available.

Merge only after acceptance criteria, relevant checks, review conversations, and contribution evidence are complete. Delete the branch after merge.
