# X-105350 — One-anchor Loewner/Hamburger calibration

This standard-library replay checks exact rational finite-atomic calibrations
for `L-105350--L-105351` and the bounded-order separator `R-105350`.

Run:

```bash
python -B experiments/X-105350-one-anchor-loewner-hamburger/verify.py \
  --output experiments/X-105350-one-anchor-loewner-hamburger/results/verification.json
```

Expected:

```text
PASS_X_105350_ONE_ANCHOR_LOEWNER_HAMBURGER
159 exact rational checks
502c6c26c11155fd3c35d49830f5ff6f8b32b0f0b6294bf73f04ea7aeeec9aee4
```

The checker verifies:

- positive atomic Hamburger factorization of every tested confluent matrix;
- exact equality between the same atoms and separated Loewner packets;
- the parity split into Stieltjes `E` hand shifted `O` Hankel blocks;
- exact safe-axis Stieltjes values;
- the exterior-residue measure for `p=x^4-2x^2+1/2`;
- a rational odd separator whose first two confluent matrices pass while the
  third fails;
- a three-node Loewner packet with every one-/two-node principal restriction
  positive but negative full determinant.

The replay does not machine-prove the infinite Hamburger or Stieltjes moment
theorems, evaluate Xi, prove `CRVH105330`, prove `OASH105350`, validate the
moving saddle, or prove RH.
