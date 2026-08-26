# L-106661 — A rational resolvent certificate for the canonical compression defect

Claim ID: `L-106661`  
Status: **PROVED EXACT FINITE-DIMENSIONAL OPERATOR INEQUALITY**  
Created: 2026-08-26  
Depends on: `L-106650`  
RH status: **not assumed**

Let \(T\) be a finite-dimensional contraction and put

\[
K=TT^*,
\qquad
0\preceq K\preceq I,
\qquad
\mathcal C=\operatorname{tr}K.
\]

For \(\tau>0\), define the rational resolvent functional

\[
\boxed{
\mathcal Q_\tau(K)
=
(1+\tau)\operatorname{tr}
\left[K(I+\tau K)^{-1}\right].
}
\tag{L-106661.1}
\]

## 1. Exact positive completion

Scalar functional calculus on \(0\le x\le1\) gives

\[
\frac{(1+\tau)x}{1+\tau x}-x
=
\frac{\tau x(1-x)}{1+\tau x}\ge0.
\]

Therefore

\[
\boxed{
\mathcal C
\le
\mathcal Q_\tau(K),
}
\tag{L-106661.2}
\]

with exact gap

\[
\boxed{
\mathcal Q_\tau(K)-\mathcal C
=
\tau\operatorname{tr}
\left[
K(I-K)(I+\tau K)^{-1}
\right]
\ge0.
}
\tag{L-106661.3}
\]

Equality holds exactly on the \(0/1\) spectral subspace. Moreover,

\[
\lim_{\tau\downarrow0}\mathcal Q_\tau(K)=\mathcal C.
\tag{L-106661.4}
\]

Thus the canonical defect is the decreasing small-\(\tau\) limit of explicit
rational positive certificates.

## 2. Cauchy-Gram coordinates

For the simple denominator packet of `L-106650`, let

\[
G=E^*E\succ0,
\qquad
D=\operatorname{diag}(A(b_1),\ldots,A(b_m)),
\qquad
H=D^*GD.
\]

For a confluent packet, \(D\) is the corresponding triangular jet matrix.
Then

\[
K=G^{-1/2}HG^{-1/2},
\qquad
\mathcal C=\operatorname{tr}(G^{-1}H).
\]

Cyclicity gives the square-root-free formula

\[
\boxed{
\mathcal Q_\tau(G,D)
=
(1+\tau)
\operatorname{tr}
\left[
H(G+\tau H)^{-1}
\right].
}
\tag{L-106661.5}
\]

This expression is invariant under every invertible change of the
denominator kernel basis. It retains the intrinsic Gram inverse but introduces
no frame-condition-number estimate and no explicit nonnormality term.

## 3. Regularized determinant companion

Concavity of \(x\mapsto\log(1+\tau x)\) on \([0,1]\) gives

\[
x\le
\frac{\log(1+\tau x)}{\log(1+\tau)}.
\]

Hence a second scalar certificate is

\[
\boxed{
\mathcal C
\le
\mathcal P_\tau(K)
:=
\frac{\log\det(I+\tau K)}{\log(1+\tau)}.
}
\tag{L-106661.6}
\]

In Cauchy-Gram coordinates,

\[
\boxed{
\mathcal P_\tau(G,D)
=
\frac{
\log\det(G+\tau D^*GD)-\log\det G
}{
\log(1+\tau)
}.
}
\tag{L-106661.7}
\]

Again \(\mathcal P_\tau\to\mathcal C\) as \(\tau\downarrow0\). The determinant
form packages every singular direction into one positive Pick/Gram scalar;
it does not rely on the product of eigenvalues alone.

## 4. Xi specialization

For each mesoscopic shallow packet of `T-106650`, take

\[
T=T_{A_j}^{(B_{-,j}^{\rm sh})}.
\]

Then the complete shallow canonical charge is bounded by either
\(\mathcal Q_{\tau,j}\) or \(\mathcal P_{\tau,j}\), computed from the explicit
confluent Cauchy Gram and numerator value/jet matrix. This is a rational or
regularized-determinant certificate for the exact same operator which
appears in `MESOSCHUR106650`.

## Scope

The lemma does not estimate the Xi matrices. For fixed positive \(\tau\) the
certificates can strictly overpay; allowing \(\tau\downarrow0\) recovers the
canonical defect exactly. The gain is a scalar, basis-invariant attack surface,
not a proof of the required asymptotic.
