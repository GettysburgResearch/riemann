# Wider meaning of the scalar supersolution obstruction

Agent: `gpt56-05-l`  
Date: 2026-07-31  
Issue: #154

## Executive conclusion

The scalar Barta no-go does not indicate that the odd localized Weil form has a
large negative direction. It identifies an illegal separation of two
exponentially large, phase-correlated terms.

For an odd packet concentrated in endpoint layers of scaled width `1/a`, the
negative polar channel contributes

```text
-2 exp(a) |Laplace_(1/2)(phi)|^2 + lower order.
```

Prime powers in the moving terminal window contribute

```text
+2 exp(a) |Laplace_(1/2)(phi)|^2 + lower order.
```

The prime number theorem proves the cancellation. The scalar local transform
retains the negative potential but discards the endpoint-reflection Hankel
energy, explaining the universal mean obstruction.

## New structural objects

- `L-15404`: exact endpoint overlap formula and PNT pole cancellation.
- `T-15402`: RH-equivalent translation boundedness of the pole-subtracted
  logarithmic prime distribution.
- `M-15402`: proof-producing terminal-prime Hankel search.
- `X-15403`: exact rational convolution regression; eight tests pass.

## Exact arithmetic control

For profile `(1,-2,3)`, ratio `1/2`, and pole scale `7/3`, the finite convolution
identity gives

```text
prime pole main  +21/8
polar main       -21/8
sum                0.
```

A separate synthetic discrepancy remains `-288/35`, demonstrating that the
zero-sensitive remainder must be tracked after the pole is removed.

## Positive and negative implications

### Positive

RH is equivalent to boundedness, under logarithmic translation, of every fixed
smooth pole-subtracted terminal prime window. A proof must control the
zero-spectrum remainder. PNT cancellation alone is only the first asymptotic
layer.

### Negative

A right-half-plane zero creates an exponentially growing oscillatory term in a
suitable terminal-window contraction. A finite polarized endpoint packet can
turn that term into a negative Weil value along a support sequence. This gives a
new existentially complete counterexample family whose prime side uses only a
fixed small prefix and a moving terminal window.

## Relationship to PR #152

The endpoint Hankel block is a concrete phase-aware low packet. It supports the
central lesson of `L-14312`--`L-14315`: negative directions, if they exist, move
through support-dependent coordinates and cannot be controlled by fixed scalar
rows. The corrected low block or a phase-aware terminal packet is not an
artifact of the proof architecture; it is mathematically forced.

## Remaining boundary

No uniform terminal-window bound and no negative Riemann packet has been
produced. The new criterion is exact but RH-equivalent. It sharpens the target
and provides a new finite search interface; it does not silently claim a
resolution.
