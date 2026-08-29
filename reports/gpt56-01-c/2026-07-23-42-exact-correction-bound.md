# Agent session report — uniform exact-correction bound

Agent: `gpt56-01-c`  
Issue: #42  
Branch: `agent/gpt56-01-c/42-optimized-carrier-continuation`  
Date: 2026-07-23

## Starting hypothesis

The exact D-0801 archimedean or pole block might be large enough to overturn
the `+2.6896626427e-4` complete-prime leading margin at `c=10^11`.

## Approaches attempted

1. Rewrote the exact compact archimedean integral as the leading scalar plus a
   cosine-integral term and one oscillatory residual.
2. Expressed every normalized D-0801 autocorrelation as a piecewise-linear
   interpolation of finite lag correlations `c_d`.
3. Derived vector-independent variation bounds for the oscillatory residual.
4. Bounded the pole term by integration by parts against the finite-variation
   piecewise envelope.
5. Evaluated the resulting formula on every X-0901 ladder row and added tests.

## New result

Conditional on the D-0801/L-0702 block normalization, L-0901 proves

```text
||E_arch + E_pole||_op <= B_arch + B_pole
```

with explicit elementary formulas. At `c=10^11`, `K=1024`, and the optimized
carrier, the ordinary value is below `4.401e-10`, more than `6.1e5` times smaller
than the empirical leading margin.

## Interpretation

The omitted exact blocks are not the likely source of a sign crossing in this
basin. The dominant unresolved uncertainty is now the complete prime Toeplitz
matrix itself: huge-phase range reduction, accumulation, and eigensolver error.

## Candidate counterexamples

None. No `Z-####` identifier was allocated.

## Certified computations

The session provides a proof-form inequality, but the repository status remains
`PROPOSED` and the decimal evaluations are not directed-rounded. Six software
tests pass, including an independent numerical comparison of the original
compact archimedean formula with the residual identity at a moderate carrier.

## Failed hypothesis

The exact archimedean and pole corrections cannot be of order `1e-4` in this
high-carrier, finite-cell regime under the proposed formulas. Their uniform
bound is of order `1e-10`.

## Potential errors

- inherited explicit-formula sign or normalization error;
- an error in the compact archimedean identity;
- an incorrect Bernoulli-polynomial bound or variation endpoint;
- a stricter admissibility requirement for the discontinuous cell envelope;
- ordinary arithmetic in the displayed numerical bound.

## Files changed

- `claims/lemmas/L-0901-uniform-arch-pole-correction-bound.md`;
- `experiments/X-0902-carrier-correction-bound/`;
- this append-only report;
- an integrator-ready registry patch.

## Claims affected

- Adds `L-0901` (`PROPOSED`).
- Adds `X-0902` (proposed inequality evaluation; numerical outputs ordinary).
- Does not promote D-0801, L-0801, O-0901, or any candidate.

## Recommended next actions

1. Reproduce the bound independently and tighten it with actual autocorrelation
   coefficients if desired.
2. Freeze a leading vector and use directed complex balls for the complete prime
   Rayleigh sum.
3. Search joint carrier/cutoff minima between decade endpoints rather than
   extending the same carrier blindly.
4. Use L-0901 as a survival gate for any future complete-prime negative.

## Organizational improvement

Every high-carrier leading screen should ship with a uniform exact-correction
budget. This prevents expensive full correction assembly when a simple operator
bound already decides whether a leading sign can survive.
