# L-91720 — The optimal moving Cauchy node gives a sharp one-over-height zero moat

Claim ID: `L-91720`  
Status: **PROVED EXACT OPTIMIZED GREEN-MOAT THEOREM**  
Created: 2026-08-13  
Depends on: `L-91520/L-91620`  
RH status: **unproved**

## 1. One-zero charge

For a crossed-zero coordinate

\[
\zeta=x+iy,\qquad 0<x<\frac12,
\]

the fixed-node Clark/Green charge is

\[
g_\eta(\zeta)
=
\log
\frac{(\eta+x)^2+y^2}
     {(\eta-x)^2+y^2}.
\]

`L-91620` gives

\[
g_\eta(\zeta)
\ge
\frac{4\eta x}
     {(\eta+x)^2+y^2}.
\tag{L-91720.1}
\]

## 2. Depth-height box

Fix

\[
0<\delta\le x\le b<\frac12,
\qquad
|y|\le Y.
\]

Then

\[
\boxed{
g_\eta(\zeta)
\ge
m_{\delta,b,Y}(\eta)
:=
\frac{4\eta\delta}
     {(\eta+b)^2+Y^2}.
}
\tag{L-91720.2}
\]

This lower bound is uniform for the whole box.

## 3. Exact optimal node

Differentiating (L-91720.2), its unique maximum occurs at

\[
\boxed{
\eta_*(b,Y)=\sqrt{b^2+Y^2}.
}
\tag{L-91720.3}
\]

At that node,

\[
\boxed{
m_{\delta,b,Y}^*
=
\frac{2\delta}
     {\sqrt{b^2+Y^2}+b}.
}
\tag{L-91720.4}
\]

For fixed `delta,b`,

\[
m_{\delta,b,Y}^*
=
\frac{2\delta}{Y}
+O_{\delta,b}(Y^{-2}).
\tag{L-91720.5}
\]

The best fixed node has only an `O(Y^-2)` moat; allowing the node to move
recovers the sharp `O(Y^-1)` scale.

## 4. Counting consequence

Let `Z_(a,b)(delta,Y)` be the crossed zeros in one annulus whose depths lie in
`[delta,b]` and whose heights have absolute value at most `Y`, counted with
multiplicity. Then

\[
\boxed{
\# Z_{a,b}(\delta,Y)
\le
\frac{
\Lambda_{a,b}^{\rm ann}(\eta_*(b,Y))
}{
m_{\delta,b,Y}^*
}.
}
\tag{L-91720.6}
\]

The result is immediate because the annular entropy is the sum of the
individual positive charges.

## 5. Safe arithmetic node

For the horizontal quotient at scale `a<1/2`, every node `eta>=1` places the
two real source samples in the absolutely convergent half-plane. For
`Y>=sqrt(1-b^2)`, the optimal node satisfies `eta_*(b,Y)>=1`.

At smaller heights one may use `eta=1`; the moving-node theorem is aimed at
the cofinal high-height regime.

## 6. Exact boundary

```text
boxwise fixed-node moat                    EXACT
optimal moving node                        EXACT
optimized moat ~ 2 delta/Y                 EXACT
zero-count bound from annular entropy      EXACT
source-identified entropy upper bound      OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVED
```
