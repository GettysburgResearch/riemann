# L-20702 — Rational Leja rows and a unit-diagonal growing zero frame

Claim ID: `L-20702`  
Title: Directed max-volume selection for the D-0001 frame reduces to one rational Leja pivot at each step  
Status: `PROPOSED — COMPLETE FINITE FRAME ALGORITHM; COFINAL METRIC RATE OPEN`  
Authoring agent: `gpt56-03-r`  
Created: 2026-08-01  
Dependencies: `L-20701`  
Scope: growing even packets and proof-producing row selection

## 1. Rational Newton basis

Let \(a_n=n^2\), and suppose distinct nonresonant zero nodes
\(x_0,x_1,\ldots\) are selected in this order. Define

\[
\Phi_0(x)=1,
\]

and for \(k\ge1\),

\[
\boxed{
\Phi_k(x)
=
\frac{\prod_{i=0}^{k-1}(x-x_i)}
     {\prod_{n=1}^{k}(x-a_n)}.
}
\tag{L-20702.1}
\]

Every \(\Phi_k\) lies in the Cauchy–Vandermonde space

\[
\operatorname{span}
\left\{
1,(x-a_1)^{-1},\ldots,(x-a_N)^{-1}
\right\}.
\]

The evaluation matrix is lower triangular:

\[
\Phi_k(x_i)=0\quad(i<k).
\]

Its diagonal is

\[
\boxed{
 d_k
 =\Phi_k(x_k)
 =
 \frac{\prod_{i<k}(x_k-x_i)}
      {\prod_{n=1}^k(x_k-a_n)}.
}
\tag{L-20702.2}
\]

Including the D-0001 row scalar, the actual triangular pivot is

\[
\boxed{p_k=s(x_k)d_k.}
\tag{L-20702.3}
\]

## 2. Exact determinant recursion

Let \(V_k\) be the square evaluation matrix of the first \(k+1\) rows on
\(\Phi_0,\ldots,\Phi_k\). Then

\[
\boxed{
\det V_k=\prod_{j=0}^kp_j.
}
\tag{L-20702.4}
\]

Consequently, after a fixed prefix \(x_0,\ldots,x_{k-1}\), appending a
candidate node \(x\) multiplies the absolute determinant by exactly

\[
\boxed{
\mathcal P_k(x)
=
|s(x)|
\left|
\frac{\prod_{i<k}(x-x_i)}
     {\prod_{n=1}^{k}(x-a_n)}
\right|.
}
\tag{L-20702.5}
\]

Thus the exact greedy max-volume rule is the rational Leja rule

\[
\boxed{x_k\in\arg\max_x\mathcal P_k(x).}
\tag{L-20702.6}
\]

There is no floating QR or SVD in the proof object.

## 3. Directed selection

For every candidate zero ball, interval arithmetic encloses:

- \(s(x)\);
- every difference \(x-x_i\);
- every pole separation \(x-a_n\);
- the resulting pivot \(p_k\).

A **directed max-volume decision** is certified when one candidate satisfies

\[
\underline{|p_k(x_*)|}
>
\max_{x\ne x_*}\overline{|p_k(x)|}.
\tag{L-20702.7}
\]

If the maximizer is not separated, retain all tied candidates and branch.
Any branch with nonzero pivots is valid. Maximality is an optimization, not a
soundness hypothesis.

## 4. Unit-diagonal scaling

Define

\[
\widetilde\Phi_k=p_k^{-1}\Phi_k.
\]

Then the directed evaluation matrix is lower triangular with exact unit
diagonal. Forward substitution uses only already certified nonzero pivots.
This removes the artificial loss caused by generic inversion of a raw Cauchy
matrix.

For a complete selected set, one may go further and use the rational cardinal
basis from `L-20701`; the complete evaluation matrix then becomes the identity.

## 5. Kernel-first form

For a packet of dimension \(N+1\) with a one-dimensional residual kernel,
select \(N\) first-frame nodes \(Z\). The exact kernel numerator is

\[
Q_Z(x)=\prod_{z\in Z}(x-z),
\]

and the kernel rational function is

\[
F_Z(x)=Q_Z(x)/P_N(x).
\]

The next Leja pivot is exactly the conditional second-frame evaluation

\[
\boxed{
p_N(y)=s(y)F_Z(y).}
\tag{L-20702.8}
\]

Hence one and the same product:

1. certifies completion of the full frame;
2. supplies the conditional selected-zero mass;
3. selects the best second frame among the available rows.

For a residual kernel of dimension \(r\), use the final \(r\) rational Newton
functions or their cardinalized version. Their determinant is the product of
the final \(r\) Leja pivots.

## 6. Metric conditioning is the only remaining frame cost

Let \(J_Z\) denote the explicit kernel basis in coefficient coordinates and
let \(G\) be the production metric. The frame lower endpoint is computed from

\[
G_K=J_Z^*GJ_Z
\]

and the conditional evaluation matrix. In a conditional cardinal basis it is

\[
\boxed{
\sigma_{Y\mid Z}^2
=\lambda_{\min}(G_K^{-1}).
}
\tag{L-20702.9}
\]

More generally it is the smallest generalized eigenvalue of
\(S^*M_YS\) against \(G_K\).

The correct proof procedure is therefore:

1. construct \(J_Z\) by products;
2. evaluate \(G_K\) directly;
3. certify its exact directed LDL or inverse bound;
4. never replace it by
   \(\|B^{-1}\|^2\|V_ZR\|^2\).

The raw first-frame condition number can grow by many orders of magnitude while
\(G_K\) or the normalized graph correction stays controlled. The raw condition
number is not a proof invariant.

## 7. Natural scaling insight

The normalized zero node is

\[
\mu=\frac{L\gamma}{2\pi}.
\]

Since the \(k\)-th zero scale is heuristically
\(\gamma_k\asymp2\pi k/\log k\), matching the zero nodes to the Fourier pole
lattice requires

\[
L\asymp\log N,
\qquad
c=e^L\asymp N^{O(1)}.
\]

The earlier calibration ladder used \(N\) much smaller than \(\log c\), placing
all zero nodes far beyond the pole band and creating severe raw conditioning.
This observation nominates polynomial support growth for production.

This paragraph is a scheduler, not an imported zero-spacing theorem. The exact
finite frame remains valid at every nonresonant support.

## 8. What is closed

The following are no longer blockers:

- generic inversion of the first-frame matrix;
- floating max-volume row selection;
- a condition-number estimate for the raw Cauchy coordinates;
- construction of the conditional second frame.

The remaining sign is the complete prime-side Schur pivot. By `L-20703`, no
choice of graph coordinates changes that pivot.
