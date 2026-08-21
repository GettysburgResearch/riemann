# L-101503: finite completion preserves the full-source real-carrier zero

Let the native duplicate-67 reciprocal-zeta source have Dirichlet multiplier

```text
B(z) = (1-67^(-z))/zeta(z).
```

Let `C_Z(z)` be any finite Euler completion multiplier, hence a finite Dirichlet polynomial and finite at `z=1`.

## Statement

The correction multiplier

```text
(C_Z(z)-1) B(z)
```

still vanishes at `z=1`.

## Proof

The reciprocal zeta function has a simple zero at `z=1`, while `1-67^(-1)` is nonzero and `C_Z(1)-1` is finite. Therefore the product vanishes at `z=1`.

## Consequence

A power-sized real carrier seen after first truncating the unsquared native tail is not automatically a carrier of the complete correction. The source-faithful order is:

```text
retain the complete native tail
-> form the finite completion correction
-> triangularize by owner
-> only then take one-sided mass.
```
