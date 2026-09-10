# A constructive Lee--Yang route for the actual theta law

**Proposed research programme and a certified finite seed; not an RH proof.
Independent mathematical and code review required.**

Instead of trying to symmetrize the nonnormal operator in PR #834, construct
finite ferromagnets whose magnetization laws converge to the exact normalized
theta law. Lee--Yang gives every finite model's global zero-location theorem
before taking the limit. Known weak-closure theory then proves the desired
property of the limit. The all-order source construction remains OPEN.

Read [PROPOSAL.md](PROPOSAL.md), then [REVIEW.md](REVIEW.md).

## Completed scope

1. A precise inverse moment-synthesis target, and a quantitative full-complex-
   compact convergence bound. Variance one and Lee--Yang structure supply the
   entire tail control. This applies classical Lee--Yang/Hadamard/Newman--Wu
   theory; it is not claimed as a new abstract closure theorem.
2. A finite 4104-spin ferromagnet exists whose weighted magnetization matches
   the ACTUAL standardized theta law through moment six, exactly. It consists
   of an eight-spin complete ferromagnetic block and 4096 independent spins.
   Only 28 couplings are nonzero. Directed theta-integral bounds and rational
   interval algebra certify the intermediate-value construction. It does not
   require a Gaussian limit, actual zero values, or numerical root counting.
3. The literal Jacobi integer-square theta sum is exactly a zero-field Villain
   cycle partition function. The current expansion identifies a structural
   source connection, but temperature is NOT magnetic field. The needed
   temperature-to-field / whole-law identification is not proved.

## The decisive open theorem

For each r, construct a finite zero-field Ising ferromagnet with nonnegative
magnetization weights, variance one, and moment errors at most 1/r through
order 2r against the exact theta law. A six-moment instance is not an induction.
No converse from RH to this ferromagnetic subclass is claimed.

## Reproduce the source certificate

```sh
python -I -S -B certify_seed.py --check seed_certificate.json
python -I -S -B -O certify_seed.py --check seed_certificate.json
python -I -S -B test_seed.py
python -I -S -B -O test_seed.py
```

The first two commands recompute every quadrature node, both complete omitted
tails, the finite-spin endpoint signs, and all 128 parameter subintervals.
The tests are bounded algebra checks, not proofs of the external Lee--Yang
theorem or of the open construction. All numerical constants used in acceptance
are outward integer/Fraction computations. See [VALIDATION.md](VALIDATION.md).

Earlier PR #296 mentions Lee--Yang in a different Brownian/Robin proposal.
This is a new explicit construction programme in this branch, not a claim
that the historical Lee--Yang/RH connection has just been discovered.
