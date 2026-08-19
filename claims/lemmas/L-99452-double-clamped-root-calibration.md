# L-99452 — Double clamping and the coboundary leave only a bounded root calibration

Claim ID: `L-99452`  
Status: **PROVED ON THE FROZEN CANONICAL FRAME INPUTS**  
Created: 2026-08-20  
Depends on: PR #645 double-clamping, PR #648 first-order calibration and
`L-99450`  
RH status: **not assumed**

## 1. The canonical continuum seed has no singular Volterra debt

For \(0<u\le1\), put

\[
F(u)=4(1-\sqrt u)+2\sqrt u\log u
\]

and extend it by zero for \(u>1\). Then

\[
F(1)=0,
\qquad
F'(1-)=0.
\]

Hence every colour

\[
\frac{\mu(k)}kF(k\theta)\mathbf1_{\theta\le1/k}
\]

enters with zero value and zero first derivative at
\(\theta=1/k\). The complete canonical seed is \(C^1\) across every activation
knot. Every distributional derivative-jump atom is therefore exactly zero.

At \(\theta=1\), the seed and its first derivative also vanish. The two
homogeneous Volterra coefficients in
\(\operatorname{span}\{\sqrt\theta,\theta\}\) are exactly zero.

Thus the generic rank-two/two-anchor firewall remains valid for arbitrary
data, but its singular and homogeneous terms are not live for the canonical
continuum seed.

## 2. Primitive calibration after the RN repair

Let

\[
E=P+A
\]

be the exact/native versus positive-frame split on the common typed source of
`L-99450`.

For the canonical continuum contribution, \(A\) has no knot atoms and no
homogeneous modes. The remaining root calibration consists of:

1. the retained-cell finite/continuum discrepancy;
2. the explicit finite anchored low-endpoint block;
3. source-owned finite omissions retained by the exact registry.

For fixed row \(j\), the retained-cell term satisfies

\[
\left|\mathcal R E_X^I(j)\right|
<
\frac{38\sqrt{67}}{j(j-1)\sqrt X}.
\tag{L-99452.1}
\]

The anchored and omission ledgers involve finitely many compact endpoint types.
Their row observations are uniformly bounded on the frozen source registry.
Therefore, for some \(B_j<\infty\),

\[
\boxed{|A_X(j)|\le B_j}
\tag{L-99452.2}
\]

uniformly in \(X\).

## 3. No descendant accumulation

By `L-99450`, the local signed term is the coboundary

\[
A-A\mathsf T.
\]

Hence

\[
(A-A\mathsf T)(I-\mathsf T)^{-1}=A.
\]

All descendant calibration cancels. The bounded quantity in (L-99452.2) is
the root potential itself, not a per-generation estimate and not a geometric
series.

## 4. Mellin consequence

For every \(X_0>1\),

\[
\mathcal A_j(s)
=
\int_{X_0}^\infty A_X(j)X^{-s-1}\,dX
\]

converges absolutely and locally uniformly for \(\Re s>0\). Therefore

\[
\boxed{
\mathcal A_j(s)\text{ is holomorphic throughout }\Re s>0.
}
\]

The only root-ledger item still requiring independent source reconstruction is
the finite anchored/omission registry. Positivity of those terms is neither
assumed nor needed; their boundedness and exact ownership are the relevant
conditions.
