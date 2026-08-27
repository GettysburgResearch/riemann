# L-105414 — The moving Xi saddle gives a uniform relative asymptotic in a fixed physical strip

Claim ID: `L-105414`  
Status: **PROPOSED COMPLETE ANALYTIC PROOF — INDEPENDENT HOSTILE REVIEW REQUIRED**  
Created: 2026-08-24  
Depends on: `L-105321`, `L-105413`  
RH status: **not assumed**

## 1. Statement

Use

\[
A_m(z)
={1\over M_m}\int_0^\infty u^m\Phi(u)e^{izu}\,du
\]

and the exact moving saddle `u_(m,z)` from `L-105413`. Define

\[
\mathcal G_m(z)
=
\exp\{S_m(u_{m,z})-S_m(w_m)+izu_{m,z}\}
\left({\kappa_m\over-S_m''(u_{m,z})}\right)^{1/2},
\tag{L-105414.1}
\]

with the square-root branch fixed at `z=0`.

There are constants `c_0>0,M_0` such that, for every fixed `H>0`,

\[
\boxed{
A_m(z)=\mathcal G_m(z)
\left(1+O_H(\kappa_M^{-1/3})\right)
}
\tag{L-105414.2}
\]

uniformly for

\[
m\ge M\ge M_0,
\qquad
|\Re z|\le c_0{M\over\log M},
\qquad
|\Im z|\le H.
\tag{L-105414.3}
\]

The model is nonzero.

For every fixed derivative order `q` and every `0<c_1<c_0`,

\[
\boxed{
A_m^{(q)}(z)
=
\mathcal G_m^{(q)}(z)
+
o_H\!\left((1+w_m)^q|\mathcal G_m(z)|\right)
}
\tag{L-105414.4}
\]

uniformly on the box with `c_1`.

## 2. Central integral

Translate the ray as in `L-105413` and write

\[
u=u_{m,z}+v,
\qquad v\in\mathbb R.
\]

The exact saddle equation removes the linear term. Uniformly in a fixed neighbourhood,

\[
S_m(u_{m,z}+v)-S_m(u_{m,z})+izv
=
{S_m''(u_{m,z})v^2\over2}
+
\sum_{j\ge3}{S_m^{(j)}(u_{m,z})v^j\over j!}.
\tag{L-105414.5}
\]

First-orbit dominance gives, for each fixed `j>=3`,

\[
S_m^{(j)}(u_{m,z})=O_j(\kappa_m).
\tag{L-105414.6}
\]

Scale by `v=x/sqrt(kappa_m)` with `x` real. The quadratic coefficient `S_m''(u_(m,z))/kappa_m` stays in a fixed compact subset of the left half-plane, while the standardized `j`th coefficient is `O_j(kappa_m^(1-j/2))`.

On `|x|<=L_M=kappa_M^(1/20)`, the complete nonquadratic exponent is `O(kappa_M^(-7/20))`. Dominated integration against `e^(-c x^2)` and the exact complex Gaussian identity

\[
\int_{\mathbb R}e^{S_m''(u_{m,z})v^2/2}\,dv
=
\sqrt{2\pi\over-S_m''(u_{m,z})}
\]

with the branch continued from `z=0` give

\[
\int_{\rm central}e^{S_m(u)+izu}\,du
=
e^{S_m(u_{m,z})+izu_{m,z}}
\sqrt{2\pi\over-S_m''(u_{m,z})}
\left(1+O(\kappa_M^{-1/3})\right).
\tag{L-105414.7}
\]

The omitted local Gaussian tail is `O(exp(-c L_M^2))`.

## 3. Global complement and normalization

`L-105413.15` pays the whole shifted-ray complement by `exp(-c L_M^2)` relative to the saddle. The compact initial segment and both connectors are still smaller.

At `z=0`, the same calculation gives

\[
M_m
=
e^{S_m(w_m)}
\sqrt{2\pi\over\kappa_m}
\left(1+O(\kappa_m^{-1/3})\right).
\tag{L-105414.8}
\]

Dividing (L-105414.7) by (L-105414.8) proves (L-105414.2).

## 4. Fixed derivative transfer

Apply the relative theorem on a box with one intermediate constant `c_1<c_*<c_0` and one larger fixed vertical height. Around every point of the `c_1` box use a `z` disk of radius

\[
r_z={c\over1+w_m}.
\]

The saddle model changes by only a bounded factor on this disk because

\[
(\log\mathcal G_m)'=iu_{m,z}+O(\kappa_m^{-1}).
\]

Cauchy's formula applied to `A_m/mathcal G_m-1` costs at most `(1+w_m)^q`. Since every fixed power of `w_m` is `o(kappa_M^(1/3))`, (L-105414.4) follows.

## 5. Exact action derivatives

With `Lambda_m=log mathcal G_m`,

\[
\Lambda_m'(z)=iu_{m,z}+O(\kappa_m^{-1}),
\tag{L-105414.9}
\]

and

\[
u_{m,z}'=-{i\over S_m''(u_{m,z})}.
\tag{L-105414.10}
\]

For the reflected even envelope and odd phase

\[
E_m(z)={\Lambda_m(z)+\Lambda_m(-z)\over2},
\qquad
\Theta_m(z)={\Lambda_m(z)-\Lambda_m(-z)\over2i},
\]

one obtains, after reducing `c_0`,

\[
\boxed{
\Re\Theta_m'(z)\ge {w_m\over2}>0
}
\tag{L-105414.11}
\]

throughout every smaller fixed-physical-width box.

## 6. Scope

This theorem resolves the analytic gap identified in `M-105331`, subject to independent review of the explicit concavity constants, complex Gaussian branch and half-infinite-tail uniformity. It does not itself execute the reflected phase-cell count or low-order descent.
