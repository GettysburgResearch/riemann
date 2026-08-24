# Report: reviewed unconditional simple-zero improvement

## Verdict

The seven-gap stability refinement survives hostile reconstruction. The exact
simple-zero theorem is unconditional and source-qualified:

\[
\liminf\frac{N_0^s(T,2T)}{N(T,2T)}
\ge0.673008527927557\ldots .
\]

## Principal audit repair

The similarly valued theorem in `Zeta23/ThmD/Final.lean` concerns `N0star`.
The correct input for simple zeros is the separate no-hypothesis theorem
`Zeta23.ThmD.thmD₀_simple_mult` in `ThmD/Mult.lean`. The packet freezes this
path and blob explicitly.

## Finite certificate audit

The seven-gap verifier was inspected at the exact external commit. It uses Arb
for transcendental enclosure, outward widening for every binary64 operation,
three independent pruning tests, and a fail-closed terminal rule. The frozen
certificate reports the exact target `F6 >= 19/5000` after 707,901 nodes.

An independent GitHub Actions replay was prepared on temporary PRs #753 and
#754. The GitHub App publication environment did not expose a run, so no second
execution is claimed. The published external certificate remains the
source-qualified computer-assisted input.

## New analytic theorem

The positive zero set of the overlap kernel is sum-free. Compactness therefore
gives a strictly positive three-point pressure without computation. This
already proves a strict unconditional improvement over `H0`; the seven-gap
certificate supplies the explicit stronger constant.

## Boundary

This result does not imply 90% or RH. The topological companion-dipole frontier
of T-105550 remains the live route toward a much larger proportion.
