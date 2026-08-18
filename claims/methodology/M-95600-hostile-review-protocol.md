# M-95600 — Hostile review protocol

Review in this order:

1. `L-95600`: verify the odd-Mertens dyadic identity and bandwise partial
   summation in both directions.
2. `L-95601`: verify every inverse coefficient and the subpower mass condition.
3. `R-95600`: retain the top-band sign-replacement witness.
4. `L-95603`: check source order, the derivative sign, the critical
   \(\delta_4\) coefficient, and pole orders.
5. `L-95602`: treat the classical zero-free-region estimate only as an
   unconditional \(X^{1-o(1)}\) bound.
6. Treat `O-95600` as floating discovery only.

Immediate rejection triggers:

```text
claiming the sign scan is cofinal;
claiming a fixed extra vanishing moment weakens RH;
dropping the J1 boundary without the exact source bridge;
using a source-blind moment or PSD inequality after R-95600;
cancelling the compact current pole by the lower-order gauge;
claiming RH has been proved.
```


---

# Q4 successor: UOSACF equivalence and finite-filter exhaustion

## Result

PR #595 correctly weakens SACF to a one-sided subpower estimate. This packet
proves the converse under RH, so that the weakened estimate is exactly
equivalent to RH.

It also proves that every fixed, and many slowly growing, scale filters have
subpower inverse cost. Additional finite annularization or moment cancellation
therefore cannot lower the arithmetic difficulty.

The finite odd-core source is related exactly to the older compact Q4 current
by

\[
R^2D_4=PR(-B_\sharp')+(\log4)Pz^2B_\sharp.
\]

The second term is a delayed lower-pole-order gauge. The first is the genuine
reciprocal-\(\zeta\) current.

## Unconditional progress

The best classical zero-free-region input transfers to the exact Q4 packet and
gives

\[
\mathcal S_H(X)
\ll
X\log^2X
\exp[-c(\log X)^{3/5}(\log\log X)^{-1/5}]
+\mathrm{polylog}.
\]

This is a genuine gain but remains \(X^{1-o(1)}\).

## Correct frontier

The remaining theorem must use the outer Möbius signs through a nonlocal
Schur, Bellman, Hardy, or equivalent global arithmetic mechanism. Fixed kernel
engineering is exhausted at the RH-equivalent scope.

RH remains unproved.
