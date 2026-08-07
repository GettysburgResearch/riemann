# X-15117 — Exact actual relative-Ward pullback checker

This experiment verifies the finite algebra used in `L-15137/T-15115`.

For symmetric rational matrices `A` (raw seam operator) and `D` (finite-jet contact operator), put

```text
K = A-D.
```

At every order `ell`, the checker verifies

```text
q_rel(ell)   = Tr(A^ell)-Tr(K^ell),
q_Ward(ell)  = delta_raw(ell)+q_rel(ell),
raw_scalar   = Tr(A^ell)+delta_raw(ell),
raw_scalar-q_Ward = Tr(K^ell).
```

At order four it independently evaluates the noncommutative contact polynomial

```text
4 Tr(A^3 D)
-4 Tr(A^2 D^2)
-2 Tr(A D A D)
+4 Tr(A D^3)
-Tr(D^4)
```

and checks that it equals `Tr(A^4)-Tr(K^4)`.

The retained control is deliberately noncommuting:

```text
A = [[1,2],[2,-1]],
D = [[0,1],[1,1]],
K = [[1,1],[1,-2]].
```

It gives

```text
Tr(A^4)        = 50
Tr(K^4)        = 31
relative q_4   = 19
Tr(A^3 D)      = 15
Tr(A^2 D^2)    = 15
Tr(A D A D)    = -1
Tr(A D^3)      = 6
Tr(D^4)        = 7
```

and therefore

```text
4*15 - 4*15 - 2*(-1) + 4*6 - 7 = 19.
```

A nonzero rational raw-diagonal defect is included at every order 2 through 8, so the checker also tests the full formula rather than only the raw-compatible specialization.

## Reproduction

```bash
python3 verify.py certificates/noncommuting-ward-pass.json
python3 -m unittest discover -s tests -v
```

The verifier uses only Python integers, `fractions.Fraction`, JSON, and SHA-256. It does not evaluate a Riemann contour integral or certify that the manuscript's displayed linear counterterm equals the nonlinear Ward pullback.
