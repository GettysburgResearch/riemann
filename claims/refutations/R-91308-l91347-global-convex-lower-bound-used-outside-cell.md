# R-91308 — The original `L-91347` checker used a global convex lower bound outside the active cell

Claim ID: `R-91308`  
Status: **EXACT PROOF-SCOPE CORRECTION — THE HALL THEOREM IS REPROVED IN `L-91350`**  
Created: 2026-08-13  
Depends on: original `L-91347`; corrected `L-91350/X-91127`  
RH status: **unproved**

## 1. The issue

In the regime `p=t/y`, one activation-cell Hall margin has the form

\[
 H(s)=C+\frac{-aA_y s^2+3B_y s}{\sqrt t},
 \qquad s=\sqrt y.
\]

When `A_y<0`, this is convex.  The first version of the checker inserted the
global real-line minimum

\[
 C+\frac{9B_y^2}{4aA_y\sqrt t}
\]

as a lower-bound candidate without first checking that the vertex lies in the
current activation cell.

At, for example, the cell beginning at `y=11` for threshold `t=915`, the global
vertex lies far outside the cell.  The global minimum is negative even though
both cell endpoints and the complete cell are strongly positive.  Thus the
original checker could reject a valid cell and its stated finite reduction was
not the proof actually required.

## 2. Correct repair

For `A_y<0`, the derivative numerator is

\[
 H_s'(s)\sqrt t=-2aA_y s+3B_y.
\]

The corrected checker evaluates this directed interval at both cell endpoints.
It proves in every such cell that the derivative has one sign throughout; no
convex vertex lies in an active cell.  Therefore the cell minimum is at an
endpoint.  Affine cells are likewise checked at endpoints.

The corrected replay performs `383472` directed rational interval gates and
proves both target and score Hall margins above one.  That proof is promoted as
`L-91350/X-91127`.

```text
original theorem conclusion              TRUE AFTER REPROOF
original global-minimum checker step      INVALID
corrected cell-derivative proof            DIRECTED EXACT
Riemann Hypothesis                         UNPROVED
```
