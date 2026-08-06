# L-15143 — Phase-complete prime energy recovers the rightmost zero

Claim ID: `L-15143`  
Title: The local \(L^2\) growth exponent of one finite triangular prime-power window is exactly the horizontal displacement of the rightmost zeta zero  
Status: **PROPOSED PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: `L-15409`; the pole-free Laplace identity and explicit-formula continuation used in `T-15406`; standard unit-interval zero counting  
Scope: one positive, phase-complete, finite-prime observable for the full RH problem

## 1. The finite prime signal

Put

\[
 h=\log 4
\]

and retain the compact piecewise-linear pole-free window

\[
 G_h(u)=F_h(u)-2F_h(u-h)
\]

from `L-15409`. Its support is `[0,3h]` and

\[
 \widehat G_{h,L}(z)
 =\left(\frac{1-e^{-hz}}{hz}\right)^2(1-2e^{-hz}).
\]

In particular,

\[
 \widehat G_{h,L}(1/2)=0
\]

and

\[
 \widehat G_{h,L}(z)\ne0
 \qquad(0<\Re z<1/2).
\]

Define the raw finite prime-power statistic

\[
 \boxed{
 Q_h(x)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 G_h(x-\log n).}
 \tag{L-15143.1}
\]

At each real `x`, only prime powers in

\[
 e^{x-3h}\le n\le e^x
\]

occur.

Let

\[
 \boxed{
 \Theta_\zeta
 =\sup_{\zeta(\rho)=0}
 \left(\Re\rho-\frac12\right).}
 \tag{L-15143.2}
\]

By the functional equation, `Theta_zeta>=0`, and RH is exactly
`Theta_zeta=0`.

## 2. Positive block and cumulative energies

For `X>=0`, define

\[
 \boxed{
 B_h(X)=\int_X^{X+1}|Q_h(x)|^2\,dx}
 \tag{L-15143.3}
\]

and

\[
 \boxed{
 A_h(X)=\int_0^X|Q_h(x)|^2\,dx.}
 \tag{L-15143.4}
\]

Both are nonnegative finite arithmetic objects. Their breakpoints occur only
at

\[
 x=\log n,\ \log n+h,\ \log n+2h,\ \log n+3h
\]

for prime powers in one finite range; on every resulting cell `Q_h` is affine
and its square is exactly integrable.

## 3. Exact rightmost-zero exponent

The two energies recover the rightmost zero exactly:

\[
 \boxed{
 \Theta_\zeta
 =\limsup_{X\to\infty}
 \frac{\log(1+B_h(X))}{2X}}
 \tag{L-15143.5}
\]

and

\[
 \boxed{
 \Theta_\zeta
 =\limsup_{X\to\infty}
 \frac{\log(1+A_h(X))}{2X}.}
 \tag{L-15143.6}
\]

Equivalently,

\[
 \boxed{
 \Theta_\zeta
 =\inf\left\{\sigma>0:
 \int_0^\infty e^{-2\sigma x}|Q_h(x)|^2\,dx<\infty
 \right\}.}
 \tag{L-15143.7}
\]

Consequently,

\[
 \boxed{
 \mathrm{RH}
 \iff B_h(X)=e^{o(X)}}
 \tag{L-15143.8}
\]

and equivalently

\[
 \boxed{
 \mathrm{RH}
 \iff A_h(X)=e^{o(X)}.}
 \tag{L-15143.9}
\]

This is strictly weaker as a positive target than the bounded-Cesaro-mean-square
criterion in `T-15405/T-15406`. Under RH those stronger bounds hold, but the
present theorem needs only subexponential energy.

## 4. Upper exponent bound

The smoothed explicit formula has the form

\[
 Q_h(x)
 =-\sum_{\rho}m_\rho
 \widehat G_{h,L}(\rho-1/2)
 e^{(\rho-1/2)x}
 +E_h^{\rm triv}(x),
 \tag{L-15143.10}
\]

with the pole term absent because `Ghat_h(1/2)=0`. The trivial-zero and initial
terms have strictly negative exponential type.

Uniformly for `0<=delta<=1/2`,

\[
 \widehat G_{h,L}(\delta+it)=O_h((1+|t|)^{-2}).
\]

Together with the standard unit-interval zero-count bound, this gives

\[
 \sum_\rho m_\rho
 |\widehat G_{h,L}(\rho-1/2)|<\infty.
\]

Since every zero satisfies

\[
 \Re\rho-1/2\le\Theta_\zeta,
\]

there is a constant `C_h` such that

\[
 |Q_h(x)|\le C_h e^{\Theta_\zeta x}+O(e^{-cx}).
 \tag{L-15143.11}
\]

Therefore

\[
 B_h(X)\ll e^{2\Theta_\zeta X}
\]

and

\[
 A_h(X)\ll (1+X)e^{2\Theta_\zeta X},
\]

which proves that the limsups in (L-15143.5)--(L-15143.6) are at most
`Theta_zeta`.

## 5. Reverse exponent bound by Hardy holomorphy

Suppose the block-energy limsup in (L-15143.5) equals `L<Theta_zeta`.
Choose

\[
 L<\eta<\sigma<\Theta_\zeta.
\]

For every sufficiently large integer `N`,

\[
 B_h(N)\le e^{2\eta N}.
\]

Hence

\[
\begin{aligned}
 \int_0^\infty e^{-2\sigma x}|Q_h(x)|^2dx
 &\le C+
 \sum_{N\ge N_0}e^{-2\sigma N}B_h(N)\\
 &<\infty.
\end{aligned}
 \tag{L-15143.12}
\]

Cauchy--Schwarz now shows that the unilateral Laplace transform of `Q_h` is
holomorphic in `Re z>sigma`.

Initially for `Re z>1/2`, `L-15409` gives

\[
 \mathcal LQ_h(z)
 =-\widehat G_{h,L}(z)
 \frac{\zeta'}{\zeta}(z+1/2).
 \tag{L-15143.13}
\]

The left side has just been continued holomorphically to `Re z>sigma`.
By uniqueness of analytic continuation, the right side cannot have a pole
there. Since `Ghat_h` is nonzero throughout

\[
 0<\Re z<1/2,
\]

there is no zeta zero with

\[
 \Re\rho-1/2>\sigma.
\]

This contradicts `sigma<Theta_zeta`. Thus the reverse inequality holds and
(L-15143.5) is proved.

The cumulative formula (L-15143.6) follows either from the same Laplace-abscissa
argument applied to the nondecreasing function `A_h`, or from

\[
 B_h(N)\le A_h(N+1)
\]

and summation of the block upper bounds.

Equation (L-15143.7) is exactly the abscissa-of-convergence formulation of the
same proof.

## 6. Finite prime-pair Gram form

Expanding the square gives

\[
 \boxed{
 B_h(X)=
 \sum_{m,n}
 \frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}}
 \mathcal K_X(\log m,\log n),}
 \tag{L-15143.14}
\]

where

\[
 \mathcal K_X(u,v)
 =\int_X^{X+1}G_h(x-u)G_h(x-v)dx.
 \tag{L-15143.15}
\]

For each frozen `X`, `K_X` is a Gram kernel. Only finitely many prime powers
contribute, and only pairs with

\[
 |\log(m/n)|\le3h
\]

occur. Thus (L-15143.5) measures the complete rightmost-zero displacement by a
sequence of finite positive prime-pair quadratic forms; no zero ordinate and no
sign choice enters their definition.

## 7. Connection to the square-screw and strip-energy routes

`L-19802` recovers `Theta_zeta` from the growth of the negative part of the
square-screw scalar. The present identity gives the same exponent from a
nonnegative, phase-complete energy:

\[
 \boxed{
 \limsup_{N\to\infty}
 \frac{\log(1+(-\mathscr S(N))_+)}{2\log N}
 =
 \limsup_{N\to\infty}
 \frac{\log(1+B_h(\log N))}{2\log N}
 =\Theta_\zeta.}
 \tag{L-15143.16}
\]

The first observable is one-sided and may have sparse negative excursions; the
second cannot lose an off-line mode by phase cancellation.

For every `omega>0`, (L-15143.7) also gives

\[
 \int_0^\infty e^{-2\omega x}|Q_h(x)|^2dx<\infty
\]

if and only if no zero lies in

\[
 \Re s>1/2+\omega.
\]

This is the prime-side Hardy-space counterpart of the Hilbert--Poisson
right-zero energy in `L-19810`.

## 8. What this changes operationally

A full positive proof no longer has to establish an eventual sign, a uniform
spectral moat, or bounded mean square. It is enough to prove the much weaker
prime-only estimate

\[
 \boxed{
 \int_X^{X+1}|Q_h(x)|^2dx=e^{o(X)}.}
 \tag{L-15143.17}
\]

A false RH, on the other hand, forces exponentially deep positive energy blocks:
for every `theta<Theta_zeta`,

\[
 e^{-2\theta X}B_h(X)
\]

is unbounded on the tail.

The theorem therefore supplies one global, phase-complete attack surface for
both proof and disproof.

## 9. Proof boundary

- The exponent theorem is an exact consequence of the pole-free transform,
  explicit-formula continuation, and elementary Hardy/Laplace theory.
- It does not establish the subexponential prime-pair estimate
  (L-15143.17); doing so would prove RH.
- Finite positive energy blocks do not prove or disprove RH without a global
  upper comparison.
- The expensive numerical work in the repository is not rerun or imported as a
  proof of the cofinal estimate.
