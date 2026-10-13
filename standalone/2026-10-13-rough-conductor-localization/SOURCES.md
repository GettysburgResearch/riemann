# Sources and overlap

## Pinned repository material actually consulted

1. **Base and earlier independent benchmark.** PR #931, mathematical source
   `3968d1b7135900e6130412f58a39bc67e73d4ecb`, publication head
   `c77671d71dcf22a08833a6d7f86a6f15a2eba84f`:
   [COMPACT_TEST_HAAR_MOMENTS.md](https://github.com/GettysburgResearch/riemann/blob/c77671d71dcf22a08833a6d7f86a6f15a2eba84f/standalone/2026-10-13-signed-moment-reassessment/COMPACT_TEST_HAAR_MOMENTS.md).
   The complete note was read. It proves the fully independent masked
   benchmark and identifies an open physical discrepancy. Those are prior
   results, not rediscoveries claimed here. Our upper proof is independent
   of its analytic-continuation argument.

2. **Native heat comparison.** PR #932, mathematical source
   `ea94f3e40b2755de0ffb9ac7727faa820e0c4cd0`:
   [NATIVE_HEAT_DEFECT_AND_PRIME_REMOVAL.md](https://github.com/GettysburgResearch/riemann/blob/ea94f3e40b2755de0ffb9ac7727faa820e0c4cd0/standalone/2026-10-13-principal-zeta-bridge/NATIVE_HEAT_DEFECT_AND_PRIME_REMOVAL.md),
   lines 1--320 consulted; Git blob `076ab93dc76158b74d7d68dcb0e5516dfbf866e9`.
   Its actual-density heat defect and the warning about unpaid coprime
   correlations are credited. This packet does not claim to solve that
   defect or to reprove the rest of #932.

3. **Residual-conductor and mask convention.** PR #929, mathematical source
   `38ee7069e23ae24fd693e70149dc817900c3caa4`:
   [RATIONAL_PRIME_INCIDENCE.md](https://github.com/GettysburgResearch/riemann/blob/38ee7069e23ae24fd693e70149dc817900c3caa4/standalone/2026-10-10-conductor-averages/RATIONAL_PRIME_INCIDENCE.md),
   lines 1--170 consulted; Git blob `f22de70e282f7f5647879060377ca927d9b458be`.
   In particular (1.3)--(1.4) distinguish the nonprincipal residual
   conductor from the principal coprimality mask. The new counting theorem
   uses these conventions, not the external subconvex/sieve inputs there.

4. The metadata of current PRs #930, #932, #933 and #934 were checked for
   overlapping directions. Their full proofs were not audited. No claim
   to have surveyed every historical branch or established global novelty
   is made. The phase projection and Rankin method are classical tools.

5. At the base head, AGENTS.md and STATUS.md were read. This is a new
   proposed standalone packet. It changes no integrated claim and requests
   no automatic merge.

## External primary sources

- Michael A. Bennett, Greg Martin, Kevin O'Bryant and Andrew Rechnitzer,
  *Explicit bounds for primes in arithmetic progressions*, Illinois J.
  Math. 62 (2018), 427--532,
  [arXiv:1802.00085v3](https://arxiv.org/abs/1802.00085v3).
  Only the explicit theta(x;q,a) estimate stated in its abstract is used,
  with q=3 and a=1, to obtain >>z/log z split primes in [z/2,z] for
  Section 4's lower construction. The elementary upper theorem does not
  use this paper. No computation or proof of that external theorem was
  reproduced here.

- Adam J. Harper, *Moments of random multiplicative functions, II: High
  moments*, Algebra & Number Theory 13 (2019), 2277--2321,
  [arXiv:1804.04114](https://arxiv.org/abs/1804.04114).
  Background and priority context only: moment-to-Euler-product methods
  are established in the random-multiplicative literature. Its sharper
  Steinhaus/Rademacher formulas are not transferred to the native sextic
  family and are not analytic inputs to this packet.

- Alexandre de Faveri, *Optimal large sieve for fixed order characters*,
  [arXiv:2610.04045](https://arxiv.org/abs/2610.04045).
  Its existence and stated scope were checked during reconnaissance.
  No theorem from it is invoked in the new proofs. In particular, this
  packet does not apply a fixed-coefficient sieve to row-dependent rough
  block coefficients.
