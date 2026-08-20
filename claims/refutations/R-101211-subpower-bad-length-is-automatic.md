# R-101211 — A subpower bad-set length premise is automatic on a logarithmic horizon

Claim ID: `R-101211`  
Status: **PROVED SCOPE CORRECTION**  
Created: 2026-08-21  
Audits: PR #698 `L-101103`

For any scalar on `[1,Y]`, the total logarithmic length of its negative set is at most

\[
\log Y=Y^{o(1)}.
\]

Therefore the hypothesis

\[
\mathfrak L_F(Y)=Y^{o(1)}
\]

in the Poincaré/coarea gate of PR #698 is automatic. At the displayed subpower scale, that theorem reduces to the derivative-energy and terminal-component estimate; it is not a genuinely independent sparsity × energy gain.

A nontrivial occupancy input must carry a complementary **power saving**, as in `L-101201`, or must count only deep excursions as in `L-101211`.

This does not invalidate the Poincaré inequality. It corrects the interpretation of its hypotheses.
