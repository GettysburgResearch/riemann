# X-28301 — Exact Markov–Pascal algebra replay

Run:

```bash
python experiments/X-28301-markov-pascal/verify.py
```

The standard-library checker verifies:

```text
third-Abel counterexample       -91/256
fourth-Abel counterexample      -10512404675923/16384
central/sibling carry rows      16,383
commutator/divisor rows         140
sibling transport rows          121
rational Gamma-domination rows  2,552
matrix-lift entries             9
mutation tests                  6/6
```

Retained classification:

```text
EXACT_MARKOV_PASCAL_GLOBAL_ATTACK_ALGEBRA
```

Proof-object SHA-256:

```text
b0d970ace6e892709f36ead9e453d1937cad3f481ea534c15422686e83b27fb0
```

## Scope

The checker authenticates finite integer/rational algebra and mutation
controls.  It does **not** integrate the continuous Markov kernel, construct a
production state partition, prove the SAPC recurrence, estimate zeta zeros, or
prove RH.
