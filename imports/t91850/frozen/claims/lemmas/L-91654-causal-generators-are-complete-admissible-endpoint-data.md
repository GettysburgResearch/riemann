# L-91654 — Causal generators are complete admissible endpoint data

Claim ID: `L-91654`  
Status: **PROVED EXACT ENDPOINT/CAPACITY THEOREM**  
Created: 2026-08-13  
Depends on: `L-91653`, retained `L-91112.25`, `L-90027`  
RH status: **unproved**

Let `p>=67`, `r=p^{-1/2}`, and `u>=p`. Consider the complete causal difference

\[
C_{p,u}=P_u-rU_pP_{u/p}
\]

from `L-91653`.

## Target and declared score

For

\[
T(u)=4\sqrt u-3,
\qquad
S(u)=5\sqrt u-3,
\]

one has

\[
T(u)-rT(u/p)
=4(1-r^2)\sqrt u-3(1-r)>0,
\]

\[
S(u)-rS(u/p)
=5(1-r^2)\sqrt u-3(1-r)>0,
\]

and

\[
[S-rS_{child}]-[T-rT_{child}]
=(1-r^2)\sqrt u>0.
\tag{L-91654.1}
\]

## Component rows

On every activation cell the exact row has

\[
Q_Y(j)=C_{j,N}\log Y-D_{j,N},
\qquad C_{j,N}>0.
\]

The row is continuous at activation knots because an entering logarithmic term
has value zero. Therefore `Q_Y(j)` is globally nondecreasing in `Y`.
Consequently

\[
\boxed{
Q_u(j)-rQ_{u/p}(j)
=[Q_u(j)-Q_{u/p}(j)]+(1-r)Q_{u/p}(j)
\ge0
}
\tag{L-91654.2}
\]

for every `j>=2`.

## Ordinary and radix-four responses

Put

\[
H(Z)=\sum_{k\le Z}k^{-1/2}\log(Z/k),
\]

with value zero for `Z<1`. Double summation gives the exact ordinary response

\[
\Gamma_Y(q)=q^{-1/2}H(Y/q).
\]

The function `H` is nonnegative and nondecreasing. Hence

\[
\Gamma_u(q)-r\Gamma_{u/p}(q)\ge0.
\]

The detail response is

\[
\Xi_Y(q)=q^{-1/2}[H(Y/q)-H(Y/(4q))].
\]

For `D(Z)=H(Z)-H(Z/4)`, on every smooth cell

\[
D'(Z)=Z^{-1}\sum_{Z/4<k\le Z}k^{-1/2}\ge0.
\]

Continuity at activation knots makes `D` globally nonnegative and
nondecreasing. Thus

\[
\boxed{
\Xi_u(q)-r\Xi_{u/p}(q)\ge0
}
\tag{L-91654.3}
\]

for every physical integer column `q>=2`.

The causal generator has zero finite-boundary reserve; all root/collar/common
boundary data are carried by the separate current datum of `L-91655`.

Therefore `C_(p,u)` is admissible in every target, component-row, ordinary, and
radix-four coordinate of `L-91653`. Its literal score deficit is bounded in
`L-91656`.