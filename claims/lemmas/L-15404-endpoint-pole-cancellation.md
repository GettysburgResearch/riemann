# L-15404 — Endpoint packets expose exact prime-pole cancellation

Claim ID: `L-15404`  
Title: Odd endpoint packets cancel the exponentially large zeta-pole and polar channels before any scalar localization  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15401`; the prime number theorem; elementary convolution algebra  
Scope: endpoint-scaled odd test functions for Suzuki's localized Weil form  
Related counterexample candidates: none

## Purpose

`L-15403` proves that the scalar Barta residual has mean about
`-16 exp(a)/a`.  This is not a negative Rayleigh value.  The present lemma
identifies the missing positive term exactly: prime powers in a terminal
multiplicative window create a phase-sensitive Hankel reflection whose
zeta-pole main term cancels the negative polar rank one at order `exp(a)`.

Thus the scalar no-go is caused by separating two terms which must be retained
as one correlated object.

## Endpoint packet

Fix `R>0` and a real profile

\[
 \phi\in C_c^\infty(0,R).
 \tag{L-15404.1}
\]

For `a>2R`, define the positive-half packet

\[
 f_{a,\phi}(x)=
 \begin{cases}
  \sqrt a\,\phi(a(1-x)),&1-R/a<x<1,\\
  0,&0<x\le1-R/a,
 \end{cases}
 \tag{L-15404.2}
\]

and let `w_(a,phi)` be its odd extension to `(-1,1)`.  Then

\[
 \boxed{\|w_{a,\phi}\|_2^2=2\|\phi\|_{L^2(0,R)}^2.}
 \tag{L-15404.3}
\]

Put

\[
 \Phi_-(\phi)=\int_0^R e^{-r/2}\phi(r)\,dr,
 \qquad
 \Phi_+(\phi)=\int_0^R e^{r/2}\phi(r)\,dr.
 \tag{L-15404.4}
\]

For `0<=v<=R`, define the same-end autocorrelation

\[
 A_\phi(v)=\int_v^R\phi(r-v)\phi(r)\,dr,
 \tag{L-15404.5}
\]

and, for `0<=u<=2R`, the endpoint-reflection convolution

\[
 C_\phi(u)=
 \int_{\max(0,u-R)}^{\min(R,u)}
 \phi(u-r)\phi(r)\,dr.
 \tag{L-15404.6}
\]

## Exact polar term

For odd `w`, only the negative `sinh` polar channel survives.  Direct change of
variables gives

\[
 S_a(w_{a,\phi})
 ={1\over\sqrt a}
 \left(e^{a/2}\Phi_-(\phi)-e^{-a/2}\Phi_+(\phi)\right).
 \tag{L-15404.7}
\]

Hence its exact contribution is

\[
\boxed{
 \mathcal R_a(\phi)
 =-2a|S_a(w_{a,\phi})|^2
 =-2\left|
 e^{a/2}\Phi_-(\phi)-e^{-a/2}\Phi_+(\phi)
 \right|^2.}
 \tag{L-15404.8}
\]

In particular,

\[
 e^{-a}\mathcal R_a(\phi)
 \longrightarrow-2|\Phi_-(\phi)|^2.
 \tag{L-15404.9}
\]

## Exact prime support reduction

Write

\[
 c_n={\Lambda(n)\over\sqrt n},
 \qquad
 \delta_n={\log n\over a}.
\]

The prime part in Suzuki's original translated-correlation form is

\[
 \mathcal P_a(w)
 =-2\sum_{n\le e^{2a}}c_n
 \operatorname{Re}\int_{-1}^{1-\delta_n}
 w(x+\delta_n)\overline{w(x)}\,dx.
 \tag{L-15404.10}
\]

For the endpoint packet, the correlation is identically zero except in two
windows:

1. `log n<=R`, where a shift overlaps each endpoint with itself;
2. `0<=2a-log n<=2R`, where a shift transports the negative endpoint packet to
   the positive endpoint packet.

The exact formula is

\[
\boxed{
\begin{aligned}
 \mathcal P_a(w_{a,\phi})={}&
 -4\sum_{\log n\le R}c_n A_\phi(\log n)\\
 &+2\sum_{0\le2a-\log n\le2R}
 c_n C_\phi(2a-\log n).
\end{aligned}}
 \tag{L-15404.11}
\]

Thus all prime powers in the enormous middle interval

\[
 e^R<n<e^{2a-2R}
\]

have exactly zero overlap with this witness.  The cofinal arithmetic is carried
by one fixed small-prime prefix and one moving terminal prime-power window.

## Terminal prime measure

Define the positive measure on `[0,2R]`

\[
 \nu_a=
 e^{-a}\sum_{0\le2a-\log n\le2R}
 {\Lambda(n)\over\sqrt n}
 \delta_{2a-\log n}.
 \tag{L-15404.12}
\]

The prime number theorem implies vague convergence

\[
\boxed{
 \nu_a\Longrightarrow e^{-u/2}\,du
 \qquad(a\to\infty).}
 \tag{L-15404.13}
\]

More explicitly, for every continuous `F` on `[0,2R]`,

\[
 e^{-a}\sum_{0\le2a-\log n\le2R}
 {\Lambda(n)\over\sqrt n}F(2a-\log n)
 \longrightarrow
 \int_0^{2R}e^{-u/2}F(u)\,du.
 \tag{L-15404.14}
\]

### Proof of the measure limit

Let `X=e^(2a)` and `psi(x)=sum_(n<=x) Lambda(n)`.  The left side is the
Stieltjes integral

\[
 X^{-1/2}\int_{Xe^{-2R}}^X
 t^{-1/2}F(\log(X/t))\,d\psi(t).
\]

The PNT gives `psi(t)=t(1+o(1))` uniformly on this fixed-ratio interval.
Integration by parts reduces the limit to the same expression with `dpsi=dt`.
The substitution `t=Xe^{-u}` then gives (L-15404.14).

## Rank-one convolution identity

Fubini gives

\[
\boxed{
 \int_0^{2R}e^{-u/2}C_\phi(u)\,du
 =|\Phi_-(\phi)|^2.}
 \tag{L-15404.15}
\]

Therefore the terminal prime term obeys

\[
 e^{-a}\left[
 2\sum_{0\le2a-\log n\le2R}
 c_nC_\phi(2a-\log n)
 \right]
 \longrightarrow2|\Phi_-(\phi)|^2.
 \tag{L-15404.16}
\]

Combining (L-15404.9) and (L-15404.16) proves the main cancellation:

\[
\boxed{
 e^{-a}\left(
 \mathcal P_a(w_{a,\phi})+
 \mathcal R_a(\phi)
 \right)\longrightarrow0.}
 \tag{L-15404.17}
\]

The fixed small-prime row in (L-15404.11) is `O_phi(1)` and does not affect the
limit.

## Complete-form scale

The remaining scalar, logarithmic, and cancellation-safe archimedean terms of
`L-15401` grow at most polynomially in `a` for one fixed smooth profile.  In
particular,

\[
 \boxed{e^{-a}q_a(w_{a,\phi})\longrightarrow0.}
 \tag{L-15404.18}
\]

This does not assert that the unscaled value tends to zero or has a fixed sign.
It says that the apparent order-`exp(a)` instability of the odd potential is
exactly absent from the true phase-aware form.

## Wider meaning

1. The two terms contributing `-8 exp(a)/a` each to the scalar potential mean
   are not independent defects.  The prime pole and polar channel are one
   rank-one cancellation pair.
2. A scalar positive ground-state transform destroys the endpoint-reflection
   convolution and therefore cannot see (L-15404.15).
3. The correct low packet is phase-aware.  At leading boundary scale it is the
   one-dimensional Laplace channel `Phi_-`; after pole subtraction, the
   remainder is governed by zeta zeros.
4. Endpoint packets provide a new exact search family whose prime side uses only
   two windows.

## Gap audit

- The exact constants inherit Suzuki's normalization from `L-15401`.
- Formula (L-15404.11) assumes `a>2R`, so the two overlap regimes are disjoint.
- The PNT gives only the leading cancellation.  It does not give an absolute
  `o(1)` bound for the unscaled form.
- A midpoint approximation to the terminal prime window is not a certificate.
- The result explains the scalar no-go; it neither proves nor disproves RH.
