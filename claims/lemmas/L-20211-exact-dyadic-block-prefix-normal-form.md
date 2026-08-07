# L-20211 — Exact dyadic-block prime-prefix normal form

Claim ID: `L-20211`  
Title: The first-knot corrected defect is one baseline plus a stream of nonnegative ramps inside `[2^r,2^(r+1)]`  
Status: `PROPOSED — COMPLETE FINITE IDENTITY`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `T-20208`; the prefix moments of `L-20201/L-20208`  
Scope: every integer `r>=2`

## 1. Fixed cell coordinate

Put

\[
 T_0=r\log2,
 \qquad
 T=T_0+u,
 \qquad
 0\le u\le\log2,
\]

so that

\[
 x=e^T=2^re^u
 \in[2^r,2^{r+1}].
\]

The corrected defect of `T-20208` is

\[
\boxed{
 \widetilde{\mathcal D}_r(T/r)
 =G(T)-H_r(T),}
 \tag{1}

where

\[
 G(T)=\sum_{q\le e^T}{\Lambda(q)\over\sqrt q}(T-\log q)
\]

and

\[
 H_r(T)=F(T)-r^2F(T/r).
\]

## 2. Baseline and local ramps

Define the complete left-prefix moments

\[
 A_r^-=\sum_{q\le2^r}{\Lambda(q)\over\sqrt q},
 \qquad
 B_r^-=\sum_{q\le2^r}{\Lambda(q)\log q\over\sqrt q}.
 \tag{2}

Then

\[
 G(T_0)=A_r^-T_0-B_r^-.
 \tag{3}

For every prime power in the open dyadic block, put

\[
 \lambda_q=\log(q/2^r)\in(0,\log2).
 \tag{4}

The prime ramp has the exact local form

\[
\boxed{
 G(T_0+u)
 =G(T_0)+A_r^-u
 +\sum_{2^r<q\le2^re^u}
  {\Lambda(q)\over\sqrt q}(u-\lambda_q).}
 \tag{5}

Every newly arriving coefficient is nonnegative, and each new ramp begins at zero.

Consequently

\[
\boxed{
\begin{aligned}
 \widetilde{\mathcal D}_r((T_0+u)/r)
 ={}&M_r^-+A_r^-u\\
 &+\sum_{2^r<q\le2^re^u}
  {\Lambda(q)\over\sqrt q}(u-\lambda_q)\\
 &-\bigl[H_r(T_0+u)-H_r(T_0)\bigr],
\end{aligned}}
 \tag{6}

where

\[
 M_r^-=G(T_0)-H_r(T_0)
 =\widetilde{\mathcal D}_r(\log2).
 \tag{7}

Thus one finite block is generated from one left-endpoint margin and a monotone stream of nonnegative ramps.

## 3. Knot recurrence

List the block prime powers as

\[
 2^r<q_1<\cdots<q_m<2^{r+1}
\]

and put

\[
 u_j=\log(q_j/2^r),
 \qquad
 A_{r,j}=A_r^-+
 \sum_{i\le j}{\Lambda(q_i)\over\sqrt{q_i}}.
\]

At a knot, the arriving ramp is zero, so

\[
\boxed{
 M_{r,j}-M_{r,j-1}
 =A_{r,j-1}(u_j-u_{j-1})
 -\bigl[H_r(T_0+u_j)-H_r(T_0+u_{j-1})\bigr].}
 \tag{8}

Equivalently,

\[
\boxed{
 M_{r,j}-M_{r,j-1}
 =\int_{u_{j-1}}^{u_j}
  [A_{r,j-1}-H_r'(T_0+v)]\,dv.}
 \tag{9}

The mass of `q_j` affects only the derivative after the knot, never the value at its own arrival.

## 4. Directed streaming certificate

A proof-producing dyadic block may be streamed in increasing prime-power order. It needs to retain only:

1. the exact left-prefix pair `(A_r^-,B_r^-)`;
2. the current knot location and current cumulative mass;
3. a directed integral of `H_r'` across the next gap;
4. the current margin;
5. the complete duplicate-free block manifest.

No full matrix and no simultaneous storage of every previous prime term is necessary.

The equivalent dual implementation stores the transport reserve

\[
 P_{r,j}=H_r^*(A_{r,j})-B_{r,j}
\]

and charges the Bregman penalty from `L-20209`.

## 5. Taylor-adapted version

By `L-20210`, on the fixed coordinate `u in [0,log2]`,

\[
 r^2F\left(\log2+{u\over r}\right)
\]

is an explicit cubic polynomial in `(r,u)` plus an `O(r^-2)` interval. Therefore every archimedean increment in (8)--(9) has a fixed-width directed evaluator independent of a growing profile grid.

## 6. Proof boundary

- Equations (1)--(9) are exact.
- The identity does not prove that the streamed margins stay nonnegative.
- Left-prefix moments still contain all earlier prime powers; their exact provenance must be retained or independently regenerated.
- A finite block replay does not establish the cofinal criterion.
