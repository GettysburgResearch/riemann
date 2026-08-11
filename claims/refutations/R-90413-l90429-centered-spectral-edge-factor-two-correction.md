# R-90413 — `L-90429` centered spectral edge requires a factor-two correction

Claim ID: `R-90413`  
Status: **EXACT NORMALIZATION CORRECTION**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Superseding theorem: `L-90430`

The state compression and divisor-renewal identities of `L-90429` are correct, but its displayed critical spectral interval was too large by a factor of two.

With

\[
P_*(y)=\frac12Q_*(y/\sqrt2),
\qquad |y|=1,
\]

`L-90423` gives

\[
2y^{-2}Q_*(y/\sqrt2)
 \in[43-30\sqrt2,43+30\sqrt2].
\]

Therefore

\[
y^{-2}P_*(y)
 \in\left[
 \frac{43-30\sqrt2}{4},
 \frac{43+30\sqrt2}{4}
 \right],
\]

not the interval displayed in `L-90429.8`.

The same correction simplifies the forcing. If

\[
\kappa_-=(43-30\sqrt2)/4,
\]

then

\[
\sum_rp_r2^{-r/2}=\kappa_-,
\qquad
\sum_rrp_r2^{-r/2}=2\kappa_-,
\]

and the normative renewal is

\[
\sum_{d\le X}d^{-1/2}F_*(X/d)
 =\kappa_-\log(X/4).
\]

The correction does not affect the RH-equivalent scalar, the fourteen-row image, PBVG, or the column-one gauge. It only fixes the centered filter normalization and the stated comparison of constants.
