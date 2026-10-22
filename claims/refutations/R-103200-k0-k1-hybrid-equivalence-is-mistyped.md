# R-103200 — The frozen K0/K1 largest-prime–Vaughan edge is mistyped

Claim ID: `R-103200`  
Status: **PROVED EXACT NORMALIZATION REFUTATION**  
Created: 2026-08-20  
Frozen inputs: PR #688 at `24a2a748b8b36a70382c88843bb7779caac97e07`; PR #685 at `4f69b7656f42dcb5ff250d13adc9f88e8d18f315`  
RH status: **unproved**

PR #688 decomposes

\[
G_0(X)=\sum_n\frac{\mu(n)}{\sqrt n}K_0(X/n)
\]

by largest-prime ownership.

PR #685 applies Vaughan to

\[
K_1=(I-\sqrt2S_2)K_0
\]

and hence to

\[
G_1(X)=\sum_n\frac{\mu(n)}{\sqrt n}K_1(X/n).
\]

Exactly,

\[
\boxed{G_1(X)=G_0(X)-\sqrt2\,G_0(X/2).}
\]

Thus the two decompositions are not decompositions of one scalar.  Their
terminal terms cannot be subtracted to obtain an \(L^1(dX/X)\) error.

The `LPMW <-> BVD` edge in the first T-101000 matrix is therefore invalid at
its frozen scopes.  The corrected same-kernel theorem is `L-103201`.
