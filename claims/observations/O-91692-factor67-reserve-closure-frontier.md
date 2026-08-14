# O-91692 — The factor-67 reserve gate closes by row transparency, not by a large perturbation constant

Claim ID: `O-91692`  
Status: **EXACT FRONTIER SYNTHESIS**  
Created: 2026-08-14  
Depends on: `L-91690`, `L-91691`, `L-91692`, `T-91661`  
RH status: **unproved**

The compact reserve problem was previously phrased as an approximation theorem:

```text
find epsilon;
bound a correction norm;
absorb 10152 ||C|| epsilon in a one-use reserve.
```

That interface is valid for genuinely approximate typed atom maps, but it is not
the right final argument for the exact factor-67 construction.

The target Hall decomposition satisfies, pointwise in every physical component
row,

\[
\text{signed row}
=
\text{positive residual row}
+
\text{positive Hall bonus row}.
\]

The equality holds before ordinary observation, and hence before radix-four
subtraction.  Its Hall-induced total-row error is exactly zero.  The physical
quantizer therefore sees the original equality-row density

\[
L(x)=2\sqrt x\sum_{n\le x}\mu(n)/n
-
\sum_{n\le x}\mu(n)/\sqrt n,
\]

not the SHARP target density used to normalize Hall.  This distinction is
load-bearing because `Psi` exceeds `2` near `x=2`, while

\[
159/500<L(x)<183/100<2
\qquad(1\le x<67).
\]

Once that is recognized, every remaining reserve is explicit:

```text
C67                                              <19
interior mismatch+collar / native detail         <5655/(32K)
chosen one-use factor                             K/(K+178)
strict interior slack                             41/[32(K+178)]
terminal possible overfill                        <4452 X^(-3/2)
top omission                                      >5033 X^(-3/2)
strict terminal slack                             581 X^(-3/2)
```

The endpoint port also sums before observation, so PSD linearity gives one
aggregate `P_61/67` port.  The causal split is applied after global thinning and
children are grouped by rough prime, preserving the original coefficient sum
below `1/8`.

The next action is hostile review of PR #473, especially:

1. the equality-row/Hall transparency identity;
2. the one-sided factor-67 density census;
3. the exact arithmetic in the interior and terminal margins;
4. the use of only the Schur-reserve portion of the `P_61/67` port theorem;
5. the global rather than fibrewise causal coefficient list.

```text
abstract 10152-epsilon reserve route           BYPASSED
Hall total-row transparency                    EXACT
compact reserve constants                      DIRECTED EXACT
SONTR producer gate                            CLOSED ON FROZEN INPUTS
independent reconstruction                     REQUIRED
Riemann Hypothesis                             UNPROVEN
```
