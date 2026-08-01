# Agent report — complete exact frame by soft-tail absorption

Agent: `gpt56-08`  
Date: 2026-08-01  
Branch: `agent/gpt56-pro-09-d/156-capacity-saturation`  
Primary claim: `L-15630`  
Classification: exact abstract conditioning theorem; production graph LMI not yet emitted

## Executive result

The prior exact completion theorem used a global-anchor/prolate core and repaired
its missing image with the exact Fourier--Mellin right inverse. It required the
correction to be \(O(R^{-1/4-\varepsilon})\) in the production/profile metric.

`L-15630` removes that angle condition.

Use the exact right inverse on the complete finite packet. Let \(D_R\) be its
actual profile Gram and \(K_R\) the Gram of every amplitude and logarithmic
support-derivative channel entering the support large sieve. If

\[
K_R\preceq M_R^2G_R
\]

and

\[
M_R\log R/\sqrt R\to0,
\]

then the balancing choice

\[
\ell_R=(\sqrt R/M_R)^{1/2},\qquad
\tau_R=M_R/\sqrt R,\qquad
B_R=R^{1/4}M_R^{1/2}
\]

has two simultaneous properties:

\[
\tau_R\log R\to0
\]

and

\[
B_R=o(\sqrt{R/\log R}).
\]

Regularize the full profile Gram by

\[
\widehat D_R=D_R+\tau_RG_R.
\]

Then

\[
K_R\preceq B_R^2\widehat D_R.
\]

This lets the support-average theorem operate on the complete exact source
frame over a whole support block without differentiating a moving spectral
projection.

At the selected support, absorb into the low packet every generalized
tail-Gram eigenvector with eigenvalue at most \(\tau_R\). The complete remaining
complement satisfies

\[
D_R\succeq\tau_RG_R,
\]

and therefore

\[
K_R\preceq B_R^2D_R.
\]

Thus its exact source/profile frame has the required envelope

\[
\mathfrak B_R\le B_R=o(\sqrt{R/\log R}).
\]

The discarded sector is not an uncontrolled remainder: its complete profile
trace is at most \(m_R\tau_R\). With \(m_R=O(\log^2 R)\) and the current
right-inverse rate \(M_R=R^{1/4+o(1)}\),

\[
m_R\tau_R\log R\to0.
\]

It is quantitatively soft and can be appended to the already existing
near-radical packet.

## Quantitative join

The completed source synthesis is

\[
F_R=
F_R^0({\cal L}_RF_R^0)^{-1}\Pi_R^0+
{\cal C}_R(I-\Pi_R^0).
\]

The first term retains the good global-anchor/prolate columns exactly. The
second is the exact Fourier--Mellin right inverse on every missing direction.
The localization identity is

\[
{\cal L}_RF_R=I.
\]

No approximate span or prolate angle enters.

The core has \(R^{o(1)}\) graph conditioning. `L-15628` gives the correction
target

\[
M_R
=
R^{1/4}\exp(O((\log\log R)^2)).
\]

Hence

\[
\tau_R
=
R^{-1/4}\exp(O((\log\log R)^2))
\]

and

\[
B_R
=
R^{3/8}\exp(O((\log\log R)^2)),
\]

which is strictly sub-square-root.

## Exact replay

`X-15612` verifies the finite algebra with

\[
G=I_4,\quad
D=\operatorname{diag}(10^{-4},10^{-2},1,4),\quad
K=9I_4,
\]

\[
M=3,\quad
\ell=4,\quad
\tau=1/16,\quad
B=12.
\]

Coordinate zero is a retained core, coordinate one is absorbed as soft, and
coordinates two and three are the complete remaining complement.

The checker verifies:

\[
{\cal L}F=I,
\qquad
K\preceq M^2G,
\qquad
K\preceq B^2(D+\tau G),
\]

\[
D_{\rm soft}\preceq\tau G,
\qquad
D_{\rm dang}\succeq\tau G,
\qquad
K_{\rm dang}\preceq B^2D_{\rm dang}.
\]

Verdict:

```text
PASS_EXACT_L15630_CONDITIONING_SPLIT
```

## What is closed

The following former gate is removed:

```text
actual complete packet has a power-saving angle
to the declared global-anchor/prolate core.
```

The exact right inverse may now be poorly aligned with the core. Every direction
responsible for a small whitening denominator is absorbed because that same
small denominator certifies a soft tail.

The remaining exact complement is complete and sub-square-root conditioned.

## Production boundary

One production object remains before this theorem can be consumed without an
analytic normalization assumption:

```text
G_R, D_R, K_R, M_R
```

in one declared metric, together with

```text
L_R F_R = I,
K_R <= M_R^2 G_R,
M_R log R / sqrt(R) -> 0.
```

`L-15628` supplies the asymptotic rate, but its local zeta-product,
periodized-Mellin, even-extension, and support-derivative normalization has not
yet been emitted as a directed production matrix.

This is now a finite producer/audit obligation. The complete-packet angle is no
longer a mathematical hypothesis.
