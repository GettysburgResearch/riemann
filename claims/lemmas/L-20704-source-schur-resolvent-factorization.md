# L-20704 — Source-canonical shorting is one scalar Weyl resolvent

Claim ID: `L-20704`  
Title: The complete prime-side source Schur quotient is the reciprocal of one constrained resolvent form  
Status: `PROVED FINITE ALGEBRA; COFINAL ARITHMETIC SIGN OPEN`  
Authoring agent: `gpt56-03-s`  
Created: 2026-08-01  
Dependencies: `L-20703`; elementary constrained minimization and the Sherman--Morrison formula  
Scope: the exact source-canonical split after all prime-power, polar, and archimedean entries have been assembled jointly  
Related counterexample candidates: none

## 1. Metric source split

Let \(U\) be a finite-dimensional real or complex Hilbert space with positive
metric \(G\). Let

\[
 \ell:U\to\mathbb C
\]

be a nonzero source functional and let

\[
 q=G^{-1}\ell^*,
 \qquad
 g=\ell q=\ell G^{-1}\ell^*>0.
\tag{L-20704.1}
\]

Then

\[
 W=\ker\ell=q^{\perp_G}
\tag{L-20704.2}
\]

and every vector satisfying \(\ell x=g\) is uniquely of the form \(q+w\),
with \(w\in W\).

Let \(A=A^*\) be the **complete** finite D-0001 operator in this metric. No
prime, polar, or archimedean component is separated below. Assume

\[
 A|_W\succ0.
\tag{L-20704.3}
\]

Define the source shorting scalar

\[
 \boxed{
 S(A;\ell,G)
 =\inf_{w\in W}\langle A(q+w),q+w\rangle .
 }
\tag{L-20704.4}
\]

In block coordinates \(q\oplus W\), this is exactly

\[
 S=A_{qq}-A_{qW}A_{WW}^{-1}A_{Wq}.
\tag{L-20704.5}
\]

The normalized source quotient used by `X-18506` is

\[
 s(A;\ell,G)=\frac{S(A;\ell,G)}{g}.
\tag{L-20704.6}
\]

For the unnormalised even D-0001 packet,

\[
 G=\operatorname{diag}(1,2,\ldots,2),
 \qquad
 \ell(x)=x_0+2\sum_{n=1}^Nx_n,
\]

so \(q=(1,\ldots,1)^T\) and \(g=1+2N\).

## 2. Exact resolvent identity

Assume additionally that \(A\) is invertible and put

\[
 \boxed{
 m_A(0)=\ell A^{-1}\ell^*.
 }
\tag{L-20704.7}
\]

Then

\[
 \boxed{
 S(A;\ell,G)=\frac{g^2}{m_A(0)},
 \qquad
 s(A;\ell,G)=\frac{g}{m_A(0)}.
 }
\tag{L-20704.8}
\]

### Proof

Minimize \(\langle Ax,x\rangle\) under the affine constraint \(\ell x=g\).
The Euler--Lagrange equation is

\[
 Ax=\lambda\ell^*.
\]

Hence \(x=\lambda A^{-1}\ell^*\), and the constraint gives

\[
 \lambda={g\over \ell A^{-1}\ell^*}={g\over m_A(0)}.
\]

Substitution yields

\[
 \langle Ax,x\rangle
 =\lambda\ell x
 ={g^2\over m_A(0)}.
\]

Because \(A|_W\succ0\), the constrained stationary point is the unique global
minimum. QED.

The same identity follows from the inverse of a two-by-two block matrix. In
particular, once \(A_{WW}\succ0\), the inertia formula gives

\[
 \boxed{
 \operatorname{ind}_-(A)=
 \begin{cases}
 0,&S>0,\\
 1,&S<0.
 \end{cases}}
\tag{L-20704.9}
\]

At \(S=0\), the full matrix is singular. Thus the complete source scalar, not
frame conditioning, carries the remaining sign.

## 3. Spectral parameter and Herglotz form

For real \(z\) below the spectrum of \(A|_W\), define

\[
 m_A(z)=\ell(A-zG)^{-1}\ell^*.
\tag{L-20704.10}
\]

The source Schur function is

\[
 \boxed{
 S_A(z)
 =g^2/m_A(z).
 }
\tag{L-20704.11}
\]

After the usual sign convention, \(m_A\) is a scalar Nevanlinna--Herglotz
resolvent. The zeros of \(S_A\) are the eigenvalues of the full block that are
not eigenvalues of the constrained block. This is the finite source-canonical
version of the scalar Weyl/Krein reduction in the localized Weil literature.

## 4. Exact pole rank-one factorization

Suppose the even operator is written in the inherited normalization as

\[
 A=B+\tau cc^*,
 \qquad \tau>0,
\tag{L-20704.12}
\]

where \(B\) contains the complete pole-free archimedean-plus-prime-power block
and \(\tau cc^*\) is the positive even pole channel. If \(B\) is invertible and

\[
 1+\tau c^*B^{-1}c\ne0,
\]

then Sherman--Morrison gives

\[
 \boxed{
 m_A(0)
 =m_B(0)
 -{\tau\,|\ell B^{-1}c|^2
    \over 1+\tau c^*B^{-1}c}.
 }
\tag{L-20704.13}
\]

Therefore the entire polar--archimedean--prime cancellation is represented by
one scalar subtraction. This formula is exact; estimating the three channels
separately can lose every meaningful digit.

## 5. Determinant form

In any basis whose first coordinate is \(q\) and whose remaining columns span
\(W\),

\[
 \boxed{
 S={\det A_{q\oplus W}\over\det A_{WW}}.
 }
\tag{L-20704.14}
\]

This is `L-20703.6` in source coordinates. It supplies two independent directed
consumers:

1. a block-LDL shorting computation;
2. a determinant or scalar-resolvent computation.

A production proof should require their intervals to overlap.

## 6. Cofinal consequence and exact boundary

For an explicit schedule \((N_j,c_j)\), assume

\[
 A_{WW,j}\succ0.
\]

Then the requested lower theorem is exactly a scalar statement about
\(m_{A_j}(0)\):

\[
 {g_j\over m_{A_j}(0)}\ge-\varepsilon_j.
\tag{L-20704.15}
\]

When the quotient is negative, (L-20704.9) shows that the full finite operator
already has one negative direction. Under a complete cofinal hierarchy, a
uniformly negative limit is the off-line-zero alternative.

Consequently:

- structured Cauchy inversion can certify \(A_{WW,j}\) and evaluate
  \(m_{A_j}(0)\) stably;
- support selection can search for favorable finite levels;
- neither operation changes the sign in (L-20704.15);
- proving the required cofinal sign is a genuine arithmetic Weyl-function
  inequality, not another conditioning lemma.

No RH conclusion is claimed in this lemma.
