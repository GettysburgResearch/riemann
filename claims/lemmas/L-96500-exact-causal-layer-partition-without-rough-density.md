# L-96500 — The factor-67 causal layer is an exact source partition and needs no rough-density estimate

Claim ID: `L-96500`  
Status: **PROVED EXACT FINITE ALGEBRA AND OWNERSHIP THEOREM**  
Created: 2026-08-17  
Frozen reconstruction source: PR #550, especially `L-96302`

Let `P_Z` be one positive labelled canonical packet. List its active rough
primes in increasing order

\[
67\le p_1<p_2<\cdots<p_k,
\]

and set

\[
r_i=p_i^{-1/2},\qquad
s_i=\prod_{h\le i}(1-r_h),\qquad s_0=1,
\]

\[
\lambda_i=r_i s_{i-1},\qquad
\alpha_i=r_i\lambda_i=r_i^2s_{i-1}.
\]

For the first-owner placement `A_{p_i}`, the exact causal identity is

\[
\boxed{
P_Z=s_kP_Z+
\sum_{i=1}^k\lambda_i
  \bigl(P_Z-r_iA_{p_i}P_{Z/p_i}\bigr)
+
\sum_{i=1}^k\alpha_iA_{p_i}P_{Z/p_i}.}
\tag{L-96500.1}
\]

Indeed,

\[
s_k+\sum_i\lambda_i=1
\]

by `s_{i-1}-s_i=lambda_i`, and the child terms cancel because
`alpha_i=r_i lambda_i`. Equation (L-96500.1) is therefore an identity in every
linear typed coordinate simultaneously: source, target, score, component row,
ordinary `q`, ordinary `4q`, and radix-four detail.

The source interpretation is literal:

* `s_kP_Z` is current positive source;
* each difference term is a paired source edge and is **not** separately
  observed as a positive child row;
* each `alpha_i A_{p_i}P_{Z/p_i}` is the sole unresolved positive child owned by
  the least active rough prime `p_i`;
* first-owner slices are disjoint, so no monomial enters two same-generation
  children.

The total unresolved coefficient satisfies

\[
\sum_i\alpha_i
 =\sum_i r_i\lambda_i
 \le r_1\sum_i\lambda_i
 <{1\over\sqrt{67}}<{1\over8}.
\tag{L-96500.2}
\]

This estimate depends only on `p_i>=67`; it makes no assertion about the number
or density of integers coprime to a prime prefix. Consequently the PR #552
rough-store counterexample is orthogonal to (L-96500.1)–(L-96500.2).

Finally, every unresolved child has scale at most `Z/67`. This well-founded
scale drop, rather than coefficient-mass convergence, is the termination
mechanism used below.
