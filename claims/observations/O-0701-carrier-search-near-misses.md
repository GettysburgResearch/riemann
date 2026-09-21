# O-0701 — Carrier-shifted search near misses and truncated-prime refutations

Claim ID: O-0701  
Title: Carrier-shifted search near misses and truncated-prime refutations  
Status: EMPIRICAL  
Authoring agent: `gpt56-01-b`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: D-0701, L-0701, L-0702, X-0701  
Scope: discovery computations only  
Related counterexample candidates: none

## Observation

At cutoff `c=10^7`, carrier heights above `3*10^12`, and carrier-lattice
dimensions 17 and 25, top-prime subsets produced ordinary floating-point
negative leading eigenvalues. Complete reevaluation using every one of the
665,134 prime-power terms through `10^7` made the representative values positive:

| Carrier | N | truncated screen | complete leading value |
|---:|---:|---:|---:|
| 3207174657920 | 8 | about -0.06397 | +0.48959298439425636 |
| 3184188297489 | 12 | about -0.10550 | +0.4528324147352132 |

The strongest retained complete leading near miss was

\[
 c=10^7,\quad T=3157430112465.479,\quad N=12,
\]

with ordinary numerical value

\[
 +0.18535251496676164.
\]

At the same carrier, increasing to `N=16` gave approximately

\[
 +0.18491323202279908.
\]

No complete leading negative and no full exact negative were retained.

## Interpretation

Prime-tail fluctuations are comparable to the distance from zero in aggressive
subset screens. Truncated-prime negativity is therefore not merely uncertified;
it can have the wrong sign by a large margin.

The complete near miss shows that carrier translation can bring a small finite
dimension substantially closer to the high-height Weil-positivity boundary than
the scalar triangular family, but it does not constitute evidence of an actual
negative direction.

## Numerical limitations

- NumPy double precision was used for matrices and eigensolvers.
- `numpy.longdouble` was used to reduce `T*log(q)` modulo `2*pi` in final checks,
  but no directed phase enclosure was produced.
- The recorded value is the high-carrier leading matrix, not the exact
  generalized eigenvalue of `P+R+A` relative to `G`.
- The compact correction terms were not interval-certified.

## Suggested next attack

Search larger cutoffs with complete-tail control, use subset screens only as
importance samplers, and hand any complete leading negative to a direct Arb
fixed-vector evaluator.
