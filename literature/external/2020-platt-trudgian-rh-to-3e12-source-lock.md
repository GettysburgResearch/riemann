# External source lock — Platt–Trudgian rigorous RH verification

Source: Dave Platt and Tim Trudgian, **The Riemann hypothesis is true up to
`3·10^12`**, arXiv:2004.09765 (2020; subsequently published).

## Imported scope

The paper rigorously verifies, using interval/ball arithmetic and Turing's
method, that all nontrivial zeta zeros with

\[
0<\Im\rho\le 3{,}000{,}175{,}332{,}800
\]

are accounted for and lie on the critical line.  In particular, every
nontrivial zeta zero satisfies

\[
|\Im\rho|>1.
\]

Only this extremely weak corollary is used by `L-91905`.

## Why the input is enough

For a centered off-line coordinate

\[
\lambda=a+ib,
\qquad |a|<1/2,
\]

the orbitwise derivative calculation in `L-91905` requires

\[
 b^2>|b|>2|ab|.
\]

The imported bound `|b|>1` supplies this immediately.  No high-zero density,
spacing, simplicity or numerical ordinate is used.

## Trust boundary

This source lock imports a published rigorous computation; it does not replay
that computation inside this repository.  The new algebraic deduction from
`|Im rho|>1` to order-two safe Pick positivity remains subject to independent
review.
