# Validation and independent-review boundary

Status: proposed analytic composition, not an independently reviewed theorem.
Proof and checker have the same author. No independent agent/human referee,
Lean build, full-repository validator, upstream theta reconstruction, transitive
axiom audit or remote CI result is claimed.

## What actually ran

- `python verify.py` and `python -O verify.py` reproduce CHECKS.json byte for
  byte. The exact checker uses only integer/Fraction arithmetic and explicit
  exceptions; it does not depend on Python assertions remaining enabled.
- 1,344 explicit predicates include 286 contour-domain checks, 30 norm and
  30 height detector checks, 9 contribution identities and their whole-interval
  Bernstein budgets, 24 reciprocal-disk checks, 30 separate scalar exponent
  reconstructions and 4 positive-theta model identities. The count also includes
  256 synthetic partitions, 512 lower-count/upper-contour membership checks,
  125 synthetic complex weighted-Cauchy cases, and setup/domain guards.
  They are not 1,344 independent analytic cases or actual Hecke computations.
- `run_mutations.py` launches FIVE separate optimized Python processes. Each
  fails at its designated gate: reverting the mean to individual convexity,
  charging a middle class at its upper zero threshold, omitting the full good
  class, using M=1, and retaining the old Mellin shift. MUTATIONS.json records
  the actual failures. These are mutated finite proof models, not proof-assistant
  perturbations of the analytic theorem.
- Syntax compilation, the payload manifest, normal/optimized replays, and all
  five negative controls passed again after fresh ZIP extraction. The download
  archive's payload bytes agree exactly with the frozen local directory.
- Both prior pending packets' full checkers and manifests were freshly replayed;
  see RECOVERY_AUDIT.md. They are already remotely recovered on #958.

## What the exact calculation does and does not establish

Every polynomial inequality in e is checked using rational Bernstein
coefficients on the WHOLE interval [0,1/100000]. Strict legal domains use
0<e; zero at the left endpoint of a margin is allowed only when positivity
on the open interval is proved. The check explicitly rejects an analytic
application at e=0. Scalar substitutions are an additional cross-check, not
the basis of the whole-interval assertion. No floating-point optimizer or
fitted exponent is used in the published proof.

The finite checks do not authenticate CT's theta realization, prove the BGL
mean or DF large sieve, validate the infinite AFE/tail arguments, identify
Hecke characters in an actual computed field, or certify an RH statement.
The proposed theorem stands or falls with the complete written source adapter
and analytic composition, not with the predicate count or Git hashes.

## Fresh primary-source audit

Unlike #958's recorded source-access limitation, the actual CT v2 body and TeX
were accessible through the web reader in this pass. The load-bearing scale,
family, correction and height interfaces were read in that primary source.
BGL Section 5 was inspected as rendered PDF pages; DF's character construction
and full zero-detector substitution were read in its primary HTML. SOURCES.md
records the scope. This is a fresh interface audit, not certification of every
upstream theorem or a claim to have downloaded and built the upstream library.

## Priority adversarial review

First inspect PROOF Section 3: choice-compatible generators, finite S-unit
characters, complete columns and powerful rows in the fixed-twist central
mean, and applying that mean to a zero-selected subset with row-dependent
correction/reciprocal factors. A defect there would invalidate the new gain.

Then inspect Sections 4--6: fixed exceptional sets before arbitrary later
losses; actual zero-free rectangles and conjugation; both principal residues;
all four disjoint classes; every horizontal/large-frequency tail; new Mellin
normalization; and the fixed-positive-e, point-by-point limit. The numerator
mean must never be advertised as a bound for inverse L-values or for the
principal native critical moment. All new mathematics remains proposed.

## Publication semantics

The packet is additive on parent #958 at
e6dfa07d07ed7a5d049039d7255919a992cadc77. No inherited file is edited, deleted,
or promoted. The publication receipt outside the payload records the resulting
commit, branch, PR and remote tree read-back. A local packet is not a claim
of a clean complete repository clone. The container's direct network download
failed DNS; all remote publication uses the connected GitHub actions.
