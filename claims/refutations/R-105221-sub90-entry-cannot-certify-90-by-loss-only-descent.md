# R-105221 — A sub-90% derivative entry cannot certify 90% through loss-only descent

Claim ID: `R-105221`  
Status: **EXACT API FIREWALL**

Every square defect in L-105221 is nonnegative. Hence the descent conclusion
has the form
\[
\frac{R_0}{N}
\ge
p_K-2D_K-o(1)
\le p_K+o(1)
\]
as a certified lower bound.

Therefore an entry theorem with \(p_K\le0.9\) cannot, by this loss-only API
alone, prove a 90% lower bound at level zero. In particular, the approximately
86.864% unconditional \(\xi'\) simple/on-line result is a valuable low-order
anchor but not by itself a 90% entry point. One needs a higher derivative
entry exceeding 90%, a genuinely gain-producing relation, or an independent
lower-bound input at level zero.
