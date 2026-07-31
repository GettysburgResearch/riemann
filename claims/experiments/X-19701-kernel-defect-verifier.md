# X-19701 — Exact Schur-corrected kernel-defect verifier

Claim ID: `X-19701`  
Title: Fraction-only replay of the off-line cardinal signature through a nontrivial positive-complement Schur correction  
Status: `EXACT FINITE SYNTHETIC REGRESSION`  
Authoring agent: `gpt56-03-o`  
Created: 2026-07-31  
Dependencies: `L-19701`, `R-19701`

The standard-library checker in

```text
experiments/X-19701-kernel-defect/
```

verifies:

- positive kernel metric and complement;
- the exact conjugate-cardinal block `[[0,m],[m,0]]`;
- invisibility of the difference vector at every selected real coordinate;
- exact Schur correction with a nonzero cross map;
- preservation and strengthening of the negative value;
- a positive all-real control using the same metric, complement, and cross map;
- immutable proof-object and file SHA-256 bindings.

Retained exact values:

```text
raw off-line quadratic          -2
Schur-corrected quadratic       -17/8
corrected generalized Rayleigh  -17/16
all-real Schur floor             31/16
```

Proof-object SHA-256:

```text
1af83681c99e1204845996f055a1bc54d98dcda85fdb73e7d97ddcfee17ca049
```

Nine adversarial tests pass locally. The experiment proves finite algebra only;
the Xi-cardinal domain, finite-support repair, and complete-kernel capture remain
analytic dependencies.
