# L-23811 — Universal one-pass balanced carry packing

Claim ID: `L-23811`  
Title: First differences of the prime ramp give an unconditional balanced carry packing with sharp one-stage constant `4 log 2`  
Status: **PROPOSED EXACT LEMMA — COMPLETE ELEMENTARY PROOF**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23808`  
Scope: unconditional positive partial packing; no RH claim

## 1. Construction

For an integer `X>=3`, put

\[
 w_X(q)=q^{-1/2}\log(X/q),
 \qquad 2\le q\le X,
 \tag{L-23811.1}
\]

and set `w_X(X+1)=0`. Since `w_X` is decreasing on `[2,X]`, the first
differences

\[
 \boxed{
 a_X(n)=w_X(n)-w_X(n+1)\ge0,
 \qquad 2\le n<X,}
 \tag{L-23811.2}
\]

are nonnegative.

Choose the central balanced split

\[
 j_n=\lfloor n/2\rfloor
 \tag{L-23811.3}
\]

and assign split flow

\[
 d_X(n,j_n)=a_X(n),
 \qquad d_X(n,j)=0\ (j\ne j_n).
 \tag{L-23811.4}
\]

## 2. Exact feasibility

Every atomized carry coefficient is either zero or one. Therefore, for every
column `q`,

\[
 \begin{aligned}
 L_q(d_X)
 &=\sum_{n=q}^{X-1}a_X(n)\chi_{n,j_n}(q)\\
 &\le\sum_{n=q}^{X-1}a_X(n)\\
 &=w_X(q).
 \end{aligned}
 \tag{L-23811.5}
\]

Thus

\[
 \boxed{d_X\ge0,\qquad L_q(d_X)\le w_X(q)}
 \tag{L-23811.6}
\]

for every finite endpoint. No Möbius estimate or asymptotic argument enters.

## 3. Entropy value

The central binomial estimate gives

\[
 \log\binom n{\lfloor n/2\rfloor}
 =n\log2+O(\log(n+1)).
 \tag{L-23811.7}
\]

Summation by parts gives exactly

\[
 \sum_{n=2}^{X-1}n\,[w_X(n)-w_X(n+1)]
 =2w_X(2)+\sum_{n=3}^{X-1}w_X(n).
 \tag{L-23811.8}
\]

Elementary integral comparison yields

\[
 \sum_{n=2}^{X-1}w_X(n)
 =4\sqrt X+O(\log X).
 \tag{L-23811.9}
\]

Moreover,

\[
 \sum_{n=2}^{X-1}a_X(n)\log(n+1)
 \le w_X(2)\log(X+1)
 =O((\log X)^2).
 \tag{L-23811.10}
\]

Combining the preceding identities,

\[
 \boxed{
 \sum_{n=2}^{X-1}a_X(n)
 \log\binom n{\lfloor n/2\rfloor}
 =4(\log2)\sqrt X+O((\log X)^2).}
 \tag{L-23811.11}
\]

The exact valuation identity of `L-23808` therefore gives the unconditional
prime-ramp bound

\[
 \boxed{
 \sum_{p^k\le X}\frac{\Lambda(p^k)}{\sqrt{p^k}}
 \log\frac X{p^k}
 \ge4(\log2)\sqrt X-O((\log X)^2).}
 \tag{L-23811.12}
\]

This is a genuine positive carry theorem, although its main constant is below
the critical value four.

## 4. General fixed split ratio

Fix `0<u<1`, choose `j_n=round(un)` with an endpoint convention keeping
`1<=j_n<n`, and use the same coefficients `a_X(n)`. The packing inequality
(L-23811.5) remains exact. Uniform Stirling estimates give

\[
 \boxed{
 \sum_na_X(n)\log\binom n{j_n}
 =4H(u)\sqrt X+O_u((\log X)^2),}
 \tag{L-23811.13}
\]

where

\[
 H(u)=-u\log u-(1-u)\log(1-u).
 \]

Since `H(u)<=log 2`, the central split is optimal among all one-pass
first-difference packings.

## 5. Why transport is necessary

The critical archimedean term is `4 sqrt(X)`, whereas every one-pass fixed-ratio
packing loses the fixed proportion

\[
 1-H(u)>0.
 \]

Thus no proof can close RH by merely selecting a better single balanced split
in (L-23811.4). It must reuse the residual column capacity through additional
state-dependent transport, Pascal cycles, or an equivalent signed arithmetic
mechanism.

This identifies the exact quantitative role of BCT:

```text
one pass:        4 log(2) sqrt(X)
required total:  4 sqrt(X)
missing mass:    4[1-log(2)] sqrt(X).
```

## 6. Proof boundary

Proved unconditionally:

- a finite nonnegative balanced packing at every endpoint;
- its exact prime-ramp implication;
- the sharp one-stage constant `4 log 2`;
- optimality among fixed one-pass split ratios.

Not proved:

- iterative exhaustion of the residual capacity;
- BCT;
- RH.
