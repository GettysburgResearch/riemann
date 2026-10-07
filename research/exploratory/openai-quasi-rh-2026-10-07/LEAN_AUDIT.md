# Lean source audit of OpenAI family 003

```text
Status: EMPIRICAL source inspection; NOT_EXECUTION_EVIDENCE (no build, no comparator replay)
Scope: openai/math @ adc7f1241b42e322a6451854ab7e4b4c146bf78a, directory lean/
What was actually run: grep over the import closure of the solution modules (3,232 files); reading of the challenge files and configs;
  elan + Lean v4.34.1 + Mathlib d13f23b cache: all four challenge files compile (expected `sorry` warnings only);
  partial build of the Siegel closure (161/306 OAI modules and 7/12 patched PNT+ modules compiled with no errors before it was stopped).
  The 7/8 closure (2,925 files, about 486.5k lines) was NOT built.
Smallest remaining gap: `lake build` plus `lake env comparator ComparatorChallenges/{QuasiRiemannHypothesis,DirichletSevenEighths,HeckeSevenEighths,SiegelZeros}.json` on independent hardware, with the axiom report recorded
```

As in the earlier external-work reviews (AS-026), formal metadata is not execution evidence. Everything below was read from source, not checked by a kernel.

## Statements (verbatim from the challenge files)

```lean
-- ComparatorChallenges/QuasiRiemannHypothesis.lean
theorem riemannZeta_ne_zero_of_seven_eighths_lt_re
    {s : ℂ} (hs : (7 / 8 : ℝ) < s.re) : riemannZeta s ≠ 0

-- ComparatorChallenges/DirichletSevenEighths.lean
theorem LFunction_ne_zero_of_seven_eighths_lt_re
    {q : ℕ} [NeZero q] (χ : DirichletCharacter ℂ q) {s : ℂ}
    (hs : (7 / 8 : ℝ) < s.re) (hpole : ¬ (χ = 1 ∧ s = 1)) :
    _root_.DirichletCharacter.LFunction χ s ≠ 0
```

- Both statements use Mathlib's own `riemannZeta` and `DirichletCharacter.LFunction`. Neither carries any analytic hypothesis.
- Mathlib's `riemannZeta 1` is a junk value, nonzero, so the zeta statement is harmless at $s=1$.
- **Hecke** (`HeckeSevenEighths.lean:237-239`): `theorem LFunction_ne_zero_of_seven_eighths_lt_re (χ : Character) {s : ℂ} (hs : (7 / 8 : ℝ) < s.re) (hpole : ¬ (χ.residue = 1 ∧ s = 1)) : LFunction χ s ≠ 0`.
- **Siegel** (`SiegelZeros.lean:8-14`): `∃ c : ℝ, 0 < c ∧ ∀ (q : ℕ) [NeZero q], 3 ≤ q → ∀ χ : DirichletCharacter ℂ q, χ.IsPrimitive → χ ≠ 1 → (∀ a : ZMod q, (χ a).im = 0) → ∀ β : ℝ, 0 < β → β < 1 → χ.LFunction (β : ℂ) = 0 → c ≤ (1 - β) * Real.log (q : ℝ)`.
  - This follows trivially from the Dirichlet 7/8 theorem with $c=\log 3/8$.
  - Its Lean proof (`OAI/NumberTheory/SiegelZeros`, 306 files) is independent and does not use the 7/8 theorem.

**The Hecke L-function is defined in the challenge file, not taken from Mathlib.** The definition lives in lines 11-235 of the challenge file:

- $K$ = `CyclotomicField 3 ℚ`.
- A `Character` is a `MulChar` on $\mathcal O/\mathfrak m$ that is trivial on units. Since $K$ has class number 1, these are exactly the finite-order ray-class characters, in imprimitive form.
- `LFunction` is $\tfrac16$ of a continued lattice sum. It is built from rescaled Mathlib `hurwitzEvenFEPair`s; the reparametrisation uses $x^2-xy+y^2=N(x+y\omega)$.

A hand check gives $\tfrac16\sum_{z\ne0}\chi(z)N(z)^{-s}=\sum_{\mathfrak a}\chi(\mathfrak a)N\mathfrak a^{-s}$ for $\Re s>1$, which is the standard object. The repository proves this identity in `Hecke/IdealBridge.lean:97` (`LFunction_eq_ideal_tsum`). It also proves the factorization $L_K(s,\chi\circ N)=L(s,\chi)L(s,\chi\chi_{-3})$ in `Hecke/Dirichlet.lean:128`.

## Comparator configuration

`ComparatorChallenges/QuasiRiemannHypothesis.json`:

- challenge module `ComparatorChallenges.QuasiRiemannHypothesis`;
- solution module `OAI.NumberTheory.DirichletL.Nonvanishing`;
- theorem `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re`;
- `permitted_axioms`: `propext`, `Quot.sound`, `Classical.choice`.

The solution theorem is `SevenEighths.ProbeFinalAssemblyUnconditional.zeta_nonzero`, re-exported in `OAI/NumberTheory/DirichletL/Nonvanishing.lean`.

If the comparator passes, the statement is proved from Mathlib with only the three standard axioms. Every classical input (cubic theta automorphy, the quadratic large sieve, the Hecke functional equation and so on) must then be proved inside Lean, because none appears as a hypothesis in the statement.

## Trust-weakening constructs (whole-word grep over the import closure)

| pattern | hits |
|---|---:|
| `sorry` | 0 |
| `admit` (whole word) | 0 |
| `axiom` declarations | 0 |
| `native_decide` / `Lean.ofReduceBool` | 0 |
| `implemented_by` / `@[extern` / `unsafe` / `opaque` | 0 |
| `debug.skipKernelTC` | 0 |
| `csimp`, `sorryAx`, `set_option`, `macro`, `elab`, `run_cmd`, `#eval`, `partial` | 0 |

- **Closure sizes:**
  - 7/8 results: 2,925 files, about 486.5k lines, all under `OAI/NumberTheory/DirichletL`. Outside dependencies: `PrimeNumberTheoremAnd.Wiener` and Rellich–Kondrachov.
  - Siegel: 306 files, 69.8k lines, plus 12 PNT+ files that exist only through a patch.
- **No hypothesis-style classes.** There are no `class` declarations. Hypothesis-shaped `Prop`s, such as `DetectorCertifiedBands`, are discharged by theorems (`detector_certified_bands`), and the final theorems take no extra hypotheses.
- **Dependency patching.** `lakefile.lean` applies `git apply` patches to 23 third-party dependencies (not Mathlib) during `lake update`.
  - The patched PNT+ (c39a751) files and Rellich–Kondrachov (70f85d4) files used contain no `sorry` or `axiom`.
  - The patch deletes upstream's two `sorry`'d Wiener lemmas.
  - A full replay should audit these patches.
- **Classical inputs located as proved theorems.**
  - Kubota character on the level-3 subgroup: `CubicSieve/RayCoefficients.lean:567-614`.
  - Cubic reciprocity: `GaussSum/SquarePhaseFactorization.lean:274`.
  - The cubic theta function, as the residue at $s=4/3$ of the Kubota Eisenstein series: `Eisenstein/ScatteringCoefficients.lean:83`. Its automorphy and eigenvalue $8/9$ are proved.
  - Quadratic large sieve over $\mathbb Z[\omega]$: `QuadraticSieve/LogarithmicLoss.lean:479`.
  - Cubic large sieve: `CubicSieve/Sharp.lean:8`.
  - Poisson summation and the Hecke functional equation come from Mathlib.
  - Ray-class prime counting: via PNT+ Wiener–Ikehara.
  - An explicit Patterson theta-coefficient theorem was not located in the time spent.
- **No separate 11/12 theorem.** The Lean proof goes straight to 7/8.
- **Comparator settings.** `definition_names` is empty in all four configs, and `enable_nanoda` is false, so no second kernel is used.
- **Elsewhere in `lean/`, outside 003:** `ComparatorChallenges/HarmonicGrowth.lean:100` declares an `axiom` in a challenge file, and other families use `opaque` and `@[csimp]`. None of these is in the 003 closure.

## Toolchain compatibility with our formal track

| | OpenAI `lean/` | our `formal/` |
|---|---|---|
| Lean | v4.34.1 | v4.33.0-rc2 |
| Mathlib | `d13f23b723b8…` | `51e6992efd06…` |

Our formal track cannot consume the OpenAI theorem until the two are aligned, either by bumping our toolchain or by vendoring the statement as a named external hypothesis.
