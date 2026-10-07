# OpenAI family 003: formalization scope and source audit

**Audit date:** 2026-10-07. **Upstream pin:** `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a`.

## Verdict

The release contains implementation source for an **unconditional** zero-free half-plane `Re(s) > 7/8` for the standard Mathlib Riemann zeta and Dirichlet L-functions, and for its explicitly constructed family of finite-order Hecke L-functions over the Eisenstein field. The exported theorems do not take an unproved zero-density estimate, positivity conjecture, or analytic-input predicate as a hypothesis. Intermediate results expose such predicates, but the top-level assembly supplies proof terms for them.

This review inspected the exported signatures and main assembly, traced all internal imports, and scanned the implementation source. **It did not compile Lean, run Comparator, or inspect kernel-reported axiom dependencies.** Those distinctions must survive any description of the import. The correct present status is “upstream supplies a full formalization; its source closure has been imported and audited structurally; independent kernel verification remains to be run.” A successful lexical scan is not a substitute for kernel verification or for checking that a newly defined analytic object matches the intended mathematical object.

## Exact exported statements

| Claim | Implementation entry point | Scope and exclusions |
| --- | --- | --- |
| Zeta | `OAI/NumberTheory/DirichletL/Nonvanishing.lean`, theorem `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re` | For every complex `s`, `7/8 < s.re` implies `riemannZeta s ≠ 0`. The standard Mathlib function is used. Its totalized value at the pole is dealt with separately by the transfer proof; this does not claim the classical meromorphic zeta function has no pole. |
| Dirichlet | Same file, theorem `OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re` | Every positive modulus and every complex Dirichlet character, including imprimitive characters. Explicit condition `¬ (χ = 1 ∧ s = 1)` excludes the principal pole. The conclusion explicitly names `_root_.DirichletCharacter.LFunction`. |
| Hecke | `OAI/NumberTheory/DirichletL/Hecke/Nonvanishing.lean` | The constructed `HeckeFamily.Character` family, with residue-character, finite-modulus, unit-triviality and period data. The principal pole is excluded. Additional wrappers accept a residue character or a ray-class character directly. |
| Uniform real-zero gap | `OAI/NumberTheory/SiegelZeros/Conclusions/Theorem.lean`, imported by `SiegelZeros/Main.lean` | There exists one real `c > 0` such that every primitive nonprincipal real character of conductor `q ≥ 3` and every real zero `0 < β < 1` satisfy `c ≤ (1-β) log q`. Both parities are included; no explicit value of `c` is supplied. |

These are open-half-plane assertions. They do not exclude a zero exactly on `Re(s)=7/8`, do not place all zeros on `Re(s)=1/2`, and do not resolve RH or GRH. The separate real-zero-gap theorem does not exclude all real zeros throughout `(0,1)`.

The release's [scope note](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/003.md) states that the papers' later applications are not included in this formalization. Its two explicitly linked manuscripts are the September 30 `7/8` paper and the October 1 real-zero-gap paper. The October 5 manuscript presents the simpler `11/12` argument; it should not be mistaken for a withdrawal of the stronger September 30 theorem, which remains the exported Lean target.

## Why the challenge files contain `sorry`

The four files in `lean/ComparatorChallenges/` are **challenge specifications**. They intentionally put `sorry` in the target proof position. The corresponding JSON files point to different solution modules:

| Challenge JSON | Solution module |
| --- | --- |
| `QuasiRiemannHypothesis.json` | `OAI.NumberTheory.DirichletL.Nonvanishing` |
| `DirichletSevenEighths.json` | `OAI.NumberTheory.DirichletL.Nonvanishing` |
| `HeckeSevenEighths.json` | `OAI.NumberTheory.DirichletL.Hecke.Nonvanishing` |
| `SiegelZeros.json` | `OAI.NumberTheory.SiegelZeros.Main` |

All four configurations permit only `propext`, `Quot.sound`, and `Classical.choice`. All set `enable_nanoda` to `false`. This describes the configured verification target; it is not evidence that a fresh local run succeeded. The `sorry` tokens in the challenge specifications must not be reported as holes in the separate implementation source.

The relevant [Comparator README](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/README.md) instructs users to install `comparator`, `landrun`, and `lean4export`, run `lake update`, obtain the cache, and invoke Comparator on the JSON challenge.

## Main proof assembly

The zeta and Dirichlet entry file imports `Foundation` and `Detector.FinalAssemblyUnconditional`. The latter proves `detector_certified_bands`, then passes this theorem to the conditional assembly layer. Its core path is:

1. `Energy.CertifiedExistence`: proves the sequence of certified bands by induction, starting with a floor certificate and using `actual_successor`; obtains the terminal certificate.
2. `Energy.CappedAnalyticSuccessor` and `Energy.CappedRadialTransport`: provide the recursive step and transport needed to construct that certificate.
3. `Detector.FinalAssemblyCertifiedBands`: converts the certificate to positive and zero-source bounds, then inverse, marked plain, and unmarked plain moment bounds. Those give a `ChosenMomentInput`.
4. `Detector.FinalAssemblyChosenData`: chooses common parameters, bounds the high part of the probe, and constructs `HeckeCommonProbe.UniformCommonProbe`.
5. `Hecke.CommonProbe`: assumes for contradiction that the supremum `β` of the family's zero real parts exceeds `7/8`, obtains a primitive zero arbitrarily near that supremum, and uses the common probe to continue the relevant reciprocal far enough to contradict that zero.
6. `Hecke.Dirichlet`: transfers the Hecke assertion to the standard Dirichlet L-functions and to zeta.

The important quantifier order is visible in `Hecke.CommonProbe`: common positive margins are chosen before the target character. The implied constants and eventual scale thresholds may depend on that character. A result proving continuation by a target-dependent distance, with no uniform lower margin over the family, would not supply the same supremum contradiction.

The separate Siegel-zero implementation follows `Conclusions.Theorem` to `Intersection.BezoutBoundary`, where the statement `LocalIsolatedBezoutStatement ℂ` is instantiated by `localIsolatedBezout_of_actual_regular_selection ℂ`. Thus that geometric input is supplied in the exported source, rather than remaining as an argument of the final theorem.

## Complete internal-source scan

The import-graph walk began at the three solution modules listed above. At this pin, it found:

| Measure | Result |
| --- | --- |
| Internal `OAI.*` modules in the union | 3,232 |
| Source lines in the union | 556,376 |
| UTF-8 source bytes in the union | 28,073,418 |
| Unresolved internal `OAI.*` imports | 0 |
| Matches for the scanned proof-hole / escape tokens | 0 |

The word-boundary scan covered `sorry`, `admit`, `axiom`, `unsafe`, `native_decide`, `sorryAx`, `ofReduceBool`, `implemented_by`, and `extern`. A separate search found no `riemannZeta` definition or abbreviation that would shadow Mathlib's function, and no local macro/elaborator or `run_tac` declaration in this implementation closure. These are source-inspection results, not a certified theorem-dependency report.

Per-root internal import counts were 2,924 for `DirichletL.Nonvanishing`, 2,925 for `DirichletL.Hecke.Nonvanishing`, and 306 for `SiegelZeros.Main`. The graph has overlap, so these counts must not be added to obtain the union. The full path inventory and scan results are recorded in [formal-dependency-audit.json](checks/artifacts/formal-dependency-audit.json).

The non-Mathlib mathematical imports found were:

- `PrimeNumberTheoremAnd.Wiener`.
- `PrimeNumberTheoremAnd.SiegelZeros.HadamardSupport`.
- `RellichKondrachov.Analysis.FunctionalSpaces.Sobolev.Euclidean.Rellich`.

The external dependencies were not recursively audited in this pass. An actual Comparator run, with the stated permitted-axiom policy, is the appropriate next check of the compiled closure. It should be performed in a fresh build environment using the pinned package versions.

## Reproducible environment and remaining verification

The upstream toolchain is `leanprover/lean4:v4.34.1`. Relevant pins include:

- Mathlib: `d13f23b723b8a846827a245b89c10fc7d3f11612`.
- PrimeNumberTheoremAnd: `c39a751132c88b6e8080b74c74023fd95b3d8be0`.
- rellich-kondrachov: `70f85d4c1bf99c6e7d61e8be4daa6f3664d08d23`.

The upstream `lakefile.lean` installs compatibility patches during dependency resolution and after updates, including for the two external mathematical packages above. Therefore a faithful import needs **the entire upstream `lean/patches` directory**, `lakefile.lean`, `lake-manifest.json`, and `lean-toolchain`, not just the theorem files. Keeping the upstream build configuration intact also preserves its additional package requirements, even where those packages are unrelated to this particular theorem.

After installing the tools specified by the upstream Comparator README, the intended checks, run from the imported `lean/` directory, are:

```sh
lake update
lake exe cache get
lake env comparator ComparatorChallenges/QuasiRiemannHypothesis.json
lake env comparator ComparatorChallenges/DirichletSevenEighths.json
lake env comparator ComparatorChallenges/HeckeSevenEighths.json
lake env comparator ComparatorChallenges/SiegelZeros.json
```

These commands were not executed in the present environment because `lean`, `lake`, `elan`, and `comparator` are not installed. Preserve the upstream pin and any generated lockfile diff in the verification record. The upstream README advises compiling only small portions of this large library and mentions Linux memory-map limits; that is an environment note, not a mathematical qualification.

## Relation to classical analytic number theory

The September 30 introduction explicitly distinguishes a **fixed zero-free half-plane** from two earlier kinds of results. Classical zero-free regions get narrower as the conductor or height increases; zero-density estimates bound the number of zeros to the right of a line and do not, merely by being strong, exclude every zero. The paper cites Guth–Maynard for the latter comparison. Its claimed result is therefore qualitatively stronger than a further critical-line proportion or a density exponent improvement.

The main inherited ingredients are cubic metaplectic/theta theory (Kubota and Patterson), explicit cusp expansions (Dunn–Radziwill), quadratic and higher-order character large-sieve estimates (Goldmakher–Louvel, Blomer–Goldmakher–Louvel, Heath-Brown), and the classical truncated-inverse zero detector. The paper states that it uses the unconditional cusp-expansion portion of Dunn–Radziwill, **not their GRH-conditional prime asymptotic**. It also explicitly says that its separate OpenAI cubic-first-moment theorem is not an input.

The new contribution claimed in the manuscript is the compatible reflection and Poisson comparison, with completed cubic support, local Euler factors, principal residues and target-independent positive exponent margins retained throughout. The `11/12` stage uses balanced scales. The `7/8` stage changes the probe using selected-prime compensation and asymmetric scales, then separately establishes the needed inverse and plain moment bounds. It is the interaction and closure of these ingredients, rather than the use of a single classical large-sieve inequality, that would need to carry a new fixed-strip theorem.

The October 1 real-zero-gap paper uses a different mechanism: a near-one real zero forces prime-character bias, which is converted into divisibility of an interpolation determinant; a weighted-row selection and uniform interpolation theorem allow the divisibility lower bound to exceed the determinant-size upper bound. Its formal source accordingly includes considerable local algebra, intersection theory, and weighted torus-jet material. It should be retained as a distinct companion route rather than presented as the same cubic-theta argument.

These observations identify the paper's stated intellectual dependencies and its claimed additions. They are not a proof of priority, independent historical novelty, or successful mathematical validation of every analytic estimate.
