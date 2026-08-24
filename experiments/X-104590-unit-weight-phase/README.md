# X-104590 — Unit-weight phase algebra replay

The standard-library replay checks the finite algebra behind `T-104590`:

1. the exact numerator identity in `L-104542`;
2. the quartic wrong-extremum firewall;
3. a cubic with two Rolle-generating extrema;
4. the marked two-moment Cauchy bound;
5. a marked contour residue fixture;
6. the period increment of the unwrapped `|sin|` phase primitive.

Run:

```bash
python3 experiments/X-104590-unit-weight-phase/verify.py \
  --output experiments/X-104590-unit-weight-phase/results/verification.json
```

Expected:

```text
PASS_T104590_UNIT_WEIGHT_PHASE_ALGEBRA
04217d866bdfcbd635c6a97a73c83781bbe23f92525f257450271b5164af117b
```

The replay does not prove `UPHASE104590`, `CM2X104590`, the fixed-order
descent, or RH.
