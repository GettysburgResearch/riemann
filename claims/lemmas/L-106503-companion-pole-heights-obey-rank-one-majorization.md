# L-106503 — Companion pole heights obey rank-one majorization

Claim ID: `L-106503`  
Status: **PROVED EXACT FOR FINITE POLYNOMIAL COMPANIONS**  
Created: 2026-08-25  
Depends on: the matrix determinant lemma and Schur–Ky Fan majorization  
RH status: **not assumed**

For a polynomial `p` with zeros `z_1,...,z_n`, counted with multiplicity, put

\[
\mathfrak h_+(p)=\sum_{\operatorname{Im}z_j>0}\operatorname{Im}z_j,
\qquad
\mathfrak h_-(p)=\sum_{\operatorname{Im}z_j<0}|\operatorname{Im}z_j|.
\]

No real-rootedness assumption is made.

## 1. Rank-one companion model

Let

\[
A=\operatorname{diag}(z_1,\ldots,z_n),
\qquad e=(1,\ldots,1)^T.
\]

The matrix determinant lemma and `p'/p=sum_j 1/(z-z_j)` give

\[
\boxed{
\det\bigl(zI-(A-i\lambda ee^*)\bigr)
=p(z)+i\lambda p'(z),
}
\tag{L-106503.1}

and

\[
\boxed{
\det\bigl(zI-(A+i\lambda ee^*)\bigr)
=p(z)-i\lambda p'(z).
}
\tag{L-106503.2}

Thus every finite companion divisor is the spectrum of a signed imaginary
rank-one perturbation of the original zero divisor.

## 2. Imaginary-height Ky Fan inequality

For any square matrix `M` with eigenvalues `mu_j`, Schur triangularization
shows

\[
\boxed{
\sum_{\operatorname{Im}\mu_j>0}\operatorname{Im}\mu_j
\le \operatorname{tr}(\operatorname{Im}M)_+.
}
\tag{L-106503.3}

Indeed the left side is the trace of `Im M` against one orthogonal projection
in a Schur basis, and the right side is the variational maximum over all
positive contractions.

Since

\[
\operatorname{Im}(A-i\lambda ee^*)
=\operatorname{diag}(\operatorname{Im}z_j)-\lambda ee^*,
\]

subtracting the positive rank-one matrix cannot increase the positive-part
trace.  Equations (L-106503.1)--(L-106503.3) therefore give

\[
\boxed{
\mathfrak h_+(p+i\lambda p')
\le\mathfrak h_+(p).
}
\tag{L-106503.4}

For the opposite orientation,

\[
\operatorname{tr}(X+\lambda ee^*)_+
\le\operatorname{tr}X_++\lambda\|e\|^2,
\]

so

\[
\boxed{
\mathfrak h_+(p-i\lambda p')
\le\mathfrak h_+(p)+\lambda n.
}
\tag{L-106503.5}

Reflection supplies the lower-half-plane analogues

\[
\boxed{
\mathfrak h_-(p-i\lambda p')
\le\mathfrak h_-(p),
\qquad
\mathfrak h_-(p+i\lambda p')
\le\mathfrak h_-(p)+\lambda n.
}
\tag{L-106503.6)

## 3. Endpoint denominator budget

For the odd endpoint denominator

\[
D_{K,\lambda}
=(p+i\lambda p')
 (p^{(K)}-i\lambda p^{(K+1)}),
\]

common-factor reduction can only remove poles.  Hence

\[
\boxed{
\mathfrak h_+(D_{K,\lambda}^{\rm red})
\le
\mathfrak h_+(p)
+\mathfrak h_+(p^{(K)})
+\lambda(n-K).
}
\tag{L-106503.7)

The mirrored denominator has the corresponding lower-height bound.

## 4. Scope

The theorem prices the **sum of companion pole depths**, not their count and
not a variable all-pass commutator.  Passing to an entire Xi window requires a
canonical-product truncation with the literal endpoint and confluent ledger.
The estimate is nevertheless uniform in the finite degree and introduces no
separation constant.
