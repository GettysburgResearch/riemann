# O-0601 — Prime-power edge scans produced deep positive near misses

Claim ID: O-0601  
Title: Prime-power edge scans produced deep positive near misses  
Status: EMPIRICAL  
Authoring agent: `gpt56-01-a`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `D-0001`, `X-0601`  
Scope: enumerated ordinary-mpmath cells only  
Related counterexample candidates: none

## Observation

An event-directed search of the cutoff-free real-even matrix found no negative
cell, but it found narrow reductions that the original integer/log grid did not
resolve.

The main scan covered 72 consecutive prime-power intervals from `q=2` through
`q=263`, band `N=12`, and 11 fractional log-offsets per interval: 792 matrix
cells at 85 decimal digits. No empirical negative occurred.

The strongest relative reductions included:

| interval | best sampled fraction | threshold value | best value | ratio |
|---|---:|---:|---:|---:|
| `5 -> 7` | 0.98 | `4.34338e-17` | `2.28102e-22` | `5.2517e-6` |
| `3 -> 4` | 0.98 | — | — | `2.0476e-5` |
| `4 -> 5` | 0.98 | — | — | `3.9546e-5` |
| `2 -> 3` | 0.98 | `1.36685e-3` | `1.05254e-7` | `7.7005e-5` |
| `13 -> 16` | 0.98 | — | — | `3.2864e-3` |

A refined search in `97 -> 101`, `N=12`, found an interior minimum near
fraction `0.0962` with

\[
 \lambda_{\min}\approx
 5.18080693547815707234989428698\times10^{-44}.
\]

The sign remained positive at 220 decimal digits. At the same cutoff, every
band `1 <= N <= 30` tested positive; the `N=30` value was approximately
`4.0854e-83` at 260 digits.

Thirty-five exact prime-power thresholds through `q=97` were also evaluated at
`N=20` and 170 digits, all positive. Representative odd-sector checks were
positive and substantially larger than the corresponding even minima.

Finally, the Lerch-resummed no-prime regime was checked for `N<=6` at
`L in {1e-1,1e-2,1e-3,1e-6,1e-9,1e-12}`. All values were positive; the
minimum increased from about `0.9839` at `L=1e-1` to about `26.1438` at
`L=1e-12`.

## Classification

Every sign in this file is ordinary arbitrary-precision evidence. No directed
rounding or entrywise ball enclosure was used. This is a negative search
record, not evidence for RH and not a universal positivity claim.

## Interpretation

The exact edge jump is real and often produces dramatic reductions, but the
smallest eigenvector nearly annihilates the endpoint moment `M_0`, and the
smooth background motion compensates the frozen negative rank-one model. The
correct discovery problem is therefore a continuous avoided-crossing search,
not a threshold-only scan.

## Gap audit

- Only the enumerated cutoffs, bands, and precisions were evaluated.
- Tiny positive eigenvalues are especially sensitive to transcription and
  precision errors.
- The finite dictionary normalization is still awaiting independent audit.
- No result excludes a negative at a larger band, different interval, or
  untested offset.

## Suggested next attack

Use interval arithmetic on the deepest positive cells to validate the matrix
assembly, then shard adaptive minimization over all `(q,N)` pairs. Candidate
promotion remains blocked until a stable negative survives a second backend and
the exact dyadic checker.
