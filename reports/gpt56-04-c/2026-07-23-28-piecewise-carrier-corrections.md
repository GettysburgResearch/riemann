# Agent report — exact correction budget for the optimized piecewise carrier

Agent: `gpt56-04-c`  
Issue: #28  
Branch: `agent/gpt56-04-c/28-piecewise-carrier-exact-corrections`  
Date: 2026-07-23

## Starting hypothesis

The omitted exact D-0801 archimedean and pole blocks might be comparable to the
`+2.6896626427e-4` high-carrier leading margin in PR #44 and could conceivably
change its sign. Before another multi-billion-term prime continuation, the
size of those corrections should be decided analytically.

## Approaches attempted

1. Re-derived the piecewise cell autocorrelation without importing X-0701 or
   X-0801 code.
2. Inserted that autocorrelation into the regularized digamma integral.
3. Derived the exact compact archimedean Toeplitz path.
4. Derived the pole term both from Fourier inversion and from finite cell
   transforms at `-T+-i/2`.
5. Recast the normalized archimedean term as an expectation against the Fourier
   energy probability measure `|W_v(u)|^2/h`.
6. Bounded central Fourier mass by an `L1`/total-variation crossover.
7. Bounded the remote tail with a global digamma estimate.
8. Bounded the pointwise digamma asymptotic by Binet's formula.
9. Bounded the pole by exact cell antiderivatives and Cauchy--Schwarz.
10. Converted every transcendental comparison in the final numerical budget to
    rational bit-length and elementary constant bounds.
11. Implemented a standard-library exact checker and a separate mpmath formula
    validation module.

## New results

### Proposed exact formulas

L-2801 gives compact one-dimensional Toeplitz integrals for the exact D-0801
archimedean and pole Rayleigh values, plus an independent finite-transform pole
formula.

### Proposed universal bound

L-2802 gives a vector-independent rational correction radius. At the PR #44
parameters the exact checker obtains

```text
98759175269343099756340 /
79835755999127184820324325961
```

which is strictly below `1/750000` and approximately `1.23703e-6`.

### Strategic consequence

The PR #44 empirical leading margin is about 217 times larger than the omitted
correction budget. The exact archimedean and pole blocks are therefore not the
likely source of a crossing at this cell. The proof bottleneck has moved to
directed prime phases and accumulation.

## Candidate counterexamples

None. No strict negative interval was produced and no `Z-####` identifier is
allocated.

## Certified computations

The correction-budget checker uses only integers and exact rational arithmetic.
Ten tests pass. The source formulas themselves remain `PROPOSED` pending
independent analytic review.

## Failed or rejected approaches

- Direct real-line numerical integration of the archimedean term converged too
  slowly for proof use because step envelopes produce `1/u^2` Fourier-energy
  tails. It was not retained as evidence.
- Direct highly oscillatory compact quadrature at `T about 10^12` was rejected;
  the universal bound is both stronger and easier to audit.
- The PR #44 decimal margin was not inserted into an apparently certified JSON
  object because it lacks directed rounding.

## Potential errors

- A project-level `2*pi` or source-sign mismatch could invalidate the inherited
  normalization.
- The Fourier first-moment estimate and global digamma bound need independent
  reconstruction.
- D-0801's step regularity may be insufficient for the final selected explicit
  formula without mollification.
- The rational checker proves only the correction budget and trusts the
  provenance of any leading interval supplied to it.

## Files changed

- `claims/lemmas/L-2801-piecewise-carrier-exact-corrections.md`
- `claims/lemmas/L-2802-piecewise-carrier-correction-budget.md`
- `claims/observations/O-2801-optimized-carrier-correction-budget.md`
- `experiments/X-2801-piecewise-carrier-corrections/README.md`
- `experiments/X-2801-piecewise-carrier-corrections/verify_correction_budget.py`
- `experiments/X-2801-piecewise-carrier-corrections/compact_corrections.py`
- certificates, results, tests, integration patch, and this report

## Claims affected

- L-2801 — new, `PROPOSED`
- L-2802 — new, `PROPOSED`
- O-2801 — new, `PARTIAL`
- X-2801 — exact algebraic checker plus non-rigorous controls
- Issue #28 — remains open
- no candidate claim

## Recommended next actions

1. Independently review L-2801 and L-2802.
2. Freeze and commit the PR #44 `c=10^11`, `K=1024` vector.
3. Implement directed phase balls for `T log(q)` and exact fixed-vector
   accumulation.
4. Ask the exact checker to separate the leading interval from zero by
   `1/750000`.
5. Independently audit the explicit-formula normalization and D-0801
   admissibility before any sign promotion.

## Organizational improvement ideas

Every asymptotic leading screen should publish a separately checkable
**omitted-term budget**. This prevents teams from spending large resources on
exact corrections that are provably too small while the dominant numerical
error lies elsewhere.
