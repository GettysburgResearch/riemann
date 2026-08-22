# L-105205 — Contour-shifted Xi saddle law on the moderate-deviation Fourier scale

Claim ID: `L-105205`  
Status: **PROPOSED UNCONDITIONAL ANALYTIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: `L-105200`; the explicit positive Xi Fourier kernel  
RH status: **not assumed**

## 1. Statement

Retain the tilted Xi measure, saddle and curvature scale

\[
d\nu_m(u)=M_m^{-1}u^m\Phi(u)\,du,
\qquad
w_m=\arg\max[m\log u+\log\Phi(u)],
\qquad
s_m^2=(-S_m''(w_m))^{-1}
\]

from `L-105200`. Put

\[
\vartheta_M=(\log M)^{-1/12},
\qquad
\boxed{
T_M^{\rm md}
=\vartheta_M\left({M\over\log M}\right)^{2/3}.
}
\tag{L-105205.1}

For every fixed `H>0`, uniformly for

\[
m\ge M,
\qquad
|\Re z|\le T_M^{\rm md},
\qquad
|\Im z|\le H,
\]

the one-sided Fourier transform

\[
A_m(z)=\int e^{izu}\,d\nu_m(u)
\]

satisfies

\[
\boxed{
A_m(z)
=
\exp\!\left(iw_mz-{s_m^2z^2\over2}\right)
\left(1+o_{M\to\infty}(1)\right).
}
\tag{L-105205.2}

The error is relative and uniform over the whole half-infinite derivative tail.
For each fixed `r>=0`, the same statement may be differentiated `r` times,
with error

\[
o\!\left(w_m^r
 e^{w_m|\Im z|-\Re(s_m^2z^2)/2}
\right).
\tag{L-105205.3}

This extends `L-105200` from a fixed multiple of the reciprocal standard
deviation to an `o((m/log m)^(2/3))` physical Fourier scale.

## 2. Standardized local expansion

Put

\[
b_m=\sqrt{w_m/m}.
\]

The saddle estimates give

\[
s_m\asymp b_m
\]

and, uniformly on `|u-w_m|<=1`,

\[
S_m^{(3)}(u)=O(m/w_m),
\qquad
S_m^{(4)}(u)=O(m/w_m).
\tag{L-105205.4}

For complex `x` satisfying `|s_mx|<=1/2`, Taylor's theorem on the explicit
zero-free first-term-dominant neighbourhood of `w_m` yields

\[
\boxed{
S_m(w_m+s_mx)-S_m(w_m)
=-{x^2\over2}
+O\!\left(b_m|x|^3+b_m^2|x|^4\right).
}
\tag{L-105205.5}

The same estimate holds after a complex displacement of size `o(1)` in the
`u` plane. This follows directly from the explicit series for `Phi`: the
`n=1` summand dominates uniformly with all four derivatives in a fixed complex
neighbourhood of the real saddle, and therefore `Phi` has no zero there for
large `m`.

## 3. Why the exponent two-thirds appears

Write

\[
\lambda=i s_m z.
\]

At the endpoint (L-105205.1), monotonicity of `log m/m` gives

\[
\boxed{
|\lambda|
\ll
\vartheta_M b_m^{-1/3}.
}
\tag{L-105205.6}

uniformly for every `m>=M`. The cubic standardized remainder at the shifted
Gaussian saddle is therefore

\[
b_m|\lambda|^3=O(\vartheta_M^3)=o(1),
\tag{L-105205.7}
\]

while

\[
b_m^2|\lambda|^4
=O(\vartheta_M^4 b_m^{2/3})=o(1).
\tag{L-105205.8}
\]

This is the sharp range of a purely quadratic relative asymptotic before a
cubic Edgeworth term becomes order one.

## 4. Contour shift and relative asymptotic

In standardized coordinates,

\[
A_m(z)
=e^{iw_mz}
{\displaystyle
 \int_{-w_m/s_m}^{\infty}
 e^{F_m(x)+\lambda x}\,dx
 \over\displaystyle
 \int_{-w_m/s_m}^{\infty}e^{F_m(x)}\,dx},
\qquad
F_m(x)=S_m(w_m+s_mx)-S_m(w_m).
\tag{L-105205.9}

The integrand before normalization is the entire function
`u^m Phi(u)e^(izu)`. Shift the `u` contour by

\[
s_m\lambda=i s_m^2z.
\]

By (L-105205.6),

\[
|s_m\lambda|
\ll\vartheta_M b_m^{2/3}=o(1).
\tag{L-105205.10}
\]

The connector at zero is exponentially negligible because of the factor
`u^m`; the connector at infinity vanishes by the double-exponential term
`exp(-pi exp(2u))`. The shifted contour remains in a strip where
`Re exp(2u)>0`.

Set `x=y+lambda`. The quadratic terms complete the square:

\[
-{(y+\lambda)^2\over2}+\lambda(y+\lambda)
=-{y^2\over2}+{\lambda^2\over2}.
\tag{L-105205.11}
\]

Choose `R_m=b_m^(-1/12)`. On `|y|<=R_m`, equations
(L-105205.5)--(L-105205.8) give

\[
F_m(y+\lambda)+\lambda(y+\lambda)
=-{y^2\over2}+{\lambda^2\over2}+o(1)
\tag{L-105205.12}
\]

uniformly. On `|y|>R_m` but `|s_my|<=1/2`, strict complex saddle concavity
gives `exp(-cR_m^2)` domination. Outside the local saddle neighbourhood, the
left `u^m` loss and right double-exponential loss used in `L-105200` remain
uniform under the displacement (L-105205.10).

Hence

\[
\int e^{F_m(x)+\lambda x}\,dx
=e^{\lambda^2/2}\sqrt{2\pi}(1+o(1)),
\]

and the denominator is `sqrt(2pi)(1+o(1))`. Since
`exp(lambda^2/2)` is nonzero, this proves the relative formula
(L-105205.2).

## 5. Derivatives

Apply the same proof with `2 vartheta_M` in place of `vartheta_M`. The resulting
relative approximation holds on a complex neighbourhood of every point in the
smaller box. Cauchy's integral formula gives all fixed `lambda` derivatives.
Combining with the exact factor `exp(iw_mz)` and
`lambda=i s_mz` proves (L-105205.3).

## 6. Explicit height/order consequence

Since

\[
T_M^{\rm md}
={M^{2/3}\over(\log M)^{3/4}},
\tag{L-105205.13}
\]

a rectangle of original height `T` lies in the moderate-deviation box once

\[
\boxed{
M\ge K T^{3/2}(\log(2+T))^{9/8}
}
\tag{L-105205.14}

for a sufficiently large constant `K=K(H)`. More flexibly, choosing any
`vartheta_M->0` gives the entry order `T^(3/2+o(1))`.

## 7. Scope

The theorem is a relative complex saddle expansion and is stronger than a
central limit theorem. It does not cover the order-one cubic Edgeworth boundary
or heights comparable to `m/log m`. It does not descend the resulting
high-derivative real-rooted box to Xi and does not prove RH.
