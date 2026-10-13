# Sources and scope

## Repository sources

- Publication base: PR #943, 24cb2cdd6e768c2c35ef87227ed8319cfc2d14ed,
  branch research/native-degree-phase-20261013. Live metadata and recent PR
  descriptions were checked. The preceding work was already published; no
  recovery or merge is performed by this pass.
- AGENTS.md and STATUS.md were read at the base. It requires own-branch proposed research
  and separates finite tests from independent mathematical review.
- PR #942, 377f548cab8759399aca80ed3188c495667d562a,
  standalone/2026-10-13-native-principal-census/BANDLIMITED_PRUNING.md:
  the complete proof was read, locally and through the live connector at
  the base. The fixed majorant, Euclidean dual gap, low-period cancellation,
  sharp/smooth distinction and mass obstruction are credited to this source.
- The same packet's PROOF.md was read for the exact principal definition,
  alias/zero conventions and principal upper bound. Those are inherited
  inputs to the full-moment implication, not new conclusions of this pass.
- The same packet's census.py is copied unchanged as native_helper.py.
  Git blob: 2a074ccede483324392a729056ccbf43a1f26eac.
  SHA256: b0f35164674ec01549788954905b2b23ad62fdbf6fba2a7cfa3bf4b340e0b52c.
  Its primitive arithmetic is used in the finite tests. Its large census
  functions are not executed by this checker.
- PR #940 at 59d5a8ebcd390ff898d63b2fc5ed7290995ae58b, singleton-budget
  MATHEMATICS.md, was available in the read source context and its current
  description was checked. Its log-square singleton scope is compared with
  our example. No theorem from it is required for PROOF.md Theorem 2.
- #943's degree and microscopic-phase results are background motivation,
  not analytic premises. Other recent PR descriptions were checked for
  overlap, not independently reconstructed. No exhaustive novelty audit
  or priority claim is made.

## Classical inputs

Poisson summation and Fourier normalization: Andrew V. Sutherland,
MIT 18.785, Fall 2021, Lecture 17, Section 17.1 and Theorem 17.8:
https://math.mit.edu/classes/18.785/2021fa/LectureNotes17.pdf
The text and page 3 were inspected online. The needed two-dimensional
lattice specialization is written out in Lemma 1.

The O(t) ideal/element count, convergence of sum (Nv)^(-A) for A>1,
fixed-order ideal divisor bounds, finite-field orthogonality and CRT are
standard elementary inputs, with the needed uses explained in the proof.

The classical prime number theorem in the fixed progression 1 mod 3 is
needed only for asymptotic nonemptiness of the illustrative prime family.
It is NOT used in any upper theorem or in the exact finite norm witness.
No growing-modulus prime theorem is assumed. The earlier repository source
for fixed-field prime counting is Burgin, arXiv:2406.08565v2; this pass does
not independently reconstruct that external theorem.

The current abstract of de Faveri's arXiv:2610.04045 was consulted during
reconnaissance; an attempted HTML fetch failed. None of its estimates is
imported. Neither an imported quasi-Riemann theorem, GRH, native higher
moment nor a new large sieve enters this packet.

The explicit positive infinite-convolution construction in Section 2A is
a standard smooth-cutoff/Fourier-decay mechanism, proved at the needed scope
here. Its use is solely to obtain fixed-test, growing-order truncation
constants; it does not randomize the native arithmetic.

The contribution is a scoped composition of classical/inherited tools,
not a claim to invent Poisson summation, inclusion-exclusion or sieve
localization. The same-author proof remains proposed pending review.
