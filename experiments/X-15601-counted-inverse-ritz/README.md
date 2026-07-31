# X-15601 — Exact counted inverse–Ritz floor

This standard-library checker implements the finite trust boundary of `L-15601`.

## Mathematical input

A complete ambient theorem first proves that at most `d` localized-Weil eigenvalues lie below `Gamma`. An exactly `d`-dimensional trial packet is then evaluated through

```text
H = <(A-t)u_i,u_j>
K = <(A-t)u_i,(A-t)u_j>.
```

For `q<0`, the exact gates

```text
H < 0
K > 0
q K - H >= 0
```

certify

```text
inf spectrum(A) >= t + 1/q.
```

## Modes

- `SYNTHETIC_MODEL`: reconstructs the forms from a complete rational finite operator and independently verifies the count cap by a coercive orthogonal complement.
- `RIEMANN_WEIL_DIRECTED`: consumes rational Loewner bounds and a typed external count certificate. It never treats a floating count or compression as an ambient theorem.

## Synthetic control

The exact operator

```text
A = [[0,1/100],[1/100,1]]
```

has at most one eigenvalue below `1/2`. The trial vector `e1`, shifted at `t=1/4`, gives

```text
H = -1/4
K = 313/5000
q = -1249/313
qK-H = 1/5000.
```

The checker certifies the rigorous ambient floor

```text
-3/4996.
```

This is a synthetic operator regression, not a Riemann-zeta result.

## Reproduction

```bash
python verify.py certificates/synthetic-counted-floor.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```
