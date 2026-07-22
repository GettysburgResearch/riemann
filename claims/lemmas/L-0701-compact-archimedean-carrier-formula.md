# L-0701 — Compact archimedean formula for the triangular carrier

Claim ID: L-0701  
Title: Compact archimedean formula for the triangular carrier  
Status: PROPOSED  
Authoring agent: `gpt56-01-b`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: D-0701; standard integral representation of the digamma function  
Scope: one-dimensional translated triangular test family  
Related counterexample candidates: none

## Statement

Let `T>0`, `L>0`, `Delta=L/(2*pi)`, and let `g=g_{T,Delta}` be D-0701. Put

\[
 h_+(r)=\operatorname{Re}\psi\!\left(\frac14+\frac{ir}{2}\right)-\log\pi.
\]

Then the archimedean contribution

\[
 A(T,L)=\frac{1}{2\pi}\int_{\mathbb R}h_+(r)g(r)\,dr
\]

has the compact representation

\[
 A(T,L)=\frac{1}{2\pi}\left[
 \log\frac{T}{2\pi}-\operatorname{Ci}(LT)
 -\int_0^{2L} b_L(t)\cos\frac{Tt}{2}\,dt
 \right],
\]

where

\[
 b_L(t)=\frac{e^{-t/4}}{1-e^{-t}}\left(1-\frac{t}{2L}\right)-\frac1t
\]

is interpreted by its removable value

\[
 b_L(0)=\frac14-\frac{1}{2L}.
\]

An equivalent cancellation-safe form, valid also at `T=0` by continuity, is

\[
 \frac{1}{2\pi}\left[
 \int_0^{2L}\left\{
 \frac{e^{-t}-\cos(Tt/2)}{t}-b_L(t)\cos(Tt/2)
 \right\}dt+E_1(2L)-\log\pi
 \right].
\]

## Proof

For `Re z>0`, use

\[
 \psi(z)=\int_0^\infty\left(\frac{e^{-t}}t-
 \frac{e^{-zt}}{1-e^{-t}}\right)dt,
\]

with the two singular terms interpreted together. Taking real parts at
`z=1/4+ir/2` gives

\[
 h_+(r)=\int_0^\infty\left(
 \frac{e^{-t}}t-rac{e^{-t/4}\cos(rt/2)}{1-e^{-t}}
 \right)dt-\log\pi.
\]

The triangular carrier satisfies

\[
 \int_{\mathbb R}g(r)\,dr=\widehat g(0)=1
\]

and, by the Fourier convention,

\[
 \int_{\mathbb R}g(r)\cos(rt/2)\,dr
 =\widehat g\!\left(\frac{t}{4\pi}\right)
 =\left(1-\frac{t}{2L}\right)\cos\frac{Tt}{2}
\]

for `0<=t<=2L`, and zero for `t>2L`. Substitution and splitting the first term at
`2L` yield the cancellation-safe formula.

To reduce it, use

\[
 \int_0^X\frac{e^{-t}-\cos(\omega t)}t\,dt+E_1(X)
 =\log\omega-\operatorname{Ci}(\omega X)
\]

with `X=2L` and `omega=T/2`, then combine `-log pi`.

The expansion of `b_L` at zero proves removability.

## Motivation

The original real-line archimedean integral is poorly suited to enormous
carriers. The compact formula moves all non-elementary integration to a fixed
interval of length `2L`, exposing a smooth oscillatory correction to the leading
term `log(T/(2*pi))/(2*pi)`.

## Analytic domain audit

- `T,L` are positive real numbers.
- `Ci(LT)` is the standard real cosine integral at positive argument; no branch
  ambiguity occurs.
- The singularity at `t=0` is removable only after the displayed cancellation.
- Interchanging integrals requires the decay/admissibility estimates for `g` and
  a dominated regularization near zero; an independent verifier should write
  this step explicitly.

## Dependency audit

The calculation uses only D-0701 and the standard digamma integral
representation. Matching this archimedean term to the project's Weil functional
still depends on the D-0001 sign and normalization audit.

## Gap audit

1. Numerically integrating the compact formula at huge `T` without an
   oscillatory error bound is not rigorous.
2. Replacing the integral and `Ci` by zero is only an asymptotic screen.
3. The `T=0` case must use the cancellation-safe form rather than `log T`.
4. An independent derivation must check the `t/(4*pi)` Fourier argument.

## Adversarial tests

X-0701 compares the cancellation-safe and `Ci` forms at multiple moderate
carriers to more than 50 decimal digits. Earlier local validation also matched
the `T=0` value against the `N=0` cutoff-free matrix normalization.

## Remaining uncertainty

The formula is complete-looking and numerically cross-checked, but it has not
received an independent analytic review. Status remains `PROPOSED`.

## Suggested next attack

Develop an Arb implementation using integration by parts or oscillatory Taylor
panels, and produce a certified enclosure uniform for `T>3e12`.
