# X-91113 — Rough-scale endpoint-port renewal

Companion replay for `L-91325`.

```bash
python3 experiments/X-91113-rough-scale-endpoint-port-renewal/verify.py
```

Expected verdict:

```text
PASS_ROUGH_SCALE_ENDPOINT_PORT_RENEWAL
```

The standard-library checker verifies the exact rational constants in the
analytic proof, the derivative polynomial identity, 90,000 high-precision
cell-endpoint mutation controls for representative rough scales, and exact
geometric-law normalization.

The positivity theorem is analytic. The Decimal scan is a mutation guard, not
the proof object.
