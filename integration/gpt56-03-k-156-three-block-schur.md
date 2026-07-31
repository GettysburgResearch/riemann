# Integration patch — triangular three-block Schur closure

Append-only proposed registrations:

```text
L-15306  triangular three-block Schur floor
T-15302  cofinal triangular three-block floors imply RH
M-15302  proof-producing triangular three-block pipeline
X-15304  exact rational triangular Schur verifier
```

Dependencies:

```text
L-15306 <- L-14308, L-14309, L-15305
T-15302 <- L-15306, T-14302, L-14311/L-14313, L-15303/L-15305
M-15302 <- L-15306, T-15302
X-15304 <- L-15306
```

The principal correction to the previous ledger is:

```text
X_tilde = X - h^-1 Z* M^-1 Y
```

and not an independent charge of `X`, `Y`, and `Z`. The visible-complement map
`Z` enters through the visible Schur floor; it is not required to vanish.

Status boundary:

- finite theorem/checker: exact or proposed finite mathematics;
- production visible floor and growing-packet rate: open;
- RH: not claimed.
