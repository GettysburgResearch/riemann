# X-20807 — Exact Lévy/Euler-flow verifier

Claim ID: `X-20807`  
Title: Fraction-only replay of the compound-Poisson reserve and finite Euler Riccati defect  
Status: `EXACT FINITE SYNTHETIC REGRESSION`  
Authoring agent: `gpt56-03-v`  
Created: 2026-08-07  
Dependencies: `L-20810`; `L-20812`

The standard-library checker at

```text
experiments/X-20807-levy-euler-flow/verify.py
```

verifies two independent identities:

```text
reserve = initial reserve + arithmetic variance - reference variance,
```

and

```text
Q_(p,K)=P_(p,K)^2+(log p)P_(p,K)-E_(p,K),
E_(p,K)>0.
```

Retained exact values:

```text
arithmetic mean                 6
arithmetic variance            26
reference variance             24
Fenchel barrier                23
reserve                         3

local P                     45/16
local Q                     117/8
finite-power cutoff defect 441/256
```

Verdict:

```text
PASS_EXACT_L20810_L20812_IDENTITIES
```

The artifact verifies finite algebra only. It contains no production Riemann
packet and makes no cofinal or RH claim.