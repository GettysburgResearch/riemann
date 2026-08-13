# `P_61` Green-boundary closure — 2026-08-13

## Result

The inherited component-row obstruction in the preferred `P_61` one-prime
splice is closed with a uniform explicit margin.  For every real `p>=67` and
`2<=j<=y<=67`,

\[
 \mathscr R_{p,y}(j)>1/500.
\]

The exact packet and directed replay are `L-91346` and `X-91125`.

## New idea

The corrected finite-Euler identity decomposes the row into a positive
rough-lattice Green bulk and a signed finite boundary operator.  Instead of
bounding each boundary spline separately, the proof subtracts the asymptotic
finite-block slope and treats the remaining error in bounded-Lipschitz duality.
The boundary weights have a very small one-dimensional
Kantorovich--Rubinstein norm, retaining the cancellation lost by total
variation.

A fixed finite certificate proves

```text
beta_61 < 1/400;
|E| < 7/6;
Lip_log(E) < 27/20;
positive log(p) coefficient in every row;
final row margin > 1/500.
```

The worst certified row is `j=66`, with margin greater than
`0.0026181964`.

## Scope

This result closes the exact inherited-row inequality.  It does not alone prove
that the signed arithmetic packet has one positive source representation which
simultaneously realizes target, score and every row, and it does not close the
activation/frontier packet above the child endpoint.  Those are separated in
`O-91311` as the next finite transport/composition theorem.

RH remains unproved.
