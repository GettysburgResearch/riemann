# R-90901 — No fixed nonlinear truncation detects every negative trace-class direction

Claim ID: `R-90901`  
Status: **EXACT ABSTRACT FIREWALL**  
Created: 2026-08-11  
Scope: exterior coefficients, bounded Fredholm range, bounded heat range, and fixed shifted-Hankel order

This note prevents a common overclaim in the Fredholm/heat programme.  Every finite stage is a valid certificate when it fails, but **no fixed finite stage is a complete positivity test**.

## 1. Exterior coefficients

For integers \(K\ge1\) and \(0<\varepsilon<1/K\), let

\[
 A=I_K\oplus(-\varepsilon).
\]

Its exterior coefficients are

\[
 e_k(A)=\binom Kk-\varepsilon\binom K{k-1}
 \qquad(1\le k\le K),
\tag{R-90901.1}
\]

and

\[
 e_{K+1}(A)=-\varepsilon<0.
\tag{R-90901.2}
\]

Thus the first \(K\) exterior coefficients are positive although \(A\) is indefinite.  More precisely, the first negative coefficient occurs at

\[
 \boxed{
 k_{\min}
 =\left\lfloor\frac{K+1}{1+\varepsilon}\right\rfloor+1.
 }
\tag{R-90901.3}
\]

## 2. Bounded Fredholm parameter

For the same operator,

\[
 \det(I+tA)=(1+t)^K(1-\varepsilon t).
\tag{R-90901.4}
\]

Hence any test restricted to \(0\le t\le T_0<1/\varepsilon\) sees a strictly positive determinant despite the negative eigenvalue.

## 3. Bounded heat time

Let \(A=1\oplus(-\varepsilon)\).  Its relative heat trace is

\[
 \Theta_A(\beta)=e^{-\beta}-1+e^{\varepsilon\beta}-1.
\tag{R-90901.5}
\]

Fix \(B>0\).  Since \(g(\beta)=\log(2-e^{-\beta})\) is concave and \(g(0)=0\), \(g(\beta)/\beta\) is decreasing.  Therefore, if

\[
 0<\varepsilon\le\frac{\log(2-e^{-B})}{B},
\tag{R-90901.6}
\]

then

\[
 \Theta_A(\beta)\le0
 \qquad(0\le\beta\le B),
\tag{R-90901.7}
\]

although \(A\) is indefinite.

## 4. Fixed shifted-Hankel order

Fix \(d\ge0\) and distinct positive numbers \(x_0,\ldots,x_d\).  Evaluation at \(-\varepsilon\) is a bounded linear functional on the \((d+1)\)-dimensional polynomial space, so there is \(C<\infty\) such that

\[
 |p(-\varepsilon)|^2
 \le C\sum_{j=0}^d x_j|p(x_j)|^2
 \qquad(\deg p\le d).
\tag{R-90901.8}
\]

Let \(A\) have \(M\) copies of each positive eigenvalue \(x_j\) and one negative eigenvalue \(-\varepsilon\).  If \(M>\varepsilon C\), then

\[
 \operatorname{tr}\big[A|p(A)|^2\big]
 =M\sum_jx_j|p(x_j)|^2
 -\varepsilon|p(-\varepsilon)|^2
 \ge0
\tag{R-90901.9}
\]

for every polynomial of degree at most \(d\).  Equivalently, every shifted-Hankel matrix through order \(d\) is positive semidefinite while \(A\) has a negative eigenvalue.

## 5. Consequence

No theorem of the following fixed-complexity forms can imply RH:

```text
first K exterior coefficients are nonnegative;
det(I+tA)>0 only on a bounded t-range;
relative heat trace has the RH sign only on a bounded beta-range;
one fixed shifted-Hankel matrix is PSD.
```

The complete hierarchy or an adaptive complexity bound is mandatory.
