# R-91404 — Aggregate recanonicalization does not by itself move unmatched mode mass between endpoints

Claim ID: `R-91404`  
Status: **EXACT SCOPE FIREWALL / SELF-CORRECTION**  
Created: 2026-08-13  
Depends on: `L-91410/L-91411`; affine child scaling  
RH status: **unproved**

The algebraic identity

\[
Q_\infty Iu+\sum_j(H_j-\alpha_jI_4)Iu=(1-\Theta)Iu
\]

is exact when every term is written in one common hidden source coordinate.

It does **not** alone authorize moving the excess part of a branch from its
actual child endpoint back to the parent endpoint. Target, score and component
rows are endpoint-dependent. A source-coordinate equality must be combined with
an exact affine transport identity before such relocation is valid.

For the one-prime pure-reserve control, the `Y`-mode branch excess

\[
p^{-1/2}-p^{-1}
\]

lives naturally at the child endpoint. Calling it part of the parent current
packet without a positive transport theorem is an extra, unproved step.

Therefore `T-91404` may use `L-91410` only as a mass/coupling identity. Its
physical current/child statement requires a same-endpoint realization of every
survival and branch-excess packet.

`L-91415` supplies that same-endpoint realization by a positive clipped ledger
projection. No endpoint relocation of unmatched mass is used there.

```text
aggregate source-coordinate identity          EXACT
unmatched-mass relocation to parent            NOT IMPLIED
same-endpoint positive realization             L-91415
Riemann Hypothesis                             UNPROVED
```
