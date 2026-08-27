# X-105330 — Dual Vandermonde contour hierarchy replay

This standard-library replay authenticates the exact finite algebra behind
`L-105328--L-105329`, `R-105328`, and `T-105330`.

Run:

```bash
python -B experiments/X-105330-dual-vandermonde-contour-hierarchies/verify.py \
  --output experiments/X-105330-dual-vandermonde-contour-hierarchies/results/verification.json
```

Expected verdict:

```text
PASS_X_105330_DUAL_VANDERMONDE_CONTOUR_HIERARCHIES
```

The checker performs 222 exact rational checks covering:

- critical Vandermonde factorizations;
- the generalized residue pencil;
- independent coefficient-side resultant evaluations;
- Cauchy–Binet/Andreief subset expansions;
- cardinal-polynomial sign witnesses;
- the quartic first-two-minor separator;
- Cauchy–Vandermonde packet determinant identities.

Proof object:

```text
93f59673fad499278a27b6a93f801d96156907759642bf6b8fc9fb0626a66c5e
```

The replay does not evaluate Xi, prove either cofinal determinant hierarchy,
prove `PRES105220` or `BRP105220`, authenticate the moving-saddle theorem, or
prove RH.
