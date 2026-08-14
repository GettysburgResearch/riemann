# L-91721 — Beyond row support, the Target-Lorenz margin is the complete signed row

Claim ID: `L-91721`  
Status: **PROVED EXACT SUPPORT REDUCTION; STRICT SIGN IMPORTS REVIEWED ROW THEOREMS**  
Created: 2026-08-14  
Depends on: `L-91684`; for strict positivity, `L-91346/L-91364`  
RH status: **unproved**

## 1. Setup

Fix

\[
 p\ge67,
 \qquad1\le y<67,
 \qquad x=py,
 \qquad2\le j\le66.
\]

Let `U` be the leftmost even target submeasure of exact odd target mass and let
`c` be its cutoff. The Target-Lorenz row margin is

\[
 \mathfrak L_j(p,y)=R_j(U)-O_R^{(j)}.
\tag{L-91721.1}
\]

## 2. Exact row support

The causal component atom is

\[
 K_R^{(j)}(d)
 =\frac1{\sqrt d}
 \left[Q_{x/d}(j)-p^{-1/2}Q_{y/d}(j)\right].
\]

Causal activation gives

\[
 Q_Y(j)=0\qquad(Y\le j).
\]

If `d>=x/j`, then `x/d<=j`; moreover

\[
 y/d\le\frac{y}{x/j}=\frac jp<j.
\]

Therefore

\[
\boxed{
 K_R^{(j)}(d)=0
 \qquad(d\ge x/j).
}
\tag{L-91721.2}
\]

All nonzero row source lies strictly to the left of `x/j`.

## 3. Cutoff beyond support

Assume

\[
\boxed{c\ge x/j.}
\tag{L-91721.3}
\]

By definition of the leftmost submeasure, every even source atom `e<c` is used
with coefficient one. Equation (L-91721.2) shows that this includes every even
atom with nonzero row. A possibly fractional cutoff atom has zero row whenever
`c=x/j`, and every atom beyond `c` has zero row.

Hence

\[
 R_j(U)=E_R^{(j)}.
\tag{L-91721.4}
\]

The odd row is already the complete odd demand, so

\[
\boxed{
 \mathfrak L_j(p,y)
 =E_R^{(j)}-O_R^{(j)}
 =\sum_{d\mid P_{61}}\mu(d)K_R^{(j)}(d).
}
\tag{L-91721.5}
\]

Thus no cutoff determinant remains in this regime.

## 4. Existing strict row inputs

If `j<=y`, the right side of (L-91721.5) is the inherited causal one-prime row
of `L-91346`, which has the directed lower bound

\[
 \mathfrak L_j(p,y)>\frac1{500}
\]

on its stated frozen inputs.

If `j>y`, the child row is inactive and (L-91721.5) is the canonical finite
Euler row

\[
 D_{P_{61},x}(j),
\]

which is strictly positive for `x>j` under `L-91364`. Here `x=py>=67>j`.

Therefore, subject to independent reconstruction of those retained row
theorems, every cell satisfying (L-91721.3) is strictly closed.

## 5. Reduced arithmetic frontier

The only Target-Lorenz cells not covered by this support reduction satisfy

\[
\boxed{c<x/j.}
\tag{L-91721.6}
\]

Since `c` is one of 185 even divisors below 2000, (L-91721.6) is a strong
quotient restriction for the remaining exact cell certificate.

## 6. Boundary

```text
causal row support d<x/j                      EXACT
cutoff beyond support -> complete signed row  EXACT
strict inherited sign                         IMPORTED / L-91346 REVIEW
strict child-inactive sign                    IMPORTED / L-91364 REVIEW
remaining cells c<x/j                         OPEN / FINITE-STRUCTURED
Riemann Hypothesis                            UNPROVEN
```
