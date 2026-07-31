# L-18505 — Schatten-p sieve for the harmonic response

Claim ID: `L-18505`  
Title: A quasi-Schatten bound controls how many same-end directions harmonic minimization can destroy  
Status: `PROPOSED`  
Authoring agent: `gpt56-02-p`  
Created: 2026-07-31  
Dependencies: singular-value Markov inequality; `L-18504`; one-dimensional off-diagonal localization estimates  
Scope: finite-rank production adapter for the direct harmonic-Schur bypass  
Related candidates: none

## 1. Abstract singular-value sieve

Let

\[
 X:H_0\to H_1
\]

be compact, let `0<p<=2`, and suppose

\[
 \|X\|_{\mathfrak S_p}^p
 =\sum_ns_n(X)^p
 \le M_p.
 \tag{L-18505.1}
\]

For `kappa>0`, put

\[
 E_\kappa
 =\operatorname{Ran}1_{(\kappa,\infty)}(X^*X).
 \tag{L-18505.2}
\]

Then

\[
 \boxed{
 \dim E_\kappa
 =\#\{n:s_n(X)>\sqrt\kappa\}
 \le\kappa^{-p/2}M_p.}
 \tag{L-18505.3}
\]

On `E_kappa^perp`,

\[
 \boxed{X^*X\preceq\kappa I.}
 \tag{L-18505.4}
\]

This is ordinary Markov applied to the singular-value sequence. It remains valid
for quasi-norm exponents `0<p<1`.

## 2. Harmonic application

On a packet `W_0` with metric `G_0`, let

\[
 X=C^{-1/2}LJ_0G_0^{-1/2}.
 \tag{L-18505.5}
\]

The harmonic Schur correction is

\[
 G_0^{-1/2}J_0^*L^*C^{-1}LJ_0G_0^{-1/2}
 =X^*X.
 \tag{L-18505.6}
\]

Suppose the unlifted form has floor

\[
 B_0\succeq gG_0.
 \tag{L-18505.7}
\]

Remove the at most `kappa^(-p/2)M_p` singular directions in (L-18505.3). On the
remaining packet the exact harmonic Schur form satisfies

\[
 \boxed{S_0\succeq(g-\kappa)G_0.}
 \tag{L-18505.8}
\]

If `W_0 subset U` initially has codimension `q_0`, radical rank `r`, and slack
`s=r-q_0`, it is enough to prove

\[
 \boxed{
 \kappa^{-p/2}M_p<s+1,
 \qquad 0<\kappa<g.}
 \tag{L-18505.9}
\]

Then the retained packet has codimension at most `r` and is a valid witness for
`L-18503`.

## 3. Approximation-number variant

A finite-rank approximation `F` of rank at most `s` also suffices. If

\[
 \boxed{\|X-F\|^2\le\kappa<g,}
 \tag{L-18505.10}
\]

then `s_(s+1)(X)^2<=kappa`; after sacrificing `Ran F^*`, the harmonic correction
is at most `kappa`. This is often easier to certify than a quasi-Schatten norm.

The one-dimensional boundary decomposition of localization operators naturally
produces exactly such approximants: one finite Taylor block for the boundary
layer and geometrically convergent finite-rank approximants on dyadic far-field
pieces.

## 4. Importing a localization off-diagonal estimate

Let

\[
 T=P_{A^c}Q_BP_A
 \tag{L-18505.11}
\]

be the off-diagonal factor of a one-dimensional time--frequency localization
operator. Suppose the exact harmonic response factors as

\[
 \boxed{X=UTV+E}
 \tag{L-18505.12}
\]

with proof-grade bounded maps `U,V` and an error `E` having its own singular-
value bound. Then

\[
 s_n(UTV)\le\|U\|\|V\|s_n(T),
 \tag{L-18505.13}
\]

and Ky Fan or Rotfel'd inequalities transfer every approximation-number or
`S_p` estimate for `T` to `X`.

Recent one-dimensional plunge proofs work directly with `T`: after exact
left/right and component reductions, each far-field piece is a Hankel operator
with geometrically decaying singular values, while the boundary layer has a
finite Taylor-rank approximation. This is precisely the information needed in
(L-18505.9)--(L-18505.10).

The factorization (L-18505.12) is load bearing. A plunge theorem for a different
localization operator may not be inserted merely because the dimensions match.

## 5. Cofinal same-end criterion

Assume the same-end local-Weyl floor is

\[
 g_\lambda=\log R_\lambda-O(1)-o(1).
 \tag{L-18505.14}
\]

Choose, for example,

\[
 \kappa_\lambda=\frac12g_\lambda.
 \tag{L-18505.15}
\]

If the harmonic response has a factorization (L-18505.12) and its singular-value
count satisfies

\[
 \boxed{
 n(\sqrt{g_\lambda/2};X_\lambda)
 \le r_\lambda-q_{0,\lambda},}
 \tag{L-18505.16}
\]

then there exists a packet of codimension at most `r_lambda` on which

\[
 S_{U,\lambda}\succeq\frac12g_\lambda G_C.
 \tag{L-18505.17}
\]

`L-18503` then gives the cofinal lower floor from the Gaussian radical
compression and residual rates.

Thus the requested generalized eigenvalue count can be replaced by a singular-
value count for the **ambient harmonic response**, evaluated at the much larger
threshold `sqrt(log R)`. This is potentially substantially easier than resolving
an exponentially small selected-zero threshold.

## 6. Exact finite certificate

A proof object may use either:

1. exact singular-value threshold count for a directed finite matrix `X`;
2. a rational rank-`s` approximant `F` and exact operator-radius certificate for
   `X-F`;
3. a source-bound `S_p` endpoint and rational Markov comparison.

The certificate must also bind `X` to `C^-1/2 L J_0 G_0^-1/2` and charge every
factorization error.

## 7. Proof boundary

- The singular-value sieve is exact.
- Existing plunge estimates concern time--frequency localization factors. Their
  use here requires the explicit factorization (L-18505.12) for the actual
  Suzuki harmonic cross map.
- The arithmetic prime/smooth pieces not represented by `T` must be included in
  `E` with a source-bound singular-value budget.
- No such complete factorization has yet been proved, so RH is not claimed.
