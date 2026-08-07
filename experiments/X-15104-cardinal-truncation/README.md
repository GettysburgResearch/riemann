# X-15104 — Exact cardinal-truncation obstruction regression

Status: exact finite arithmetic / regression for `R-15102`.

## Objective

For

```text
D_N(x)=product_(m=-N)^N (x-m),
P_N(x)=sum_(n=-N)^N (-1)^n D_N(x)/(x-n),
```

`R-15102` proves analytically that `P_N` has no real root for every `N>=1`,
although the corresponding entire cardinal transforms converge locally
uniformly to the nonzero constant `pi`.

The checker independently reconstructs the integer numerator and uses an exact
`fractions.Fraction` Sturm chain to verify the finite ladder declared by the
certificate. It also verifies:

- degree `2N`;
- even parity;
- nonvanishing at every interpolation node;
- zero distinct real roots.

The all-`N` theorem is the alternating-series proof in `R-15102`; this experiment
is an adversarial implementation regression only.

## Run

```bash
cd experiments/X-15104-cardinal-truncation
python verify.py certificates/cardinal-N24.json \
  > results/cardinal-N24-verification.json
PYTHONPATH=. python -m unittest discover -s tests -v
```

Expected proof digest:

```text
dbb89c2554290c9e3231a080262de4a8bcae4626f1df4a8562a00ed74f6bec65
```

## Trust boundary

The checker uses only:

- Python integers;
- `fractions.Fraction`;
- exact polynomial division;
- Sturm variation counts at `+/- infinity`;
- JSON and SHA-256.

No floating-point arithmetic, polynomial root finder, special function, or
Riemann-zeta value enters the result.

The synthetic control with all-positive residues has all `2N` numerator roots
real, confirming that the zero-root result is tied to the alternating cardinal
residues rather than a defect in the Sturm implementation.
