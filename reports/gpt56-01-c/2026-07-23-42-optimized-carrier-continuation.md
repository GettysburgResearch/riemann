# Agent session report — optimized carrier continuation

Agent: `gpt56-01-c`  
Issue: #42  
Branch: `agent/gpt56-01-c/42-optimized-carrier-continuation`  
Date: 2026-07-23

## Starting hypothesis

The complete D-0801 margin at `c=10^10` might cross zero when PR #37's 1,024-cell Toeplitz family is evaluated at the much lower carrier basin found independently in the earlier carrier search, rather than at PR #37's original carrier.

## Approaches attempted

1. Recomputed the complete prime-power operator at cutoffs `10^8` through `10^11` with exact contiguous shard coverage.
2. Doubled the piecewise envelope from `K=1024` to `K=2048` at `c=10^10`.
3. Froze the leading `c=10^10`, `K=1024` vector and accumulated complete carrier moments through order six.
4. Applied an explicit Taylor remainder bound to local carrier shifts.
5. Evaluated an independent high-height `xi'/xi` criterion near the same carrier using a Riemann--Siegel curvature screen and high-precision scalar escalation.

## New results

### Empirical complete-prime facts

At `T=4709203636353.65`, every complete leading margin remained positive:

- `c=10^8`, `K=1024`: `+0.006643091775833554`;
- `c=10^9`, `K=1024`: `+0.0023504233978552946`;
- `c=10^10`, `K=1024`: `+0.0006076603725748697`;
- `c=10^10`, `K=2048`: `+0.0006027589005261902`;
- `c=10^11`, `K=1024`: `+0.00026896626427230785`.

The `10^11` computation included exactly `4,118,054,813` primes and `28,156` higher prime powers. The coverage-checked merger accepted 50 contiguous shards and rejected no parameter inconsistency.

### Empirical local-optimality fact

The frozen-vector quadratic stationary shift was approximately `-1.025e-6` and improved the margin by only about `3.1e-12`. The order-six Taylor remainder was explicitly bounded, and no local fixed-vector crossing occurred.

### Empirical independent cross-check

A 401-point no-remainder curvature grid found no negative point. At the grid minimum, ordinary high-precision values of `Re(xi'/xi)` at real parts `0.5001`, `0.501`, and `0.505` were all positive. The closest was about `+0.00307585840221`.

## Candidate counterexamples

None. No `Z-####` identifier was allocated.

## Certified computations

The following are exact finite-integer or exact-formula controls, not a certified matrix sign:

- contiguous segment-range validation;
- prime plus higher-prime-power count identities;
- unique higher-power-stream rule;
- analytic Taylor-remainder formula.

All matrix and special-function signs remain noninterval numerical results.

## Failed approaches

1. Increasing equal-cell resolution beyond 1,024 produced negligible gain.
2. Tiny local carrier shifts cannot remove the positive `c=10^10` margin.
3. Blind decade cutoff continuation narrowed but did not cross the margin.
4. The independent pointwise criterion did not show a negative at the same spectral basin.

## Potential errors

- inherited D-0801 prime coefficient or sign may be wrong;
- huge phase reduction is not enclosed;
- binary64 accumulation can hide small errors;
- exact archimedean and pole corrections may change the leading margin;
- piecewise envelopes may need smoothing to meet the exact admissibility class;
- the Riemann--Siegel curvature screen omits its remainder.

## Files changed

- `claims/observations/O-0901-optimized-carrier-cutoff-ladder.md`;
- `claims/methodology/M-0901-complete-carrier-continuation.md`;
- `experiments/X-0901-optimized-carrier-continuation/`;
- `integration/gpt56-01-c-registry-patch.md`;
- this report.

## Claims affected

- Adds `O-0901` (`EMPIRICAL`).
- Adds `M-0901` (`PROPOSED`).
- Adds `X-0901` (`EMPIRICAL`).
- Does not modify or promote D-0801/L-0801.

## Recommended next actions

1. Derive and evaluate the exact D-0801 archimedean and pole Rayleigh corrections on the frozen low-margin vector before another decade-scale prime stream.
2. Replace huge-phase arithmetic with directed complex balls on fixed vectors.
3. Search joint `(T,c)` basins between decade endpoints using complete block updates, not only larger cutoffs.
4. Independently review the D-0801 admissibility and Toeplitz orientation.
5. Continue the `xi'/xi` route with proof-grade balls only after deterministic reconnaissance nominates an actual negative midpoint.

## Organizational improvement ideas

Every expensive complete-prime run should emit a small coverage manifest and a separate compact mathematical summary. Carrier-local derivative moments should be accumulated in the same pass as a finalist, so local optimization never requires repeating billions of phases.
