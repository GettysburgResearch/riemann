# T-27201 — Deterministic ternary fragmentation positivity implies RH

Claim ID: `T-27201`  
Title: Nonnegativity of one explicit descending `1/3–2/3` carry recurrence gives a zero-slack balanced carry certificate and the Riemann Hypothesis  
Status: **FULL CONDITIONAL PROPOSAL / ONE SCALAR POSITIVITY THEOREM OPEN**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-27201`, `L-27202`, `T-26202`, `L-23808`, `L-23809`  
Scope: complete implication; no claim that the positivity hypothesis is proved

## 1. Ternary Fragmentation Positivity

For the logarithmic target

\[
w_X(q)=q^{-1/2}\log(X/q),
\]

construct `r_X` and the deterministic coefficients `A_X(n)` by
`L-27201.2`--`L-27201.6`.

The sole hypothesis is

\[
\boxed{
A_X(n)\ge0
\qquad(2\le n\le X)
}
\tag{TFP}
\]

for every sufficiently large integer `X`.

Equivalently, the scalar renewal tail `S_X` in (L-27201.12) is nonincreasing.

## 2. TFP gives the exact MFT certificate

Put

\[
d_{n,j}=A_X(n)\mathbf1_{j=\lceil n/3\rceil}.
\]

The split is uniformly balanced with `eta=1/4`. By `L-27201.7`, every integer
carry column is saturated exactly:

\[
\sum_{n,j}d_{n,j}\chi_{n,j}(q)=w_X(q).
\]

Thus `TFP` is a deterministic strengthening of `MFT_{1/4}`; no quadratic LP,
choice rule, or unbounded split dictionary remains.

## 3. Sharp entropy transfer

The atomized carry/Legendre identity gives

\[
\sum_{n,j}d_{n,j}\log\binom nj
=
\sum_{q=p^a\le X}\frac{\Lambda(q)}{\sqrt q}\log(X/q).
\]

The balanced carry-count/entropy comparison and the exact capacity bound imply

\[
\sum_{q=p^a\le X}\frac{\Lambda(q)}{\sqrt q}\log(X/q)
\ge4\sqrt X-O(\log^2X).
\tag{T-27201.1}
\]

## 4. RH completion

At `X=N^2`, the reviewed square-screw identity converts (T-27201.1) into a
polylogarithmic upper envelope for the negative RH-sensitive screw channel.
The square-sampling/Landau theorem forces rightmost-zero displacement zero.
Functional-equation symmetry gives

\[
\boxed{\mathrm{RH}.}
\]

## 5. Exact remaining theorem

`L-27201.17` proves `TFP` on the outer range `5n>=X`. The unresolved theorem is
therefore the explicit finite inequality

\[
\boxed{
S_X(n)\ge S_X(n+1)
\qquad(2\le n<X/5),
}
\tag{T-27201.2}
\]

where `S_X` is given recursively by

\[
S_X(n)=u_n+S_X(\lceil3n/2\rceil)+S_X(3n-2).
\]

This statement retains the coherent Möbius mode. It is not claimed to follow
from generic renewal positivity or finite reconnaissance.

## 6. Status boundary

Exact and reviewable:

- deterministic producer;
- zero-slack carry saturation;
- fixed balance reserve;
- scalar tail-renewal equivalence;
- outer positivity;
- conditional entropy/Landau completion.

Open and RH-bearing:

- inner `TFP` / renewal monotonicity.

RH remains unproved.
