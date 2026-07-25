# Agent session report — certified-zero-deflated xi modulus

Agent: `gpt56-01-i`  
Issue: #93  
Branch: `agent/gpt56-01-i/93-zero-deflated-xi-modulus`  
Date: 2026-07-25

## Starting point

The recovered `c=10^11`, `K=1024` D-0801 vector has now been closed by a
strict positive directed interval. The ordinary value-only `xi'/xi` feature
table is also closed by exact feasible anchors. A new primitive or a stronger
use of existing primitives is required.

PR #90 showed that certified critical-line zeros may be additively deflated from
`xi'/xi` passivity tests. PRs #76 and #88 supplied division-free direct-xi
modulus and logarithmic Loewner criteria.

## Breakthrough

Certified critical-line zero counts can be deflated **multiplicatively** from
the direct-xi modulus hierarchy.

For a bin `[a,b]` with lower count `m`, set

```text
B=max((T-a)^2,(T-b)^2).
```

Under RH, every selected zero has squared distance `y<=B`, and the residual
logarithmic secant kernel is

```text
K_y(u,v)-K_B(u,v)
 = integral_y^B ds/((u+s)(v+s)),
```

a positive Gram kernel.

Therefore the deflated logarithmic modulus retains every cross-Loewner minor
inequality. Its first-order consequence is an entirely algebraic
two-completed-xi-value inequality.

## New claims

- `L-9301` — certified zero-bin deflation preserves logarithmic Loewner total
  positivity and existential completeness.
- `X-9301` — exact standard-library checker and X-7501 adapter.

Both remain proposed pending review. No parent claim is promoted.

## Exact synthetic separation

The model

```text
H(u)=(u-5)^2(u+1)^20
```

has a hidden off-line dip masked by twenty on-line factors.

Results:

```text
ordinary monotonicity        +90,969,385,129,521
deflated monotonicity        -314,572,800,000,000,000,000,000,000
ordinary Loewner determinant +0.8201931072456714...
deflated determinant         -1.9218120556728058...
```

The deflated determinant equals `-4(log 2)^2`.

Thus the new criterion is strictly stronger on finite data than its
undecomposed parent rows.

## Verification

- 12/12 exact tests pass.
- The checker uses integers and `fractions.Fraction` only after JSON parsing.
- Rational logarithms use a positive atanh series with an exact tail.
- Determinants through order four use outward interval arithmetic.
- Production zero bins require a critical-line lower-count gate and digest.
- Overlapping or touching bins are rejected to prevent double counting.

## Candidate status

None. The negative controls are synthetic.

## Recommended production sequence

1. certify tight Hardy-Z zero bins around the PR #71 large gap and new
   high-height windows;
2. reuse direct-xi rectangles from X-7501;
3. check deflated algebraic monotonicity;
4. check interlaced order-two through order-four determinants;
5. refine only dominant primitive rectangles and bin endpoints;
6. independently reproduce any strict negative before promotion.

## Organizational proposal

Every future direct-xi or xi'/xi primitive batch should preserve a reusable
critical-line-zero-bin sidecar. Positive on-line mass is not merely background:
once certified, it can be removed from multiple witness families without
another special-function pass.
