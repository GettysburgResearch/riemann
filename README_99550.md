# T99550 — Double-clamped Volterra equality-frame closure

This add-only successor is stacked on the distributional Volterra audit in
PR #638 at exact head

```text
73ee57ccc684f4062769a6d1c0456b3ef6318db2
```

**The Riemann Hypothesis remains unproved.**

## Exact result

For

\[
(Vf)(x)=\frac{2x^2f''(x)-xf'(x)+f(x)}{2\sqrt x},
\]

define

\[
\Phi(y)=4y\log y+2\sqrt y\log y-12y+12\sqrt y
\quad (y\ge1),
\]

and extend it by zero for \(0<y<1\). Then

\[
V\Phi(y)=2\sqrt y-1,
\qquad
\Phi(1)=\Phi'(1+)=0.
\]

The two clamps are decisive. Every arithmetic activation
\(\mu(n)\Phi(x/n)\) enters with zero value and zero first derivative, so the
distributional knot mass

\[
n^{3/2}\bigl(f'(n+)-f'(n-)\bigr)
\]

is exactly zero. At the lower endpoint, both homogeneous coefficients in
PR #638's Green formula vanish. Consequently the clamped arithmetic frame

\[
f_\mu(x)=\sum_{n\le x}\mu(n)\Phi(x/n)
\]

has the exact distributional representation

\[
f_\mu(X)=
\int_1^X
\frac{2(X-\sqrt{Xt})}{t^{3/2}}
\left(
2\sqrt t\sum_{n\le t}\frac{\mu(n)}n
-\sum_{n\le t}\frac{\mu(n)}{\sqrt n}
\right)dt,
\]

with no hidden activation atoms and no \(\sqrt X\) or \(X\) nullspace term.

The physical parabolic endpoint packet

\[
b_X(t)=
2\sqrt t\log(X/t)-4\sqrt t+\frac{4t}{\sqrt X}
\]

obeys the same double-clamping equations at \(X=t\).

## What this closes

Relative to PR #638, this packet closes the generic boundary-mode alternatives
for the specific clamped arithmetic frame:

```text
activation-knot atom ledger          identically zero
Volterra sqrt(x) coefficient         zero
Volterra x coefficient               zero
two-anchor calibration               unnecessary for this frame
open-cell density alone              still insufficient without clamps
```

## What it does not close

This packet does not replay the inherited compact Hall/profile campaign,
all-column realization, terminal source theorem, or Mellin–Landau consumer.
It does not establish RH. Any downstream proof must still identify its actual
endpoint observable with this clamped frame in the same physical coordinates
and reconstruct all imported local inputs.

## Replay

```bash
python3 experiments/X-99550-clamped-volterra/verify.py
sha256sum -c T99550_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_T99550_CLAMPED_VOLTERRA_EQUALITY_FRAME
c1a44d3bf130a535ee4d389c1a524075c8d812ca37b5c7497916d154befff64c
```
