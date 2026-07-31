# X-15302 — Exact zero-evaluation obstruction

This is the finite arithmetic companion to `L-15304`.

## Purpose

A complete low-symbol packet should not automatically be identified with a
small-tail radical packet. Exact global radical transforms vanish at every zeta
zero. Certified zero evaluations can therefore prove that an evaluation-visible
subspace stays a positive distance from every localized radical truncation whose
exterior tail is small in the same Hardy metric.

## Exact finite gate

For a packet basis, the certificate supplies:

```text
H       metric Gram matrix
G       certified-zero evaluation Gram matrix
s^2     lower generalized singular-value square
C^2     upper square of the Hardy evaluation-operator norm
q       rational lower bound for s/C
epsilon radical-tail upper bound.
```

The checker proves

```text
G - s^2 H > 0,
q^2 C^2 <= s^2,
```

and returns the exact obstruction

```text
distance >= q - epsilon.
```

A production packet may replace strict positive definiteness by a separately
certified semidefinite factorization, but this first checker intentionally uses
strict rational LDL and fails closed.

## Retained synthetic control

```text
H                    identity_2
G                    diag(4,1)
s^2                  1/2
C^2                  2
q                    1/2
tail upper           1/10
distance lower       2/5
```

Verification SHA-256:

```text
475f0f5955170c08c6cf2477d0d60f90dde71ea3539e21593ea8704bcf87d054
```

## Reproduction

```bash
python experiments/X-15302-zero-evaluation-obstruction/verify.py \
  experiments/X-15302-zero-evaluation-obstruction/certificates/synthetic.json

python -m unittest discover \
  -s experiments/X-15302-zero-evaluation-obstruction/tests -v
```

## Production handoff

1. build the complete finite low-symbol packet;
2. evaluate its basis at proof-grade critical-line zeros;
3. construct an exact rational lower bound for the visible singular block;
4. split off a rational near-kernel basis;
5. apply radical repair only to that near-kernel;
6. directly certify the visible block in the final Schur matrix.

## Trust boundary

The checker does not verify that supplied evaluations come from zeta zeros, that
the basis has the declared Hardy Gram matrix, or that the operator constant is a
valid analytic bound. It checks only the exact finite implication after those
source gates are bound.