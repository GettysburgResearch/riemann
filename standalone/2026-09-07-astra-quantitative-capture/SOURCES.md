# Sources and dependence boundaries

## Repository and supplied artifacts read in this pass

- PR #812 was read at `2d683186cb3dd4f304159d8176215ceae8ac59fb`, including
  `standalone/2026-09-07-astra-feedback-and-conditioning/PROOF.md`. It records
  the fixed finite-controller obstruction and an overlapping quasipolynomial
  conditioning theorem. This continuation does not reuse that forbidden
  fixed-controller Newton composition.
- The supplied source-stability proof is 17,698 bytes, SHA256
  `63dda3d0ff38e28829ca7d80a491201a12a32b7282c8b301f2aef54d062e58b8`, Git blob
  `d407fcc6b2ecf7d92f9393c3fc474f445095ca31`. Its upload was subsequently
  confirmed by PR #814 at `dc7babb830cb696810fb68bd74f6a33459f5f921`.
  This pass read that source and reconstructs the relevant small-value proof.
  The uploader's Windows symlink limitation remains part of ITS receipt;
  no fresh parent test run or independent confirmation is claimed here.
- The optimal-tail and future-realization manuscripts supplied in the
  conversation were read for the target, horizon, source-domain and compact
  realization conventions. No prior Python producer is executed or imported.

The new proof is self-contained at the component level apart from the
classical analytic inputs below. SOURCE_LOCK.json records lineage; its
validation is a metadata-consistency check, not a new authenticated remote
checkout or an independent mathematical review.

## Classical inputs

1. NIST DLMF, section 25.9, approximate functional equation (25.9.1), used ONLY
   for |zeta(1/2+it)|=O((1+|t|)^(1/4)), by absolute estimates of its two
   length-sqrt(t) sums. https://dlmf.nist.gov/25.9
2. NIST DLMF, section 25.2, Euler--Maclaurin continuation. The fifth periodic
   Bernoulli remainder and elementary bound used in HC26 are displayed and
   estimated in the proof, including the removable pole normalization.
   https://dlmf.nist.gov/25.2
3. Classical Hardy inner/outer factorization, outer Poisson formula, Beurling
   cyclicity, and the projection onto B H2. Context checked in the primary
   paper J. A. Ball, V. Bolotnikov and Q. Fang, "Multivariable backward-shift-
   invariant subspaces and observability operators," arXiv:math/0610634.
   Only the classical scalar Hardy statements are imported; no multivariable
   theorem or rate is needed. https://arxiv.org/abs/math/0610634
4. Jensen, Harnack and Cauchy estimates; Plancherel, Fourier/Hilbert projection
   on the circle, Fejer-kernel positivity, and elementary Holder interpolation.
   Their quantitative uses and fractional-norm equivalences are proved in the
   manuscript rather than imported as unverified rate theorems.

No novel-priority claim is made for clipped outer regularization, fractional
Dirichlet methods, polynomial approximation, Hardy projections or feedback
ideas. Source-specific composition and the horizon-uniform application are
submitted as proposed component results; literature exhaustiveness is not
claimed. No alleged full proof found in a search is used as an input.

## What is NOT assumed

RH, a zero-free critical half-plane, Lindelof, a square-root Mertens bound,
simplicity, separation of zero ordinates, an oracle for B, a uniformly bounded
source inverse, or a vanishing intrinsic minimum. Possible off-line zeros
are retained in the regularity estimates. No singular inner factor is
silently discarded; its exclusion for this source is argued explicitly.
