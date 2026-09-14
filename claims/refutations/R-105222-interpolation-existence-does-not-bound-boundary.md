# R-105222 — Finite interpolation existence does not control its boundary norm

Claim ID: `R-105222`  
Status: **EXACT FIREWALL**

Debt-free interpolation in L-105222 is an identity, not a free estimate.
Uniform boundary control can fail under node coalescence.

For fixed \(a>0\) and \(\varepsilon>0\), the even polynomial
\[
U_\varepsilon(z)
=\frac{z^2-a^2}{(a+\varepsilon)^2-a^2}
\]
satisfies
\[
U_\varepsilon(\pm a)=0,
\qquad
U_\varepsilon(\pm(a+\varepsilon))=1.
\]
The interpolation data stay bounded, but for every fixed \(R>a\),
\[
|U_\varepsilon(R)|
=\frac{R^2-a^2}{2a\varepsilon+\varepsilon^2}
\longrightarrow\infty.
\]
Therefore L-105222 closes the adjacent-pole bookkeeping but does not by itself
bound the outer contour. Any conclusion-facing use needs a separation theorem,
a weighted minimal-norm interpolant, or a source-specific de Branges/Pick
estimate.
