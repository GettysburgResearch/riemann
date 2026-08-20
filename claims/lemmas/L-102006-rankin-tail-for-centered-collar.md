# L-102006 — Rankin control of the centered large-product collar tail

Claim ID: `L-102006`  
Status: **PROVED EXACT/UNCONDITIONAL WEIGHT BOUND; DOES NOT CLOSE THE SIGN**  
Created: 2026-08-21  
Depends on: `L-102005`; PR #691 `L-100615--L-100616`  
RH status: **not assumed**

Retain the centered collar expansion

\[
\widetilde H_{ij}(X)
=
\sum_{\substack{S\subseteq(i,j)\\m_S>X/(p_ip_j)}}
(-1)^{|S|}m_S^{-1/2}\widetilde K_{ij}(X/m_S).
\]

For `0<theta<1/2`, Rankin's inequality on the forced threshold gives

\[
1_{m_S>X/(p_ip_j)}
\le
\left({m_Sp_ip_j\over X}\right)^\theta.
\]

Hence the unsigned coefficient tail satisfies

\[
\boxed{
\sum_{\substack{S\subseteq(i,j)\\m_S>X/(p_ip_j)}}m_S^{-1/2}
\le
\left({p_ip_j\over X}\right)^\theta
\prod_{p_i<p<p_j}(1+p^{-1/2+\theta}).
}
\tag{L-102006.1}
\]

This formula is exact as a finite Euler-product bound. It exposes the limitation of source-blind Rankin control: because `1/2-theta<1`, the prime sum

\[
\sum_{p_i<p<p_j}p^{-1/2+\theta}
\]

is power-sized in the upper endpoint, so (L-102006.1) is not subcritical on supercritical long intervals.

Therefore the large-product threshold of `L-102005`, though genuine, cannot be closed by an unsigned Rankin argument. The finite-squaring step of PR #691 is essential: it must be applied before absolute values so selected small/intermediate primes pay `p^-1` rather than `p^-1/2`.

## Squared Rankin version

After source-side squaring of every interior prime `p<=Z`, the corresponding unsigned threshold bound becomes

\[
\boxed{
\left({p_ip_j\over X}\right)^\theta
\prod_{\substack{p_i<p<p_j\\p\le Z}}(1+p^{-1+2\theta})
\prod_{\substack{p_i<p<p_j\\p>Z}}(1+p^{-1/2+\theta}).
}
\tag{L-102006.2}
\]

If `Z>=sqrt(X/(p_ip_j))`, every subset made solely from unsquared primes above `Z` has product either `1` or exceeds the physical threshold after at most a bounded number of labels. This is the precise interface where a depth-one/depth-two argument can replace the divergent unsquared Euler product.

No claim of subpower closure is made here. The theorem identifies why Rankin alone fails and what the finite squaring must accomplish on the same centered collar.