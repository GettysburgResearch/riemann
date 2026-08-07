# L-15421 — The de Branges kernel is the horizontal integral of the Riemann Weyl kernel

Claim ID: `L-15421`  
Title: Exact de Branges–Weyl shift-flow identity for the even Riemann kernel  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-01  
Dependencies: the Fourier normalization of the even Riemann kernel `Phi`; the coordinate Weyl kernel in arXiv:2606.29555  
Scope: direct canonical-system bridge for Issue #180  
Related counterexample candidates: none

## Setup

Let `Phi` be real, even, and rapidly decreasing, and use the Fourier convention

\[
 \Xi(z)=\int_{\mathbb R}\Phi(t)e^{izt}\,dt.
 \tag{L-15421.1}
\]

For `omega>=0`, define

\[
 E_\omega(z)=\Xi(z+i\omega),
 \qquad
 E_\omega^\#(z)=\overline{E_\omega(\bar z)}=\Xi(z-i\omega).
 \tag{L-15421.2}
\]

The de Branges kernel is

\[
 \mathcal D_\omega(z,w)=
 \frac{
 E_\omega(z)\overline{E_\omega(w)}
 -E_\omega^\#(z)\overline{E_\omega^\#(w)}
 }{2\pi i(\bar w-z)}.
 \tag{L-15421.3}
\]

For real coordinate variables `a,b`, put

\[
 s={a+b\over2},
 \qquad
 d={a-b\over2}.
 \tag{L-15421.4}
\]

Let the Riemann Weyl kernel be

\[
 \boxed{
 \mathcal K_\omega^{W}(a,b)=
 {1\over2}
 \int_{|s|}^{\infty}
 y\cosh(2\omega y)
 \Phi(y+d)\Phi(y-d)\,dy.}
 \tag{L-15421.5}
\]

This is the coordinate kernel appearing in equation (6) of arXiv:2606.29555, up to its declared harmless scalar Fourier normalization.

## Exact coordinate formula

For `z,w` in the upper half-plane,

\[
 {1\over i(\bar w-z)}
 =\int_0^\infty e^{-i(\bar w-z)r}\,dr.
 \tag{L-15421.6}
\]

Substitution of the Fourier integrals for `E_omega,E_omega^#`, followed by

\[
 a=t+r,
 \qquad
 b=u+r,
 \tag{L-15421.7}
\]

gives

\[
 \mathcal D_\omega(z,w)
 =\iint_{\mathbb R^2}
 \widetilde{\mathcal D}_\omega(a,b)
 e^{iza-i\bar wb}\,da\,db,
 \tag{L-15421.8}
\]

where

\[
 \boxed{
 \widetilde{\mathcal D}_\omega(a,b)=
 {1\over\pi}
 \int_{|s|}^{\infty}
 \sinh(2\omega y)
 \Phi(y+d)\Phi(y-d)\,dy.}
 \tag{L-15421.9}
\]

The absolute value in the lower limit is exact. Before using evenness, the lower limit is `-s`; the product

\[
 \Phi(y+d)\Phi(y-d)
\]

is even in `y`, while `sinh(2 omega y)` is odd. Therefore

\[
 \int_{-s}^{\infty}(\text{odd integrand})\,dy
 =\int_{|s|}^{\infty}(\text{same integrand})\,dy.
 \tag{L-15421.10}
\]

## Horizontal Loewner-flow identity

Differentiating (L-15421.9) under the integral gives

\[
 \partial_\omega
 \widetilde{\mathcal D}_\omega(a,b)
 = {2\over\pi}
 \int_{|s|}^{\infty}
 y\cosh(2\omega y)
 \Phi(y+d)\Phi(y-d)\,dy.
 \tag{L-15421.11}
\]

Hence, with the normalization (L-15421.5),

\[
 \boxed{
 \partial_\omega
 \widetilde{\mathcal D}_\omega
 ={4\over\pi}\mathcal K_\omega^{W}.}
 \tag{L-15421.12}
\]

Since `E_0=E_0^#`, one has `widetilde D_0=0`. Therefore

\[
 \boxed{
 \widetilde{\mathcal D}_\omega
 ={4\over\pi}
 \int_0^\omega \mathcal K_u^{W}\,du.}
 \tag{L-15421.13}
\]

The identity holds first on Schwartz test functions, then on every closed form domain for which either side is defined.

## Canonical consequence

It is sufficient to prove the **cumulative Weyl inequality**

\[
 \boxed{
 \int_0^\omega \mathcal K_u^{W}\,du\succeq0
 \qquad(0<\omega<1/2).}
 \tag{L-15421.14}
\]

Pointwise Weyl positivity in `u` is stronger than necessary. Equation (L-15421.13) then gives positivity of the shifted de Branges kernel directly. No KLM coherent-state intertwiner or limiting pullback map is required.

This closes the algebraic bridge listed as open in Appendix C.1 of arXiv:2606.29555, subject to independent review of the common Fourier normalization and form closure.

## Gap audit

- The sign in (L-15421.9) depends on choosing `E_omega(z)=Xi(z+i omega)` exactly as displayed.
- The denominator is `2 pi i (bar(w)-z)`; changing its orientation changes the sign.
- The identity bridges the **original coordinate Weyl kernel**, not merely a normalized quotient model.
- It does not prove cumulative Weyl positivity.
- Any use of a Volterra quotient certificate still needs an exact quotient-to-original equality before (L-15421.13) can consume it.
- No claim of historical priority is made before a dedicated source comparison.
