# L-104638 — Mesoscopic carrier variation is negligible in the normalized fifth source

Claim ID: `L-104638`  
Status: **PROVED UNCONDITIONALLY AT SOURCE-MEAN-SQUARE SCOPE**  
Created: 2026-08-27  
Depends on: `L-106612`, `L-106620` at PR #731 head
`433490c133b26bce4163f4edf7ad04aeda9d33e3`; the classical fixed-order
second moment of zeta derivatives  
RH status: **not assumed**

Let

\[
\Xi(t)=A(t)e^{i\vartheta(t)}h(t),
\qquad h(t)=\zeta(1/2+it),
\]

\[
q=A'/A,\qquad \omega=\vartheta',\qquad
\mathscr L=D+q+i\omega.
\]

Partition `[T,2T]` into

\[
J_T=\lceil(\log T)^B\rceil
\]

regular subintervals and freeze `omega` at `omega_j` on the `j`th interval,
as in `L-106620`. Put

\[
\mathscr L_j=D+q+i\omega_j.
\]

Normalize every fifth packet by `(i omega_j)^5` and every first-order
companion by the constant scale `lambda_j=omega_j^(-1)`.

## 1. Exact remainder

With

\[
E_j=i(\omega-\omega_j),
\]

the noncommutative identity

\[
\mathscr L^5-\mathscr L_j^5
=\sum_{r=0}^{4}\mathscr L^{4-r}E_j\mathscr L_j^r
\tag{L-104638.1}
\]

shows that every actual-minus-frozen coefficient contains at least one of

\[
{\omega-\omega_j\over\omega_j},
\qquad
{\omega^{(r)}\over\omega_j^{r+1}}\quad(1\le r\le4).
\tag{L-104638.2}
\]

Stirling and the window geometry give

\[
\left\|{\omega-\omega_j\over\omega_j}\right\|_{L^\infty(I_j)}
\ll(\log T)^{-B-1},
\tag{L-104638.3}
\]

and

\[
{\omega^{(r)}\over\omega_j^{r+1}}
\ll_r T^{-r}(\log T)^{-r-1}.
\tag{L-104638.4}
\]

The `q` connection and its derivatives satisfy the same or stronger
fixed-order Stirling bounds.

## 2. Fixed-order derivative mean square

For every fixed `0<=r<=6`, the approximate functional equation and the
Montgomery--Vaughan Dirichlet-polynomial mean-value theorem give

\[
\boxed{
\int_T^{2T}|\zeta^{(r)}(1/2+it)|^2dt
\ll_r T(\log T)^{2r+1}.
}
\tag{L-104638.5}
\]

After division by `omega_j^r`, every normalized derivative grade therefore
has total mean square `O_r(T log T)`.

Let `P_j^act` and `P_j^fr` denote any of the four normalized channel packets
`C_0,R_0,C_5,R_5` in the actual and frozen carriers. Equations
(L-104638.1)--(L-104638.5), followed by Cauchy--Schwarz over the finite number
of grades, yield

\[
\boxed{
\sum_j\int_{I_j}|P_j^{act}(t)-P_j^{fr}(t)|^2dt
\ll_B T(\log T)^{-2B-1}.
}
\tag{L-104638.6}
\]

Since

\[
N(T,2T)\asymp T\log T,
\]

this is `o(N(T,2T))` for every fixed `B>0`.

The same conclusion holds after insertion of any bounded fractional-current
multiplier from `L-104631` on a compact `H` interval.

## 3. Exact surviving interface

Thus the variable Riemann--Siegel carrier does not consume a positive fraction
of the fifth-endpoint budget at the **source mean-square level**. Combined
with `L-104637`, the principal source packet is transported exactly and its
carrier perturbation is `o(N)`.

This does not prove `SELFKRYLOV104636`: inner factorization and model-space
projection can amplify small boundary/source perturbations near shallow zeros.
The surviving theorem is precisely the source-to-inner-factor promotion for
the literal fractional Grams.
