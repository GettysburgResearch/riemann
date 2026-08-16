# T-96010 — Eventual positivity of the two smallest annular rows directly implies the Riemann Hypothesis

Claim ID: `T-96010`  
Status: **PROVED COMPLETE IMPLICATION / TWO EXPLICIT PRODUCER INEQUALITIES REMAIN**  
Created: 2026-08-16  
Depends on: `L-96010`, `L-96011`, Landau's theorem for Mellin transforms  
RH status: **unproved because the two-row positivity producer is not certified**

Assume that for \(j=2,3\) there is \(X_j\) such that

\[
a_X(j)=c_X(j)-c_{X/4}(j)\ge0
\qquad(X\ge X_j).
\tag{T-96010.1}
\]

For either row, remove the bounded initial interval \([1,X_j)\). Its Mellin
transform is entire, so it changes no pole of `L-96010.6`. The remaining
Mellin transform is the transform of a nonnegative function.

Let \(\sigma_j\) be its real abscissa of convergence. A crude bound
\(a_X(j)=O_j(\sqrt X\log X)\) makes \(\sigma_j\) finite. Landau's theorem says
that a finite real abscissa of a nonnegative Mellin transform is singular.
But `L-96010.6` is analytic at every real \(s>0\): zeta has no real zero in
\((1/2,\infty)\), its pole at one becomes a zero of \(1/\zeta\), and
\(1-4^{-s}\ne0\). Hence \(\sigma_j\le0\), and the defining integral is
holomorphic throughout \(\Re s>0\).

Suppose \(\zeta(\rho)=0\) with \(\Re\rho>1/2\), and put
\(s_\rho=\rho-1/2\). By `L-96011`, one of \(P_2(\rho),P_3(\rho)\) is nonzero.
Choose that row. In `L-96010.6`, the factor \(1-4^{-s_\rho}\) is nonzero, so
\(s_\rho\) is a nonremovable pole. This contradicts holomorphy of the defining
integral in \(\Re s>0\).

The functional equation reflects every nontrivial zero left of the critical
line to one right of it. Therefore (T-96010.1) implies RH.

```text
J_Lambda/P_Lambda/F_Lambda bridge     not used
full-row annular telescope             not used
prime-square moat                      not used
large-j noncancellation                not used
rows required                          exactly 2 and 3
eventual two-row positivity            sole producer gate
```
