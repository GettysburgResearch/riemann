# L-96602 — The factor-67 first-owner tree is kernel-independent and preserves complete finite colors

Claim ID: `L-96602`  
Status: **PROVED EXACT SOURCE IDENTITY**  
Created: 2026-08-17  
Depends on: the exact causal identity; PR #552 source dictionaries

Define the positive scale-four source kernel

\[
 h_X(n)=\frac1{\sqrt n}
 \min\!\left(\log4,\log\frac Xn\right)_+.
\]

It has exact scale covariance. If `n=pm`, then

\[
 p^{-1/2}h_{X/p}(m)=h_X(pm).
 \tag{L-96602.1}
\]

Consequently

\[
 h_X-p^{-1/2}A_ph_{X/p}
\]

is literally the restriction of `h_X` to source indices not divisible by `p`.
It is a positive packet; no signed child is observed.

For ordered active rough primes `p_i>=67`, put

\[
 r_i=p_i^{-1/2},
 \quad s_i=\prod_{\nu\le i}(1-r_\nu),
 \quad \lambda_i=r_is_{i-1},
 \quad \alpha_i=r_i\lambda_i.
\]

The exact identity

\[
P_X=s_kP_X+
\sum_i\lambda_i(P_X-r_iA_{p_i}P_{X/p_i})+
\sum_i\alpha_iA_{p_i}P_{X/p_i}
\tag{L-96602.2}
\]

is polynomial algebra:

\[
s_k+\sum_i\lambda_i=1,
\qquad
-\lambda_ir_i+\alpha_i=0.
\]

It applies to the annular kernel because only positivity and (L-96602.1) are
used. Recursive children have scale at most `X/67`; the tree therefore
terminates after finitely many generations.

The finite colors `d|P_61` are passive labels throughout the rough tree. Rough
ownership never splits or observes them. At a terminal current edge with owner
`p`, all colors are summed first, and the signed row is exactly

\[
 E_{j,Pp}(Z)=E_j(Z)-p^{-1/2}E_j(Z/p).
 \tag{L-96602.3}
\]

Thus the tree has one owner per source occurrence and no individual-color
positivity assertion. This is the required correction to the ambiguous leaf
wording in PR #555.
