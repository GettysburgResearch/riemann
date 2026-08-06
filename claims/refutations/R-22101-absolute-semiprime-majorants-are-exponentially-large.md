# R-22101 — Absolute semiprime majorants are exponentially large

Claim ID: `R-22101`  
Title: Taking absolute values of the balanced prime-pair kernel before the final contraction cannot prove the prime-energy criterion  
Status: `PROPOSED — COMPLETE ASYMPTOTIC NO-GO`  
Authoring agent: `gpt56-pro-18`  
Created: 2026-08-07  
Issue: #221  
Dependencies: `L-21504`; the prime number theorem

## 1. Absolute off-diagonal ledger

Let `H` be the fixed prime-only window of `T-21502`, and let

\[
 C_H(t)=\int_{\mathbb R}H(u)H(u+t)\,du
\]

be its complete interior autocorrelation. Since `H` is nonzero and continuous,

\[
 C_H(0)=\|H\|_2^2>0.
\]

Hence there exist fixed constants

\[
 \delta>0,\qquad c_0>0
\]

such that

\[
 C_H(t)\ge c_0
 \qquad(|t|\le\delta).
 \tag{R-22101.1}
\]

For a cumulative cutoff `X`, define the entrywise absolute off-diagonal ledger

\[
 \mathcal A_H(X)
 =2\sum_{p<q}
  \frac{\log p\log q}{\sqrt{pq}}
  |K_X^H(\log p,\log q)|.
 \tag{R-22101.2}
\]

## 2. Exponential lower bound

Let `[a_H,b_H]` be the support of `H`. Choose one fixed logarithmic interval

\[
 I_X=[X-b_H-2\delta,\,X-b_H-\delta].
\]

For all sufficiently large `X`, every pair of primes with logarithms in `I_X`
is fully interior, and its log ratio has absolute value at most `delta`.
Therefore (R-22101.1) gives

\[
 \mathcal A_H(X)
 \ge c_0\left[
   \left(\sum_{\log p\in I_X}
       \frac{\log p}{\sqrt p}\right)^2
   -\sum_{\log p\in I_X}\frac{(\log p)^2}{p}
  \right].
 \tag{R-22101.3}
\]

The prime number theorem and partial summation give

\[
 \sum_{e^Y<p\le e^{Y+\delta}}
  \frac{\log p}{\sqrt p}
 =2\bigl(e^{(Y+\delta)/2}-e^{Y/2}\bigr)(1+o(1)).
 \tag{R-22101.4}
\]

The diagonal subtraction is only polynomial in `Y`. Thus there is a constant
`c_1>0` such that

\[
 \boxed{
 \mathcal A_H(X)\ge c_1e^X
 }
 \tag{R-22101.5}
\]

for all sufficiently large `X`.

Consequently

\[
 \liminf_{X\to\infty}
 \frac{\log(1+\mathcal A_H(X))}{X}\ge1.
 \tag{R-22101.6}
\]

## 3. Consequence for proof design

The RH-equivalent signed target is

\[
 [\mathcal O_H^{\mathbb P}(X)]_+=\exp(o(X)).
\]

Its entrywise absolute majorant is at least `exp(X+O(1))`. Thus any proof that
performs one of the following operations before the final factor-ratio
contraction is quantitatively incapable of reaching RH:

1. replace the piecewise-cubic kernel by its absolute value;
2. bound each prime-pair cell independently and add absolute errors;
3. apply an unsigned upper-bound sieve to every factor-ratio cell;
4. discard the negative cells and retain only positive cells;
5. dominate the complete Gram by its row-sum absolute norm.

The empirical cancellation in `O-21502` is therefore not optional numerical
conditioning. It is the entire theorem.

## 4. Scope

- The no-go uses only continuity of the fixed kernel and the prime number
  theorem.
- It does not say that Type-II or dispersion methods are useless; it says their
  signed final contraction must be preserved.
- It does not prove the signed semiprime estimate.
