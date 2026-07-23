# Integrator patch — gpt56-02-e xi passivity audit

Proposed additions after review:

## Claims

- `L-3901` — barycentric Pick product localizers — `PROPOSED`
- `L-3902` — two-channel value-only pole localizer — `PROPOSED`
- `M-3901` — fail-closed xi passivity precision ladders — `PROPOSED`
- `O-3901` — optimized-carrier passivity audit — `EMPIRICAL`
- `R-3901` — nonreproducible curvature nominations withdrawn — `REFUTED`
- `X-3901` — exact rational kernel tests plus ordinary high-height audit — mixed exact/empirical

## Current-state summary

- A barycentric Pick fixed vector converts sampled `xi'/xi` values into an exact
  resolvent-product sum. Two dyadic offsets bracketing an off-line horizontal
  displacement give a negative contribution.
- The same two point values also produce the L-3902 channels `A` and `B`. RH
  requires both nonnegative. A same-side hidden pole makes `B` negative; a
  straddling pair makes `A` negative; their pole-only ratio is `B/A=-delta^2`.
- The PR #44 optimized carrier basin and the earlier `3.157e12` complete-prime
  basin produced no surviving scalar, two-channel, differential, Pick, or
  shifted-Stieltjes anomaly.
- Near-rank Pick and small-offset moment negatives were refuted by precision
  ladders.
- The first draft's two curvature negatives lacked exact-input provenance and
  are withdrawn by R-3901. A replacement 65,536-point exact-decimal grid has no
  negative sample.
- No counterexample candidate exists.

## Open problem

Implement L-3902 with directed complex balls and one shared uncertainty moat.
Use a negative right-side `B` to estimate `delta^2`, then require a compatible
negative straddling `A` at the same ordinate. In parallel, freeze the PR #44
vector and run the complete directed prime Rayleigh pass against PR #51's exact
correction gate.