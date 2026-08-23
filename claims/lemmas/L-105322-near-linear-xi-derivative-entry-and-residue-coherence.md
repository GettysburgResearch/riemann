# L-105322 — Near-linear Xi derivative entry and coherent inverse curvature

Claim ID: `L-105322`  
Status: **PROPOSED UNCONDITIONAL ANALYTIC THEOREM — INDEPENDENT HOSTILE REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: `L-105321`; parent reverse-Rolle and residue-coherence identities  
RH status: **not assumed**

## 1. Statement

Let `c_0` be the saddle constant from `L-105321`. Fix

\[
0<c_2<c_1<c_0
\qquad\text{and}\qquad H>0,
\]

and put

\[
T_M=c_1{M\over\log M}.
\tag{L-105322.1}
\]

For all sufficiently large `M`, simultaneously for every integer `m>=M`, all
zeros of

\[
\Xi^{(m)}(z)
\]

in

\[
\boxed{
|\Re z|\le T_M,
\qquad
|\Im z|\le H
}
\tag{L-105322.2}
\]

are real and simple.

Let `Theta_m` be the exact saddle phase of `L-105321.15`. Uniformly for every
`m>=M` and every regular `T<=T_M`,

\[
\boxed{
N_m(T)
={\Theta_m(T)-\Theta_m(-T)\over\pi}+O(1).
}
\tag{L-105322.3}
\]

Moreover,

\[
\boxed{
N_m(T)
={2w_mT\over\pi}+O(c_1T)+O(1),
}
\tag{L-105322.4}
\]

so adjacent high-derivative zero counts have ratio `1+o(1)`.

For every real zero `c` of `Xi^(m+1)` in the buffered box

\[
|c|\le c_2{M\over\log M},
\]

define

\[
\rho_{m,c}={\Xi^{(m)}(c)\over\Xi^{(m+2)}(c)}.
\tag{L-105322.5}
\]

Then

\[
\boxed{
\rho_{m,c}=-w_m^{-2}(1+o(1))<0
}
\tag{L-105322.6}
\]

uniformly over the complete derivative tail and all critical points in the
buffered box. Consequently the residue coherence satisfies

\[
\boxed{
\mathfrak C_{m,M}=1-o(1)
}
\tag{L-105322.7}
\]

uniformly for every `m>=M`.

Equivalently, every original-height rectangle

\[
|\Re z|\le T,
\qquad |\Im z|\le H
\]

is cleared by all derivative orders

\[
\boxed{
m\ge K T\log(2+T)}
}
\tag{L-105322.8}

for a sufficiently large constant `K=K(H,c_1)` and all sufficiently large
`T`.

## 2. Exact saddle model for the reflected Xi derivative

The companion identity is

\[
\Xi^{(m)}(z)
=i^mM_m\left[A_m(z)+(-1)^mA_m(-z)\right].
\tag{L-105322.9}
\]

Write

\[
\mathcal G_m(z)=e^{\Lambda_m(z)},
\]

and use the even envelope and odd phase

\[
E_m(z)={\Lambda_m(z)+\Lambda_m(-z)\over2},
\qquad
\Theta_m(z)={\Lambda_m(z)-\Lambda_m(-z)\over2i}.
\]

The nonvanishing exact-saddle model is

\[
\mathcal X_m(z)
=i^mM_m
\left[\mathcal G_m(z)+(-1)^m\mathcal G_m(-z)\right].
\]

Thus, apart from a nonzero constant,

\[
\boxed{
\mathcal X_m(z)
=
\begin{cases}
2e^{E_m(z)}\cos\Theta_m(z),&m\text{ even},\\
2ie^{E_m(z)}\sin\Theta_m(z),&m\text{ odd}.
\end{cases}
}
\tag{L-105322.10}
\]

`L-105321.16` gives

\[
\Re\Theta_m'(z)\ge w_m/2>0
\tag{L-105322.11}
\]

on a slightly larger box. Hence `Theta_m` is univalent there by the
Noshiro–Warschawski criterion. It is real and strictly increasing on the real
axis, and

\[
\operatorname{sgn}\Im\Theta_m(x+iy)=\operatorname{sgn}y.
\tag{L-105322.12}
\]

Therefore every zero of the model (L-105322.10) in the strip is real and
simple.

## 3. Cellwise Rouché theorem

Let `epsilon_M` be the uniform relative error in `L-105321.8`. Choose

\[
\delta_M\to0,
\qquad
\epsilon_M=o(\delta_M).
\]

For each real model zero `lambda`, use the phase cell

\[
\mathcal D_{m,\lambda}
=\{z:|\Theta_m(z)-\Theta_m(\lambda)|<\delta_M\}.
\tag{L-105322.13}
\]

Univalence makes these cells disjoint. On their boundaries, the sine or cosine
factor has modulus `gg delta_M` relative to the larger exponential. The two
relative errors in `A_m(z)` and `A_m(-z)` are `o(delta_M)`. Rouché therefore
gives exactly one Xi-derivative zero in every complete cell.

On the complement, there are two cases.

1. If `|Im Theta_m(z)|>=delta_M/2`, one of `exp(iTheta_m)` and
   `exp(-iTheta_m)` dominates and the model bracket has a fixed relative lower
   bound.
2. If `|Im Theta_m(z)|<delta_M/2`, exclusion from the phase cells gives a
   `gg delta_M` lower bound for the real sine/cosine factor.

The relative error excludes all additional zeros. Every cell is invariant
under conjugation and contains one zero counted with multiplicity. Since
`Xi^(m)` is real entire, that zero is real and simple.

This proves (L-105322.2).

## 4. Exact phase count

Every real zero corresponds to one crossing of `Theta_m` through the sine or
cosine lattice. Hence

\[
N_m(T)
={\Theta_m(T)-\Theta_m(-T)\over\pi}+O(1).
\]

From `L-105321.14`,

\[
\Theta_m'(x)
={u_{m,x}+u_{m,-x}\over2}+O(1/\kappa_m)
=w_m+O(c_1)+o(1)
\tag{L-105322.14}
\]

uniformly. Integration proves (L-105322.4). The error is `O(T)`, not `O(1)`;
the exact phase formula (L-105322.3) is the normative count.

## 5. Critical-residue calculation from one order

It is unnecessary to compare three independently normalized saddle models.
Use instead

\[
\Xi^{(m+2)}=(\Xi^{(m)})''.
\]

For the scalar model

\[
g(x)=e^{E_m(x)}\chi(\Theta_m(x)),
\]

where `chi` is sine or cosine, put

\[
q={\chi'(\Theta_m)\over\chi(\Theta_m)}.
\]

At a critical point of `g`,

\[
q=-{E_m'\over\Theta_m'}.
\]

Since `dq/dTheta=-(1+q^2)`, exact logarithmic differentiation gives

\[
\boxed{
{g''\over g}
=E_m''-(\Theta_m')^2-(E_m')^2
-{E_m'\Theta_m''\over\Theta_m'}.
}
\tag{L-105322.15}
\]

The exact saddle derivatives imply, uniformly on the buffered box,

\[
\Theta_m'=w_m+O(c_1),
\qquad
E_m'=O(c_1),
\qquad
E_m''=O(1/\kappa_m),
\qquad
\Theta_m''=O(1/\kappa_m).
\tag{L-105322.16}
\]

Therefore

\[
{g''(c)\over g(c)}=-w_m^2(1+o(1)).
\]

The buffered `C^2` approximation in `L-105321.9`, together with critical-point
localization by the preceding Rouché cells, transfers this identity to
`Xi^(m)`, proving (L-105322.6).

Uniform monochromaticity immediately yields (L-105322.7).

## 6. Height/order inversion

The condition

\[
T\le c_1M/\log M
\]

holds for

\[
M=\lceil KT\log(2+T)\rceil
\]

once `K` is sufficiently large. Applying (L-105322.2) with this `M` proves
(L-105322.8).

## 7. Consequence for the reverse-Rolle frontier

The exact cumulative ledger on the parent programme may now take terminal
order

\[
\boxed{r(T)=O(T\log T),}
\tag{L-105322.17}
\]

rather than `O(T^2 log T)` or the cubic-truncation `O(T^(3/2) log T)`. The
remaining coherence/endpoint/winding budget still spans the first
`O(T log T)` derivative levels and is not estimated here.

## 8. Scope

This theorem is conditional only on the proposed analytic contour theorem
`L-105321`; it contains no RH assumption. It is still a high-derivative entry
theorem. It does not cross the first low derivative carrying a wrong extremum,
does not control the Levinson boundary charge, and does not prove RH.
