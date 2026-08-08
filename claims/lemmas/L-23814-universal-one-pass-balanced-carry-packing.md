# L-23814 — Universal one-pass balanced carry packing

Claim ID: `L-23814`  
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
\qquad2\le q\le X,
\]

and set `w_X(X+1)=0`. Since `w_X` is decreasing, define

\[
\boxed{
a_X(n)=w_X(n)-w_X(n+1)\ge0.}
\tag{L-23814.1}
\]

Choose the central split `j_n=floor(n/2)` and put

\[
d_X(n,j_n)=a_X(n),
\qquad d_X(n,j)=0\ (j\ne j_n).
\tag{L-23814.2}
\]

## 2. Exact feasibility

Every atomized carry coefficient is zero or one. Hence

\[
\begin{aligned}
L_q(d_X)
&=\sum_{n=q}^{X-1}a_X(n)\chi_{n,j_n}(q)\\
&\le\sum_{n=q}^{X-1}a_X(n)
=w_X(q).
\end{aligned}
\]

Thus this is a nonnegative balanced carry packing at every finite endpoint.

## 3. Sharp one-stage value

The central binomial estimate gives

\[
\log\binom n{\lfloor n/2\rfloor}
=n\log2+O(\log(n+1)).
\]

Summation by parts gives

\[
\sum_{n=2}^{X-1}n[w_X(n)-w_X(n+1)]
=2w_X(2)+\sum_{n=3}^{X-1}w_X(n),
\]

while elementary integral comparison yields

\[
\sum_{n=2}^{X-1}w_X(n)=4\sqrt X+O(\log X).
\]

The logarithmic error costs only `O((log X)^2)`. Therefore

\[
\boxed{
\sum_{n=2}^{X-1}a_X(n)
\log\binom n{\lfloor n/2\rfloor}
=4(\log2)\sqrt X+O((\log X)^2).}
\tag{L-23814.3}
\]

By the exact valuation identity,

\[
\boxed{
\sum_{p^k\le X}\frac{\Lambda(p^k)}{\sqrt{p^k}}
\log\frac X{p^k}
\ge4(\log2)\sqrt X-O((\log X)^2).}
\tag{L-23814.4}
\]

## 4. Optimality among fixed one-pass ratios

For one fixed split ratio `0<u<1`, choose `j_n=round(un)` with any consistent
endpoint convention. The same feasibility proof works, and uniform Stirling
bounds give

\[
\boxed{
\sum_na_X(n)\log\binom n{j_n}
=4H(u)\sqrt X+O_u((\log X)^2),}
\tag{L-23814.5}
\]

where `H(u)=-u log u-(1-u)log(1-u)`. Since `H(u)<=log2`, the central split is
optimal among all fixed-ratio one-pass first-difference packings.

## 5. Consequence for the research frontier

The critical archimedean term is `4 sqrt(X)`. Every fixed one-pass ratio leaves
a positive proportion of the carry capacity unused. A completion must reuse the
residual through state-dependent fragmentation, Pascal circulation, or an
equivalent signed arithmetic theorem.

## 6. Proof boundary

Proved unconditionally:

- finite nonnegative balanced packing at every endpoint;
- exact prime-ramp implication;
- sharp one-stage constant `4 log2`;
- optimality among fixed one-pass ratios.

Not proved:

- iterative exhaustion;
- BCT/BTF;
- RH.
