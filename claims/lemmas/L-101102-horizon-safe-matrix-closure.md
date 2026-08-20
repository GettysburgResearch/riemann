# L-101102 — Horizon-safe use of auxiliary completion matrices

## Statement

Let `F` be one fixed conclusion-bearing scalar and

\[
 N_F(Y)=\int_1^Y(F(X))_-\frac{dX}{X}.
\]

Suppose that for every horizon `Y` one may choose auxiliary currents,
operators, and a nonnegative matrix `M_Y`, possibly depending on `Y`, such
that

\[
 n_Y\le M_Yn_Y+e_Y,
\]

`N_F(Y)` is bounded by a fixed nonnegative linear functional of `n_Y` plus
`Y^{o(1)}`, and

\[
 \sup_{Y\ge Y_0}\rho(M_Y)\le1-\eta
\]

for some `eta>0`, with `||(I-M_Y)^{-1}||=Y^{o(1)}` and `e_Y=Y^{o(1)}`.
Then

\[
 N_F(Y)=Y^{o(1)}.
\]

The auxiliary completion need not define one fixed positive function on all
scales.

## Proof

Apply the finite-dimensional Neumann inverse separately at each horizon:

\[
 n_Y\le(I-M_Y)^{-1}e_Y=Y^{o(1)}.
\]

The assumed fixed linear comparison gives `N_F(Y)=Y^{o(1)}`.  Landau is then
applied only to the Mellin transform of the original, fixed `F`.

## Firewall

It remains invalid to feed a family of `Y`-dependent positive auxiliary
functions directly to Landau.  The permissible use is narrower: they may
prove a finite-horizon inequality for the negative mass of one fixed scalar.
This distinction repairs, rather than ignores, the diagonal-positivity
firewall recorded in the adaptive-squaring branch.
