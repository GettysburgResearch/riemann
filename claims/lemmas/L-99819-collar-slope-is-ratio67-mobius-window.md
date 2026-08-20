# L-99819 — The only nonconstant collar mode is exactly a ratio-67 Möbius window

Claim ID: `L-99819`  
Status: **PROVED EXACT ALL-PRIME COEFFICIENT IDENTITY**  
Created: 2026-08-20  
Depends on: PR #659 canonical scalar box; `L-99818`  
RH status: **unproved**

Work in logarithmic coordinate `u=log y`. Let `P` be any finite set of active rough primes and put

\[
F_P(u)=\prod_{p\in P}(I-p^{-1/2}U_p)\Phi(u),
\]

where the collar part of the box potential is

\[
\Phi(u)=8+(-8-3u)e^{-u/2}\qquad(0<=u<\log67).
\]

On every activation cell, `F_P` has the form

\[
F_P(u)=a_P(u)+(b_P(u)+c_P(u)u)e^{-u/2},
\]

with coefficients constant on that cell. The coefficient of `u e^{-u/2}` comes only from shifted collar occurrences. For a subset `A subset P`, its Euler coefficient is

\[
(-1)^{|A|}p_A^{-1/2},
\qquad p_A=\prod_{p\in A}p.
\]

If `u-log p_A` lies in the collar, then shifting `-3(u-log p_A)e^{-(u-log p_A)/2}` and multiplying by `p_A^{-1/2}` cancels the half-order weight exactly. Hence

\[
\boxed{
 c_P(u)
 =-3\sum_{A:\ e^u/67<p_A<=e^u}(-1)^{|A|}.
}
\tag{L-99819.1}

Equivalently, after identifying subsets with squarefree rough integers,

\[
\boxed{
 c_P(u)
 =-3\sum_{e^u/67<n<=e^u\atop p|n\Rightarrow p\in P}\mu(n).
}
\tag{L-99819.2}

Thus every many-prime activation complication in the compact box collapses to one ordinary ratio-67 Möbius window. No prime weights, owner probabilities, or graph capacities remain in this coefficient.

This identity also explains why a finite-state coefficient cone cannot close the proof: the window sum is not uniformly bounded as `P` grows. The correct conclusion-facing target is therefore a one-sided or logarithmically averaged estimate for these ratio-67 Möbius windows, not pointwise coefficient control.

The theorem is an exact bridge. It does not prove the required window estimate or RH.
