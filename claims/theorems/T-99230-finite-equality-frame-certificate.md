# T-99230 — The PR #620 equality-frame interface is a finite rank-two cone certificate

Claim ID: `T-99230`  
Status: **UNCONDITIONAL REDUCTION; ACTUAL CERTIFICATE OPEN**  
Created: 2026-08-19  
Depends on: `L-99230`, `L-99231`, `R-99230`  
RH status: **unproved**

The endpoint inverse used in PR #620 has only two homogeneous modes. Therefore
its complete positive equality frame is established once the following finite
data are certified:

1. outward nonnegativity of the smooth inverse density on every activation
   cell;
2. the exact derivative-jump atom at every knot, with nonnegative weight and
   one owner;
3. two positive anchored packets whose homogeneous coefficient matrix is
   nonsingular;
4. nonnegative coefficients
   `M^{-1}(A_a,B_a)^T`;
5. one common typed measure for target, score, all physical columns, and child
   labels.

Once these data are supplied, `L-99231` gives the exact equality measure and
`L-99220` composes it through the continuum endpoint root and complete
factor-67 tree.

This packet does not claim the actual T99020 data satisfy the five conditions.
The current status is:

```text
distributional inverse formula          PROVED
activation-knot atom formula            PROVED
Volterra nullspace rank two              PROVED
two-anchor calibration theorem           PROVED
actual knot ledger                       OPEN
actual anchor matrix and coefficients    OPEN
4sqrt(X) equality normalization          OPEN PENDING CERTIFICATE
Riemann Hypothesis                       UNPROVEN
```
