# Integration handoff — central carry cascade

Branch:

```text
research/gpt56-sol/277-central-carry-cascade
```

Base:

```text
PR #247
fb69b22bb3a29e5709f9927d129ef968c2d04fb9
```

## Add

```text
L-27701  exact central residual and unconditional two-pass packing
L-27702  continuum cascade and exact lattice commutator
T-27701  DCCS conditional RH theorem
M-27701  production/review protocol
```

## Cross-route dependencies

```text
PR #247  atomized carry/Pascal algebra, one-pass theorem, RH consumer
PR #272  complete balanced Pascal-cycle kernel and capacity-debt adapter
PR #276  WSTS equivalence used only as a scope firewall, not as an input
```

## New unconditional advance

The central first residual is proved decreasing for the critical target, so a
second positive packing stage is available without any arithmetic hypothesis.
The proposed asymptotic lower bound is

```text
prime_ramp(X)
 >= 4 log(2)(2-log(2)) sqrt(X)-O(log^2 X).
```

## New full proposal

```text
positive central atoms
-> exact residual T_X
-> continuum geometric contraction
-> exact O(log X)-stage signed finite cascade
-> DCCS subpower lattice debt
-> capacity/entropy adapter
-> sharp prime ramp
-> RH.
```

## Promotion rule

Do not promote to an RH proof until `DCCS` is proved uniformly through the full
support-halving cascade.  Fixed-stage asymptotics, finite monotonicity scans,
or replacement of `2kq-1` by `2kq` do not suffice.

## Recommended next attack

Construct a weighted variation norm for the lattice commutator satisfying a
strict contraction under the continuum residual, or use the explicit PR #272
Pascal cycles to repair every negative central edge with polylogarithmic total
capacity.
