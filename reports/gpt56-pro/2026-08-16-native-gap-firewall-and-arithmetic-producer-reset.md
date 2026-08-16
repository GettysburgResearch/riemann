# Research reset: the native physical compiler omits the complete arithmetic gap

## Executive finding

The strongest exact result of this reset is a load-bearing normalization
correction. The native endpoint compiler from PR #530 is a valid finite
positive packing construction, but its conclusion-producing scalar was
misidentified.

The exact identity is

\[
J_\Lambda(X)-\mathcal H(d)
=
\underbrace{J_\Lambda(X)-P_\Lambda(X)}_{F_\Lambda(X)}
+
\underbrace{P_\Lambda(X)-\mathcal H(d)}_{\text{positive physical slack}}.
\]

PR #530 kept only the second term.

## Why this matters

The physical cone can make its own residual small, and finite optimization may
even saturate all weighted columns. Such saturation leaves the arithmetic gap
\(F_\Lambda\) exactly unchanged. The endpoint packing problem and the RH-bearing
arithmetic problem are therefore additive rather than interchangeable.

The error is visible without asymptotics. At \(X=3\), the zero row gives

\[
F_\Lambda(3)
=
\log2\left[
\frac3{\sqrt2}\log(3/2)-4\sqrt2+\frac8{\sqrt3}
\right]
<-\frac{289}{5000}.
\]

Thus the false equality fails at the first nontrivial endpoint.

## NEDB disposition

The NEDB support statement may still be studied as a finite positive-cone
problem. If true, it bounds the weighted physical slack. It does not bound
\(F_\Lambda\), and therefore it cannot close RH by itself.

Targeted reconnaissance found macroscopic blocker columns at selected finite
endpoints. These computations are not promoted to an asymptotic refutation;
they reinforce that blocker support is a poor proxy for the arithmetic
producer.

## Strongest surviving route

The reset retains PR #531's exact double-zero cubic reduction:

\[
\mathcal L_W(X)
=
\sum_{\sqrt X<d\le X/2}\mu(d)F_W(X/d)+O(\log X).
\]

The small-divisor range is already unconditional. The remaining large-divisor
Möbius cancellation is a genuine arithmetic theorem and cannot be replaced by
native packing slack.

Other independent routes remain live—the phase-locked First-Hermite hierarchy,
radial xi curvature, and raw Brownian Dirichlet-Hermite stability—but each
still has an explicit pointwise arithmetic gate. None was imported as proved.

## Scientific status

This packet is not a full RH proof. It is a substantive fail-closed reset:

```text
false physical-to-arithmetic composition      removed
finite endpoint compiler                       retained
exact arithmetic gap                           restored
honest cubic arithmetic frontier               retained
new unconditional RH proof                     not obtained
Riemann Hypothesis                             unproved
```
