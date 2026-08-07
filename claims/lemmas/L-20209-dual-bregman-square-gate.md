# L-20209 — Dual Bregman square gate for the prime transport reserve

Claim ID: `L-20209`  
Title: The curvature penalty in the renormalized prime polygon is an exact dual Bregman divergence bounded by one centered prime-mass square  
Status: `PROPOSED — COMPLETE CONVEX-ANALYTIC PROOF; ARITHMETIC SQUARE BOUND OPEN`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `L-20208`  
Scope: every prime-power knot in the compact-cell dilation criterion

## 1. Exact duality

Let `H` be a differentiable strictly convex function, let

\[
 A=H'(\tau),
 \qquad p=H'(T),
\]

and write its Bregman divergence as

\[
 D_H(T,\tau)=H(T)-H(\tau)-H'(\tau)(T-\tau).
 \tag{1}
\]

The Legendre transform satisfies the exact dual identity

\[
\boxed{
 D_H(T,\tau)=D_{H^*}(A,p).}
 \tag{2}
\]

Indeed, `H*(H'(x))=xH'(x)-H(x)`, and direct substitution gives (2).

For the renormalized barrier

\[
 H=H_r,
 \qquad
 A=A_j,
 \qquad
 T=T_j=\log q_j,
 \qquad
 \tau=\tau_{r,j}=(H_r')^{-1}(A_j),
\]

`L-20208` therefore sharpens to

\[
\boxed{
 M_{r,j}
 =P_{r,j}-D_{H_r^*}
   \bigl(A_j,H_r'(T_j)\bigr),}
 \tag{3}
\]

where

\[
 P_{r,j}=H_r^*(A_j)-B_j
\]

is the prime-polygon transport reserve and `M_(r,j)` is the actual compact-cell knot value.

Thus the complete local defect is the dual reserve minus the convex cost of the centered prime-mass mismatch

\[
\boxed{
 \varepsilon_{r,j}=A_j-H_r'(T_j).}
 \tag{4}
\]

## 2. Sharp strong-convexity bound

Assume

\[
 H''(x)\ge m>0
\]

between `T` and `tau`. Then

\[
 (H^*)''(u)={1\over H''((H')^{-1}(u))}\le{1\over m}.
\]

Taylor's theorem with integral remainder gives

\[
\boxed{
 D_H(T,\tau)
 =D_{H^*}(A,p)
 \le{(A-p)^2\over2m}.}
 \tag{5}

Consequently the single scalar inequality

\[
\boxed{
 P_{r,j}
 \ge {\varepsilon_{r,j}^2\over2m_{r,j}}}
 \tag{6}
\]

is sufficient for `M_(r,j)>=0`, where `m_(r,j)` is any rigorous lower bound for `H_r''` on the interval joining `T_j` and `tau_(r,j)`.

This improves the earlier generic estimate involving both a lower and an upper curvature bound. Only strong convexity is required.

## 3. Explicit uniform curvature on the compact cell

For

\[
 H_r(T)=F(T)-r^2F(T/r)
\]

one has

\[
 H_r''(T)=F''(T)-F''(T/r).
 \tag{7}
\]

Fix `0<a<b<log 2`. Since `F''` is strictly increasing, for every `r` with `ra>b` and every `T in [ra,rb]`,

\[
\boxed{
 H_r''(T)
 \ge m_r:=F''(ra)-F''(b)>0.}
 \tag{8}
\]

Hence the production-ready gate is

\[
\boxed{
 H_r^*(A_j)-B_j
 \ge
 {\bigl[A_j-H_r'(T_j)\bigr]^2
  \over2\,[F''(ra)-F''(b)]}.}
 \tag{9}

Every term is a scalar interval:

- `A_j,B_j` are exact prime-power prefix moments;
- `T_j=log q_j` is one directed logarithm;
- `F',F''` are explicit archimedean/Lerch functions;
- `H_r*(A_j)` is obtained from one monotone inverse of `H_r'`.

## 4. Selberg-energy interface

The numerator in (9) is the square of the centered cumulative prime-mass discrepancy

\[
 A_j-H_r'(T_j).
\]

This is precisely the type of quadratic quantity retained by Selberg's symmetry formula and by the finite prime-pair energy of PR #216. The bridge is now exact:

```text
prime-pair / Selberg square
    controls
centered mass mismatch squared
    divided by
renormalized archimedean curvature
    and paid by
prime-polygon transport reserve.
```

A proof need not control each prime arrival by absolute value. It may accumulate a positive block reserve through `L-20208.17` and spend that reserve on the quadratic penalties (9).

## 5. Block certificate

For a consecutive block of knots `p<j<=q`, let

\[
 \Delta P_{p,q}
 =\int_{A_p}^{A_q}
  [\tau_r(A)-\nu_{pp}(A)]\,dA
\]

be the exact transport increment from `L-20208`. If a directed certificate proves

\[
 P_{r,p}+\Delta P_{p,j}
 \ge
 {\varepsilon_{r,j}^2\over2m_r}
 \qquad(p<j\le q),
 \tag{10}
\]

then every knot in that block is nonnegative. Endpoint rows are checked directly.

A cofinal block partition satisfying (10) up to a total `e^(o(r))` shortfall proves the prime-positive compact-cell criterion and therefore RH.

## 6. Proof boundary

- The Bregman duality and square bound are exact.
- No Selberg or prime-pair estimate strong enough for (9) is proved here.
- The reserve `P_(r,j)` itself may be negative; the square gate is a sufficient, not necessary, route.
- A finite collection of passing blocks has no cofinal consequence.
