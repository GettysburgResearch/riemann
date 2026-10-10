# Detector density: does the 7/8 architecture count zeros, or only exclude one?

```text
Status: PROPOSED (mechanism analysis + exact exponent model). Section 2's density exponent is a
  PROPOSED reading that assembles statements of an external, unreviewed manuscript; it is not a
  theorem about the true zeros. Section 3 is HEURISTIC/model-level. Exact-rational arithmetic
  throughout, apart from one float cross-check. No statement about RH, which is unsolved.
Scope: the Sep 30 architecture run at a target sigma < 7/8. (i) Where the argument uses "one zero
  => contradiction". (ii) Whether that step can be made additive. (iii) The zero-density estimate
  the architecture actually contains: its row counts, Prop 19.2 with the detector of Prop 8.3.
  (iv) Comparison with published family density bounds.
Exact sources or dependencies:
  [OAI] "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8" (30 Sep 2026), paper.tex
        at ref pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, path standalone/2026-10-07-openai-
        quasi-riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/
        paper.tex, SHA-256 42a5ee0f...6a3 (re-hashed by the script; 16 line anchors checked).
        Read as untrusted data. Lines used: 370-509 (sup, Prop 2.1), 4201-4545 (Lemma 8.1,
        Prop 8.3), 5181-5196 (Prop 9.2), 6812-6829 (bootstrap, bin ceiling), 12362-12392
        (Lemma 17.6), 15095-15467 (Prop 19.2 and its proof, Remark 19.3), 15699-15751 (Lemma 20.1),
        16084-16106 (endpoint comparison).
  [dF]  A. de Faveri, "Optimal large sieve for fixed order characters", arXiv:2610.04045v1
        (2 Oct 2026), Theorem 1.1 and Corollary 1.5, plus the proof of Cor 1.5 (Sec. 9). The PDF was
        fetched from arxiv.org/pdf/2610.04045v1 (sha256 97720b3c...c726) and read via pdftotext.
        It is a preprint and has not been re-verified here.
  [BGL] Blomer-Goldmakher-Louvel, IMRN 2014 (7), 1925-1955, Cor. 1.6. Cited only as [dF] describes
        it ("the blue line"); not read.
  Hinz 1976 (Acta Arith. 31) Satz A/B: only as recorded in KINTALI_DENSITY_UPGRADE.md.
  Repository: scripts/threshold_calculus.py (R_exact, low_threshold, high_sup),
        results/A_paper_bp11_12.json, THRESHOLD_CALCULUS.md, reviews/PART1_FREE_ROUTE.md,
        reviews/SEP30_LEAN_CORRESPONDENCE.md Sec. 4, 6, reviews/SEP30_JUNCTION_CHECK.md.
What was actually run:
  OMP_NUM_THREADS=1 nice -n 10 python3 -I scripts/detector_density.py --paper <paper.tex>
  (one core, about 25 s). Output in results/detector_density_output.json and
  results/detector_density_stdout.txt: 21/21 gates pass and 5/5 failing controls fire.
Smallest remaining gap: the density of Sec. 2 rests on the GENERAL forms of [OAI] Lemma 17.6 (with
  Lemma 17.1 behind it) and, for the last 1/560 only, Lemma 18.1 in its zero-slot case. Lean
  formalizes only the instances used inside the 7/8 contradiction
  (SEP30_LEAN_CORRESPONDENCE.md Sec. 6). The smallest statement whose failure sinks Sec. 2 is
  the amplified inverse moment, sum_u |M_u(U^r)|^2 << U^{max(1,(1+5r)/6)+eps}, for
  1 <= r <= 3/2 with rowwise tests. The non-additivity finding (Sec. 1) depends on no lemma being
  true; it is a statement about the proof's logical form.
```

RH is unsolved, and nothing here bears on the critical line. "Rows" are the sixth-power-free
elements `u` with `q_u ≍ U` of the Poisson side. Each row carries the finite set of presentations
`X_u = {ν(·)χ_·(u)^{±1} : ν ∈ Θ}` of [OAI] 4227-4236 (`Θ = ⟨η, T̂⟩` is a fixed finite group). All
exponents are taken base `U`. The row family has about `U` members, so "Kummer-family DH" means
`U^{2(1−σ)}`.

## 0. Answer

1. **The outer step is not additive. It uses one zero and cannot count.** The contradiction is the
   non-continuability of one reciprocal at one zero: the zero that realizes the family supremum
   `β*` (Sec. 1). All other zeros in the family enter only through the rows. They enter as
   **costs**, with positive coefficients, in the high-side error. So adding zeros never adds signal.
   No function `f` with `f(7/8) = 0` comes out of the architecture. That is the mechanism finding.
2. **The inner step is additive and already gives a family density estimate.** The detector
   (Prop 8.3) turns each row with a zero into two large polynomial values. Moment bounds count those
   values. This is Halász–Montgomery-style detection. Assembled at the best detector parameter
   `t ∈ [1, 3/2]` (PROPOSED reading), it gives

   `#{rows q_u ≍ U with a zero in Re s ≥ σ, |Im s| ≤ T} ≪ U^{f(σ)+ε} T^{O(1)}`,  for `T ≤ U^{1/100}`,

   where `f(σ) = (31 − 32σ)/(21 − 12σ)` on `(51/100, 11/12]` and `f(σ) = 2(1−σ)` on `[11/12, 1]`.
   - On the asked interval, `f(13/15) = 49/159 ≈ 0.3082` and **`f(7/8) = 2/7 ≈ 0.2857`, not 0.**
   - `f` vanishes only at `σ = 1`. Combined with the 7/8 theorem, the architecture's family statement
     jumps from `U^{2/7}` just left of 7/8 to "no rows" right of it.
3. **Comparison.** On all of `(51/100, 1)` this exponent is below:
   - the best published bound for this kind of family that we located: [dF] Cor 1.5 at `n = 6`,
     `0.4661` at 7/8;
   - the paper's own sextic large-sieve envelope (Part I, `5/8` at 7/8);
   - full-family Hecke bounds restricted to the rows (Hinz A/B, `2/3` and `4/7`; hypothetical
     full-family DH, `1/2`).

   It is above Kummer-family DH (`1/4` at 7/8) by the factor `A_eff = 8/7` there. It matches DH from
   `σ = 11/12` on. This is PROPOSED and conditional on the general forms of [OAI]'s moment lemmas
   (Sec. 4 lists the caveats).

## 1. Where "one zero ⇒ contradiction" is used, and why it cannot become a count

### 1.1 The single-zero step

* **The supremum (384-387).** `β*` is the supremum of the real parts of zeros over the whole family
  of primitive finite-order Hecke characters of `Q(√−3)`.
* **Prop 2.1 (401-503).** Suppose that for every target `η`:
  * `|J_η| ≪_η Z^{C(σ0)+ω}` (eq. 426);
  * `|J_η − f_η| ≪_η Z^{C(β*)−σ}` (eq. 428).

  Then the Mellin transform of `f_η` continues `1/L^S(s, η)` to `Re s > β* − ε*`, by Fourier inversion
  and the identity theorem (466-491). The contradiction (497-502) reads: "*By the definition of β*,
  some target has a zero ρ with Re ρ > β* − ε*. Its reciprocal has a pole at ρ*".

  That is **one** zero of **one** target, chosen by the supremum. Its depth enters the bookkeeping only
  as the subtracted `Δ = C(β*) − C(7/8)` in the endpoint comparison
  `E_actual(h) − Δ ≤ −49/440640 − (51/64)Δ` (16097-16106).

### 1.2 Four structural reasons the step cannot be made additive

* **(O1) No large value to count.** Prop 2.1 is soft. A zero gives no lower bound for `|f_η(Z)|` at
  any specified `Z`. Constants, thresholds and `H_η` may depend on `η` (429-431). In classical
  zero-detection each zero yields a value of a Dirichlet polynomial `≥ 1/2`, and the mean value
  theorem counts these values. Here a zero yields an obstruction to analytic continuation, and an
  obstruction is not summable.
* **(O2) The other zeros are noise measured against the supremum.** Rows are other members of the
  family: twists `ν χ_·(u)^{±1}` of conductor `≍ U`. Their zeros are controlled only through the bin
  ceiling `a ≤ β*` (6824-6829: "*real parts of actual zeros, all at most β**"). The high error is
  measured relative to `C(β*)` (428; 504-509), not relative to the zero being detected.
  * A target zero at `β` produces signal `Z^{C(β)}`, while the rows give up to `Z^{C(β*) − m}`, where
    `m` is the high-side margin.
  * So a zero is visible only if `β > max(σ0(G), β* − m(G))`.
  * In the model the window is empty at the manuscript geometry (`σ0 = 7/8`, `m ≈ 2.3·10⁻⁴`). At the
    best geometry found (`σ0 = 0.874961`, `m = 2.0·10⁻⁵`; results/A_paper_bp11_12.json) it has width
    `2.0·10⁻⁵`. Even PR 910's exact envelope `0.874957` allows at most `4.3·10⁻⁵`.
  * Inside the window the same argument already proves that there are no zeros. Its "count" is
    therefore 0, and below the window it is undefined (gate C5).
* **(O3) Wrong sign.** In Lemma 20.1's exponent (15726-15735) the row count enters as
  `+d·R`. The paper states this at 16089: "*The coefficient of R … is d*". The bin depth enters as
  `∂E/∂a = 1 − l_y + d > 0`. Every additional witnessed row, and every deeper row zero, *raises* the
  error the single signal must beat (gates C2, C3). Additive detection needs the opposite sign: zeros
  must create large values whose number is bounded above.
* **(O4) No averaging over targets.** The low side is a per-target bound as `Z → ∞` at fixed `η`.
  Prop 2.1 lets thresholds depend on `η`. So no target-aspect mean value (large sieve over `η`) is
  available to turn many target zeros into a moment.

The inner layer is also "one zero per row" (Lemma 8.1, 4281-4330). `M_i(u)` is the *rightmost* zero
of the row's presentations up to height `3iT_1`, and one witness is built from it. So it counts
**members** (rows), not zeros. Zeros of one member number `≪ T log(UT)`, which adds only `U^ε T`.

### 1.3 The quantity that does count

That quantity is the number of witnessed rows per bin, `#B ≪ U^{R+ε}`, in Prop 19.2 (15185-15220).
It is a genuine count from additive detection. In the proof of 7/8 it is consumed as a cost (O3). Run
"at target σ < 7/8", the architecture therefore yields no new density statement; it fails at the
barriers of THRESHOLD_CALCULUS.md (13/15, 167/192). The density it does contain is the row count
itself. Sec. 2 extracts it as a stand-alone statement.

## 2. The density estimate inside the detector (PROPOSED reading)

### 2.1 Inputs, all stated in [OAI] for `a > 51/100`, `δ = 2a − 1 ≤ 1`

* **Prop 8.3 (4510-4545).** For every `t ∈ [1, 3/2]`, each row in bin `a` has witnesses `M_r`, `S_m` with:
  * `t − 1/2 − O(ε) ≤ r ≤ t`, `r + m ≥ t`, `0 ≤ m ≤ 1/2 + O(ε)`;
  * `|M_r|² ≫ U^{δr−ε}` and `|S_m|² ≫ U^{δm−ε}`.

  The bound `m ≤ 1/2` comes from pointwise bounds, not from a moment.
* **Lemma 17.6 (12362-12392), via eq. (no-slot-inverse-count) (15282-15290) and Remark 19.3
  (15448-15467).** Inverse count `e(r) − δr`, which is `1 − δr` for `r ≤ 1` and `1 − α + (α−δ)r` for
  `r ≥ 1`, with `α = 5/6`. Remark 19.3 states it "for each fixed `t ∈ [1,3/2]`", for `δ ≤ 1`, with
  no prime-supply hypothesis.
* **Lemma 18.1, zero-slot case (12531ff; used at 15239).** Plain count `1 − 2δm`. With `z = 0`, `κ`
  and the `β* ≤ (1+κ)/2` hypothesis do not enter.
* **No prime slots.** Amplitude class `x = 0` is the *worst* class for a total count, because slots
  only lower the per-class count. So a count of all rows in a bin is governed by `x = 0`, which needs
  neither the supply hypothesis `> 7/37` nor `κ`. The `+Δ/4` of Prop 19.2 comes only from the slot
  capacity at `x > 0` (15392-15405).

### 2.2 Assembly

For a fixed `t`, a row subdivision `(r, m)` is counted by the better of its two witnesses, and the
worst subdivision is taken. Then `t` is chosen:

    R(δ) = min_{t∈[1,3/2]} max( 1 − 2δt/3 ,  1 − δ + (α−δ)(t−1) ) = 1 − 2αδ/(3α − δ)   (δ ≤ α),
    R(δ) = 1 − δ                                                                       (δ ≥ α),

The optimum is `t* = α/(α − δ/3)`, which is `10/7` at `δ = 3/4`.

* At `t = 1` this is the paper's own no-slot clause, `1 − 2δ/3` (15214-15219, 15438-15445; gate A4).
* It is the `x = 0` limit of the paper's selected formula `R* = 1 − δ + (α−δ)δP_x/(2J)` (gate A5).
* It agrees with `threshold_calculus.R_exact` at `x = 0` (gate A8, float).

The paper states the no-slot count only at `t = 1`, so using `t ∈ (1, 3/2]` without slots is a
recombination of stated pieces: PROPOSED, needing its own review. With `δ = 2σ − 1`:

    f(σ) = (31 − 32σ)/(21 − 12σ)   for 51/100 < σ ≤ 11/12,      f(σ) = 2(1 − σ)   for 11/12 ≤ σ ≤ 1.

Two variants:

* **Inverse witness only** (drops Lemma 18.1 entirely). The count is
  `1 − δ/2 − δ²/(2α) = 1 − δ/2 − 3δ²/5`, which is `23/80 = 0.2875` at 7/8. The plain fourth moment is
  worth only `1/560` there (gate A9). The estimate therefore rests essentially on Prop 8.3 and
  Lemma 17.6 alone.
* **Height.** Zeros up to height `3IT_1` with `T_1 = Z^τ ≤ U^{1/100}`, at a cost `(1 + T_1)^{A_𝒜}`
  with `A_𝒜` unspecified. This is a `U`-aspect statement with an unquantified `T`-power.

### 2.3 Table on (13/15, 7/8] (exponents of `U`; script output, exact values in the JSON)

| σ | trivial | Part I envelope [OAI Prop 9.2] | Hinz A (restricted) | Hinz B (restricted) | [dF] n=6 | full-family DH (restricted, hyp.) | detector, inverse only | **detector f** | Kummer DH (hyp.) |
|---|---|---|---|---|---|---|---|---|---|
| 13/15 | 1 | 0.6333 | 0.7059 | 0.6154 | 0.4891 | 0.5333 | 0.3107 | **0.3082** (49/159) | 0.2667 |
| 0.868 | 1 | 0.6320 | 0.6996 | 0.6083 | 0.4855 | 0.5280 | 0.3070 | **0.3046** | 0.2640 |
| 0.870 | 1 | 0.6300 | 0.6903 | 0.5977 | 0.4800 | 0.5200 | 0.3014 | **0.2992** | 0.2600 |
| 0.872 | 1 | 0.6280 | 0.6809 | 0.5872 | 0.4745 | 0.5120 | 0.2959 | **0.2939** | 0.2560 |
| 0.874 | 1 | 0.6260 | 0.6714 | 0.5767 | 0.4689 | 0.5040 | 0.2903 | **0.2884** | 0.2520 |
| 7/8 | 1 | 0.6250 | 0.6667 | 0.5714 | 0.4661 | 0.5000 | 0.2875 (23/80) | **0.2857** (2/7) | 0.2500 |

Context values of `f`:

| σ | 3/4 | 4/5 | 5/6 | 11/12 | 19/20 |
|---|---|---|---|---|---|
| `f` | 0.5833 | 0.4737 | 0.3939 | 1/6 | 1/10 |
| [dF] n = 6 | 0.7273 | 0.6411 | 0.5714 | 1/3 | 0.2340 |

**Sanity.**
* `f(7/8) = 2/7 ≠ 0`.
* `f` is strictly decreasing, with `f > 2(1−σ)` on `(51/100, 11/12)` and equality from `11/12` on
  (gate A7).
* `A_eff(7/8) = f/(2(1−σ)) = 8/7`.

## 3. The model for the outer step, in "density mode"

Task 2's additive exponent model cannot be built for the outer step, because the step is not additive.
The script computes the three quantities that replace it:

1. **Sign table (exact, manuscript geometry).**
   * `∂E/∂R = d = 13/16` at `d = h`.
   * `∂E/∂a = 4/3`.
   * The target's zero enters only as `−Δ` (gates C2-C4).
2. **Visibility window.** As in (O2): empty at the manuscript geometry, width `2·10⁻⁵` at the best
   model geometry, and inside the region the argument already makes zero-free (gate C5).
3. **The jump.** The architecture's combined family statement is `≪ U^{f(σ)+ε}` for `σ ≤ 7/8` and
   "empty" for `σ > 7/8`. The left limit at 7/8 is `2/7` (gate C6).

Getting `f(7/8) = 0` would require changing both of the following:

* A **quantitative** per-target detector, in which a zero at `β` gives `|J_η(Z)| ≥ Z^{C(β)−ε}` at
  controlled `Z`, uniformly in the conductor of `η`. This replaces (O1) and (O4).
* High-side noise measured against **each target's own** zero rather than the family supremum. This
  replaces (O2) and (O3). Since a target's rows are other family members, the second change
  presupposes the conclusion: the members dirtier than the target must already be few. It is a
  bootstrap in density, not a reformulation.

Pricing such a hypothetical is DH-input territory, already covered by THRESHOLD_CALCULUS.md
Scenario D (`167/192`) and KINTALI_DENSITY_UPGRADE.md. It is not repeated here.

## 4. Literature comparison and caveats

* **[dF] Cor 1.5** (arXiv:2610.04045v1). Let `K ⊇ μ_n`, and sum over `n`-th power free
  `a ∈ I(S)` with `N(a) ≤ N`. The bound is `Σ N(σ,T,a) ≪ N^{1−δ_n(σ)+ε} T^{1+d(1−σ)/(3−2σ)+ε}`,
  with a three-piece `δ_n` (breaks at `1/2 + 1/n` and `1 − 1/(2n)`).
  * The script checks continuity and the endpoints, and a planted typo fires control FC3.
  * `K = Q(√−3)` contains `μ_6`, so `n = 6` applies. The `2n`-th roots condition belongs to
    [dF] Thm 1.4 only.
  * [dF] improves [BGL] Cor 1.6, using the new large sieve `A + B + A^{1−1/n}B^{2/n} + A^{2/n}B^{1−1/n}`.
* **Why the detector does better (PROPOSED).** [dF] works through the large sieve, which holds for
  all coefficient vectors. For `n = 3, 4` that operator norm is provably non-orthogonal
  (de Faveri–Dunn–Hoffstein, arXiv:2607.07911, as recorded in CUBIC_RELAXED_INDUCTION.md). [OAI]
  Lemma 17.6 instead claims an orthogonal-quality mean value for the *specific* truncated-Möbius
  coefficients: `U^{1+ε}` up to length `U`, and slope `5/6` beyond. The failing controls show that
  this claim carries the gain:
  * without `t > 1`, `f(7/8) = 1/2` and the detector no longer beats [dF] (FC1);
  * without amplification, `f(7/8) = 1/3` (FC2).
* **Normalizations.** Full-family bounds (Hinz; hypothetical full-family DH) are for roughly `Q²`
  characters of conductor norm `≤ Q`. Restricting them to the roughly `U` rows (`Q ≍ U`) is lossy.
  That comparison only shows the thin-family estimate is not implied by them.
* **Caveats.**
  1. *Family identification.* `X_u` adds the fixed twist group `Θ` and both orientations, and
     excludes rows supported on `S`. Its identification with [dF]'s `χ_a` (via reciprocity, up to
     `S`-local factors) is PROPOSED and unchecked.
  2. *Counting.* The detector counts members, while [dF] counts zeros with multiplicity. The
     detector's `T`-range is short, `T ≤ U^{1/100}`, with an unspecified power; [dF] is explicit in
     `T`.
  3. *Status of the inputs.* [OAI] is unreviewed. Lean formalizes Lemmas 17.1, 17.6 and 18.1 and
     Prop 19.2's counts only as the instances used inside the 7/8 contradiction (SEP30_LEAN_CORRESPONDENCE.md
     Sec. 4 item 4, Sec. 6). The general statements needed here are not formalized.
  4. *Rowwise tests.* SEP30_JUNCTION_CHECK.md names a qualitative open point: Lemma 18.1 applied
     with rowwise tests. The inverse-only variant avoids it, at a cost of `1/560` at 7/8.
  5. *Status of [dF].* It is a v1 preprint, not re-verified.

## 5. Controls (all fire)

| control | effect |
|---|---|
| FC1 detector `t = 1` only (the paper's no-slot clause) | `f(7/8) = 1/2 > 0.4661`: no longer beats [dF] |
| FC2 no sixth-power amplification (`α = 1`) | `f(7/8) = 1/3` |
| FC3 planted typo in [dF]'s middle piece | continuity at `σ = 2/3` breaks (`2/9 ≠ 1/6`) |
| FC4 planted sign flip of `R` in Lemma 20.1's exponent | `∂E/∂R < 0` is detected |
| FC5 hypothesis "`f(7/8) = 0`" | refuted: the architecture's density gives `2/7` |

## 6. Misreadings to avoid

* "The 7/8 method gives a zero-density estimate vanishing at 7/8." It does not. The zero-free step is
  a supremum argument, and its only density content is the row count, which is `2/7` at 7/8.
* "The detector density is a theorem." It is a PROPOSED assembly of unreviewed lemma statements in
  their general form. Only instance forms are formalized.
* "It beats DH." It does not. It is `8/7` times Kummer-family DH at 7/8, and below *full-family* DH
  only after restriction to a thin family.
* "Lowering σ gives density instead of zero-freeness." Below 7/8 the architecture fails at its
  barriers (13/15 low side, 167/192 floor bin; THRESHOLD_CALCULUS.md). That failure does not turn
  into a count.
