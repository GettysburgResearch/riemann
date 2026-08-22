# R-102600 — First-chaos cancellation does not identify native and completed sources

Claim ID: `R-102600`  
Status: **PROVED EXACT SCOPE FIREWALL**  
Created: 2026-08-22  
Depends on: `L-102600--L-102603`  
RH status: **unproved**

The identity

\[
\text{owner atom}+\text{completion-transfer atom}=0
\]

is exact, but it occurs in a joint native/completion ledger.

It does not imply

\[
E=C.
\]

At the Dirichlet-series level,

\[
E(z)=\frac{1-67^{-z}}{\zeta(z)},
\qquad
C(z)=\frac{1-67^{-2z}}{\zeta(2z)}.
\]

The second function is holomorphic for \(\Re z>1\), while the first retains the
reciprocal-zeta singularities relevant to RH.  Their difference is precisely
the conclusion-bearing defect.

Any argument which drops the Duhamel current after observing the first-chaos
cancellation proves only a statement about the squared completion and has
removed the RH detector.
