# Paired factor-67 parity/grouping hardening after PRs #555, #556, #559, and #561

## Verdict

The accumulated-parity objection in PR #561 is decisive against every
bounded-depth repair. The distinction made in PR #556 between individual finite
colors and the complete grouped annular reserve is correct and remains
necessary, but grouping is a linear diagonal operation and therefore cannot
remove the rough-history character. The scalar reduction of PR #559 is valuable
at the Mellin consumer, where it produces one zero-safe numerator, but it also
preserves the same history sign and fails at depth two by more than `62.7`.

## New exact statements

- `L-97010` proves that complete-color grouping and row scalarization commute
  with the parity swap and inherit `(-1)^m` on a rough history of length `m`.
- `R-97010` transports PR #561's fixed-depth asymptotic no-go through both
  proposed salvage interfaces and records the explicit negative `5:3` depth-two
  scalar.
- `T-97010` isolates `ASHP67`, a single all-depth scalar Hall producer, and
  composes it with the exact zero-safe scalar Mellin–Landau consumer.

## Scientific boundary

```text
finite-color grouping before observation          required and exact
scalar numerator factorization                    exact
bounded-depth parity reset                        refuted
bounded-depth grouped-annular reset                refuted
bounded-depth 5:3 scalar reset                     refuted
all-depth scalar Hall producer ASHP67              open / RH-bearing
Riemann Hypothesis                                unproved
```

This is a hardening and producer reduction, not a proof of RH.
