# PFR-T8 — flower curvature is the phase acceleration of zeta-prime

Claim ID: `PFR-T8`  
Status: **KNOWN CURVATURE IDENTITY / PROVED EXACT PROJECT ADAPTER**  
Depends on: `PFR-T6`  
RH status: **unproved**

On an open Hardy petal, with `s=1/2+it`, the `PFR-T6` fields satisfy

\[
D_H=|\zeta'(s)|^2,
\qquad
-\vartheta'\mathfrak C_H
=\operatorname{Re}(\overline{\zeta'(s)}\zeta''(s)),
\]

and therefore

\[
-\frac{\vartheta'\mathfrak C_H}{D_H}
=\operatorname{Re}\frac{\zeta''}{\zeta'}(s)
=\frac{d}{dt}\arg\zeta'(s).
\]

Consequently the positive open-turn term in the curvature-defect ledger is
exactly

\[
\int
\left(\operatorname{Re}\frac{\zeta''}{\zeta'}(1/2+it)\right)_+dt.
\]

For a finite polynomial `P`, the corresponding field on `Re(s)=sigma_0` is

\[
\operatorname{Re}\frac{P''}{P'}(\sigma_0+it)
=\sum_{P'(c)=0}
\frac{\sigma_0-\operatorname{Re}c}
{(\sigma_0-\operatorname{Re}c)^2+(t-\operatorname{Im}c)^2}.
\]

Thus left critical points generate positive Poisson turning and right critical
points negative turning.  This is a finite Speiser-compatible model; the full
zeta-prime pole/background ledger remains open.

Full proof and novelty boundary: `CONTINUATION_108320.md`.
