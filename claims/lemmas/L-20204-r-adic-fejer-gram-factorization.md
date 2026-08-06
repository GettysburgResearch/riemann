# L-20204 — `r`-adic Fejér–Gram factorization

Claim ID: `L-20204`  
Title: Every integer-dilation defect is an exact finite portfolio of four-tap screw squares  
Status: `PROPOSED — COMPLETE ALGEBRAIC IDENTITY`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: the screw normalization of `T-20201`; elementary Fejér/variance algebra  
Scope: every integer `r>=2` and every real scale `t`

## 1. Spectral polynomial

Put `z=e^(-ix)` and

\[
 S_r(z)=1+z+\cdots+z^{r-1}.
\]

Since

\[
 1-z^r=(1-z)S_r(z),
\]

one has

\[
\begin{aligned}
&r^2(1-\cos x)-(1-\cos rx)\\
&\qquad={1\over2}|1-z|^2
 \left(r^2-|S_r(z)|^2\right).
\end{aligned}
\tag{1}
\]

For `r` unit complex numbers `1,z,...,z^(r-1)`, the elementary variance identity
is

\[
\boxed{
 r^2-|S_r(z)|^2
 =\sum_{0\le j<k\le r-1}|z^j-z^k|^2.}
\tag{2}
\]

Combining (1) and (2) gives

\[
\boxed{
 r^2(1-\cos x)-(1-\cos rx)
 ={1\over2}
 \sum_{0\le j<k\le r-1}
 |(1-z)(z^j-z^k)|^2.}
\tag{3}
\]

This proves the trigonometric nonnegativity without an inequality estimate.

## 2. Explicit four-tap vectors

For every pair `0<=j<k<=r-1`, define a vector in `C^(r+1)` by

\[
 a^{(j,k)}=e_j-e_{j+1}-e_k+e_{k+1}.
\tag{4}
\]

Coincident coordinates are combined when `k=j+1`; the vector is still exact and
has coefficient sum zero. Its Fourier polynomial is

\[
 A_{j,k}(z)=(1-z)(z^j-z^k).
\tag{5}
\]

Thus (3) is a finite Fejér–Riesz portfolio, with no irrational factorization and
no numerical spectral decomposition.

## 3. Exact screw-form identity

For a zero-sum finite vector `a=(a_0,...,a_m)`, define its screw quadratic by

\[
 Q_{a,t}
 =-{1\over2}\sum_{p,q=0}^m
 a_p\overline{a_q}\,
 \Psi((p-q)t).
\tag{6}
\]

Under RH, the zero expansion gives

\[
 Q_{a,t}
 =\sum_{\gamma>0}{m_\gamma\over\gamma^2}
 |A(e^{-i\gamma t})|^2.
\tag{7}
\]

Apply (7) to the vectors in (4). Equation (3) yields

\[
\boxed{
 \mathcal D_r(t)
 =\sum_{0\le j<k\le r-1}Q_{a^{(j,k)},t}.}
\tag{8}
\]

Indeed, each zero contributes

\[
 {2m_\gamma\over\gamma^2}
 \left[r^2(1-\cos\gamma t)-(1-\cos r\gamma t)\right],
\]

which is exactly the sum of the squares in (3) divided by `gamma^2`.

Equation (8) is an identity of the screw kernel itself, not merely an RH-side
formal calculation; the RH assumption is needed only to interpret the common
quadratic as a positive zero sum.

## 4. Proof-producing consequence

The direct formula

\[
 r^2\Psi(t)-\Psi(rt)
\]

subtracts two large scalar values. Equation (8) permits a cancellation-resistant
producer:

1. form the exact positive Gram portfolio
   \[
   W_r=\sum_{j<k}a^{(j,k)}(a^{(j,k)})^*;
   \]
2. aggregate its autocorrelation coefficients exactly;
3. contract each prime, pole, and archimedean primitive once against that
   aggregate;
4. widen only after the shared-feature cancellation.

This is the same dependence-preserving principle used by the Toeplitz Gram
portfolio work: separately enclosing each four-tap value and then summing may be
much wider than contracting the aggregate portfolio.

## 5. Connection to complete finite search hierarchies

`T-14201` gives a countable complete dyadic FIR hierarchy. The present theorem
shows that every global `r`-adic scalar criterion already lies inside a finite
explicit FIR/Gram packet of that hierarchy. The difference is quantifier
organization:

- the complete hierarchy varies arbitrary vectors at every mesh;
- `T-20203` fixes one canonical portfolio for each integer dilation and proves
  that its cofinal scalar sign alone is RH-equivalent.

Thus the global criterion does not require a new operator normalization. It
selects a canonical renormalization direction from the existing complete screw
geometry.

## 6. Positive mixtures

For coefficients `c_r>0`,

\[
 \sum_r c_r\mathcal D_r(t)
\]

is the positive Gram portfolio obtained by weighting every vector (4) by `c_r`.
Therefore the positive-mixture pole-descent theorem in `T-20203` has an explicit
finite screw-vector realization at every scale.

## 7. Proof boundary

- The Fejér/variance identity and the vector portfolio are exact.
- This does not prove any cofinal sign; it supplies a stable representation of
  the RH-equivalent scalar.
- A production checker must preserve shared autocorrelation dependence rather
  than independently widening the component quadratics.
- Independent review should verify the factor `1/2` in the screw convention and
  its compatibility with the imported Nakamura–Suzuki normalization.