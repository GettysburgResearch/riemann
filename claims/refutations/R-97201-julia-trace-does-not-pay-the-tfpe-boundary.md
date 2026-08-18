# R-97201 — The PSD Julia trace cannot by itself pay the TFPE boundary

Claim ID: `R-97201`  
Status: **PROVED DIRECTED FINITE SEPARATOR OF A SHORTCUT**  
Created: 2026-08-18  
RH status: **TFPE itself is not refuted**

Let `X=500` and let `P` contain every odd prime at most `500`. Define

\[
T_{P,X}=\sum_{d\mid P}\psi_X(d),
\qquad
B_{P,X}=\sum_{(n,P)=1}h_X(n).
\]

Since every odd integer `n<=500` has an odd prime factor at most `500`, the coprime bulk consists exactly of the powers of two.

Directed 80-digit decimal intervals prove

\[
T_{P,500}>40.75888153133406722024,
\]

while

\[
6B_{P,500}<26.86217458425043977536.
\]

Therefore

\[
\boxed{T_{P,500}>6B_{P,500}.}
\]

The elementary PSD estimate `D<=T` cannot prove TFPE.

At the same witness the signed parity coefficient is negative:

\[
D_{P,500}<-3.72455418320932524069,
\]

so the actual TFPE margin is strictly positive:

\[
6B_{P,500}-D_{P,500}>30.58672876745976501604.
\]

Hence this is a separator against **trace-only extraction**, not against TFPE. The missing state must retain parity cancellation or an equivalent prime-completion covariance.
