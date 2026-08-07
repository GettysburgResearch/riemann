# Integration handoff — Issue #232

## Add

```text
L-23201  exact finite Möbius resolvent packet
L-23202  high-order geometric Mertens equivalence
L-23203  terminal reduction of finite packet systems
L-23204  finite Selberg-Hankel terminal adapter
T-23201  full terminal-contraction RH proposal
M-23201  adversarial review protocol
X-23201  exact synthetic proposal regression
```

## Stack

Base this proposal on PR #158 at:

```text
c5a57f33ae5c33fe16ded944ab2d3c50edc7fe07
```

Cross-branch frozen inputs:

```text
PR #229  1daf03443265ce36cfb6efbd8de1ca9c702de793
PR #216  b76eef1b769584aa9d66d082bfc6634126f986a2
PR #231  R-22802 only
```

## Do not supersede

This proposal does not retroactively verify PR #158's `CP(K)`, PR #229's
critical-correlation lemma, or any failed proof on PR #231/#165.

## Promotion rule

Promote only after an unbounded source-bound family proves `STC(K)` and

```text
eta_K/delta_K -> 0
```

or the tensor analogue, with the first-cell Mertens mutation passing.

## Public status

```text
FULL PROPOSAL
TERMINAL CERTIFICATE FAMILY OPEN
RH UNPROVED
```
