# L-90431 — The complete bottom prefix is a sixteen-state Möbius Green map

Claim ID: `L-90431`  
Title: Column-one deletion forces the total Möbius-adjoint mass to vanish, so the first fifteen carry-inverse coefficients and PBVG depend only on sixteen explicit samples of one Möbius Green state  
Status: **PROPOSED COMPLETE EXACT FINITE-STATE REDUCTION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: the average-carry inverse formula of PR #329; corrected `T-90421`; finite Möbius inversion  
Scope: exact finite algebra; no positivity, PBVG, or RH conclusion

## 1. Möbius-adjoint coordinates

Let `w(2),...,w(X)` be a finite target and extend it by

\[
w(1)=0.
\tag{L-90431.1}
\]

Define

\[
\boxed{
u_m=\sum_{k\le X/m}\mu(k)w(mk).}
\tag{L-90431.2}
\]

Finite switching gives

\[
\begin{aligned}
\sum_{m=1}^Xu_m
&=\sum_{q=1}^Xw(q)\sum_{m\mid q}\mu(q/m)\\
&=w(1)=0.
\end{aligned}
\]

Hence

\[
\boxed{
\sum_{m=1}^Xu_m=0.
}
\tag{L-90431.3}
\]

This identity is the exact algebraic effect of deleting the carry column one.

## 2. Finite-prefix form of the triangular inverse

For the unique average-carry inverse coefficients, PR #329 gives

\[
 c(j)=\frac{
 (j+1)[j u_j-(j-2)u_{j+1}]
 +2\sum_{m=j+2}^Xu_m
 }{j(j-1)}.
\tag{L-90431.4}
\]

Using (L-90431.3),

\[
\boxed{
 c(j)=\frac{
 (j+1)[j u_j-(j-2)u_{j+1}]
 -2\sum_{m=1}^{j+1}u_m
 }{j(j-1)}.
}
\tag{L-90431.5}
\]

Therefore the entire prefix

\[
(c(2),c(3),\ldots,c(15))
\]

is a fixed rational linear image of

\[
(u_1,u_2,\ldots,u_{16}).
\]

No tail variable survives.

## 3. Critical hinge specialization

For

\[
w_X(q)=q^{-1/2}\log(X/q),\qquad q\ge2,
\]

let `Phi` be the canonical state of `L-90430`. Then

\[
\boxed{
u_1(X)=\Phi(X)-\log X,}
\tag{L-90431.6}
\]

and

\[
\boxed{
u_m(X)=m^{-1/2}\Phi(X/m),\qquad2\le m\le16.}
\tag{L-90431.7}
\]

Thus every coordinate entering PBVG is an explicit sample of one function at the sixteen rational scales

\[
X,\ X/2,\ldots,X/16.
\]

## 4. Exact finite cone for PBVG

Let `A` denote the rational `14 x 16` matrix defined by (L-90431.5), and let `S_m<0` be the suffix weights of `L-90428`. Put

\[
c=A u.
\tag{L-90431.8}
\]

Then PBVG is exactly the finite piecewise-linear condition

\[
(Au)_2\ge0,
\tag{L-90431.9}
\]

\[
\boxed{
\sum_{m=3}^{15}(-S_m)
 [(Au)_{m-1}-(Au)_m]_+
 \le\sigma_*(Au)_2.
}
\tag{L-90431.10}

No infinite carry state remains in this formulation.

A proof may therefore proceed by finding a forward-invariant polyhedral or quadratic cone for the sixteen Green samples under the exact positive renewal (L-90430.8). Such an invariant is not supplied here.

## 5. Why this is not already RH

Although the state dimension is fixed, the entries `Phi(X/m)` retain the complete reciprocal-zeta spectrum. Finite dimensionality of the observation does not imply a scale-uniform invariant. In particular, replacing (L-90431.10) by a numerical scan or by unrestricted norm equivalence would be invalid.

## 6. Proof boundary

Closed exactly here:

1. zero total adjoint mass;
2. removal of the infinite inverse tail;
3. fixed `14 x 16` bottom-prefix map;
4. sixteen-sample critical specialization;
5. exact finite PBVG cone.

Open:

1. a scale-invariant cone for the Green samples;
2. PBVG;
3. RH.
