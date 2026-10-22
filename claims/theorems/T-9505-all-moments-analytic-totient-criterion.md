# T-9505 — An all-moments ladder is equivalent to the critical analytic-totient bound

Claim ID: `T-9505`  
Title: Dyadic even-moment bounds recover the uniform critical energy estimate  
Status: `PROPOSED — COMPLETE REDUCTION; MOMENT LADDER OPEN`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: `L-9512`; the elementary average order of `phi(n)/n`  
Scope: alternative full-RH attack through averaged positive quantities  
Related counterexample candidates: none

## Statement

Let `E^AN` be the analytic summatory-totient error in `L-9512`. The following
are equivalent:

1. the Riemann Hypothesis;
2. for every integer `k>=1` and every `epsilon>0`,
   \[
   \boxed{
   \int_X^{2X}|E^{\rm AN}(t)|^{2k}dt
   \ll_{k,\varepsilon}X^{k+1+\varepsilon}
   \qquad(X>=2).}
   \tag{T-9505.1}
   \]
3. (T-9505.1) holds for an unbounded sequence of integers `k`.

Thus one may replace the uniform pointwise RH estimate by a hierarchy of
strictly positive averaged moment estimates. No uniformity of the implied
constant in `k` is required.

## RH implies the moment ladder

Under RH, `L-9512` and the classical analytic-part criterion give, for every
`delta>0`,

\[
E^{\rm AN}(t)\ll_\delta t^{1/2+\delta}.
\]

Choose `delta=epsilon/(2k)`. Then on `[X,2X]`,

\[
|E^{\rm AN}(t)|^{2k}
\ll_{k,\varepsilon}X^{k+\varepsilon},
\]

and integration proves (T-9505.1).

## Unconditional local Lipschitz bound

For noninteger `x>1`, differentiating the exact Riesz form gives

\[
\frac d{dx}E^{\rm AN}(x)
=\frac6{\pi^2}x
-\sum_{n<x}\frac{\varphi(n)}n.
\tag{T-9505.2}
\]

The elementary estimate

\[
\sum_{n\le x}\frac{\varphi(n)}n
=\frac6{\pi^2}x+O(\log(2x))
\tag{T-9505.3}
\]

therefore gives

\[
\boxed{
|E^{\rm AN}(y)-E^{\rm AN}(x)|
\le C\log(4X)|y-x|
\qquad(x,y\in[X/2,3X]).}
\tag{T-9505.4}
\]

The function is continuous at integers; only its derivative jumps. Hence the
piecewise estimate integrates to the global dyadic Lipschitz bound.

## Moment ladder implies the pointwise bound

Fix `eta>0`. Choose one retained moment order `k` so large that

\[
\frac1{4k+2}<\frac\eta3.
\tag{T-9505.5}
\]

Let `x in [X,2X]` and put

\[
H=|E^{\rm AN}(x)|,
\qquad L=C\log(4X).
\]

By (T-9505.4), on at least one one-sided interval adjacent to `x` of length

\[
\ell\ge c\min\left(X,\frac H L\right),
\tag{T-9505.6}
\]

one has

\[
|E^{\rm AN}(t)|\ge\frac H2.
\tag{T-9505.7}
\]

The alternative `ell comparable to X` is already incompatible with
(T-9505.1) unless `H` satisfies a stronger bound than required. In the other
case, applying the moment estimate on one of the neighboring dyadic blocks
gives

\[
\frac{H^{2k+1}}{C_k\log(4X)}
\ll_{k,\varepsilon}X^{k+1+\varepsilon}.
\tag{T-9505.8}
\]

Therefore

\[
H
\ll_{k,\varepsilon}
X^{(k+1+\varepsilon)/(2k+1)}
(\log X)^{1/(2k+1)}.
\tag{T-9505.9}
\]

Since

\[
\frac{k+1}{2k+1}
=\frac12+\frac1{4k+2},
\tag{T-9505.10}
\]

choose the moment-bound epsilon sufficiently small and absorb the logarithm.
Equations (T-9505.5)--(T-9505.10) give

\[
E^{\rm AN}(x)=O_\eta(x^{1/2+\eta}).
\tag{T-9505.11}
\]

Because `eta>0` was arbitrary, `L-9512` implies RH.

The proof uses only one sufficiently high moment for each desired pointwise
exponent. Hence any unbounded sequence of passing moment orders is enough.

## Energy consequence

The pointwise estimate (T-9505.11) inserted in (L-9512.12) gives

\[
\boxed{
\mathfrak A(x)=O_\eta(x^{-3+\eta}).}
\tag{T-9505.12}
\]

Thus the requested uniform critical energy estimate may be attacked through the
positive scalar hierarchy (T-9505.1), without first controlling exceptional
points.

## Why this is a genuine change of attack surface

A single mean square controls only a typical value and cannot exclude a narrow
exceptional spike. The complete even-moment ladder makes increasingly narrow
spikes too expensive. The unconditional Lipschitz bound converts arbitrarily
high averaged moments into the exact pointwise exponent.

This creates a concrete progression:

```text
2nd moment -> exponent 2/3,
4th moment -> exponent 3/5,
6th moment -> exponent 4/7,
...
2k-th moment -> exponent 1/2 + 1/(4k+2).
```

The sequence converges to the RH exponent.

## Proof boundary

- The reduction from the full moment ladder to RH is complete.
- The critical moment estimates (T-9505.1) are not proved here.
- Proving only finitely many moment orders does not prove RH, although it yields
  an explicit zero-free half-plane through (T-9505.9).
- A proof of all moments must preserve correlations among the reciprocal-cell
  Bernoulli channels; independent absolute-value bounds are too large.
- This theorem does not convert a finite numerical moment table into a cofinal
  result.
