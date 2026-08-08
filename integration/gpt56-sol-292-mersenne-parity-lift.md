# Integration handoff — Mersenne parity lift

Branch:

```text
research/gpt56-sol/285-mersenne-parity-lift
```

Stacked on PR #285 at:

```text
61d0b66196f308981d36dbb8723d5e64d7a27533
```

## Add

```text
L-29201  automatic logarithmic Mersenne collar
L-29202  parity-sibling lift and odd-divisor network
T-29201  PPMFL full conditional RH proposal
M-29201  fail-closed production/review protocol
X-29201  exact standard-library regression
report   refreshed full-problem attack
```

## Replace in the proof graph

The separate MCF assumption

```text
Mersenne collar mass = X^o(1)
```

is no longer an open theorem. It follows from exact nonnegative sub-saturation by
one diagonal carry column.

The corrected MCF frontier is

```text
exact support-feasible nonnegative flow
-> automatic O(log X) collar
-> eta lower envelope
-> RH.
```

## Do not supersede

This continuation does not supersede:

- PR #291's finite shell one-crossing theorem;
- PR #286's shifted analytic-bulk contraction;
- PR #272's complete Pascal-cycle/debt normal form;
- PR #263/#269 physical parity/factor-five programme.

It supplies a finite positive construction interface joining their common
factor-two boundary source.

## Promotion rule

Promote only after a recursive PPMFL certificate reconstructs every odd node,
Mersenne edge, endpoint row, and carry column. The exact local algebra may be
merged independently at proposed scope. RH remains unproved.
