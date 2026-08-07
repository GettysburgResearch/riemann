# L-21910 — Canonical Xi Mellin–gamma interpolant

Claim ID: `L-21910`  
Title: The Riemann Xi moment data have one canonical entire interpolation whose unit shift quotient reproduces the exact Bernstein-gamma coefficients  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Primary external interface: Konstantopoulos–Patie–Sarkar, arXiv:2211.16680, especially (4.14), Theorem 23, and (4.15)–(4.18)  
Scope: exact interpolation and coefficient reconstruction; no Pick or zero-location assertion

## 1. Normalized Riemann characteristic function

Let

\[
 \Xi(t)=\frac{\xi(\frac12+it)}{\xi(\frac12)}.
 \tag{L-21910.1}
\]

Use the classical positive even Riemann kernel `Phi`, normalized by

\[
 \Xi(t)=\frac{2}{\xi(\frac12)}
 \int_0^\infty \Phi(x)\cos(tx)\,dx.
 \tag{L-21910.2}
\]

Thus `Xi` is the characteristic function of the symmetric probability density

\[
 p_\Xi(x)=\frac{\Phi(|x|)}{\xi(\frac12)}.
 \tag{L-21910.3}
\]

Put

\[
 m_{2n}=\int_{\mathbb R}x^{2n}p_\Xi(x)\,dx
 =\frac{2}{\xi(\frac12)}
 \int_0^\infty x^{2n}\Phi(x)\,dx.
 \tag{L-21910.4}
\]

Then

\[
 \boxed{
 \Xi(t)=\sum_{n=0}^\infty
 \frac{(-1)^n m_{2n}}{(2n)!}t^{2n}.}
 \tag{L-21910.5}
\]

The kernel is even analytic at zero and superexponentially decreasing at
infinity. Write its local expansion as

\[
 \Phi(x)=\sum_{k=0}^\infty a_kx^{2k}.
 \tag{L-21910.6}
\]

## 2. Meromorphic fractional-moment transform

Initially for `Re z>-1/2`, define

\[
 \mathcal M_\Xi(z)
 =\frac{2}{\xi(\frac12)}
  \int_0^\infty x^{2z}\Phi(x)\,dx.
 \tag{L-21910.7}
\]

For every integer `N>=1`, Taylor subtraction gives

\[
\begin{aligned}
 \mathcal M_\Xi(z)
 =\frac{2}{\xi(\frac12)}\Bigg[&
 \int_1^\infty x^{2z}\Phi(x)\,dx\\
 &+\int_0^1x^{2z}
   \left(\Phi(x)-\sum_{k=0}^{N-1}a_kx^{2k}\right)dx\\
 &+\sum_{k=0}^{N-1}\frac{a_k}{2z+2k+1}
 \Bigg].
\end{aligned}
 \tag{L-21910.8}
\]

The first two terms are holomorphic for `Re z>-N-1/2`. Therefore
`M_Xi` extends meromorphically to the whole plane, with possible simple poles
only at

\[
 z=-k-\frac12,
 \qquad k=0,1,2,\ldots.
 \tag{L-21910.9}
\]

The residue at `-k-1/2` is `a_k/xi(1/2)`.

## 3. Gamma cancellation and the canonical entire interpolant

Define

\[
 \boxed{
 C_\Xi(z)=
 \frac{\sqrt\pi\,4^{-z}}
      {\Gamma(z+\frac12)}
 \mathcal M_\Xi(z).}
 \tag{L-21910.10}
\]

The reciprocal gamma factor has a simple zero at every point in
(L-21910.9), and no other zero. Hence every Mellin pole is removable and

\[
 \boxed{C_\Xi\text{ is entire}.}
 \tag{L-21910.11}
\]

It is real on the real axis, satisfies

\[
 C_\Xi(0)=1,
 \tag{L-21910.12}
\]

and is strictly positive on `(-1/2,infinity)` because the integral in
(L-21910.7) and the gamma factor are positive there.

At every nonnegative integer, the gamma duplication identity gives

\[
 \frac{\sqrt\pi\,4^{-n}}
      {\Gamma(n+\frac12)}
 =\frac{n!}{(2n)!}.
 \tag{L-21910.13}
\]

Consequently

\[
 \boxed{
 C_\Xi(n)=\frac{n!m_{2n}}{(2n)!}.}
 \tag{L-21910.14}
\]

This is exactly the coefficient interpolation required by equation (4.17) of
Konstantopoulos–Patie–Sarkar, written directly in the probability normalization
of `Xi`.

## 4. Canonical unit-shift quotient

Define the meromorphic shift quotient

\[
 \boxed{
 \phi_\Xi(z)=\frac{C_\Xi(z-1)}{C_\Xi(z)}.}
 \tag{L-21910.15}
\]

For `Re z>1/2`, no continuation is needed and (L-21910.10) yields the explicit
fractional-moment ratio

\[
 \boxed{
 \phi_\Xi(z)
 =4\left(z-\frac12\right)
  \frac{\mathcal M_\Xi(z-1)}
       {\mathcal M_\Xi(z)}.}
 \tag{L-21910.16}
\]

At every positive integer,

\[
 \boxed{
 \phi_\Xi(n)
 =2(2n-1)\frac{m_{2n-2}}{m_{2n}}.}
 \tag{L-21910.17}
\]

This is the exact moment-ratio form of the discrete interpolation problem in
(4.18) of the cited paper.

## 5. Exact Bernstein-gamma telescoping

For a function `phi` on the positive integers, write

\[
 W_\phi(n+1)=\prod_{k=1}^n\phi(k),
 \qquad W_\phi(1)=1.
 \tag{L-21910.18}
\]

Using (L-21910.15) and `C_Xi(0)=1`,

\[
 \boxed{
 W_{\phi_\Xi}(n+1)
 =\prod_{k=1}^n\frac{C_\Xi(k-1)}{C_\Xi(k)}
 =\frac1{C_\Xi(n)}.}
 \tag{L-21910.19}
\]

Put

\[
 \Psi_\Xi(u)=u\phi_\Xi(u).
 \tag{L-21910.20}
\]

Then

\[
 W_{\Psi_\Xi}(n+1)
 =n!W_{\phi_\Xi}(n+1)
 =\frac{n!}{C_\Xi(n)}
 =\frac{(2n)!}{m_{2n}}.
 \tag{L-21910.21}
\]

Therefore the generalized Bessel series attached to this integer data is
exactly the normalized Riemann function:

\[
\begin{aligned}
 \mathcal J_{\Psi_\Xi}(t)
 &=\sum_{n=0}^\infty
   \frac{(-1)^n}{W_{\Psi_\Xi}(n+1)}t^{2n}\\
 &=\sum_{n=0}^\infty
   \frac{(-1)^nm_{2n}}{(2n)!}t^{2n}\\
 &=\boxed{\Xi(t).}
\end{aligned}
 \tag{L-21910.22}
\]

No interpolation uniqueness theorem is used in (L-21910.22): the series only
uses the positive-integer values, and those values telescope exactly.

## 6. One exact Pick-kernel interface

The canonical quotient is a Pick function precisely when the kernels

\[
 \boxed{
 \mathfrak P_\Xi(z,w)
 =\frac{
   \phi_\Xi(z)-\overline{\phi_\Xi(w)}
  }{z-\overline w}}
 \tag{L-21910.23}
\]

are positive semidefinite on every finite subset of the upper half-plane.
Substitution of (L-21910.15) rewrites the numerator without division by a
moment ratio:

\[
 \boxed{
 \phi_\Xi(z)-\overline{\phi_\Xi(w)}
 =\frac{
 C_\Xi(z-1)\overline{C_\Xi(w)}
 -C_\Xi(z)\overline{C_\Xi(w-1)}
 }{C_\Xi(z)\overline{C_\Xi(w)}}.}
 \tag{L-21910.24}
\]

Thus the final interpolation question can be attacked either through the
upper-half-plane Pick matrices (L-21910.23) or through the zero geometry of the
single entire function `C_Xi`.

## 7. What is and is not proved

Closed exactly:

- global meromorphic continuation of the fractional-moment transform;
- cancellation of all Mellin poles by the reciprocal gamma factor;
- the entire function `C_Xi`;
- its exact positive-integer values;
- the canonical shift quotient;
- the complete coefficient telescoping
  `J_(u phi_Xi)=Xi`.

Not proved:

- that `phi_Xi` is a Bernstein function;
- that it is Pick;
- positivity of every matrix in (L-21910.23);
- real, simple, one-separated zeros of `C_Xi`;
- RH.

Those conditions are isolated in `T-21903`. The present lemma must not be read
as a zero-location theorem.