# K839 headline statements grounded in the paper and actual count definitions

Reviewer: search_skeptic. Date: 2026-11-17. Pinned repository: `sources/formal_round2/839-v1`, commit `0e961ea199b425010843bc8044676d4ad29fe031`. Paper: K. M. Knausgård, arXiv2610.08965v1, 6 October 2026, title and Theorems 1.1–1.5, pp1–3. This is a statement/definition audit, not a full proof, build or axiom-closure certification.

**Main scope correction:** `Line889` proves the stated bound for zeros that are **simple OR on the critical line**, counted with multiplicity. Its 88.93% does not mean that 88.93% are on the critical line, distinct, or simple and on the line. The actual definitions, Challenge/Solution types and paper agree on the union interpretation; a directory name alone would not establish it.

## Exact counts and common quantifiers

In every statement the denominator N(T) is `Ncount 0 T`: zeros of Mathlib's actual `riemannZeta` satisfying 0<Reρ<1 and 0<Imρ≤T, weighted by the order of vanishing `(analyticOrderAt riemannZeta ρ).toNat`. This is a positive-ordinate cumulative count, not an absolute-height count.

The exact Lean form of each ratio lower bound q is

`∀ ε > 0, ∃ T₀ : ℝ, ∀ T ≥ T₀, (q − ε) * (Ncount 0 T : ℝ) ≤ target(T)`.

For the average row, `target(T)=(Nsimple 0 T+N0mult 0 T)/2`; all other targets are the indicated count. These are eventual asymptotic lower bounds, not finite-height verification statements or estimates with a displayed effective T₀.

| Paper location | Exact lower bound | Numerator/quantity and its scope | Actual Solution locator | Development headline |
|---|---|---|---|---|
| Theorem 1.1, p2 | 1645064/1960733 = 0.839004596750… | N_d: distinct zero **points anywhere in the open critical strip**, each once | `lean/Solution839.lean:23` (`distinct_zeros_839`) | `lean/Distinct839/Main.lean:19` |
| Corollary 1.2, p2 | 1329395/1960733 = 0.678009193500… | N_s: **simple zeros anywhere** in the strip; multiplicity exactly one | `lean/Solution839.lean:39` (`simple_zeros_678`) | `lean/Distinct839/Simple.lean:66` |
| Theorem 1.3, p3 | 1669159/2478195 = 0.673538200181… | N₀ˢ: **simple AND on the critical line**; each such point once | `lean/Solution673.lean:18` (`simple_critical_zeros_673`) | `lean/Simple673/Main.lean:42` |
| Theorem 1.4 first bound, p3 | 2073677/2478195 = 0.836769100090… | (N_s+N₀)/(2N): **average** of simple-anywhere proportion and critical-line proportion; N₀ includes multiplicity | `lean/SolutionFurther.lean:54` (`average_simple_and_critical_8367`) | `lean/Further/Main.lean:58` |
| Theorem 1.4 second bound, p3 | 3376433/3797325 = 0.889160922491… | N_{s∪0}: **simple OR critical-line**, union counted with multiplicity; first-window consequence | `lean/SolutionFurther.lean:61` (`simple_or_critical_8891`) | `lean/Further/Main.lean:87` |
| Theorem 1.5, p3 | 50652159/56956375 = 0.889315006441… | Same **simple OR critical-line** union count, improved by third window | `lean/Solution889.lean:37` (`simple_or_critical_8893`) | `lean/Line889/Main.lean:45` |

All paths in the table are relative to the pinned repository. The first two constants obey exactly `simple=2q−1`. The average constant is exactly `(1+s₀)/2`, where s₀ is the simple-critical constant in the third row. These identities were checked with exact rational arithmetic.

## Definitions actually read, rather than inferred from comments or labels

* `Challenge839.lean:38–55` defines the zeta predicate, analytic multiplicity, ordinate window, `Ncount`, `Ndist` and `Nsimple`; the two types are at61–68.
* `Challenge673.lean:33–46` has the same underlying zeta/count definitions and defines `N0simple` by intersecting **both** `{ρ | ρ.re = 1/2}` and `{ρ | zeroMult ρ = 1}`. Its theorem is at53–55.
* `ChallengeFurther.lean:53–64` defines `N0mult` as the multiplicity sum on the critical line, `Nsimple` as the cardinality of multiplicity-one points, and the union count as

  `∑ᶠ ρ ∈ zerosIn T₁ T₂ ∩ ({ρ | zeroMult ρ = 1} ∪ {ρ | ρ.re = 1 / 2}), zeroMult ρ`.

* `Challenge889.lean:38–53` repeats the actual zeta definitions and the same union sum; the 50652159/56956375 theorem type is at60–63.
* `Solution889.lean:25–33` repeats that union definition and gives `NsimpleOrLine_eq_library : … = Further.NsimpleOrLine … := rfl`; its headline theorem delegates to `Line889.simple_or_critical_8893`.
* `SolutionFurther.lean` repeats the actual `N0mult`, `Nsimple`, union definitions and their `rfl` identifications. `Further/Defs.lean:33–43` defines these weighted counts and identifies `N0mult` with `Zeta23.N0`.

The source README pins upstream zeta23 to `fbdc36bbf17d20af3fd0447c6d1a8a02773c9844`. I read the cached pinned dependency's `ChallengeDeps.lean:41–67` and `Zeta23/Statement.lean:38–65`. An offline static check found18 exact definition matches between the relevant Challenge files, `ChallengeDeps` and `Zeta23/Statement`, also checking the extra simple/union definitions and the renamed `N0mult`/`N0` equality. No replacement abstract zero set was found in these headline definitions. Correctness of finiteness and positive finite analytic order is a separate proof obligation: the dependency's `ZetaSeam` fields at `Statement.lean:75–83` explicitly expose those properties. This statement check does not certify the proofs of every seam field.

The Challenge files deliberately contain `sorry` placeholders: their role is to display the claim using only Mathlib. They are not themselves proof artifacts. The Solution files import the development and delegate their matching statements. This review inspected those source types and definitions but did not compile or kernel-replay their complete closure. The paper's additional computational axioms and the separate replay audits must retain their existing status.

## Scope traps and what can actually be concluded

1. The paper title's “more than83.9% distinct” and “more than67.35% simple and on the critical line” match the first and third rows. The 67.8009% corollary concerns simple zeros anywhere and cannot replace the title's critical-line qualifier.
2. `Line889` is an inclusive union. A multiple zero on the critical line contributes its **full multiplicity** to N_{s∪0}; a simple off-line zero contributes one; a multiple off-line zero contributes zero. The exact finite-count identity is N_{s∪0}=N_s+N₀−N₀ˢ. Thus the intersection is counted once, not twice. The average row instead intentionally includes the overlap in both summands.
3. A large union fraction alone implies no equally large fraction for either component separately. In hypothetical zero-count data, all off-line simple points give union100% and critical-line0%; all on-line multiple points give union100% and simple0%. These are logical count examples, not assertions about zeta zeros. Similarly the average lower bound implies that the **larger** of the two component proportions is at least that average asymptotically; it does not show both proportions are at least83.67% or select one fixed component with that lower limit.
4. The source's direct stand-alone critical-line lower bound here comes from N₀ˢ≤N₀: at least the0.673538200181… fraction lies on the line. None of the reviewed headline types states an88.93% lower bound for N₀ alone. The 88.9315% union bound equivalently bounds the multiplicity mass of zeros that are **off-line AND not simple** by at most11.0685% asymptotically.
5. All counts are zeta counts. No reviewed type is a generalized-RH or all-L-functions statement, and none is a proof of RH or simplicity of every zero.

## Reproducibility and audit status

Run `python experiments/code/839_statement_grounding_checks.py`. It performs exact source-definition comparisons, union/count identification checks, rational identities and decimal evaluation; it saves source hashes and results to `experiments/results/839_statement_grounding_checks.json`. Observed exit0. This is static evidence about what the source claims, not evidence that the complete formal proofs build.

Classification: definitions and headline scopes independently checked with no mismatch found between paper, Challenge types and Solution source. The misleading inference from the label `Line889` to “88.93% on the line” is ruled out by the actual theorem type. No author error is alleged.
