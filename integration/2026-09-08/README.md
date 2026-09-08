# Native-source integration candidate

**Status: prepared for review; not merged or activated. RH remains unproved.** The published baseline is still selected by [canonical/CURRENT.json](../../canonical/CURRENT.json). The [scientific reading path](../../research/integrated/native_sources/README.md) is organized by mathematics, not review chronology.

## Scope and preservation

This candidate begins at main `f99d9e3908dde4865377c75d9ca051c1f545bf4f`. Its controlling review is [PR #827](https://github.com/GettysburgResearch/riemann/pull/827) at `29237183dc6973cfa9bd953ac1710b7f00929d04`. The final uploaded bundle's 30 files reconstruct Git subtree `cb3693cc59cab61ef92c616558f97b2b5e201dd0`, exactly the remote pass-four tree. Earlier local handoff variants are preserved, not substituted for the published reviews.

The original source import is commit `35dc6094b0fb93c49d22141801a7e0767068e054`, whose sole parent is that main. It copies 35 exact source directories covering 45 selected packets and the unchanged dated review directory. No research or review branch history is merged. Older mathematical source directories, historical integrations, contributor instructions, license, workflows and trusted Lean sources remain unchanged.

The [source manifest](SOURCE_TREES.json) records complete tree identities and source commits. The [selection table](PACKETS.tsv) maps every packet to its current thematic statement and resident principal manuscripts. The controlling [component recommendations](../../reviews/2026-09-08-postintegration/pass4/EXTRACTION.tsv) and [final decisions](../../reviews/2026-09-08-postintegration/pass4/DECISIONS.tsv) remain immutable. A copied directory is not blanket acceptance of its claims or executables.

## Current mathematics and corrections

The cumulative README, status, results, approach map and open problems preserve earlier work. The [current statement guide](../../research/integrated/CURRENT_RESULTS.md) leads to the source-specific operator, residual, causal, prime-energy and structural chapters. The [proof library](../../research/integrated/native_sources/SOURCE_INDEX.md) includes useful predecessor results and failed mechanisms; the [evidence guide](../../research/integrated/native_sources/EVIDENCE.md) separates audited reconstructions from archival programs.

All six review qualifications are applied beside the affected statements and indexed in [REPAIRS.json](REPAIRS.json). The infinite Schur repair has a readable complete statement and proof. Original manuscripts and the [correction report](../../reviews/2026-09-08-postintegration/pass4/REPAIRS.md) are preserved separately. No new argument, stronger quantifier, finer numerical endpoint or graph-to-physical implication is approved by editorial consolidation.

The shared squarefree anchoring result is one mathematical selection with both sources credited. Geometric-reservoir/root-coupling and native-source/survival extensions remain separate. All RH-bearing upper bounds and the all-window sign remain open. Unselected author programs are archival unless independently selected under a documented evidence contract.

## Verification commands for the exact candidate

Use a clean full checkout containing the baseline commit and the candidate head. Fetch the integration branch normally, then record its full SHA in `HEAD_SHA`. Commit all intended changes before validation; the checker deliberately rejects working bytes that differ from HEAD, including changes hidden by Git status flags. Outputs must be outside the repository.

```sh
HEAD_SHA=$(git rev-parse HEAD)
python3 -I -S -B integration/2026-09-08/verify.py --expect-head "$HEAD_SHA" > /tmp/riemann-candidate-normal.json
python3 -I -S -B -O integration/2026-09-08/verify.py --expect-head "$HEAD_SHA" > /tmp/riemann-candidate-optimized.json
cmp /tmp/riemann-candidate-normal.json /tmp/riemann-candidate-optimized.json
python3 -I -S -B integration/2026-09-08/test_verify.py
python3 -I -S -B -O integration/2026-09-08/test_verify.py
```

The candidate check authenticates every selected source and review tree, checks baseline preservation, the 45-packet selection and six repair destinations, and scans the explicitly named current reading pages. It does not execute author research code, prove mathematics, or run the inherited graph resolver. Run that separate unchanged baseline check too, using new or empty output directories outside the checkout:

```sh
python3 -I -S -B integration/2026-09-06/hardening/verify.py --output /tmp/riemann-baseline-normal
python3 -I -S -B -O integration/2026-09-06/hardening/verify.py --output /tmp/riemann-baseline-optimized
```

The existing graph's missing-premise/RH guard remains intact. This candidate does not concatenate raw research edges into accepted implications or change the published resolver pointer. Refer to [VALIDATION.md](VALIDATION.md) for actually executed checks and limitations, not an inference of PASS from these instructions.

## Final integration review and activation

The next reviewer should use [FINAL_REVIEW.md](FINAL_REVIEW.md) against the exact PR head. Check the public statements against their selected sources and all six repairs, the preservation of older results, evidence boundaries, and the full-checkout commands above. New source commits require two-endpoint tree comparison rather than reuse of an old branch-title verdict.

After approval, activation must be a separately reviewed, explicit change: choose the current registry/manifest and verifier composition, reconcile the candidate qualifiers and affected historical open-status statements, run both verification layers on the final committed tree, and record the exact merge receipt. This branch does not pre-authorize a main merge, enable Actions, alter permissions, or complete the repaired Lean implementation.
