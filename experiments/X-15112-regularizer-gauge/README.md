# X-15112 — Exact Sobolev-regularizer gauge audit

A two-dimensional rational model proves that a symmetric raw form made
Hilbert--Schmidt by a Sobolev sandwich does not acquire a canonical determinant.

With

```text
A=diag(1,4), B=diag(1,3), K_a=(I+A)^(-a) B (I+A)^(-a),
```

one obtains

```text
a=1: spectrum (1/4,3/25), Tr(K^2)=769/10000;
a=2: spectrum (1/16,3/625), Tr(K^2)=392929/100000000.
```

Swapping the reference eigenvectors gives spectrum `(1/25,3/4)` at `a=1`.
The regularized determinant zeros therefore change with the smoothing data.

Proof-object digest:

```text
43a4394de405e75c9dc57b9f2967089c1bbc4b3c08b3a7487e454ad33477b325
```

This is a synthetic exact audit, not a Riemann computation. It proves that
reference/chart/exponent invariance or the complete moment match is an
additional theorem; Schatten membership alone is not target identification.

Reproduce with:

```bash
python3 verify.py
```
