# X-0902 — Uniform correction bound for the optimized carrier basin

Status: proposed analytic inequality plus ordinary floating evaluation.  
Agent: `gpt56-01-c`  
Issue: #42  
Dependency: L-0901 and the D-0801/L-0801 carrier normalization.

## Question

Can the exact archimedean and pole blocks, omitted by the high-carrier leading
screen in X-0901, reverse the sign of the lowest complete-prime margins?

## Result

L-0901 gives a vector-independent normalized operator bound

```text
B_arch = [(K/L)(log K + 2) + 6K + 5 + 1/L] / (pi T)
B_pole = 4 sqrt(c) K^2 / (pi L T^2)
```

for `L=log(c)`. At the lowest X-0901 cell

```text
c = 10^11
K = 1024
T = 4709203636353.65
```

the ordinary evaluation is

```text
B_arch = 4.400400811105406e-10
B_pole = 7.516345184600634e-16
B_total = 4.4004083274505903e-10
```

against the reported complete-prime leading margin

```text
+2.6896626427230785e-4.
```

Thus the correction bound is smaller by a factor above `6.1e5`.

This is **not** a proof that the cell is positive, because the prime phases,
accumulation, and leading eigensolve are not interval-certified. It narrows the
proof target: exact archimedean and pole matrices cannot plausibly supply the
missing crossing; the next proof-grade work belongs on the complete prime
Rayleigh value and its huge phases.

## Reproduce

```bash
python correction_bound.py --output results/correction-bound-summary.json
PYTHONPATH=. python -m unittest discover -s tests -v \
  > results/tests.txt 2>&1
python -m py_compile \
  correction_bound.py \
  tests/test_correction_bound.py \
  tests/test_residual_identity.py
sha256sum results/correction-bound-summary.json results/tests.txt \
  > results/SHA256SUMS
```

## Files

- `correction_bound.py` — parameter validation and bound evaluation.
- `tests/test_correction_bound.py` — scaling, failure, and promotion guards.
- `tests/test_residual_identity.py` — compact-form/residual identity and moderate-carrier bound check.
- `results/correction-bound-summary.json` — all X-0901 ladder rows.
- `results/tests.txt` and `results/SHA256SUMS` — test and provenance records.

## Proof boundary

- The derivation is in L-0901 and remains `PROPOSED` pending independent review.
- Decimal evaluation uses binary64, not directed rounding.
- The X-0901 margins copied into the result are empirical.
- No counterexample candidate is created.
