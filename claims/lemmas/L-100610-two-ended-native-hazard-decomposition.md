# L-100610 — Exact two-ended native hazard decomposition

Claim ID: `L-100610`  
Status: **PROVED EXACT POSITIVE-COEFFICIENT OPERATOR IDENTITY**  
Created: 2026-08-20  
Depends on: PR #652 `L-99601`; PR #691 `L-100605`  
RH status: **not assumed**

Let

\[
0<r_i<1,\qquad U_iU_j=U_jU_i,
\qquad 1\le i,j\le k,
\]

and put

\[
E_{a:b}=\prod_{h=a}^{b}(I-r_hU_h),
\qquad
\Delta_i=I-U_i,
\]

with an empty product equal to `I`. Define the left and right survival factors

\[
L_i=\prod_{h<i}(1-r_h),
\qquad
R_i=\prod_{h>i}(1-r_h),
\qquad
s=\prod_{h=1}^{k}(1-r_h).
\tag{L-100610.1}
\]

Then

\[
\boxed{
\begin{aligned}
E_{1:k}
={}&sI
 +\sum_{i=1}^{k} r_iL_iR_i\,\Delta_i\\
&+\sum_{1\le i<j\le k}
 r_ir_jL_iR_j\,
 \Delta_i\Delta_jE_{i+1:j-1}.
\end{aligned}
}
\tag{L-100610.2}
\]

Every scalar coefficient in (L-100610.2) is nonnegative. The only signed
operator left inside an off-diagonal term is the Euler product on the finite
prime interval `(i,j)`.

## Proof by a Bernoulli difference expansion

For one label,

\[
I-r_iU_i=(1-r_i)I+r_i(I-U_i).
\tag{L-100610.3}
\]

Expanding the product of (L-100610.3) gives

\[
E_{1:k}
=
\sum_{S\subseteq[k]}
\left(\prod_{i\in S}r_i\right)
\left(\prod_{i\notin S}(1-r_i)\right)
\Delta_S,
\qquad
\Delta_S=\prod_{i\in S}\Delta_i.
\tag{L-100610.4}
\]

The empty subset gives `sI`. A singleton `S={i}` gives
`r_iL_iR_i Delta_i`. For `|S|>=2`, group the subset by

\[
i=\min S,\qquad j=\max S.
\]

The labels outside `[i,j]` must use the survival branch, the two endpoints
must use the difference branch, and summing over all choices inside `(i,j)`
gives

\[
\prod_{i<h<j}\bigl[(1-r_h)I+r_h\Delta_h\bigr]
=
\prod_{i<h<j}(I-r_hU_h)
=E_{i+1:j-1}.
\]

This proves (L-100610.2).

## Row and column marginals

The off-diagonal row with fixed least owner `i` satisfies

\[
R_i\Delta_i
 +\sum_{j>i}r_jR_j\Delta_i\Delta_jE_{i+1:j-1}
=
\Delta_iE_{i+1:k}.
\tag{L-100610.5}
\]

Consequently the complete `i`th row of (L-100610.2) is precisely

\[
r_iL_i\Delta_iE_{i+1:k},
\]

the sequential first-owner current of `L-99601`. Reversing the order gives the
column identity

\[
L_j\Delta_j
 +\sum_{i<j}r_iL_i\Delta_i\Delta_jE_{i+1:j-1}
=
\Delta_jE_{1:j-1}.
\tag{L-100610.6}
\]

Thus the first-owner and largest-owner decompositions are not competing route
choices. They are the row and column marginals of one positive two-ended
hazard tensor.

## Difference from the direct min/max monomial tensor

`L-100605` partitions native Euler monomials uniquely by their least and
greatest selected labels. Equation (L-100610.2) instead expands each local
Euler factor into a survival branch and a difference branch. It is a positive
operator decomposition, not a second claim of unique occurrence ownership.
The two tensors share the same finite interval core and are used for different
purposes:

```text
direct min/max tensor      coefficient provenance and exact source ownership;
two-ended hazard tensor    positivity, Jensen, and two-sided energy estimates.
```

No analytic estimate or form of RH enters this identity.