# X-9301 — Certified-zero-deflated direct-xi modulus witnesses

Experiment ID: X-9301  
Agent: `gpt56-01-i`  
Issue: #93  
Status: exhaustive disjoint PR #71 grid certified positive through 256 nearest zeros

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

using exact rational power-of-two reduction and an outward-rounded dyadic
evaluation of the positive atanh series. The fixed-point enclosure keeps
intermediate denominator sizes bounded without changing the rigorous positive
tail estimate. It then
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

Forty-two exact tests pass. They cover:

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
- Boolean logarithm-term rejection;
- production source reconstruction and adversarial re-signing;
- fixed-point logarithm enclosure against the exact positive series;
- nearest-zero selection and precision nesting;
- complete-ladder summary binding and input-digest drift.

## Globally-nearest guard

Sorting only the balls emitted by a finite block does not prove that the chosen
prefix is globally nearest: an un-emitted predecessor or successor could be
closer. The nearest-zero builder therefore requires a consecutive indexed block
with an unselected exterior guard on each side. It proves, using exact rational
bounds, that the largest selected distance upper bound is strictly below every
unselected distance lower bound. The source-bound verifier independently
reconstructs this separation.

The production workflow emits 320 consecutive Hardy-zero balls, retains the
globally nearest 256, and leaves 64 guard balls.

## Exhaustive fixed-grid scan

`summarize_pr71_exhaustive_grid.py` deterministically generates every
derivative-free disjoint row available from the nine primitive nodes. Up to
row/column transpose, the order-`k` determinant count is

```text
binomial(9, 2k) binomial(2k, k) / 2.
```

The resulting rung contains 36 monotonicity rows, 378 order-two minors, 840
order-three minors, and 315 order-four minors: 1,569 exact rows in total. The
script checks canonical pattern coverage before replay, source-binds both
precisions and the guarded zero block, requires precision nesting, and records
a compact digest of every final interval.

The CLI returns `0` for every resolved arithmetic replay, including a strict
negative, `1` for unresolved intervals, and `2` for rejection. Production
certificates additionally require `--primitive-artifact` and
`--zero-artifact`. Before any expensive determinant replay, the verifier checks
their canonical digests and reconstructs the ordinate, squared nodes, completed-
xi rectangles, selected zero indices, zero-bin bounds, counts, and gate digests.
A re-signed certificate that drifts from either producer artifact is rejected.

At the PR #71 height, the unscaled completed-xi ball has a binary exponent so
large that expanding its rational denominator during JSON serialization can
request tens of gigabytes. The generated producer therefore multiplies every xi
rectangle by the same exact factor `2^5335951715288`. Logarithmic secants cancel
the resulting common additive constant, while algebraic rows acquire the same
positive factor on both sides. The scale is recorded and source-bound in every
production certificate.

## Production adapter

`adapt_x7501_zero_deflation.py` consumes:

1. an X-7501 `riemann.xi-modulus-witness.v1` synthetic certificate;
2. a `riemann.xi-modulus-zero-deflation-config.v1` file containing zero bins and
   requested rows.

It squares every exact horizontal offset, copies the primitive rectangles,
preserves source fingerprints, and emits the X-9301 schema. It performs no
special-function evaluation.

The generic X-7501 adapter is synthetic-only until it accepts a reviewed
zero-source artifact and can reconstruct all production zero bins. PR #71
production uses the dedicated gap and indexed-Hardy-block builders.

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

## Retained PR #71 production result

The source-bound local replay was extended to 192, 256, 384, and 512 bits. A
block of 320 consecutive indexed Hardy-zero balls certifies the globally nearest
256 and leaves 64 exterior guards. At 512 bits, all 240 originally declared
cells are strictly positive: 20 fixed rows at each cumulative rung
`2, 4, 8, 16, 32, 64, 96, 128, 160, 192, 224, 256`.

All twelve determinant sequences descend strictly across every rung. The
tightest final interval is the order-four row `d4-0`:

```text
6.85769045758189919e-116
<
d4-0 (256 globally-nearest zeros)
<
6.85769045758190802e-116.
```

The exhaustive scan closes every derivative-free disjoint row on the same
nine-point grid. All 18,828 cells (1,569 rows at twelve rungs) are strictly
positive at 512 bits, and all 1,533 determinant sequences descend strictly. The
tightest final row separates the four smallest nodes from the next four:

```text
rows    = (x-20, x-18, x-16, x-14)
columns = (x-12, x-10, x-8, x-6)

4.26598510145821543e-128
<
det
<
4.26599336658844784e-128.
```

The retained verdicts are `CERTIFIED_POSITIVE_FIXED_PR71_TABLE` and
`CERTIFIED_POSITIVE_EXHAUSTIVE_DISJOINT_PR71_GRID`; no counterexample is
nominated. This closes only the exact ordinate, nine-point value-only grid, and
twelve cumulative zero subsets. See `results/pr71/summary.json` and
`results/pr71/exhaustive-grid-summary.json`.

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
