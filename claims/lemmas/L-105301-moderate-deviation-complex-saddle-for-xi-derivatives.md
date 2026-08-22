# L-105301 — Cubic-corrected Xi saddle law on the two-thirds Fourier scale

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

Define the standardized cubic saddle coefficient

\[
\gamma_m=S_m^{(3)}(w_m)s_m^3.
\tag{L-105301.1}
\]

For every fixed `C,H>0`, put

\[
\boxed{
T_M^{(3)}=C\left({M\over\log M}\right)^{2/3}.
}
\tag{L-105301.2}

Uniformly for

\[
m\ge M,
\qquad
|\Re z|\le T_M^{(3)},
\qquad
|\Im z|\le H,
\]

the one-sided Xi Fourier transform satisfies the relative asymptotic

\[
\boxed{
A_m(z)
=
\exp\!\left(
 iw_mz-{s_m^2z^2\over2}
 +{\gamma_m(i s_mz)^3\over6}
\right)
(1+o_{M\to\infty}(1)).
}
\tag{L-105301.3}

For every fixed `r>=0`, the same statement may be differentiated `r` times,
with error `o(w_m^r)` relative to the displayed nonzero model on a buffered
box.

This reaches a fixed multiple of `(m/log m)^(2/3)`. The cubic term is essential:
at this scale it is order one, so the purely Gaussian formula of the parent
programme is no longer a relative asymptotic.

## 2. Explicit standardized derivatives

Put

\[
b_m=\sqrt{w_m/m}.
\]

The saddle equation and the first-term asymptotic of `Phi` give

\[
\kappa_m=-S_m''(w_m)
={2m\over w_m}(1+O(1/w_m)),
\qquad
s_m={b_m\over\sqrt2}(1+O(1/w_m)).
\tag{L-105301.4}

For every fixed `k>=3`, differentiating the explicit Xi kernel gives

\[
S_m^{(k)}(w_m)
=-{2^{k-1}m\over w_m}(1+O_k(1/w_m)).
\tag{L-105301.5}
\]

Consequently

\[
\boxed{
\gamma_m
=-\sqrt2\,b_m(1+O(1/w_m)),
}
\tag{L-105301.6}
\]

and

\[
S_m^{(4)}(w_m)s_m^4
=-2b_m^2(1+O(1/w_m)).
\tag{L-105301.7}
\]

In particular `gamma_m<0` for all sufficiently large `m`.

## 3. Standardized local expansion

The first Xi summand dominates uniformly with all fixed derivatives in a
complex neighbourhood of `w_m`; hence `Phi` is zero-free there. For
`|s_mx|<=1/2`, complex Taylor expansion gives

\[
\boxed{
S_m(w_m+s_mx)-S_m(w_m)
=-{x^2\over2}+{\gamma_mx^3\over6}
+O\!\left(b_m^2|x|^4ight).
}
\tag{L-105301.8}

Write

\[
\lambda=i s_mz.
\]

At height (L-105301.2), monotonicity of `log m/m` gives

\[
|\lambda|\ll_C b_m^{-1/3}.
\tag{L-105301.9}
\]

Thus

\[
\gamma_m\lambda^3=O_C(1),
\qquad
b_m^2\lambda^4=O_C(b_m^{2/3})=o(1).
\tag{L-105301.10}
\]

## 4. Contour shift

In standardized coordinates,

\[
A_m(z)
=e^{iw_mz}
{\displaystyle
 \int e^{F_m(x)+\lambda x}\,dx
 \over\displaystyle
 \int e^{F_m(x)}\,dx},
\qquad
F_m(x)=S_m(w_m+s_mx)-S_m(w_m),
\tag{L-105301.11}
\]

with the lower endpoint `-w_m/s_m` understood. The unnormalized integrand
`u^mPhi(u)e^(izu)` is entire. Shift the `u` contour by

\[
s_m\lambda=i s_m^2z.
\]

Since `|s_m lambda|=O_C(b_m^(2/3))`, the connector at zero is killed by `u^m`,
the connector at infinity is killed by the double-exponential Xi factor, and
the contour remains in a strip with `Re exp(2u)>0`.

Set `x=y+lambda`. Completing the quadratic square and using
(L-105301.8) gives

\[
\begin{aligned}
F_m(y+\lambda)+\lambda(y+\lambda)
={}&-{y^2\over2}+{\lambda^2\over2}
+{\gamma_m\lambda^3\over6}\\
&+{\gamma_m\lambda^2y\over2}
+{\gamma_m\lambda y^2\over2}
+{\gamma_my^3\over6}
+O(b_m^2|y+\lambda|^4).
\end{aligned}
\tag{L-105301.12}

For Gaussian-size `y`, the three nonconstant cubic terms are respectively
`O_C(b_m^(1/3)|y|)`, `O_C(b_m^(2/3)y^2)`, and `O(b_m|y|^3)`. The quartic
remainder is `o(1)`. On `|y|<=b_m^(-1/12)` all these terms are uniformly
`o(1)`; the complementary local Gaussian tail is exponentially small. The
outer real tails from the parent saddle proof remain exponentially negligible
under the `O(b_m^(2/3))` contour displacement.

Therefore

\[
\int e^{F_m(x)+\lambda x}\,dx
=
\exp\!\left({\lambda^2\over2}+{\gamma_m\lambda^3\over6}\right)
\sqrt{2\pi}(1+o(1)),
\]

and the denominator is `sqrt(2pi)(1+o(1))`. This proves (L-105301.3).

## 5. Derivatives

Run the proof with a slightly larger fixed constant `C_1>C`. The relative
asymptotic then holds on a complex neighbourhood of the closed `C` box.
Cauchy's formula gives every fixed derivative and proves the derivative form
of the theorem.

## 6. Real-axis phase

For real `x`, define

\[
\Theta_m(x)
=w_mx-{\gamma_ms_m^3x^3\over6}.
\tag{L-105301.13}
\]

Because `gamma_m<0`,

\[
\Theta_m'(x)
=w_m-{\gamma_ms_m^3x^2\over2}>0.
\tag{L-105301.14}
\]

Moreover for `z=x+iy` with `|y|<=H`,

\[
\Im\Theta_m(z)
=y\left[
 w_m-{\gamma_ms_m^3\over6}(3x^2-y^2)
\right]
\]

has the sign of `y` for large `m`. Thus the cubic model has no nonreal
sine/cosine preimages in the fixed vertical strip.

## 7. Height/order consequence

A rectangle of original height `T` lies in the two-thirds box once

\[
\boxed{
M\ge K T^{3/2}\log(2+T)
}
\tag{L-105301.15}

for a suitable `K=K(C,H)`. This is the natural inversion of
`T=(M/log M)^(2/3)`.

## 8. Scope

The theorem is a cubic-corrected relative saddle law. It does not cover heights
where the quartic standardized term is order one, nor heights comparable with
`m/log m`. It does not descend a high derivative to Xi and does not prove RH.
