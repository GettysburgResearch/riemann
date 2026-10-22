# X-90019 — Improved rational factor-64 annular replay

Companion to `L-90022` and `T-90015`.

```bash
python experiments/X-90019-factor64-rational/verify.py --max-x 5000000
```

Expected line:

```text
PASS_FACTOR64_RATIONAL_UNIT_CIRCLE_CERTIFICATE
```

The checker verifies the exact `Q(sqrt(2))` moments, the unit-circle roots of `y^2+3y/4+1`, a 1,024-cell rational Bernstein certificate for `|P_64^*|^2<11`, the rigorous fixed-margin corridor, and every aligned endpoint through the selected finite maximum.

The finite scan is reconnaissance only. It does not prove eventual negativity or RH.
