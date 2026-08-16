# L-94202 — The large-divisor Möbius tail is a genuine arithmetic producer after the native-gap reset

Claim ID: `L-94202`
Status: **PROVED EXACT COMPOSITION OF FROZEN INPUTS / ESTIMATE OPEN**
Created: 2026-08-16
Frozen input: PR #531 head `e1b3b03d97d47c5046aa84f31e51c925d92baabd`
RH status: **unproved**

Let \(W\) be the compact two-switch cubic of `L-93261` and

\[
F_W(Y)=\sum_{m\le Y}(\log m)W(m/Y).
\]

The exact identity \(\Lambda=\mu*\log\) gives

\[
\mathcal L_W(X)
=
\sum_{d\le X}\mu(d)F_W(X/d).
\]

The double Mellin zero yields the unconditional forcing estimate

\[
|F_W(Y)|\le512\frac{1+\log Y}{Y},
\qquad Y\ge2.
\]

Consequently

\[
\boxed{
\mathcal L_W(X)
=
\sum_{\sqrt X<d\le X/2}\mu(d)F_W(X/d)
+O(\log X).
}
\tag{L-94202.1}
\]

Everything before the displayed tail is unconditional and arithmetic. No
native packet, endpoint greedy, rough child, or physical slack enters
(L-94202.1).

The frozen Mellin pole audit shows that a bound

\[
\boxed{
\sum_{\sqrt X<d\le X/2}\mu(d)F_W(X/d)
=
O(\sqrt X\log^B(2X))
}
\tag{L-94202.2}
\]

for one fixed \(B\) would give the cubic RH criterion. Estimate (L-94202.2)
remains open and is not imported as an antecedent.

The point of the lemma is compositional: after `L-94201`, any valid successor
must contain an arithmetic theorem of this kind (or a genuinely different
arithmetic producer). Improving only the physical packing cannot substitute for
it.

```text
double-zero forcing estimate                 unconditional
small-divisor sector                         O(log X)
large-divisor Mobius tail                    exact surviving producer
square-root/polylog tail estimate            open / RH-bearing
physical packing as substitute               invalid
Riemann Hypothesis                           unproved
```
