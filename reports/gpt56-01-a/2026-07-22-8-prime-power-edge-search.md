# Agent report — prime-power edge and tiny-support search

Agent: `gpt56-01-a`  
Issue: #8, continuation of #1  
Branch: `agent/gpt56-01-a/1-prime-power-edge-jump`  
Date: 2026-07-22

## Starting hypothesis

The X-0001 grid may miss a negative excursion because a new prime-power term is
exactly zero at its admission threshold but has a negative one-sided derivative.
A second possibility is that taking `c=exp(L)` extremely close to `1` moves a
small band to very high spectral frequency, but the direct correction sums made
that regime computationally inaccessible.

## Approaches attempted

1. Derived the exact prime-power derivative jump in full and even coordinates.
2. Derived the first nonzero edge order under successive even-moment constraints.
3. Derived the exact susceptibility threshold for a frozen negative rank-one
   update and used it only as an event-ranking statistic.
4. Implemented an independent cutoff-free mpmath even-matrix assembler and
   shardable interval scanner.
5. Scanned every prime-power interval through `q=263` at `N=12` on an
   endpoint-biased log grid.
6. Re-ran deepest cells at increased precision, searched an interior minimum in
   `97 -> 101`, and checked all bands through `N=30` at the refined cutoff.
7. Checked exact thresholds through `q=97` at `N=20`.
8. Audited representative odd-sector blocks.
9. Derived exact Lerch-transcendent formulas for the four geometric correction
   sums and used them to reach `L=1e-12`.
10. Tested the frozen-background model against the full moving matrix.

## New results

### Proposed exact results

- `L-0601`: at `q=p^a`, the right-minus-left `u=log(c)` derivative jump is
  `-(2/(a*sqrt(q))) 11^T`; in even coordinates it is the corresponding
  `r_N r_N^T` update.
- `L-0602`: if `M_0=...=M_s=0`, the new `q` contribution begins negatively at
  order `epsilon^(4s+5)` with an explicit squared-moment coefficient.
- `L-0603`: exact rank-one susceptibility threshold
  `1/(r^T A^{-1}r)`.
- `L-0604`: exact Lerch resummation eliminating the `O(1/L)` direct-sum cost.

These are `PROPOSED` pending independent normalization and proof review.

### Empirical computation

- 792 `N=12` edge cells over 72 intervals through `q=263`: zero negatives.
- 35 `N=20` threshold cells through `q=97`: zero negatives.
- Refined `97 -> 101`, `N=12` minimum near fraction `0.0962`:
  `5.18080693547815707234989428698e-44`, positive at 220 digits.
- Same cutoff, all `1<=N<=30`: positive; `N=30` about `4.0854e-83` at
  260 digits.
- Representative odd-sector minima: positive and materially larger.
- Tiny-support scan `L=1e-1` through `1e-12`, `N<=6`: zero negatives.
- Nine automated tests pass.

## Candidate counterexamples

None. No `Z-####` identifier was allocated.

## Certified computations

None for the Weil matrix. Tests of finite algebraic identities pass, but all
special-function and matrix signs use ordinary mpmath rather than directed
balls.

## Failed approaches and useful negative results

1. **Threshold-only scan.** The new prime term vanishes exactly at the threshold,
   so threshold cells alone omit its edge effect.
2. **Frozen rank-one crossing prediction.** It can predict an in-interval
   crossing while the full moving matrix remains positive. Smooth background
   motion and vector rotation cannot be ignored.
3. **Moment-neutral primary edge search.** The condition `M_0=0` suppresses the
   edge through fourth order; every added moment condition delays it four more
   powers. Such subspaces need different offset schedules.
4. **Odd-sector shortcut.** Representative odd minima were positive and larger;
   no hidden negative appeared.
5. **Tiny-`L` frequency shortcut.** Lerch resummation made it feasible, but the
   tested minima increased as `L` decreased.

## Potential errors

- A shared sign or normalization error in `D-0001` remains the dominant analytic
  risk.
- Tiny eigenvalues require precision far above machine arithmetic.
- The exact Lerch identities do not make mpmath's `lerchphi` interval-rigorous.
- The adaptive search is finite and can miss an untested narrow minimum.
- The result file records raw-output hashes, but raw JSON is not committed.

## Files changed

- `claims/lemmas/L-0601-prime-power-derivative-jump.md`
- `claims/lemmas/L-0602-moment-neutral-edge-order.md`
- `claims/lemmas/L-0603-rank-one-susceptibility.md`
- `claims/lemmas/L-0604-lerch-resummation.md`
- `claims/observations/O-0601-edge-scan-near-misses.md`
- `claims/methodology/M-0601-event-directed-weil-search.md`
- `experiments/X-0601-prime-power-edge-search/*`
- this report

## Claims affected

`L-0601`, `L-0602`, `L-0603`, `L-0604`, `O-0601`, `M-0601`, `X-0601`.

## Recommended next actions

1. Independently reconstruct `D-0001/L-0001`; do not certify a negative for an
   unaudited matrix.
2. Add a directed-ball exporter for both the original sums and the Lerch
   resummation.
3. Shard adaptive interval minimization over `(q,N)` rather than expanding a
   uniform grid.
4. Use verified-zero-height information to design spectral targeting instead of
   relying only on small cutoffs and bands.
5. Preserve the exact event formulas as regression tests for any accelerated
   matrix path.

## Organizational improvement ideas

The issue registry should distinguish **event kernels**, **discovery scans**,
**entry enclosers**, and **exact checkers**. A candidate should link one artifact
from each layer. Raw large scans should be identified by deterministic
parameters and hashes, with compact summaries committed.
