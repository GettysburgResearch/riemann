# L-105413 — The explicit Xi kernel gives uniform global dominance on the moving-saddle ray

Claim ID: `L-105413`  
Status: **PROPOSED COMPLETE ANALYTIC PROOF — INDEPENDENT HOSTILE REVIEW REQUIRED**  
Created: 2026-08-24  
Depends on: `L-105321`, `M-105331`, the explicit positive Xi Fourier kernel  
RH status: **not assumed**

## 1. Purpose

`M-105331` isolated the missing statement in the moving-saddle programme: local existence of the saddle did not prove that the rest of the translated contour was exponentially smaller. This lemma proves the required global comparison from the first theta orbit of the explicit Xi kernel.

Write

\[
\Phi(u)=\sum_{n\ge1}
\pi n^2 e^{5u/2}
(2\pi n^2e^{2u}-3)e^{-\pi n^2e^{2u}}
\tag{L-105413.1}
\]

in the strip `|Im u|<pi/4`, and

\[
S_m(u)=m\log u+\log\Phi(u)
\tag{L-105413.2}
\]

near the positive real saddle `w_m`.

## 2. Uniform first-orbit dominance

Fix a sufficiently small

\[
0<\delta_0<\pi/16.
\]

There is `U_0` such that, uniformly for

\[
\Re u\ge U_0,
\qquad
|\Im u|\le2\delta_0,
\]

the first orbit

\[
\phi_1(u)
=
\pi e^{5u/2}(2\pi e^{2u}-3)e^{-\pi e^{2u}}
\tag{L-105413.3}
\]

is nonzero and, for every fixed `j`,

\[
\boxed{
\partial_u^j
\left({\Phi(u)\over\phi_1(u)}-1\right)
=
O_j\!\left(e^{-c e^{2\Re u}}\right).
}
\tag{L-105413.4}
\]

Indeed the `n`th summand divided by the first is a polynomial in `n` and `e^u` times

\[
\exp\{-\pi(n^2-1)e^{2\Re u}\cos(2\Im u)\},
\]

and `cos(2 Im u)` is bounded below.

Put

\[
x(u)=2\pi e^{2u}.
\]

A direct differentiation gives

\[
\boxed{
(\log\phi_1)''(u)
=
-2x(u)-{12x(u)\over(x(u)-3)^2}.
}
\tag{L-105413.5}
\]

After enlarging `U_0`, (L-105413.4)--(L-105413.5) imply

\[
\boxed{
\Re(\log\Phi)''(u)
\le-c_1e^{2\Re u}.
}
\tag{L-105413.6}
\]

## 3. The exact translated ray

Let `u_(m,z)` solve

\[
S_m'(u_{m,z})+iz=0,
\]

and put

\[
\delta_{m,z}=u_{m,z}-w_m.
\tag{L-105413.7}
\]

For one sufficiently small fixed `c_0`, uniformly for `m>=M` and

\[
|\Re z|\le c_0{M\over\log M},
\qquad
|\Im z|\le H,
\tag{L-105413.8}
\]

the local implicit-function argument gives

\[
|\delta_{m,z}|\le\delta_0.
\tag{L-105413.9}
\]

The correct translated contour is

\[
\delta_{m,z}+[0,\infty).
\]

Parametrize it by `u=t+delta_(m,z)`. The saddle occurs at the real parameter `t=w_m`.

Define the real action on this ray:

\[
A_{m,z}(t)
=
\Re\{S_m(t+\delta_{m,z})+iz(t+\delta_{m,z})\}.
\tag{L-105413.10}
\]

The exact saddle equation gives

\[
A_{m,z}'(w_m)=0.
\tag{L-105413.11}
\]

The linear Fourier factor does not enter the second derivative. For `t>=U_0`, (L-105413.6) and

\[
\Re{1\over(t+\delta)^2}
\ge {c\over t^2}
\]

give

\[
\boxed{
A_{m,z}''(t)
=
\Re S_m''(t+\delta_{m,z})
\le
-c_2\left({m\over t^2}+e^{2t}\right)<0.
}
\tag{L-105413.12}
\]

Thus the real action is strictly concave on the complete large part of the shifted ray and has its unique maximum there at `t=w_m`.

## 4. Quantitative global loss

On `|t-w_m|<=1`, the real-saddle equation and `e^(2w_m) asymp m/w_m` give

\[
A_{m,z}''(t)\le-c_3\kappa_m,
\qquad
\kappa_m=-S_m''(w_m).
\tag{L-105413.13}
\]

Choose

\[
L_M=\kappa_M^{1/20},
\qquad
r_m={L_M\over\sqrt{\kappa_m}}.
\tag{L-105413.14}
\]

Strict concavity, first on the unit saddle neighbourhood and then on `[U_0,infinity)`, gives

\[
\boxed{
\sup_{\substack{t\ge U_0\\|t-w_m|\ge r_m}}
\left[A_{m,z}(t)-A_{m,z}(w_m)\right]
\le-c_4L_M^2.
}
\tag{L-105413.15}
\]

For `0<=t<=U_0`, the factor `|t+delta|^m` is bounded by `(U_0+delta_0)^m`, whereas the saddle contains `w_m^m`. The fixed vertical tilt contributes only `O_H(w_m)`. Hence

\[
\boxed{
\sup_{0\le t\le U_0}
[A_{m,z}(t)-A_{m,z}(w_m)]
\le-c_5m\log w_m.
}
\tag{L-105413.16}
\]

Equations (L-105413.15)--(L-105413.16) prove the missing global dominance inequality of `M-105331`.

## 5. Connector estimates

The integrand `u^m Phi(u)e^(izu)` is analytic in the strip used by the translation.

- On the connector from `0` to `delta_(m,z)`, `|u|<=delta_0`; its contribution is `exp(-c m log w_m)` relative to the saddle.
- On the connector at real part `R`, the factor `exp[-pi e^(2R) cos(2 Im u)]` dominates every power and the fixed vertical Fourier growth, so the connector tends to zero uniformly.

Therefore the real ray may be translated to the exact moving-saddle ray with an exponentially negligible relative error.

## 6. Scope

This lemma supplies a complete proof of global shifted-ray dominance and the connectors, subject to hostile review of the strip constants and first-orbit estimates. It does not by itself perform the central complex Gaussian integral, transfer `z` derivatives, or prove the phase-cell theorem. Those steps are completed in `L-105414` and `L-105415`. No low-order descent or RH conclusion is claimed.
