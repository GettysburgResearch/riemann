# De Branges correction-free continuation

Date: 2026-08-23  
PR: #728  
RH status: unproved

The moving-centre correction ledger can be avoided at a genuine downward
reverse–Rolle step, where the derivative has already been shown real-rooted.

For a finite polynomial `p`, let `G=p'` have simple real zeros and set
`E=G+iG'`. The positive multipole weight is the modulus square of

\[
g_a(z)=6/\prod_{h=1}^3(z-a+ih).
\]

Subtracting the three lower-half-plane principal parts from `g_a G'/G` and
`g_a p/G` produces two polynomials `u_a,v_a` in the finite de Branges space.
Their Gram entries are exactly the actual weighted count, first moment and
second moment. Hence

\[
\pi^2(NB-A^2)=\|u_a\wedge v_a\|^2.
\]

This is a correction-free factorization: no `p''` debt and no nonreal critical
term survive once the derivative spectrum is real.

The remaining Xi task is now an entire de Branges exhaustion plus a quantitative
angle estimate. It interfaces directly with PR #724's independent
exterior-square Fourier Gram and PR #726's summable high-derivative tail.
