# T-20206 — Curvature-corrected prime-transport criterion for RH

Claim ID: `T-20206`  
Title: RH is equivalent to eventual domination of every atomic Bregman cost by the renormalized prime-polygon transport reserve  
Status: `PROPOSED — COMPLETE COMPOSITION OF T-20205/L-20207/L-20208; TRANSPORT INEQUALITY OPEN`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `T-20205`; `L-20207`; `L-20208`; `L-20209`  
Scope: one fixed compact base cell before the first prime knot

## 1. Finite level

Fix

\[
 0<a<b<\log2.
\]

For each integer `r>=2`, put

\[
 I_r=[ra,rb],
 \qquad
 H_r(T)=F(T)-r^2F(T/r).
\]

Let

\[
 \mathcal K_r
 =\{ra,rb\}
  \cup\{\log q:q\text{ a prime power},\ e^{ra}\le q\le e^{rb}\}.
\]

For every interior prime-power knot `T_j=log q_j`, define

\[
 A_j=\sum_{q\le q_j}{\Lambda(q)\over\sqrt q},
 \qquad
 B_j=\sum_{q\le q_j}{\Lambda(q)\log q\over\sqrt q},
\]

\[
 \tau_{r,j}=(H_r')^{-1}(A_j),
 \qquad
 P_{r,j}=H_r^*(A_j)-B_j,
\]

and

\[
 \mathfrak C_{r,j}
 =D_{H_r}(T_j,\tau_{r,j}).
\]

Then

\[
\boxed{
 \mathcal D_r(T_j/r)
 =P_{r,j}-\mathfrak C_{r,j}.}
 \tag{1}
\]

The two endpoint values are evaluated directly from the complete finite prime formula.

By the strict concavity between knots proved in `L-20207`,

\[
\boxed{
 \inf_{a\le t\le b}\mathcal D_r(t)
 =\min\left\{
  \mathcal D_r(a),\mathcal D_r(b),
  \min_{T_j\in(ra,rb)}
   (P_{r,j}-\mathfrak C_{r,j})
 \right\}.}
 \tag{2}

Thus one finite level is decided entirely by two endpoint rows and finitely many scalar transport-minus-curvature rows.

## 2. Exact global equivalence

The compact-cell theorem `T-20205` now becomes

\[
\boxed{
\begin{aligned}
 RH\quad\Longleftrightarrow\quad
 &\mathcal D_r(a)\ge0,
 \quad \mathcal D_r(b)\ge0,\\
 &P_{r,j}\ge\mathfrak C_{r,j}
 \quad\text{for every prime-power knot in }I_r,
\end{aligned}}
 \tag{3}

for every sufficiently large integer `r`.

Equivalently, RH holds if and only if the negative part of the minimum in (2) is

\[
\boxed{e^{o(r)}.}
 \tag{4}

The implication from RH is the positive screw-square theorem. The converse is exactly the compact-cell covering and Landau argument of `T-20205`.

## 3. Sufficient square version

Let

\[
 m_r=F''(ra)-F''(b)>0
\]

for all sufficiently large `r`. By `L-20209`, it is enough to prove

\[
\boxed{
 P_{r,j}
 \ge
 {\bigl[A_j-H_r'(T_j)\bigr]^2\over2m_r}}
 \tag{5}

for every knot, together with the endpoint rows.

A relaxed cofinal version is also sufficient: for every `epsilon>0`, allow the right side of each final lower bound to miss by at most `C_epsilon e^(epsilon r)`, uniformly over all rows at level `r`.

This is the proof-facing theorem. It asks for a positive transport reserve to dominate a positive quadratic centered-prime discrepancy. It no longer asks for the sign of a cancellation between two exponentially large raw quantities.

## 4. Exact block formulation

Let `nu_pp(A)` be the prime-power quantile step function and

\[
 \tau_r(A)=(H_r')^{-1}(A).
\]

For a consecutive mass block `[A_p,A_q]`, define

\[
 \mathfrak T_{r;p,q}
 =\int_{A_p}^{A_q}
  [\tau_r(A)-\nu_{pp}(A)]\,dA.
 \tag{6}

Then

\[
 P_{r,q}=P_{r,p}+\mathfrak T_{r;p,q}.
 \tag{7}

Therefore a block certificate consists of:

1. one incoming reserve `P_(r,p)`;
2. one lower interval for every partial transport integral in the block;
3. one upper interval for each exact or square Bregman cost;
4. the two endpoint rows;
5. a complete, duplicate-free prime-power manifest.

Negative individual prime arrivals are permitted. Only cumulative transport and the final atomic-placement costs matter.

## 5. Relation to the other global routes

The theorem supplies a common scalar interface for three repository programs:

- PR #219: `P_(r,j)` is the renormalized prime-polygon reserve;
- PR #216: the square in (5) is a centered prime-mass/prime-pair energy target;
- PR #218: the resulting knot rows are the prime-positive dilation defects whose cofinal lower envelope implies RH.

Thus the full positive attack can now be stated as

```text
prime-mass transport reserve
    >=
curvature-normalized Selberg discrepancy square
    cofinally
    =>
RH.
```

This is not merely a dictionary. Equations (1)--(7) specify the exact finite proof object that would close the chain.

## 6. Proof boundary

- The equivalence and finite reduction inherit the proposed review status of the dependencies.
- No cofinal transport or Selberg-square domination is proved here.
- A phase-blind PNT remainder is too large for (5).
- Finite numerical success does not establish the eventual or `e^(o(r))` quantifier.
