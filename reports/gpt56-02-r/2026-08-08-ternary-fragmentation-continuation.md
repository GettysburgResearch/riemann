# Deterministic ternary continuation of the Möbius fragmentation proposal

Agent: `gpt56-02-r`  
Date: 2026-08-08  
Status: **EXACT DETERMINISTIC REDUCTION; INNER POSITIVITY UNPROVED; RH UNPROVED**

## Result

The broad Möbius Fragmentation Transport cone on PR #272 contains a much smaller
candidate: use only the split

\[
n\to\lceil n/3\rceil+\lfloor2n/3\rfloor
\]

at every parent.

For any target, one descending recurrence emits unique real coefficients
`A_X(n)`. Its divergence is exactly the multiples-Möbius divergence, so every
carry column is saturated with zero slack. Nonnegativity of these coefficients
therefore proves the full MFT theorem with fixed balance `eta=1/4`.

The recurrence has the exact scalar tail form

\[
S_X(n)=u_n+S_X(\lceil3n/2\rceil)+S_X(3n-2),
\qquad A_X(n)=S_X(n)-S_X(n+1).
\]

Thus the quadratic fragmentation LP is reduced to monotonicity of one explicit
one-dimensional renewal. The reviewed outer theorem proves this monotonicity on
`5n>=X`; only the inner fifth remains.

## New ternary digit connection

The exact split carry is

\[
\chi_3(n,q)=C_{1/3}(n,q)
-1_{3\nmid n}1_{q\mid\lceil n/3\rceil}.
\]

The first term is the positive continuum ternary carry. The second is one
explicit divisibility boundary, which groups as

\[
E_X(m)=A_X(3m-2)+A_X(3m-1).
\]

The base-three endpoint satisfies

\[
\sum_{m\le N}(1-2v_3(m))=s_3(N)\ge0.
\]

This places the deterministic producer in the same source language as the
positive `p=3` digit comb of `L-23013`, while keeping the boundary charge visible.

## Targeted reconnaissance

Ordinary double-precision evaluation of the actual logarithmic target found no
negative ternary coefficient through `X=5,000,000`. This is explicitly not a
proof: the smallest positive coefficients are of order `X^{-3/2}` near the
terminal endpoint, and a hypothetical off-line zero could force only eventual
large-scale oscillation.

## Exact proof boundary

Proved exactly:

- deterministic ternary grammar;
- exact divergence and all-column saturation;
- scalar tail renewal;
- outer positivity;
- ternary continuum/boundary identity;
- base-three endpoint identity;
- conditional chain to the sharp prime ramp and RH.

Open:

\[
S_X(n)\ge S_X(n+1)\qquad(n<X/5).
\]

This is now the smallest deterministic version of MFT. It is RH-bearing and is
not being presented as routine renewal positivity.
