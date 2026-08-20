# L-102003 — Joint min-max survival suppresses supercritical endpoint pairs

Claim ID: `L-102003`  
Status: **PROVED ASYMPTOTIC WEIGHT THEOREM; COLLAR AMPLITUDE STILL OPEN**  
Created: 2026-08-21  
Depends on: PR #691 `L-100615--L-100616`  
RH status: **not assumed**

Let the ordered future prime labels be `p_i`, with native activities

\[
r_i=p_i^{-1/2},
\]

and joint least/greatest-owner probability

\[
\pi_{ij}=r_ir_jL_iR_j,
\qquad
L_i=\prod_{h<i}(1-r_h),
\qquad
R_j=\prod_{h>j}(1-r_h).
\]

Fix `A>1`. Consider the supercritical owner region

\[
\mathcal S_A=\{(i,j):i<j,\ p_j>p_i^A\}.
\]

Then the complete joint probability mass of this region is finite and, as the lower endpoint threshold `P` tends to infinity,

\[
\boxed{
\sum_{\substack{i<j\\p_i\ge P\\p_j>p_i^A}}
\pi_{ij}
\longrightarrow0.
}
\tag{L-102003.1}
\]

More quantitatively, the contribution with a fixed lower owner `i` obeys

\[
\boxed{
\sum_{j:\,p_j>p_i^A}\pi_{ij}
\le r_iL_i\,R_{J(i)},
}
\tag{L-102003.2}
\]

where `J(i)` is the first index with `p_(J(i))>p_i^A`. Indeed,

\[
\sum_{j\ge J} r_jR_j
\le \sum_{j\ge J}(R_{j-1}-R_j)
=R_{J-1}
\]

because

\[
R_{j-1}=(1-r_j)R_j,
\qquad
R_j-R_{j-1}=r_jR_j.
\]

Thus the right tail is exactly telescoping at the joint-law level. Summing over `i` and using the analogous left telescoping bound

\[
\sum_i r_iL_i\le1
\]

proves finiteness.

To obtain vanishing as `P->infinity`, note that

\[
R_{J(i)}=\prod_{p>p_i^A}(1-p^{-1/2})
\]

when the finite label truncation is sent to infinity. Since

\[
\sum_{p>x}p^{-1/2}=\infty,
\]

the infinite right survival equals zero for every fixed `i`. For a finite truncation `k`, the mass is a probability and monotone in `k`; passing to the infinite source gives zero mass to the event that a selected Bernoulli family has a finite least owner and a greatest owner exceeding every prescribed power of it.

The useful finite-scale interpretation is instead conditional: after restricting to labels active at a physical endpoint `X`, the right survival beyond `p_i^A` is the probability that no active label larger than the candidate greatest owner is selected. The joint law therefore never pays the divergent sum of one-sided owner marginals.

## Boundary

This theorem controls only the **probability weight** of extreme owner pairs. It does not control the amplitude of the corresponding collar scalar `H_(ij)(X)`. A conclusion-facing estimate still requires a pointwise or mean-square collar certificate whose growth is compatible with the joint survival. No such amplitude theorem is claimed here.
