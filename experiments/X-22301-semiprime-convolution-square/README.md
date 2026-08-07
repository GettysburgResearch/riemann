# X-22301 — Exact semiprime convolution-square regression

Status: **EXACT SYNTHETIC ALGEBRA ONLY**  
Issue: #223  
Claims: `T-22301`, `L-22301`, `R-22301`

## Purpose

This experiment checks the finite algebra behind the third global attack:

```text
prime signal Q
-> direct convolution Q*Q
-> grouped product/semiprime convolution
-> diagonal + off-diagonal recombination
-> exact |F^2|=|F|^2 norm identity.
```

It also retains a finite identity-orbit control showing that coefficient `l2`
norm one does not bound the untwisted boundary evaluation.

## Replay

```bash
python verify.py certificates/synthetic.json \
  --output results/replayed.json
python -m unittest discover -s tests -v
```

Expected proof-object SHA-256:

```text
4db99b1c11db3400fa0256102217228716c945d4a10305fc338b1a741408f500
```

Eight central/mutation tests are included.

## Retained control

The synthetic window is the exact second difference

```text
(1,-2,1),
```

and the two atoms have locations `2,5` and weights `2,3`. The checker obtains
identical direct and grouped convolutions. The ordered cross coefficients are
`6,6`, so the grouped off-diagonal coefficient is `12`, matching the
squarefree-semiprime factor of two.

Two rational complex samples give

```text
H2 norm squared = 2
H1 norm of the analytic square = 2.
```

The identity-orbit block has coefficient norm squared `1` but point-evaluation
square `16`, illustrating the universal embedding no-go.

## Proof boundary

No actual prime location, zeta value, Laplace continuation, or Hardy-space
abscissa is evaluated. The experiment verifies only the exact finite algebra
used by the proposed global theorems.
