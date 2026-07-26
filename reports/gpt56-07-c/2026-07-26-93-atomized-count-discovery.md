# Atomized count deflation and new-candidate reconnaissance

Agent: `gpt56-07-c`  
Issue: #93  
Branch: `cursor/total-count-xi-production-7f09`  
Date: 2026-07-26

## Starting hypothesis

The completed PR71 count table might support stronger discovery computations
than concentric total-count subtraction. In particular, exact endpoint values
`N(T+-R)` could localize asymmetric zero mass at shifted direct-xi ordinates,
and scale-normalized ranking could distinguish genuine spectral near-nullity
from clustered-node Vandermonde factors.

## Approaches attempted

1. Audited new concurrent PRs on overlapping count envelopes, selected-factor
   removal, and normalized minors to avoid duplicating their interfaces.
2. Derived L-9307: consecutive exact endpoint counts determine disjoint atom
   multiplicities, each reusable at a shifted ordinate with its own
   farthest-endpoint distance.
3. Implemented a fail-closed atomized profile in the PR71 adapter.
4. Replayed the dense fine-mesh minimum using the atomized endpoint profile.
5. Scanned 65 exact ordinates on a `T+-8` mesh with 16 direct-xi points each.
6. Escalated the only negative 256-bit midpoint using an existing 512-bit
   primitive at the same exact ordinate.

## New results

The retained endpoint counts determine 17 consecutive intervals, 12 of which
have positive mass. Their multiplicities sum to the certified total of 70.

At the dense local basin, atomization improves the deflation and moves the
minimum from shift `477/1024` to `483/1024`. The exact order-four interval is:

```text
[8.15927411303488367082543395993660298195214288308488e-104,
 8.15927411303488367082665424432172959892044923176279e-104].
```

It is strictly positive.

The wide scan found one negative midpoint at shift `1/2` in 256-bit discovery
arithmetic. A 512-bit recomputation gave the positive midpoint

```text
+2.13337193847624842601824707095786756e-103.
```

The apparent negative was precision cancellation and is refuted.

## Candidate counterexamples

None. No midpoint survived escalation and no `Z-####` identifier is justified.

## Certified computations

- Exact atom counts reconstructed from all unique endpoint count balls.
- Exact shifted atom radii and cumulative profile.
- One 512-bit atomized direct-xi order-four certificate.
- Strict positive sign at the atomized fine minimum.

## Failed approaches

- Raw clustered-node determinant magnitude dramatically overstated promise.
  Concurrent normalized-minor work confirms that the tiny scale is largely
  Vandermonde geometry.
- One wide-scan negative midpoint was a 256-bit precision ghost.
- Further refinement of the same PR71 center did not produce a sign crossing.

## Potential errors and proof boundary

- L-9307 requires consistent endpoint-open/closed semantics.
- Every endpoint count ball must isolate a unique integer.
- Common xi scaling must remain point-independent.
- Midpoint scans are empirical filters only.
- Independent count and xi reproduction plus L-9303/L-9306/L-9307 review remain
  required for any future negative.

## Files changed

- `claims/lemmas/L-9307-atomized-count-endpoint-deflation.md`
- `experiments/X-9302-total-count-zero-deflation/build_pr71_total_count_certificate.py`
- `experiments/X-9302-total-count-zero-deflation/results/pr71-wide-scan/`
- `experiments/X-9302-total-count-zero-deflation/results/pr71-shift-fine/`

## Claims affected

- `L-9306`: renumbered shifted-count reuse lemma to avoid concurrent claim-ID
  collisions.
- `L-9307`: new atomized endpoint-count lemma, `PROPOSED`.
- `X-9302`: widened candidate reconnaissance; no negative candidate.

## Recommended next actions

1. Stop refining the now-certified-positive PR71 center.
2. Rank new count centers with normalized direct-xi minors before paying for
   Turing counts.
3. At a new center, request asymmetric endpoint counts adaptively so L-9307 or
   the general overlapping-envelope LP forces the most near-side mass.
4. Independently reproduce the atomized fine certificate.

## Organizational improvement ideas

Claim IDs must be checked against concurrent draft branches before publication.
Candidate rankings should report normalized moats and precision-survival, not
raw determinant magnitude alone.
