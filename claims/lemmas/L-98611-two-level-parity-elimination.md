# L-98611 — Exact two-level parity elimination on the finite future-prime DAG

Claim ID: `L-98611`  
Status: **PROVED EXACT ALGEBRAIC THEOREM**  
Created: 2026-08-18  
Depends on: PRs #589/#591 paired recurrence  
RH status: **not assumed**

Let `R` be the positive, strictly upper-triangular future-prime operator on a
finite quotient DAG. Suppose the oriented deficits satisfy

\[
D^+=d^+ +RD^-,\qquad D^-=d^- +RD^+.
\]

Eliminating the reverse orientation gives

\[
\boxed{(I-R^2)D^+=g^+,\qquad g^+=d^+ +Rd^-.}
\]

Since `R` is nilpotent,

\[
\boxed{D^+=\sum_{k\ge0}R^{2k}g^+.}
\]

Therefore the exact parity-restored transition occurs in two-prime steps. A
noncircular Bellman proof must control the complete positive resolvent sum, not
merely demand `g^+>=0` state by state.
