# L-105522 — Accretive resolvent anchor and negative-trace absorption

Claim ID: `L-105522`  
Status: **PROVED EXACT, OPERATOR/FINITE-INERTIA THEOREM**  
Created: 2026-08-24  
RH status: **not assumed**

## 1. Accretive resolvent identity

Let \(X\) be a strict contraction on a Hilbert space and put

\[
R=(I-X)^{-1}.
\]

Then

\[
\boxed{
R+R^*-I
=
(I-X^*)^{-1}(I-X^*X)(I-X)^{-1}\succeq0.
}
\tag{L-105522.1}
\]

Equivalently,

\[
R+R^*
=
(I-X^*)^{-1}(2I-X-X^*)(I-X)^{-1}\succeq I.
\tag{L-105522.2}
\]

For every bounded source coordinate \(P\),

\[
\boxed{
P^*(R+R^*)P\succeq P^*P.
}
\tag{L-105522.3}
\]

If \(P\) is invertible and \(\|P^{-1}\|\le c^{-1}\), then the right side is at
least \(c^2I\).

This is a safe-line source theorem.  It does not say that the complete Xi
residue matrix is positive; the contour-transfer remainder contains the
conclusion-bearing information.

## 2. Negative-trace absorption

Let \(G\) be positive definite on a \(d\)-dimensional space and suppose

\[
B\succeq\kappa G,\qquad C=B+E,
\qquad \kappa>0.
\]

Put

\[
\widetilde E=G^{-1/2}EG^{-1/2}.
\]

If \(W\) is the nonpositive spectral subspace of
\(G^{-1/2}CG^{-1/2}\), then for an orthonormal basis \(w_1,\ldots,w_r\) of
\(W\),

\[
0\ge\sum_{j=1}^r
\langle G^{-1/2}CG^{-1/2}w_j,w_j\rangle
\ge r\kappa-\operatorname{tr}(\widetilde E_-).
\]

Hence

\[
\boxed{
\nu_{\le0}(C)
\le
\frac{\operatorname{tr}(\widetilde E_-)}{\kappa}.
}
\tag{L-105522.4}
\]

In particular, if

\[
\operatorname{tr}(\widetilde E_-)
<
\frac{\kappa d}{20},
\]

then

\[
\nu_+(C)>\frac{19d}{20}.
\tag{L-105522.5}
\]

Combined with the confluent full-signature identity, an asymptotically
full-dimensional Xi compression satisfying (L-105522.5) gives a critical-line
proportion greater than \(2(19/20)-1=0.9\).

The theorem requires only a **one-sided negative trace** for the transfer
remainder.  It is strictly weaker than a two-sided 99/101 trace and
Hilbert--Schmidt comparison.
