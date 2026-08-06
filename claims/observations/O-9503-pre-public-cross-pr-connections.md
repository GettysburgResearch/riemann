# O-9503 — Cross-PR connections exposed by the pre-public review

Claim ID: `O-9503`  
Status: **PROPOSED — CONNECTIONS ONLY; NO FROZEN PR IS RETROACTIVELY VERIFIED**  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Reviewed PRs: #4, #19, #21, #22, #23, #24, #27, #30, #33, #34, #37, #38, #40, #43

## Status boundary

These are new integration observations discovered during independent review.
They have not received independent review and do not alter the classifications
in `reports/gpt56-08/2026-08-01-pre-public-review-prs-4-43.md`.
A proposed repair or connection cannot retroactively verify a flawed or blocked
frozen claim.

## 1. One normalization audit unlocks four Weil/carrier branches

PRs #23, #27, #30, and #37 use different finite geometries, but their RH-facing
interpretation passes through the same object:

```text
D-0001 cutoff-free Guinand--Weil matrix
+ admissibility of the induced band-limited test
+ real-axis autocorrelation square
+ exact zero-sum identity.
```

Their event calculus, compact carrier kernels, source compression, and piecewise
Toeplitz deposition are separately useful and mostly elementary.  A single
independent proof card reconstructing `D-0001` from the classical explicit
formula should therefore be treated as shared infrastructure rather than being
reproved independently inside every descendant PR.

Proposed production consequence: after the common audit, use one exact primitive
matrix schema and one fixed-vector interval checker for all four carrier
families; only the source-to-matrix map changes.

## 2. Hybrid Robin coverage: CA chords first, canonical tree only on gaps

The following components fit without changing their individual proofs:

- #38 `L-3203`: an exact adjacent colossally-abundant contact pair whose endpoint
  Robin inequalities are strict certifies every integer between the contacts;
- #34 `T-2501/T-2502`: an exact canonical terminal stream certifies a bounded
  region, including cases whose canonical image lies below the Robin domain;
- #40 `L-3502`: a powered rational shared-budget envelope strengthens the tail
  prune used by the canonical tree.

Proposed scheduler:

1. certify exact CA transition/contact intervals and consume every covered
   integer interval by the concavity chord;
2. represent the uncovered transition-order gaps as explicit disjoint integer
   intervals;
3. run the canonical terminal verifier only on those gaps;
4. use the powered envelope as an optional stronger prune, while preserving the
   original size-aware ceiling as a fallback;
5. produce one sorted interval-union certificate whose verifier proves no gap or
   overlap and whose terminal records retain the finite upper endpoint.

This can greatly reduce a finite Robin proof object, but it remains a finite
range theorem unless an additional all-depth argument is proved.

## 3. Confluent positive-real certificates unify #38 and #43

PR #38 uses the multi-point positive-real/Pick kernel for

\[
F=\xi'/\xi,
\]

while PR #43 uses one-point horizontal derivatives and a shifted Stieltjes
moment hierarchy.  These are two finite compressions of the same conditional
zero-resolvent Gram.

For a positive semidefinite holomorphic kernel, finite value/derivative jets at
coalescing nodes form a positive semidefinite confluent Gram matrix.  This
suggests a mixed certificate containing:

```text
several right-half-plane xi'/xi values;
selected horizontal xi jets at the same or coalescing points;
one exact dyadic quadratic vector;
one directed negative quadratic-form endpoint.
```

The value-only principal block specializes to `L-3202`; an appropriate
coalescing horizontal block specializes to the `L-4102` moments/localizers.
A proof card must derive the exact derivative signs and factorial
normalizations before this is used.  No such mixed theorem is claimed verified
here.

Potential benefit: an off-line pole may be weak in a value-only matrix but
strong in a right-side derivative localizer; a confluent packet can combine the
two without evaluating unrelated high-height phases.

## 4. Verified-height results are exclusion tools, not positivity engines

PR #21's finite-height zero theorem and effective Jensen theorem combine with
#22's amplification barrier and #33's quartet window as follows:

- finite-height line location excludes low-height off-line candidates and gives
  a large finite Jensen-hyperbolicity range;
- an off-line zero immediately above the verified height can influence Li
  coefficients only at very large indices unless it lies appreciably off the
  line;
- once a certified off-line zero box exists, `L-3105` supplies a bounded
  factor-six index window for its quartet's negative algebraic contribution.

The missing step remains a rigorous complete Li coefficient, not the quartet
alone.  This connection improves target selection but does not turn a finite
height verification into RH.

## SERIOUS RESOLUTION PATH

No new full RH proof or disproof follows from these connections.  The strongest
new integration opportunities are:

1. a shared exact `D-0001` audit followed by a directed negative carrier search;
2. a hybrid CA/canonical finite Robin certificate with stronger powered prunes;
3. a confluent value/jet xi certificate for counterexample discovery.

Each remains either a finite extension or a finite counterexample architecture.
