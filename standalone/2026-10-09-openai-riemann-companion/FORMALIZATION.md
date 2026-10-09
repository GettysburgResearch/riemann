# Formal source coverage and verification boundary

Status: **IMPORTED / LEXICALLY AUDITED / NOT KERNEL-REPLAYED HERE**.

This packet preserves the advertised comparison statements, their JSON mappings,
and the transitive internal implementation imports. It does not report a fresh
Lean build, Comparator run, independent checker run, or full semantic audit.
The original core's [formalization audit](../2026-10-07-openai-quasi-riemann-import/FORMALIZATION_AUDIT.md)
remains a separate historical record.

## Exact scope

The combined selected view contains **12 comparator configurations**, mapping
**19 theorem names** to **10 distinct solution modules**. These are eight new
comparators and the four inherited family-003 comparators. The generated
[dependency audit](checks/artifacts/dependency-audit.json) records the exact
configuration contents and complete external-import inventory.

The internal implementation inventory comprises **11,576 Lean modules and
1,414,189 source lines**. It includes the complete original core selection plus
the transitive internal imports needed by the selected new solution modules;
it is not advertised as the smallest possible closure. The lexical traversal
found no missing internal imports and no scanned implementation markers.
It records **762 distinct external module imports**. Those external package
implementations are not vendored or independently audited here.

### Comparison map

Paths below are relative to the `lean/` directory in the assembled view. The
configuration for each row is `ComparatorChallenges/<name>.json`; its paired
challenge specification is `ComparatorChallenges/<name>.lean`.

| Family | Comparator name | Solution module | Advertised scope |
| --- | --- | --- | --- |
| 003 | `QuasiRiemannHypothesis` | `OAI.NumberTheory.DirichletL.Nonvanishing` | Zeta nonvanishing in the strict half-plane $\Re s>7/8$ |
| 003 | `DirichletSevenEighths` | `OAI.NumberTheory.DirichletL.Nonvanishing` | Dirichlet L-function nonvanishing in that half-plane |
| 003 | `HeckeSevenEighths` | `OAI.NumberTheory.DirichletL.Hecke.Nonvanishing` | The specified finite-order Hecke family over $\mathbb Q(\sqrt{-3})$, with its pole exclusion |
| 003 | `SiegelZeros` | `OAI.NumberTheory.SiegelZeros.Main` | The two mapped absolute real-zero-gap statements |
| 007 | `OrdinaryElliott` | `OAI.NumberTheory.OrdinaryCorrelations.Elliott.Main` | Corrected ordinary Elliott statement under the stated nonpretentiousness hypothesis |
| 007 | `OrdinaryTwoPointCorrelations` | `OAI.NumberTheory.TwoPointCorrelations.FinalMain` | Liouville logarithmic saving, binary corrected Elliott, and affine corrected Elliott |
| 012 | `JointDickman` | `OAI.NumberTheory.JointDickman.PaperMain` | Joint ordinary-density law and both strict largest-prime-factor ordering densities |
| 021 | `Jacobsthal` | `OAI.NumberTheory.Jacobsthal.Main` | Quadratic Jacobsthal bound |
| 021 | `JacobsthalImproved` | `OAI.NumberTheory.Jacobsthal.Main` | Iterated-logarithm improvement |
| 023 | `PattersonFirstMoment` | `OAI.NumberTheory.CubicMoment.Theta.CubicThetaMains` | First moment, angular comparison, and fixed angular cancellation |
| 026 | `PrimeGaps` | `OAI.NumberTheory.PrimeGaps.RatioCorollary` | A conjunction: positive lower density of large gaps for each fixed positive threshold, and positive lower density of prime-ratio increases |
| 182 | `SquareDifference` | `OAI.Combinatorics.SquareDifference.Main` | The square-difference-free power-saving theorem only |

The [related-results review](RELATED_RESULTS.md) links the resident manuscripts,
scope documents and new specifications, and records their mathematical
hypotheses. The generated audit gives every fully qualified theorem identifier;
the JSON source is the authority for which names a targeted comparison checks.

## Important differences between a paper and its comparator

**Family 029 has a broader-field Hecke theorem but no advertised main-claim
comparator in this selection.** Its cyclotomic-field half-plane
$\Re s>1-10^{-6}$ is not the statement of `HeckeSevenEighths`. Importing the
latter does not formalize the former.

No main-claim comparator or per-family scope document was advertised for
families **011, 014, 029, or 142** in the inspected catalogue. Some ingredients
may appear in other modules; that does not establish formal coverage of these
papers' main claims.

For **182**, the supplied comparator concerns squares. The two later papers
on general intersective polynomials and prime arguments remain separate
manuscript assertions. For **026**, `lean/docs/026.md` describes the prime-ratio
corollary, while the actual mapped challenge theorem contains both claims
listed in the table. This source discrepancy is retained explicitly.

The comparison specifications intentionally contain `sorry` placeholders for
the challenge claims. They are interfaces against which the separately named
solution modules are compared. Their presence must not be confused with a
proof in a solution module. Conversely, absence of lexical markers in the
implementation does not establish that it proves the intended mathematical
statement or uses only permitted axioms.

## What the lexical audit does

The checker reads the selected `.lean` source, masks comments and string
literals, follows static internal `OAI.*` and `ComparatorChallenges.*` imports,
and records implementation markers using the inherited audit patterns. It
recomputes the configuration map from the resident JSON files. This detects
missing source dependencies and specified textual markers; it is not a Lean
parser, elaborator, dependency-package audit, or theorem-equivalence checker.

The selected configurations permit `propext`, `Quot.sound`, and
`Classical.choice`. All twelve set **`enable_nanoda: false`**. These are recorded
configuration settings, not a claim that this contribution executed an axiom
check or an independent kernel.

## Reproduction environment

The preserved toolchain is **`leanprover/lean4:v4.34.1`**. The upstream Lake
configuration, package manifest and compatibility patches are included in the
combined selected view. Lake's hooks clone and patch external packages at
their recorded revisions. Preserve those pins and run the hooks only in a
fresh assembled working copy.

The [reproduction guide](REPRODUCE.md) lists the twelve targeted Comparator
commands from the upstream workflow. An untargeted build of the entire OpenAI
umbrella library is outside this selection. At the time of this contribution,
`lean`, `lake`, `comparator`, `landrun`, and `lean4export` were unavailable in
the execution environment; none was run.

For a future formal-validation record, freeze the companion head, assemble its
exact manifest, record the tool and dependency versions, run the specified
comparisons, and preserve their outputs. Review the exported statements and
definitions as well as the exit status. A successful formal run and a
mathematical acceptance review are distinct contributions.
