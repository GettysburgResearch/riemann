# X-14301 — Exact prolate ground-state certificate kernel

This directory contains a fail-closed rational verifier for the finite linear
algebra in L-14301.  It certifies that an interval-enclosed, parity-commuting
symmetric matrix has a unique simple even ground state near a declared even
candidate.  An optional exact weighted Gram block certifies the projective
Hardy-strip target bound used by T-14301.

## Reproduce

From the repository root:

```bash
python3 -m py_compile \
  experiments/X-14301-prolate-ground-certificate/verify.py

python3 -m unittest discover \
  -s experiments/X-14301-prolate-ground-certificate/tests -v

python3 experiments/X-14301-prolate-ground-certificate/verify.py \
  experiments/X-14301-prolate-ground-certificate/certificates/synthetic-exact.json \
  --output experiments/X-14301-prolate-ground-certificate/results/synthetic-exact-verification.json

sha256sum -c experiments/X-14301-prolate-ground-certificate/SHA256SUMS
```

The verifier uses only the Python standard library and `fractions.Fraction`.

## Certificate schema

Required top-level fields:

```text
schema
matrix_interval.lower
matrix_interval.upper
parity_permutation
candidate
even_complement_basis
odd_basis
midpoint_residual_norm_upper
midpoint_gap_even
midpoint_gap_odd
```

All scalar values must be integers, rational strings such as `"17/31"`, or
objects with integer `numerator` and `denominator` fields.

The basis vectors are stored as rows.  They need not be orthonormal, but they
must have the exact expected dimensions and ranks.  The shifted congruence
matrices are checked by exact unpivoted LDL.

Optional block:

```text
weighted_projective.gram
weighted_projective.candidate_norm_upper
weighted_projective.even_complement_factor_upper
weighted_projective.target_tail_upper
```

The optional block proves a weighted target-line bound conditional on the
identity and provenance of the supplied Gram and tail data.

## Fail-closed boundary

The checker does not prove:

- that the matrix is a Connes–Consani–Moscovici truncated Weil matrix;
- that every exact matrix in generic entry boxes commutes with parity;
- that the weighted Gram is the T-14301 Hardy-strip Gram;
- that the target tail belongs to the explicit prolate function;
- that any asymptotic sequence of certificates exists.

Those are explicit upstream gates in M-14301.
