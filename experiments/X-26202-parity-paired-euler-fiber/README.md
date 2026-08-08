# X-26202 — Exact parity-paired Euler-fiber regression

This standard-library checker authenticates the finite algebra used by `L-26204`, `L-26205`, and `T-26202`.

It verifies exactly in `Q(sqrt(2))`:

- the complete local polynomial
  `(1-z)(1-2z)(1-sqrt(2)z)^2`;
- its critically normalized palindromic five-tap fiber;
- the polynomial expansion of
  `|p(z)|^2+|p(-z)|^2`;
- the sharp lower-bound factorization
  `>=45/4` on `1/2<=|z|<=1/sqrt(2)`;
- plus/minus completely multiplicative twisting;
- even/odd two-adic channel orthogonalization;
- complete five-tap fibers on every checked odd squarefree core;
- the mutation showing that one channel alone vanishes at a boundary root.

Run:

```bash
python experiments/X-26202-parity-paired-euler-fiber/verify.py
```

Retained verdict:

```text
PASS_EXACT_PARITY_PAIRED_EULER_FIBER_ALGEBRA
```

Proof-object SHA-256, computed before inserting the digest field:

```text
660cf891a3e729c25dd16f830d6707838cb26e1a381be862890fbb9e22ea450d
```

## Proof boundary

This checker proves no physical-block contraction, no uniform Schur reserve, no lower-scale recurrence, and no result about RH. It authenticates only the exact finite source/filter/frame algebra.