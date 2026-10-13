# O5 — wild ideas: 18 mechanisms, triaged

```text
Status: EXPLORATORY triage. Labels per item: PROVED-HERE (elementary, unreviewed), PROPOSED,
  CONDITIONAL, HEURISTIC, EMPIRICAL (finite numerics, binary64 or exact integers), OPEN.
  RH is unsolved. No zero-free region is proved here. Sep 30 (7/8) and Oct 5 (11/12) are external,
  unreviewed manuscripts; anything resting on them is IMPORTED/CONDITIONAL. The 7/8 Lean statements are
  comparator-accepted under the trust assumptions of reviews/LEAN_BUILD_ATTEMPT.md.
Scope: new mechanisms that might move a quasi-RH exponent below 11/12 (Oct 5 architecture) or 7/8, or
  give RH-adjacent consequences. Routes reserved for O1-O4 and O6 are not duplicated.
Exact sources or dependencies: ../../SYNTHESIS.md, ../../RUNG_STRENGTH.md, ../../LEVERAGE_FAMILIES.md,
  ../../DISPERSION_GRH_STEP.md, ../../DETECTOR_DENSITY.md, ../../moments/DUAL_ANATOMY.md,
  ../../CONDITIONAL_CONSEQUENCES.md, ../../ZERO_DENSITY_CONDITIONAL.md, ../../reviews/HECKE_LEAN_FIDELITY.md;
  Oct 5 paper2.tex Secs. 1-2 (session scratchpad copy of the PR 908 import).
What was actually run:
  python3 -I triage_exponents.py   (sympy, exact rationals, ~2 s; all asserts pass) -> triage_exponents.out
  python3 -I galois_cubic_checks.py (exact Z[omega] symbols + the moments/ C kernel, ~1 min)
    -> galois_cubic_checks.json
  python3 -I kappa_window.py (moments/ C kernel, binary64, ~1 min) -> kappa_window.json
Smallest remaining gap: a coefficient-specific bound at ONE sub-diagonal row range,
  sum_{N u <= D^(1-eta)} |A_u(D)|^2 << D^(2-(1-kappa) eta) with kappa < 5/6 (the kappa-law,
  ROW_REWEIGHTING_CLOSURE.md Sec. 3); it would give 11/12 - eta (5/6 - kappa)/2.
```

## Bottom line

* **No mechanism found here moves an exponent below 11/12 (Oct 5 architecture) or below 7/8.**
  Of the 18 mechanisms, 14 are DEAD, each with an exact killing term. 3 are ALIVE as conditional
  corollaries or as a target, and 1 is OPEN (Weil positivity).
* **Best positive outputs:**
  1. *Kummer-field corollaries* (CONDITIONAL on HECKE-7/8, PROPOSED proofs).
     * `ζ_F ≠ 0` on `Re s > 7/8` for every field `F` contained in an abelian extension of
       `Q(√−3)`. This includes pure cubic fields, `Q(m^{1/6})` and ring class fields.
     * The least prime `p ≡ 1 (3)` with `m` a cubic non-residue is `≪ (log m)^{8+ε}`, effectively.
  2. *The κ-law* and *Prop. L*.
     * The κ-law is a minimal sufficient target, strictly weaker than Mom(1, ρ):
       `σ = 11/12 − η(5/6 − κ)/2`.
     * New (PROPOSED, conditional on Oct 5 as stated): lifting rows by `p⁶` already *proves* the
       sub-diagonal bound `Σ_{N u ≤ D^{1−η}} |A_u|² ≪ D^{2−η/6+ε}`, i.e. `κ = 5/6`, for every
       `η < 6/11` (every `η < 1` under the all-`H` form of Oct 5).
     * So the whole gap below 11/12 is the step from `κ = 5/6` to any `κ < 5/6` at a single `η`.
       Lifting is a fixed point and cannot make that step.
     * Numerically `κ̂ ∈ [−0.09, −0.02]` on single windows (`D ≤ 32000`), with μ inside the
       random-sign spread.
  3. *A closure theorem* (Prop. W). No positive combination of Oct 5-type inputs over row ranges,
     scales, heights, angular twists, Mellin kernels or multiplicity-weighted density beats
     `min(σ₀, 11/12)`.
* **A structural coincidence (exact).** Counted with multiplicity, the Sep 30 inner-detector density
  `f(σ) = (31−32σ)/(21−12σ)` crosses the leverage threshold `1/6` exactly at `σ = 11/12`.

## Triage table

| # | mechanism (seed) | best exponent / test outcome | verdict | killing term or what is missing |
|---|---|---|---|---|
| 1 | Galois symmetry `μ(n̄)=μ(n)` → positivity (seed 1) | `A_ū = conj A_u` (dev 1.3e-14); μ_K on rational columns is `χ₋₃·μ²` | DEAD | rational columns erase the Möbius sign; the Galois piece is positive and carried by random `f(π)=f(π̄)` (DUAL_ANATOMY) |
| 2 | 7/8 as pointwise input to the Oct 5 bootstrap (seed 2b) | `σ₁ = (σ₀(k−1)+11/12)/k`; at `σ₀=7/8`: `7/8 + 1/(24k)` | DEAD | fixed point 11/12 > 7/8; zero-density version gives `7/8 + ρ/24` |
| 3 | 7/8 for Kummer Hecke L-functions (seed 2a) | already a special case; corollaries K1, K2 | ALIVE (corollary) | moves no exponent; Hecke characters of `K(u^{1/6})` not induced from `K` are OPEN |
| 4 | multi-scale / hybrid `u×D`, `u×t` families (seed 3) | `1 − h/12 ≥ 11/12` on `h+τ=1`; coherence gain `J² = D^{o(1)}` | DEAD | `t`-rows have no principal copies; `≪ D^ε` independent scales |
| 5 | sieve weights `λ_d` in place of μ (seed 4) | general-coefficient sieve gives `2σ ≥ 2` (trivial) at every `h` | DEAD | over all rows, Δ ≥ `H^{1/6}N` (principal class, b ≡ 1); absorption needs `μ(p) = −1` (S7: drop μ → fails by 2); Selberg `μ·P(log)` is just another `W` |
| 6 | Deuring–Heilbronn inside the family (seed 5) | repulsion `1−β₁ ≥ c Q^{−C(1−β)}` | DEAD | vacuous when `1−β₁ ≍ 1`; log-scale only |
| 7 | zero density with multiplicity (seed 6) | fixed point `1 − 1/(6A)`: DH 11/12; Huxley-type 19/21, Ivić-type 9/10 *if* they held with multiplicity | DEAD (circular) | the `Q = 1` term `H^{1/6}` makes the input contain the conclusion |
| 8 | Kuznetsov / spectral large sieve on the cover (seed 7) | no exponent | DEAD (HEURISTIC) | any bound valid for all coefficient vectors has Δ ≥ L (RUNG §3a); the μ is already spent in absorption |
| 9 | Größencharacter / angular twists (seed 8) | `c = 1 − 1/(6(1+τ))` | DEAD | adds rows, no principal copies; twist exponent `j` (B_{p,j} = χ^{−j−2}) unchanged |
| 10 | Hasse–Davenport products, Gross–Koblitz, Stickelberger (seed 9) | no new family | DEAD | Galois angle condition (LEVERAGE §1.3) holds for every algebraic identity; Gross–Koblitz is p-adic (no archimedean sign); multi-Gauss products need several Poisson variables (Lemma A: σ ≥ 7/6) |
| 11 | repository criteria under 7/8 (seed 10) | Robin graded (done); dBN `Λ ≤ 9/32` (no gain); Li growth rate factor 3/4; NB none | CONDITIONAL, small | constant factors only; see §11 |
| 12 | function-field truth table (seed 11, conceptual) | Stepanov's method has no number-field analogue at power scale | DEAD for power scale | Oct 1 determinants (the nearest analogue) are log-scale (SIEGEL_DETERMINANT) |
| 13 | N-a diagonal-free cross-scale moment `Σ_u A_u(D) conj A_u(4D)` | no original or dual diagonal | DEAD | the principal part is not sign-definite; a Hermitian completion restores diagonals |
| 14 | N-b κ-law partial sub-diagonal target + Prop. L (lifting) | `σ = 11/12 − η(5/6−κ)/2`; Oct 5 ⇒ `κ = 5/6` for `η < 6/11` (PROPOSED); numerics `κ̂ ≈ −0.05` | ALIVE (target) | κ = 5/6 is a fixed point of lifting; `κ < 5/6` needs coefficient-specific large values for generic rows |
| 15 | N-c row reweighting / structured rows (S-units, weights `N(u)^{−α}`) | best = 11/12 at range `x = 1` | DEAD | mediant inequality; leverage = principal ÷ average multiplicity, which is uniform on S-unit rows |
| 16 | N-e Vaughan/Heath-Brown bilinear split of μ into short pieces | type II via Hölder needs `H ≥ max(A,B)² ≥ D` | DEAD | the principal class of `B_u²` gives `H^{1/6}A⁴`; principal-row type II sums have no oscillation |
| 17 | N-f the 7/8 import as base case for the Oct 5 induction at `ρ < 1` | none | DEAD | the dual sums `B_h` have no Euler product, so zero-free regions do not bound them |
| 18 | Weil positivity on short support under 7/8 | not quantified | OPEN | needs an explicit-formula analysis of support length against `2β − 1 ≤ 3/4` |

Two more mechanisms were examined inside the rows above:
* the product family `A_u(D)A_u(Z)`: its coefficient `μ*μ` gives `d(n)ᾱγ₂` → the A2 fourth moment
  (AGENDA A1), with `c` unchanged;
* the norm-form rows `u = N_{L/K}(x)`: principal for all columns only on sixth powers
  (Grunwald–Wang), so nothing new.
* the anticyclotomic family `n ↦ χ_n(u/ū) = (u/N n)₆` (own idea).
  * It looks like leverage `c = 1/2`: all rational `u` (`≍ √H` rows) are principal, and the
    principal sum is still `Σ μ_K(n)W`.
  * But `u ↦ u/ū` has fibres of size `≍ √H` for *every* member, so the multiplicity is uniform.
    Leverage is principal multiplicity divided by typical multiplicity, which here is 1.
  * Poisson gives `γ·γ̄`-type products, so absorption fails (LEVERAGE §2.2, quotient row). DEAD.

## Short notes per mechanism (≤ 1 page each)

**1. Galois symmetry (PROVED-HERE + EMPIRICAL).**
* Complex conjugation gives `(ū/n̄)₆ = conj (u/n)₆`, and `μ(n̄) = μ(n)`. Hence `A_ū(D) = conj A_u(D)`
  for real Galois-invariant `ν`, `W`. Checked with the moments/ kernel: max deviation `1.3·10⁻¹⁴` over
  5436 rows; rational rows give real `A_u`.
* The principal set is Galois-stable, so this halves rows and principal rows alike: `c` is unchanged.
* For a rational squarefree column `m`: split `p` gives two prime ideals (`μ_K = +1`) and inert `q`
  gives `−1`, so `μ_K(m) = χ₋₃(m) μ(m)²`. The Möbius sign is gone.
* At split `p`, `χ_p(u) = (u/π)₆(u/π̄)₆ = χ_π(u/ū)`. Checked exactly: 979/979 pairs, and
  1508/1508 rational rows trivial.
* So the rational-column subfamily has leverage `1/2` but no μ: its principal sum has Dirichlet series
  `L(s,χ₋₃)/L(2s, ·)`.
* The remaining Galois structure is the positive Galois-coherence piece of DUAL_ANATOMY §1.2. It
  cancels nothing, and random multiplicative signs with `f(π) = f(π̄)` reproduce it.

**2. Pointwise 7/8 + ladder (PROVED-HERE bookkeeping).**
* Hölder with the Oct 5 second moment gives `σ₁ − σ₀ = (11/12 − σ₀)/k`. Mixed moments over two
  scales have the same homogeneous bookkeeping.
* With DH multiplicity density (DISPERSION §3c) and `β* = 7/8`, the output is `7/8 + ρ/24`.
* In conductor-graded form, the 7/8 import already pays RUNG §4 item 2 at `ρ = 9/10`
  (`1/2 + 5·(9/10)/12 = 7/8`). Only the generic large-values count (item 3) is missing; see
  ROW_REWEIGHTING_CLOSURE §3.

**3. Kummer Hecke (CONDITIONAL).** See [KUMMER_FIELD_COROLLARIES.md](KUMMER_FIELD_COROLLARIES.md).

**4, 9, 13, 15. Multi-scale, hybrid, angular, reweighting.** See
[ROW_REWEIGHTING_CLOSURE.md](ROW_REWEIGHTING_CLOSURE.md), Prop. W, Lemmas W1–W4.

**5. Sieve weights.**
* With non-multiplicative `λ_d`, the twisted multiplicativity
  `γ_j(ab) = γ_j(a)γ_j(b)χ_a(b)^jχ_b(a)^j` still holds for the Gauss sums. But
  `λ(n)γ₁(n)/(G(n) conj γ₂(n))` is a Hecke character only if `λ(p) = −1·(Hecke)` at every prime and
  `λ` is multiplicative on squarefrees, i.e. `λ = μ·(Hecke)`. The control S7 of LEVERAGE (drop μ →
  every identity fails by exactly 2) is the exact statement.
* Without absorption, only general-coefficient sieves remain. Over all rows they carry the
  principal-class term `H^{1/6}N`, so extraction is trivial (`2σ ≥ 2` at every `h`; sympy `M5`).
* Note: the bare BGL bound *without* that term would give a spurious 23/24 at `h = 1/2`. That is
  exactly the illusion the multiplicity term removes.
* Selberg-type `μ(d)P(log d/log z)` is `μ` times a non-compact `W`, so it is covered by Prop. R.

**6. Deuring–Heilbronn.**
* Every known form (Linnik, Bombieri, Gallagher's averaged version) bounds `1 − β₁` from below by
  `c·Q^{−C(1−β)}` or needs `1 − β₁ ≪ 1/log Q`.
* For a hypothetical zero at fixed distance `1 − β₁ ≈ 1/12`, the inequality is vacuous. No
  power-scale repulsion is known; this matches the log-scale verdict on Oct 1 (SIEGEL_DETERMINANT).

**7. Multiplicity-weighted zero density.** See ROW_REWEIGHTING_CLOSURE Lemma W4. Exact fixed points
(sympy):
* `A = 2` gives 11/12; `A = 12/5` gives 67/72;
* `A = 3/(3σ−1)` gives 19/21; `A = 3/(2σ)` gives 9/10; the Ford-type value is 0.9798.

The middle two would beat 11/12, but a with-multiplicity density estimate contains the conclusion
(the `Q = 1` member has `H^{1/6}` rows). It cannot be proved by general-coefficient large values,
which see the principal class as a single character repeated `H^{1/6}` times (Halász–Montgomery
off-diagonal = `D` for same-class pairs).

**8. Kuznetsov (HEURISTIC verdict).**
* The dual mean square is a sum over twists `h` of theta-coefficient sums. A spectral large sieve
  bounds sums over the *spectrum*, not over twists. Converting twists into spectral data
  (Kuznetsov on the cubic cover) yields a bound valid for every coefficient vector in the
  remaining variable. RUNG §3(a) then caps it at `ρ = 1`.
* The μ-specific information was already used up when μ was absorbed into `γ₂`. No unused μ-structure
  is left for a spectral method to exploit (DUAL_ANATOMY: no structured μ term).

**10. Higher Gauss-sum identities.**
* The angle condition `e/m − a/n ≡ s/2 (mod 1)` (LEVERAGE §1.3) is necessary for every identity
  among Gauss sums, algebraic Hecke characters and powers of `q`. This includes the Hasse–Davenport
  product formula `∏_a g(χψ^a) = −χ^{−k}(k) g(χ^k) ∏ g(ψ^a)` and Stickelberger factorizations.
* Gross–Koblitz expresses Gauss sums through the p-adic Gamma function. It determines them p-adically
  (ideal factorization, congruences), not their archimedean sign, so it cannot supply the Möbius
  parity.
* Products of several Gauss sums need several Poisson variables. LEVERAGE Lemma A then gives
  `σ ≥ 7/6` at threshold.

**11. Repository criteria under 7/8 (CONDITIONAL; constants only).**
* Robin: graded statement already in ROBIN_GRADED (exponent `−1/8` versus RH's `−1/2`).
* de Bruijn–Newman: strip `|Im z| ≤ 3/4` gives `Λ ≤ 9/32`, weaker than the known `Λ ≤ 0.2`.
  Zero density cannot help, because de Bruijn's theorem needs *no* zeros outside the strip.
* Li coefficients: an off-line partner zero `1 − β + iγ` contributes growth
  `|1 − 1/ρ'|^n ≈ exp(n(2β−1)/(2γ²))`. The import caps `2β − 1 ≤ 3/4` instead of `< 1`, so the `n`-range
  in which a hypothetical off-line zero at height `> T₀` cannot yet dominate grows by the factor `4/3`
  (HEURISTIC; the exact Li-positivity range theorem was not re-derived).
* Nyman–Beurling: `d_N → 0 ⟺ RH`. The import changes neither direction, and no rate follows.

**12. Function fields (conceptual; O6 owns the lab).**
* Over `F_q(T)` the analogue of Mom(1, ρ) is true for every `ρ` (Weil). Its elementary proof
  (Stepanov–Bombieri) uses Frobenius-fixed points as an auxiliary-polynomial constraint.
* The only number-field analogue in this wave is the Oct 1 interpolation determinant (Frobenius at
  inert primes), whose budget is intrinsically logarithmic (SIEGEL_DETERMINANT). DEAD for power-scale
  exponents.

**14. κ-law and Prop. L.** See ROW_REWEIGHTING_CLOSURE §3.
* Prop. L: for every row `u` and prime `p`,
  `A_u(x) = A_{up⁶}(x) − νψ_u(p)A_{up⁶}(x/Np)`. Averaging over `≍ Y/log Y` primes with `Y⁶ = x^{1+θ}/R`
  places the sub-diagonal rows inside the Oct 5 range and saves `Y = (x^{1+θ}/R)^{1/6}`.
* This gives `κ = 5/6` at every `η < 6/11`, using Oct 5 only as stated (two fixed `ϑ ≤ 1/10`).
* `kappa_window.py` (EMPIRICAL): on single windows the true family has `M/Diag ∈ [0.83, 0.96]`,
  inside the random-sign spread, so `κ̂ ≈ 0`.

**16. Bilinear split of μ.**
* With Heath-Brown's identity, `A_u` becomes sums of products `B_u(A)C_u(B)` with `AB = D`. A type II
  bound through `(Σ|B_u|⁴)^{1/2}(Σ|C_u|⁴)^{1/2}` needs diagonal-size fourth moments of the shorter pieces.
* Over all rows, the principal class contributes `H^{1/6}A⁴`. So one needs `A², B² ≤ H^{5/6}`, i.e.
  `H ≥ D^{6/5}` at `A = B = √D`, and extraction from `H = D^{6/5}` returns `σ = 1`.
* Without the principal rows (sixth-power-free rows) leverage is lost. Either way: DEAD.

**17. 7/8 as an induction base.** The Oct 5 canonical induction needs `max(H, LF) ≤ Σ`; at `ρ < 1`
it has no base (RUNG §3b). The 7/8 half-plane controls `1/L(s, ψ_u)`, not the theta-twisted series
`B_h`, which have no Euler product (DISPERSION §3e). Even pointwise Lindelöf for `B_h` gives only the
dual diagonal.

**18. Weil positivity (OPEN).** Positivity of Weil's functional for test functions with short support
is known unconditionally for small support (Yoshida). Whether the cap `2β − 1 ≤ 3/4` enlarges the
admissible support was not worked out here. This is the one seed-10 item left OPEN rather than
closed.

## Top three and the single next step

1. **Kummer-field corollaries** (CONDITIONAL-ALIVE). 7/8 for `ζ_F`, `F` ⊂ any abelian extension of
   `Q(√−3)`; least cubic-non-residue prime `≪ (log m)^{8+ε}`.
2. **κ-law** (ALIVE target). `11/12 − η(5/6 − κ)/2`; `κ < 5/6` at any `η > 0` suffices.
3. **Detector–leverage coincidence** (EXACT). `f(σ) = 1/6 ⟺ σ = 11/12`. Both architectures meet
   the wall at the same point when counting with multiplicity.

**Single most promising next step.** Prove (Κ_{η,κ}) with some `κ < 5/6` for ONE small `η`, on ONE
dyadic window `N u ∼ D^{1−η}`.
* By Prop. L, Oct 5 already gives `κ = 5/6` there, and lifting propagates any improvement to the
  whole ladder. The target is therefore a saving of `D^{δη}` over the *lifted* Oct 5 bound on one
  window just below the `ρ = 1` wall.
* That is the smallest statement whose truth would move 11/12. Numerically it holds with `κ ≈ 0`.
* Caution, so as not to mislead: the lifted rows `up⁶` carry no new characters
  (`ψ_{up⁶} = ψ_u` away from `p`), so "cancellation between `p`-lifts" is the window problem again.
* The equivalent form worth attacking is a *restricted* Oct 5 mean square on the thin, structured
  row set `S = {u p⁶ : N u ∼ D^{1−η}, N p ∼ Y}`, of density `D^{−5(η+θ)/6}` in the Oct 5 range:
  `Σ_{u ∈ S} |A_u(D)|² ≪ D^{2+θ−δ}` for some `δ > 0`.
* Oct 5 bounds this by the *full* range, which is exactly the `κ = 5/6` loss. Any restricted large
  sieve that sees the thinness of `S` would do. Note that `S` is not a lattice region, so Poisson in
  `u` does not apply directly.

## Files

| file | content | status |
|---|---|---|
| [README.md](README.md) | this index and triage | EXPLORATORY |
| [ROW_REWEIGHTING_CLOSURE.md](ROW_REWEIGHTING_CLOSURE.md) | developed idea 1: Prop. W (closure), κ-law, detector coincidence | PROPOSED |
| [KUMMER_FIELD_COROLLARIES.md](KUMMER_FIELD_COROLLARIES.md) | developed idea 2: Props. K1, K2 | CONDITIONAL + PROPOSED + EMPIRICAL |
| `triage_exponents.py`, `triage_exponents.out` | exact bookkeeping for every number above | PROPOSED (exact) |
| `galois_cubic_checks.py`, `galois_cubic_checks.json` | Galois symbol identity, `A_ū = conj A_u`, least cubic non-residue primes | EMPIRICAL / exact integers |
| `kappa_window.py`, `kappa_window.json` | κ-law on single dyadic row windows, μ vs random signs | EMPIRICAL (binary64) |
