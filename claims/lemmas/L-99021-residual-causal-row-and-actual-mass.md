# L-99021 — Exact residual-only causal splitting contracts actual child mass and preserves literal row score

Claim ID: `L-99021`  
Status: **PROPOSED COMPLETE EXACT THEOREM**  
Created: 2026-08-18  
RH status: **not assumed**

Let `P` be a positive residual-source packet at endpoint `Y`. Let its ordered
active rough primes be

\[
67\le p_1<\cdots<p_k,
\qquad r_i=p_i^{-1/2}.
\]

Put

\[
s_i=\prod_{h\le i}(1-r_h),
\qquad
\lambda_i=r_i s_{i-1},
\qquad
\alpha_i=r_i\lambda_i.
\]

For the same-index child operator `U_i`, causal zero extension makes `U_iP_i`
zero whenever the prime is inactive. Then

\[
\boxed{
P=s_kP+
  \sum_i\lambda_i(P-r_iU_iP_i)+
  \sum_i\alpha_iU_iP_i.
}
\tag{L-99021.1}

Indeed,

\[
s_k+\sum_i\lambda_i=1,
\qquad
-\lambda_i r_i+\alpha_i=0.
\]

The endpoint monotonicity of the canonical component rows gives

\[
Q_Y-r_iQ_{Y/p_i}
=(Q_Y-Q_{Y/p_i})+(1-r_i)Q_{Y/p_i}\ge0,
\]

and the identical formula holds in every ordinary and radix-four response.
Thus every current difference in (L-99021.1) is a positive row packet.

Because literal entropy is a linear functional of the physical row, the exact
row identity gives, without an auxiliary source-score identification,

\[
\mathcal H(P)
=
\mathcal H(P^{\rm cur})+
\sum_i\alpha_i\mathcal H(U_iP_i).
\tag{L-99021.2}

Let `m` be the positive target-mass coordinate. Same-index placement is target
nonexpansive:

\[
m(U_iP_i)\le m(P).
\tag{L-99021.3}

Since

\[
\sum_i\alpha_i
\le r_1\sum_i\lambda_i
<67^{-1/2}<1/8,
\]

one obtains the actual-mass estimate

\[
\boxed{
\sum_i\alpha_i m(U_iP_i)<\frac18m(P).
}
\tag{L-99021.4}

Positive direct integration and arbitrary common restrictions preserve
(L-99021.1)--(L-99021.4) by Tonelli. Grouping children by complete provenance
label and normalizing by their actual masses therefore yields a hereditary
coefficient family whose total is below `1/8`.

The Hall row sort of `L-99020` is excluded from this operation. It has no child
coordinate.

## Literal-score backup inequality

For independent auditing, put

\[
E(Y)=\sum_{2\le m\le Y}\frac{\log m}{\sqrt m}\log\frac Ym,
\qquad S(Y)=5\sqrt Y-3.
\]

For every real `p>=67` and `Y>=p`, the packet also proves

\[
\boxed{
E(Y)-p^{-1/2}E(Y/p)
\ge
S(Y)-p^{-1/2}S(Y/p).
}
\tag{L-99021.5}

The proof is included in the standalone manuscript. It is not needed for the
coefficient-one score identity (L-99021.2), but it independently blocks any
hidden loss when the source-declared score is used as an audit coordinate.
