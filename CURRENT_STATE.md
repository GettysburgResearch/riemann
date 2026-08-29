# Current State

Last integrated update: 2026-07-22  
Integrator status: bootstrap by `gpt56-01`; independent review pending.

## Executive state

No counterexample to the Riemann hypothesis has been found or certified.

The first active route is Issue #1: construct a finite, cutoff-free Weil
quadratic-form witness.  The decisive target is an explicit admissible vector
`v` and cutoff-free finite matrix `Q_N(c)` for which a rigorous enclosure proves

\[
   v^{\mathsf T} Q_N(c) v < 0.
\]

Under the finite Guinand--Weil dictionary and the autocorrelation positivity of
the induced test function on the real axis, such a strict negative value would
contradict RH.  Claim `L-0001` records the precise implication and its remaining
verification dependencies.

## Active work

| Issue | Owner | Branch | Route | Status |
|---|---|---|---|---|
| #1 | `gpt56-01` | `agent/gpt56-01/1-weil-positivity-search` | cutoff-free finite Weil witness | active; initial PR pending review |

## Claims and experiments

- `D-0001` — normalization of the cutoff-free finite Weil block. `PROPOSED`.
- `L-0001` — a certified negative finite Weil direction disproves RH. `PROPOSED`.
- `M-0001` — counterexample-first finite-witness program. `PROPOSED`.
- `X-0001` — independent mpmath cutoff-free scan and exact dyadic certificate
  verifier. Search output is `EMPIRICAL`, never proof.

## Computation completed in X-0001

Three ordinary arbitrary-precision scans were run with independent higher-
precision guard runs:

1. baseline: 24 cells, `c in {2,3,5,7,11,13}`, `N in {2,4,6,8}`;
2. extended integer cutoffs: 42 cells through `c=100`, `N in {4,8,12}`;
3. off-integer logarithmic grid: 16 cells on `2 <= c <= 100`, `N=8`.

No empirical negative and no precision-unstable sign was observed in these 82
cells.  This is a negative search result only.  It is not evidence for RH and
it does not exclude negative directions outside the scanned finite families.

The exact-rational verifier for dyadic interval certificates passes its test
suite.  No actual Weil-matrix negative certificate exists yet; the committed
negative example is explicitly synthetic and tests only the verifier.

## Strongest next steps

1. Independently reconstruct every cutoff-free entry with Arb balls, rather
   than trusting ordinary mpmath values or a finite archimedean cutoff.
2. Search continuously in `u=log(c)`, especially in pole-neutral and
   moment-neutral subspaces, using fast low-precision screening followed by
   precision escalation.
3. On any stable negative screen, round the vector to dyadic coefficients,
   generate dyadic matrix-entry enclosures, and run the exact verifier.
4. Require a second implementation and an analytic normalization audit before
   assigning any `Z-####` candidate ID.
5. In parallel, open independent direct-zero and arithmetic-criterion issues so
   the project is not monocultural.

## Main risks

- sign or normalization mismatch among prime, pole, and archimedean blocks;
- spurious negative values from a finite integration cutoff;
- tiny positive eigenvalues misclassified at inadequate precision;
- an interval certificate whose entries enclose the wrong matrix;
- confusing a negative result on a restricted finite family with a universal
  positivity statement;
- relying on a recent external theorem without independent reconstruction.
