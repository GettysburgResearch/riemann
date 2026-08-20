# R-100131 — Finite positive von-Mangoldt completions cannot cancel the real carrier

Claim ID: `R-100131`  
Status: **PROVED EXACT COEFFICIENT-ISOLATION THEOREM**  
Created: 2026-08-20  
RH status: **not assumed**

Let

\[
A_k=\underbrace{\Lambda*\cdots*\Lambda}_{k\text{ times}},
\qquad k\ge1.
\]

Then `A_k(n)>=0`, and `A_k(n)=0` whenever `n` has more than `k` distinct
prime factors.

Let

\[
P(s)=\sum_{d\in D}c_d d^{-s}
\]

be a finite Dirichlet polynomial, and suppose the convolution

\[
b=P*A_k
\]

is coefficientwise nonnegative.

Then

\[
\boxed{c_d\ge0\qquad(d\in D).}
\tag{R-100131.1}
\]

## Proof

Fix `d in D`. Choose `k` distinct fresh primes

\[
p_1,\ldots,p_k
\]

which divide no integer in the finite set `D`, and put

\[
R=p_1\cdots p_k.
\]

At `n=dR`,

\[
b(dR)=\sum_{e\mid dR}c_e A_k(dR/e),
\]

where `c_e=0` off `D`.

If `e in D` divides `dR`, freshness forces `e|d`. If `e!=d`, then `d/e>1`
contains a prime outside `{p_1,...,p_k}`. Hence `dR/e` has at least `k+1`
distinct prime factors and

\[
A_k(dR/e)=0.
\]

Only `e=d` survives. Since

\[
A_k(R)=k!\prod_{j=1}^k\log p_j>0,
\]

we have

\[
0\le b(dR)=c_dA_k(R),
\]

which proves (R-100131.1).

Consequently every nonzero such multiplier satisfies

\[
\boxed{P(\sigma)>0\qquad(\sigma\in\mathbb R).}
\tag{R-100131.2}
\]

It cannot have a real zero cancelling the pole of
`(-zeta'/zeta)^k` while preserving coefficient positivity.

## Matrix form

The same isolation works for Hermitian matrix coefficients `C_d`. If every
coefficient of

\[
\left(\sum_dC_dd^{-s}\right)A_k(s)
\]

is positive semidefinite, then

\[
\boxed{C_d\succeq0\quad(d\in D).}
\tag{R-100131.3}
\]

Hence a vector annihilated by the real-carrier matrix
`sum_d C_d d^(-sigma)` is annihilated by every `C_d`; the same observation
channel is then absent at every complex point. A finite PSD matrix completion
cannot cancel only the real carrier while retaining an off-line zero detector.

## Scope

This theorem rules out a broad finite-dimensional escape from the minimal
wavelet frontier:

```text
positive Lambda^(*k) source
 + finite scalar or PSD multiplier
 + real-carrier cancellation
```

cannot coexist nontrivially. It does not rule out genuinely signed/Krein,
infinite-dimensional, or source-specific cross-core mechanisms.