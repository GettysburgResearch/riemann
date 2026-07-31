# X-14313 — Exact separated-zero frame-floor verifier

Claim ID: `X-14313`  
Title: Fraction-only verification of the `L-14320` Hardy-frame floor  
Status: `EMPIRICAL`  
Authoring agent: `gpt56-pro-09-c`  
Created: 2026-07-31  
Dependencies: `L-14320`  
Scope: exact scalar composition of directed analytic bounds

The checker verifies

```text
sigma^2
 = d_lower (1-r_upper) - m epsilon_upper
```

with exact rational arithmetic.  Production use requires a typed gate binding
the selected certified zeros, their separation, the reciprocal-Hardy kernel
normalization, and directed evaluations of the three analytic bounds.

The retained synthetic packet proves `147/100` from

```text
d_lower=2,
r_upper=1/4,
m=3,
epsilon_upper=1/100.
```

Six adversarial tests are retained.
