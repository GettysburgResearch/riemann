# Central xi power-sum and moment criteria — literature alignment

Date: 2026-08-01  
Authoring agent: `gpt56-04-f`

## Primary source

Ruiming Zhang, *On Power Sums of Positive Numbers*, arXiv:1510.03420
(2015).

Zhang studies a genus-zero entire function

\[
 f(z)=\prod_n(1-\lambda_n z)
\]

with absolutely summable reciprocal-zero sequence and proves that positivity of
all `lambda_n` is equivalent to a Hausdorff complete-monotonicity hierarchy for
the power sums.  Applied to

\[
 \frac{\Xi(\sqrt z)}{\Xi(0)},
\]

the paper gives an RH-equivalent all-order finite-difference criterion for the
central inverse-square zero sums.

## Relationship to `T-15110`

`T-15110` uses the same central power sums but packages positivity through the
Stieltjes moment theorem:

\[
 H_r=(s_{i+j})\succeq0,
 \qquad
 H_r^+=(s_{i+j+1})\succeq0
 \quad(r\ge1).
\]

The two forms are equivalent after scaling by a number not smaller than the
largest inverse-square zero modulus:

- Zhang: Hausdorff finite differences on a compact interval;
- `T-15110`: ordinary and shifted Stieltjes Hankel matrices, with compactness
  recovered from the positive convergence radius.

Thus `T-15110` is an independent reconstruction/alternative certificate
language, not a claim that central power-sum criteria are new.

## Consequence for the July determinant proposal

The determinant moments in `L-15128` are exactly these central power sums after
the target identity is imposed. Therefore proving their all-order arithmetic
match is equivalent to proving one of the known power-sum positivity
hierarchies. It cannot be treated as routine finite-window bookkeeping.

## Current computational status

`O-15105` gives ordinary midpoint positivity through Hankel size three.  No
all-order theorem, directed ladder, or RH conclusion is obtained.
