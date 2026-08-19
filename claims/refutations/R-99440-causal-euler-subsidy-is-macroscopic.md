# R-99440 — The causal/Euler subsidy is macroscopic and cannot be a holomorphic calibration

Claim ID: `R-99440`  
Status: **PROVED EXACT/ASYMPTOTIC NO-GO — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-20  
Frozen parent: PR #649 at `433fd3662f7b2e4ba384ce64f196380e88624090`  
RH status: **unproved**

## 1. Exact one-prime discrepancy

Let \(P_Y\) be one nonzero canonical component row at endpoint \(Y\), let
\(P_{Y/p}\) be its same-index child, and put

\[
r=p^{-1/2}.
\]

The literal Möbius Euler update is

\[
E_p(P_Y)=P_Y-rP_{Y/p}.
\tag{R-99440.1}
\]

For one active prime, the positive causal coefficients are

\[
s=1-r,\qquad \lambda=r,\qquad \alpha=r^2.
\]

Therefore the positive current is

\[
P_Y^{\rm cur}=sP_Y+\lambda(P_Y-rP_{Y/p})
=P_Y-r^2P_{Y/p},
\tag{R-99440.2}
\]

and current plus recursive child is \(P_Y\). The exact missing subsidy is

\[
\boxed{
P_Y^{\rm cur}-E_p(P_Y)
=
r(1-r)P_{Y/p}.
}
\tag{R-99440.3}
\]

This persists after the exact Radon–Nikodym child thinning. The RN map repairs
ownership; it does not change the coefficient \(r^2\) into \(r\).

## 2. The subsidy is of order \(\sqrt Y\)

For the canonical row \(Q_Y(j)\), put

\[
C_j=\frac{2}{j(j-1)}.
\]

Its coefficient expansion can be written

\[
Q_Y(j)=C_jH(Y)+F_j(Y),
\]

where

\[
H(Y)=\sum_{m\le Y}m^{-1/2}\log(Y/m)
\]

and \(F_j\) is a fixed finite linear combination of the functions
\(m^{-1/2}\log(Y/m)\). Since the summand in \(H\) is positive and decreasing,
elementary sum–integral comparison gives

\[
H(Y)=4\sqrt Y+O(\log(2Y)).
\]

Hence, for every fixed row,

\[
\boxed{
Q_Y(j)=4C_j\sqrt Y+O_j(\log(2Y)).
}
\tag{R-99440.4}
\]

Substituting \(Y/p\) into (R-99440.3) gives

\[
\boxed{
r(1-r)Q_{Y/p}(j)
=
\frac{4C_j(1-r)}{p}\sqrt Y
+
O_{p,j}(\log(2Y)).
}
\tag{R-99440.5}
\]

For the exact \(5{:}3\) witness

\[
Q_*(Y)=5Q_Y(2)+3Q_Y(3),
\]

one has

\[
C_*=5C_2+3C_3=6,
\]

and therefore

\[
\boxed{
r(1-r)Q_*(Y/p)
=
\frac{24(1-r)}{p}\sqrt Y
+
O_p(\log(2Y)).
}
\tag{R-99440.6}
\]

The discrepancy is not bounded and is not a terminal or compact calibration.

## 3. Mellin obstruction

Let

\[
H_j(z)=\sum_{m\ge j}a_{j,m}m^{-z}
=
C_j\zeta(z)+P_j(z).
\]

The Mellin transform of the subsidy is, initially for \(\Re s>1/2\),

\[
\boxed{
\int_1^\infty
r(1-r)Q_{X/p}(j)X^{-s-1}\,dX
=
r(1-r)p^{-s}
\frac{H_j(s+1/2)}{s^2}.
}
\tag{R-99440.7}
\]

Because \(C_j>0\), the right-hand side has a genuine positive-real pole at

\[
s=\frac12.
\]

Thus the subsidy cannot be inserted into any defect class whose Mellin
transform is required to be holomorphic throughout \(\Re s>0\).

In particular:

```text
the PR #641 bounded fixed-row calibration cannot absorb it;
the PR #648 calibration coboundary can only move it to the root potential;
that root potential then has sqrt(X) growth and a pole at s=1/2.
```

The causal/Euler mismatch is therefore conclusion-bearing rather than
bookkeeping.

## 4. Critical half-order gap

For the \(5{:}3\) row \(W_X\), positive causal current gives at best

\[
W_X-r^2W_{X/p}\ge0.
\]

The Euler/Harnack statement required for the Möbius row is

\[
W_X-rW_{X/p}\ge0.
\]

The missing term is exactly

\[
r(1-r)W_{X/p}.
\]

The remaining problem is therefore a half-order coefficient upgrade
\(p^{-1}\to p^{-1/2}\), not a source-label repair.
