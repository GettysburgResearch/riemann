# Lean source audit of OpenAI family 003

```text
Status: EMPIRICAL source inspection; NOT_EXECUTION_EVIDENCE (no build, no comparator replay)
Scope: openai/math @ adc7f1241b42e322a6451854ab7e4b4c146bf78a, directory lean/
What was actually run: grep over lean/OAI/NumberTheory/DirichletL (2,926 .lean files); reading of the comparator challenge files and configs
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
- The Hecke and Siegel statements were not re-read here.

## Comparator configuration

`ComparatorChallenges/QuasiRiemannHypothesis.json`:

- challenge module `ComparatorChallenges.QuasiRiemannHypothesis`;
- solution module `OAI.NumberTheory.DirichletL.Nonvanishing`;
- theorem `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re`;
- `permitted_axioms`: `propext`, `Quot.sound`, `Classical.choice`.

The solution theorem is `SevenEighths.ProbeFinalAssemblyUnconditional.zeta_nonzero`, re-exported in `OAI/NumberTheory/DirichletL/Nonvanishing.lean`.

If the comparator passes, the statement is proved from Mathlib with only the three standard axioms. Every classical input (cubic theta automorphy, the quadratic large sieve, the Hecke functional equation and so on) must then be proved inside Lean, because none appears as a hypothesis in the statement.

## Trust-weakening constructs (whole-word grep over `OAI/NumberTheory/DirichletL`)

| pattern | hits |
|---|---:|
| `sorry` | 0 |
| `admit` (whole word) | 0 |
| `axiom` declarations | 0 |
| `native_decide` / `Lean.ofReduceBool` | 0 |
| `implemented_by` / `@[extern` / `unsafe` / `opaque` | 0 |
| `debug.skipKernelTC` | 0 |

## Toolchain compatibility with our formal track

| | OpenAI `lean/` | our `formal/` |
|---|---|---|
| Lean | v4.34.1 | v4.33.0-rc2 |
| Mathlib | `d13f23b723b8…` | `51e6992efd06…` |

Our formal track cannot consume the OpenAI theorem until the two are aligned, either by bumping our toolchain or by vendoring the statement as a named external hypothesis.
