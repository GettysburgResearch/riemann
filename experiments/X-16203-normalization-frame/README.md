# X-16203 — Exact normalization, radical-frame, and endpoint-ledger audit

This standard-library-only experiment checks three finite algebraic kernels used
by the continuation on Issue #162:

1. the exact identity
   `positive-ray leakage norm^2=d(1+chi)/2`;
2. the global two-anchor codimension-two radical frame and its Loewner bounds;
3. the directed endpoint-jet Poisson alias formulas.

The retained certificate is synthetic rational data. It contains no Riemann
zeta zero, production PSWF, or Weil matrix.

## Replay

```bash
python verify.py certificate.json --output results/verification.json
python -m unittest discover -s tests -v
```

Expected proof-object SHA-256:

```text
256920244b63d93d0b618b6803c1babeb34aa8b534ca75fb632d38ea5fcc6d63
```
