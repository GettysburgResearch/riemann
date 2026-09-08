# Resume after pass three

## 1. Freeze deltas before reviewing them

Read SOURCE_HEADS.json, FILES.tsv, COVERAGE.tsv and the closing PR comment. Refetch main, PR #827, every watched research ref, and recent PR/issue activity. The inventory is not globally atomic. Review source files at the full commit in FILES.tsv, not the current branch name or a stale head printed in a PR body.

For each source, fetch the recorded and newly observed objects into a separate checkout. First ask whether the old head is an ancestor; then compare the **two exact endpoint trees**, restricted to each packet:

```sh
git merge-base --is-ancestor OLD NEW
git diff --name-status OLD NEW -- standalone/EXACT-PACKET/
git diff OLD NEW -- standalone/EXACT-PACKET/PROOF.md
```

Do not use a three-dot diff as a substitute after a rebase or force push. If ancestry fails, explicitly record divergent history and review the two-tree difference; do not silently choose a new baseline. Unchanged reviewed files preserve only their prior component scope. A new SYNTHESIS, wrapper, result or source lock can alter claimed implications even when PROOF.md is unchanged. Classify every changed path as inspected, out of scope, or queued; separately record new branch-only deposits.

Published pass-one and pass-two directories are frozen. Append pass four or a dated delta outside them. Do not rewrite a previous omission to look retrospectively checked. In particular the published second pass, not an older local ZIP, controls its coverage: source-stability was read; entropy feedback and the three RC minima were not cleared until this pass.

## 2. Remaining work, in priority order

| Priority | Packet/source | Specific final-review work |
|---|---|---|
| P0 | New commits on #803/#804/#805/#811/#828/#829 and any new PR/branch | Two-tree deltas, revised theorem/claim summaries and source locks; no retrospective acceptance by unchanged title. |
| P0 | #803 ANT, #828 GCP, #829 CCS | Read the remaining SYNTHESIS/ATTEMPT/source-lock/application material. Check that no wrapper identifies graph energy with the physical residual or deletes the coherent function channel. Reconcile shared squarefree anchoring once, retaining geometric/root-coupling and native-source/survival additions separately. |
| P0 | #804 CD/DC, #812 FR | Audit and, where selected for integration, replay the fixed-horizon ordinary-input realization and older ramp/compact-source numerical witnesses with all future states. IE's different unit-exponential trial and its reused core do not certify these. |
| P1 | #803 LC/WP and #819 IE | Complete source-to-form/domain bindings and the original package inventory, parser, rejection and supplied-result checks. Retain pass2's actual full numerical subset replays without claiming full author package execution. Do not redo the same expensive certificate merely to inflate counts. |
| P1 | #803 RN/RC/ANT and #805 DO/BG/BL/GE/TE | Compare author accepting code/result semantics with this pass's independent reconstructions; review the remaining full packages if they will be shipped as trusted evidence. RN has two jets; RC's displayed minima only one. Correct the three small statement/citation issues in REPORT.md with explicit dispositions. |
| P1 | #818 CCT/SSQ | Read remaining attempt/source files, certify the selected actual Li_2 endpoint-sample prefixes and their entire arithmetic contract. Do not confuse finite sample energy, orthogonal detail, or the infinite coarse bound. |
| P1 | #825/#826/#828/#829 | Complete author checker/application contracts for any retained executables; preserve all prime powers, measure weights, geometric-domain conditions and cutoff-versus-product distinctions. Carry the eleven-prime N=32 wording correction. |
| P1 | #804 MW | If the large N=65536 work campaign is cited, audit/replay its full tail and accepting arithmetic or explicitly leave it as author-reported. The small reviewer W3 check does not cover it. |
| P1 | #811/#814/#817/#823 and TSR | Review remaining auxiliary attempts, analytic-source locks, norm/inner-factor conventions and proposed connecting arrows. Finish the source/library/package obligations already listed in earlier reviews. The all-rank affine classification is not global automorphy. |
| P2 | Classical/imported dependencies | Keep exact publication/normalization hypotheses, including finite-height zero verification, Balazard-Saias conditional scope, Brun-Titchmarsh versus RH-conditional Cramer, critical-line convexity and Hardy source domains. Rerun external historical computations only if necessary for the chosen acceptance claim. |

All 45 frozen principal packets have now been read at main-argument level. Remaining rows above are **not** a demand to solve RH or prove every open arithmetic upper bound. Give each executable/certificate/source interface a disposition: cleared at a precise scope, exploratory only, or held with a named missing check. A paper component may be extractable while its author code remains untrusted or unshipped.

## 3. Final handoff, then integration

The final review should produce a component-level extraction list with current sources, mandatory repairs, inherited versus newly reconstructed evidence, shared results/aliases, and open premises. Keep each norm, target, support, frequency cutoff, window and asymptotic quantifier explicit. In particular preserve the unit-window sign, the graph bounds and their real limitations in the future public account.

After that review, construct a separate integration branch from **then-current main**. Copy only selected current statements/proofs/evidence and the reviews needed for provenance; preserve exploratory work with its proposed status. Do not merge PR #827 or a long research branch wholesale to manufacture scientific coverage. The integrated branch must then be reviewed and validated at its exact tree before any final merge.
