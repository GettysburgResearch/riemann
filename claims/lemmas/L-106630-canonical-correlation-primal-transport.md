# L-106630 — Canonical-correlation defect is an exact primal transport residual

Claim ID: `L-106630`  
Status: **PROVED EXACT FINITE HILBERT-SPACE IDENTITY**  
Created: 2026-08-26  
RH status: **not assumed**

Let \(\mathcal H\) be a Hilbert space and let

\[
E_-:\mathbb C^m\to\mathcal H,
\qquad
E_+:\mathbb C^n\to\mathcal H
\]

have full column rank. Put

\[
G_-=E_-^*E_-,
\qquad
G_+=E_+^*E_+,
\qquad
C=E_-^*E_+ .
\]

Let \(P_-\) and \(P_+\) be the orthogonal projections onto the two column
spaces. The oriented canonical-correlation defect is

\[
\mathfrak C(E_-,E_+)
=\operatorname{tr}\bigl(P_-(I-P_+)\bigr).
\]

## 1. Exact primal formula

For every matrix \(X\in\mathbb C^{n\times m}\), define

\[
\boxed{
\mathcal R(X)
=
\operatorname{tr}\!\left[
G_-^{-1}
\left(
G_- -CX-X^*C^*+X^*G_+X
\right)
\right].
}
\tag{L-106630.1}
\]

Equivalently,

\[
\mathcal R(X)
=
\left\|
(E_- -E_+X)G_-^{-1/2}
\right\|_{\mathcal S_2}^2.
\]

Then

\[
\boxed{
\mathfrak C(E_-,E_+)
=
\inf_X\mathcal R(X).
}
\tag{L-106630.2}
\]

The unique minimizer is

\[
\boxed{
X_*=G_+^{-1}C^*,
}
\tag{L-106630.3}
\]

and the minimum is

\[
\boxed{
\mathfrak C
=
m-\operatorname{tr}
\left(G_-^{-1}CG_+^{-1}C^*\right).
}
\tag{L-106630.4}
\]

## 2. Exact completion of the square

For every \(X\),

\[
\boxed{
\mathcal R(X)
=
\mathfrak C
+
\operatorname{tr}\!\left[
G_-^{-1}
(X-X_*)^*G_+(X-X_*)
\right].
}
\tag{L-106630.5}
\]

Equivalently, with the normal-equation error

\[
Y=G_+X-C^*,
\]

one has

\[
\boxed{
\mathcal R(X)
=
\mathfrak C
+
\operatorname{tr}
\left(
G_-^{-1}Y^*G_+^{-1}Y
\right).
}
\tag{L-106630.6}
\]

Thus any explicit approximate transport matrix gives a rigorous upper bound
for the adverse canonical-correlation defect, and its loss relative to the
optimal transport is itself a positive, exactly typed quadratic form.

## 3. Basis invariance

Replace

\[
E_-\mapsto E_-S,
\qquad
E_+\mapsto E_+T
\]

with \(S,T\) invertible and transform

\[
X\mapsto T^{-1}XS.
\]

Then \(\mathcal R(X)\) is unchanged. Consequently the certificate has no
hidden basis or Gram-condition-number penalty. The inverse \(G_-^{-1}\) is
the intrinsic whitening of the denominator model space, not an auxiliary
inequality.

## 4. Confluent Cauchy scope

For finite inner functions, take \(E_\pm\) to be the synthesis maps of
normalized upper-half-plane reproducing kernels. At a multiple zero, replace
the kernel by its derivative jet. The Grams become the usual confluent Cauchy
blocks, remain positive definite after common-factor reduction, and
(L-106630.1)--(L-106630.6) remain unchanged.
