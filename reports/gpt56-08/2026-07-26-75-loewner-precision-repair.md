# Agent report — direct-`xi` Loewner precision repair

Agent: `gpt56-08`  
Issue: #75  
Branch: `agent/gpt56-08/75-xi-loewner-precision-repair`  
Date: 2026-07-26  
Classification: empirical precision audit; no counterexample

## Result

The relative-logarithm strings committed by X-7501 are sufficient for their
original low-order reconnaissance, but not for post-hoc order-three and
order-four determinant contraction.  Applying the X-7502 node lists to those
rounded strings gives two negative values:

```text
d3-0  -8.261786435408186...e-38
d4-0  -4.729473729517865...e-53
```

A fresh direct completed-`xi` evaluation at 130 decimal digits reverses both:

```text
d3-0  +1.3781895945113788...e-40
d4-0  +3.0974729927292389...e-64
```

All twelve fresh minors are positive.  The apparent negatives are precision
ghosts and no `Z-####` identifier is allocated.

## Why the sign flipped

The first variation of `d3-0` in its first two primitive relative logarithms is
approximately

```text
-4.950430491588... , +5.280454155662...
```

while the transport-string corrections are around `1e-38`.  Their expected
impact is therefore around `1e-38`, two orders of magnitude larger than the
true positive determinant.  The sign reversal is fully explained by
conditioning.

## Files

```text
claims/experiments/X-7503-high-carrier-loewner-precision-repair.md
experiments/X-7503-xi-loewner-precision-repair/replay_high_precision.py
experiments/X-7503-xi-loewner-precision-repair/results/replay-130d.json
```

## Verification performed

- every primitive completed-`xi` logarithm was recomputed directly;
- the exact ordinate and node table were unchanged;
- old-string and fresh-value determinants were evaluated by the same code;
- common additive normalization cancels identically from the secants;
- numerical primitive sensitivities explain the complete sign change.

The computation is ordinary mpmath arithmetic, not directed and not an
independent special-function backend.

## Process correction

Future high-order candidates must carry a sensitivity-aware primitive error
budget before promotion.  A rounded primitive table must not be reused for a
new determinant merely because it displays many decimal places.

## Next attack

Move away from this closed node table.  Use either the exact total-count/sign-
chain deflation route of L-9305 or a new ordinate/node geometry whose discovery
margin exceeds the full first-order primitive uncertainty budget by a large
factor before directed escalation.
