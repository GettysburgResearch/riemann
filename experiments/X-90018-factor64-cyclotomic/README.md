# X-90018 — Zero-safe factor-64 cyclotomic annular replay

Companion to `L-90019` and `T-90014`.

```bash
python experiments/X-90018-factor64-cyclotomic/verify.py
```

Expected line:

```text
PASS_FACTOR64_CYCLOTOMIC_ANNULAR_CERTIFICATE
```

The checker verifies:

- the exact `Q(sqrt(2))` coefficient moments;
- the root/factor structure of the cyclotomic dressing;
- an exact rational-Bernstein certificate for `|P_64(e^{it})|^2<16`;
- the broad rigorous constant corridor `moat<-0.194`, `zero bound<0.185`, hence RH-side margin `<-0.009` before the harmless `sqrt(2)` rescaling.

It does not prove the unconditional annular sign or RH.
