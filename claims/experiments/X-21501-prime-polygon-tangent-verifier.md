# X-21501 — Prime-power polygon tangent verifier

Claim ID: `X-21501`  
Title: Exact rational contraction of a finite prime-polygon RH-disproof witness  
Status: `EXACT FINITE CHECKER / SYNTHETIC REGRESSION; NO RIEMANN VERDICT`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: `L-21501`, `T-21501`

The checker verifies the one-sided implication

\[
2A_j\log r-F(2\log r)-B_j>0
\quad\Longrightarrow\quad
\Psi(2\log r)<0.
\]

It performs exact rational interval arithmetic after all transcendental and
prime-prefix inputs have been externally directed. The positive Lerch tail is
enclosed by a partial sum and an exact geometric majorant. The production
classification is fail-closed and requires immutable source bindings.

The retained artifact is synthetic. It returns

```text
SYNTHETIC_POSITIVE_TANGENT_WITNESS
```

with proof-object SHA-256 recorded in
`experiments/X-21501-prime-polygon/results/synthetic-verification.json`.
Seven tests pass. No actual prime prefix is claimed to violate the polygon
barrier, and no counterexample to RH is claimed.
