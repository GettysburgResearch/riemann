# L-95040 — Root completion is exactly the signed interior carry span

Claim ID: `L-95040`  
Status: **PROPOSED COMPLETE EXACT FINITE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: PR #272 at `fa787eed202aef67b2a4e23a64aeedfb05f93645`, especially the node-divergence/carry equivalence; PR #474 at `da557977e6d496cdc395c823e0c8c2aa830ee3e1`, especially the root source in `L-93021`  
Scope: real signed quarter-balanced split flows whose children are at least two; no positivity, cofinal estimate, or RH conclusion

## 1. Interior split space

Fix `X>=6`. Let `E_X^circ` contain the unordered quarter-balanced splits

\[
e=(n,j),\qquad 4\le n\le X,\qquad
2\le j\le n-j,\qquad 4j\ge n.
\]

Its node-divergence column is

\[
B_e=e_n-e_j-e_{n-j}.
\]

Every such column has zero node-one coordinate and conserves size:

\[
(B_e)_1=0,
\qquad
\sum_m m(B_e)_m=0.
\]

Put

\[
\mathcal V_X^
=\left\{r\in\mathbb R^X:
 r(1)=0,
 \ \sum_{m=1}^Xmr(m)=0
\right\}.
\]

We prove

\[
\boxed{
\operatorname{span}_{\mathbb R}\{B_e:e\in E_X^\circ\}
=\mathcal V_X.
}
\tag{L-95040.1}
\]

Thus the dyadic root coordinate is the only linear obstruction to using no unit child.

## 2. Canonical trees terminating at nodes two and three

Define signed-flow trees recursively:

\[
T_2=T_3=0,
\]

and for `n>=4`, with

\[
j_n=\lfloor n/2\rfloor,
\qquad k_n=\lceil n/2\rceil,
\]

put

\[
T_n=[n,j_n]+T_{j_n}+T_{k_n}.
\tag{L-95040.2}
\]

Every edge is quarter-balanced and has both children at least two. Induction gives unique nonnegative integers `a_n,b_n` with

\[
2a_n+3b_n=n
\]

and

\[
\boxed{
\partial T_n=e_n-a_ne_2-b_ne_3.
}
\tag{L-95040.3}
\]

Two legal decompositions of node six are

\[
T_6^{(3,3)}=[6,3],
\]

and

\[
T_6^{(2,4)}=[6,2]+[4,2].
\]

Their difference

\[
C_6=T_6^{(3,3)}-T_6^{(2,4)}
\]

has

\[
\boxed{
\partial C_6=3e_2-2e_3.
}
\tag{L-95040.4}
\]

This is the unique size-zero direction on the two terminal nodes.

## 3. Explicit signed decoder

Let `r in V_X`. Form

\[
D_0=\sum_{n=4}^Xr(n)T_n.
\]

Set

\[
A=\sum_{n=4}^Xa_nr(n),
\qquad
B=\sum_{n=4}^Xb_nr(n).
\]

Then

\[
\partial D_0
=\sum_{n=4}^Xr(n)e_n-Ae_2-Be_3.
\]

The terminal mismatch is

\[
\Delta_2=r(2)+A,
\qquad
\Delta_3=r(3)+B.
\]

Size conservation and `2a_n+3b_n=n` give

\[
2\Delta_2+3\Delta_3=0.
\]

Therefore

\[
\tau={\Delta_2\over3}=-{\Delta_3\over2}
\]

is well defined, and

\[
\boxed{
D(r)=D_0+\tau C_6
}
\tag{L-95040.5}
\]

satisfies

\[
\boxed{
\partial D(r)=r.
}
\tag{L-95040.6}
\]

This proves the reverse inclusion in (L-95040.1). The construction is triangular, finite, and uses no arithmetic estimate.

## 4. Carry-coordinate corollary

Let `t(q)` be any finite carry target and `r^(t)` its exact multiples-Möbius node divergence. Retain the two-contact source

\[
b_2=(\varepsilon-\delta_2)*\mu.
\]

The root identity from PR #474/PR #326 is

\[
\rho_2(t):=\sum_qb_2(q)t(q)=r^{(t)}(1).
\]

Hence

\[
\boxed{
\rho_2(t)=0
\iff
r^{(t)}\text{ has an exact signed realization using only }E_X^\circ.
}
\tag{L-95040.7}
\]

The root completion introduced on PR #474 is therefore exactly the correct algebraic operation for removing unit-child edges. No additional signed-span obstruction remains.

## 5. What this does not prove

The decoder (L-95040.5) is signed. Its coefficients inherit the signs of the source and of the terminal correction. It gives no positive fragmentation and no capacity estimate.

The positive CRCTP theorem is therefore a genuine cone-membership theorem, not missing linear algebra.

## 6. Proof boundary

Established exactly:

1. complete characterization of the signed interior split span;
2. explicit quarter-balanced two-leaf decoder;
3. exact terminal correction through one six-node cycle;
4. equivalence between dyadic root completion and signed interior realizability.

Open:

1. positivity for the actual root-completed critical target;
2. subpower capacity debt;
3. RH.
