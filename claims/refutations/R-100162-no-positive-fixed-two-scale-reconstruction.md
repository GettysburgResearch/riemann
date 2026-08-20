# R-100162 — The duplicate-67 square does not give a positive fixed reconstruction of the critical Harnack difference

Status: **PROVED EXACT OPERATOR FIREWALL**  
Created: 2026-08-20  
RH status: **unproved**

Write `S=S_67` and `r=67^(-1/2)`. The critical half-order Harnack sequence is

\[
B=(I-rS)M,
\]

where `M=M_(1/2)` is the ordinary half-order Möbius prefix. The duplicate-67 local square is

\[
C=(I-rS)^2M.
\]

A tempting fixed-dimensional repair is to express `B` as a positive linear combination of `M` and `C` (and finitely many positive dilates) so that positivity of the squared object transfers to the first difference.

Already the two-object ansatz

\[
B=aM+bC
\]

fails coefficientwise. Comparing powers of `S` in

\[
a+b(1-rS)^2=1-rS
\]

forces

\[
b r^2=0,
\]

hence `b=0`, and then the `S` coefficient cannot match. More generally, any finite polynomial identity which reconstructs `1-rS` from nonnegative combinations of even powers `(1-rS)^(2j)` and nonnegative dilation monomials must reproduce a negative coefficient at the first `S` term; a purely positive coefficient representation cannot do so.

Thus the duplicate-67 square supplies useful positive higher-order information but no fixed positive desmoothing map back to the critical first Harnack difference.
