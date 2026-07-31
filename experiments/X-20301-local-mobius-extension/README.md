# X-20301 — Local Möbius radical extension

This experiment is the exact finite regression for `L-20301/L-20302`.

Run:

```bash
python3 verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json

python3 -m unittest discover -s tests -v

sha256sum -c SHA256SUMS
```

The checker uses only the Python standard library and
`fractions.Fraction`.

## Model

The target density is piecewise constant on `[2,5]`. The cutoff is `N=3`, so
`N*a-b=1>0`. A normalized correction supported on `[1/2,1)` enforces the
source integral exactly without changing the arithmetic image on `[2,5]`.

The verifier exhausts every piecewise-constant reconstruction cell, rather
than checking a few sample points. Three separate points below the support
exercise the explicit lower tail.

## Verdict

```text
CERTIFIED_EXACT_LOCAL_MOBIUS_RADICAL_EXTENSION
```

## Nonclaim

The finite model verifies the algebraic extension and residual formulas only.
The production RH route still needs a uniform Weil-form/Schur bound for the
explicit lower-tail operator.
