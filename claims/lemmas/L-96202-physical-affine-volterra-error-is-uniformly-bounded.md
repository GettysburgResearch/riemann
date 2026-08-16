# L-96202 — The physical affine–Volterra packing error remains uniformly bounded

Claim ID: `L-96202`  
Status: **PROVED ON THE RETAINED-CELL ERROR ESTIMATE; ENDPOINT SCOPE CORRECTED**  
Created: 2026-08-16  
Depends on: PR #513 `L-93920--L-93921`, elementary Chebyshev bounds  
RH status: not assumed

Assume the exact hybrid identity
\[
c_X=d_X^0+\mathcal R E_X^I
\]
and the retained-cell estimates
\[
|v_q(E_X^I)|<\frac{57}{2q\sqrt K},
\qquad
|\mathcal D_4v_q(E_X^I)|<\frac{171}{4q\sqrt K},
\]
where \(K=\lfloor X/67\rfloor+1\).

For
\[
\tau_K=\frac{\sqrt K}{\sqrt K+24},\qquad d_X=\tau_Kd_X^0,
\]
the all-column proof gives
\[
C_{d_X}\le w_X,\qquad \Xi_{d_X}\le\Omega_X.
\]

The correct physical-score loss is
\[
P_\Lambda-\mathcal H(d_X)
=(1-\tau_K)P_\Lambda
+\tau_K\sum_q\Lambda(q)v_q(E_X^I).
\]
Using
\[
P_\Lambda(X)<16(\log2)\sqrt X
\]
and
\[
\sum_{q\le X}\frac{\Lambda(q)}q
\le 4(\log2)(1+\log X),
\]
one obtains for \(X\ge10^{12}\)
\[
\boxed{
0\le P_\Lambda(X)-\mathcal H(d_X)<3457.
}
\]

The signed mismatch is actually bounded by
\[
\left|\sum_q\Lambda(q)v_q(E_X^I)\right|
<
\frac{114(\log2)(1+\log X)}{\sqrt K}<1.
\]

This theorem repairs the *meaning* of the old constant without changing its all-column algebra. It gives no estimate for \(F_\Lambda\).
