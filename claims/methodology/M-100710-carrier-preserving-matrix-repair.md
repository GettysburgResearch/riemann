# M-100710 — Carrier-preserving repair of the short/long implication matrix

The short/long source partition is exact, but the norm assignment in
`L-100704` is not compatible with its leading arithmetic.

The asymptotics are

\[
G_{\rm sh}(X)=-\kappa_0{\sqrt X\over\log X}
+O(\sqrt X/\log^2X),
\]

\[
G_{\rm lo}(X)=+\kappa_0{\sqrt X\over\log X}
+O(\sqrt X/\log^2X).
\]

Thus the first-order carrier is a **cross-region covariance**, not a regional
error. Any repaired implication matrix must retain it until after the two
regions are recombined.

Two viable successor formulations are:

## Route A — balanced cross-region covariance

Keep the exact scalar pair `(G_sh,G_lo)` in one two-component observation and
prove a centered estimate for

\[
G_{\rm sh}+G_{\rm lo}=G_\mu
\]

without taking either component in absolute value separately. The natural
positive object is the centered `2x2` Gram after projecting away the explicit
carrier vector `(-1,+1)`. The terminal estimate is then a cross-covariance
Carleson theorem, not `SCME100704`.

## Route B — source-side prime-chaos renormalization

Before the short/long split, remove the complete first-chaos prime carrier by
an exact source projection and retain the compensating carrier as a separate
known coordinate. Repeat at the semiprime level only if the projected
remainder still has a power main term. Every projection must commute with the
minimal-wavelet observation and must preserve the reciprocal-zeta detector.
A fixed finite truncation is insufficient; the source projection must be an
exact positive/orthogonal chaos decomposition.

Neither repair is proved here. The binding rule is:

```text
never apply an absolute regional norm before the short/long prime carrier has
cancelled.
```
