# X-15115 — Exact contour-cyclic order-four and diagonal-gap checker

This Fraction-only checker verifies the finite product-contour construction of
`L-15133` and the type separation of `R-15110`.

The retained two-dimensional example has

```text
G = [[2,1],[1,2]]
B = [[1,2],[2,-1]]
```

and proves

```text
Tr((G^-1 B)^2) = 46/9
Tr((G^-1 B)^3) = -244/27
Tr((G^-1 B)^4) = 1666/81
Tr((G^-1 B)^5) = -10324/243
Tr((G^-1 B)^6) = 66286/729
```

The direct eight-index order-four connected contour contraction is `1666/81`.
The disconnected degree-four contraction `(Tr K^2)^2` is `2116/81`, so the
connected/logarithmic choice is nontrivial.

The same one-copy contour biform and readout data permit a one-contour central
order-four value `0` unless an additional cyclic diagonal identity is supplied.
This is an exact logical-independence control, not a Riemann computation.

With `||K||_2 <= 3` and `r=1/6`, the uniform series majorant is exactly `3`.

## Reproduction

```bash
python3 verify.py certificates/cyclic-order4.json
python3 -m unittest discover -s tests -v
```

Eleven central/adversarial tests pass.

Proof-object SHA-256:

```text
de435821c005892e8903edf4c1e964cc9e3d7414d01eae66fbef99fd0ee7af1c
```

No `xi` value, zeta zero, or Guinand--Weil production contour is evaluated.
