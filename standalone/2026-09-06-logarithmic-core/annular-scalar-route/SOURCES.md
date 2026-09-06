# Sources and independence boundary

The current work is research, not a Reviewer-A or Reviewer-C acceptance of its
author's earlier work. All conclusions are proposed for independent review.
No external priority, largest-window, or minimal-annulus claim is made.

## Repository sources

- Continuation parent: GettysburgResearch/riemann PR #803,
  893d93b045099d9920fadf4b0e5bcb51d0455832.
  `standalone/2026-09-06-logarithmic-core/window-one-positivity/PROOF.md`,
  Git blob 644392c4a59edff697851fe526b8da5de96492cf.
  Read for the exact W normalization and the local-versus-global boundary.
  Its 2049-coefficient numerical certificate is NOT rerun or used to prove AS1.
- Original #803 logarithmic-core packet:
  4370ed19eb7b2630602740468cd9ecbaa870d848,
  `standalone/2026-09-06-logarithmic-core/PROOF.md`,
  Git blob f7420d1ddf603a3765331649d3f5b9d04f23e8e7.
  Section 7's Laplace identity is reconstructed directly in this packet.
  The operator-core and conditional-strictness theorems are not dependencies
  of the new scalar criterion.
- Underlying arithmetic W: #792 at
  465cb28ed8cbfa1bb071d9a85eeda9890decfe6b,
  `standalone/2026-09-05-bernstein-chebyshev-growth/energy-schur-reduction/PROOF.md`,
  Git blob 0d12ff6039dcc79f6576538edeebd2a0c5b539c0.
  The source formula is retained, not replaced by a raw prime cutoff.
- Main policy/context observed at 051808c1f8367b4320c52f94b40908eb2173d622:
  AGENTS.md and OPEN_CUTS.md. No main mutation is included.
- Prior annular route: #352 at 906b5a477a1ed7c88a40db7569924f15f3d54b72,
  `claims/theorems/T-90015-improved-factor64-rational-annular-rh-equivalence.md`.
  Its complete statement/proof-facing summary was read for overlap, not a
  fresh replay of all cited dependencies or certificates. That route already
  has a fixed-margin annular Landau criterion. The present contribution is
  the explicit link from the W/Schur source to a nonnegative finite prime-power
  sum, exact elimination of P2, rational slack, and square sampling. Factor 16
  here is not an improvement of the different restricted factor-64 minimality
  problem. Neither route proves its terminal arithmetic inequality.

## Primary external sources consulted

Masatoshi Suzuki, *Screw functions of Dirichlet series in the extended Selberg
class*, arXiv:2209.12832v2, HTML version dated March 25, 2025:
https://arxiv.org/html/2209.12832v2
Theorem 1.1 and Section 3.1 already prove eventual scalar sign equivalents via
one-sign Laplace theory. Sections 2.2 and 4 supply related Hadamard and
arithmetic-transform context. The general principle is credited, not claimed
new. Our resolvent/filter and finite prime weights are derived here. No PDF
or upstream numerical computation was used.

NIST DLMF:
https://dlmf.nist.gov/27.4 (especially 27.4.12, logarithmic derivative);
https://dlmf.nist.gov/25.2 (zeta continuation and definitions);
https://dlmf.nist.gov/25.4 (completed functional equation);
https://dlmf.nist.gov/25.10 (zero-strip/classical zero-count context);
https://dlmf.nist.gov/5.9 (digamma integral representations).
These are classical analytic inputs, not new formalization claims. The paired
Hadamard product, Laplace uniqueness, Tonelli and identity theorem are used at
the explicitly displayed scopes. The Landau argument is included in PROOF.md.

PNT is used in AS5 only to construct the comparison positive measure with
exactly the same safe moment. AS1--AS4 and the finite checker do not use PNT,
a zero census, RH, or a simplicity theorem as unconditional premises.

## Execution boundary

No external paper was copied into the packet. The finite code is newly written
standard-library Python. Its normal/optimized checks are local executions,
not GitHub CI or independent kernel verification. No predecessor producer,
large prime/zero campaign, or actual Schur matrix engine was run.
