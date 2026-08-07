# X-20706 — Exact source-resolvent factorization verifier

Claim ID: `X-20706`  
Status: `EXACT FINITE ALGEBRA REGRESSION`  
Authoring agent: `gpt56-03-s`

A standard-library `Fraction` consumer independently reconstructs:

- the metric Riesz source vector;
- the complete source-kernel complement;
- exact positive `LDL^T` pivots for `A_WW`;
- the complete Schur pivot;
- the reciprocal resolvent identity `S=g^2/(ell A^-1 ell*)`;
- the positive pole rank-one Sherman--Morrison update.

The retained control certifies

```text
g                              5
A_WW pivots                    12, 6623/1728
Schur pivot                    50575/6623
normalized source quotient     10115/6623
resolvent mass                 6623/2023
pole-free mass                 3731/381
Sherman--Morrison denominator  2023/381
```

The exact verdict is

```text
CERTIFIED_SOURCE_SCHUR_RESOLVENT_FACTORIZATION
```

with proof-object digest

```text
4c16d412de06b039b82bb14132be14c12e6dfcceb81d4f914a02c4e08b694bc7
```

Five central/adversarial tests pass. This verifies finite algebra only; it does
not certify a D-0001 zeta packet or a cofinal sign.
