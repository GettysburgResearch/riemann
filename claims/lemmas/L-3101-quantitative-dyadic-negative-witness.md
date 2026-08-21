# L-3101 — Quantitative dyadic preservation of a negative finite form

Claim ID: L-3101  
Title: An explicit rounding radius preserves a strict negative Hermitian direction  
Status: PROPOSED  
Authoring agent: `gpt56-05`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: finite-dimensional operator norm; L-0311 for qualitative context only  
Scope: quantitative witness extraction for finite matrix criteria  
Related counterexample candidates: cutoff-free Weil, carrier-Weil, and any finite Hermitian positivity criterion

## Statement

Let `A` be an `m x m` Hermitian matrix and let `B>=||A||_2`. Let `x in C^m`
satisfy

\[
 x^*Ax\le -\mu<0.
\]

If `d=x+e` and `||e||_2<=delta`, then

\[
 d^*Ad\le -\mu+B\bigl(2||x||_2\delta+\delta^2\bigr).
\]

Consequently,

\[
 B\bigl(2||x||_2\delta+\delta^2\bigr)<\mu
 \quad\Longrightarrow\quad d^*Ad<0.
\]

For a unit vector `x`, it is enough that `B(2 delta+delta^2)<mu`.

If every real and imaginary coordinate of `x` is rounded to the nearest multiple
of `2^{-k}`, the resulting complex dyadic vector `d_k` satisfies

\[
 ||d_k-x||_2\le 2^{-k-1}\sqrt{2m}.
\]

For real `x`, the sharper bound is `2^{-k-1} sqrt(m)`. Therefore any `k` for
which the corresponding value of `delta` satisfies the displayed strict
inequality gives a certified bit-depth target for dyadic witness extraction.

A useful uncertainty corollary is the following. Suppose `A_tilde` is Hermitian,

\[
 ||A-A_tilde||_2\le epsilon,
 \qquad ||x||_2=1,
 \qquad x^*A_tilde x\le-eta,
\]

with `eta>epsilon`. Then `x^*Ax<=-(eta-epsilon)`, and it is enough to use

\[
 B=||A_tilde||_2+epsilon,
 \qquad \mu=eta-epsilon
\]

in the rounding condition above.

## Motivation

L-0311 proves qualitatively that a genuine finite negative direction has a
rational or dyadic witness. Candidate-producing agents need a quantitative
answer: how many bits are enough, and how much matrix uncertainty may be
absorbed before rounding destroys the sign? This lemma turns a discovered
negative margin and an operator-norm bound into an explicit dyadic precision
requirement. It applies to both active Weil families and to future finite
matrix criteria.

## Proof

Write `d=x+e`. Since `A` is Hermitian,

\[
 d^*Ad-x^*Ax=2\operatorname{Re}(e^*Ax)+e^*Ae.
\]

By Cauchy--Schwarz and the definition of the operator norm,

\[
 |e^*Ax|\le ||e||_2\,||Ax||_2
 \le B||e||_2||x||_2,
\]

and

\[
 |e^*Ae|\le B||e||_2^2.
\]

Thus

\[
 d^*Ad
 \le x^*Ax+2B||x||_2||e||_2+B||e||_2^2
 \le -\mu+B(2||x||_2\delta+\delta^2).
\]

The strict-negativity condition follows immediately.

Under nearest dyadic rounding, each of the `2m` real coordinates of a complex
vector changes by at most `2^{-k-1}`. Summing their squared errors gives

\[
 ||d_k-x||_2^2\le 2m\,2^{-2k-2}.
\]

The real-vector estimate is identical with only `m` real coordinates.

Finally,

\[
 x^*Ax=x^*A_tilde x+x^*(A-A_tilde)x
 \le -eta+||A-A_tilde||_2
 \le -(eta-epsilon),
\]

while the triangle inequality gives
`||A||_2<=||A_tilde||_2+epsilon`. Substitution proves the uncertainty
corollary. ∎

## Analytic domain audit

This is finite-dimensional linear algebra. No analytic continuation, contour,
or logarithm occurs.

## Dependency audit

Only the Hermitian expansion, Cauchy--Schwarz, and the spectral operator norm
are used. L-0311 is not logically required; it is the qualitative predecessor
that this claim strengthens.

## Gap audit

- The margin `mu`, norm bound `B`, and uncertainty `epsilon` must themselves be
  rigorous bounds before the lemma is used as proof.
- A floating eigenvalue is not a valid value of `mu` unless enclosed.
- Entrywise error bounds do not automatically equal an operator-norm bound;
  they need a proved conversion, such as a Frobenius or row-sum bound.
- The vector need not be renormalized after rounding; renormalization can add a
  second untracked error and is unnecessary because the sign is homogeneous.
- If `eta<=epsilon`, the approximate negative direction carries no rigorous
  sign information.

## Adversarial tests

1. Take `A=diag(-2^{-100},1)` and verify that coarse dyadic rounding may lose
   the negative direction while the stated bit condition rejects it.
2. Scale `x` by a rational constant and check the non-unit formula rather than
   silently applying the unit-vector corollary.
3. Use a matrix perturbation with norm exactly `epsilon` aligned against `x`;
   the loss of margin `epsilon` is sharp.
4. Compare the complex `sqrt(2m)` and real `sqrt(m)` coordinate counts.

## Remaining uncertainty

No mathematical gap is known. Practical sharpness depends on obtaining a good
norm bound; a crude Frobenius bound may demand more dyadic bits than necessary.

## Suggested next attack

Add this calculation to the X-0001 and X-0701 nomination stages. For every
stable negative screen, emit `(eta, epsilon, B, k)` together with a dyadic
vector, then let the existing exact interval checker decide the final sign.
