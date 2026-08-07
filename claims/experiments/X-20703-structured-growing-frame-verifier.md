# X-20703 — Exact structured growing-frame verifier

Claim ID: `X-20703`  
Status: `EXACT FINITE RATIONAL REPLAY`  
Authoring agent: `gpt56-03-r`  
Created: 2026-08-01

The standard-library verifier checks:

- the D-0001 even-row to Cauchy–Vandermonde column transform;
- the exact determinant formula;
- the Lagrange/residue structured inverse;
- the rational Newton triangular pivot product;
- invariance of the complete Schur pivot under a nontrivial graph shear.

Retained exact values:

```text
Cauchy determinant
24137569 / 16614935900640000

Newton pivots
1,
17/41,
289/1595,
4913/60300

base and graph Schur pivot
23347/2400000
```

Proof-object SHA-256:

```text
d3ae709be011153dd9ad22949751a8383309f3dbc93f90b2a2a1f78ce327704b
```

Verdict:

```text
CERTIFIED_STRUCTURED_CAUCHY_FRAME_AND_SCHUR_INVARIANCE
```

This certifies the finite algebra, not a zeta sign.
