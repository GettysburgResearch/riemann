# M-100160 — Product-band Bonferroni program for the reciprocal activation prefix

Status: **OPEN PROGRAM AFTER EXACT REDUCTIONS**  
Created: 2026-08-20

The continuation reduces the unresolved critical activation geometry to the reciprocal-weight squarefree prefix

\[
S_1(x)=\sum_{P_A\le x}(-1)^{|A|}P_A^{-1}
\]

for rough-prime labels `p>=67` (with the duplicate-67 bookkeeping handled separately at the source level).

Finite-cube diagnostics through twelve actual rough primes show `S_1(x)>0` on every activation prefix tested. If this is proved globally, then PR #679's interior critical-point condition `S_1<0, S_(1/2)<0` is impossible, and the Turán half of `PATG100200` vanishes.

The exact cardinality-layer recurrence is

\[
(k+1)E_{k+1}(x)
=\sum_{|A|=k,\,P_A\le x}
 w(A)
 \sum_{\substack{p\notin A\\p\le x/P_A}}{1\over p-1},
\]

where `w(A)=prod_(p in A)(p-1)^(-1)` after factoring the full positive Euler product. A global adjacent-layer bound fails because the inner prime-harmonic sum diverges at low `k`.

The proposed repair is product-band pairing. Partition extension primes by multiplicative bands

\[
e^j < p \le e^{j+1}
\]

(or a source-adapted ratio-67 partition). Each band has bounded reciprocal-prime mass, while adjoining a prime moves the subset product to a strictly higher band. The goal is to pair odd extensions against even parent mass band-by-band before summing over all bands, so the global harmonic divergence is replaced by a telescoping flux through product scale.

A valid proof must preserve the exact activation ideal and cannot replace the sharp product cutoff by a source-blind smooth majorant whose inverse cancels the reciprocal-zeta detector.

RH remains unproved.
