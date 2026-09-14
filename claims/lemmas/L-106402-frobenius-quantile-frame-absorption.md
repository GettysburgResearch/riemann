# L-106402 — Frobenius quantile absorption for an endpoint frame

Claim ID: `L-106402`  
Status: **PROVED EXACT FINITE LINEAR ALGEBRA**  
Created: 2026-08-24  
Depends on: none beyond the spectral theorem  
RH status: **not assumed**

Let \(G_0,G,Q\) be \(d\times d\) Hermitian matrices with

\[
G_0>0,\qquad G>0,\qquad Q\succeq0.
\]

Put

\[
\widetilde G=G_0^{-1/2}GG_0^{-1/2},
\qquad
\widetilde Q=G_0^{-1/2}QG_0^{-1/2}.
\]

Assume

\[
\|\widetilde G-I\|_{\mathrm F}^2\le\delta d
\tag{L-106402.1}
\]

and fix \(0<a<1\).  Let \(P_a\) be the spectral projection of
\(\widetilde G\) onto eigenvalues at least \(a\).

## 1. Lower-frame quantile

Every discarded eigenvalue \(\lambda<a\) satisfies

\[
|\lambda-1|>1-a.
\]

Therefore

\[
\boxed{
\operatorname{rank}(I-P_a)
\le\frac{\delta}{(1-a)^2}d.
}
\tag{L-106402.2}
\]

On the retained subspace,

\[
P_a\widetilde G^{-1}P_a\preceq a^{-1}P_a.
\]

Consequently

\[
\boxed{
\operatorname{tr}
\bigl(P_a\widetilde G^{-1/2}\widetilde Q
      \widetilde G^{-1/2}P_a\bigr)
\le a^{-1}\operatorname{tr}\widetilde Q.
}
\tag{L-106402.3}
\]

The theorem needs only a Frobenius-square average.  No operator-norm closeness
of \(G\) to \(G_0\) is required.

## 2. Dimension-normalized form

Suppose the source frame has dimension

\[
d\ge(1-\kappa)N
\]

inside a conclusion-facing space of dimension \(N\).  If an exact index or
reverse--Rolle ledger charges:

```text
original source codimension;
low-eigenvalue frame discard;
inverse-frame leakage trace,
```

then (L-106402.2)--(L-106402.3) bound the total normalized charge by

\[
\boxed{
\kappa+(1-\kappa)
\left[
\frac{\delta}{(1-a)^2}+\frac q a
\right],
}
\tag{L-106402.4}
\]

whenever

\[
\operatorname{tr}\widetilde Q\le qd.
\]

## 3. Record-capable constants

Choose

\[
\kappa=\frac1{1000},\qquad
\delta=\frac1{100},\qquad
q=\frac1{200},\qquad
a=\frac12.
\]

Then the complete charge is at most

\[
\boxed{
\frac1{1000}
+\frac{999}{1000}\left(\frac1{25}+\frac1{100}\right)
=\frac{1019}{20000}
=0.05095.
}
\tag{L-106402.5}

Against the fixed-order input \(599/625=0.9584\), this leaves

\[
\boxed{
\frac{599}{625}-\frac{1019}{20000}
=\frac{18149}{20000}
=0.90745.
}
\tag{L-106402.6}

The unused margin above ninety percent is

\[
\boxed{
\frac{18149}{20000}-\frac9{10}
=\frac{149}{20000}
=0.00745.
}
\tag{L-106402.7}

## Scope

The lemma is exact finite linear algebra.  It does not prove that an Xi frame
satisfies (L-106402.1) or the trace bound; it fixes the precise tolerances that
would suffice.
