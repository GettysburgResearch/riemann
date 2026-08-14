# Euler-shell recovery and exact remaining producer

Date: 2026-08-14  
Authoring model: GPT-5.6 Pro  
RH status: **unproved**

## Executive result

The native-root correction packet is extended by an exact Euler survival-shell
convexification, positive shell output densities, and a new logarithmic-debt
consumer.  Two tempting shortcuts are fenced:

1. the canonical `P_61` finite-Euler row is not native-capacity admissible;
2. global canonical shell-row positivity contains the full native Möbius row
   and is therefore not a weaker producer target.

The logarithmic-debt calculation is valid only per unit target mass.  It does
not close the unnormalized native root, whose target mass is on square-root
scale.  `R-91315` therefore blocks the zero-row shortcut.  The remaining
producer must still realize the leading benchmark through a nonnegative current
row while routing source-disjoint children without duplicating the rough
reservoir.

## New exact chain

```text
native normalization and rough-reservoir firewall   L-91377--L-91380
Euler factor = survival/shell convexification        L-91381
shell ordinary/detail/entropy densities positive     L-91382
shell row = positive Green bulk + finite boundary    L-91383
canonical global shell positivity native-row hard    R-91314
zero-row causal debt <= 5 log(3X) target mass         L-91385
subcritical normalized recurrence -> O(log X)        T-91316
zero-row native closure                               FALSE / R-91315
positive native current-row producer                  OPEN / T-91314
```

## Why logarithmic local debt is sufficient

The earlier provenance route asked for an absolute constant local debt.  That
is unnecessarily strong.  If child mass contracts by `theta<1`, then

\[
 \Lambda(X)\le C\log(3X)+\theta\Lambda(X/R+C_0)
\]

implies

\[
 \Lambda(X)=O(\log X)=o(\log^2X).
\]

For a positive component packet,

\[
 E(Y)\le4(4\sqrt Y-3)\log(3Y).
\]

For a causal prime residual with `p>=67`, its target remains at least
`66/67` of the parent target.  The zero row is therefore a complete local
producer with debt at most `5 log(3Y)` times target mass.

## Exact open theorem

Construct the Native-Root Capacity Theorem of `T-91314`: one nonnegative
current row and source-disjoint contracted children, all inside the native
ordinary/detail capacities, with absolute `o(log^2 X)` weighted slack.  The
current row must realize the square-root leading benchmark; a normalized
logarithmic target-mass bound is insufficient.

## Verification

```text
X-91143: PASS_EULER_SHELL_RECOVERY_AND_FIREWALL
```

The replay is deliberately scoped.  It does not certify HTE, CFFP, or RH.
