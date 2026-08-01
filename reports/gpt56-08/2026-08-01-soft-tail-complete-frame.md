# Agent report — exact source conditioning by regularized completion and a hard/soft split

Agent: `gpt56-08`  
Date: 2026-08-01  
Branch: `agent/gpt56-pro-09-d/156-capacity-saturation`  
Primary claims: `L-15630`, `L-15631`, `R-15604`, `X-15612`  
Classification: exact abstract conditioning theorem; production graph LMI and finite soft Weil-sign block open

## Executive result

The earlier exact completion used a global-anchor/prolate core plus an exact
Fourier--Mellin correction and required a power-saving angle between the actual
packet and that core.

The new construction removes the angle from the **conditioning problem**.

1. Retain the prolate core exactly on its represented image.
2. Fill every missing finite Fourier direction with an exact smooth source
   right inverse.
3. Let `D_R` be the actual omitted-tail/profile Gram of the resulting complete
   frame and `K_R` the Gram of all support-amplitude and logarithmic derivative
   channels.
4. Use a small regularization `D_R+tau_R G_R` while averaging the support.
5. At a selected support, split the actual profile Gram into soft and hard
   generalized spectral sectors.

The complete hard complement is exactly represented and has the required
sub-square-root actual-profile envelope. The soft sector has vanishing ordinary
profile trace, but its finite Weil sign remains explicit; it is not silently
promoted to a radical packet.

## Exact core-preserving source frame

Let `L_R` denote the localized arithmetic source map, `F_R^0` the
well-conditioned global-anchor/prolate core, `Pi_R^0` a projection onto its
represented image, and `C_R` an exact right inverse on the full finite Fourier
space. Define

\[
F_R
=
F_R^0({\cal L}_RF_R^0)^{-1}\Pi_R^0
+{\cal C}_R(I-\Pi_R^0).
\]

Then

\[
{\cal L}_RF_R=I
\]

exactly. The prolate columns are preserved rather than replaced, and the exact
inverse is used only where needed.

## Smooth exact right inverse

`L-15631` replaces the sharp box/guard construction by a smooth differential
cardinal.

Fix a smooth compact bump `eta` of integral one and put

\[
\chi_L=(L^{-1}1_{[-L/2,L/2]})*\eta.
\]

For `omega_k=2 pi k/L`, set

\[
g_{k,L}=\chi_Le^{i\omega_kt},
\qquad
q_{k,L}={ (\partial_t+1/2)g_{k,L}\over i\omega_k+1/2}.
\]

Then, exactly,

\[
\widehat q_{k,L}(\omega_j)=\delta_{kj}
\]

and

\[
\widehat q_{k,L}(i/2)=0.
\]

The corresponding multiplicative source is smooth, compactly supported away
from zero, satisfies `f(0)=0`, and has ordinary integral zero. Dividing its
sample by the finite zeta multiplier gives an exact projected arithmetic right
inverse.

The sinc factor survives smoothing, so the transform has the exact two-end
phase decomposition

\[
\widehat q_{k,L}(z)
=e^{iLz/2}a_{k,+}(z,L)+e^{-iLz/2}a_{k,-}(z,L).
\]

The amplitudes and support derivatives have polynomial logarithmic graph norm.
Cofinal zero avoidance plus the local zeta product gives the target inverse
bound

\[
M_R
\le
R^{1/4}\exp(O((\log\log R)^2))
=R^{1/4+o(1)}.
\]

The local zeta-product and exact production metric normalization remain audit
items.

## Regularized complete-frame conditioning

Let

\[
D_R=T_R^*T_R
\]

be the complete actual profile Gram and

\[
K_R=A_R^*A_R
\]

the support-amplitude/derivative Gram. Assume the directed unwhitened LMI

\[
K_R\preceq M_R^2G_R.
\]

It is enough that

\[
{M_R\log R\over\sqrt R}\to0.
\]

Choose

\[
\tau_R={M_R\over\sqrt R},
\qquad
B_R=R^{1/4}M_R^{1/2}.
\]

Then

\[
\tau_R\log R\to0
\]

and

\[
B_R=o(\sqrt{R/\log R}).
\]

For the regularized metric

\[
\widehat D_R=D_R+\tau_RG_R,
\]

one has

\[
K_R\preceq B_R^2\widehat D_R.
\]

Thus the entire exact completed frame is sub-square-root conditioned in one
fixed metric over a support block.

## Actual-profile hard/soft split

After choosing a good support, split the compressed generalized profile Gram
`D_R/G_R` at `tau_R`.

On the complete hard sector,

\[
D_R\succeq\tau_RG_R
\]

and hence

\[
K_R\preceq B_R^2D_R.
\]

Therefore the exact restricted source frame spans every remaining hard
direction and satisfies

\[
\mathfrak B_R\le B_R=o(\sqrt{R/\log R}).
\]

On the soft sector,

\[
D_R\preceq\tau_RG_R.
\]

If the finite packet dimension is `m_R=O(log^2 R)`, then

\[
\operatorname{Tr}_{G_R}D_R|_{soft}
\le m_R\tau_R
\]

and

\[
m_R\tau_R\log R\to0.
\]

Thus all poor actual-profile denominators are isolated in a finite sector with
vanishing ordinary profile trace.

## Necessary scope correction

The first version of the argument said that the soft sector could therefore be
absorbed into the near-radical packet. That inference is not valid from
ordinary profile mass alone.

`R-15604` gives the exact family

\[
D_j=\operatorname{diag}(\tau_j^2,1),
\qquad
A_j=\operatorname{diag}(-1,1),
\]

where the first coordinate has vanishing profile mass but fixed negative form.
An off-line Xi-cardinal direction has the same logical signature.

The correct remaining finite matrix is the soft-sector Weil/Schur block

\[
\mathscr S_R^{soft}.
\]

To promote the soft sector into the low near-radical packet one must prove

\[
\left\|
\left[G_{S,R}^{-1/2}\mathscr S_R^{soft}G_{S,R}^{-1/2}
\right]_{-}
\right\|\to0,
\]

or a stronger two-sided compression/residual estimate.

This sign obligation is now isolated from conditioning. It can be sent directly
to the joint arithmetic/harmonic shorted LMI of PR #191.

## Exact replay

`X-15612` uses

\[
G=I_4,
\quad
D=\operatorname{diag}(10^{-4},10^{-2},1,4),
\quad
K=9I_4,
\]

\[
M=3,
\quad
\ell=4,
\quad
\tau=1/16,
\quad
B=12.
\]

Coordinate zero is a retained core, coordinate one is soft, and coordinates two
and three form the complete hard complement. The checker verifies

\[
{\cal L}F=I,
\quad
K\preceq M^2G,
\quad
K\preceq B^2(D+\tau G),
\]

\[
D_{soft}\preceq\tau G,
\quad
D_{hard}\succeq\tau G,
\quad
K_{hard}\preceq B^2D_{hard}.
\]

Verdict:

```text
PASS_EXACT_L15630_CONDITIONING_SPLIT
```

Six central/adversarial tests pass. Certificate SHA-256:

```text
98305b42792dda68d2b9d9b06373f7cc177fc26ae9434520a6b75200e389835e
```

## Exact production boundary

The remaining conditioning producer must emit, in one declared normalization,

\[
{\cal L}_RF_R=I,
\qquad
K_R\preceq M_R^2G_R,
\qquad
{M_R\log R\over\sqrt R}\to0,
\]

followed by the directed `D_R/G_R` split.

The hard-sector conditioning theorem is complete. The exact mathematical
obstruction remaining after conditioning is the finite soft-signature matrix,
not a complete-frame angle or an uncontrolled arbitrary Möbius inverse.

No RH conclusion is claimed.
