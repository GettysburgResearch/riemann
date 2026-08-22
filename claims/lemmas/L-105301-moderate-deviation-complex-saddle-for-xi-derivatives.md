# L-105301 — Contour-shifted Xi saddle law on the moderate-deviation Fourier scale

Claim ID: `L-105301`  
Status: **PROPOSED UNCONDITIONAL ANALYTIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: proposed parent `L-105200`; the explicit positive Xi Fourier kernel  
RH status: **not assumed**

## 1. Statement

Retain the tilted Xi measure, saddle and curvature scale

\[
d\nu_m(u)=M_m^{-1}u^m\Phi(u)\,du,
\qquad
w_m=\arg\max[m\log u+\log\Phi(u)],
\qquad
s_m^2=(-S_m''(w_m))^{-1}.
\]

Put

\[
\vartheta_M=(\log M)^{-1/12},
\qquad
\boxed{
T_M^{\rm md}
=\vartheta_M\left({M\over\log M}\right)^{2/3}.
}
\tag{L-105301.1}

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
\tag{L-105301.2}

The error is relative and uniform over the whole half-infinite derivative tail.
For each fixed `r>=0`, the statement may be differentiated `r` times, with
error

\[
o\!\left(w_m^r
 e^{w_m|\Im z|-\Re(s_m^2z^2)/2}
\right).
\tag{L-105301.3}

This extends the parent natural-scale Gaussian theorem from a fixed multiple
of reciprocal standard deviation to an `o((m/log m)^(2/3))` physical Fourier
scale.

## 2. Standardized local expansion

Put

\[
b_m=\sqrt{w_m/m}.
\]

The saddle estimates give `s_m asy b_m` and, uniformly on
`|u-w_m|<=1`,

\[
S_m^{(3)}(u)=O(m/w_m),
\qquad
S_m^{(4)}(u)=O(m/w_m).
\tag{L-105301.4}

For complex `x` satisfying `|s_mx|<=1/2`, Taylor's theorem on the explicit
zero-free first-term-dominant neighbourhood of `w_m` gives

\[
\boxed{
S_m(w_m+s_mx)-S_m(w_m)
=-{x^2\over2}
+O\!\left(b_m|x|^3+b_m^2|x|^4\right).
}
\tag{L-105301.5}

The same estimate holds after an `o(1)` complex displacement. The explicit
series for `Phi` is dominated there by its first summand with all four
derivatives, so `Phi` is zero-free in this saddle neighbourhood for large
`m`.

## 3. The two-thirds threshold

Write

\[
\lambda=i s_m z.
\]

Monotonicity of `log m/m` gives, uniformly for `m>=M`,

\[
\boxed{
|\lambda|
\ll
\vartheta_M b_m^{-1/3}.
}
\tag{L-105301.6}

Therefore

\[
b_m|\lambda|^3=O(\vartheta_M^3)=o(1),
\tag{L-105301.7}
\]

and

\[
b_m^2|\lambda|^4
=O(\vartheta_M^4b_m^{2/3})=o(1).
\tag{L-105301.8}

The exponent `2/3` is exactly where the standardized cubic correction becomes
order one under a purely quadratic relative approximation.

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
\tag{L-105301.9}

Before normalization the integrand is the entire function
`u^m Phi(u)e^(izu)`. Shift the `u` contour by

\[
s_m\lambda=i s_m^2z.
\]

Equation (L-105301.6) gives

\[
|s_m\lambda|
\ll\vartheta_Mb_m^{2/3}=o(1).
\tag{L-105301.10}

The connector at zero is exponentially negligible because of `u^m`; the
connector at infinity vanishes through the double-exponential Xi kernel. The
shift remains inside a strip where `Re exp(2u)>0`.

Set `x=y+lambda`. The quadratic terms complete the square:

\[
-{(y+\lambda)^2\over2}+\lambda(y+\lambda)
=-{y^2\over2}+{\lambda^2\over2}.
\tag{L-105301.11}

Choose `R_m=b_m^(-1/12)`. On `|y|<=R_m`, equations
(L-105301.5)--(L-105301.8) give

\[
F_m(y+\lambda)+\lambda(y+\lambda)
=-{y^2\over2}+{\lambda^2\over2}+o(1)
\tag{L-105301.12}
\]

uniformly. On `|y|>R_m` inside the saddle neighbourhood, strict complex saddle
concavity gives `exp(-cR_m^2)` domination. Outside it, the left `u^m` loss and
right double-exponential loss from the parent saddle theorem remain uniform
under the displacement (L-105301.10).

Hence

\[
\int e^{F_m(x)+\lambda x}\,dx
=e^{\lambda^2/2}\sqrt{2\pi}(1+o(1)),
\]

whereas the denominator is `sqrt(2pi)(1+o(1))`. This proves the relative
formula (L-105301.2).

## 5. Derivatives

Apply the argument with `2 vartheta_M` on a slightly larger complex box.
Cauchy's formula gives every fixed `lambda` derivative. Combining with the
exact factor `exp(iw_mz)` and `lambda=i s_mz` proves (L-105301.3).

## 6. Height/order consequence

Since

\[
T_M^{\rm md}
={M^{2/3}\over(\log M)^{3/4}},
\tag{L-105301.13}
\]

a rectangle of original height `T` lies in this box once

\[
\boxed{
M\ge K T^{3/2}(\log(2+T))^{9/8}
}
\tag{L-105301.14}

for a sufficiently large `K=K(H)`. More generally, an arbitrarily slowly
decreasing `vartheta_M` gives entry order `T^(3/2+o(1))`.

## 7. Scope

This is a relative complex saddle theorem, not an additive central limit
statement. It does not cover the order-one cubic Edgeworth boundary or heights
comparable with `m/log m`. It does not descend a high-derivative box to Xi and
does not prove RH.
