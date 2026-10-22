# PFR-T11 — Flower--Speiser Gauss law and harmonic screening

Status: **AUTHOR-PROVED EXACT ARGUMENT-PRINCIPLE / SCREENING SYNTHESIS**  
RH status: **unproved**

For a finite polynomial, the derivative critical-point field on a vertical
line splits as `L-R`, where `L` and `R` are nonnegative sums of Poisson kernels
from critical points to the left and right.  If

\[
\mathscr O=\int\min(L,R),
\]

then exactly

\[
\int(L-R)_+=\pi N_L-\mathscr O,
\qquad
\int(R-L)_+=\pi N_R-\mathscr O.
\]

For actual zeta, put `G(s)=(s-1)^2 zeta'(s)` and let `Omega` be a boundary-zero-
free rectangle between `Re s=sigma_0` and the critical line.  With

\[
J_L=\int \Re G'/G(\sigma_0+it)dt,
\qquad
H_T=\int_{\sigma_0}^{1/2}\Im G'/G(\sigma+iT)d\sigma,
\]

one has

\[
\int_{T_0}^{T_1}\Re\frac{\zeta''}{\zeta'}(1/2+it)dt
=2\pi N_G(\Omega)+Q+J_L+H_{T_1}-H_{T_0},
\]

where

\[
Q=\int_{T_0}^{T_1}(t^2+1/4)^{-1}dt.
\]

Hence every left-of-line `zeta'` zero is paid by critical-line positive flower
curvature or by explicit side/endpoint flux.  Inserting this identity into
`PFR-T6` gives the finite petal--Speiser conservation inequality (2.28) of
`CONTINUATION_108420.md`.

No estimate of the screening or boundary terms is proved.
