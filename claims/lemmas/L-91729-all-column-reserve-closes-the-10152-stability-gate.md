# L-91729 — The repaired all-column reserve closes the `10152 ||C|| epsilon` stability gate

Claim ID: `L-91729`  
Status: **PROVED EXACT QUANTITATIVE REPAIR ON FROZEN CELL/RESERVE INPUTS**  
Created: 2026-08-15  
Frozen inputs: `L-91689`, `L-91723`, `L-91724`; one bounded common correction map  
RH status: **unproved**

Raw Lipschitz interpolation is insufficient at a vanishing capacity.  PR #479
removes finite activation collars and gives positive same-cell refinement on
the retained compact cells.

After PR #479's square-root thinning, every nonterminal column has normalized
reserve

\[
 r_K=\frac1{\sqrt K+130}.
\]

Let `C` be the complete bounded one-use correction map and let the retained-cell
native-relative atom error be `epsilon_X`.  The fixed-window stability theorem
gives

\[
 \delta_X=10152\|C\|\varepsilon_X.
\]

If `C!=0`, choose the mesh so that

\[
 \varepsilon_X<
 \frac1{2\cdot10152\|C\|(\sqrt K+130)}.
\]

Then `delta_X<r_K/2`, and the post-correction reserve satisfies

\[
 \boxed{
 \operatorname{Reserve}_X^{\rm final}
 >\frac{r_K}{2}
 >10152\|C\|\varepsilon_X.
 }
 \tag{L-91729.1}
\]

If `C=0` or `epsilon_X=0`, the pre-existing `r_K>0` proves the strict inequality
directly.  The terminal error is chosen smaller than half the independent
margin `581X^-3/2`.

The collar, refinement, thinning and correction are applied once to the common
positive parent measure; none is assigned to a child.

```text
activation-knot relative refinement          PR #479 / EXACT
all-column normalized reserve                 PR #479 / EXACT
Reserve >10152||C||epsilon                     EXACT
zero-error edge case                          CLOSED
one-use ownership                             EXACT
native scalar cost                            L-91728
Riemann Hypothesis                            UNPROVED
```
