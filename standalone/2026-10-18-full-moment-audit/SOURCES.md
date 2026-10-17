# Sources, dependencies and reading scope

No RH/GRH, unproved native moment or signed-covariance estimate is an input to
the new upper theorems. They are source-qualified deductions from the stated
analytic theorems/interfaces below. None of the deep proofs was rebuilt or
Lean-verified in this pass. No global literature-priority claim is made.

## Fresh primary reads

1. Leo Goldmakher and Benoit Louvel, *A quadratic large sieve inequality over
   number fields*, arXiv:1112.1642v2 (31 May2012), Theorem1.1, Corollary1.2,
   Definition1 and reciprocity conventions. Primary PDF:
   https://arxiv.org/pdf/1112.1642
   Printed page2 was rendered and read. Both squarefree indices, primitive
   quadratic-family conditions, fixed field/modulus constants and powers of
   an even-order family are retained. The CT identification of its actual
   reflected character with that family is an adopted interface, not proven
   by the finite rational Jacobi fixtures here.

2. Alexandre de Faveri, *Optimal large sieve for fixed order characters*,
   arXiv:2610.04045v1 (2 October2026). Primary HTML:
   https://arxiv.org/html/2610.04045v1
   Freshly read: Theorem1.1, definitions of Xi_n and Theta_n, Section2.5's
   conductor/multiplicativity/zero extension, the sixth-power decomposition
   mechanism and Section9's full detector calculation. Both Theta indices
   are nth-power-free. For n=6 its four monomials are precisely those used
   in NUMERATOR_HIERARCHY and CRITICAL_TARGET. Fixed field, S and generator
   data constants are NOT uniform over these parameters. The full norm of
   a sixth-free ideal, not its radical or conductor, indexes the family.
   The stated cubic conductor-ordered second moment is not imported as a
   sixth-order theorem. No new zero-density claim is made in this packet.

3. Valentin Blomer, Leo Goldmakher and Benoit Louvel, *L-functions with n-th
   order twists*, arXiv:1112.1650, Section5, especially the complete-column
   AFE and the zero detector before Cauchy. Primary PDF:
   https://arxiv.org/pdf/1112.1650
   Printed page18 was rendered and read. It documents the classical AFE/
   Mellin mechanism and separates numerator L-values from reciprocal ones.
   The present all-order AFE deduction is supplied in full, not asserted
   to be BGL's printed all-order theorem. The new theta hierarchy needs
   only item1 and the pinned reflection, not BGL's zero detector.

## Adopted CT interface and exact archive

Dean Cureton and Jesse Thorner, *A quasi-Riemann hypothesis for Dedekind
zeta functions*, Hexagon2610.00200v2. Direct fresh access to both the landing
record and the TeX endpoint failed during this pass. The attempted endpoint:
https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex

We instead read in FULL the delivered thirteen-file short-support source's
REFLECTED_MOMENT.md, whose exact original tree is
`a80cb7e2404e0f6835c47017597b6acbeb9cb264`. It is recovered in #966 through
`standalone/2026-10-17-short-support-recovery/`. In particular R-A/R-B,
(R3)-(R6), and the bounded generator/local-class semantics are the adopted
inputs. THETA_ALL_MOMENTS Sections2-5 state them and reconstruct the
higher-order deduction without extrapolating the M>1 corollary. The original
k=1 theorem and subunit-length tail technique are prior work and credited.
An error in this exact reflection interface would invalidate the theta
application, even if the abstract quadratic-polynomial lemma remained valid.

## Exact repository sources read, not silently merged

- #971, `3f1d2a07631eb6cca1f2716be01f64e874667639`: live recovery metadata
  was checked. The ramified packet is already resident. This pass does not
  duplicate it or promote its proposed local/shifted-detector proofs.
- Pending eighth packet: thirteen original files, tree
  `2385ec9053f269f736ee52f54bfd7c1af60d26c5`. MOMENTS.md and its surrounding
  source/validation records were read. Its original manifest and normal/
  optimized checker were freshly replayed, byte-identical. Recovery is now
  separately published on this branch, without historical qualification edits.
- #968, `14f544fb4293ffb59942ff8d345ab9d6da67025c`: its central all-order
  numerator formula was inspected in the live detailed PR description and
  credited. The full packet was NOT independently replayed here.
- #969: the off-central fourth-order conductor argument was read in the
  preceding packet's complete source context. Its original right7/12 and
  left5/12 conclusions are not claimed new here. Latest PR metadata was seen;
  its full final contour composition is not an input.
- #974, `89c37b6707cb77fc5a86143ea98d8756759fdcbc`, actual file
  `standalone/2026-10-17-three-route-continuation/critical/DIAGONAL_FINITE_PART.md`,
  was read through a live full content fetch. Its zero-sensitive first finite
  part and the physical factor Z^(-1/2)(Z/Y)^s Y^v are cited only as an
  alternative target. No projection upper bound is inferred from its
  holomorphic bare residue. The other routes in #974 were description-only.
- #955's norm-twist/native-coherence warning and #961's high-powerful
  localization are prior context. The new Hk corollary extends the latter's
  k=1 calculation; no claim that those earlier packets are independently
  certified follows from this pass.

No complete repository-wide independent review, new source-import theorem,
formal dependency audit, L-value evaluation, zero census or remote CI result
is claimed. The base/main and all frozen inherited mathematical files remain
unchanged. The checker verifies finite identities and exponent algebra; the
written proofs carry the infinite quantifiers.
