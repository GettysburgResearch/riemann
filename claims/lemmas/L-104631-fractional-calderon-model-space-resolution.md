# L-104631 — Fractional Calderón resolution of a finite canonical defect

Claim ID: `L-104631`  
Status: **PROVED EXACT FINITE HILBERT-SPACE THEOREM**  
Created: 2026-08-27  
Depends on: `L-105625`, `L-105642`, `L-104630`  
RH status: **not assumed**

Work in the Paley--Wiener frequency space `L^2(0,infinity)`. Let `A,B` be
finite upper-half-plane inner functions and put

\[
Q_{A,B}=P_{K_B}(I-P_{K_A})P_{K_B}\succeq0.
\]

Its trace is the exact oriented canonical-correlation defect

\[
\mathfrak C(A,B)=\operatorname{tr}Q_{A,B}.
\tag{L-104631.1}
\]

Fix `a>0`. For `H>0` define the positive multiplier

\[
W_{a,H}
={H^{a-1}\over\Gamma(a)}M_{\xi^ae^{-H\xi}}.
\tag{L-104631.2}
\]

## 1. Exact continuous identity resolution

For every `xi>0`,

\[
{1\over\Gamma(a)}\int_0^\infty H^{a-1}\xi^ae^{-H\xi}\,dH=1.
\]

Hence, strongly on `L^2(0,infinity)`,

\[
\boxed{\int_0^\infty W_{a,H}\,dH=I.}
\tag{L-104631.3}
\]

Because `Q_(A,B)` has finite rank, Tonelli and trace cyclicity give

\[
\boxed{
\mathfrak C(A,B)
=\int_0^\infty\operatorname{tr}(Q_{A,B}W_{a,H})\,dH.
}
\tag{L-104631.4}
\]

Every integrand is nonnegative.

## 2. Exact source-scale law for one zero

For a normalized model vector

\[
\phi_b(\xi)=\sqrt{2y}\,e^{-y\xi}e^{-ix\xi},
\qquad b=x+iy,
\]

the scale density is

\[
\boxed{
w_{y,a}(H)
=\langle W_{a,H}\phi_b,\phi_b\rangle
={2ay\,H^{a-1}\over(H+2y)^{a+1}}.
}
\tag{L-104631.5}
\]

It has total mass one and exact distribution function

\[
\boxed{
\int_0^{H_0}w_{y,a}(H)\,dH
=\left({H_0\over H_0+2y}\right)^a.
}
\tag{L-104631.6}
\]

Thus the fractional scale is adapted automatically to the physical zero
height `y`. A fixed exponential multiplier cannot recover degree as
y decreases to zero, whereas the full scale integral always assigns mass one.

## 3. Tail bound for a finite inner denominator

Let the zeros of `B` be `b_nu=x_nu+i y_nu`, repeated with multiplicity. The
tail operator

\[
T_{a,H_0}=\int_{H_0}^\infty W_{a,H}\,dH
\]

is multiplication by the decreasing regularized-gamma profile
`Gamma(a,H_0 xi)/Gamma(a)`. Using the orthogonal product decomposition of a
finite model space and the causal contraction theorem `L-105625`,

\[
\boxed{
\operatorname{tr}_{K_B}T_{a,H_0}
\le\sum_\nu\left[1-\left({H_0\over H_0+2y_\nu}\right)^a\right].
}
\tag{L-104631.7}
\]

Since `0 <= Q_(A,B) <= P_(K_B)`, if every `y_nu<=eta`,

\[
\boxed{
\int_{H_0}^\infty\operatorname{tr}(Q_{A,B}W_{a,H})\,dH
\le(\deg B)\left[1-\left({H_0\over H_0+2\eta}\right)^a\right].
}
\tag{L-104631.8}
\]

## 4. Replacement by the actual fifth-current metric

Let

\[
\widetilde W_{a,H}^{(5)}
={H^{a-1}\over\Gamma(a)}M_{\xi^ar_{5,H}(\xi)}.
\tag{L-104631.9}
\]

By `L-104630`, for `0<H<=H_0`,

\[
W_{a,H}\preceq
\exp\!\left({7H_0^2\over3\kappa_0}\right)
\widetilde W_{a,H}^{(5)}.
\]

Combining this with (L-104631.4) and (L-104631.8) proves

\[
\boxed{
\begin{aligned}
\mathfrak C(A,B)
\le{}&
\exp\!\left({7H_0^2\over3\kappa_0}\right)
\int_0^{H_0}\operatorname{tr}
 \left(Q_{A,B}\widetilde W_{a,H}^{(5)}\right)dH\\
&+(\deg B)
\left[1-\left({H_0\over H_0+2\eta}\right)^a\right].
\end{aligned}
}
\tag{L-104631.10}
\]

This is an exact current-weighted replacement of the unweighted shallow
canonical defect. It has no finite sampling bank, no omitted model-space
direction and no frame condition number.

The current-weighted trace remains an arithmetic phase/transport quantity; it
is not bounded here.
