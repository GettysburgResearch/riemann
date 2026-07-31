# X-15304 — Exact triangular three-block Schur verifier

This experiment is the finite arithmetic companion to `L-15306`.

It verifies, using Python integers and `fractions.Fraction` only,

```text
B_R + e G_R > 0
C - h M > 0
B_V - h^-1 Z^T M^-1 Z - beta G_V > 0
kappa G_R
 - h^-1 Y^T M^-1 Y
 - beta^-1 X_tilde^T G_V^-1 X_tilde > 0
```

with

```text
X_tilde = X - h^-1 Z^T M^-1 Y.
```

The certified lower floor is

```text
-(e+kappa+delta)
```

relative to `diag(G_R,G_V,M)`.

## Synthetic strict control

The retained scalar packet uses

```text
B_R = 0
B_V = C = 3/2
X = 1/20
Y = 1/10
Z = 1/2
h = beta = 1
```

so that

```text
X_tilde = X - ZY = 0
```

exactly. The naive independent-cross estimate misses this cancellation. The
checker certifies

```text
radical correction matrix  1/100
kappa                       1/80
radical lower loss          1/1000
assembly radius             1/10000
final negative floor        17/1250
```

Proof-object SHA-256:

```text
83553370cdf517e38ac7d186286cebd7ef61f011d26dcfb4f072f20e2d3554b8
```

Verification SHA-256:

```text
ef8e96b8a88eda00549c5514fa89bee4cf432f8f2e8deb94f5c8747d27db858d
```

## Run

```bash
python experiments/X-15304-triangular-three-block-schur/verify.py \
  experiments/X-15304-triangular-three-block-schur/certificates/synthetic.json

python -m unittest discover \
  experiments/X-15304-triangular-three-block-schur/tests
```

Nine adversarial tests cover every load-bearing LMI, exact corrected-cross
reconstruction, malformed metrics, dimensions, Boolean rationals, and assembly
radius.

## Proof boundary

The verifier checks exact finite algebra only. It does not prove source
radicality, certified-zero completeness, a symbol floor, a high-zero tail bound,
cofinal rates, or RH.
