# X-20701 — Directed actual-zeta conditional-frame ladder

This experiment is the first non-synthetic consumer of the two-frame machinery
from PR #206.

## Actual finite operator

At each integer cutoff `c`, it constructs the cutoff-free D-0001 / X-0001
finite Weil block with `N=1` and then restricts it to the two-dimensional even
sector. The producer includes:

- every prime power `q <= c` exactly once;
- the cutoff-free pole block;
- the cutoff-free archimedean block;
- directed digamma/polygamma evaluation;
- explicit outward balls for every omitted geometric correction tail.

No finite archimedean cutoff and no floating eigensign enters the certificate.

## Actual zeta frames

The first two critical-line zeros are produced by
`python-flint/acb.zeta_zeros`. The gate `N(25)=2` is also certified. For each
support the evaluation row is assembled twice:

1. directly in the full `{-1,0,1}` coordinates and projected to the even
   sector;
2. by the closed even Cauchy formula.

The directed rows must overlap coordinatewise.

A frozen dyadic approximation to the ordinary-discovery lowest eigenvector is
used only to choose the one-dimensional near-kernel direction. Its exact
orthogonal complement is formed by integer arithmetic. The exact first frame,
conditional second frame, positive complement block, joint corrected residual,
and Schur floor are then reconstructed from outward intervals.

## Ladder

The retained configuration uses

```text
c = 5, 10, 20, 50, 100, 200,
    500, 1000, 2000, 5000, 10000, 100000.
```

The workflow evaluates the same immutable vectors and zero rows at 256 and 384
Arb bits. Every higher-precision primitive interval must be contained in its
lower-precision counterpart.

## Result classes

```text
CERTIFIED_POSITIVE_ACTUAL_D0001_CONDITIONAL_FRAME_LEVEL
UNRESOLVED_ACTUAL_D0001_CONDITIONAL_FRAME_LEVEL
```

The exact consumer fails closed if a first-frame denominator, second-frame
floor, positive-sector pivot, joint margin, or full Schur ratio touches zero.

## Scope

This is actual zeta data and an actual complete finite D-0001 Weil block. It is
not yet the complete augmented Suzuki low packet required by T-14302. A positive
support ladder in this fixed `N=1` test family is a production calibration and a
concrete conditional-frame result, not a proof of RH.

The proof-facing global continuation must additionally construct growing packet
levels whose outside complement is controlled in the same metric and whose
joint conditional-frame margin satisfies the Issue #207 cofinal rate.
