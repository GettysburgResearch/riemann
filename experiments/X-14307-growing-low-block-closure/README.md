# X-14307 — Exact growing-low-block closure regressions

This standard-library experiment accompanies:

- `R-14301` — fixed-row decay does not control a growing matrix;
- `L-14312` — common-frame tightness upgrades strong decay to norm decay;
- `L-14313` — a whole-packet exact radical tail map gives a dimension-free
  Schur lower bound.

It performs no Riemann-zeta evaluation. All arithmetic is exact
`fractions.Fraction` arithmetic.

## Run

```bash
python experiments/X-14307-growing-low-block-closure/verify.py \
  --output experiments/X-14307-growing-low-block-closure/results/selftest.json

python -m unittest discover \
  -s experiments/X-14307-growing-low-block-closure/tests -v
```

## Preserved result

```text
PASS_EXACT_FINITE_REGRESSIONS
proof object SHA-256:
a97c525a0efc578ece75038764be27dc59cd040763aabfbfae233e716b03965d
```

The escaping regression has every fixed prefix entry eventually zero while the
minimum eigenvalue remains exactly `-1`. The positive controls verify exact
rational `LDL` certificates for the quantitative `L-14312` bound and the
`L-14313` dimension-free corrected Schur floor.

## Proof boundary

The checker verifies finite linear algebra only. It does not prove that the
actual zeta generalized-prolate packets are collectively compact or admit exact
global Weil-radical frames with a shrinking tail-synthesis operator norm.
