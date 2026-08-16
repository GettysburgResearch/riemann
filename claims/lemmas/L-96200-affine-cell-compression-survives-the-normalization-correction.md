# L-96200 — Exact affine-cell Volterra compression survives the endpoint normalization correction

Claim ID: `L-96200`  
Status: **PROVED EXACT**  
Created: 2026-08-16  
Depends on: PR #495 `L-91760`, review #503, T-94000 `L-94000`  
RH status: not assumed

For every complete endpoint cell \(n\le s<n+1\),
\[
g_s=a_n-s^{-1/2}b_n,\qquad
p_s=\mathcal Rg_s=A_n-s^{-1/2}B_n.
\]
If \(I=[a,b]\subset[n,n+1]\) and \(w\ge0\), put
\[
M_I=\int_Iw(s)\,ds,\qquad
\bar u_I=M_I^{-1}\int_Iw(s)s^{-1/2}\,ds.
\]
Then \(b^{-1/2}\le\bar u_I\le a^{-1/2}\), and with
\[
\theta_I=\frac{\bar u_I-b^{-1/2}}{a^{-1/2}-b^{-1/2}}\in[0,1]
\]
one has
\[
\boxed{
\int_Iw(s)p_s\,ds
=M_I\left[\theta_Ip_a+(1-\theta_I)p_{b-}\right].
}
\]

This is a finite positive two-node realization preserving every *linear physical-row observation*. In particular it preserves:

- every component row;
- ordinary \(q\) and ordinary \(4q\);
- radix-four detail after those two observations are formed;
- physical entropy \(\mathcal H\).

It does **not** identify the declared source benchmark \(J_\Lambda\) with the physical score. Thus `R-96200` changes the endpoint composition but does not invalidate the affine-cell theorem.

The exact negative review-#503 witness remains binding:
\[
p_{1005}(14)-67^{-1/2}p_{15}(14)<0.
\]
No derivative-fibre causal operation is used.
