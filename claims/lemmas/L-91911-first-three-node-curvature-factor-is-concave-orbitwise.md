# L-91911 — The first three-node curvature factor is concave orbitwise

Claim ID: `L-91911`  
Status: **PROPOSED COMPLETE; REVIEW REQUIRED AT THE CENTERED ORBIT EXPANSION JOINT**  
Created: 2026-08-13  
Depends on: `L-91905`, `O-91910`, Platt–Trudgian source lock  
RH status: **unproved**

Use the notation of `O-91910` and write

\[
h(t)=\sqrt t\,F(\sqrt t).
\]

For one critical-line orbit with ordinate `b` and multiplicity `m`, its contribution is

\[
h_{0,b}(t)=\frac{2mt}{t+b^2},
\qquad
h_{0,b}''(t)=-\frac{4mb^2}{(t+b^2)^3}<0.
\]

For one symmetric noncritical orbit, write

\[
A=a^2-b^2<0,\qquad B=2ab,\qquad U=t-A.
\]

Up to its positive multiplicity factor, the contribution to `g(t)=F(sqrt(t))/sqrt(t)` is `U/(U^2+B^2)`. Direct differentiation gives

\[
h_{a,b}''(t)
=-\frac{8m Q(t)}{(U^2+B^2)^3},
\]

where

\[
Q(t)=(-A)U(U^2-3B^2)+B^2(3U^2-B^2).
\]

Hence this contribution is strictly concave whenever `U^2>3B^2`.

For the actual zeta zero set, the rigorous low-height verification imported on the parent branch implies that any hypothetical noncritical zero must occur far above the verified range. Since `|a|<1/2`, this gives `U^2>3B^2` with a very large margin for every safe `t>1/4`.

Therefore every zero orbit contributes concavity to `h`. Subject to the same centered Hadamard expansion and normal-convergence review joints explicitly listed in `L-91905`, summing gives

\[
\boxed{h''(t)<0\qquad(t>1/4).}
\]

Combining with `O-91910`, the remaining three-node determinant sign is therefore the opposite sign of the second divided difference of

\[
k(t)=\frac{\sqrt t}{F(\sqrt t)}.
\]

This does not prove that `k` is concave and does not prove RH.
