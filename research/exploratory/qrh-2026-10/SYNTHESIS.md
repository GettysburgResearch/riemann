# Synthesis of the October 2026 quasi-RH research wave

```text
Status: EXPLORATORY synthesis (PROPOSED analyses, EMPIRICAL checks, IMPORTED claims); no RH claim
Scope: two external architectures for zero-free half-planes (OpenAI Sep 30 "7/8" and Oct 5 "11/12");
  their barriers and their scaling; bridges to this repository's programmes
Exact sources or dependencies: INTAKE.md; THRESHOLD_CALCULUS.md; FOURTH_MOMENT_A2.md; BRIDGE_MELLIN.md;
  CONDITIONAL_CONSEQUENCES.md; reports/REPO_RECENT_WORK.md; companion notes listed in Section 5;
  prior repository work: PRs 908, 909, 910 and branch claude/openai-math-riemann-analysis-w5copg
What was actually run: see each file's header
Smallest remaining gap: RH needs exponent 0 everywhere; the best imported claim gives 7/8 (3/8 excess)
```

**RH remains unproved. Nothing here proves or disproves it.** The October 2026 manuscripts claim
*quasi*-RH (a zero-free half-plane `Re s > 7/8`) and are unreviewed. This wave asked what those
methods *can* and *cannot* do, and where a push could move the constant.

## 1. Two architectures, two very different scaling laws

| | Sep 30 "7/8" architecture | Oct 5 "11/12" architecture |
|---|---|---|
| core object | cubic-theta probe with three scales and prime slots; Poisson rows binned by zeros | sextic Möbius family `A_u(D)`, mean square over rows `u`, extraction at `u = p⁶` |
| what sets the constant | low (reflection) estimate `θ_low` | leverage of sixth-power rows (`c = 5/6`) times the moment order |
| scaling with better inputs | **stalls**: 13/15 even with perfect zero counts, perfect energy and row-by-row GLH; 5/6 floor for the probe family | **tends to 1/2**: diagonal `2k`-th moments give `1/2 + 5(1+θ)/(12k)` (PR 910 Prop. 7.2) |
| next rung | cross-row (ratios-type) cancellation, or a bilinear bound beating Cauchy–Schwarz | the fourth moment (PR 910 (3.5)), giving 17/24 |

The Sep 30 architecture is the one that proves 7/8 today. The Oct 5 architecture is the one whose
*structure* points toward the critical line. Every moment rung moves it, and only analytic input
(moments of a specific automorphic family) is missing.

## 2. What is new in this wave (all PROPOSED / EMPIRICAL; see files)

1. **Exact barrier certificates for the Sep 30 architecture.** These use rational LP duals.
   * Low estimate: `σ0 ≥ 13/15` in every geometry; the multipliers `(17/30, 2/5, 1/30)` cancel all
     geometry.
   * Zero-free floor rows: `σ0 ≥ 167/192` at the manuscript's detector floor `a0 = 51/100`, for any
     zero-counting input. As `a0 → 1/2` this becomes 13/15. This reconciles our 0.8698 with
     w5copg's "DH → 13/15".
   * 13/15 survives perfect energy and row-by-row GLH; contour flexibility does not help.
   * A bilinear saving `ϑ` on the reflected side gives `13/15 − 4ϑ/5`, down to 2/3 at `ϑ = 1/4`.
   * [THRESHOLD_CALCULUS.md](THRESHOLD_CALCULUS.md)
2. **Rigidity of 7/8.**
   * Re-optimizing the geometry gains `4·10⁻⁵`; this agrees with PR 910's exact limit.
   * Iterating the bootstrap from `β* ≤ 7/8` gains nothing.
   * Single moment constants (capacities, amplification slope) buy less than `5·10⁻⁴` each.
   * PR 910's joint moment (6.6), even granted on the whole detector range, buys at most
     `1/192`, because the floor rows then bind.
3. **The fourth moment has GL(3)-metaplectic shape.**
   * The dual coefficients of PR 910's fourth-moment target are `γ₂(d)γ₂(e)·conj((e/d)₃)` on
     coprime squarefree pairs.
   * This is the cubic A2 Weyl-group-multiple-Dirichlet-series pattern, i.e. Whittaker coefficients
     of cubic `GL(3)` Eisenstein series.
   * An exact nesting identity reduces it to the second-moment column sum at rows `h·d⁴`. Both
     identities were checked with exact sextic symbols.
   * Proposed programme: completion / `GL(3)` reflection / removal, one rank above the proved
     `GL(2)` argument.
   * [FOURTH_MOMENT_A2.md](FOURTH_MOMENT_A2.md), with a literature assessment in
     [A2_LITERATURE.md](A2_LITERATURE.md).
4. **Bridges to this repository.** See [BRIDGE_MELLIN.md](BRIDGE_MELLIN.md) and
   [CONDITIONAL_CONSEQUENCES.md](CONDITIONAL_CONSEQUENCES.md).
   * Two-sided relative continuation (QRH) versus one-sided Landau (repo).
   * A graded Mellin lemma (premise exponent `θ` excludes zeros right of `1/2+θ`).
   * The graded NRC32 identity `limsup log S_Y/log Y = 4Θ − 2`.
   * A family-relative single step that would suffice for RH (RH-strength).
   * Under the imported claim, every RH-equivalent subpower premise here has exponent `3/8`
     instead of the trivial one; RH needs `0`.
5. **Kintali's 47/48 architecture** has closed form `max(11/12, 7/6 − 1/(2A))` in its density
   exponent `A`. It reaches 11/12 only with DH-quality Hecke density, and never below.
6. **Verification:** 53/53 exact checks of the 7/8 manuscript's stated arithmetic. Reviews and
   numerics are in Section 5.

## 3. Where a breakthrough would have to come from (ranked)

1. **Fourth moment of the sextic Möbius family (Oct 5 architecture).** This is the only identified
   input with unbounded leverage toward 1/2. It needs a `GL(3)` analogue of the cubic theta
   reflection and of the quadratic large sieve after reflection. Decisive first computation: the
   local twist produced by the A2 functional equation at `p | h`. In `GL(2)` this was
   `χ_p^{-1}χ_p^{-2} = χ_p³`, quadratic.
2. **Cross-row cancellation for zero-free rows (Sep 30 architecture).** A ratios-type average of
   `L(w, χ_u)/L(s, ηχ_u)` over the sextic family. See [FLOOR_BIN_BARRIER.md](FLOOR_BIN_BARRIER.md)
   for the payoff table.
3. **Bilinear saving on the reflected side (Sep 30).** Worth `4/5` per unit, uncapped down to 2/3
   in this model.
4. Everything else (moment constants, detector floor, joint moments, iteration) is capped at
   `≤ 1/120` by the certificates.

## 4. What this wave does **not** show

* It does not verify the manuscripts. Only their stated arithmetic and selected identities were
  checked.
* The barriers are barriers for the stated lemma outputs in the stated architecture. They are not
  theorems about the true size of any probe.
* The A2 identification is a coefficient-shape identification, not a theorem.
* No numerical finding here is a proof of any moment estimate.

## 5. Companion notes and their status

| File | Thread | Status |
|---|---|---|
| [INTAKE.md](INTAKE.md) | statements, architecture, ledger | IMPORTED + EXACT ledger |
| [THRESHOLD_CALCULUS.md](THRESHOLD_CALCULUS.md) | Sep 30 exponent model and barriers | PROPOSED + exact certificates |
| [FOURTH_MOMENT_A2.md](FOURTH_MOMENT_A2.md) | Oct 5 fourth moment ↔ cubic GL(3) | PROPOSED + EMPIRICAL identities |
| [BRIDGE_MELLIN.md](BRIDGE_MELLIN.md) | repo Mellin / NRC32 bridges | PROPOSED |
| [CONDITIONAL_CONSEQUENCES.md](CONDITIONAL_CONSEQUENCES.md) | graded lemma, corollaries, non-improvements | PROPOSED / CONDITIONAL |
| [reports/REPO_RECENT_WORK.md](reports/REPO_RECENT_WORK.md) | digest of PRs 901–910 and branches | SURVEY |
| other companion notes | floor-bin, alternative probes, zero density, numerics, moments, reviews | see README.md |
