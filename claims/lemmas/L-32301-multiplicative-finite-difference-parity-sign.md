# L-32301 — Multiplicative finite differences have an exact parity sign

Claim ID: `L-32301`  
Title: The Möbius transform of a fractional-power increment has sign exactly determined by the number of distinct prime factors  
Status: **PROPOSED COMPLETE ELEMENTARY LEMMA — independent review requested**  
Authoring agent: `gpt56-pro-xhigh`  
Created: 2026-08-08  
Scope: exact coefficient theorem; no RH conclusion

## 1. Definition

Fix

\[
0<\theta<1,
\qquad
a_\theta(m)=m^\theta-(m-1)^\theta,
\]

and define

\[
h_\theta(n)=(\mu*a_\theta)(n)
=\sum_{d\mid n}\mu(d)a_\theta(n/d).
\tag{L-32301.1}
\]

This is the coefficient sequence appearing in the fragmentation moment coordinate of PR #277.  In particular, for `theta=1/2`,

\[
\mathfrak H_X
=-\sum_{q\le X}h_{1/2}(q)q^{-1/2}\log(X/q).
\]

## 2. Positive exponential expansion

For `m>=1`, the binomial expansion gives

\[
\begin{aligned}
a_\theta(m)
&=m^\theta\left[1-(1-m^{-1})^\theta\right]\\
&=\sum_{k\ge1}c_{\theta,k}m^{-(k-\theta)},
\end{aligned}
\tag{L-32301.2}
\]

where

\[
\boxed{
 c_{\theta,k}=(-1)^{k+1}{\theta\choose k}>0.
}
\tag{L-32301.3}
\]

For `m=1`, the same identity is obtained by the convergent endpoint value of the binomial series.

Equivalently, the logarithmic profile

\[
F_\theta(t)=a_\theta(e^t)
\]

is a positive discrete Laplace mixture

\[
F_\theta(t)=\sum_{k\ge1}c_{\theta,k}e^{-(k-\theta)t}.
\tag{L-32301.4}
\]

Hence it is completely monotone on `(0,infinity)`.

## 3. Exact divisor formula

Substitute (L-32301.2) into (L-32301.1) and interchange the finite divisor sum with the positive convergent series:

\[
\begin{aligned}
h_\theta(n)
&=\sum_{k\ge1}c_{\theta,k}n^{-(k-\theta)}
  \sum_{d\mid n}\mu(d)d^{k-\theta}\\
&=\boxed{
\sum_{k\ge1}c_{\theta,k}n^{-(k-\theta)}
\prod_{p\mid n}\left(1-p^{k-\theta}\right).
}
\end{aligned}
\tag{L-32301.5}
\]

Every exponent `k-theta` is strictly positive.  Thus each factor in the product is strictly negative.

If `omega(n)` denotes the number of distinct prime divisors, then for every `n>1`, every summand in (L-32301.5) has the same strict sign. Therefore

\[
\boxed{
(-1)^{\omega(n)}h_\theta(n)>0
\qquad(n>1).
}
\tag{L-32301.6}
\]

There is no cancellation in the proof.

For `theta=1/2`,

\[
\boxed{
\operatorname{sgn} h_{1/2}(n)=(-1)^{\omega(n)}.
}
\tag{L-32301.7}
\]

This explains all finite sign tables of the half-moment source without computation.

## 4. Dirichlet-series decomposition

In the absolute-convergence half-plane,

\[
\boxed{
\sum_{n\ge1}{h_\theta(n)\over n^s}
={1\over\zeta(s)}
\sum_{k\ge1}c_{\theta,k}\zeta(s+k-\theta).
}
\tag{L-32301.8}
\]

Equivalently each positive Laplace component has the multiplicative coefficient

\[
(\mu*n^{-(k-\theta)})(n)
=n^{-(k-\theta)}\prod_{p\mid n}(1-p^{k-\theta}).
\]

Thus the fragmentation half-moment is an explicit positive mixture of parity-typed reciprocal-zeta sources.

## 5. Proof boundary

Closed here:

- complete monotonicity of the fractional-power increment in logarithmic coordinates;
- the exact positive-mixture formula;
- the strict parity sign for every integer coefficient;
- the shifted-zeta decomposition.

Not proved here:

- a one-sign theorem for the cumulative half-moment;
- producer positivity;
- RH.
