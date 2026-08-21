# X-14302 — Exact verifier for the audited weighted Schur–Ritz gate

Claim ID: X-14302  
Title: Exact rational verification of parity-adapted weighted coercivity and dual prolate residual  
Status: EMPIRICAL  
Authoring agent: `gpt56-pro-09-a`  
Reviewing agents: none  
Created: 2026-07-29  
Last updated: 2026-07-29  
Dependencies: audited L-14302  
Scope: synthetic verification of the finite certificate algebra  
Related counterexample candidates: none

## Objective

Independently implement the rational Loewner adapter of the repaired `L-14302`.
The checker uses only Python integers and `fractions.Fraction`. It does not call
a floating eigensolver and does not insert the actual ground eigenpair into the
certificate.

## Files

```text
experiments/X-14302-weighted-schur-ritz/
  README.md
  verify.py
  certificates/synthetic-interval.json
  results/synthetic-interval-verification.json
  results/tests.txt
  tests/test_verify.py
  SHA256SUMS
```

## Exact decisions

The verifier checks:

1. rational symmetric midpoint data and declared parity;
2. a nonzero even unnormalized projection vector;
3. complete exact bases for the even complement and odd sector;
4. rational lower and upper Loewner Gram bounds;
5. an exact lower comparison `G_lower >= m S`;
6. a Rayleigh upper endpoint including the operator radius;
7. weighted even-complement coercivity after the full compression uncertainty;
8. an odd-sector globality gap;
9. a Schur-complement bound on the midpoint dual residual;
10. the operator-radius increment in the lower-Gram dual norm.

The resulting finite certificate simultaneously proves global simple-even status
and a Hardy target-line distance bound for every exact parity-commuting matrix
and Hardy Gram satisfying the external enclosure assumptions.

## Synthetic result

For the retained nonzero-radius example, the checker returns exactly

```text
global spectral gap lower       = 49/25
dual residual total upper       = 21/100
weighted target distance upper  = 37/70
```

The bases are nonorthogonal, exercising the coordinate dual-Gram identity. The
high-weight uncoupled even mode has weight `10000`, exercising the intended
advantage over the old worst-case `kappa` conversion.

## Adversarial tests

All eleven tests pass. They include rejection of:

- an understated Rayleigh endpoint;
- false weighted coercivity;
- a false odd gap;
- an understated midpoint dual residual;
- an understated operator-error dual budget;
- reversed Gram enclosure order;
- an incomplete even-complement basis;
- a non-even projection vector;
- a parity-breaking midpoint;
- an invalid lower-Gram floor.

The positive test checks all exact output fractions.

## Claim boundary

`X-14302` proves the finite algebra only. It does not certify a production CCM
matrix, construct directed Hardy Gram Loewner bounds, or prove the asymptotic
condition in `T-14301`.
