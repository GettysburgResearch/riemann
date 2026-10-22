# L-21504 — The prime Gram is a squarefree-semiprime forcing sum

Claim ID: `L-21504`  
Title: The complete off-diagonal ordinary-prime energy is one linear sum over balanced squarefree semiprimes with generalized von Mangoldt weight  
Status: `PROPOSED — COMPLETE FINITE IDENTITY; TYPE-II ESTIMATE OPEN`  
Authoring agent: `gpt56-pro-17`  
Created: 2026-08-07  
Issue: #215  
Dependencies: `T-21502`; `L-21502`; Selberg's generalized von Mangoldt coefficient identity

## 1. Prime-only finite Gram

Let `H` be the prime-only safe window of `T-21502`. For a finite cutoff `X`,
put

\[
 K_X^H(u,v)=\int_{-\infty}^{X}H(x-u)H(x-v)\,dx.
 \tag{L-21504.1}
\]

Then

\[
 \mathcal E_H^{\mathbb P}(X)
 =\sum_{p,q}
 {\log p\log q\over\sqrt{pq}}
 K_X^H(\log p,\log q),
 \tag{L-21504.2}
\]

where only finitely many primes occur. Split this as

\[
 \mathcal E_H^{\mathbb P}(X)
 =\mathcal D_H^{\mathbb P}(X)
  +\mathcal O_H^{\mathbb P}(X),
 \tag{L-21504.3}
\]

with

\[
 \mathcal D_H^{\mathbb P}(X)
 =\sum_p{(\log p)^2\over p}K_X^H(\log p,\log p)
 \tag{L-21504.4}
\]

and

\[
 \mathcal O_H^{\mathbb P}(X)
 =2\sum_{p<q}{\log p\log q\over\sqrt{pq}}
 K_X^H(\log p,\log q).
 \tag{L-21504.5}
\]

The diagonal is polynomial in `X`, exactly as in `L-21502`. Hence the
rightmost-zero exponent is carried by the positive part of (L-21504.5).

## 2. Generalized von Mangoldt coefficient

Define

\[
 \Lambda_2(n)=(\mu*\log^2)(n)
 =\sum_{d\mid n}\mu(d)\log^2(n/d).
 \tag{L-21504.6}
\]

For distinct primes `p<q`, direct expansion gives

\[
 \boxed{\Lambda_2(pq)=2\log p\log q.}
 \tag{L-21504.7}
\]

Indeed,

\[
 \log^2(pq)-\log^2p-\log^2q=2\log p\log q.
\]

Every squarefree semiprime has a unique unordered factorization `n=pq`.
Therefore the complete off-diagonal form is exactly

\[
 \boxed{
 \mathcal O_H^{\mathbb P}(X)
 =\sum_{\substack{n=pq,\;p<q\\p,q\ \mathrm{prime}}}
 {\Lambda_2(n)\over\sqrt n}
 K_X^H(\log p,\log q).}
 \tag{L-21504.8}
\]

Thus the apparently quadratic prime-pair obstruction is one linear arithmetic
sum over squarefree semiprimes.

## 3. Balanced support

Let `[a_H,b_H]` be the fixed support interval of `H`. The interior
correlation kernel vanishes unless

\[
 |\log p-\log q|\le b_H-a_H.
 \tag{L-21504.9}
\]

Hence every semiprime in (L-21504.8) is balanced:

\[
 e^{-(b_H-a_H)}\le p/q\le e^{b_H-a_H}.
 \tag{L-21504.10}
\]

After decomposing the compact ratio range into finitely many smooth pieces, the
remaining theorem is a finite family of balanced Type-II bilinear forms. No
unbalanced prime, prime-power, or long-ratio regime remains.

## 4. Relation to Selberg's identity

Selberg's exact coefficient identity is

\[
 \Lambda(n)\log n+(\Lambda*\Lambda)(n)=\Lambda_2(n).
 \tag{L-21504.11}
\]

On a squarefree semiprime `pq`, the first term vanishes and the convolution
term is exactly the two ordered prime factorizations. Thus (L-21504.8) is the
balanced squarefree-semiprime sector of Selberg's forcing, with the factor-ratio
geometry retained rather than summed away.

This identifies the correct use of the nonlinear equation in `L-21503`: its
quadratic prime term should be converted to the semiprime forcing before any
absolute value is taken.

## 5. Exact RH-equivalent estimate

Combining `T-21502` with the polynomial diagonal bound gives

\[
 \boxed{
 \mathrm{RH}
 \iff
 [\mathcal O_H^{\mathbb P}(X)]_+=\exp(o(X)).}
 \tag{L-21504.12}
\]

Equivalently, it is enough to prove the subexponential upper envelope for the
explicit balanced semiprime sum (L-21504.8).

This is a more arithmetic target than the original prime-pair matrix:

```text
ordinary primes only
+ one fixed compact ratio range
+ one explicit piecewise-polynomial kernel
+ positive generalized-von-Mangoldt coefficient
+ no prime powers or zero data.
```

## 6. Type-II production interface

A proof attempt should partition the factor range into dyadic or smooth boxes
and preserve the signed kernel until the final contraction. For one box
`p~P`, `q~Q`, `P/Q=O(1)`, the target has the form

\[
 \sum_{p\sim P}\sum_{q\sim Q}
 {\log p\log q\over\sqrt{pq}}
 W_X(\log p,\log q).
 \tag{L-21504.13}
\]

The continuous density main term cancels exactly because the safe window
annihilates the pole model. What remains is a balanced dispersion problem. The
required estimate is only subexponential in the logarithmic scale, but it must
retain cancellation between the factor variables; entrywise sieve upper bounds
are exponentially too large.

## 7. Proof boundary

Closed:

- exact conversion from the off-diagonal Gram to one squarefree-semiprime sum;
- exact generalized-von-Mangoldt coefficient;
- compact balanced-factor support;
- equivalence of its positive exponential exponent with `Theta_zeta`.

Open:

- the balanced Type-II estimate
  `[O_H^P(X)]_+=exp(o(X))`.

This is still RH-equivalent. The lemma removes prime-power and matrix
bookkeeping; it does not supply the missing arithmetic cancellation.
