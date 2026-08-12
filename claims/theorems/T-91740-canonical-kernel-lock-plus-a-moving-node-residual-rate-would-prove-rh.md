# T-91740 — Canonical kernel lock plus a moving-node residual rate would prove RH

Claim ID: `T-91740`  
Status: **FULL CONDITIONAL RH PROPOSAL / EXPLICIT KERNEL LOCK OPEN**  
Created: 2026-08-13  
Depends on: `L-91740/L-91741`, `R-91740`, `T-91730`  
RH status: **unproved**

For every dyadic annulus `j` and moving node

\[
\eta_j(Y)=\sqrt{a_{j-1}^2+Y^2},
\]

construct on one common carrier/delay core:

1. the explicit arithmetic source kernel `A_j(Y)` from the completed Julia
   cascade;
2. the canonical critical-plus-stable model kernel `C_j(Y)`;
3. the exact completed source lock identifying
   `A_j-C_j` with hyperbolic plus auxiliary output.

Prove

\[
\boxed{
A_j-C_j\succeq0
}
\]

on every finite packet and, on the moving-node Cauchy vector,

\[
\boxed{
(A_j-C_j)(\eta_j(Y),\eta_j(Y))
=
o_j(Y^{-2}).
}
\]

`L-91740` then constructs the canonical minimal source-to-model isometry, and
`L-91741` deletes every crossed zero in annulus `j`. If the theorem holds for
all `j`, RH follows.

This criterion replaces the open-ended instruction “construct the
intertwiner” by two explicit tasks:

```text
prove one polarized kernel defect is PSD;
prove its moving-node diagonal is o(1/Y^2).
```
