# L-9512 — The parabolic Riesz state is exactly the classical analytic totient error

Claim ID: `L-9512`  
Title: Exact identification of the two-Green state with the Kaczorowski–Wiertelak analytic part  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: `L-9511`; elementary Möbius inversion  
Scope: exact arithmetic identity and literature/source normalization  
Related counterexample candidates: none

## Two functions

Put

\[
c=\frac6{\pi^2}.
\tag{L-9512.1}
\]

For real `x>0`, let

\[
\mathcal R_1(x)=
\sum_{n<x}\frac{\varphi(n)}n(x-n)-\frac c2x^2.
\tag{L-9512.2}
\]

For `x>=0`, define the classical analytic part of the summatory-totient error
by

\[
\boxed{
E^{\rm AN}(x)
=\frac12\left(
1+\sum_{d=1}^{\infty}
\mu(d)\left\{\frac xd\right\}^{2}
\right).}
\tag{L-9512.3}
\]

The series converges because, for `d>x`, its summand is
`mu(d)x^2/d^2`, while the initial segment is finite.

## Exact identity

For every real `x>=1`,

\[
\boxed{\mathcal R_1(x)=-E^{\rm AN}(x).}
\tag{L-9512.4}
\]

For `0<=x<=1`, define

\[
\widetilde E^{\rm AN}(x)=\frac c2x^2,
\tag{L-9512.5}
\]

and for `x>=1` put `widetilde E^AN=E^AN`. Then the identity valid on the
complete positive half-line is

\[
\boxed{\mathcal R_1(x)=-\widetilde E^{\rm AN}(x).}
\tag{L-9512.6}
\]

The two definitions agree at `x=1`.

## Proof

Insert

\[
\frac{\varphi(n)}n=\sum_{d\mid n}\frac{\mu(d)}d
\]

in (L-9512.2), write `n=dm`, and use

\[
\frac1d(x-dm)=\frac xd-m.
\]

Because the main constant is

\[
\frac c2x^2
=\frac{x^2}{2}\sum_{d=1}^{\infty}\frac{\mu(d)}{d^2},
\]

we obtain

\[
\mathcal R_1(x)=
\sum_{d=1}^{\infty}\mu(d)
\left[
\sum_{m<x/d}\left(\frac xd-m\right)
-\frac{x^2}{2d^2}
\right].
\tag{L-9512.7}
\]

For every real `y>0`, direct finite summation gives

\[
\boxed{
\sum_{m<y}(y-m)-\frac{y^2}{2}
=-\frac12\lfloor y\rfloor
-\frac12\{y\}^{2}.}
\tag{L-9512.8}
\]

The strict-cutoff convention causes no ambiguity at integer `y`: the omitted
endpoint has weight zero.

Applying (L-9512.8) in (L-9512.7) yields

\[
\mathcal R_1(x)=
-\frac12\sum_{d=1}^{\infty}\mu(d)
 \left\lfloor\frac xd\right\rfloor
-\frac12\sum_{d=1}^{\infty}\mu(d)
 \left\{\frac xd\right\}^{2}.
\tag{L-9512.9}
\]

For `x>=1`, Möbius inversion gives exactly

\[
\sum_{d=1}^{\infty}\mu(d)
 \left\lfloor\frac xd\right\rfloor=1.
\tag{L-9512.10}
\]

Equations (L-9512.3), (L-9512.9), and (L-9512.10) prove (L-9512.4).
For `0<x<1`, the finite sum in (L-9512.2) is empty, giving
`R_1(x)=-cx^2/2`; this proves (L-9512.6).

## Exact Mellin transform

For `Re(s)>2`, termwise integration gives

\[
\boxed{
\int_1^\infty E^{\rm AN}(x)x^{-s-1}\,dx
=-\frac{\zeta(s-1)}{s(s-1)\zeta(s)}
+\frac{3/\pi^2}{s-2}.}
\tag{L-9512.11}
\]

Indeed

\[
\int_n^\infty(x-n)x^{-s-1}\,dx
=\frac{n^{1-s}}{s(s-1)},
\]

and

\[
\sum_{n=1}^{\infty}\frac{\varphi(n)}{n^s}
=\frac{\zeta(s-1)}{\zeta(s)}.
\]

The apparent pole at `s=2` cancels. Every nontrivial zero `rho` of `zeta(s)`
produces a genuine pole at `s=rho`, because `zeta(rho-1)` is nonzero and the
rational factors do not vanish there.

## Energy identity

The positive energy of `L-9511` is therefore exactly

\[
\boxed{
\mathfrak A(x)
=x^{-4}|E^{\rm AN}(x)|^2
+x^{-5}\left[
\frac{c^2}{20}
+\int_1^x|E^{\rm AN}(t)|^2dt
\right]
\qquad(x>=1).}
\tag{L-9512.12}
\]

The constant `c^2/20` is the contribution of the canonical extension
`widetilde E^AN(t)=ct^2/2` on `0<t<1`.

Thus the proposed MMD energy is not merely analogous to the classical analytic
summatory-totient error: it is its endpoint square plus one weighted square
mean exactly.

## Literature boundary

Kaczorowski and Wiertelak introduced the decomposition of the summatory Euler
totient error into arithmetic and analytic parts and proved the RH-equivalent
bound

\[
E^{\rm AN}(x)=O_\varepsilon(x^{1/2+\varepsilon}).
\]

The identity (L-9512.4) places the repository's independently derived
parabolic/two-Green state directly in that classical normalization. It prevents
presenting `T-9503` as a historically new RH equivalence; the new content of the
current stack is the finite parabolic observable, its exact positive RKHS
energy, and the connections to the square-screw and Jordan/Volterra programs.

Primary sources:

1. J. Kaczorowski and K. Wiertelak, *Oscillations of the remainder term related
   to the Euler totient function*, J. Number Theory 130 (2010), 2683–2700.
2. H. Iwata, *On a relation to the Riemann Hypothesis and an analytic part for
   the divisor function*, arXiv:2601.11052, Section 1.1, which restates the
   totient analytic part and the exact RH equivalence.

## Gap audit

- The identity is exact and unconditional.
- It does not prove the critical bound for `E^AN`.
- Consequently it does not prove the critical energy bound or RH.
- The endpoint term in (L-9512.12) is load-bearing. A square-mean estimate alone
  does not automatically control an exceptional pointwise spike.
- Any future proof should be compared directly with the existing analytic-part
  literature before a priority claim is made.
