# X-16208 — complete Poisson alias moat at gamma = 4096

This experiment closes the production field deliberately left null by
`X-16207`:

```text
complete_arithmetic_alias.cross_error_upper
```

for the repaired CCM packet with modes `0,4,8,12` at `gamma=4096`.

The proof object combines:

- exact rational localization of every finite-alias stationary point;
- an exact interval proof of the amplitude/curvature weight;
- both incoming/outgoing stationary branches;
- nonstationary higher-alias integration by parts;
- the nondegenerate Airy transition;
- normalized radial outgoing endpoint/polylogarithm channels;
- the post-cutoff alias remainder;
- source-bound ODE/template and finite-cell enclosure errors.

The midpoint matrix

```text
[[-0.00513, 0.01017],
 [ 0.01017, 0.00858]]
```

is a floating diagnostic only. The proof uses the outward operator budget.

## Directed result

```text
operator budget reconstructed       0.8297864380283328...
C_cross operator upper              27/32 = 0.84375
required threshold                  0.9999999
complete arithmetic Gram lower      0.1562499
complete arithmetic Gram upper      18
```

The bound source packet is promoted to

```text
PRODUCTION_PROFILE_GRAM_CLOSED
```

and the hardened wrapper gives

```text
good support measure lower          13/16
relative scalarization epsilon      <31/32
ground correction ratio             63/563 <1/8
```

## Cofinal bound

With alias cutoff `K=floor(sqrt(gamma))` and Airy scale
`q=floor(cuberoot(gamma))`, the same ledger gives

```text
||C_cross(gamma)||
 <= 18/sqrt(gamma) + 2/cuberoot(gamma) + 1792/gamma.
```

This tends to zero. At the next scheduled block `gamma=32768`, the bound is
`5019/23168`, approximately `0.21664`.

## Replay

```bash
python verify.py certificate.json --output results/verification.json
python -m unittest discover -s tests -v
```

No RH proof is claimed. This experiment closes the finite complete-alias/profile-
Gram moat. A cofinal RH argument still requires source-bound passing blocks on
an unbounded support sequence and an independent verification of the CCM
finite-real-zero implication.
