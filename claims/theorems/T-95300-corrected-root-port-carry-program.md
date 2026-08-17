# T-95300 — Corrected carry programme after the PICR separator

Claim ID: `T-95300`  
Status: **CORRECTED CONDITIONAL PROGRAMME — RH UNPROVED**  
Created: 2026-08-17  
Depends on: `R-95300`, `L-95300`, `L-95301`; retained exact results of PR #562

## Corrected architecture

For the square-root hinge,

\[
h_T=h_T^\circ-\rho_T\gamma,
\qquad
\gamma=\chi_{3,1},
\qquad
\langle b_2,h_T^\circ\rangle=0.
\]

The exact signed-span theorem realizes \(h_T^\circ\) in the interior. The
boundary coefficient \(-\rho_T\) is unavoidable and unique.

A valid one-channel positive construction must therefore prove both:

1. the root-port orientation
   \[
   \rho_T\le0;
   \]
2. a nonnegative interior realization of the root-neutral remainder
   \[
   h_T^\circ=h_T+\rho_T\gamma.
   \]

The first condition alone is already RH-bearing by `L-95301`. The second
cannot be inferred from signed span, root neutrality, or Julia-column
positivity.

## Surviving conclusion

PR #562's exact \(5{:}3\) terminalization and Julia reserve remain valid on any
genuine positive interior packet. What is withdrawn is the claim that the
unmodified hinge can enter that packet.

```text
PICR                                         FALSE
one-dimensional root quotient               CLOSED
minimal boundary root port                  CLOSED
signed transverse realization               CLOSED
positive two-channel realization            CLOSED
root-port one-sign                          OPEN / RH-BEARING
positive root-neutral interior realization  OPEN
Riemann Hypothesis                          UNPROVEN
```
