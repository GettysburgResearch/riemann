# L-105662 — Physical prefactor and Cauchy determinant absorb the universal gap

**Claim ID:** `L-105662`  
**Status:** proved exact finite-packet sufficient theorem  
**Date:** 2026-08-31

Let

\[
\tau_H=n^{-1}\operatorname{tr}(G_0^{-1}G_H).
\]

If a physical source profile obeys `0<=r(xi)<=c e^{-Hxi}`, `0<=c<=1`, its
unused packet reserve is at least `n-cn tau_H`. L-105660 gives phase defect at
most `(32/27)n(1-tau_H)`. Therefore

\[
\boxed{\tau_H\ge\frac5{32-27c}\Longrightarrow
\mathfrak P_{0,H}\le\mathfrak R_r.}\tag{1}
\]

The normalized compression `C_H=G_0^{-1/2}G_HG_0^{-1/2}` is positive, so
`tau_H>=(det C_H)^{1/n}`. The Cauchy determinant is explicit:

\[
\boxed{\Delta_H:=\det C_H=
\prod_i\frac{2\Re\lambda_i}{2\Re\lambda_i+H}
\prod_{i<j}\left|\frac{\overline\lambda_i+\lambda_j}
{\overline\lambda_i+\lambda_j+H}\right|^2.}\tag{2}
\]

Hence `Delta_H^{1/n}>=5/(32-27c)` is an inverse-free sufficient test.
For the actual Xi current of L-105645, `c=h/(b+h)`. Whenever `b>0` the
threshold is strictly below one and is automatically met for sufficiently
shallow translations. At `b=0`, it becomes one, so arbitrary-scale
constant-one CTI remains necessary.
