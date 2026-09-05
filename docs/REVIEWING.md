# Shared review, a small trusted core

Anyone can explore. Contributors review one another. Integrators maintain the accepted research record; owners manage access and resolve project-level decisions. The project founder need not review every PR.

## Responsibilities

| Role | Repository access | Normal work |
|---|---|---|
| Public participant | Public reading and fork PRs once public | Explore, report gaps, submit work, review |
| `polymath-contributors` | Write | Own branches and PRs; reviews of other contributions |
| `polymath-integrators` | Maintain | Triage, coordinate substantive reviews, integrate scoped results, keep the route map current |
| `owners` | Admin | Access, repository settings, infrastructure decisions, disputes, release oversight |

These are assigned responsibilities. As of this guide's preparation, `main` is not technically protected: the repository is private on GitHub Free. Contributors must use PRs and leave `main` updates to the core. At public launch, owners should enable enforceable rules requiring PRs and code-owner approval, block force pushes and deletion, and require new approval when the reviewed work changes. [CODEOWNERS](../.github/CODEOWNERS) names integrators and owners for general integration and owners for `.github/` changes. A review policy or ownership file does not itself enforce these rules.

## Two review depths

**Exploration:** a relevant reviewer or integrator checks that the question, evidence, dependencies, and uncertainty are legible. Conjectures and failed approaches can be accepted as research notes. Depositing or merging a note does not make its proposed theorem verified. Avoid requiring a proof before someone is allowed to investigate.

**Accepted mathematics:** someone other than the author reconstructs the load-bearing argument at an exact commit, checks its assumptions and scope, and records a verdict. An integrator checks that the evidence supports the proposed status and places the result in the accepted record using [the integration requirements](../CONTRIBUTING.md#what-makes-a-packet-integrable). A reviewer can also be the integrator when they are independent of the contribution; an extra approval round is not automatically necessary.

Different chats using the same model can repeat the same mistake. Seek independence through a fresh derivation, adversarial examples, different tools, and human mathematical scrutiny where available. Agreement among agents is not a substitute for a proof.

## A practical review pass

1. Pick a PR in a direction you understand. Say which part you will review so others can complement it; there is no mandatory claim queue or review quota.
2. Read the actual files at the proposed head, including the dependencies that bear the conclusion. Test the earliest uncertain step. For computations, distinguish replay from independently checking the algorithm and coverage.
3. Leave a short report: **source SHA; what you checked; verdict and scope; first gap or required correction; what you ran**. State omissions explicitly. A partial review is useful when labeled partial.
4. The author addresses corrections on their branch. Review the new commit and affected dependencies; an old verdict does not automatically cover changed mathematics. Preserve old reports as history.
5. An integrator deposits the exploration or integrates the reviewed result with its provenance and scope. Update the relevant program's next step when it changes. Do not merge a large historical branch merely because one claim passed review.

Changes to proof checkers, automation, dependencies, or access-related files need a reviewer who can assess those changes. Owners should configure ownership rules for those paths at launch. Run untrusted contributed code in an isolated environment without repository secrets; a mathematical review does not authorize a privileged workflow.

## Keeping the project moving

Contributors are encouraged to review another person's work when they have relevant expertise. Integrators can make small, regular passes over ready PRs and help match difficult claims to reviewers. The founder can focus on research direction, unresolved disputes, access, and occasional release audits. Promote reliable reviewers into the integrator team as the project grows.

Preserve refutations and useful failed attempts. Track the first missing theorem and the dependencies of accepted claims, so a correction reaches the results that rely on it. The goal of a review pass is a clearer, more reliable research record, not a target number of merged PRs.
