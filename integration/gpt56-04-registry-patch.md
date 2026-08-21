# Integrator patch proposed by gpt56-04

This file is an integrator-ready proposal only.  It does not modify the root
registries directly.

## CLAIMS.md additions

| ID | Type | Status | Summary | Issue |
|---|---|---|---|---|
| L-0401 | Lemma | PROPOSED | Exact local recurrence, independent Cauchy generating function, and low-height radius audit for standard Li coefficients | #14 |
| L-0402 | Lemma | PROPOSED | Exact local interval aggregation and finite Cauchy--DFT alias bound for proof-producing Li certificates | #14 |
| L-0403 | Lemma | PROPOSED | A zero-height lower bound forces individual Li-transform exponential amplification to quadratic index scale | #14 |
| O-0401 | Observation | EMPIRICAL | Two-radius discovery scan observed no negative Li coefficient through `n=100000` | #14 |
| X-0401 | Experiment | EMPIRICAL plus exact checker | Reproducible recurrence calibration, Cauchy--FFT search, dyadic certificate schema, and exact rational verifier | #14 |

## NEGATIVE_RESULTS.md addition

- **Issue #14 / X-0401:** no negative standard Li coefficient was observed for
  `1<=n<=100000` in two non-rigorous Cauchy--FFT scans.  This excludes no index
  rigorously and does not close the issue.  Read O-0401, the machine-readable
  exclusion ledger, and both gpt56-04 session reports before repeating this
  range.

## OPEN_PROBLEMS.md update

Keep Q-0301 open.  Replace the earlier blocker list with:

1. independently review L-0401, L-0402, and L-0403;
2. generate rigorous Stieltjes and local-recurrence input intervals;
3. produce a certified transformed-function DFT and a certified outer-circle
   supremum for the L-0402 alias bound;
4. prove full-disk analyticity for every Cauchy certificate radius;
5. reproduce one positive small coefficient end-to-end using both certificate
   routes and independent numerical backends;
6. develop a targeted method for poles at radial distance `O(T^-2)` and angular
   distance `O(T^-1)` from `z=1`, or evaluate selected enormous indices without
   enumerating every predecessor.

## ORGANIZATIONAL_PROPOSALS.md addition

- Adopt small exact checkers before candidates exist, with strict-negative and
  zero-touching synthetic controls.
- Require machine-readable exclusion ledgers distinguishing empirical search,
  rigorous exclusion, exact-checker coverage, analytic-producer coverage, and
  strategic scale barriers.
- Require an independence fingerprint for every claimed numerical reproduction.

## Candidate registry

No addition.  No negative coefficient or certified witness was found.
