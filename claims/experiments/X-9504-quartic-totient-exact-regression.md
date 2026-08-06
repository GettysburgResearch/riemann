# X-9504 — Exact quartic totient/Bernoulli regression

Claim ID: `X-9504`  
Title: Fraction-only replay of the quartic cell and Möbius decompositions  
Status: `PROPOSED CERTIFIED FINITE ALGEBRA`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: `L-9508`  
Scope: finite algebra only  
Related counterexample candidates: none

## Result

The standard-library verifier under

```text
experiments/X-9504-quartic-totient-exact/
```

checks:

1. the direct quartic cell sum against `L-9508.5` at five rational values;
2. the direct exact totient observable against `L-9508.10` for every integer
   `2 <= x <= 100`;
3. exact strict-cutoff behavior at integer endpoints.

The retained verdict is

```text
PASS_EXACT_L9508_BERNOULLI_MOBIUS_IDENTITY
```

and the canonical proof-object SHA-256 is

```text
b39d7cb81881d6fcf6abbb14f4d2fbb202535911e9640fdab487be93acdcf7f1
```

## Classification

This verifies only the finite identities. It does not verify:

- the asymptotic Mertens estimate;
- the RH-equivalent bound of `T-9502`;
- any universal sign or finite-to-global inference.

## Independent review

Reviewers should mutate Bernoulli coefficients, powers of `x`, the strict
endpoint convention, and one totient or Möbius value. Every mutation must break
an exact equality.
