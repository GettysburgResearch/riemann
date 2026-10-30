# Riemann literature pass — 30 October 2026

Status: **LITERATURE / SOURCE-INSPECTED**, with verification depth stated per item.  
Scope: recent external research relevant to the project's zero-free, signed-moment, positivity, and formalization programmes.  
Exact dependencies: versioned primary sources in [CATALOGUE.md](CATALOGUE.md), [SOURCES.json](SOURCES.json), and [references.bib](references.bib); repository sources in [REPO_MAP.md](REPO_MAP.md).  
What was actually run: web and GitHub source retrieval, version/status comparisons, structured bibliographic checks, and independent editorial review of source scope. No external Lean dependency closure or analytic proof was rerun.  
Smallest remaining gap: assess and reproduce the specific new external input before using it in a repository theorem.

## What changes the research picture

**The most urgent new source is an upstream formal zero-free result merged this morning.** QuasiRiemannTracker [PR #97](https://github.com/GTimG/QuasiRiemannTracker/pull/97), by ArviFoxy, records Dirichlet nonvanishing for
$$
\operatorname{Re}s>\frac{43670599}{50000000}=0.87341198,
$$
excluding the principal pole. The live API confirms a 30 October merge; the archived protected admission records PASS with Lean, NanoDa and con-ron. This pass checked those records and the canonical target, not the complete proof. Start with catalogue **L01** and [TRACKER_EVIDENCE.json](TRACKER_EVIDENCE.json).

This is a narrower stated family than Liu's arbitrary-number-field finite-order Hecke theorem. Keep separate columns for these families. The new source also overtakes the smaller scalar retunes in our current PR #1023; redoing that optimization is no longer the first task.

**Two revisions dated 29 October deserve focused reading.** Liu's all-field paper now has a v2 with additional moment-uniformity material; its stated boundary remains $B_\flat=0.874886647039964\ldots$. Sra's author-site v2 gives finite-order positivity for reciprocal-xi densities. Their value here is in the precise estimates and proof interfaces. Neither revision is presented in this packet as a new RH proof. See **L02–L03**.

The remainder of the catalogue distinguishes new large-value/density tools, conditional negative moments, real exceptional-zero results, finite formalization, and speculative sources. It explicitly marks known imports and access limitations.

## Reading order

1. **L01 and the upstream selected-norm construction:** compare against the exact source of our PR #1023.
2. **L02:** audit the new weighted-moment and two-transform details against our inherited inverse/product-moment interfaces.
3. **L03:** compare reciprocal-kernel positivity with the actual xi/Weil objects used in the repository.
4. Read the analytic tools and arithmetic consequences in the catalogue before choosing a specific next experiment.
5. Use [REPO_MAP.md](REPO_MAP.md) for concrete tasks and [SEARCH_LOG.md](SEARCH_LOG.md) for coverage and exclusions.

## Files

| File | Purpose |
|---|---|
| [CATALOGUE.md](CATALOGUE.md) | Annotated, prioritized primary-source literature |
| [REPO_MAP.md](REPO_MAP.md) | Exact repository overlap and actionable follow-ups |
| [SEARCH_LOG.md](SEARCH_LOG.md) | Search coverage, date/version decisions, and limits |
| [SOURCES.json](SOURCES.json) | Machine-readable bibliography, scope and evidence levels |
| [references.bib](references.bib) | Reusable citations; arXiv and Hexagon identifiers kept distinct |
| [TRACKER_EVIDENCE.json](TRACKER_EVIDENCE.json) | Extracted upstream verification fields and immutable locators |
| [VALIDATION.md](VALIDATION.md) | Checks performed and limits of this literature pass |

## Publication boundary

This packet is additive on main at `f99d9e3908dde4865377c75d9ca051c1f545bf4f`. It adds no native zero-free theorem and does not change the integrated scientific-status files. It cites external research without treating a bibliographic import, a PR merge, an AI review, or finite arithmetic checks as interchangeable forms of mathematical verification.

Original annotations are contributed under the repository's license. Linked third-party papers, software, and formal proofs retain their own licenses. No third-party manuscript or proof dependency tree is vendored.
