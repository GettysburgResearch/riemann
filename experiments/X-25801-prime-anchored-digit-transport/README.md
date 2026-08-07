# X-25801 — Prime-Anchored Digit Transport algebra replay

Run:

```bash
python experiments/X-25801-prime-anchored-digit-transport/verify.py
```

The checker uses only the Python standard library. It verifies finite
Dirichlet-convolution identities with an integer-valued completely additive
formal logarithm, positive nonmultiple-count increments, dyadic bit-layer
identities, and one exact rational vector-flow identity.

Expected output:

```text
PASS_EXACT_TOP_TRANSPOSE_DIGIT_DEPLETION_AND_FLOW_ALGEBRA
cases 6
mutation tests 7/7
proof-object SHA-256 cfae02e722f534195e9bfef00065e5457b0da1e5a18a96589ea0e9560aa2a7b3
verify.py SHA-256 88f95846b827a4c62e1e23685534b2728c7f279ec807600b7deb7d0376f2e23a
```

## Scope

Verified:

- top-depth logarithmic transposition;
- source-specific `Q`-depletion and exact recovery;
- reciprocal-free dipole algebra;
- positive nonmultiple-count increments;
- dyadic bit-layer and parity identities;
- abstract adjacent-flow divergence.

Not verified:

- the complete zeta source manifest in the two-frequency block;
- any production `PADT(K,J)` flow;
- the quadratic transport-cost theorem;
- `PARC(K)`;
- RH.
