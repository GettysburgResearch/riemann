## Purpose

Publish the recovered packet as a distinct successor to PR #576 at exact head
`0f6ea6eae813c1d867ae50744cf5fd57e2720bb7`, under a collision-free namespace.
The mathematical reconstruction itself freezes PR #565 at
`339e3367660f40c74795802a6f8170b15e19b13a`.

The recovered work replaces PR #565's false
`1/40` bias claim by the exact global theorem, and reconstruct the complete
source interface rather than stopping at scalar arithmetic.

## Exact scalar result

```text
unique minimizer: x=184
F(184)/M(184):
0.02398429355876630467327315865313747748...

1199/50000 < F/M < 9/200 for every x>=67
1199/50000 - 1/42 = 179/1050000
```

The proof object enumerates every compact real cell, both directed endpoint
states, all `P61` and `P37` finite-color events, and the complete analytic tail.
It includes an independent 448-bit targeted reconstruction.

## Source reconstruction

The improved scalar bound does not close PR #565. At `X=184`, its low-child
recombination deletes the six genuine rough-prime terms for
`p=67,71,73,79,83,89`. Their total is a directed positive quantity
`>1.3631478826704517`, so the packet observes `F61(184)` rather than the native
annular scalar.

A no-go theorem then rules out every fixed-cutoff repair that expands native
rough children individually and controls arbitrary parity by a uniform l1
contraction: the normalized mass grows like `sum 1/p`.

## Optimization

The nearby `P37` cutoff has certified bias `17/500 < F37/M37 < 8/125`, but it
shares the same source-completeness obstruction. The `5:3` weights remain the
unique two-row choice eliminating the `3^-z` Mellin frequency.

## Replay

```bash
python experiments/X-97620-exact-annular-bias/verify_retained.py
python experiments/X-97620-exact-annular-bias/tests/test_verify.py
```

This recovered download contains the eight retained gzip certificate streams
and their final verification record. It does **not** contain the two raw JSON
generator outputs, `build_and_replay.sh`, or `src/mpfr_min.h`; consequently it
supports retained-certificate verification, not a from-source regeneration of
the original 320/448-bit computation. No substitute evidence has been invented.

Expected proof object:

```text
32695b45ac021a862aac27fecfbe92bb98773dfca702d1fd06f7b313f970f8b4
```

## Scientific status

```text
sharp scalar theorem                 proved
PR #565 source induction             refuted
substantial l1 contraction family    ruled out
repaired RH proof                     not obtained
Riemann Hypothesis                    unproved
```
