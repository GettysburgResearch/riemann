# L-106650 — The canonical defect splits into numerator values and truncated-Toeplitz nonnormality

Claim ID: `L-106650`  
Status: **PROVED EXACT FOR FINITE INNER FUNCTIONS**  
Created: 2026-08-26  
Depends on: `L-106512`, `L-106630`; finite model-space functional calculus  
RH status: **not assumed**

Let \(A,B\) be finite upper-half-plane inner functions and put

\[
P_A=P_{K_A},
\qquad
P_B=P_{K_B},
\qquad
m=\deg B.
\]

The oriented canonical defect is

\[
\mathfrak C(A,B)
=
\operatorname{tr}\bigl(P_B(I-P_A)\bigr).
\tag{L-106650.1}
\]

This is the exact shallow charge in `T-106630` when \(A\) is the selected
numerator inner subfactor and \(B\) is the shallow denominator factor.

## 1. Compression identity

Let

\[
T_A^{(B)}
=
P_BM_A\big|_{K_B}
\]

be the analytic truncated Toeplitz operator with symbol \(A\) on \(K_B\).
The model space \(K_B\) is invariant under \(M_A^*\), so

\[
\left(T_A^{(B)}\right)^*
=
M_A^*\big|_{K_B}.
\]

Since \(A\) is inner,

\[
M_AM_A^*=P_{AH^2}=I-P_A.
\]

Consequently

\[
\boxed{
\mathfrak C(A,B)
=
\operatorname{tr}\!\left(
T_A^{(B)}\left(T_A^{(B)}\right)^*
\right)
=
\left\|T_A^{(B)}\right\|_{\mathcal S_2}^2.
}
\tag{L-106650.2}
\]

Thus the adverse model-space charge is the Frobenius energy of one explicit
finite compression.

## 2. Eigenvalue inventory

Let \(b_1,\ldots,b_m\) be the zeros of \(B\), counted with multiplicity.
For a simple zero,

\[
M_A^*k_{b_\nu}
=
\overline{A(b_\nu)}\,k_{b_\nu}.
\]

The kernel vectors span \(K_B\), so the eigenvalue multiset of
\(T_A^{(B)}\) is

\[
A(b_1),\ldots,A(b_m).
\tag{L-106650.3}
\]

At a zero of multiplicity \(q\), the derivative-kernel jet gives a triangular
\(q\times q\) block with diagonal value \(A(b)\).  Hence (L-106650.3)
remains valid with multiplicity.

Take a unitary Schur decomposition

\[
T_A^{(B)}=Q(D+N)Q^*,
\]

where

\[
D=\operatorname{diag}(A(b_1),\ldots,A(b_m))
\]

and \(N\) is strictly upper triangular.  Frobenius orthogonality of \(D\) and
\(N\) gives

\[
\boxed{
\mathfrak C(A,B)
=
\sum_{\nu=1}^m|A(b_\nu)|^2
+
\mathfrak N(A,B),
}
\tag{L-106650.4}
\]

where

\[
\boxed{
\mathfrak N(A,B)
=
\left\|T_A^{(B)}\right\|_{\mathcal S_2}^2
-
\sum_{\nu=1}^m|A(b_\nu)|^2
=
\|N\|_{\mathcal S_2}^2
\ge0.
}
\tag{L-106650.5}
\]

The number \(\mathfrak N(A,B)\) is basis independent.  It is the Frobenius
departure from normality of the compressed numerator multiplier.

Therefore

\[
\boxed{
\sum_{B(b)=0}|A(b)|^2
\le
\mathfrak C(A,B),
}
\tag{L-106650.6}
\]

with equality exactly when \(T_A^{(B)}\) is normal.

This reverses the unsafe value-only shortcut: raw numerator values at
denominator zeros are a lower bound for the charge, not an upper bound, unless
one also pays the nonnormality.

## 3. Exact nonorthogonal Cauchy form

Assume first that the denominator zeros are simple.  Let \(E\) synthesize the
normalized kernels \(e_{b_\nu}\), put

\[
G=E^*E,
\qquad
D=\operatorname{diag}
\bigl(A(b_1),\ldots,A(b_m)\bigr).
\]

With the Cauchy-Gram convention of `L-106506/L-106630`, the kernel
eigenvector relation gives

\[
\boxed{
\mathfrak C(A,B)
=
\operatorname{tr}\!\left(G^{-1}D^*GD\right).
}
\tag{L-106650.7}
\]

In particular,

\[
\boxed{
\mathfrak N(A,B)
=
\operatorname{tr}\!\left(G^{-1}D^*GD\right)
-
\operatorname{tr}(D^*D)
\ge0.
}
\tag{L-106650.8}
\]

For a confluent denominator divisor, \(D\) is replaced by the corresponding
triangular jet matrix in the derivative-kernel basis.  Equations
(L-106650.7)--(L-106650.8) persist, while the diagonal eigenvalue inventory in
(L-106650.3)--(L-106650.5) remains unchanged.

## 4. Product calibration

For simple zeros,

\[
|A(b_\nu)|^2
=
\prod_{A(c)=0}
\left|
\frac{b_\nu-c}{b_\nu-\overline c}
\right|^2,
\tag{L-106650.9}
\]

with multiplicities included.  Thus the spectral part of (L-106650.4) is an
explicit product of pseudohyperbolic distances from every shallow denominator
companion zero to the selected numerator divisor.

The exact determinant is

\[
\boxed{
\det\!\left(
T_A^{(B)}\left(T_A^{(B)}\right)^*
\right)
=
\prod_{\nu=1}^m|A(b_\nu)|^2.
}
\tag{L-106650.10}
\]

A small product alone does not control the trace: up to \(m-1\) singular
directions may remain near one.  The trace-bearing information is exactly the
sum in (L-106650.4), including \(\mathfrak N(A,B)\).

## 5. Scope

```text
canonical defect = compressed-inner Frobenius energy      PROVED EXACT
compression eigenvalues = numerator values at poles       PROVED EXACT
defect = value sum + nonnormality departure                PROVED EXACT
value sum alone upper-bounds the defect                    FALSE
nonnormality estimate for the Xi companion packet          OPEN
```
