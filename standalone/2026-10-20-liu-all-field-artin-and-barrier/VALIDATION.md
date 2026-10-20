# Validation and reconstruction

The finite checkers verify the displayed algebraic and finite-group claims.
They do not certify the external zero-free theorem or the written analytic
arguments. Source and proof reviews are separately recorded in REVIEW.md.

## One-command standard-library replay

From this packet directory, run:

```sh
python -I -S -B replay.py
```

This authenticates every sibling file against MANIFEST.json, parses the Python
sources, verifies the local Markdown links, and runs each of the following
four programs in both ordinary and optimized isolated Python. Every output
must match its committed receipt byte for byte. Explicit exceptions implement
acceptance, so `-O` cannot remove a gate.

The manifest identifies the packet contents; its digest is bound by the
published Git commit. It is not an external signature or a substitute for
reading the pinned source formulas. The checkers reconstruct their finite
objects rather than trusting a `PASS` field in a supplied JSON file.

## Finite mathematical contracts

| Program | Arithmetic and primitive input | Coverage / acceptance | Stored receipt |
|---|---|---|---|
| beyond_hybrid_barrier.py | EXACT_RATIONAL; Fraction intervals, polynomial remainder arithmetic, source comparison formulas and quartic | Root bracket and derivative; every division; direct original critical E_av substitution at b=0,1; four affine b intervals including the unbounded ray; four free-length identities and four negative-b identities; exact coefficient inequalities | beyond_hybrid_barrier.json |
| verify_a5_artin.py | CERTIFIED_INTEGER_COVERAGE / EXACT_RATIONAL; even permutations of five symbols, Z[z]/Phi_15 | All 60 elements, actual A4 and C5 subgroups and homomorphisms, every induction sum, all five irreducible character rows and 25 inner products, nonmonomial obstruction | A5_CERTIFICATE.json |
| verify_principal_factorization.py | EXACT_RATIONAL; three independent local variables v,D,R and integer phase/exponent tuples | Six cleared-denominator identities and five algebraic negative controls; angular phase and eta^6 retained | PRINCIPAL_FACTORIZATION_CERTIFICATE.json |
| run_barrier_mutations.py | Exact source mutations executed in isolated optimized Python | Changed quartic, broken witness join, and flipped unequal-length sign must each fail at its designated gate; original source remains unchanged | beyond_mutation_controls.json |

The barrier's rational interval operations enclose the specified algebraic
root. They are not ordinary floating-point calculations described as directed
arithmetic. Decimal conversions appear only in human-readable output; they
do not determine acceptance. The entire b continuum is covered by exact
affinity and checked slope signs, not by a finite b grid.

The critical-class identity is checked directly from the original averaged
exponent in Q[k]/(Q), including denominator coprimality. Acceptance does not
assume the algebraic conclusion of source Lemma 14.9. The source count and
endpoint formulas themselves remain the stated inputs to the scalar theorem.

Individual replays, if desired:

```sh
python -I -S -B beyond_hybrid_barrier.py
python -I -S -B verify_a5_artin.py
python -I -S -B verify_principal_factorization.py
python -I -S -B -O run_barrier_mutations.py
```

## Independent symbolic implementation

The optional verify_independent_review.py uses SymPy 1.14.0. It was written
separately from the standard-library checker and reconstructs 22 exact
identities from the mathematical expressions. These include the critical
averaged zero at b=0,1, its nonvanishing denominators, all four affine and
negative-asymmetry reductions, the unrestricted direct dual, the principal
local factor, both boundary-polynomial substitutions, and the annular weight.

In an environment with SymPy 1.14.0 installed:

```sh
python -B verify_independent_review.py
```

The output matches INDEPENDENT_SYMBOLIC_REVIEW.json. This is a second algebra
implementation, not a second proof of the upstream analytic theorem or a
replacement for the rational witness sign coverage.

## Source reconstruction

SOURCES.json records the exact arXiv version and PDF digest, the source
locators used by each argument, primary references for the classical
ingredients, and the relevant repository commits. The full source can be
retrieved from <https://arxiv.org/pdf/2610.26835v1>; its SHA-256 must be

```text
5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5
```

The source was read in both extracted text and its rendered principal-local-
factor pages. It is 136 pages. Only original notes and source locators are
contributed here; the PDF is not republished under the repository license.

## What was not validated

No entire-repository test run, native theta rebuild, new zero census, global
Lean formalization, or complete independent reconstruction of source
Sections 10-12 was performed. The scalar checker does not validate the
unproved mixed U^(6/5) target. The field-uniform small-prime constant was not
computed, and no actual ray-class computation or least-prime search was run.

The recorded reviews are file-level reviews by separate AI agents in this
research session. They are not human referee reports or an integration vote.
The draft PR's exact head SHA identifies the assembled packet submitted for
subsequent review; main's integrated scientific status is preserved.
