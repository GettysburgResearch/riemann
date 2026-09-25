# Sources and attribution

## Live repository inspection

- GettysburgResearch/riemann PR #907, head
  `4f769249e35d23a9cf955fbab620e70d07117e58`: NJV34 under
  `standalone/2026-09-25-native-jacobi-virial/`. The current head and PR status
  were read through the connected GitHub tool; no review comments were present
  at inspection. This is the parent, not a newly independently reviewed source.
- PR #904, head `8c506696d8ad7772ccaf48fbb8678fcd889e8beb`:
  `standalone/2026-09-21-mellin-hankel-bandwidth/PROOF.md`, especially §§1–3.
  The exact source, product-kernel un-reduction, reciprocal balance, endpoint
  term, and complex square in the Mellin–Hankel formula were read. Its actual
  product kernel is substituted into the adapter in RLC35 §6. Its analytic
  estimates and prior finite campaigns were not replayed here.
- PR #906, head `ddc25eafe85d637b6c7e8a7e276b39e4998fd648`: current PR summary
  read for the completion-quotient and product-threshold scope. We do not claim
  a new independent review of the entire packet or use its bounds as an
  unproved black box.
- Repository operating rules in AGENTS.md: own-branch PR publication, scoped
  proposed claims, explicit source/coverage/rounding contracts, and no canonical
  promotion without review.

## Classical mathematical inputs

1. T. M. Apostol, NIST DLMF Chapter 27, §27.5, especially equations
   27.5.1–27.5.5: Dirichlet convolution, Möbius inversion, and the divisor sum
   for the logarithm. https://dlmf.nist.gov/27.5
2. NIST DLMF §27.6, equation 27.6.2: the divisor-product formula
   `sum_{d|n}mu(d)f(d)=product_{p|n}(1-f(p))`. This is the exact classical
   source of the phase and damping products, not a new Euler-product identity.
   https://dlmf.nist.gov/27.6
3. Finite Abel summation; Young's convolution inequality; Fourier Plancherel;
   a first-order Volterra equation and integration by parts. The relevant
   normalizations and proofs are written in PROOF.md. No zeta-zero assumption,
   asymptotic PNT estimate, or imported subconvexity exponent is used here.
4. M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the
   Möbius function*, arXiv:1807.05890 (2018). The author-provided abstract was
   consulted as background on classical finite product-source reconstruction;
   no theorem in this packet depends on a new reading of its full proof.
   https://arxiv.org/abs/1807.05890

The DLMF pages and arXiv abstract were opened during this pass. No PDF was
analyzed. The logarithmic derivative hierarchy is classical arithmetic
calculus, closely related to the usual differentiated convolution identities;
we do not claim it as a new number-theoretic identity.

## Claim of contribution

The proposed contribution is the explicit native finite-source realization,
its radical compatibility classification, the sharp uniform phase comparison,
the complete quadratic balance, and the source/phase/cutoff-correct adapter
with its unresolved error terms. External priority is not asserted. The
checker is newly written in this packet; it does not import the parent's
checker or receipts. Same-author replay is not independent mathematical review.
