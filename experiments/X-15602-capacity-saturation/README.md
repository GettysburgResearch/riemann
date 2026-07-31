# X-15602 — Exact capacity-saturation checker

This experiment verifies the finite trust boundary of `L-15603`, `L-15604`,
and `L-15601`.

It accepts one exact rational finite operator and a trial packet. It verifies:

1. the packet has the declared full rank;
2. every packet direction lies strictly below `t`;
3. the complete orthogonal complement lies above `Gamma`;
4. therefore the exact spectral counts below `t` and `Gamma` both equal the
   packet dimension;
5. the counted inverse-Ritz moat `q K-H >= 0`, `q<0`;
6. the resulting ambient lower floor `t+1/q`.

No floating-point eigensolver enters the checker.

## Synthetic packet

The retained control is

```text
A = [[0,0,1/100],
     [0,0,0],
     [1/100,0,1]]

L = span(e1,e2)
t = 1/4
Gamma = 1/2
q = -1249/313.
```

The two trial directions lie below `t`, while `L^perp=span(e3)` lies above
`Gamma`. Hence both low counts equal two. The exact inverse-Ritz moat has pivots

```text
1/5000, 3/5008
```

and the ambient floor is

```text
-3/4996.
```

This is synthetic finite algebra, not a localized Riemann-zeta result.

## Run

```bash
python verify.py certificates/synthetic-saturation.json \
  --output /tmp/synthetic-verification.json

python -m unittest discover -s tests -v
```

## Production boundary

A production adapter must replace the explicit full matrix by directed Loewner
forms and bind:

- the localized-Weil normalization;
- the exact repaired radical packet;
- the complete symbol outer floor;
- the finite visible Schur block;
- the assembly radius.

A cofinal sequence of such finite certificates plus the rates in `T-15602`
would imply RH. A finite list does not.
