# L-100616 — Exact joint min–max hazard decomposition and stable collar bound

Claim ID: `L-100616`  
Status: **PROVED EXACT FINITE IDENTITY AND CONVEX INEQUALITY**  
Created: 2026-08-20  
Depends on: `L-100610--L-100611`  
RH status: **not assumed**

Let `U_1,...,U_k` be commuting scale shifts and let `0<r_i<1`.  Put

\[
L_i=\prod_{h<i}(1-r_h),\qquad
R_i=\prod_{h>i}(1-r_h),\qquad
s_k=\prod_{h=1}^k(1-r_h),
\]

and

\[
E_{a:b}=\prod_{a\le h\le b}(I-r_hU_h).
\]

Then

\[
\boxed{
\begin{aligned}
E_{1:k}={}&s_kI
+\sum_{i=1}^k r_iL_iR_i(I-U_i)\\
&+\sum_{1\le i<j\le k}
 r_ir_jL_iR_j
 (I-U_i)(I-U_j)E_{i+1:j-1}.
\end{aligned}}
\tag{L-100616.1}
\]

Every coefficient in (L-100616.1) is nonnegative, and

\[
\boxed{
 s_k+\sum_i r_iL_iR_i+
 \sum_{i<j}r_ir_jL_iR_j=1.
}
\tag{L-100616.2}
\]

The three families in (L-100616.2) are respectively the probabilities that a
family of independent Bernoulli variables of parameters `r_i` has zero
successes, exactly one success at `i`, or least and greatest successes
`i<j`.  Thus the pair coefficient

\[
\pi_{ij}=r_ir_jL_iR_j
\tag{L-100616.3}
\]

is the literal joint min–max law; it must not be replaced by unrelated row and
column marginals.

## Convex observation inequality

Let `O` be any linear observation into a Hilbert space.  Applying `O` to
(L-100616.1) and Jensen's inequality gives

\[
\boxed{
\begin{aligned}
\|OE_{1:k}f\|^2\le{}&s_k\|Of\|^2
+\sum_i r_iL_iR_i\|O(I-U_i)f\|^2\\
&+\sum_{i<j}\pi_{ij}
 \|O(I-U_i)(I-U_j)E_{i+1:j-1}f\|^2.
\end{aligned}}
\tag{L-100616.4}
\]

For a real scalar observation, assume the root and singleton terms are
nonnegative.  Writing

\[
H_{ij}=O(I-U_i)(I-U_j)E_{i+1:j-1}f,
\]

one obtains the exact stable one-sided bound

\[
\boxed{
(OE_{1:k}f)_-
\le
\sum_{i<j}\pi_{ij}(H_{ij})_-.
}
\tag{L-100616.5}
\]

Because `sum_(i<j) pi_ij<=1`, this bound has no artificial owner-count or
one-sided-survival divergence.

## A genuine two-certificate AND gate

Suppose concrete nonnegative collar certificates `A_ij,B_ij` satisfy

\[
(H_{ij})_-^2\le A_{ij}B_{ij}.
\tag{L-100616.6}
\]

Define

\[
\mathcal A_k=\sum_{i<j}\pi_{ij}A_{ij},\qquad
\mathcal B_k=\sum_{i<j}\pi_{ij}B_{ij}.
\]

Cauchy--Schwarz on the joint probability space gives

\[
\boxed{
(OE_{1:k}f)_-
\le\sqrt{\mathcal A_k\mathcal B_k}.
}
\tag{L-100616.7}
\]

This is the correct logical shape for a first-owner/last-owner conjunction:
`A` and `B` must be two estimates of the same source-owned collar occurrence,
not two marginal sums obtained by deleting one of the survival factors.