# Sources, exact reading levels and dependency boundaries

## Established external input used in the main theorem

Terence Tao, *The logarithmically averaged Chowla and Elliott conjectures for
two-point correlations*, Forum of Mathematics, Pi 4 (2016), e8.
Version: arXiv:1509.05422v4, 29 July 2016.
https://arxiv.org/abs/1509.05422v4
https://arxiv.org/pdf/1509.05422

Theorem 1.3 and Corollary 1.5, printed pages 5--6, are the imported bounded
correlation statements. The PDF text was read, and both pages were rendered
and inspected. Page 6 explicitly discusses the Mobius application and the
strong nonpretentiousness input. The prime-distance perturbation (4.3) and
all unbounded coefficient, CRT, truncation, density and Gaussian arguments
are supplied in this packet.

The entropy-decrement proof and its supporting deep theorems were NOT
independently reconstructed or formally rebuilt. This is a standard theorem
import, not a new proof of the logarithmic Elliott theorem. The finite
checker does not authenticate that theorem. No quasi-RH input is used.

## New ordinary correlation release: NOT a dependency of the main theorem

Repository: https://github.com/openai/math
Pinned commit: 1581d4cbdd69a0faf34b2089614fe2a814316a6a

Inspected:
- lean/docs/007.md, blob dad638d19609ebbddc93a5594dfc2ecd2a26a7a6
- lean/ComparatorChallenges/OrdinaryElliott.lean,
  blob 914f601065031ff59b509058cb3d9d709fd0b23e
- lean/ComparatorChallenges/OrdinaryTwoPointCorrelations.lean,
  blob 8764f91cc16967f765b4f19c4378ff8fb5f29cd0
- lean/OAI/NumberTheory/TwoPointCorrelations/FinalMain.lean,
  blob 2bd48811e73bbdc80c1f738fa889a14189186408

The preprint directory was listed. Its final.pdf blob is
 a1fa025a59ecbfc5176d16cfdc6e0afd418cc82e (819391 bytes), but the full paper
was NOT read in this pass. The scope note and final wrapper state ordinary
affine binary cancellation under uniform nonpretentiousness. Section 8
states the exact additional conclusion conditional on accepting that
external input. A specification containing `sorry` is not the solution;
no claim of a successful comparator, axiom audit, or full Lean build is made.

## Live repository context

Repository: GettysburgResearch/riemann.
Intended patch base: a93d382951f8fac7b0c28783061a7ddb99fcf0a4 (#953).

- #953, a93d382951f8fac7b0c28783061a7ddb99fcf0a4:
  THEOREMS.md in the supplied packet and its live PR description provide
  the source conventions and the divisibility/prime-quotient frontier.
- #952, 3b7d2948840446c752bbf284f6f90f6592395a29:
  the exact Gaussian kernel and its normalization are credited. The relevant
  source was available in the preceding conversation and supplied archive;
  the fixed-lag adapter is proved afresh here.
- #954, 3241178607671c4dd979cefdad0670fd426194da:
  latest PR description read for the full norm-collision and long-twist
  result. No tensor-square theorem is imported into the present proof.
- #955, 20883bec3d5b939d7602beaf2c91dbf102669166:
  live PR description and THEOREMS.md Sections 1--5 read. Its complete
  long-twist theorem does not supply a fixed-twist theorem. It is credited,
  not used as a proof input.
- #779, stationary beta/additive Chowla programme: PR description read.
  The repository already had an additive-correlation coordinate. Neither
  that coordinate nor Chowla as a proposed connection is claimed new here.
- AGENTS.md read at the patch base. Scientific integration requirements are
  preserved: these files do not change any integrated theorem status.

## Prior unpushed packet

The user-supplied riemann-mesoscopic-prime-exchange.zip was inspected. Its
THEOREMS.md was read for the exact proportional-prime family and its scope.
All 13 files are preserved unchanged in the companion recovery patch. Its
old tests were not re-executed in this pass; the archive/manifests and patch
bytes were checked. Its publication labels remain historical and are not
silently rewritten. No matching publication was found in the targeted PR
search; this is not claimed as a full repository-tree absence proof.

## Novelty and scope

No claim is made to have invented CRT, mean-square approximation, arithmetic
progression reindexing, Gaussian/Stieltjes integration or binary Elliott
cancellation. The proposed new repository contribution is their rigorous
application to these exact unbounded prime-power completions, with uniform
powerful-profile tails and complete signed additive-filter consequences.
No exhaustive global literature-priority audit was performed.
