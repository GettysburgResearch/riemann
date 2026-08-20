# L-100601 — Square-root cofactor cutoff collapses the unsquared tail to depth one

Claim ID: `L-100601`
Status: **PROVED EXACT COMBINATORIAL REDUCTION**
Depends on: `L-100600`; PR #688 largest-prime ownership
RH status: **not assumed**

In the rough largest-prime wavelet decomposition, every contributing source integer has

\[
n=pm,\qquad X/8\le pm\le X,\qquad p=P^+(n),\qquad P^+(m)<p.
\]

Fix the cofactor squaring cutoff

\[
Z_X=\sqrt X.
\]

Because `m<=X/p<X`, the cofactor `m` cannot contain two prime factors exceeding `Z_X`: if distinct primes `q_1,q_2>Z_X` both divided the squarefree cofactor, then

\[
m\ge q_1q_2>X,
\]
contradicting `m<X`.

Therefore every cofactor occurrence has exactly one of the two forms

\[
m=a,
\qquad\text{or}\qquad
m=qa,
\]
where

\[
P^+(a)\le\sqrt X,
\qquad q>\sqrt X,
\qquad q<p.
\]

After applying the source-faithful finite cofactor squaring of `L-100600`, all prime factors of `a` become squared labels of activity `1/r`, while the optional `q` remains the **only** unsquared cofactor label.

Hence the completed rough wavelet source has depth at most one above a strictly subcritical squared-small-prime core.

## Exact decomposition

Write `C_X(a)` for the completed squared-small-prime core coefficient and retain the unique outer largest-prime owner `p`. Then the completed rough packet separates into

\[
\mathcal R_0(X)
=-\sum_p p^{-1/2}
  \sum_a C_X(a)\,K_0(X/(pa)),
\]

and

\[
\mathcal R_1(X)
=+\sum_p p^{-1/2}
  \sum_{\sqrt X<q<p}q^{-1/2}
  \sum_a C_X(a)\,K_0(X/(pqa)),
\]
with the same squarefree/owner restrictions inherited from the source identity. No term with two unsquared cofactor primes exists.

Thus `HCFB100600` reduces to a single large-owner/large-cofactor-prime/squared-core trilinear interface rather than an arbitrary-depth Euler cube.

This reduction is exact and uses no analytic estimate.