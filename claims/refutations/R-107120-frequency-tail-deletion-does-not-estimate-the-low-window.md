# R-107120 — Frequency-tail deletion does not estimate the surviving beta window

**Claim ID:** `R-107120`  
**Status:** binding mechanism firewall  
**Date:** 2026-08-31

`L-107121` deletes all frequencies

\[
|t|>Y^{1/2}(\log(2Y))^B
\]

at subpower cost. This is an analytic localization theorem, not an arithmetic
cancellation theorem.

Indeed the same classical mean-value estimate on the retained interval gives
only

\[
\int_{|t|\le T_B(Y)}|D_Y(t)|^2dt
\ll (T_B(Y)+Y)\log(2Y)
\ll Y\log(2Y).
\]

The resulting exponent is one, exactly the source-blind scale already present
before localization. By `T-107120`, any fixed power improvement of the
weighted low-window integral proves a new zero-free half-plane.

Likewise, one fixed additive shift `h` cannot replace the complete aggregate
of `L-107120`: finite coefficient arrays can have the `h`-correlation equal to
zero while another shift, and hence the positive stationary square, is
nonzero. The RH-bearing statement retains all physical shifts or the complete
Fourier window.

Therefore none of the following is a proof of the open estimate:

```text
paying the high-frequency tail;
bounding the number of retained frequencies;
controlling finitely many fixed shifts;
replacing the signed shift aggregate by absolute correlations;
replacing maximal horizons by one endpoint.
```
