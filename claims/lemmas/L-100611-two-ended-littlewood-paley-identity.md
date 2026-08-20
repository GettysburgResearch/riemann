# L-100611 — Exact two-ended Littlewood–Paley identity

Claim ID: `L-100611`  
Status: **PROVED EXACT HILBERT-SPACE IDENTITY**  
Created: 2026-08-20  
Depends on: PR #660 `L-99720`; `L-100610`  
RH status: **not assumed**

Let `H` be a Hilbert space, let `U_1,...,U_k` be commuting isometries, and use

\[
E_{a:b}=\prod_{h=a}^{b}(I-r_hU_h),
\qquad
\Delta_i=I-U_i,
\]

with `0<r_i<1`. Put

\[
L_i=\prod_{h<i}(1-r_h),
\qquad
R_i=\prod_{h>i}(1-r_h),
\qquad
s=\prod_{h=1}^{k}(1-r_h).
\tag{L-100611.1}
\]

Then for every `f in H`,

\[
\boxed{
\begin{aligned}
\|E_{1:k}f\|^2
={}&s^2\|f\|^2\\
&+\sum_{i=1}^{k}
 r_iL_i^2R_i^2\,\|\Delta_i f\|^2\\
&+\sum_{1\le i<j\le k}
 r_ir_jL_i^2R_j^2\,
 \|\Delta_i\Delta_jE_{i+1:j-1}f\|^2.
\end{aligned}
}
\tag{L-100611.2}
\]

This is the energy counterpart of the two-ended hazard identity. Every
unresolved square is attached to one finite interval between an explicit least
and greatest owner.

## Full ANOVA form

The one-prime identity

\[
\|(I-rU)g\|^2
=(1-r)^2\|g\|^2+r\|(I-U)g\|^2
\tag{L-100611.3}
\]

may be iterated in all coordinates because the shifts and differences commute.
It gives

\[
\boxed{
\|E_{1:k}f\|^2
=
\sum_{S\subseteq[k]}
\left(\prod_{i\in S}r_i\right)
\left(\prod_{i\notin S}(1-r_i)^2\right)
\|\Delta_S f\|^2.
}
\tag{L-100611.4}
\]

Group the empty set, the singleton sets, and the sets of size at least two by
`i=min S`, `j=max S`. For fixed `i<j`, the interior sum is

\[
\begin{aligned}
&\sum_{S\subseteq\{i+1,\ldots,j-1\}}
 \left(\prod_{h\in S}r_h\right)
 \left(\prod_{h\notin S,\ i<h<j}(1-r_h)^2\right)
 \|\Delta_i\Delta_j\Delta_Sf\|^2\\
&\qquad=
\|E_{i+1:j-1}\Delta_i\Delta_jf\|^2
\end{aligned}
\]

by applying (L-100611.3) on the interior interval. This proves
(L-100611.2).

## Survival-vector bounds

Define

\[
a_i=\sqrt{r_i}\,L_i,
\qquad
b_i=\sqrt{r_i}\,R_i.
\tag{L-100611.5}
\]

Then

\[
\boxed{
\sum_i a_i^2\le1,
\qquad
\sum_i b_i^2\le1.
}
\tag{L-100611.6}
\]

Indeed,

\[
L_i^2-L_{i+1}^2
=(2r_i-r_i^2)L_i^2
\ge r_iL_i^2=a_i^2,
\]

and summation telescopes; the right-survival statement is the reversed
identity.

These norm-one endpoint vectors are the exact reason a two-sided Schur estimate
can combine first-owner and largest-owner information without paying the
number of active prime labels.

## Scope firewall

Equation (L-100611.2) is an identity in a Hilbert space on which all `U_i` are
isometries. A source-blind map from the free labelled space to one physical
scalar need not be contractive; the prime-interval separator of PR #660 remains
binding. The use of (L-100611.2) in the implication matrix is therefore through
an explicit interval collapse operator and a two-sided Schur test, not through
an unproved generic collapse.