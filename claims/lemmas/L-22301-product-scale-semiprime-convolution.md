# L-22301 — Product-scale semiprime convolution

Claim ID: `L-22301`  
Title: The analytic square of the prime-only RH signal is one one-dimensional prime-square and squarefree-semiprime convolution  
Status: `PROPOSED — COMPLETE FINITE ARITHMETIC IDENTITY`  
Authoring agent: `gpt56-pro-19`  
Created: 2026-08-07  
Issue: #223  
Dependencies: `T-22301`; elementary multiplicative convolution  
Scope: exact arithmetic source of the critical H1 function

## 1. Window square

Let

\[
 W=H*H.
 \tag{L-22301.1}
\]

Since `H` is compactly supported and piecewise linear, `W` is a compactly
supported piecewise-cubic function. Its bilateral Laplace transform is

\[
 \widehat W(z)=\widehat H(z)^2.
 \tag{L-22301.2}
\]

## 2. Direct product expansion

For

\[
 Q(x)=\sum_p\frac{\log p}{\sqrt p}H(x-\log p),
\]

local finiteness permits direct convolution:

\[
\begin{aligned}
 (Q*Q)(x)
 &=\sum_{p,q}
   \frac{\log p\log q}{\sqrt{pq}}
   W(x-\log p-\log q)\\
 &=\boxed{
   \sum_{p,q}
   \frac{\log p\log q}{\sqrt{pq}}
   W(x-\log(pq)).}
\end{aligned}
\tag{L-22301.3}
\]

Every fixed `x` contains only finitely many pairs.

Group the ordered pairs by their product. Define

\[
 b_{\mathbb P,2}(n)
 =\sum_{pq=n\atop p,q\ \mathrm{prime}}
   \log p\log q,
 \tag{L-22301.4}
\]

where ordered pairs are counted. Then

\[
 \boxed{
 (Q*Q)(x)
 =\sum_{n\ge4}
   \frac{b_{\mathbb P,2}(n)}{\sqrt n}
   W(x-\log n).}
 \tag{L-22301.5}
\]

Thus the two-prime geometry has collapsed to one product coordinate.

## 3. Prime squares and squarefree semiprimes

The coefficient is supported exactly on integers with two prime factors counted
with multiplicity:

\[
 b_{\mathbb P,2}(p^2)=(\log p)^2,
 \tag{L-22301.6}
\]

and, for distinct primes `p<q`,

\[
 \boxed{
 b_{\mathbb P,2}(pq)=2\log p\log q.}
 \tag{L-22301.7}
\]

For squarefree semiprimes the latter coefficient equals

\[
 \Lambda_2(pq)=(\mu*\log^2)(pq).
 \tag{L-22301.8}
\]

Therefore

\[
\boxed{
\begin{aligned}
(Q*Q)(x)
={}&\sum_p\frac{(\log p)^2}{p}
 W(x-2\log p)\\
&+\sum_{p<q}
 \frac{\Lambda_2(pq)}{\sqrt{pq}}
 W(x-\log(pq)).
\end{aligned}}
\tag{L-22301.9}
}
\]

The first line is the exact product-diagonal. The second is one linear
squarefree-semiprime signal.

Unlike the original Gram, formula (L-22301.9) has no factor-ratio variable. The
balanced-ratio restriction is encoded implicitly in the compact product window
and in the factorization condition `n=pq`.

## 4. Full von Mangoldt square and Selberg forcing

For comparison, let

\[
 Q_\Lambda(x)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 H(x-\log n).
 \tag{L-22301.10}
\]

Then

\[
 \boxed{
 (Q_\Lambda*Q_\Lambda)(x)
 =\sum_{n\ge4}
   \frac{(\Lambda*\Lambda)(n)}{\sqrt n}
   W(x-\log n).}
 \tag{L-22301.11}
\]

Selberg's exact coefficient identity

\[
 \Lambda(n)\log n+(\Lambda*\Lambda)(n)
 =\Lambda_2(n)
 \tag{L-22301.12}
\]

therefore gives

\[
 \boxed{
 (Q_\Lambda*Q_\Lambda)(x)
 =\sum_n
 \frac{\Lambda_2(n)-\Lambda(n)\log n}{\sqrt n}
 W(x-\log n).}
 \tag{L-22301.13}
\]

This is the one-dimensional form of the nonlinear Selberg channel isolated in
`L-21503`.

## 5. Finite proof interface

For a finite `x` interval, a production object consists of:

1. the complete prime or prime-power manifest in the compact product annulus;
2. the explicit piecewise-cubic window `W`;
3. the product coefficient `b_(P,2)`, or `Lambda_2-Lambda log`;
4. one exact or outward-enclosed one-dimensional contraction;
5. an independent direct pair-convolution replay.

The pair and product producers must agree. This is a strong normalization check
because their enumerations and conditioning are different.

## 6. Proof boundary

The convolution identities and coefficients are exact. They remove the
ratio-variable bookkeeping, but they do not prove that the critical Fourier
`L1` norm of `T-22301` is finite. The remaining theorem is a signed local
embedding/cancellation statement for this one semiprime signal.
