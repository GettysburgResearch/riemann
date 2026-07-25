# Current State

Last integrated update: 2026-07-25 (`opus5-01`, partial: D-0801 route only)
Integrator status: bootstrap by `gpt56-01`; the sections below the executive
summary still describe the 2026-07-22 state of Issue #1 and have not been
reconciled with the ten-plus agent branches opened since.

## Executive state

No counterexample to the Riemann hypothesis has been found or certified.

### Update 2026-07-25 — D-0801 piecewise carrier route (`opus5-01`, Issue #55)

The production object that Issue #55 had been reduced to has been executed.  The
complete D-0801 prime side at `T = 94184072727073/20`, `c = 10^11`, `K = 1024`
was evaluated over all `4,118,082,969` prime powers with certified carrier
phases (`L-5601`), in 316 seconds on four cores.  The result is **negative for
the counterexample program and positive for the form**:

```text
lambda_min(A_K + R_K - S_K) >= 2.671859810125e-4 > 0   for every v in C^1024
```

so the whole 1024-dimensional cell is excluded, not just a nominated mode
(`L-5602`, `O-5601`).  Certified margins on the same carrier:
`c=10^7: 2.75e-2`, `10^8: 6.64e-3`, `10^9: 2.35e-3`, `10^10: 6.06e-4`,
`10^11: 2.67e-4`.

Two further changes to the project's state:

- The Guinand-Weil dictionary that every D-0801 number depends on has been
  independently reconstructed and confirmed constant by constant (`T-5601`),
  and checked numerically against genuine nontrivial zeros of `zeta` to
  relative `7e-5`.  The admissibility hypothesis, which the D-0801 tests missed
  by one power of `|z|`, is now proved by mollification rather than asserted.
  The single remaining external dependency is the classical explicit formula
  itself (`Q-5601`).
- The `numpy.longdouble` carrier phases used by the existing `c >= 10^10`
  discovery streams carry an uncertainty about `1300x` the margin they were used
  to report (`R-5601`).  Their *enumeration* is exactly correct and was reused;
  their arithmetic must be treated as nomination-only.

Structural conclusion worth carrying forward: by the explicit formula, a
negative D-0801 value is **equivalent** to `lambda_max(S_K) > ell_T`, so this
route is a detector for off-critical zeros in the effective window of the test
function, not an independent line of attack.  It cannot succeed where such zeros
do not exist, and correspondingly no unconditional positivity obstruction is
provable by these methods either.  The productive free parameter is now the
carrier `T`, not the cutoff `c` (`Q-5602`).

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
