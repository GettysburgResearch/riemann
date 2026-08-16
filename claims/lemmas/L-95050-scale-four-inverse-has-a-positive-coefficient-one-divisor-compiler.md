# L-95050 — The scale-four inverse has a positive coefficient-one divisor compiler

Claim ID: `L-95050`  
Status: **PROPOSED COMPLETE EXACT ARITHMETIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: PR #474 at `da557977e6d496cdc395c823e0c8c2aa830ee3e1`, especially the scale-four source dictionary; no factor-67 input  
Scope: Dirichlet coefficients and a finite multiplicative Markov compiler; no additive carry-capacity or RH conclusion

## 1. Positive inverse coefficients

Put

\[
G_4(s)
=\frac1{A_4(s)}
=\zeta(s)\frac{1-4^{-s}}{1-4^{1-s}}.
\tag{L-95050.1}
\]

Write

\[
G_4(s)=\sum_{n\ge1}{g_4(n)\over n^s}.
\]

At every odd prime the Euler factor is the ordinary zeta factor. With `z=2^{-s}`, the dyadic factor is

\[
{1+z\over1-4z^2}
=(1+z)\sum_{k\ge0}4^kz^{2k}.
\]

Therefore

\[
\boxed{
g_4(n)=4^{\lfloor v_2(n)/2\rfloor}>0.}
\tag{L-95050.2}
\]

## 2. Nonnegative generalized primes

Define

\[
-\frac{G_4'(s)}{G_4(s)}
=\sum_{n\ge1}{\Lambda_4(n)\over n^s}.
\tag{L-95050.3}
\]

For every odd prime power,

\[
\Lambda_4(p^r)=\log p.
\]

For powers of two,

\[
\boxed{
\Lambda_4(2^r)
=\begin{cases}
\log2,&r\text{ odd},\\
(2^{r+1}-1)\log2,&r\text{ even}.
\end{cases}}
\tag{L-95050.4}
\]

Thus

\[
\boxed{\Lambda_4(n)\ge0.}
\tag{L-95050.5}
\]

## 3. Exact coefficient-one recursion

The identity

\[
-G_4'=\left(-{G_4'\over G_4}\right)G_4
\]

gives coefficientwise, for every `n>=2`,

\[
\boxed{
g_4(n)\log n
=\sum_{\substack{d\mid n\\d>1}}
 \Lambda_4(d)g_4(n/d).}
\tag{L-95050.6}
\]

Every term is nonnegative. Define

\[
P_n(d)
={\Lambda_4(d)g_4(n/d)\over g_4(n)\log n}
\qquad(d\mid n,\ d>1).
\tag{L-95050.7}
\]

Then

\[
\boxed{P_n(d)\ge0,
\qquad\sum_{d\mid n,d>1}P_n(d)=1.}
\tag{L-95050.8}
\]

Choosing `d` according to `P_n` and replacing `n` by `n/d` gives a descending multiplicative Markov chain which terminates at one. Equation (L-95050.6) says that every coefficient-times-log source is spent exactly once among its proper divisor children.

This is a genuine positive, coefficient-one compiler for the scale-four inverse state.

## 4. Relation to the positive Q4 source

Retain

\[
\Lambda_+=(\varepsilon+2\delta_2)*\Lambda_4\ge0
\]

and

\[
c_\circ=(\varepsilon-2\delta_2)*\Lambda_+.
\]

Every `Lambda_4` occurrence has two positive source labels before the final signed Haar observation:

```text
direct label d         weight 1;
doubled label 2d       weight 2.
```

The divisor compiler acts on the positive `Lambda_4` source before this observation. No source atom is duplicated inside (L-95050.6).

## 5. Proof boundary

Established exactly:

1. positive coefficients of `G_4`;
2. nonnegative generalized-prime sequence;
3. coefficient-one divisor recursion;
4. a finite positive Markov compiler with exact source exhaustion.

Not established:

1. bounded additive carry cost;
2. a square-root estimate for the Q4 mean;
3. RH.
