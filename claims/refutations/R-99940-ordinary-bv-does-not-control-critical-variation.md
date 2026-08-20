# R-99940 — Positive convergence and ordinary bounded variation do not control critical weighted variation

Claim ID: `R-99940`  
Status: **EXACT COUNTEREXAMPLE**  
Created: 2026-08-20

Consider a positive cadlag function which equals `1` except that at time

\[
u_k=k\log2
\]

it jumps downward by `2^{-k}` and shortly afterward jumps upward by the same
amount. Its ordinary total variation is

\[
2\sum_{k\ge1}2^{-k}=2,
\]

and it converges to `1`. But its exponentially weighted downward variation is

\[
\sum_{k\ge1}e^{u_k}2^{-k}
=\sum_{k\ge1}1
=\infty.
\]

Hence the properties proved in `L-99941` do not imply the estimate required in
`L-99942`. Any closure must use arithmetic cancellation at the critical
weight.
