# L-105270 — Carrier-renormalized polynomial Wick source

Claim ID: `L-105270`  
Status: **PROVED EXACT AT SAFE-LINE SOURCE AND CLOSED-CONTOUR ALGEBRA SCOPE**  
Created: 2026-08-24  
Depends on: R-105270; L-105250--L-105253; L-105320; L-105520  
RH status: not assumed

Let

\[
R_L(x)=(1-x)^{-1}
\]

be the normalized frozen reciprocal source and let \(P_K\) be the degree-\(K\)
truncation of \(\sqrt{1-x}\).  The exact source identity is

\[
P_K(x)^2R_L(x)
=1+Q_K(x),
\qquad
Q_K(x)=\sum_{m\ge K+1}q_{K,m}x^m,
\qquad q_{K,m}\ge0.
\tag{1}
\]

## 1. Closed-contour renormalization

Let \(C[\cdot]\) denote the critical-residue contour compression.  The degree
zero term in (1) is holomorphic on the conclusion contour, so R-105270 gives

\[
\boxed{
C[P_K^2R_L]=C[Q_K].
}
\tag{2}
\]

Thus the conclusion-facing source is not `I+Q_K`; it is the carrier-free tail
`Q_K`.

The half-order and physical-cutoff energy law remains valid:

\[
\mathcal D_K(\alpha)
=
\sum_{m\ge K+1}q_{K,m}^2
\frac{m!}{(2m)!}\alpha^{2m}.
\tag{3}
\]

Hence high-degree Wick cancellation genuinely makes the carrier-free source
small in Hilbert--Schmidt norm.  What it does **not** supply is a positive
identity trace.

## 2. Finite unilateral trace firewall

Let \(S_t\) be the zero-extended right shift on a finite one-sided interval and
let \(V\) be any finite-dimensional shift-invariant nilpotent model.  Every
strictly positive shift has zero trace on the natural triangular basis.  Since
`Q_K` has no degree-zero term,

\[
\boxed{
\operatorname{tr}Q_K(S)=0
}
\tag{4}
\]

in every exact finite triangular source model.

More generally, for any compression whose reproducing diagonal is translation
invariant up to `o(d)`, the trace of the carrier-free stationary model is
`o(d)`.  Therefore the rank--trace quantity

\[
\frac{(\operatorname{tr}C)_+^2}{d\|C\|_{\rm HS}^2}
\]

cannot tend to one merely because \(\mathcal D_K\to0\): both the useful trace
and the fluctuation have been removed.

## 3. Correct use of the polynomial hierarchy

The hierarchy can still be used in either of two legitimate ways:

1. as a small perturbation around a **separately proved conclusion-facing
   carrier** whose positive index is owned by residues, a Cauchy index, or a
   non-holomorphic boundary jump;
2. as a small contour field when the desired conclusion is an upper bound on a
   nonnegative defect, such as an additive reverse--Rolle square loss.

It cannot by itself create a positive closed-contour identity block.

This is a source correction, not a refutation of the coefficient identities,
Banach invertibility, or superfactorial energy estimates in T-105250.
