# Sources, exact versions, and independence

## Repository source objects

Repository: GettysburgResearch/riemann.
Observed PR #803 head at the start of this pass:
`93e5d45b63f6a9a60f981e81df589feff1ba1cfb`.
Its reported root tree was `a972bff8286b446c9797fc09d2c4375341cc131b`.
The live PR metadata and the height-transfer proof were read through the
connected GitHub tools. AGENTS.md was read at that same commit.

The corresponding local parent proof bytes were authenticated by Git blob
hash and SHA-256 before this work. These two exact objects are retained in
SOURCE_LOCK.json and rechecked by verify.py:

1. `standalone/2026-09-06-logarithmic-core/annular-scalar-route/PROOF.md`.
   Git blob `0f1b21227d064e61f4f532d9025c78106baa688e`.
   Parent AS1--AS4 supplies the fixed arithmetic normalization, all-powers
   compact filter, local archimedean correction and conditional Landau consumer.
   AS5 is the weaker continuous-source control extended here. Its proof is
   not an independent acceptance of this author's own earlier work.
2. `standalone/2026-09-06-logarithmic-core/height-transfer-and-prime-squares/PROOF.md`.
   Git blob `2ee61d78b5bcf8e06de973f7e29634112c37e1a9`.
   Read for current state and exact native scalar. Its finite-height theorem
   is NOT an input to ET1--ET6; no new zero-verification result is imported in
   this pass. The earlier large positive range remains at its previous scope.

No original parent producer or large source campaign is newly replayed.
The predecessor proof hashes are not claims that those analytic proofs have
been machine-checked. New paper proofs require non-author review.

The earlier #792 Hardy/Laguerre bridge was also consulted at
`465cb28ed8cbfa1bb071d9a85eeda9890decfe6b`, path
`standalone/2026-09-05-bernstein-chebyshev-growth/cross-route-hardy-laguerre/BRIDGE.md`,
for the distinction between a conserved form and its positivity. Its
operator/core/certification theorems are not needed for the present results.

## Classical inputs and online reading

- NIST DLMF 27.12, Prime Number Theorem, especially 27.12.5:
  https://dlmf.nist.gov/27.12
  Used only for the ordinary qualitative PNT after deriving the elementary
  all-x Chebyshev bound in the paper. The usual equivalence psi(x)~x follows
  by partial summation and the elementary negligible higher-prime-power bound.
  No optimized constant, modern prime record or finite zero range is imported.
- NIST DLMF 25.10(i):
  https://dlmf.nist.gov/25.10
  Used for classical zero-free Re s>=1, real-axis/trivial-zero distinctions,
  and the standard zeta-zero symmetry. The analytic discrete zero set is
  countable. No hypothesis about its actual off-line members is assumed.
- NIST DLMF 27.4:
  https://dlmf.nist.gov/27.4
  Euler products and Dirichlet convolution context. Every local coefficient
  formula used here is independently derived in the paper.
- M. Suzuki, Screw functions of Dirichlet series in the extended Selberg class,
  arXiv:2209.12832v2:
  https://arxiv.org/html/2209.12832v2
  Prior art for one-sign/screw criteria. Its class-specific theorem is NOT
  applied to F, which does not satisfy the Riemann functional equation.
  The required one-sign implication is reproved from the explicit model
  transform and the elementary Landau theorem.

These primary/reference pages were accessed in this pass. No new original
PDF examination or imported computational certificate is claimed.

## Proofs supplied rather than unnamed analytic assumptions

The finite-prime phase approximation is proved by unique factorization,
Fourier-character time averages, and trigonometric approximation of a bump.
The safe-moment parameter exclusion uses analyticity and uniqueness of an
absolutely convergent Dirichlet series, with its least-index proof given.
The full model pole and the functional-equation failure are checked at their
specific points. The all-order Selberg hierarchy follows by an exact induction.
The PNT transfer to the fixed annular test is derived by Stieltjes integration.

No novelty claim is made for the classical mechanisms or the specialized
counterfamily absent a separate literature review. This is a proposed research
continuation, not a Reviewer-C acceptance report or an RH completion.
