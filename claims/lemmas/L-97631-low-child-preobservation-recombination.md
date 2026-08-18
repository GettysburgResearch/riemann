# L-97631 — Low rough children recombine before signed observation

Claim ID: `L-97631`  
Status: **PROVED EXACT ALGEBRAIC IDENTITY**

For active rough primes `p_i`, set
\[
r_i=p_i^{-1/2},\quad
s_i=\prod_{h\le i}(1-r_h),\quad
\lambda_i=r_is_{i-1},\quad
\alpha_i=r_i\lambda_i.
\]
Then
\[
s_k+\sum_i\lambda_i=1,\qquad
\sum_i\alpha_i<\frac1{\sqrt{67}}<\frac18.
\]

For every child scale `y_i=x/p_i<239`,
\[
\boxed{
\lambda_i\bigl(P_x-r_iSA_{p_i}P_{y_i}\bigr)
+\alpha_iSA_{p_i}P_{y_i}
=\lambda_iP_x.
}
\tag{L-97631.1}
\]
The child is recombined before signed observation. Therefore no low odd-history
leaf is separately fed into a parity-blind terminal Hall map.
