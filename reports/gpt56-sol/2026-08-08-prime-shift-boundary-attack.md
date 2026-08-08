# Prime-shift boundary attack — 2026-08-08

## Outcome

The boundary attack produced a clean binary result.

First, the generic functional-analytic shortcut is false: truncating an absolutely monotone seed at the origin destroys arbitrary-shift positivity. `R-23802` gives a concrete two-shift counterexample.

Second, the actual prime-log product has extra arithmetic structure not present in that counterexample. The Gamma/carry factor can be written as the finite prime-shift state

\[
G(t)=\sum_{n\le e^t}\mu(n)h_0(t-\log n),
\]

with one three-dimensional exponential-polynomial trajectory on every quotient layer and a single knot jump `mu(n)/8` at every logarithmic integer.

The entire open problem is therefore a boundary-charge problem.

## New exact mechanism

For every negative jump `mu(n)=-1`, squarefreeness gives

\[
1=\sum_{p\mid n}\frac{\log p}{\log n},
\qquad
\mu(n/p)=+1,
\qquad n/p\le n/2.
\]

Thus every downward boundary charge has a canonical positive convex routing to favorable parent nodes at strict half scale. The seed itself has the reserve

\[
h_0(\log x)\ge x/8.
\]

This suggests a tree/Carleson no-double-spend proof rather than a B-spline proof.

## What was not proved

The local parent identities do not by themselves prevent one favorable parent from being charged by too many negative descendants. Paying only the `1/8` birth jumps is also insufficient: the subsequent negative interior trajectories must be funded as well.

The remaining theorem `BCT` therefore requires a global capacity ledger. It is intentionally fail-closed: a proof must emit child-parent charges and parent balances, rather than infer them from the desired scalar positivity.

## Reconnaissance

Independent floating quotient-layer evaluation found no negative value of the actual prime-shift state through one million integer layers, and the state was increasing on every tested open layer. This is discovery evidence only and is not part of the proof boundary.

## Preferred proposal

The branch now promotes exactly one closing mechanism:

```text
prime-shift boundary state
-> half-scale positive parent charge
-> Boundary Charge Transport (BCT)
-> Gamma/carry positivity
-> FGCM
-> sharp carry entropy
-> prime ramp
-> square-screw/Landau
-> RH.
```

If a genuine capacity-overload family refutes BCT, the correct pivot is the weaker finite-horizon FGCM or PR #254's signed parabolic defect transport. The generic B-spline route should not be revisited.

RH remains unproved.
