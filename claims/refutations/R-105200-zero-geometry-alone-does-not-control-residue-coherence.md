# R-105200 — Zero geometry alone does not control critical-residue coherence

Claim ID: `R-105200`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-23  
RH status: **not assumed**

Let

\[
f_C(x)={x^3\over3}-x+C.
\]

Then

\[
f_C'(x)=x^2-1
\]

has the same two simple real zeros `-1,1` for every real `C`. The derivative
zero count, spacing and simplicity are therefore completely independent of
`C`.

The derivative-ratio residues are

\[
\rho_+(C)={f_C(1)\over f_C''(1)}={C-2/3\over2},
\]

\[
\rho_-(C)={f_C(-1)\over f_C''(-1)}=-{C+2/3\over2}.
\]

At `C=0`, both residues equal `-1/3` and the coherence is one. At `C=1`, one
residue is positive and the other negative. By varying `C`, their magnitudes
and coherence can be changed while the derivative zeros remain fixed.

Therefore none of the following, alone, implies the residue mean-value theorem:

```text
all derivative zeros are real;
model zero spacing;
consecutive zero counts;
Rouche localization of the derivative only.
```

The simultaneous adjacent-order approximation in `L-105201`, together with
the canonical positive-frequency integration constant from `L-104516`, is
load-bearing. This firewall prevents `T-105200` from being misread as a formal
corollary of high-band real-rootedness alone.
