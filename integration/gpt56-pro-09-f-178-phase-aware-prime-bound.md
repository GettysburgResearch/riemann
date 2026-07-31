# Integration handoff — phase-aware pole-free bound

Stack on PR #177.

## Add

```text
L-15613  scalar selected-phase / residual-zero bound
L-15614  terminal-prime matrix version
T-15604  finite strict violation implies off-line zero
M-15604  proof-producing pipeline
O-15607  five-notch exact-translation nomination
X-15605  exact rational final comparator
```

## Compose with

- PR #165 for the universal zero-free window, notch factors, and pole-free raw
  statistic;
- PR #177 for the centered terminal-prime matrix;
- Issue #178 for the directed phase-complete production run.

## Key formula

Under RH,

```text
|Q_G(x)-S_Z(x)-T_M(x)|
 <= 2 sum_shell (M_shell-r_shell) H_shell
    +2 A_p Z_p(T)
    +trivial_tail.
```

For a real profile packet, replace `2|g|` by the Loewner charge
`4 Phi*G^-1 Phi`.

## Production target

```text
x=8578244975439/549755813888
five notches
first 100 selected zero phases
64,542 prime-power terms in the current ordinary manifest
```

No RH claim.  A strict directed failure is a counterexample nomination requiring
independent explicit-formula and numerical reproduction.
