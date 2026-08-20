# L-102100 — The physical joint min–max hazard is a survival-weighted mixed coboundary

Claim ID: `L-102100`  
Status: **PROVED EXACT FINITE OPERATOR THEOREM**  
Created: 2026-08-21  
Depends on: PR #691 `L-100610/L-100616`; PR #695 `L-100700`  
RH status: **not assumed**

Let `U_1,...,U_k` be commuting shifts, let `0<r_i<1`, and put

\[
E_{a:b}=\prod_{h=a}^{b}(I-r_hU_h),
\qquad
L_i=\prod_{h<i}(1-r_h),
\qquad
R_j=\prod_{h>j}(1-r_h).
\]

Define the survival-weighted interval state

\[
\boxed{B_{ij}=L_iR_jE_{i:j}.}
\tag{L-102100.1}
\]

For `i<j`, the physical joint min–max hazard entry is

\[
H_{ij}=r_ir_jL_iR_j(I-U_i)(I-U_j)E_{i+1:j-1}.
\tag{L-102100.2}
\]

Then

\[
\boxed{
H_{ij}=B_{ij}-B_{i+1,j}-B_{i,j-1}+B_{i+1,j-1}.
}
\tag{L-102100.3}
\]

## Proof

Use

\[
L_{i+1}=(1-r_i)L_i,
\qquad
R_{j-1}=(1-r_j)R_j.
\]

After factoring `L_i R_j E_(i+1:j-1)`, the right side of (L-102100.3) becomes

\[
\begin{aligned}
&(I-r_iU_i)(I-r_jU_j)-(1-r_i)(I-r_jU_j)\\
&\quad -(1-r_j)(I-r_iU_i)+(1-r_i)(1-r_j)I\\
&=r_ir_j(I-U_i)(I-U_j).
\end{aligned}
\]

## Rectangle and staircase telescopes

For `a<=b<c<=d`,

\[
\boxed{
\sum_{i=a}^{b}\sum_{j=c}^{d}H_{ij}
=B_{a,d}-B_{b+1,d}-B_{a,c-1}+B_{b+1,c-1}.
}
\tag{L-102100.4}
\]

Let `m_i` be nondecreasing and sum the staircase
`a<=i<=b`, `m_i<=j<=d`. Then

\[
\boxed{
\begin{aligned}
\sum_i\sum_{j=m_i}^{d}H_{ij}
={}&B_{a,d}-B_{b+1,d}\\
&-\sum_{i=a}^{b}(B_{i,m_i-1}-B_{i+1,m_i-1}).
\end{aligned}
}
\tag{L-102100.5}
\]

The boundary increment is the literal first-owner trace

\[
\boxed{
B_{i,j}-B_{i+1,j}=r_iL_iR_j(I-U_i)E_{i+1:j}.
}
\tag{L-102100.6}
\]

Moreover

\[
\sum_i r_iL_i=1-\prod_i(1-r_i)\le1.
\tag{L-102100.7}
\]

Therefore a two-dimensional long-interval bulk may be collapsed to an oriented one-dimensional owner boundary with no owner-count loss. This does not sign the boundary current; it locates the correct remaining estimate.
