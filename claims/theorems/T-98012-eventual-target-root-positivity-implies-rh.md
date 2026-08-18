# T-98012 — Eventual positivity of the complete target root implies RH

Claim ID: `T-98012`  
Status: **PROVED COMPLETE CONDITIONAL MELLIN–LANDAU THEOREM**  
Created: 2026-08-18  
Depends on: the completed squarefree owner ledger; classical Landau theorem  
RH status: **the arithmetic sign hypothesis is open**

Define

\[
\mathcal T_X
=\sum_{k\le X}{\mu(k)\over\sqrt k}
\left(4\sqrt{X/k}-3\right).
\tag{T-98012.1}
\]

Then

\[
\boxed{
\mathcal T_X\ge0\ \text{for all sufficiently large real }X
\Longrightarrow
\mathrm{RH}.
}
\tag{T-98012.2}
\]

Call the arithmetic hypothesis in (T-98012.2) **Target Root Positivity** (`TRP67`).

## 1. Exact Mellin transform

For `Re s>1/2`, absolute Fubini and `X=kY` give

\[
\begin{aligned}
\int_1^\infty\mathcal T_X X^{-s-1}\,dX
&=
\left(\sum_{k\ge1}{\mu(k)\over k^{s+1/2}}\right)
\int_1^\infty(4\sqrt Y-3)Y^{-s-1}\,dY\\
&={1\over\zeta(s+1/2)}
\left({4\over s-1/2}-{3\over s}\right).
\end{aligned}
\]

Hence

\[
\boxed{
\int_1^\infty\mathcal T_X X^{-s-1}\,dX
={s+3/2\over s(s-1/2)\zeta(s+1/2)}.
}
\tag{T-98012.3}
\]

At `s=1/2`, the reciprocal zeta zero cancels the displayed factor `s-1/2`; the point is removable. The finite numerator has its only zero at `s=-3/2`.

## 2. Pole survival

Let `rho` be a zeta zero with `Re rho>1/2`, of arbitrary multiplicity. Then

\[
s_\rho=\rho-1/2
\]

lies in `Re s>0`. Neither `s`, `s-1/2`, nor `s+3/2` cancels the reciprocal-zeta pole at `s_rho`. Thus (T-98012.3) has a nonremovable pole there.

For every positive real `s`, `z=s+1/2` is a positive real point greater than `1/2`; zeta has no real zero there. The apparent point `s=1/2` is removable. Therefore the continuation in (T-98012.3) is analytic at every positive real `s`.

## 3. Landau conclusion

Assume `TRP67`. Remove the finite initial interval and set

\[
f(t)=\mathcal T_{e^t}\ge0.
\]

The elementary bound `mathcal T_X=O(sqrt(X)log(2X))` gives a finite Laplace abscissa. Landau's theorem for a nonnegative locally integrable function forces a singularity at a positive real abscissa if that abscissa is positive. Equation (T-98012.3) is analytic at every positive real point, so the abscissa is at most zero.

The Laplace transform is consequently holomorphic throughout `Re s>0`. The pole at `s=rho-1/2` is impossible. Hence zeta has no zero in `Re rho>1/2`; functional-equation symmetry yields RH.

## 4. Relation to the zero-marginal route

By `L-98013`, the upper target sandwich is unconditional for sufficiently large `X`. Thus

\[
\mathrm{TRP67}
\Longrightarrow
\mathrm{ZMTS67}.
\]

Combined with `L-98011`, `TRP67` makes the zero hinge the global Lorenz minimum. But `T-98012` shows that `TRP67` is itself already conclusion-producing. It must therefore be classified as an RH-bearing arithmetic producer, not as a routine auxiliary Hall estimate.

```text
zero-band domination                         PROVED
TRP67 -> ZMTS67                              PROVED
TRP67 Mellin transform                       PROVED EXACT
finite numerator zero-safe                   PROVED
TRP67 -> RH                                  PROVED CONDITIONAL
TRP67 arithmetic sign                        OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVEN
```
