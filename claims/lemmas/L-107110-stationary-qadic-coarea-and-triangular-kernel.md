# L-107110 — Stationary q-adic coarea is one fixed triangular kernel

**Claim ID:** `L-107110`  
**Status:** proved exact finite coarea identity  
**Date:** 2026-08-31  
**RH:** not assumed

Let `q>1`, put `L=log q`, and for `tau in [0,1)` define the shifted
multiplicative bands

\[
\mathcal B_{j,\tau}
 =\{n\ge1:q^{j+\tau}<n\le q^{j+\tau+1}\},
 \qquad j\in\mathbf Z.
\]

For finitely supported complex coefficients `(a_n)`, set

\[
S_{j,\tau}=\sum_{n\in\mathcal B_{j,\tau}}a_n,
\qquad
\mathcal Q_q(a)=\int_0^1\sum_j|S_{j,\tau}|^2\,d\tau.
\]

Then

\[
\boxed{
\mathcal Q_q(a)
 =\sum_{m,n}a_m\overline{a_n}\,
 \Lambda_q\!\left(\log{m\over n}\right),
}
\tag{L-107110.1}
\]

where

\[
\boxed{
\Lambda_q(v)=\left(1-{ |v|\over\log q}\right)_+.
}
\tag{L-107110.2}
\]

## Proof

Write `x=log_q m` and `y=log_q n`. As `tau` runs through one period, the two
points lie in the same translated unit interval exactly when no point of
`tau+Z` separates them. The measure of those shifts is

\[
(1-|x-y|)_+.
\]

Expanding the square and integrating proves (L-107110.1). No limiting
argument, random model, or averaging over arithmetic data is used.

The kernel is positive definite because it is an average of orthogonal band
projections. With the Fourier convention

\[
\widehat f(t)=\int_{\mathbf R}f(v)e^{-itv}\,dv,
\]

its transform is

\[
\boxed{
\widehat\Lambda_q(t)
 = (\log q)
 \left({\sin(t\log q/2)\over t\log q/2}\right)^2
 \ge0.
}
\tag{L-107110.3}
\]

Thus stationary q-adic coarea produces one fixed ratio-`q`, compact,
positive-definite Mellin kernel. It removes the moving outer-grid boundary
from the annular geometry while retaining every coefficient and sign.

## Prefix form

For coefficients supported on `n<=Y`, the same formula holds with every band
intersected with `[1,Y]`. At most

\[
N_q(Y)=2+\lceil\log_qY\rceil
\]

bands are nonempty. If

\[
M_a(Y)=\max_{Z\le Y}\left|\sum_{n\le Z}a_n\right|,
\]

then every band sum is a difference of two prefixes, while the complete
prefix is the sum of all band sums. Consequently

\[
\boxed{
{1\over N_q(Y)}
\left|\sum_{n\le Y}a_n\right|^2
\le \mathcal Q_q(a\mathbf1_{n\le Y})
\le4N_q(Y)M_a(Y)^2.
}
\tag{L-107110.4}
\]

After maximizing the middle expression over `Y<=X`, the left side also
contains `M_a(X)^2/N_q(X)`. Hence stationary coarea and the maximal prefix
have the same power exponent.

## Scope

The shift average is part of the definition of a new fixed observable. It is
not asserted to equal one particular unshifted annular partition pointwise.
The theorem is exact for arbitrary finite coefficients and introduces no
arithmetic estimate.