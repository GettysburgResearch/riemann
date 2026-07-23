# X-2801 — Exact piecewise-carrier correction certificates

Experiment ID: `X-2801`  
Agent: `gpt56-04-c`  
Issue: #28  
Status: `PARTIAL / exact algebraic checkers`  
Date: 2026-07-23

## Question

Can the exact D-0801 archimedean and pole terms overturn the very small positive
complete-leading carrier margin reported in draft PR #44?

## Independent source reconstruction

L-2801 independently reduces both terms to compact cellwise Toeplitz formulas,
without importing the X-0701/X-0801 numerical core. The validation module checks
those formulas at moderate carriers against separately arranged expressions.

## Two exact correction certificates

### Self-contained fallback budget

L-2802 derives a deliberately coarse rational bound directly from Parseval,
Fourier total variation, digamma estimates, and finite cell transforms. At

```text
c = 10^11
K = 1024
T = 4709203636353.65
```

`verify_correction_budget.py` proves

```text
correction radius =
98759175269343099756340 /
79835755999127184820324325961

correction radius < 1/750000
```

This route is independent of the concurrent sharper operator argument.

### Exact specialization of the sharper operator bound

While this branch was in progress, the PR #44 base added L-0901, which obtains
a much sharper `O(1/T)` uniform operator bound by integrating the oscillatory
archimedean residual by parts. L-2803 independently checks its target constants
using exact rational arithmetic.

`verify_variation_budget.py` proves

```text
variation radius =
136091541158257193750 /
292731105330133011007855861857

variation radius < 1/2000000000
```

The exact value is approximately `4.6490290468e-10`.

PR #44's empirical leading margin is approximately `2.6896626427e-4`, about
`5.785e5` times the exact variation radius. That leading value is not a directed
interval and is not promoted by this experiment.

## Checker schemas

```text
riemann.piecewise-carrier-correction-budget.v1
riemann.piecewise-carrier-variation-budget.v1
```

Both checkers take an exact rational carrier, decimal-power cutoff, and cell
count. An optional separately produced leading-margin interval is widened by
the relevant radius.

Verdicts:

- `CERTIFIED_POSITIVE` when the widened lower endpoint is positive;
- `CERTIFIED_NEGATIVE` when the widened upper endpoint is negative;
- `UNRESOLVED` otherwise.

The checkers do not establish the analytic provenance of a supplied prime
interval and do not audit D-0801 admissibility or the Guinand--Weil
normalization.

## Reproduction

```bash
python -m unittest discover -s tests -v
python verify_correction_budget.py \
  certificates/target-budget-c1e11.json
python verify_variation_budget.py \
  certificates/target-variation-budget-c1e11.json
```

The committed test transcripts contain 18 passing tests in total. They cover:

- exact target fractions and strict threshold comparisons;
- safe synthetic positive and negative intervals;
- zero-touch rejection;
- schema and integer-type failures;
- non-power-of-two cell handling;
- cellwise autocorrelation endpoints;
- compact versus finite-transform pole evaluation;
- the `K=1` compact archimedean formula in two algebraic arrangements.

Synthetic threshold fixtures test checker logic only and are not mathematical
candidates.

## Files

- `verify_correction_budget.py` — self-contained fallback rational checker;
- `verify_variation_budget.py` — exact specialization of L-0901;
- `compact_corrections.py` — independent non-rigorous formula validation;
- `certificates/target-budget-c1e11.json`;
- `certificates/target-variation-budget-c1e11.json`;
- synthetic positive and negative controls;
- exact retained JSON outputs and test transcripts;
- `tests/` — adversarial arithmetic and formula checks.

## Classification

- L-2801 formulas: `PROPOSED` pending independent review.
- L-2802 fallback inequality: `PROPOSED` pending independent review.
- L-0901 sharper operator inequality: concurrent `PROPOSED` dependency.
- L-2803 rational specialization: `PROPOSED` pending review of L-0901.
- Checker arithmetic and retained fractions: exact finite computation.
- Compact mpmath controls: ordinary high precision, not certified.
- PR #44 leading margin: empirical and never used as proof input.
- Counterexample status: none.

## Remaining proof bottleneck

The dominant missing item is now unambiguously the complete prime side. A
directed producer must freeze a dyadic vector, enclose every huge phase and all
prime-power accumulation, and emit a leading-margin interval. Conditional on
L-0901, separation from zero by `1/2000000000` is sufficient at the current
target.
