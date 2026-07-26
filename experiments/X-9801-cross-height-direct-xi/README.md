# X-9801 — Cross-height algebraic direct-`xi` portfolios

This experiment implements `L-9801` with a small trusted boundary.

For several exact heights it consumes direct completed-`xi` squared-modulus
intervals and integer exponent vectors whose sum is zero at every height. It
reconstructs the positive quadratic-factor products

```text
A(z) = product_{n>0} ((z-(T-origin))^2+u)^n
B(z) = product_{n<0} ((z-(T-origin))^2+u)^(-n)
```

and accepts the initial polynomial cone only when an exact Sturm sequence proves
`A-B` has no real root and `A(0)-B(0)>0`. It then contracts

```text
product_{n>0} H_T(u)^n - product_{n<0} H_T(u)^(-n)
```

using nonnegative rational interval arithmetic.

No checker path evaluates a special function, logarithm, floating point, or
`xi'/xi`.

## Files

```text
verify.py
    Fraction-only polynomial/Sturm and product-interval checker.

build_from_pr105.py
    Binds the retained PR #105 p192/p256 primitive rectangles to one exact
    candidate.

generate_manifest.py
    Reconstructs the seventeen small-integer symmetric-height polynomial
    candidates and their proof-object digests.

candidates/symmetric-pr105.json
    Immutable candidate manifest.

certificates/synthetic-negative.json
    Exact strict synthetic separation with product difference -7.

results/synthetic.json
    Exact checker output for the synthetic control.

results/pr105-midpoint-reconnaissance.json
    Ordinary positive midpoint values for the first two candidates.

tests/test_verify.py
    Eight fail-closed adversarial tests.
```

## Exact local controls

```bash
python -m unittest discover -s tests -v
python verify.py certificates/synthetic-negative.json \
  --output results/synthetic.json
python generate_manifest.py
```

Expected synthetic verdict:

```text
SYNTHETIC_STRICT_SEPARATION
product difference = -7
response polynomial distinct real roots = 0
```

## PR #105 production replay

The workflow

```text
.github/workflows/pr105-cross-height-direct-xi.yml
```

uses the retained symmetric height tables

```text
T0-5/16  max-mass-jm25
T0       pr71
T0+5/16  positive-control-jm5
```

at 192 and 256 bits. For every manifest row it:

1. verifies source schema, normalization, exact ordinate and functional equation
   gates;
2. converts each complex rectangle to an exact squared-modulus interval;
3. reconstructs the exact response polynomial;
4. runs the Sturm gate;
5. contracts the integer product row;
6. requires the p256 final interval to nest in the p192 interval;
7. nominates only a strict negative p256 upper endpoint.

A positive complete run excludes only these seventeen portfolios on this exact
symmetric triple. A negative is a finite nomination pending independent
completed-`xi` reproduction and review of `L-9801`.

## Discovery discipline

Polynomial validity and Riemann-`xi` sign are separate layers.

- A valid response polynomial is an exact reusable candidate.
- A negative midpoint is empirical.
- An interval meeting zero is unresolved.
- Only a strict directed negative is a counterexample nomination.
