# L-97601 — The completed rough-history owner ledger is finite, exact and parity covariant

Claim ID: `L-97601`  
Status: **PROVED EXACT SOURCE-PROVENANCE THEOREM**  
Created: 2026-08-17  
Inputs independently reconstructed from PR #575  
RH status: **unproved**

Every squarefree source index has a unique decomposition

\[
k=d p_1\cdots p_t,
\qquad d\mid P_{61},
\qquad67\le p_1<\cdots<p_t.
\]

Moving a rough prime `p` into the ordered history preserves both activation and
coefficient magnitude:

\[
{X/p\over k/p}={X\over k},
\qquad
p^{-1/2}(k/p)^{-1/2}=k^{-1/2}.
\]

It swaps the two parity channels once.  Consequently every native occurrence
retains exactly

\[
\text{activation }X/k,\qquad
\text{magnitude }k^{-1/2},\qquad
\text{sign }\mu(d)(-1)^t=\mu(k).
\]

At fixed `X`, no occurrence has more than `floor(log X/log 67)` rough factors,
so the completed history expansion is finite.  Complete `P_61` colour grouping
commutes with the parity swap; neither grouping nor the scalar observation
`5R_2+3R_3` erases the character `(-1)^t`.

This theorem proves ownership and parity.  It does not prove that a swapped
terminal packet has a positive Hall realization.
