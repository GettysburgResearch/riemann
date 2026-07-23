# X-2801 — Exact piecewise-carrier correction budget

Experiment ID: `X-2801`  
Agent: `gpt56-04-c`  
Issue: #28  
Status: `PARTIAL / exact algebraic checker`  
Date: 2026-07-23

## Question

Can the exact D-0801 archimedean and pole terms overturn the very small positive
complete-leading carrier margin reported in draft PR #44?

## Result

L-2801 independently reduces both terms to compact cellwise Toeplitz formulas.
L-2802 then avoids an oscillatory quadrature entirely by bounding the complete
normalized correction for every unit vector.

For

```text
c = 10^11
K = 1024
T = 4709203636353.65
```

`verify_correction_budget.py` proves using exact rational arithmetic that

```text
correction radius =
98759175269343099756340 /
79835755999127184820324325961

correction radius < 1/750000
```

The exact radius is approximately `1.2370293741e-6`. PR #44's empirical
leading margin is approximately `2.6896626427e-4`, but the latter is not a
rigorous interval.

## Checker

Schema:

```text
riemann.piecewise-carrier-correction-budget.v1
```

The checker takes an exact rational carrier, decimal-power cutoff, and cell
count. It computes a universal correction radius using only integers and
`fractions.Fraction`. An optional separately produced leading-margin interval
is widened by that radius.

Verdicts:

- `CERTIFIED_POSITIVE` when the widened lower endpoint is positive;
- `CERTIFIED_NEGATIVE` when the widened upper endpoint is negative;
- `UNRESOLVED` otherwise.

The checker does not establish the analytic provenance of a supplied leading
interval and does not audit the Guinand--Weil normalization.

## Reproduction

```bash
python -m unittest discover -s tests -v
python verify_correction_budget.py \
  certificates/target-budget-c1e11.json
```

The optional mpmath validation layer can be exercised through the same test
suite. It is independent of the X-0701/X-0801 source code and checks:

- cellwise autocorrelation endpoints;
- compact versus finite-transform pole evaluation;
- the `K=1` compact archimedean formula in two algebraic arrangements.

## Files

- `verify_correction_budget.py` — proof-producing exact rational checker;
- `compact_corrections.py` — independent non-rigorous formula validation;
- `certificates/target-budget-c1e11.json` — actual parameter budget request;
- `certificates/synthetic-positive-threshold.json` — checker control only;
- `certificates/synthetic-negative-threshold.json` — checker control only;
- `results/target-budget-output.json` — exact retained result;
- `results/tests.txt` — test transcript;
- `tests/` — ten adversarial and formula tests.

## Classification

- L-2801 formulas: `PROPOSED` pending independent review.
- L-2802 correction inequality: `PROPOSED` pending independent review.
- Rational checker arithmetic and target fraction: exact finite computation.
- Compact mpmath controls: ordinary high precision, not certified.
- PR #44 leading margin: empirical and not imported as proof data.
- Counterexample status: none.

## Remaining proof bottleneck

The dominant missing item is now the complete prime side, not the omitted
archimedean/pole correction. A directed producer must freeze a dyadic vector,
enclose all huge phases and all prime-power accumulation, and emit a leading
margin interval. At the current target, separation by `1/750000` is enough.
