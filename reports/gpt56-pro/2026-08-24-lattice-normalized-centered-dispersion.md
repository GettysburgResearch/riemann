# Lattice-normalized centered dispersion continuation

## Purpose

Continue PR #719 from the clean four-owner phase frontier while preserving the stopped largest-two source exactly.

## Binding correction

The original centered outer kernel `R_L` has a nonzero negative square-lattice moment.  Its unrestricted Type-I term contains a favorable nonnegative square and is not power-small in absolute value.  Only its adverse part is `O(Y^(-1/6))`.

The logarithmic derivative

```text
K_L=D R_L
```

has exact zero square-lattice moment.  Its unrestricted Type-I lattice is genuinely `O(Y^(-1/6))` in absolute value and it remains a fixed zero-safe RH detector.

## Exact stopped decomposition

The derivative scalar has one coefficient-exact stopped-prime Vaughan split:

```text
power-small unrestricted lattice
+ derivative smooth boundary
+ stopped balanced Type-II.
```

No unrestricted integer or zero additive phase is inserted into the two retained rows.

## Centered phase packing

Summing only nonzero additive phases produces the exact centered kernel

```text
product_i [ell_i 1_(ell_i | b^2-b'^2)-1].
```

The principal frequencies are therefore subtracted before Cauchy.

For complete dyadic prime families with their natural `1/(ell_1 ell_2)` weights, the coherent energy obeys

```text
E << (Y^o(1)/Q)
     [1+L_1 L_2/(B log(2L_1)log(2L_2))].
```

This closes the global weighted long-core phase transform when `B>=L_1L_2`.  It is a genuine family-level packing theorem rather than a sum of fixed-quadruple estimates.

## Smooth boundary

The smooth-boundary source diagonal is `O((log log Y)^2)` and equal-product multiplicity is `Y^o(1)`.  Its remaining operation is the same distinct-product cross-owner restriction as the balanced current.

## Boundary

The exact remaining statement is `SLCD102890`: the combined derivative smooth-boundary and residual stopped balanced centered-dispersion current has subpower logarithmic negative mass after one-use owner/weight allocation.

```text
SLCD102890   OPEN / RH-BEARING
RH           UNPROVED
```
