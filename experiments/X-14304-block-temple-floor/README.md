# X-14304 — Exact block Temple–Schur floor checker

This experiment implements the finite arithmetic interface of `L-14308`.
It does **not** evaluate zeta functions, prime sums, prolate functions, or an
ambient Weil operator.  After JSON parsing, it uses only Python integers and
`fractions.Fraction`.

## Mathematical packet

The certificate supplies

```text
A = [ B   R* ]
    [ R   C  ]
```

on a declared low packet plus its complete complement, together with a positive
complement metric `M` and exact rationals `gamma,h` satisfying

```text
C - gamma I - h M > 0.
```

The checker forms

```text
K = B - h^-1 R* M^-1 R
```

and proves a rational floor `F` by exact positive `LDL*` pivots for `K-FI` and
the comparison `gamma >= F`.  A separately certified ambient operator/form
radius `delta` is then subtracted:

```text
inf spectrum(A_exact) >= F-delta.
```

Production packets are rejected unless their radius is bound to a
`CERTIFIED_OPERATOR_NORM_RADIUS` gate.

## Synthetic squared-residual control

The retained one-dimensional packet has

```text
B = 0,
R = 1/1000,
C = 1 + 2/1000,
M = 1,
gamma = 1,
h = 1/1000.
```

Its exact diagnostics are

```text
dual residual squared     1/1,000,000
distance ratio squared    1
energy penalty            1/1,000
corrected low scalar     -1/1,000
certified floor          -1001/1,000,000
```

The projective residual/gap ratio does not improve at all, while the spectral
floor error tends to zero in the corresponding epsilon family.  This is the
strict separation used by `T-14302`.

Exact proof-object SHA-256:

```text
bdc5d3a7d70ae9fe048411d2195f6c18de2323015a86c9e85ac8e9fd6de09463
```

## Reproduction

```bash
python experiments/X-14304-block-temple-floor/verify.py \
  experiments/X-14304-block-temple-floor/certificates/synthetic-squared-residual.json \
  --output /tmp/x14304-result.json

python -m unittest discover \
  -s experiments/X-14304-block-temple-floor/tests -v
```

Expected test result:

```text
9 tests, all passing
```

## Production schema

A production certificate uses

```json
{
  "schema": "riemann.x14304-block-temple-floor.v1",
  "classification": "RIEMANN_WEIL_DIRECTED",
  "blocks": {"B": [], "R": [], "C": [], "M": []},
  "gamma": {},
  "h": {},
  "claimed_midpoint_floor": {},
  "operator_radius": {},
  "operator_radius_gate": {
    "status": "CERTIFIED_OPERATOR_NORM_RADIUS",
    "sha256": "..."
  }
}
```

All matrix entries and scalars are integers or rational objects with integer
numerator and positive denominator.

## Trust boundary

The checker certifies finite rational algebra only.  A Riemann-Weil conclusion
also needs independent proof that:

1. the low block, cross map, complement block, and metric represent the stated
   exact ambient form;
2. the complement coercivity includes every omitted mode;
3. the operator/form radius is rigorous;
4. all vectors lie in the declared domains;
5. the localized Weil normalization agrees with the source theorem.

A positive finite compression without those gates is not an ambient lower
bound.
