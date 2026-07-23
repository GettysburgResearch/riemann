# Agent session report — complete phase-backend comparison

Agent: `gpt56-01-c`  
Issue: #42  
Branch: `agent/gpt56-01-c/42-optimized-carrier-continuation`  
Date: 2026-07-23

## Starting hypothesis

The long-double phase backend used in the complete carrier stream might move a
small leading margin materially, even after the exact archimedean and pole
correction budget was shown negligible.

## Approaches attempted

1. Derived an exact weighted phase-perturbation bound for the D-0801 Toeplitz
   matrix and for one frozen Rayleigh vector.
2. Converted the X-0901 frozen-vector absolute weight sum into a required common
   phase radius.
3. Independently recomputed every prime-power phase through `c=10^8` using
   binary128 logarithm, multiplication, and reduction.
4. Used Kahan long-double accumulation in both paths and compared the complete
   Toeplitz matrices.
5. Attempted a decade-higher binary128 stream; recorded the performance barrier
   rather than treating a partial stream as evidence.

## New results

The exact L-0902 survival inequality is

```text
||S_tilde-S|| <= sum_q Lambda(q)/(pi sqrt(q)) eta_q.
```

For the frozen X-0901 `c=10^10` vector, the recorded data require a common phase
radius below `1.2306921641349523e-6` after L-0901's correction budget.

The complete `c=10^8` comparison included 5,762,859 prime powers. The
binary128-phase margin remained positive at `+0.006641474117036417`. Relative
to long-double phase reduction, the margin moved by about `-1.619e-6`, and the
Toeplitz operator moved by about `8.045e-6`.

## Candidate counterexamples

None. No `Z-####` identifier was allocated.

## Certified computations

The phase perturbation inequality is an exact finite algebraic reduction, but
its status remains `PROPOSED` pending review. The backend results are ordinary
numerical computations; binary128 is not treated as a directed ball backend.
Three software tests pass.

## Failed approaches

A fully binary128-transcendental `c=10^9` stream exceeded the session execution
budget. The failure is computational, not mathematical. It demonstrates that a
production verifier should be vector-specific and checkpointed instead of
rebuilding a full interval eigensystem.

## Potential errors

- binary128 library functions are not guaranteed here to be correctly rounded;
- the two backends share the prime enumeration and deposition algebra;
- Kahan accumulation is not a proof enclosure;
- the frozen vector and its phase weight are ordinary numerical objects;
- D-0801/L-0801 and the explicit-formula normalization remain proposed.

## Files changed

- `claims/lemmas/L-0902-phase-perturbation-survival.md`;
- `claims/observations/O-0903-phase-backend-comparison.md`;
- `experiments/X-0904-phase-backend-comparison/`;
- this append-only report;
- an integrator-ready registry patch.

## Recommended next actions

1. Export a frozen leading vector as dyadic coefficients.
2. Accumulate the fixed-vector complete prime sum and its absolute phase weight
   in one coverage-checked stream.
3. Replace binary128 midpoint phases with MPFR/Arb outward complex balls.
4. Use L-0901 and L-0902 to combine nonprime, phase, accumulation, and vector
   rounding budgets in one exact final inequality.
