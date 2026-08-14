# L-91670 — The joint stopped-leaf producer is an exact finite rational cone problem

Claim ID: `L-91670`  
Status: **PROVED EXACT FINITE PRIMAL/DUAL REDUCTION**  
Created: 2026-08-14  
Motivation: PR #456 refutes the branchwise no-upward Hall producer used by PRs #451 and #455  
RH status: **unproved**

## 1. Frozen stopped-leaf datum

Fix one stopped least-prime leaf with parameters

\[
 p\ge67,
 \qquad 1\le y<67,
\]

one `P_61` Boolean source label, and one finite physical row cutoff large enough to contain every active row and capacity column of that leaf.

Let the exact signed leaf datum be the vector

\[
 d=(t,s,r,o,h,e),
\]

where

```text
t  target coordinates;
s  native-score coordinates;
r  literal component-row coordinates;
o  ordinary-column capacities;
h  radix-four detail capacities;
e  shared endpoint-port capacities.
```

All coordinates are real algebraic numbers in the frozen finite model.  After adjoining explicit square-root variables or directed rational enclosures, they may be represented by exact rational inequalities.

Let

\[
 v_1,\ldots,v_N
\]

be the complete finite list of allowed nonnegative physical packet templates.  Write

\[
 v_k=(t_k,s_k,r_k,o_k,h_k,e_k).
\]

The list may mix survival and hazard templates.  No branchwise Hall order is imposed.

## 2. Joint producer definition

A **joint stopped-leaf producer** is a coefficient vector

\[
 x=(x_1,\ldots,x_N)\ge0
\]

and a target-null row bonus

\[
 b\ge0
\]

such that

\[
 \sum_kx_kt_k=t,
 \tag{L-91670.1}
\]

\[
 \sum_kx_ks_k\ge s,
 \tag{L-91670.2}
\]

\[
 \sum_kx_kr_k+b=r,
 \tag{L-91670.3}
\]

\[
 \sum_kx_ko_k\le o,
 \tag{L-91670.4}
\]

\[
 \sum_kx_kh_k\le h,
 \tag{L-91670.5}
\]

\[
 \sum_kx_ke_k\le e.
 \tag{L-91670.6}
\]

Every source label is represented in the template index.  Thus source disjointness is encoded before projection and cannot be repaired after the fact.

The row bonus is eliminated by (L-91670.3): it exists with `b>=0` exactly when

\[
 \sum_kx_kr_k\le r.
 \tag{L-91670.7}
\]

Hence a joint producer exists precisely when one nonnegative vector `x` satisfies target equality, score superordination and all row/capacity subordinations simultaneously.

## 3. Matrix normal form

Collect target equalities into a rational matrix `B` and vector `b_0`, and all score, row, ordinary, detail and port inequalities into a rational matrix `G` and vector `c_0`, after reversing signs where necessary.  Then (L-91670.1)--(L-91670.7) are equivalent to

\[
 \boxed{
 Bx=b_0,
 \qquad
 Gx\le c_0,
 \qquad
 x\ge0.
 }
 \tag{L-91670.8}
\]

This is one finite rational polyhedron.

The equality and inequality rows must be generated from the same native normalization.  Separate feasibility checks against copies of the parent budget do not imply (L-91670.8).

## 4. Exact Farkas alternative

Introduce nonnegative slack variables `u>=0` and write

\[
 Gx+u=c_0.
\]

The system becomes

\[
 \begin{pmatrix}B&0\\G&I\end{pmatrix}
 \binom xu
 =
 \binom{b_0}{c_0},
 \qquad
 x,u\ge0.
 \tag{L-91670.9}
\]

By the rational Farkas lemma, exactly one of the following holds.

### Primal certificate

There are rational vectors

\[
 x\ge0,
 \qquad u\ge0
\]

satisfying (L-91670.9).  They are a finite proof object for the complete joint producer.

### Dual separator

There are rational vectors `lambda` and `z` such that

\[
 B^T\lambda+G^Tz\ge0,
 \qquad z\ge0,
 \tag{L-91670.10}
\]

but

\[
 \boxed{
 b_0^T\lambda+c_0^Tz<0.
 }
 \tag{L-91670.11}
\]

The separator is an exact obstruction: every allowed nonnegative packet has nonnegative dual cost, while the required stopped-leaf datum has negative cost.

Thus the stopped-leaf producer is fail closed.  There is no third outcome.

## 5. Why the PR #456 counterexample does not settle the joint cone

A branchwise no-upward Hall transport imposes additional restrictions:

```text
survival and hazard are projected separately;
edges must respect one prescribed order;
each branch satisfies its own Hall prefixes.
```

Those restrictions define a proper subcone of (L-91670.8).  PR #456 proves that the survival no-upward subcone is empty at

\[
 p=67,
 \qquad y=13,
 \qquad t=13.
\]

It does **not** prove that the complete joint cone (L-91670.8) is empty.  A mixed survival-hazard producer may compensate a negative branch prefix while remaining exact in the summed target and nonnegative in literal row and physical capacity.

Conversely, the failure of one branchwise Hall prefix means that no theorem may infer joint feasibility merely from the old Hall certificate.

## 6. Finite global reduction

For fixed `P_61` there are only finitely many Boolean labels and finitely many terminal parameters `1<=y<67`.  The rough prime remains unbounded through

\[
 r=p^{-1/2}\in(0,67^{-1/2}].
\]

On every fixed activation cell, each coefficient in (L-91670.8) is an algebraic-rational function of `r`.  Therefore a global proof may proceed by:

1. decomposing the compact interval `0<=r<=67^{-1/2}` into finitely many activation cells;
2. producing one rational primal certificate whose slack remains positive on each cell; or
3. producing an exact dual separator on a failing cell.

A certificate with directed positive slack is uniform over every rough prime in that cell.

## 7. Consequence for the factor-54 route

If (L-91670.8) is certified for every stopped leaf and every source label, then the valid source-disjoint least-prime partition may sum the joint producers.  The exact native response identities and same-index child replacement may then be applied after the full current row is formed.

At that point the remaining proof obligations are the one-use outer/current normalization, the global fixed-67 score theorem, the terminal mass telescope and the frozen endpoint chain.

This lemma does not assert that the joint cone is feasible.  It proves that the post-Hall obstruction has been reduced to one explicit finite primal/dual theorem rather than an informal search for a new transport.

```text
branchwise no-upward Hall for all leaves          FALSE
joint stopped-leaf cone formulation               EXACT
finite rational primal/dual alternative           EXACT
actual joint cone feasibility                      OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVEN
```
