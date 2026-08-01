# Source-derived production-moat continuation — corrected relative normalization

## Published prefix

The prepared X-16205 cofinal-prefix status and digest manifest were committed to
PR #164 in commit

```text
e75294743d155affaf0ae2ea4a586a06524c3e4b
```

and the first X-16207 source-derived stack in

```text
18cb1a1befbfc51aae7706c63a1024573d756f1c.
```

## Valid actual gamma=4096 source data

The directed infinite Legendre--Jacobi calculation resolves the modes
`0,4,8,12`, their concentration defects, and the exact repaired columns. The
normalized coefficient-tail synthesis gives

```text
radial tail L2 squared              <= 1e-4181
frequency-derivative tail L2^2      <= 1e-4174
horizontal-strip tail L2^2          <= 1e-4180
first-alias Gram                    [0.9999999,1.0000001]
```

These quantities were divided by the exact positive-ray leakage norms and
remain valid.

## Correction to the endpoint claim

The first X-16207 certificate incorrectly inserted an absolute compact-source
bound `||f^(4)||_1<=45000` into the endpoint remainder for a unit tail profile.
The correct bound contains

```text
||f^(4)||_1/sqrt(first_alias_energy).
```

At gamma=4096 the logarithms of the two first-alias energies are approximately
`-3538.8421` and `-3524.1072`, so the omitted divisor changes the scale by about
`10^1769` and `10^1762`. The previously reported endpoint charges and
`1/40000` deterministic error are withdrawn.

`R-16205` records the refutation. `X-16207` v2 now returns

```text
RADIAL_DERIVATIVE_CLOSED_NORMALIZED_ENDPOINT_OPEN
```

and refuses downstream binding.

## Correct remaining production moat

Two fields must be emitted from one normalized radial phase/ODE replay:

1. the normalized endpoint channels plus a relative exterior remainder;
2. the complete Poisson cross-alias operator bound and full Gram upper bound.

Only after both are present does `bind_downstream.py` populate X-16204.
No new support block should be generated before this one-block relative profile
moat closes.

No RH proof is claimed.
