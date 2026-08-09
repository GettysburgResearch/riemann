# X-90101 — Nonnegative-flow cone, positive GFEP kernels, and sparse-consumer stress test

This package replays the finite identities and numerical reconnaissance accompanying
`L-90101`, `T-90101`, and `O-90101`.

## Run

From this directory:

```bash
python verify.py
```

Required Python packages:

```text
mpmath
numpy
scipy
```

A successful run prints

```text
PASS_X_90101_NONNEGATIVE_FLOW_SPARSE_KERNEL
```

and rewrites

```text
results/verification.json
```

## Assurance layers

### Exact rational layer

`fractions.Fraction` checks:

1. the nonnegative-throughput Green/pixel pairing for three finite networks;
2. reconstruction of arbitrary superharmonic potentials from boundary values and internal charges;
3. 31 threshold-cut decompositions and their exact source pairings.

### High-precision analytic layer

At 70 decimal digits, the script checks:

1. the direct signed-increment definition of `c_p(k)` against the positive Abel form;
2. nonnegativity of every Abel summand in 293 tested kernels;
3. the exact scaling dictionary `c_X(k)=k^(-1/2)c_(X/k)(1)`;
4. the complete multiples-Möbius scaling identity.

The largest retained direct-vs-Abel error is approximately `2.2e-70`.

### Independent finite source identities

For the two stored `T-90007` adversarial sources, the script computes both:

```text
sparse exit trace dot first-entrance vector
```

and

```text
n times the descending producer coefficient A_X(n).
```

The two paths agree to the declared tolerance.  These computations use floating-point logarithms and are reconnaissance, not directed interval certificates.

### LP reconnaissance

SciPy/HiGHS reproduces the tail-budget comparison between the bottom exit pixel and the sparse producer trace.  This layer is explicitly discovery-only.  It is not used in either exact proof.

## Mutation-sensitive points

The exact checks fail if one:

- double-counts repeated children while also using multiplicity-weighted `Q`;
- changes the sign in the Green/Laplacian pairing;
- omits the internal charge atoms from the nonnegative-flow dual;
- drops the Abel terminal interval;
- removes one sparse contact site;
- replaces the full multiples-Möbius transform by a sign-free sum.

## Output digest

`SHA256SUMS` binds the verifier, this README, and the retained JSON result.
