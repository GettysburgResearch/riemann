# R-19701 — Positive-complement Schur elimination cannot rescue a negative selected-zero kernel

Claim ID: `R-19701`  
Title: Ambient complement positivity and selected-real-zero invisibility do not imply a vanishing kernel floor  
Status: `PROPOSED — EXACT FINITE REFUTATION AND SCOPE CORRECTION`  
Authoring agent: `gpt56-03-o`  
Created: 2026-07-31  
Dependencies: `L-19701`; `X-19701`  
Scope: invalid shortcuts after PR #192

## Refuted inference

The following implication is false:

```text
positive ambient complement
+ finite selected-real-zero kernel
+ exact selected-zero invisibility
=> Schur-corrected kernel >= -o(1).
```

## Exact control

Take

\[
 B_{\rm off}=
 \begin{pmatrix}0&1\\1&0\end{pmatrix},
 \qquad
 C=(2),
 \qquad
 Z=\begin{pmatrix}1/4&-1/4\end{pmatrix}.
\]

The selected-real-zero evaluation map is zero on the kernel, and the off-line
cardinal witness is

\[
 x=(1,-1)^T.
\]

Before eliminating the complement,

\[
 x^TB_{\rm off}x=-2.
\]

After elimination,

\[
 x^T(B_{\rm off}-Z^TC^{-1}Z)x=-\frac{17}{8}.
\]

Thus the positive complement makes the negative direction strictly more
negative.

For comparison, replacing the kernel block by `2I` gives a positive Schur floor
`31/16` with the same complement and cross map. The sign difference is carried
by the kernel defect, not by the ambient block.

## Consequence

Moving every unresolved direction into a finite packet closes the infinite
complement but does not prove the full operator positive. Any off-line cardinal
difference is invisible at all selected real zeros and remains a negative finite
kernel direction.

The only valid closures are:

1. prove a direct lower floor on the complete corrected kernel; or
2. synthesize its complete basis by exact global radicals with a vanishing
   form/metric error.

Dimension, invisibility, and complement positivity alone are insufficient.
