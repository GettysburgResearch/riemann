# R-100616 — The unbalanced one-sided owner-marginal Schur energy diverges

Claim ID: `R-100616`  
Status: **PROVED EXACT SCOPE REFUTATION**  
Created: 2026-08-20  
Depends on: `L-100610--L-100614`  
RH status: **not assumed**

Let the ordered future labels satisfy `p_i>=67`, with a second separately
labelled copy of `67`, and put

\[
r_i=p_i^{-1/2},\qquad
L_i=\prod_{h<i}(1-r_h),\qquad
a_i=\sqrt{r_i}L_i.
\]

For `i<j`, let

\[
H_{ij}(X)=
(I-U_{p_i})(I-U_{p_j})
\prod_{i<h<j}(I-r_hU_{p_h})\Psi(X),
\]

where

\[
\Psi(y)=64\begin{cases}
3y-y^{3/2},&0<y\le1,\\
3\sqrt y-1,&y\ge1.
\end{cases}
\]

Let `M_ij` be the nonnegative large-argument carrier of `L-100614` and
`\widetilde H_ij=H_ij-M_ij`.  The earlier candidate row energy was

\[
\mathfrak R_k(X)=
\sum_i a_i^2
\sum_{j>i}\sqrt{r_ir_j}\,|\widetilde H_{ij}(X)|.
\tag{R-100616.1}
\]

Then, for every fixed label `i`,

\[
\boxed{\mathfrak R_k(1)\longrightarrow\infty\qquad(k\to\infty).}
\tag{R-100616.2}
\]

Consequently the one-sided marginal gate `FOCR100610`, in the form using
(R-100616.1), is false and may not appear in the conclusion graph.

## Proof

At `X=1` every shifted argument is in the lower polynomial branch of `Psi`.
Finite expansion therefore gives

\[
\begin{aligned}
H_{ij}(1)
={}&192(1-p_i^{-1})(1-p_j^{-1})
 \prod_{i<h<j}(1-p_h^{-3/2})\\
&-64(1-p_i^{-3/2})(1-p_j^{-3/2})
 \prod_{i<h<j}(1-p_h^{-2}).
\end{aligned}
\tag{R-100616.3}
\]

The two interior products converge to strictly positive limits as `j` tends
to infinity.  Moreover, for `p_i>=67`,

\[
\prod_{h>i}(1-p_h^{-3/2})
\ge1-\sum_{h>i}p_h^{-3/2}
>1-\sum_{n\ge67}n^{-3/2}
>\frac34.
\]

Since the exponent-two product is at most one, (R-100616.3) has a strictly
positive limit.  In particular, there are constants `c_i>0` and `J_i` such
that

\[
H_{ij}(1)>c_i\qquad(j\ge J_i).
\tag{R-100616.4}
\]

On the other hand the carrier is

\[
M_{ij}(1)=192(1-p_i^{-1/2})(1-p_j^{-1/2})
\prod_{i<h<j}(1-p_h^{-1}),
\]

and tends to zero by divergence of the prime harmonic series.  Hence, after
increasing `J_i`,

\[
|\widetilde H_{ij}(1)|>\frac{c_i}{2}.
\]

The `i`th summand in (R-100616.1) is therefore bounded below by

\[
\frac{c_i}{2}a_i^2\sqrt{r_i}
\sum_{J_i\le j\le k}\sqrt{r_j}
=
\frac{c_i}{2}a_i^2p_i^{-1/4}
\sum_{J_i\le j\le k}p_j^{-1/4},
\]

which diverges.  This proves (R-100616.2).

## Binding consequence

The joint coefficient

\[
\pi_{ij}=r_ir_jL_iR_j
\]

is stable because it retains both outside survivals.  Splitting it so that one
factor loses the entire right survival, or the other loses the entire left
survival, creates a nonphysical divergent obligation.  The corrected matrix
must keep the joint min--max measure until after the collar is factorized.