# R-96601 — The scalar-prefix successor does not import the failed prime-sieved transports

Claim ID: `R-96601`  
Status: **BINDING LINEAGE FIREWALL**  
Created: 2026-08-17

PR #552 proves two exact failures in neighboring prime-sieved transports:

1. at `(j,P,n)=(3,6,24)`, a fixed-product divisor cube leaves coefficient `-1` at one physical knot and cannot create a three-knot convex packet;
2. at `(P,p,u)=(30,5,2)`, the actual `P`-rough mass in `[2,10)` is only `1/sqrt(7)<1/2`, while the substituted all-integer block bound exceeds `2`.

This successor uses neither argument. Its prime induction is only the exact recurrence

\[
M_{Pp}(N)=M_P(N)-p^{-1/2}M_P(\lfloor N/p\rfloor),
\]

with the actual coefficient ledger (L-96601.3). Any future proof must establish the scale inequality on that ledger; it may not replace rough capacity by an unsieved integer interval.
