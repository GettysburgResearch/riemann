# Fidelity of the Lean `HeckeFamily.LFunction` to finite-order Hecke L-functions of Q(√−3)

```text
Status: EXPLORATORY review note (definition-fidelity reading, paper-level argument, EMPIRICAL
  float spot checks). Verdict, as a reading: the Lean family is exactly the finite-order Hecke
  L-functions of K = Q(√−3) as the Sep 30 paper defines them (ray class characters, extended
  by zero, primitive or imprimitive), with the same pole exception. Not a kernel check of any
  bridge lemma by this note, not an integration record, not a statement about RH. RH is unsolved.
Scope: the statement
    OAI.SevenEighths.HeckeFamily.LFunction_ne_zero_of_seven_eighths_lt_re :
      ∀ (χ : Character) {s : ℂ}, 7/8 < s.re → ¬(χ.residue = 1 ∧ s = 1) → LFunction χ s ≠ 0
  and the project definitions it depends on, against the Hecke clause of Thm 1.1 (thm:main) of
  the Sep 30 manuscript. Closes the definition-level question left open in
  SEP30_LEAN_CORRESPONDENCE.md §6 "Not addressed", item 6, at the level stated below.
Exact sources or dependencies (all untrusted data, read at ref
  31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6):
  [CH]  standalone/2026-10-07-openai-quasi-riemann-import/upstream/lean/ComparatorChallenges/
        HeckeSevenEighths.lean, 245 lines, SHA-256 cb5e404f...0cfc2 (full: cb5e404fa65a502c0a9006b9ad45c28914feb79e4b7b1ffcf05e4af82ed0cfc2).
        Comparator config HeckeSevenEighths.json: solution module
        OAI.NumberTheory.DirichletL.Hecke.Nonvanishing, definition_names = [].
  [SOL] solution-side bridge files under upstream/lean/OAI/NumberTheory/DirichletL/:
        Hecke/Family.lean (9871d175...), Hecke/IdealBridge.lean (6c1fc33b...),
        Hecke/RayFamily.lean (86c80381...), Hecke/Nonvanishing.lean (9e120752...),
        Hecke/Theta.lean, Hecke/FamilySeries.lean, Hecke/CharacterAnalytic.lean,
        RayOrthogonality.lean, IdealCharacter.lean. All are in the import closure of the
        solution module (checked here with a stdlib import walk: 2,925 OAI modules).
  [ML]  Mathlib d13f23b7 (read-only scratch copy): NumberTheory/LSeries/AbstractFuncEq.lean
        (WeakFEPair, f_modif, Λ₀, Λ, hasMellin, differentiableAt_Λ),
        NumberTheory/LSeries/HurwitzZetaEven.lean (evenKernel, cosKernel,
        hurwitzEvenFEPair), NumberTheory/MulChar/Basic.lean (MulChar, `1 = trivial`).
  [P]   upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
        SHA-256 42a5ee0f...6a3; lines 36-42 (abstract), 50-63 (definition of finite-order
        Hecke character and L_F), 106-111 (thm:main), 373-377 (reduction to primitive),
        568-590 (O = Z[ω], units), 1437-1438 (trivial infinite type).
  Build facts quoted, not re-run: LEAN_BUILD_ATTEMPT.md Addendum C (Hecke module built,
        `#print axioms` = [propext, Classical.choice, Quot.sound], results/lean_hecke_axioms.log).
What was actually run (no Lean, Lake or comparator process was started):
  - Line-by-line reading of [CH], the bridge statements in [SOL], and the cited Mathlib
    definitions in [ML].
  - reviews/hecke_lean_fidelity.py (SHA-256 1c76434a...4d6a), `python3 -I`, single thread,
    6.9 s. Outputs results/hecke_lean_fidelity.json (07fd7c51...4e712) and
    results/hecke_lean_fidelity_stdout.txt (3a8a3998...a6222). EMPIRICAL, IEEE doubles plus
    mpmath at 15 digits. It re-implements the challenge definitions by hand; it checks this
    reading, not the Lean term.
Smallest remaining gap: Mathlib has no Hecke character or Hecke L-function, so no formal
  statement ties `LFunction χ` to an externally defined object. The identification rests on
  (a) the paper-level argument in §2-§3 below, (b) the solution's bridge lemmas
  (`LFunction_eq_ideal_tsum`, `LFunction_differentiableAt`, `LFunction_entire_nonprincipal`,
  `HeckeRayFamily.character`, `principal_iff`), which were compiled in the 0-error, 0-sorry
  build but are not comparator targets and had no `#print axioms` run of their own, and
  (c) the textbook step "finite-order idelic Hecke character = ray class character" (not
  formalized anywhere here).
```

RH is unsolved. The Lean theorem is a statement about `Re s > 7/8`. Nothing in this note bears on the critical line.

## 0. Verdict

Labels: READING (what the Lean text says), PAPER-LEVEL (an argument at the level of a written proof, by this reviewer), EMPIRICAL (float computation).

* **READING + PAPER-LEVEL.** For every `χ : Character`, `LFunction χ` agrees on `Re s > 1` with Σ over nonzero ideals 𝔞 of ψ(𝔞) N𝔞^(−s). Here ψ is the ray class character mod 𝔪 = `χ.modulus` attached to `χ.residue`, extended by zero to ideals not coprime to 𝔪. `LFunction χ` is holomorphic on `Re s > 0` except for a simple pole at s = 1 when `χ.residue = 1`. It is entire when `χ.residue ≠ 1`. So on the region `{Re s > 7/8} \ {1}` it is the analytic continuation of that L-function. When `χ.residue ≠ 1`, this holds at s = 1 as well.
* **PAPER-LEVEL.** Every finite-order Hecke character of K = Q(√−3) has trivial infinity type, so it is a ray class character. Every ray class character mod 𝔪 arises from some `Character` with modulus 𝔪. Conversely, every `Character` gives a finite-order ray class character.
* **Conclusion.** The Lean statement says the same thing as the Hecke clause of Thm 1.1: L(s, ψ) ≠ 0 for Re s > 7/8, for every finite-order Hecke character ψ of Q(√−3), with only the principal pole at s = 1 allowed. It is not narrower. It is not broader in any mathematical sense. The `period` field and the choice of an imprimitive modulus only change the representation:
  * the extra Euler factors 1 − ψ(𝔭)N𝔭^(−s) of an imprimitive modulus do not vanish for Re s > 0;
  * the paper's own definition (l. 52-54) also admits imprimitive moduli.
* Characters of infinite order are not covered. This includes Größencharaktere with infinity type (z/|z|)^k, k ≠ 0. The paper does not claim them either. Twists by |N𝔞|^(it) are covered trivially, because the half-plane is invariant under vertical shifts.

## 1. What the challenge file defines (READING, [CH] l. 206-239 unless stated)

**Field and ring.** `K = CyclotomicField 3 ℚ`, `O` = its ring of integers. `omega` = the integral element of a primitive cube root of unity. `coordinateElement x y = x + y·ω` for x, y ∈ ℤ. No complex embedding is fixed. None is needed, because both embeddings give the same norm form x² − xy + y². The solution proves `{1, ω}` is a ℤ-basis (`coordinateEquiv : ℤ × ℤ ≃ O`) and that `normForm x y = x² − xy + y²` equals `Ideal.absNorm (span {x + yω})` (`normForm_eq_absNorm_span`, IdealBridge l. 26-38).

**`Character` (l. 217-224).** Fields:

| field | meaning |
|---|---|
| `modulus : Ideal O`, `modulus_ne_bot` | a nonzero integral ideal 𝔪 (𝔪 = ⊤ = (1) allowed) |
| `residue : MulChar (O ⧸ 𝔪) ℂ` | a Mathlib multiplicative character of the finite ring O/𝔪: a monoid hom O/𝔪 → ℂ that is **0 on non-units** (`map_nonunit'`, [ML] MulChar/Basic l. 72-73). Equivalently, a character of (O/𝔪)^× extended by zero |
| `unit_trivial` | `residue (u mod 𝔪) = 1` for all six units u ∈ O^× = μ₆ |
| `period : ℕ`, `period_pos`, `period_mem` | a positive integer N with N ∈ 𝔪. It makes `residue(x + yω mod 𝔪)` depend only on (x mod N, y mod N). It is bookkeeping only: `Character.ofResidue` uses N = \|O/𝔪\|, and `continuedLattice_eq_of_elementCoeff_eq` (FamilySeries l. 57) shows the value does not depend on it for Re s > 0, s ≠ 1 |

`residue = 1` means `residue = MulChar.trivial`, the principal character mod 𝔪 (1 on units, 0 elsewhere). If 𝔪 = ⊤, then O/𝔪 is the zero ring. Its only MulChar is the constant 1, which equals `trivial`, and the Character gives ζ_K.

**Coefficients (l. 228-231).** `elementCoeff χ z = residue(z mod 𝔪)`. `coefficients χ (a, b) = elementCoeff χ (a + bω)` for (a, b) ∈ Fin N × Fin N, with representatives in [0, N).

**Theta assembly (l. 91-202).** `hurwitzEvenFEPair α` is the Mathlib pair:
* f = evenKernel α, where evenKernel α x = Σ_n exp(−π(n+α)²x);
* g = cosKernel α, where cosKernel α x = Σ_n cos(2πnα) exp(−πn²x);
* k = 1/2, ε = 1, f₀ = [α = 0], g₀ = 1.

The file then builds the following.
* `rescale P u`: f(x) = P.f(ux), g(x) = P.g(x/u), ε = P.ε·u^(−1/2).
* `product`: multiplies f's, g's, ε's, f₀'s and g₀'s, and adds the k's.
* `rectangularPair α β u v` = product of the two rescaled even pairs, with k = 1.
* `parityPair a b L e` (e ∈ {0, 1}) = `rectangularPair` with α = (2a − b − Le)/(2L), β = (b + Le)/(2L), u = L², v = 3L².
* `finitePair P w`: f = Σ w_i f_i, g = Σ w_i ε_i g_i, k = 1, ε = 1, f₀ = Σ w_i f₀_i, g₀ = Σ w_i ε_i g₀_i.
* `pair w` sums `parityPair a b N e` over ((a, b), e) ∈ (Fin N)² × Fin 2, with weight w(a, b).
* `completed w = (pair w).Λ`, using Mathlib's Λ(s) = Λ₀(s) − f₀/s − ε g₀/(k − s), where Λ₀ = Mellin transform of f_modif ([ML] AbstractFuncEq l. 249-252, 378-381).
* `latticeL w s = π^s Γ(s)^(−1) completed w s`.
* `continuedLattice χ = latticeL (coefficients χ)` and `LFunction χ s = continuedLattice χ s / 6`.

**The parity trick (PAPER-LEVEL, also checked exactly).** Put x = a + N(n + m) and y = b + N(2m + e), for n, m ∈ ℤ and e ∈ {0, 1}. Then N²(n + α)² + 3N²(m + β)² = x² − xy + y². As (n, m, e) ranges, (x, y) runs over the residue class (a, b) mod N exactly once, because 2m + e runs over ℤ exactly once. So

  (pair w).f(t) = Σ_{(x,y) ∈ ℤ²} w(x mod N, y mod N) · exp(−π t (x² − xy + y²)),

which is the solution's `theta_eq_pair` (Theta l. 112). Exactly one of the 2N² pieces has α, β ∈ ℤ, namely ((0, 0), 0). Hence f₀ = w(0, 0) (solution: `pair_f₀`, Theta l. 116). Check P of the script verifies all of this with exact rationals for N = 1..6: the norm identity, single coverage of a box, and exactly one f₀ cell.

**Why divide by 6.** O^× = μ₆ has order 6, and K has class number 1. Each nonzero ideal therefore has exactly six generators. By `unit_trivial`, all six give the same term. The element sum is 6 times the ideal sum (`continuedLattice_eq_six_ideal_tsum`, IdealBridge l. 80).

## 2. The Dirichlet series for Re s > 1 (PAPER-LEVEL; matches solution lemmas)

For Re s > k = 1, Mathlib's `WeakFEPair.hasMellin` gives Λ(s) = ∫₀^∞ (f(t) − f₀) t^(s−1) dt. Integrating term by term (absolute convergence for Re s > 1) gives:

  Λ(s) = π^(−s) Γ(s) Σ_{z ∈ O∖0} χ(z) N(z)^(−s),
  LFunction χ s = (1/6) Σ_{z ≠ 0} χ(z) N(z)^(−s) = Σ_{𝔞 ≠ 0} ψ(𝔞) N𝔞^(−s),

where ψ((z)) := residue(z mod 𝔪). ψ is well defined because of `unit_trivial`, and it is defined on all ideals because O is a PID. It vanishes exactly on ideals not coprime to 𝔪, by MulChar's `map_nonunit`. It is completely multiplicative on ideals. The solution states this as `LFunction_eq_ideal_tsum` (IdealBridge l. 97), with `idealCoeff = IdealCharacter.ofResidue`, a `Ideal O →*₀ ℂ`.

**Does the construction force χ trivial on units, or does it silently give 0?** It forces it: `unit_trivial` is a field of the structure. Without that field the construction would silently give 0. If residue(u) ≠ 1 for some unit u, then substituting z ↦ uz shows the element sum equals residue(u) times itself, so it vanishes identically. `LFunction` would then be the zero function and the theorem would be false. The negative control NC in §5 (the cubic residue symbol mod 3 + ω: even, but residue(ω) ≠ 1) returns |sum| ≈ 4·10⁻¹⁶. So the field is load-bearing, and it is exactly the condition for ψ to be well defined on principal ideals.

**Continuation.** `LFunction_differentiableAt` holds for s ≠ 0 with (s ≠ 1 or residue ≠ 1), and `LFunction_entire_nonprincipal` (IdealBridge l. 102-113) holds as well. At paper level this comes from two facts:
* Λ₀ is entire, and 1/Γ is entire with no zeros in Re s > 0.
* The pole terms are f₀/s and g₀/(1 − s). Here f₀ = w(0,0) = residue(0), which is 0 unless 𝔪 = ⊤. And g₀ = (2/(√3 N²)) Σ_{(a,b)} w(a, b) (each ε_i = (N²·3N²)^(−1/2)). The map (ℤ/N)² ≅ O/NO → O/𝔪 has equal fibres, so this sum is a multiple of Σ_{r ∈ O/𝔪} residue(r), which is 0 for a non-principal MulChar.

Since {Re s > 7/8} ∖ {1} is connected and contains Re s > 1, `LFunction χ` is there the unique analytic continuation of the Dirichlet series. One cross-check of normalisation: for the trivial character (N = 1), g₀ = 2/√3. The Lean residue at s = 1 is then π g₀ / 6 = π/(3√3). This equals the class-number-formula residue 2πhR/(w√|d|) = 2π/(6√3) for h = R = 1, w = 6, d = −3.

**Junk value.** For principal χ at s = 1, Lean's Λ formula divides by k − s = 0, which Lean sets to 0, so `LFunction χ 1` is a finite junk value. The hypothesis `¬(residue = 1 ∧ s = 1)` excludes exactly this point. For non-principal χ, s = 1 is included, and it is the true value L(1, ψ).

## 3. Which Hecke characters (PAPER-LEVEL)

**Finite order forces trivial infinity type.** Let ψ: 𝔸_K^×/K^× → ℂ^× be continuous with ψⁿ = 1. Its infinity component ψ_∞ = ψ|_{K_∞^×} is a continuous map from K_∞^× = ℂ^× into the finite set μ_n. Since ℂ^× is connected, ψ_∞ is constant, so ψ_∞ = 1. Continuity at the finite places then makes ψ trivial on some U_𝔪 = Π_𝔭 (1 + 𝔭^{e_𝔭}O_𝔭). So ψ factors through the ray class group Cl_𝔪. The paper gives the same argument (l. 55-56, 1437; Milne CFT VI.1).

*Correction to the argument as phrased in the task.* "The infinity type must be of finite order and the units are finite" is not the reason:
* Finite order alone does not kill ψ_∞ at a real place: ℝ^× is disconnected, and sign characters survive. That is why narrow ray class characters exist over real fields.
* At a complex place, the reason is connectedness.
* The finiteness of O^× works the other way. It is why an imaginary quadratic field has many Hecke characters with nontrivial infinity type (z/|z|)^k: the compatibility condition only involves the finite group μ₆. Those characters all have infinite order, because their values on (α) with α ≡ 1 mod 𝔪 are (α/|α|)^k, which are dense in the circle when k ≠ 0.

The conclusion of the task's argument is correct.

**Ray class characters versus `Character`.** Since h_K = 1, the sequence O^× → (O/𝔪)^× → Cl_𝔪 → Cl_K = 1 gives Cl_𝔪 ≅ (O/𝔪)^× / im(μ₆). So the characters of Cl_𝔪 are exactly the characters of (O/𝔪)^× that are trivial on the image of the units. Extended by zero, these are exactly the MulChars on O/𝔪 satisfying `unit_trivial`. Given ψ with conductor 𝔣 (or any multiple 𝔪), take modulus 𝔪 and period N = N𝔪 ∈ 𝔪. This is `Character.ofResidue`. The resulting `LFunction` is L_𝔪(s, ψ), which equals L(s, ψ) when 𝔪 = 𝔣. The solution packages this direction as `HeckeRayFamily.character` on `RayOrthogonality.rayCharacters 𝔪`. That type is the group of MulChars on O/𝔪 trivial on the image of the global units, with `principal_iff`. Hecke/Nonvanishing.lean also states a copy of the 7/8 theorem indexed by it (`HeckeRayFamily.LFunction_ne_zero_of_seven_eighths_lt_re`). Conversely, any `Character` takes root-of-unity values on units, so it is a finite-order ray class character mod 𝔪, extended by zero.

**Imprimitive moduli.** L_𝔪(s, ψ) = L(s, ψ_prim) · Π_{𝔭 | 𝔪, 𝔭 ∤ 𝔣} (1 − ψ_prim(𝔭) N𝔭^(−s)). The extra factors have no zeros in Re s > 0. So zero-freeness for all `Character`s is equivalent to zero-freeness for primitive ones, as the paper itself notes (l. 373-377). The principal character mod 𝔪 gives ζ_K(s) Π_{𝔭|𝔪}(1 − N𝔭^(−s)). Its only pole is at s = 1, and the hypothesis `hpole` removes exactly that point.

## 4. Edge cases (READING + PAPER-LEVEL)

| case | what Lean gives | matches the paper? |
|---|---|---|
| 𝔪 = ⊤, residue = 1 | ζ_K(s) = ζ(s) L(s, χ₋₃). f₀ = 1, g₀ = 2/√3. Poles of Λ only at s = 0, 1; 1/Γ(0) cancels the one at 0 | yes; s = 1 excluded |
| principal mod 𝔪 ≠ ⊤ | ζ_K times finitely many nonvanishing Euler factors. f₀ = 0 | yes |
| non-principal, any 𝔪 | Σ w = 0 ⇒ g₀ = 0, and f₀ = 0 ⇒ entire | yes, including s = 1 |
| imprimitive 𝔪 | L_𝔪 = L_prim × factors with no zeros for Re s > 0 | yes (same zero set in Re s > 7/8) |
| residue nontrivial on units | excluded by the type. Would give LFunction ≡ 0 | not a Hecke character on ideals; correctly excluded |
| `period` not minimal | same value (FamilySeries l. 57) | bookkeeping only |

## 5. Numerical sanity check (EMPIRICAL, floats)

The script `hecke_lean_fidelity.py` computes each value three ways:
* **M1:** the Lean construction re-implemented literally: the 2N² parity pieces with Lean's shifts, scalings and ε's; Λ = Λ₀ − f₀/s − g₀/(1 − s), with Λ₀ = ∫₁^∞ (F − f₀) t^(s−1) dt + ∫₁^∞ (G − g₀) u^(−s) du (the (0, 1) part of f_modif rewritten through the pair's functional equation) by quadrature; then π^s/Γ(s)·Λ/6.
* **M2:** a direct element sum Σ_{0 < N(z) ≤ X} w(z) N(z)^(−s)/6, plus a tail correction (mean weight × 2π/√3 × X^(1−s)/(s − 1)).
* **M3:** independent values:
  * an Euler product over prime ideals of Z[ω] up to p ≤ 2·10⁵ (split primes found by a Euclidean gcd);
  * for principal and base-change characters, mpmath ζ and Dirichlet L-values: L(χ_D∘N, s) = L(s, χ_D) L(s, χ_D χ₋₃).

The script also checked:
* the MulChar axioms on O/NO for every test character: 0 multiplicativity failures, 0 mismatches between "zero" and "non-unit mod 𝔪";
* unit triviality;
* Lean's functional equation F(t) = t⁻¹ G(1/t) at two points: relative error ≤ 2.6·10⁻¹⁵.

Values at s = 2 (M1 value; absolute differences from the others):

| character | N | Σw | M1 at s = 2 | \|M1−M2\| | \|M1−Euler\| | \|M1−mpmath\| |
|---|---|---|---|---|---|---|
| A trivial, 𝔪 = (1): ζ_K | 1 | 1 | 1.285190955484 | 6.6e-12 | 4.9e-7 * | 2.0e-15 |
| B principal mod (2) | 2 | 3 | 1.204866520766 | 6.8e-12 | 4.6e-7 * | 2.2e-16 |
| C χ₋₄∘N mod (4) | 4 | 0 | 0.869895388368 | 9.0e-12 | 4.2e-10 | 1.1e-16 |
| D (·/5)∘N mod (5) | 5 | 0 | 0.915686838621 | 1.8e-11 | 1.3e-10 | 1.1e-16 |
| E quadratic mod (4+ω), N𝔭 = 13 (not Galois-invariant) | 13 | 0 | 0.841385544202 | 1.4e-11 | 9.4e-11 | — |
| F cubic residue mod (5+2ω), N𝔭 = 19 ≡ 1 mod 9 | 19 | 0 | 0.897454431175 − 0.037752414911 i | 6.0e-11 | 3.7e-10 | — |
| NC cubic mod (3+ω), N𝔭 = 7, **not** unit-trivial | 7 | 0 | \|M1\| = 3.8e-16 | \|M2\| = 1.4e-16 | Euler on chosen generators 0.912 (ill-defined) | — |

\* This is the Euler-product truncation at p ≤ 2·10⁵. Its expected size is about 1/(P log P). The other columns agree to ~1e-11.

Inside and near the strip, for A-D, M1 agrees with the mpmath values at s = 1.5, 0.9, 0.95 + 3i and 0.876 + 6i. The maximum difference is 3.1·10⁻¹³. This checks the continuation mechanism (f_modif, the f₀/s and g₀/(1 − s) terms, and the 1/Γ factor) as read here. M1 values for E and F at these points are recorded in the JSON, but there is no independent value to compare them with.

These are float computations at a handful of points. They confirm that the reading of the definitions in §1-§2 is internally consistent and gives the expected L-functions. They do not evaluate the Lean term, and they say nothing about zeros.

## 6. Conclusion

* **Statement match.** `HeckeFamily.LFunction_ne_zero_of_seven_eighths_lt_re` says: for every nonzero ideal 𝔪 of Z[ω] and every character of the ray class group mod 𝔪, the L-function L_𝔪(s, ψ) (ψ extended by zero at primes dividing 𝔪) has no zero in Re s > 7/8, except that the principal character may have its pole at s = 1. By §3 this is the same as "L(s, ψ) ≠ 0 for Re s > 7/8 for every finite-order Hecke character ψ of Q(√−3), with the principal pole allowed", which is the Hecke clause of Thm 1.1 (l. 106-111, with the definition at l. 50-63).
* **Neither narrower nor broader.** It is not narrower: every finite-order Hecke character is represented, by §3. It is not broader: every `Character` is such a character, and imprimitive moduli and the `period` field add no new L-functions up to factors with no zeros in Re s > 0.
* **Not covered.** Hecke characters of infinite order with nontrivial infinity type are not covered, and the paper does not claim them.
* **Trust.** The formal content is what comparator and `#print axioms` certify for that statement, under the trust assumptions recorded in LEAN_BUILD_ATTEMPT.md. This note adds only the definition-level identification, at the evidence levels labelled above. It changes nothing about the manuscript's own verification status. RH remains unsolved.

## 7. Known misreadings to avoid

* "The Hecke theorem is stated with Mathlib's Hecke L-functions." Mathlib has none. `Character` and `LFunction` are project definitions inside the challenge file. This note checks that they mean what the paper means.
* "`unit_trivial` restricts the family." It does not. It is exactly the condition for a residue character to define a function on ideals. Without it, the Lean `LFunction` would be identically zero.
* "Finite-order characters of an imaginary quadratic field can have nontrivial infinity type." They cannot, because ℂ^× is connected. The finiteness of the unit group is not the reason.
* "The numerics verify the Lean term." They verify a hand re-implementation of the definitions, at a few points, in floating point.
