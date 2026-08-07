# X-25801 — Prime-Anchored Digit Transport schema regression

Claim ID: `X-25801`  
Title: Exact finite replay of top-depth transposition, radix depletion, stable recovery, dyadic bit layers, and adjacent-flow divergence  
Status: **EXACT SYNTHETIC REGRESSION; NO PRODUCTION PADT FLOW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #258

The standard-library checker verifies:

1. top-depth logarithmic transposition on six finite parameter cases;
2. exact source-specific depletion
   \[
   (\varepsilon-\delta_Q)T=\mu_V*(a_Q*T);
   \]
3. exact geometric recovery through `H_Q`;
4. the reciprocal-free dipole identity `a_Q*Lambda=(epsilon-delta_Q)*log`;
5. positive nonmultiple-count increments;
6. exact adjacent-flow divergence on rational vector fibers;
7. dyadic bit-layer factorization and the parity identity `2a_2=1+lambda_2`;
8. seven fail-closed mutation tests.

Retained result:

```text
verdict
PASS_EXACT_TOP_TRANSPOSE_DIGIT_DEPLETION_AND_FLOW_ALGEBRA

finite parameter cases                 6
dyadic layer rows                   3584
all algebraic mismatch counts           0
mutation tests                         7/7
proof-object SHA-256
cfae02e722f534195e9bfef00065e5457b0da1e5a18a96589ea0e9560aa2a7b3

verify.py SHA-256
88f95846b827a4c62e1e23685534b2728c7f279ec807600b7deb7d0376f2e23a
```

The checker does **not** verify:

- the two-frequency zeta source manifest;
- a production signed flow;
- a subexponential quadratic transport-cost theorem;
- `PADT(K)` or `PARC(K)`;
- RH.
