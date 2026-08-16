# L-96201 — The complete endpoint loss splits into arithmetic gap plus physical packing slack

Claim ID: `L-96201`  
Status: **PROVED EXACT**  
Created: 2026-08-16  
Depends on: `R-96200`, the exact row identities of PR #495 / PR #513  
RH status: not assumed

Let \(c_X\) be the canonical signed native row satisfying
\[
C_{c_X}(q)=w_X(q).
\]
Hence
\[
\mathcal H(c_X)=P_\Lambda(X).
\]

Suppose an affine–Volterra producer gives a nonnegative row \(d_X\) and a signed row error \(e_X=c_X-d_X\). Then exactly
\[
P_\Lambda(X)-\mathcal H(d_X)=\mathcal H(e_X),
\]
and therefore
\[
\boxed{
J_\Lambda(X)-\mathcal H(d_X)
=F_\Lambda(X)+\mathcal H(e_X).
}
\tag{L-96201.1}
\]

For the hybrid row
\[
c_X=d_X^0+\mathcal R E_X^I,\qquad d_X=\tau_Kd_X^0,
\]
this becomes
\[
\boxed{
J_\Lambda-\mathcal H(d_X)
=F_\Lambda
+(1-\tau_K)P_\Lambda
+\tau_K\mathcal H(\mathcal R E_X^I).
}
\tag{L-96201.2}
\]

Thus the existing thinning and mismatch estimates still prove
\[
P_\Lambda-\mathcal H(d_X)=O(1),
\]
but the complete loss contains the additional exact term \(F_\Lambda\).

No source allocation, tail certificate, or physical-row refinement can remove \(F_\Lambda\) merely by reducing \(P_\Lambda-\mathcal H(d_X)\).
