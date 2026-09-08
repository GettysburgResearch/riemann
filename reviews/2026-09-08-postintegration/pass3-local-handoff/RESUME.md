# Next review and eventual integration handoff

This is a review continuation, not an instruction to merge a research wave. Do not restore old main from the review branch. The eventual integration must start from **then-current main** and preserve its cumulative public-facing structure.

## Start with exact deltas

Read current main, PR #827 and SOURCE_HEADS.json. The controlling review baseline for this packet is PR #827 at `13ac26caae546c8a6481a85b2f61ecc524dbbb27`. Its pass1/pass2 directories must remain unchanged when adding pass3. Compare each currently fetched head against the exact source commit in FILES.tsv; compare *all changed files*, not just the old manuscript directory.

Example using the two actual #803 checkpoints:

```sh
before=31a35a90b0b924dc98a2c89c463fb59577f45a4e
after=db175de165a9077e709b1cb482998171ffc0c6e7
GIT_NO_REPLACE_OBJECTS=1 git merge-base --is-ancestor "$before" "$after"
GIT_NO_REPLACE_OBJECTS=1 git diff --name-status "$before" "$after"
GIT_NO_REPLACE_OBJECTS=1 git diff "$before" "$after" -- standalone/
```

For a later pass, replace `after` by the freshly fetched full commit and use the reviewed head here as `before`. Record the ancestry exit status. If histories diverge, use the two exact trees and examine replacements/deletions; an ordinary GitHub three-dot comparison can omit changes relative to the reviewed tree. For every read file, compare `git rev-parse "$after:$path"` with its locked Git blob. Unchanged file bytes preserve only their recorded review, subject to changed dependencies. Unread siblings remain unread even when a branch does not move.

Repeat all-state recent PR/issue discovery and relevant comments, including branches without PRs. Snapshots are sequential, not atomic. Do not count an updated PR description as new mathematics when its source was already frozen.

## Eight remaining main manuscripts

All eight are on #805 at `602d7ddf9dbd2ba79bd6cada149772111ca72150`:

| Packet | Root relative to standalone/ | Main review purpose |
|---|---|---|
| DO | 2026-09-06-astra-dilation-observability | Complete dictionary, literal full norm and leakage; source domain and all integer coordinates |
| BG | 2026-09-06-astra-block-gain | Distinguish the solved detail relaxation from the unbounded full gain and coarse coupling |
| GT | 2026-09-06-astra-growth-transfer | Uniform operator/source transfer and explicitly conditional analytic inputs |
| BL | 2026-09-06-astra-balanced-lift | Constrained optimizer, real horizon, all tail terms and zero-forced growth |
| GE | 2026-09-06-astra-green-energy | Full finite Green form and tridiagonal inverse, not only first interval |
| TE | 2026-09-06-astra-terminal-endpoint | Harmonic comparison versus different terminal-balanced source; exact fixed-grid scalar |
| BH | 2026-09-07-astra-balanced-hyperbola | Complete native hyperbola/cancellation identities and unchanged target norm |
| CL | 2026-09-07-astra-critical-line-attempt | Actual attempted closing estimate, contour/jet conditions and why remaining bound is open |

Read the complete sequence in dependency order, including its failed approximations, not merely the current PR description. Preserve the terminal-source/earlier-optimizer distinction. The review at #805's head should not automatically extend to later additions.

## Supporting work still required for a fully scoped extraction

- **RN and RC:** audit/replay their optimized finite minima with the correct two-jet versus balance-only class. The independent PR trial values in this pass are not replacements for optimality certificates. Respect the published/attachment discrepancy in RECONCILIATION.md.
- **FR and CD:** independently audit/replay each different fixed-horizon complete-tail witness. IE's different exponential-target certificate is not a substitute. Check ordinary-input versus ideal impulse realization and the price of compactification.
- **WP and IE:** prior full numerical subsets have replay evidence; original package authentication and CLI rejection suites still have their own boundaries.
- **SSQ/CCT:** complete actual finite prime-energy prefix replay and auxiliary/source audits. Keep unconditional Brun–Titchmarsh detail separate from the explicitly RH-conditional Cramér converse.
- **ADG/DPG/GCP/CCS/ANT:** inspect original manifests, accepting code and full package rejection suites before labeling those programs accepted. This pass provides independent capacity/profile/native identities, not an executed original package. The overlapping squarefree theorem must be extracted once; higher exponents and all edge directions remain.
- **LC/CSM/HC/ST and #790 predecessors:** finish the source adapters and auxiliary manuscripts that previous file-level reviews excluded. Do not relabel the old #790 September-5 dependency as newly deposited research. Its review/independence holds matter when a new theorem consumes it.
- **MW and older finite evidence:** the actual N=3 signed-work test is new independent evidence; the original 65,536-event and compact-realization campaigns remain distinct. No broad rerun is required to state the analytic obstruction, but advertised numerical campaigns need their own disposition.
- **TSR:** preserve the reviewed affine census at its exact branch-only source; finish publication/attribution and any claimed global-family adapter. Repeating the finite classification does not prove global coherence.
- **Auxiliary notes and source discussions:** main-manuscript coverage does not automatically clear all ATTEMPT, SOURCES, README, certificate, or later discussion claims. Give these an explicit per-file disposition at the intended extraction boundary.

## Exit condition

Every proposed extraction should have a readable statement, exact assumptions, source/dependency lock, and an explicit evidence status. Open RH-strength estimates may remain open and discoverable. Unreplayed code can remain research, or be excluded from the accepted extraction with its hold retained; it must not be advertised as verified. Do not turn the 37/45 manuscript count into a package-acceptance statistic.

Only after this review reconciliation should a separate integration branch be organized from current main, followed by an independent integration review and an actual validation run at its exact tree. Nothing in this review authorizes changing visibility, permissions, licensing or Actions settings.
