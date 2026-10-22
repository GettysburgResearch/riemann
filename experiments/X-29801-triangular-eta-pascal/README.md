# X-29801 — Triangular eta–Pascal exact regression

Run:

```bash
python experiments/X-29801-triangular-eta-pascal/verify.py
```

The standard-library checker verifies only finite formal/rational algebra:

```text
formal stopped-log telescopes          8,255
positive rational finite differences   8,960
eta residual/capacity pairs            1,024
Euler weight partitions                   32
feedback mutation                         1
```

Expected classification:

```text
EXACT_TRIANGULAR_ETA_PASCAL_ALGEBRA_VERIFIED
```

Verifier SHA-256:

```text
ff861bec6e3413e1a8465b0e9af28b50f5f5f60aee39802638acf488d04e3214
```

The checker does **not** certify the complete endpoint-jet source manifest, the no-feedback theorem, Cycle Debt, the prime-ramp estimate, or RH.
