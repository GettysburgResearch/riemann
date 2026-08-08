# X-30501 — Boundary atomization lower bound

This package replays the exact rational and integer inequalities used in
`L-30501/R-30501`.

It verifies:

```text
scaled top-band boundary upper endpoint    -123/512 < -1/5
stopped layer node moat                     1/25
endpoint geometry                           X=192,...,4096
linear source-node count                    X=192,...,100000
resulting atomic-norm lower bound           X/750
raw/divided source mutation                 1/121 != 1/484
```

Run:

```bash
python experiments/X-30501-boundary-atomization/verify.py
```

The checker uses only Python integers and `fractions.Fraction`.

## Proof boundary

The package certifies the elementary constants and finite integer geometry. The
analytic proof of the infinite paired-tail estimate is written in `L-30501` and
uses the mean-value and integral tests displayed there.

The package does **not** prove:

- a linear lower bound for optimized Cycle Debt;
- impossibility of a structured pre-atomization recombination;
- RH.
