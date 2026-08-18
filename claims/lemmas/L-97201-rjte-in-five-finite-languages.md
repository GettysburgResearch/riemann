# L-97201 — RJTE in five exact finite languages

Claim ID: `L-97201`  
Status: **PROVED EXACT FINITE REFORMULATIONS**  
Created: 2026-08-18  
Depends on: `L-97200`  
RH status: **unproved**

Fix a finite Euler prime set `P` and horizon `N`. Let `b_P`, `g_P` be the inverse/reciprocal coefficients obtained from the dyadic local factor and the odd Euler factors in `P`.

## 1. Truncated moment problem

Put

\[
f_P(n)=b_P(n)/g_P(n)\in[-1,1],
\]

and define the positive atomic measure

\[
\nu_{P,N}=\sum_{n\le N}\frac{g_P(n)}{\sqrt n}\,\delta_{f_P(n)}.
\]

Then

\[
\mathcal B_P(N)=\int x\,d\nu_{P,N}(x).
\]

Every Hankel moment matrix of `nu_(P,N)` is positive semidefinite. RJTE is not ordinary moment positivity: it asks that the first moment be at most the external unit boundary, not at most the total mass.

## 2. Julia / semidefinite form

The cumulative Julia matrix is

\[
J_{P,N}=\sum_{n\le N}\frac1{\sqrt n}
\begin{pmatrix}g_P(n)&b_P(n)\\b_P(n)&g_P(n)\end{pmatrix}\succeq0.
\]

Its off-diagonal is `mathcal B_P(N)`. Positivity gives only

\[
|\mathcal B_P(N)|\le\sum_{n\le N}g_P(n)/\sqrt n.
\]

The desired unit-normalized Schur condition is

\[
\begin{pmatrix}1&\mathcal B_P(N)\\\mathcal B_P(N)&1\end{pmatrix}\succeq0.
\]

It is a genuinely additional boundary constraint.

## 3. Extremal martingale problem

The variables `f_P(n)` obey the exact triangular harmonic equations

\[
f_P(n)+\sum_dP_{P,n}(d)f_P(n/d)=0,
\qquad f_P(1)=1,
\qquad |f_P(n)|\le1.
\]

RJTE is the linear objective

\[
\sum_{n\le N}\frac{g_P(n)}{\sqrt n}f_P(n)\le1.
\]

This is a finite linear programme with a triangular equality system. Its dual is a Bellman superpotential on the divisor DAG. The local martingale constraints alone do not normalize the boundary functional.

## 4. Hardy / Schur interpolation

A scalar unit-normalized passive realization would require the `2x2` Schur matrix above to be positive. Hence any finite value `mathcal B_P(N)>1` is simultaneously:

* a failed unit Schur interpolation condition;
* a negative Schur-complement determinant;
* a separation certificate against a scalar passive one-port.

The coefficientwise Julia system remains positive; what fails is the chosen scalar boundary normalization.

## 5. Prime-adjoining Bellman form

Adding a new odd prime gives

\[
\mathcal B_{P\cup\{p\}}(N)
=\mathcal B_P(N)-p^{-1/2}\mathcal B_P(\lfloor N/p\rfloor).
\]

Thus the exact preservation inequality is

\[
1-\mathcal B_P(N)+p^{-1/2}\mathcal B_P(\lfloor N/p\rfloor)\ge0.
\]

A one-number state `mathcal B_P(N)` is not Markovian: the child value at `floor(N/p)` is indispensable. Iteration closes on the finite quotient profile

\[
\mathbf B_P^{(N)}=
\bigl(\mathcal B_P(\lfloor N/m\rfloor)\bigr)_{m\ge1},
\]

which has only `O(sqrt N)` distinct coordinates.
