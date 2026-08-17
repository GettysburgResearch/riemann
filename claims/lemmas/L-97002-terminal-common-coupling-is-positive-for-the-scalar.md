# L-97002 — The directed terminal common coupling is positive for the 5:3 scalar

Claim ID: `L-97002`  
Status: **PROPOSED COMPLETE SPECIALIZATION OF FROZEN DIRECTED INPUTS**  
Created: 2026-08-17  
Frozen source: PR #550 at `20646a78c3e8843001cb49ea0c9741f6d0d446f7`

A grouped terminal leaf has `p>=67`, `1<=y<67`, and all `d|P61` colours retained
with their Möbius parity. The frozen compact-plus-MPFR Target--Lorenz theorem
uses one coefficient vector simultaneously in target and every component row
and proves
\[
R_j(U)-R_j(O)\ge0\qquad(2\le j\le66).
\tag{L-97002.1}
\]
Its domains are `py<166000` for the compact theorem and `py>=166000` for the
256-bit MPFR tail, with strict retained tail margin
\[
26.7858198871370094575061.
\]

Apply the positive row functional `5R_2+3R_3` to (L-97002.1). Every grouped
terminal packet therefore has nonnegative scalar observation. Outer sources of
scale `<67` are covered by the frozen directed outer-row certificate and the
same positive functional.

No new numerical sweep is claimed here; this lemma is a specialization of the
pinned directed inputs.
