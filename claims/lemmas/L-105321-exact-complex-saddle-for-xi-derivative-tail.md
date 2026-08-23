# L-105321 — Exact moving complex saddle for the Xi derivative tail

Claim ID: `L-105321`  
Status: **PROPOSED UNCONDITIONAL ANALYTIC THEOREM — INDEPENDENT HOSTILE REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: parent `L-105200`; `L-105301`; the explicit positive Xi Fourier kernel  
RH status: **not assumed**

## 1. Setup

Use the classical one-sided Xi Fourier measure

\[
M_m=\int_0^\infty u^m\Phi(u)\,du,
\qquad
d\nu_m(u)=M_m^{-1}u^m\Phi(u)\,du,
\]

and

\[
A_m(z)=\int_0^\infty e^{izu}\,d\nu_m(u).
\tag{L-105321.1}
\]

Put

\[
S_m(u)=m\log u+\log\Phi(u)
\]

in the zero-free neighbourhood of its positive real saddle `w_m`, and define

\[
S_m'(w_m)=0,
\qquad
\kappa_m=-S_m''(w_m)>0.
\tag{L-105321.2}
\]

The real saddle estimates give

\[
w_m={1\over2}\log m+O(\log\log m),
\qquad
\kappa_m={2m\over w_m}\left(1+O(1/w_m)\right).
\tag{L-105321.3}
\]

## 2. Statement

There are absolute constants `c_0>0` and `M_0`, and for every fixed `H>0`
a sequence `epsilon_M(H)->0`, such that the following holds.

Put

\[
T_M=c_0{M\over\log M}.
\tag{L-105321.4}
\]

For every `M>=M_0`, every integer `m>=M`, and every

\[
|\Re z|\le T_M,
\qquad
|\Im z|\le H,
\tag{L-105321.5}
\]

there is a unique saddle `u_(m,z)` in a fixed complex disk about `w_m`
satisfying

\[
\boxed{
S_m'(u_{m,z})+iz=0.
}
\tag{L-105321.6}
\]

Choose the analytic square-root branch equal to one at `z=0` and define

\[
\mathcal G_m(z)
=
\exp\!\left(
 S_m(u_{m,z})-S_m(w_m)+izu_{m,z}
\right)
\left({\kappa_m\over-S_m''(u_{m,z})}\right)^{1/2}.
\tag{L-105321.7}
\]

Then

\[
\boxed{
A_m(z)=\mathcal G_m(z)
\left(1+O(\epsilon_M(H))\right)
}
\tag{L-105321.8}
\]

uniformly in the complete range (L-105321.5). The model never vanishes.

For every fixed integer `r>=0`, on a box with any smaller constant
`0<c_1<c_0`,

\[
\boxed{
A_m^{(r)}(z)
=\mathcal G_m^{(r)}(z)
+o\!\left((1+w_m)^r|\mathcal G_m(z)|\right)
}
\tag{L-105321.9}
\]

uniformly over the same half-infinite derivative tail.

The earlier Gaussian and cubic formulas are the first terms of the Taylor
expansion of the **exact saddle action** (L-105321.7). No finite cumulant
truncation is required at the scale `m/log m`.

## 3. Zero-free complex saddle neighbourhood

For `u` in a fixed strip

\[
\Re u\ge w_m-1,
\qquad
|\Im u|\le\delta<\pi/4,
\]

the `n=1` summand of the explicit Xi kernel is

\[
\pi e^{5u/2}(2\pi e^{2u}-3)e^{-\pi e^{2u}}.
\]

Every `n>=2` summand is smaller by

\[
O\!\left(
 e^{-\pi(n^2-1)e^{2\Re u}\cos(2\Im u)}
\right)
\]

together with all fixed derivatives. The first summand has no zero in this
strip for large `m`. Rouché therefore gives a zero-free fixed complex
neighbourhood of `w_m`, uniformly in `m`. A single analytic branch of
`log Phi` and hence of `S_m` is available there.

The differentiated saddle estimates imply, in that neighbourhood,

\[
-S_m''(u)\asymp\kappa_m,
\qquad
S_m^{(r)}(u)=O_r(\kappa_m)\quad(r\ge3).
\tag{L-105321.10}
\]

Choose `c_0` small enough that `|z|<=2c_0 kappa_m` keeps the Newton map

\[
u\longmapsto u-{S_m'(u)+iz\over S_m''(u)}
\]

inside this disk and makes it a contraction. Since `kappa_m` is eventually
increasing and `T_M<<kappa_m` uniformly for `m>=M`, this proves existence,
uniqueness and analyticity of `u_(m,z)`. Moreover

\[
\boxed{
|u_{m,z}-w_m|\ll {|z|+H\over\kappa_m}\le O(c_0)+o(1).
}
\tag{L-105321.11}
\]

## 4. Contour through the exact saddle

The unnormalized integrand

\[
u^m\Phi(u)e^{izu}
\]

is entire because `m` is an integer and `Phi` is entire. Translate the
positive real ray to the parallel contour through `u_(m,z)`. The short
connector at zero is exponentially small relative to the saddle: on it
`|u|^m=O(1)^m`, whereas

\[
e^{S_m(w_m)}
=\exp\{m\log w_m+O(m/w_m)\}.
\]

The connector at infinity vanishes because the displacement in
(L-105321.11) lies in `|Im u|<delta` and

\[
\Re(e^{2u})\ge e^{2\Re u}\cos(2\delta)>0.
\]

Write `u=u_(m,z)+v` with `v` real on the shifted contour. The saddle equation
removes the linear term. On `|v|<=r_0`,

\[
S_m(u_{m,z}+v)-S_m(u_{m,z})+izv
={S_m''(u_{m,z})v^2\over2}
+O(\kappa_m|v|^3).
\tag{L-105321.12}
\]

After the scaling

\[
v={y\over\sqrt{-S_m''(u_{m,z})}},
\]

every standardized derivative of order at least three is
`O_r(kappa_m^(1-r/2))=o(1)`. Hence the central integral is

\[
\sqrt{2\pi\over-S_m''(u_{m,z})}
\left(1+o(1)\right)
\tag{L-105321.13}
\]

uniformly.

For `r_0>=|v|>=kappa_m^(-2/5)`, the real part of the quadratic term is at most
`-c kappa_m v^2`; this pays the local complement. Outside the fixed saddle
neighbourhood, the real-saddle inequalities remain strict under the small
complex displacement: the left side loses through `u^m`, and the right side
through `exp(-pi exp(2u))`. Both tails are exponentially smaller than the
complex saddle contribution, even when the latter contains the moderate
factor `exp(-O(c_0^2 kappa_m))`, provided `c_0` was fixed sufficiently small.

Dividing by the ordinary real-saddle asymptotic for `M_m` proves
(L-105321.8).

## 5. Derivative control

Repeat the theorem with a constant strictly between `c_1` and `c_0`. Every
point of the smaller box then has a complex neighbourhood whose radius is a
fixed positive fraction of `kappa_m`. The relative approximation and its
nonvanishing model hold there. Cauchy's formula gives (L-105321.9).

## 6. Action derivatives and the exact phase

Put

\[
\Lambda_m(z)=\log\mathcal G_m(z)
\]

with the branch fixed by `Lambda_m(0)=0`. The envelope theorem and the
curvature prefactor give

\[
\boxed{
\Lambda_m'(z)=iu_{m,z}+O(1/\kappa_m).
}
\tag{L-105321.14}
\]

Define

\[
E_m(z)={\Lambda_m(z)+\Lambda_m(-z)\over2},
\qquad
\Theta_m(z)={\Lambda_m(z)-\Lambda_m(-z)\over2i}.
\tag{L-105321.15}
\]

For real `x`, `E_m(x)` and `Theta_m(x)` are real. From
(L-105321.11)--(L-105321.14), after reducing `c_0` if needed,

\[
\boxed{
\Re\Theta_m'(z)\ge {w_m\over2}>0
}
\tag{L-105321.16}
\]

throughout every fixed smaller box. Thus

\[
\operatorname{sgn}\Im\Theta_m(x+iy)=\operatorname{sgn}y.
\tag{L-105321.17}
\]

This phase monotonicity is the input for `L-105322`.

## 7. Firewalls and scope

- The constant `c_0` is fixed and small. No claim is made up to the first
  complex-saddle collision.
- The count at this scale is governed by the exact phase `Theta_m`, not by
  `w_mx` with an `O(1)` phase error.
- The theorem is a proposed contour theorem; the exact finite replay on this PR
  does not authenticate it.
- It proves no low-order reverse-Rolle budget and no form of RH.

The smallest load-bearing review target is the uniform domination of the
shifted-contour complement relative to the exact complex saddle when
`|Re z|` is a fixed small multiple of `kappa_m`.
