# R-91002 — Unweighted centre averages of radial curvature are RH-blind

Claim ID: `R-91002`  
Status: **EXACT METHOD FIREWALL**  
Created: 2026-08-11  
Depends on: `L-91005`  
RH status: **unproved**

For a finite symmetric zero packet `Z`, `L-91005` proves

\[
 \frac{8t^{3/2}}\pi
 \int_{\mathbb R}\mathcal C_{Z,x}(t)\,dx
 =N_0(Z)+2N_{<\sqrt t}^{\rm off}(Z).
\tag{R-91002.1}
\]

The right side is nonnegative whether or not off-line pairs exist. Indeed every reflected pair of depth below `sqrt(t)` contributes its full two-zero mass with a **positive** sign.

Consequently none of the following can prove RH by itself:

```text
nonnegativity of the unweighted centre average;
a lower bound for that average;
an asymptotic formula for that average;
an average trace that retains only the zero-frequency centre mode.
```

A successful averaged method must retain additional centre frequencies, localization, a signed window, or a nonlinear statistic. This explains why the pointwise negative pole and curvature blow-up coexist with positive density-one and positive mean results.

This firewall does not rule out localized Zeta23/Gabor compressions, higher signatures, adaptive centre windows, or the pointwise radial-concavity theorem.
