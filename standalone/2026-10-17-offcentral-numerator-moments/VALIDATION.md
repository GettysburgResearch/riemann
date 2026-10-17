# Validation: finite certificates and analytic review boundary

Status: same-author proposed analytic proof and finite checker, not an external
referee report, formal build or accepted global theorem. The checker does not
prove the large sieve, functional equation, approximate functional equation,
metaplectic reflection, infinite convergence arguments, or family identification.

## Executed checks

The complete `verify.py` run passes **4,399 explicit finite predicates**,
including setup and repeated guards. Ordinary and optimized Python reproduce
CHECKS.json byte-for-byte. All scripts syntax-compile. The groups include:

- 72 AFE monomial checks at the three conductor/column triangle vertices,
  for orders 2,4,8, plus six right/reflected exponent identities. Affineness
  makes the vertex calculation cover all conductor sizes in those triangles;
  it is not sampled numerical optimization.
- 784 exact two-prime column decompositions and 1,568 abstract character-mask
  identities, retaining exponent-6/7 columns and shared residual/power primes.
  These are formal root-of-unity/zero fixtures, not Hecke computations in a
  real number field or a full physical theta census.
- 57 local divisor-convolution identities and 768 finite Holder arrays.
- 140 norm and 140 height density monomials (all ten per threshold), plus
  parameter/formula guards. All fifteen classes, actual lower-count/upper-
  contour membership and the full rational quadratic budgets are retained.
- 495 central contour guards, other principal/small/large contour guards,
  70 reciprocal-disk inequalities, actual scale/mellin/remainder identities.
- 35 finite cross-checks of identities in the positive-estimate model. The
  universal asymmetric optimization rests on MODEL.md's written case proof,
  not these finitely many examples.

The polynomial utility and DF substitutions in arith.py are adapted from the
historical verifier recovered in #967 and credited. The off-central AFE,
complete-column, Holder, new class assignment and diagnostic checks are newly
written. This is not advertised as a wholly independently authored codebase.
Rational Bernstein coefficients certify every e-polynomial budget on the
entire interval [0,10^-6]. The strict analytic domains use 0<e; no theorem is
applied at e=0. No floating-point optimization or measured L-value is a premise.

## Ten executed negative controls

`run_mutations.py` launches ten separate optimized Python processes and requires
a specified failing gate in each. They alter the dual conductor weight, erase
the sixth-power mask, add false residual/power coprimality, revert fourth or
eighth off-central means to reflected second means, count a middle class at
its upper threshold, reuse the old small-z line, delete the diagonal reflected
term, set the large-tail gap to zero, or retain the old Mellin shift.
MUTATIONS.json records the actual exit codes and gates. These are corrupted
FINITE models, not proof-assistant perturbations of the analytic theorem.

## Reproducibility and publication semantics

The manifest authenticates every packet file except itself using byte length,
SHA-256 and Git blob identity. A fresh ZIP extraction is replayed with normal
and optimized checkers, all ten mutations and the manifest before delivery.
The separate publication receipt records the resulting remote commit/branch/PR
and read-back scope; a locally stored file or Git object is not itself a push.

The new directory is additive on #967. No inherited source, main or integrated
scientific-status statement is edited. The prior thirteen-file recovery and
its fresh complete replays are documented in SOURCE_REVIEW.md, not counted as
new research. No unseen archive from another conversation is claimed recovered.
No full-repository validator, remote CI result, independently computed actual
zero census, Lean elaboration or transitive axiom audit is claimed.

Priority analytic review: BOTH off-central AFE terms and small conductors;
complete-column summability and masks; inherited short-support reflection;
family/zero-density transfer; every new contour and the point-by-point e limit.
A defect in any such step would invalidate the claimed global consequence even
when all 4,399 checks and all publication hashes match.
