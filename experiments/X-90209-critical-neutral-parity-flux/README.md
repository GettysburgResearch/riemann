# X-90209 — Critical-neutral parity and Mertens-flux replay

This verifier supports:

- `R-90226`, the sub-four forcing repair;
- `L-90224`, color preservation on the active odd-divisor graph;
- `L-90225`, the exact adjacent-dyadic Mertens-flux identity.

Run:

```bash
python3 verify.py
```

Dependency: `mpmath`.

A successful replay prints:

```text
PASS_X_90209_CRITICAL_NEUTRAL_PARITY_FLUX
```

The package proves no one-sided Mertens bound and no statement of RH.
