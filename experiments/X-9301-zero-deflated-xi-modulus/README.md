# X-9301 — Certified-zero-deflated direct-xi modulus witnesses

Experiment ID: X-9301  
Agent: `gpt56-01-i`  
Issue: #93  
Status: exact checker and synthetic separation complete; Riemann-xi production pending

## Purpose

This experiment composes three proof interfaces:

1. direct completed-xi rectangles from X-7501;
2. logarithmic modulus Loewner total positivity from L-7504;
3. independently certified critical-line zero lower counts from L-8404 or another
   proof-grade zero-count source.

For a zero bin `I=[a,b]` containing at least `m` critical-line zeros, set

```text
B = max((T-a)^2,(T-b)^2).
```

The checker subtracts

```text
m log(u+B)
```

from the logarithmic modulus at every horizontal node. Under RH this cannot
over-subtract: each selected actual zero has squared distance `y<=B`, and its
residual secant kernel is

```text
integral_y^B ds / ((u+s)(v+s)).
```

The residual is a positive Gram kernel.

## Supported exact rows

### Deflated algebraic monotonicity

For `0<u<v`, RH implies

```text
H(v) product_r (u+B_r)^m_r
>=
H(u) product_r (v+B_r)^m_r,
```

where

```text
H(u)=|xi(1/2+sqrt(u)+iT)|^2.
```

This row uses no logarithm.

### Raw and deflated cross-Loewner determinants

The checker encloses

```text
G(u)=log H(u)
```

or

```text
G_def(u)=G(u)-sum_r m_r log(u+B_r)
```

using exact rational power-of-two reduction and a positive atanh series. It then
forms exact interval secants and determinants through order four.

## Synthetic hidden-offline-zero control

Use

```text
H(u)=(u-5)^2 (u+1)^20.
```

The `(u+1)^20` factor models twenty certified critical-line zeros at squared
distance one. The `(u-5)^2` factor models a reflected off-line pair.

The ordinary two-point row is strictly positive:

```text
H(4)-H(3)=90,969,385,129,521.
```

The deflated algebraic row is strictly negative:

```text
H(4) 4^20 - H(3) 5^20
= -314,572,800,000,000,000,000,000,000.
```

For rows `(3,6)` and columns `(4,7)`:

```text
raw logarithmic Loewner determinant
  approximately +0.8201931072456714

deflated determinant
  = -4 (log 2)^2
  approximately -1.9218120556728058.
```

Thus certified deflation exposes a hidden off-line component while both
undecomposed tests are strictly positive.

These are synthetic exact controls, not Riemann-xi evaluations.

## Verification

```bash
python verify_zero_deflated_modulus.py \
  certificates/synthetic-hidden-offline-zero.json \
  --output /tmp/verification.json

python -m unittest discover -s tests -v
```

Twenty-five tests pass. They cover:

- the strict hidden-offline separation;
- the exact algebraic negative integer;
- overlapping-bin rejection;
- zero and Boolean count rejection;
- production-gate enforcement;
- point-digest mutation;
- row/column collision;
- wider-bin validity;
- X-7501 adapter coordinate squaring;
- missing source points;
- Boolean logarithm-term rejection.

The CLI returns `0` for every resolved arithmetic replay, including a strict
negative, `1` for unresolved intervals, and `2` for rejection. Production
certificates additionally require `--primitive-artifact` and
`--zero-artifact`; their canonical digests must match the certificate before a
negative can be labeled source-bound.

At the PR #71 height, the unscaled completed-xi ball has a binary exponent so
large that expanding its rational denominator during JSON serialization can
request tens of gigabytes. The generated producer therefore multiplies every xi
rectangle by the same exact factor `2^5335951715288`. Logarithmic secants cancel
the resulting common additive constant, while algebraic rows acquire the same
positive factor on both sides. The scale is recorded and source-bound in every
production certificate.

## Production adapter

`adapt_x7501_zero_deflation.py` consumes:

1. an X-7501 `riemann.xi-modulus-witness.v1` directed certificate;
2. a `riemann.xi-modulus-zero-deflation-config.v1` file containing zero bins and
   requested rows.

It squares every exact horizontal offset, copies the primitive rectangles,
preserves source fingerprints, and emits the X-9301 schema. It performs no
special-function evaluation.

## Zero-count gates

Production bins must carry

```text
CERTIFIED_CRITICAL_LINE_ZERO_LOWER_BOUND
```

and a 64-hex digest. The arithmetic checker does not fabricate that proof. A
valid source may be:

- a directed Hardy-Z sign change at exact endpoints;
- a proof-grade critical-line zero isolation/counting routine;
- another independently reviewed multiplicity lower bound.

A total-zeta-zero count is not a substitute for a critical-line lower count.

## Suggested first production targets

1. the exact PR #71 large-gap ordinate, after tight bins are certified around the
   bracketing critical-line zeros;
2. the four high-height carrier windows already supported by the Riemann-Siegel
   Arb backend;
3. new ordinates ranked by large ordinary positive line-zero mass, since those
   are precisely the windows where deflation can improve the most.

At each target:

1. check deflated monotonicity first;
2. check interlaced order-two determinants;
3. escalate to orders three and four;
4. refine only the xi rectangles and zero bins dominating the interval width.

## Proof boundary

Exact in this experiment:

- rational parsing and interval arithmetic;
- modulus-square enclosure;
- farthest-endpoint squared-distance bounds;
- disjoint-bin and count checks;
- rational logarithm enclosures;
- secant and determinant contraction;
- source/point/gate fingerprints;
- synthetic separation.

External:

- direct completed-xi primitive provenance;
- actual critical-line zero-count certificates;
- L-9301 analytic review;
- independent special-function reproduction of any negative result.

No Riemann-xi negative interval or counterexample is claimed.
