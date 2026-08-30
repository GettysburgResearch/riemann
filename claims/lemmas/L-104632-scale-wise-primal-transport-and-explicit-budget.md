# L-104632 — Scale-wise primal transport and the explicit fifth-endpoint budget

Claim ID: `L-104632`  
Status: **PROVED EXACT REDUCTION WITH RATIONAL CONSTANTS**  
Created: 2026-08-27  
Depends on: `L-104631`; `T-106590`, `L-106591`, `L-106630` at PR #731 head
`433490c133b26bce4163f4edf7ad04aeda9d33e3`  
RH status: **not assumed**

## 1. Scale-wise transport identity

Let

\[
M_H=\left(\widetilde W_{a,H}^{(5)}\right)^{1/2}.
\]

For each scale,

\[
\begin{aligned}
\operatorname{tr}
 \left(Q_{A,B}\widetilde W_{a,H}^{(5)}\right)
&=\left\|(I-P_{K_A})P_{K_B}M_H\right\|_{\mathcal S_2}^2\\
&=\inf_{\operatorname{ran}Y\subseteq K_A}
 \left\|P_{K_B}M_H-Y\right\|_{\mathcal S_2}^2.
\end{aligned}
\tag{L-104632.1}
\]

The minimizer is `Y=P_(K_A)P_(K_B)M_H`. Consequently any explicit,
source-defined family `Y_H` gives a rigorous upper bound. Unlike the
unweighted primal formula, the transport may vary with the physical current
scale `H`; the fractional identity has already fixed the coefficient with
which each scale is charged.

Define the complete shallow fractional-current residual by summing the left
side of (L-104632.1) over the mesoscopic endpoint packets:

\[
\mathfrak I_{\rm sh}(T)
=\sum_j\int_0^{H_0}\operatorname{tr}
 \left(Q_{A_j,B_j}\widetilde W_{a,H}^{(5)}\right)dH.
\tag{L-104632.2}
\]

## 2. Exact numerical choices

Use

\[
\kappa_0={20476\over2345},\qquad
\eta={1\over100},\qquad
H_0={1\over20},\qquad
a={1\over1000}.
\tag{L-104632.3}
\]

The current-metric exponent is

\[
\delta_0={7H_0^2\over3\kappa_0}
={3283\over4914240}<{1\over1001}.
\]

Since `e^x <= (1-x)^(-1)` for `0<=x<1`,

\[
\boxed{e^{\delta_0}<{1001\over1000}.}
\tag{L-104632.4}
\]

For a shallow zero `y<=1/100`,

\[
{H_0\over H_0+2y}\ge{5\over7}.
\]

Furthermore

\[
\log{7\over5}<{17\over50},
\]

because the cubic Taylor lower bound for `e^(17/50)` is

\[
1+{17\over50}+{1\over2}\left({17\over50}\right)^2
+{1\over6}\left({17\over50}\right)^3
={1053263\over750000}>{7\over5}.
\]

Therefore

\[
\boxed{1-\left({5\over7}\right)^{1/1000}<{17\over50000}.}
\tag{L-104632.5}
\]

Across one fifth-endpoint window the two denominator companion factors have
total degree at most twice the common zero-count scale. After disjoint
windowing,

\[
\sum_j\deg B_j^{\rm sh}\le2N(T,2T)+o(N).
\tag{L-104632.6}
\]

Equations (L-104631.10) and (L-104632.4)--(L-104632.6) give

\[
\boxed{
{\mathfrak C_{\rm sh}(T)\over N}
\le{1001\over1000}{\mathfrak I_{\rm sh}(T)\over N}
+{17\over25000}+o(1).
}
\tag{L-104632.7}
\]

## 3. Strict 90-percent margin

If

\[
\boxed{
\limsup_{T\to\infty}{\mathfrak I_{\rm sh}(T)\over N(T,2T)}
<{21\over1000},
}
\tag{L-104632.8}
\]

then

\[
\limsup{\mathfrak C_{\rm sh}(T)\over N}
<{1001\over1000}{21\over1000}+{17\over25000}
={21701\over10^6}<{11\over500}.
\tag{L-104632.9}
\]

The already-proved deep charge is `3/40=75000/10^6`. Thus the complete
fifth-endpoint charge is below

\[
{75000+21701\over10^6}={96701\over10^6}<{97\over1000}.
\tag{L-104632.10}
\]

With the pinned unconditional fifth-derivative input
`R_5/N>997/1000-o(1)`,

\[
{R_0\over N}>{997000-96701\over10^6}
={900299\over10^6}>0.9.
\tag{L-104632.11}
\]

The numerical margin is

\[
\boxed{{299\over10^6}.}
\]

The only unproved item in this chain is the Xi estimate (L-104632.8).
