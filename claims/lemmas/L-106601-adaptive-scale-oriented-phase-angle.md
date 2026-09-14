# L-106601 — Adaptive-scale endpoint charge has a phase-angle majorant

Claim ID: `L-106601`  
Status: **CORRECTED EXACT MAJORIZATION FOR FINITE REDUCED INNER QUOTIENTS**  
Created: 2026-08-26  
Corrected: 2026-08-26  
Depends on: corrected `L-106514`, `L-106600`  
RH status: **not assumed**

Retain the variable-scale endpoint quotient \(U_{K,a}\) of `L-106600`.
After common-factor reduction and canonical normalization at infinity, write

\[
U_{K,a}=\frac{B_{+,a}}{B_{-,a}},
\]

where \(B_{+,a},B_{-,a}\) are finite upper-half-plane inner functions.
On the real boundary let

\[
B_{-,a}(t)=e^{i\beta_a(t)},
\qquad
\beta_a'(t)\ge0.
\]

The previous version of this claim used the superseded equality in
`L-106514`.  The exact statement is an inequality.

## 1. Correct oriented majorant

The corrected denominator phase-angle theorem gives

\[
\boxed{
\|H_{U_{K,a}}\|_{\mathcal S_2}^2
\le
\frac1{4\pi}\int_{\mathbb R}
\beta_a'(t)|1-U_{K,a}(t)|^2\,dt.
}
\tag{L-106601.1}
\]

Using `L-106600.6` gives

\[
\boxed{
\|H_{U_{K,a}}\|_{\mathcal S_2}^2
\le
\frac1{\pi}\int_{\mathbb R}
\beta_a'(t)
\frac{a(t)^2\mathcal L_K(t)^2}
{(F^2+a^2F'^2)
 ((F^{(K)})^2+a^2(F^{(K+1)})^2)}
\,dt.
}
\tag{L-106601.2}
\]

The right side charges only the adverse denominator phase, but it may
overpay the exact canonical defect by the nonnegative cross-Hankel
phase-alignment slack in `L-106514.9`.

## 2. Strict enlargement of the exact optimization class

Let \(\mathcal A_T\) be any source-predeclared class of admissible positive
analytic scales on the regular window.  If it contains the positive
constants, then the exact charges still satisfy

\[
\boxed{
\inf_{a\in\mathcal A_T}\|H_{U_{K,a}}\|_{\mathcal S_2}^2
\le
\inf_{\lambda>0}\|H_{U_{K,\lambda}}\|_{\mathcal S_2}^2.
}
\tag{L-106601.3}
\]

Thus adaptive scaling weakens the open conclusion-facing canonical-correlation
estimate without changing the endpoint index or the high-derivative entry
theorem.

For the stronger phase majorants one may separately optimize

\[
\mathcal A_-(U_{K,a})
=
\frac1{4\pi}\int\beta_a'|1-U_{K,a}|^2.
\]

A small optimized phase majorant is sufficient for a small exact charge, but
the two infima are not asserted equal.

## 3. Slope form

Where \(FF^{(K)}\ne0\), put

\[
x_a=a\frac{F'}F,
\qquad
y_a=a\frac{F^{(K+1)}}{F^{(K)}}.
\]

Then the pointwise boundary identity remains exact:

\[
\boxed{
|1-U_{K,a}|^2
=
\frac{4(x_a-y_a)^2}
{(1+x_a^2)(1+y_a^2)}
=
4\sin^2\!\left(\arctan x_a-\arctan y_a\right).
}
\tag{L-106601.4}
\]

It must be integrated against the scale-dependent positive measure
\(\beta_a'dt\).  Optimizing it pointwise while ignoring that measure is
invalid.

## 4. Entire-Xi passage

For Xi, apply the finite majorization to regular canonical-product
exhaustions.  The admissible scale must be holomorphic on the exhaustion
contour and strictly positive on the real window.  Common-zero, confluent,
horizontal, and cofinal errors remain in the explicit regularization ledger.

```text
adaptive canonical charge                               EXACT
adaptive denominator phase statistic                    EXACTLY DEFINED
canonical charge <= phase statistic                     PROVED
canonical charge = phase statistic                      REFUTED IN GENERAL
adaptive shallow-correlation gate                       OPEN
```
