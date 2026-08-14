# Native-root capacity compilation, exact separator, and two fail-closed successor routes

Date: 2026-08-14  
Base: PR #468 at `a41f81466f85d52597c97b41505756a8860698d0`  
Status: **research packet; NRCT and RH unproved**

## Executive result

PR #464 is not a quick unconditional repair in the exact native normalization.

Its finite fixed-window Hall algebra is valuable and survives. But the global
packet must be distinguished from the canonical finite-Euler datum. The latter
is

\[
D_{P_{61},X}
=
c_X+\sum_{m\in\mathcal R_{67},\,m>1}m^{-1/2}c_{X/m},
\]

so its ordinary/detail/benchmark coordinates equal the native datum plus the
positive rough reservoir.

At \(X=136,q=2\), the ordinary reservoir is exactly

\[
\frac1{\sqrt{134}}\log\frac{68}{67}>\frac1{816}.
\]

Thus the ordinary coordinate itself is an exact dual separator: a producer
which uses the canonical packet as current and also retains the rough children
cannot satisfy native one-use capacity.

## What survives from PR #464

```text
fixed-window score Hall                     retained;
same coefficients for score/target/rows     retained;
formal positive endpoint integration        retained;
one global quantizer algebra                retained.
```

What is not supplied is the exact source-disjoint removal of the rough
reservoir and the native \(Y_4\)-slack ledger required by `T-91314`.

## Route B advance

The complete causal profile theorem on PR #467 implies that the stopped-leaf
LP has a canonical basis. The leftmost target fill:

```text
minimizes score;
maximizes every component row;
uses one source submeasure.
```

Therefore a row failure is already a Farkas separator for the full declared
LP. There is no need to search arbitrary stable bases.

The live remaining signs form a finite activation-cell campaign with `185`
possible cutoff nodes below `2000`. A summation-by-parts formula shows that this
gate is strictly weaker than the stopped-leaf Hall prefixes refuted on PR #463.

Broad non-proof reconnaissance found no negative row gate on the integer
corridor through prime `1000` or on `1000` random continuous samples through
prime `5000`. This is motivation only.

## Route C advance

The direct native LP minimizes

\[
\sum_qY_4(q)s(q)
\]

subject to row nonnegativity, source-disjoint children, one-use
ordinary/detail/port capacities and total child mass below `1/8`.

This objective is exactly the endpoint deficit. \(Y_4\)-zero columns are
score-free repair directions. Every finite cell must return either a directed
rational primal certificate or an exact rational dual separator.

## Status

```text
PR464 fixed-window finite algebra          RETAINED
PR464 direct native compilation            EXACTLY SEPARATED
leftmost target-Lorenz optimizer           PROVED
live target-Lorenz cells                   OPEN / FAIL-CLOSED
direct Y4 native LP                        EXACT FORMULATION
PASS_NATIVE_ROOT_CAPACITY_THEOREM          NOT YET
Riemann Hypothesis                         UNPROVED
```
