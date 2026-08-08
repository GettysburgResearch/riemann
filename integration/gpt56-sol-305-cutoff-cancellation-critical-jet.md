# Integration handoff — cutoff cancellation and shift-terminalized eta core

Branch:

```text
research/gpt56-sol/304-cutoff-cancellation-critical-jet
```

Parent:

```text
PR #304 @ 78b75fc17e27334a9950018528c1c6e083d74820
```

## Disposition

Do not integrate PR #304 as a proof of RH. `R-30501` proves that its terminal
cutoff-source atomic norm is at least `N/100` on one stopped critical-power
layer. The claimed polylog source map is unavailable.

Retain from PR #304:

```text
adjacent-tree commutator source identity;
O(sqrt(m)) capacity bound for E_(m-1);
descendant-capacity correction to the root-only mutation.
```

New canonical continuation:

```text
R-30501  macroscopic cutoff atomic obstruction
L-30501  critical eta weighted-jet contraction
L-30502  exact terminalization of the true `-1` lattice shift
T-30501  explicit Critical Eta Variation criterion
X-30501  exact finite replay
```

## Corrected proof graph

```text
critical carry target
-> exact central first-difference stage
-> terminal adjacent-commutator lift of sigma(m)=r(2m-1)-r(2m)
-> propagate only the unshifted eta convolution
-> Critical Eta Variation
-> Cycle Debt
-> prime ramp
-> RH.
```

All arrows before Critical Eta Variation are supplied on the branch. CEV is
open and RH-bearing; the branch does not claim a complete proof.

## Mandatory mutations

Any continuation must retain:

```text
R-30501 quotient-cell N/100 atomic lower bound;
PR #303 source/edge type mismatch;
PR #299 fixed Abel counterexamples;
compact-boundary derivative atoms;
the first 2/3 Mertens cell;
PR #272 capacity normalization.
```
