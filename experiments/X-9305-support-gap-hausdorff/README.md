# X-9305 — Support-gap Hausdorff residual witnesses

Agent: `gpt56-08`  
Issue: #93  
Status: exact checker and exact synthetic separation; Riemann-`xi` production pending

## New primitive

After every zero in an exact ordinate slab `(a,b)` has been certified on the
critical line and removed from

```text
R_T(u) = log |xi(1/2+sqrt(u)+iT)|^2 - selected slab factors,
```

every residual RH factor has squared distance at least

```text
A = min((T-a)^2, (b-T)^2).
```

This support information is stronger than positivity of the residual Stieltjes
measure.

For `u0<u1<u2`, let

```text
L1 = log((u1+A)/(u0+A))
L2 = log((u2+A)/(u0+A)).
```

`L-9307` proves the value-only inequality

```text
L1*(R(u2)-R(u0)) - L2*(R(u1)-R(u0)) >= 0.
```

It also proves that normalized logarithmic-derivative moments form a Hausdorff
moment sequence on `[0,1]`.  The checker implements:

- three-value support-gap chord rows;
- arbitrary finite Hausdorff differences;
- Hausdorff Hankel Rayleigh rows;
- `(1-q)` localizing Rayleigh rows.

## Why this is genuinely stronger

Take the exact synthetic residual

```text
A = 1
R(u) = log(u+1/2).
```

This is a perfectly valid ordinary Stieltjes factor.  Its logarithmic derivative
is completely monotone, and its ordinary Hankel matrix is positive semidefinite.
But its spectral mass lies at `1/2<A`, inside the declared support gap.

At nodes `(0,1,2)`, the new row is

```text
log(2)*log(5) - log(3)^2
  ≈ -0.091371609522601157486582695212017...
```

The derivative hierarchy gives

```text
B_n = 2^n
B_1-B_2 = -2
```

while the ordinary rank-one Hankel control remains exactly zero.  Thus the new
cone separates a hidden inside-gap positive factor that every ordinary
complete-monotonicity test accepts.

## Files

```text
verify_support_gap.py
    Integer/Fraction-only checker.  No special function and no floating point.

certificates/synthetic-inside-gap-factor.json
    Exact strict separation from the ordinary Stieltjes cone.

tests/test_verify_support_gap.py
    Six exact adversarial tests.
```

## Reproduction

```bash
python experiments/X-9305-support-gap-hausdorff/verify_support_gap.py \
  experiments/X-9305-support-gap-hausdorff/certificates/synthetic-inside-gap-factor.json

python -m unittest discover \
  -s experiments/X-9305-support-gap-hausdorff/tests -v
```

Expected classification:

```text
chord-inside-gap          CERTIFIED_NEGATIVE
first-difference          CERTIFIED_NEGATIVE
ordinary-hankel-control   CERTIFIED_NONNEGATIVE
support-localizer         CERTIFIED_NEGATIVE
```

## PR71 reconnaissance note

Applying the chord row after removing only the nearest sixteen empirical line
zeros gives negative ordinary high-precision values, with representative
magnitudes between `1e-34` and `1e-30`.  This is **expected and is not a
counterexample**: another 156 certified slab zeros remain inside the proposed
support gap, so the hypothesis of `L-9307` is not yet satisfied.

This behavior is nevertheless useful.  The row is functioning as a signed
spectral separator and directly measures incomplete slab deflation.  The
production attack must first transport all 172 sign-chain bins from PR #108,
then evaluate the same rows with directed residual intervals.

## Production gate

A production certificate must carry

```text
CERTIFIED_COMPLETE_SLAB_SUPPORT_GAP
```

and an immutable digest binding:

1. the multiplicity-aware total count;
2. complete critical-line isolation of every slab zero;
3. selected-factor residual construction;
4. the exact support lower bound `A`;
5. the direct completed-`xi` primitive table.

The checker rejects a production object without that gate.

## Counterexample semantics

A strict negative production interval is an RH-disproof nomination only after:

- independent review of `L-7501`, `L-9306`, and `L-9307`;
- independent total-count and Hardy-`Z` reproduction;
- independent completed-`xi` or logarithmic-jet production;
- exact normalization review;
- a final upper endpoint below zero.

No Riemann-`xi` negative is claimed by this experiment.