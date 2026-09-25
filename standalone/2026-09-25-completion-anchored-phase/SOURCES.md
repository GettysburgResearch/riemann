# CAP36 sources and provenance

## Frozen project sources

1. RLC35, own parent on draft PR #907:
   `0e4be03a59c266ec54b3a3862b7d4eba2e08ba28`,
   `standalone/2026-09-25-radical-logarithmic-calculus/PROOF.md`.
   The uncompressed capped-source defect, complex-square distinction, and late
   balance-repair obstruction remain unchanged. CAP36 changes the interface:
   factorwise compression and an explicitly observable-invisible early repair.
   https://github.com/GettysburgResearch/riemann/blob/0e4be03a59c266ec54b3a3862b7d4eba2e08ba28/standalone/2026-09-25-radical-logarithmic-calculus/PROOF.md

2. NCG28, read from PR #904 head
   `8c506696d8ad7772ccaf48fbb8678fcd889e8beb`,
   `standalone/2026-09-20-native-composite-covariance/PROOF.md`, Sections 0–1.
   Source: the cap-three completion, F_Y, full completion budget, and elementary
   cubic point estimate. Needed estimates are rederived in CAP36 Section 4.
   No rerun or independent approval of NCG28's full campaign is claimed.
   https://github.com/GettysburgResearch/riemann/blob/8c506696d8ad7772ccaf48fbb8678fcd889e8beb/standalone/2026-09-20-native-composite-covariance/PROOF.md

3. CQT32, PR #906 frozen head
   `ddc25eafe85d637b6c7e8a7e276b39e4998fd648`,
   `standalone/2026-09-21-completion-covariance-quotient/PROOF.md`, Section 4.
   Source: the exact same smooth microscopic mask, centered harmonic tails,
   unreduction, derivative bounds, and rectangular bilinear estimate.
   CAP36 Section 5 repeats the proof and makes the complex-source case explicit.
   https://github.com/GettysburgResearch/riemann/blob/ddc25eafe85d637b6c7e8a7e276b39e4998fd648/standalone/2026-09-21-completion-covariance-quotient/PROOF.md

4. MHB32, `8c506696d8ad7772ccaf48fbb8678fcd889e8beb`,
   `standalone/2026-09-21-mellin-hankel-bandwidth/PROOF.md`.
   The target identification and phase-preserving Hankel distinctions are
   inherited from the earlier read recorded by RLC35. CAP36 does not use its
   improved bandwidth exponent or its imported zeta estimate.

## Classical inputs, verified on 25 September 2026

- NIST DLMF 27.5: Dirichlet convolution and Mobius inversion.
  https://dlmf.nist.gov/27.5
- NIST DLMF 27.6.2: the multiplicative divisor product.
  https://dlmf.nist.gov/27.6.E2
- Finite Abel summation, full-line Fourier Plancherel, and elementary multiplier
  maximization are classical. The particular identities and bounds needed
  here are proved explicitly in PROOF.md, not imported under new names.

No external-priority claim is made for the assembled results. The checker is
standalone code written for this packet; its small sieve, rational arithmetic,
and convolution routines implement elementary definitions. No historical
receipts or historical predicate counts are represented as newly replayed.
