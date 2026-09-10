# Sources and attribution

## Exact repository sources

- GettysburgResearch/riemann PR #812, commit
  `cc5277c34fdbc48787cf650b4627a44a77862f1d`, packet
  `standalone/2026-09-07-astra-future-realization/`.
  PROOF.md: 17,291 bytes, Git blob `cd5d68c82169f32da6b41eb788b7313ed5d7e547`.
  verification.json: 4,366 bytes, Git blob `bd1d5915847416c22a7daa49046d195441b2081d`.
  Full SHA-256 identities are in SOURCE_LOCK.json and hardcoded in check.py.
  Both were freshly read remotely in this pass. The supplied archive copies
  match these identities. The input polynomial, source normalization, safe
  source norms and full filtered-source cutoff inequality are retained.
- The earlier optimal-tail manuscript supplied by the user describes the
  intrinsic horizon minimum and the prospective future-correction route.
  This packet does not depend on an unverified publication of that manuscript:
  the conditional completion and required output-growth estimate are restated
  and proved where used. No prior numerical result is counted as a new replay.

## Classical analytic inputs

- NIST Digital Library of Mathematical Functions, 25.11.5 and 25.11.6,
  https://dlmf.nist.gov/25.11 . The Euler-Maclaurin/fractional-part identity
  supplies the analytic continuation and elementary bounds used here. The
  exact variant needed in the proof is derived from the same integral.
- Standard Jensen formula, Harnack inequality, finite disk Blaschke division,
  Riemann-Lebesgue lemma, Hardy-Laplace Plancherel and inner/outer factorization.
  The local constants, exceptional-set estimates, and bounded-controller
  implication are derived explicitly, rather than imported as RH-specific
  theorems. Euler's divergence of sum_p 1/p is reproved in the text.
- Catherine Beneteau and Raymond Centner, *A survey of optimal polynomial
  approximants, applications to digital filter design, and related open
  problems*, arXiv:2102.01725, https://arxiv.org/abs/2102.01725 . Context for
  least-squares inverses, digital filters and cyclicity. Only bibliographic
  abstract/context was consulted; no uninspected convergence-rate theorem
  from that work is used.
- Bettin, Conrey and Farmer, *An optimal choice of Dirichlet polynomials for
  the Nyman-Beurling criterion*, arXiv:1211.5191,
  https://arxiv.org/abs/1211.5191 . The abstract explicitly retains RH and an
  inverse-zero-derivative hypothesis. It is NOT used to fill the missing
  unconditional rate here; no theorem from it is a proof dependency.

The functional equation and ordinary Euler expansion of zeta are used in
standard unconditional forms. No critical-line zero computation, simple-zero
assumption, RH, Lindelof bound, PNT rate, or reciprocal-zeta estimate is imported
into the new component theorems. The source's closed-space interpretation uses
the classical Hardy factorization, with its singular-factor boundary made explicit.

## Novelty and permissions

No novelty or priority is asserted for minimum-modulus methods, feedback
iteration, Hardy factorization, Toeplitz Grams, or classical zeta criteria.
The proposed additions specialize and combine them at the frozen literal source.
No external paper, font, dataset, or external code is redistributed. Two unchanged
repository files accompany the downloadable replay subset solely as its pinned
parent dependencies; they are not copied over their resident repository versions.
