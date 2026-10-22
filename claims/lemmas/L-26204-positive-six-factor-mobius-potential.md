# L-26204 — Positive six-factor potential for the complete Euler-fiber source

Claim ID: `L-26204`  
Status: `PROPOSED COMPLETE — exact compact-factor and source algebra pending independent review`  
Scope: fixed-source physical-space factorization; no RH input  
Date: 2026-08-08  
Depends on: `L-26201`

Put `h=log 2` and, for `alpha in {0,1/2,1}`, define

\[
u_\alpha(t)=e^{\alpha t}{\bf1}_{0\le t\le h}.
\tag{L-26204.1}
\]

Retain

\[
W=u_1*u_{1/2}*u_{1/2}
\]

and the Euler-fiber inverse source

\[
B_{\mathcal E}(s)
=\frac{(1-2^{1-s})(1-2^{1/2-s})^2}{\zeta(s)}.
\]

## 1. The normalized source window

For the centered variable `z`, the compact signal of `T-26201` has transform

\[
\widehat Z(z)
=\widehat W(z)
 \frac{P(z+1/2)}{\zeta(z+1/2)},
\tag{L-26204.2}
\]

where

\[
P(z+1/2)
=(1-2^{1/2-z})(1-2^{-z})^2.
\tag{L-26204.3}
\]

Define the nonnegative compact convolution

\[
\boxed{
K
=u_1*u_{1/2}*u_{1/2}*u_{1/2}*u_0*u_0.
}
\tag{L-26204.4}
\]

Then

\[
K(t)\ge0,
\qquad
\operatorname{supp}K\subset[0,6\log2],
\tag{L-26204.5}
\]

and

\[
\widehat K(z)
=\frac{1-2^{1-z}}{z-1}
 \left(\frac{1-2^{1/2-z}}{z-1/2}\right)^3
 \left(\frac{1-2^{-z}}{z}\right)^2.
\tag{L-26204.6}
\]

Consequently

\[
\boxed{
\widehat W(z)P(z+1/2)
=z^2(z-1/2)\widehat K(z).
}
\tag{L-26204.7}
\]

## 2. Positive-potential representation

Define

\[
\boxed{
Y_K(t)
=\sum_{n\ge1}\frac{\mu(n)}{\sqrt n}
 K(t-\log n).
}
\tag{L-26204.8}
\]

At each fixed `t` the sum is finite. Equation (L-26204.7) gives the exact physical identity

\[
\boxed{
Z
=\partial_t^2(\partial_t-1/2)Y_K
}
\tag{L-26204.9}
\]

as a causal distribution, including every endpoint atom of the compact spline.

Thus the complete five-tap Euler-fiber source is a third-order boundary operator applied to one positive compact Möbius potential. This does not assert that `Y_K` or `Z` has one sign.

## 3. The normalized five-tap fiber

Let an odd squarefree core be `m`. Dividing the local coefficients of `b_E(2^nu m)` by `sqrt(2^nu m)` gives, apart from the common factor `mu(m)/sqrt(m)`, the polynomial

\[
\boxed{
 r(z)
 =(1-z/\sqrt2)(1-\sqrt2 z)(1-z)^2.
}
\tag{L-26204.10}
\]

Equivalently,

\[
\boxed{
\begin{aligned}
r(z)={}&1-\left(2+\frac{3\sqrt2}{2}\right)z
 +(2+3\sqrt2)z^2\\
&-\left(2+\frac{3\sqrt2}{2}\right)z^3+z^4.
\end{aligned}}
\tag{L-26204.11}
\]

The fiber is palindromic. Its even taps are all positive and its odd taps are all negative. Splitting by the parity of `v_2(n)` therefore produces two sign-complete local subfibers.

## 4. Strip zeros and scope

The additional differential multiplier in (L-26204.9) is

\[
z^2(z-1/2),
\]

whose zeros lie on the boundary lines of the centered counterexample strip. The compact factors in `K_hat` likewise have zeros only on the boundary lines

\[
\Re z\in\{0,1/2,1\}.
\]

Therefore the positive-potential representation neither cancels nor moves a hypothetical off-line pole of `1/zeta(z+1/2)`.

It supplies a fixed compact Sobolev/Green realization for production. It does not by itself give a block-energy upper bound.

## 5. Proof boundary

Closed exactly:

- the six-factor nonnegative compact potential;
- the third-order physical boundary operator;
- the normalized palindromic five-tap fiber;
- preservation of every off-line inverse-zeta pole.

Not closed:

- a coercive local block estimate;
- reflected forcing control;
- `EFRC`;
- RH.
