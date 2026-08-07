# L-15150 — Complete support ledger for `Lambda_2`

Claim ID: `L-15150`  
Title: Selberg's second generalized von Mangoldt coefficient is nonnegative exactly on integers with at most two distinct prime factors  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: elementary Möbius inversion  
Scope: repair of the arithmetic channel statement in `M-15110`

Define

\[
 \Lambda_2(n)
 = (\mu*\log^2)(n)
 =\sum_{d\mid n}\mu(d)\log^2(n/d).
\]

Let

\[
 n=\prod_{i=1}^r p_i^{a_i}
\]

with distinct primes `p_i` and positive exponents `a_i`.

## 1. Exact formulas

If `r=1`, so `n=p^a`, then only `d=1,p` contribute and

\[
 \boxed{
 \Lambda_2(p^a)
 =a^2(\log p)^2-(a-1)^2(\log p)^2
 =(2a-1)(\log p)^2>0.}
\]

If `r=2`, so `n=p^a q^b` with `p!=q`, the four squarefree divisors give the mixed second difference

\[
 \boxed{
 \Lambda_2(p^a q^b)=2\log p\log q>0.}
\]

The value is independent of the positive exponents `a,b`.

If `r>=3`, the alternating squarefree-divisor sum is an `r`-fold finite difference of the quadratic polynomial

\[
 \left(\sum_i a_i\log p_i\right)^2.
\]

Every finite difference of order greater than two vanishes. Hence

\[
 \boxed{
 \Lambda_2(n)=0
 \qquad\text{when }\omega(n)\ge3.}
\]

Consequently

\[
 \boxed{
 \Lambda_2(n)\ge0\quad\text{for every }n.}
\]

## 2. Correction to the semiprime-channel statement

PR #216's `L-21504` exactly identifies the ordinary-prime off-diagonal sector

\[
 n=pq,\qquad p<q,
\]

through

\[
 \Lambda_2(pq)=2\log p\log q.
\]

That sector is load-bearing and correctly described as a balanced squarefree-semiprime sum. It is not the complete `Lambda_2` ledger required by a full Selberg square completion.

The complete positive ledger also contains:

1. every prime-power channel `p^a`, with coefficient `(2a-1)(log p)^2`;
2. every two-distinct-prime channel `p^a q^b`, with coefficient `2 log p log q`;
3. no integer with three or more distinct prime factors.

Thus the wording in `M-15110` must be “at most two distinct prime factors,” not “at most two prime factors,” and the proposed factor maps must explicitly include repeated-prime and nonsquarefree two-prime channels.

## 3. Proof boundary

This lemma proves coefficient nonnegativity and support only. It does not prove that the corresponding operator contributions assemble into positive difference squares, nor that they control the target norm. Those remain separate factorization and coercivity gates.