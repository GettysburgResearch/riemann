# Phase-locked safe-line repair and a two-row direct Landau consumer

## Executive result

This successor corrects the first false interface in the 93270 packet and
shrinks the direct Mellin consumer from an unbounded family of component rows
to two explicit rows.

The raw carrier field contains the continuous prime mode

\[
e^{(1/2+it)r}\widehat W_C(1+it),
\]

so its unweighted scale energy is infinite for generic carriers. After exact
continuous-mode subtraction and one critical normalization, the field moves to
the zero-free line `Re s=1` and has an unconditional `O(log^2 t)` L2 norm.

The Q4 critical-adjoint multiplier

\[
P(z)=5-4\cos((\log4)z)
\]

cancels the complete critical-boundary zero lattice in the cubic inverse. This
produces a legal residue-completed pairing between the centered field and every
phase-locked First-Hermite kernel.

Separately, the fixed-row Mellin consumer of PR #542 only needs rows two and
three. Their numerators satisfy an exact algebraic no-common-zero theorem; the
only common zeros are zero and minus one. Removing the small primes two and
three leaves a positive smooth-number reservoir and explicit three/four-knot
large-prime packets. Positivity of those two rows alone would imply RH by
Landau.

## What remains

```text
SCID_PL:
  signed phase-locked safe-line covariance;

LPTRP_23:
  global allocation from the 2,3-smooth reservoir to the explicit
  large-prime packets.
```

Both are RH-bearing and remain open. The packet is a substantial unconditional
advance and a fail-closed closure contract, not an accepted RH proof.

Proof-object SHA-256: `4ce6d093731ac104026f821cf10fc83b0b94521a94cf3cb66c60139eb4883167`
