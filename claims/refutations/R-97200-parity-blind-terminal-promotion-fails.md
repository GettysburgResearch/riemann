# R-97200 — Parity-blind terminal promotion does not compose

Claim ID: `R-97200`  
Status: **IMPORTED EXACT REFUTATION FROM PR #561**  
Created: 2026-08-17  
Frozen source: PR #561 at `db9bdc63c855c6ddf664b763d748f8155a6a2c67`

The statement “unchanged coefficient `k^{-1/2}`” in `L-97001.7` is insufficient
for terminal positivity. Every odd rough history reverses signed observation.

PR #561 gives the exact witness

\[
X=67\cdot71\cdot13=61841,
\qquad h=(67),
\qquad (p,y)=(71,13).
\]

The canonically oriented Target–Lorenz terminal packet has strictly positive
`E_T-O_T` (the directed audit proves a margin greater than `17`). The incoming
history has odd length, so the native source requires the swapped packet and the
opposite signed orientation. Consequently the parity-blind leafwise promotion
used by PR #559 cannot preserve the root marginal.

This refutes the composition step, not the compact or directed terminal
inequality in its canonical orientation.
