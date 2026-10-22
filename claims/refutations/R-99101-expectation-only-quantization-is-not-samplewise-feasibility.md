# R-99101 — Feasibility in expectation is not a feasible physical leaf

Claim ID: `R-99101`  
Status: **PROVED EXACT ONE-COLUMN FIREWALL**  
Created: 2026-08-19

Let one physical column have capacity one. Define a random rounded row `X` by

\[
 X=2\quad\text{with probability }\frac12,
 \qquad
 X=0\quad\text{with probability }\frac12.
\]

Then

\[
 \mathbb E X=1,
\]

so the fractional barycenter is feasible. But the sampled leaf violates the capacity with probability one half.

Therefore unbiased coordinatewise or martingale rounding does not establish a physical producer. Samplewise feasibility must be built into the leaf support, as in the integral-flow decomposition of `L-99102`, or proved separately.
