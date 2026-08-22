# L-105100 — Exact second critical-residue balance

Claim ID: L-105100

Status: **PROPOSED EXACT FINITE-POLYNOMIAL IDENTITY; review pending**

Created: 2026-08-23

Arithmetic class: **EXACT_RATIONAL proof fixtures; symbolic proof below**

RH status: **not assumed**

## 1. Statement

Let p be a monic polynomial of degree \(n\ge2\), with roots
\(z_1,\ldots,z_n\) counted with multiplicity. Assume:

1. every zero c of \(p'\) is simple and \(p(c)\ne0\);
2. every zero d of \(p''\) is simple.

The first condition implies that \(p'(d)\ne0\) at every zero d of \(p''\).
When \(n=2\), the second sum below is empty.

Define

\[
\rho_c=\frac{p(c)}{p''(c)}
\quad\text{for }p'(c)=0,
\tag{L-105100.1}
\]

and

\[
\tau_d=\frac{p(d)^2}{p'(d)p'''(d)}
\quad\text{for }p''(d)=0.
\tag{L-105100.2}
\]

Let

\[
\bar z=\frac1n\sum_{r=1}^n z_r,
\qquad
V_j=\sum_{r=1}^n(z_r-\bar z)^j.
\tag{L-105100.3}
\]

Then

\[
\boxed{
\sum_{p'(c)=0}\rho_c^2
+
\sum_{p''(d)=0}\tau_d
=
\mathcal K_4(p)
}
\tag{L-105100.4}
\]

where

\[
\boxed{
\mathcal K_4(p)=
\frac{(6n^2-18n+13)V_2^2
-3n(n-1)(n-2)V_4}
{n^4(n-1)^3}.
}
\tag{L-105100.5}
\]

All sums in (L-105100.4) are algebraic sums. They are not sums of absolute
values at nonreal points.

## 2. Residue proof

Consider

\[
Q(z)=\frac{p(z)^2}{p'(z)p''(z)}.
\tag{L-105100.6}
\]

At a zero c of \(p'\), simplicity gives

\[
p'(z)=p''(c)(z-c)+O((z-c)^2),
\]

and \(p''(c)\ne0\). Therefore

\[
\operatorname{Res}_{z=c}Q(z)
=\frac{p(c)^2}{p''(c)^2}
=\rho_c^2.
\tag{L-105100.7}
\]

At a zero d of \(p''\), simplicity gives

\[
\operatorname{Res}_{z=d}Q(z)
=\frac{p(d)^2}{p'(d)p'''(d)}
=\tau_d.
\tag{L-105100.8}
\]

These are the only possible finite poles of Q. A zero of \(p\) at a
\(p''\)-zero can make the corresponding singularity removable, in which case
(L-105100.8) is zero. It remains to compute the coefficient of \(z^{-1}\) in
the Laurent expansion at infinity.

Translation conjugates Q by the same shift and leaves its residue multiset,
its \(z^{-1}\) coefficient, and the centered moments invariant. Thus translate
until \(\bar z=0\). Put \(L=p'/p\). The root expansion is

\[
L(z)
=\frac n z+\frac{V_2}{z^3}+\frac{V_3}{z^4}
+\frac{V_4}{z^5}+O(z^{-6}).
\tag{L-105100.9}
\]

Since \(p''/p=L'+L^2\),

\[
\begin{aligned}
L(L'+L^2)
={}&\frac{n^2(n-1)}{z^3}
+\frac{n(3n-4)V_2}{z^5}
+\frac{n(3n-5)V_3}{z^6}\\
&+\frac{3n(n-2)V_4+3(n-1)V_2^2}{z^7}
+O(z^{-8}).
\end{aligned}
\tag{L-105100.10}
\]

But

\[
Q=\frac1{L(L'+L^2)}.
\]

Inverting (L-105100.10), the coefficient of \(z^{-1}\) is

\[
\frac1{n^2(n-1)}
\left[
\frac{(3n-4)^2V_2^2}{n^2(n-1)^2}
-
\frac{3n(n-2)V_4+3(n-1)V_2^2}{n^2(n-1)}
\right],
\]

which simplifies to (L-105100.5). The sum of all finite residues equals the
coefficient of \(z^{-1}\) in Q, proving (L-105100.4).

## 3. Exact real/nonreal decomposition

Suppose p has real coefficients. Split the critical points into

\[
\mathcal R=\{c\in\mathbb R:p'(c)=0\},
\qquad
\mathcal C=\{c\notin\mathbb R:p'(c)=0\}.
\]

At a real critical point, \(\rho_c\) is real. Hence the exact second moment
needed by a real-extrema argument is

\[
\boxed{
\sum_{c\in\mathcal R}|\rho_c|^2
=
\mathcal K_4(p)
-
\sum_{c\in\mathcal C}\rho_c^2
-
\sum_{p''(d)=0}\tau_d.
}
\tag{L-105100.11}
\]

Conjugate pairing makes the right side real, but neither correction has a
fixed sign in general.

## 4. Relation to the PR #720 frontier

At exact head 10bba584c01277e880aaa21e1fea09f396ca7246, PR #720's
L-104523.3 already identifies \(p^2/(p'p'')\) as the local contour observable
for squared residues and warns that a global contour also encloses the
\(p''\)-zeros. L-105100 is the continuation that computes the missing
infinity coefficient and makes that warned correction explicit.

The same PR defines the open Xi input RCMV104530 using

\[
M_{2,k}(T)
=\sum_{\Xi^{(k)}(c)=0,\ c\in\mathbb R}
\left|\frac{\Xi^{(k-1)}(c)}{\Xi^{(k+1)}(c)}\right|^2.
\]

The finite identity is global: it sums every critical point of one polynomial.
RCMV104530 is height truncated: it sums real critical points with
\(|c|<T\). Therefore (L-105100.11) is not directly a finite-T Xi
decomposition.

A possible continuation through symmetric polynomial truncations of
\(\Xi^{(k-1)}\) has four separate burdens:

1. localize the global residue identity to \(|c|<T\), retaining exterior
   residues and window-boundary terms;
2. pass the centered \(V_2,V_4\) ledger and localized residue sums through a
   two-parameter truncation/height limit with an explicit order of limits;
3. control the off-real zeros of \(\Xi^{(k)}\) in the squared-residue sum;
4. control the cross-residue debt at zeros of \(\Xi^{(k+1)}\).

This is a global finite-polynomial interface only. Height localization,
exhaustion, correction bounds, the Xi mean-value estimate, and RCMV104530
remain open.

## 5. Scope

The identity is exact under the displayed finite hypotheses. It supplies no
positivity, no asymptotic estimate, and no entire-function limit. Repeated
critical points require a confluent residue formula and are outside this
claim. No claim is made for a height-truncated residue sum.
