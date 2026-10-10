# Remark 19.3 as a lemma, with the two high-bin lemmas of the Part-I-free route

```text
Status: PROPOSED (exploration level; bounded paper-level check by one agent). It states three
  lemmas: P1F.0 (Remark 19.3 of the Sep 30 manuscript, written as a lemma), P1F.1 (high-bin row
  count) and P1F.2 (high-bin margin, with Review 2's correction lambda <= 527/300). Each has a
  paper-level proof and a Lean cross-reference. Nothing here is integrated or independently
  reviewed. It is not a claim about RH, which is unsolved.
Scope: the derivation at paper.tex 15248-15294 and Remark 19.3 (15448-15467) for bins with
  5/6 <= delta <= 1; the input results it uses (Lemmas 4.5, 8.1, 8.2, Prop 8.3, Lemmas 17.1,
  17.2, 17.6), stated with their hypotheses but not re-proved; Lemmas P1F.1-P1F.2 of
  reviews/PART1_FREE_ROUTE.md; the Lean declarations that prove the matching instances.
  Out of scope: the proofs of the input results (their statuses are those of
  SEP30_VERIFICATION_MAP_V2.md, addendum v2.1), the rest of the Part-I-free composition
  (README.md here), and Lean definitional fidelity beyond what Sec. 6 says.
Exact sources or dependencies:
  [OAI]  Sep 30 paper.tex at ref 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, path
         standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
         The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
         SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (gate T0).
         External and unreviewed; read as untrusted data. Line numbers refer to this file.
  [LEAN] upstream/lean/OAI/NumberTheory/DirichletL at the same ref (17 files; each byte-identical
         to its git blob, gate L0). Read only.
  Repo notes: reviews/PART1_FREE_ROUTE.md, reviews/PART1_FREE_ROUTE_REVIEW2.md,
         reviews/SEP30_LEAN_CORRESPONDENCE.md, reviews/SEP30_VERIFICATION_MAP_V2.md (v2.1),
         reviews/LEAN_BUILD_ATTEMPT.md (build record; not re-run).
What was actually run:
  python3 -I remark_19_3_checks.py <paper.tex> --lean <upstream/lean> --json ...
  (stdlib + sympy, exact rationals only; one core; about 2 s).
  Result: 43/43 gates pass, 14/14 failing controls fire. Output: remark_19_3_checks_output.json
  and remark_19_3_checks_stdout.txt in this folder. Script SHA-256 8b810cca...1fdd85e1 at the
  time of the run.
  Line-by-line reading of [OAI] 1123-1160, 4201-4686, 9209-9269, 12343-12476, 15095-15500,
  15700-15760, 15880-16000, 16100-16240, and of the Lean declarations quoted in Sec. 6.
  No Lean, Lake or comparator process was started.
Smallest remaining gap: Lemma P1F.0 is only as strong as its inputs. Its own step (re-running
  15248-15294 for 5/6 <= delta <= 1) is checked here, but it sits on Lemma 17.6, whose raw
  moment comes from Lemma 17.1 (Rp in v2.1) and so from Lemma 17.2 (Rp). The paper-level status
  of P1F.0 is therefore no better than Rp. The Lean instance (Sec. 6) is kernel-checked, but
  only in Lean's own normalization, and the match of Lean's witness and row objects with the
  paper's was not re-checked here.
```

RH is unsolved. The 7/8 statement is a fixed zero-free half-plane `Re s > 7/8`; it says nothing about the critical line. "Checked" below means a bounded check by one agent with the scope above.

## 0. Summary

* **The question.** The Part-I-free route ([PART1_FREE_ROUTE.md](../../reviews/PART1_FREE_ROUTE.md)) needs a row count for bins with `5/6 ≤ δ ≤ 1`. In the paper this is Remark 19.3 (15448-15467). The remark has no label, and its only justification is a pointer back to 15248-15294. Review 2 rated it "no better than Rp".
* **Lemma P1F.0** (Sec. 2) states the remark as a lemma, with every quantifier and every input result. Sec. 3 proves it at paper level, step by step, following 15248-15294.
* **Review 2's claim is confirmed.**
  * In the proof of Prop 19.2 (15222-15446), the first line that uses `δ ≤ α` is 15303. It is also the only line there with an explicit inequality `δ ≤ α` (gate T3).
  * The derivation 15248-15294 contains no `Δ`, `κ`, `1/24`, `5/6`, `β*` or `11/12`.
  * There, `α` occurs only once, at 15289, inside the identity `(1+5r)/6 − δr = 1 − α + (α − δ)r`, which holds for every `δ` (gates T4, A1).
  * The proof never states an upper bound on `Δ` (gate T8).
* **Lemmas P1F.1 and P1F.2** (Secs. 4-5) are restated from the route note and proved. P1F.2 now carries Review 2's bound `λ ≤ 527/300`. That bound is needed only for the `2ζ` cap in the extension past `d = h`.
* **Lean** (Sec. 6). Each lemma has a kernel-checked counterpart in the import closure of the Lean 7/8 theorem.
  * P1F.0: `no_slot_inverse_count`. Its range is wider, it takes the raw moment as a hypothesis (discharged elsewhere in the closure), and its normalization differs.
  * P1F.1: `high_bin_count`, the same two-case inequality, and `high_count_from_raw_moments`, specialized to `t = 3/2`.
  * P1F.2: `high_source_margin`, which is stronger in `δ`, `Δ` and `q` and has the cruder constant `2ζ`.
* **Status.** All three lemmas are PROPOSED. P1F.1 and P1F.2 add only exact algebra on top of P1F.0 and Prop 8.3. P1F.0 is a re-derivation and inherits Rp from Lemmas 17.1-17.2.

## 1. Setting and notation

These are the paper's objects. Nothing is redefined.

* **Contradiction hypothesis, weak form.** `7/8 < β* ≤ 1`. So `Δ = β* − 7/8 ∈ (0, 1/8]` and `κ = 3/4 + 2Δ ∈ (3/4, 1]`. Write `α = 5/6`.
* **Bins** (Lemma 8.1, 4281-4322). A retained row `u` has a bin `(i, a)` with `a ∈ (51/100 + eℤ≥0) ∩ [51/100, 1]`, `1 ≤ i ≤ I − 1` and `I = ⌈1/e⌉ + 2`. Put `δ = 2a − 1 ∈ [1/50, 1]` (4372). If `a > 51/100`, some presentation `ψ ∈ 𝒳_u` has a zero `ρ = σ + iγ` with `a ≤ σ < a + e` and `|γ| ≤ 3iT₁`.
* **Rows.** Retained nonprincipal sixth-power-free physical rows `u` with `q_u ≍ U = Z^d`, where `d_min ≤ d ≤ d_max`.
* **Polynomials.** `M_u(D; W) = D^{−1/2} Σ_n μ(n) ψ_u(n) W(q_n/D)`, with `ψ_u(n) = ν(n) χ_n(u)^{ε_χ}` (9227-9233).
* **Amplified exponent.** `e(r) = max{1, (1+5r)/6}` (12383).
* **Presentation/dyadic subdivision.** This is a set of rows whose Prop 8.3 witnesses share the label `(ϑ, ς) ∈ Θ × {−1, 1}` and the dyadic pair `(D, N) = (U^r, U^m)` (4541-4546, 15223-15228). Within it, `r`, `m`, `D` and `D_* = U^t` are common.

## 2. Lemma P1F.0 (high-bin no-slot row count)

**Lemma P1F.0 (PROPOSED; Remark 19.3 written as a lemma).** The order of choices is as follows.

1. Fix the arithmetic data `𝒜`, numbers `0 < d_min < d_max`, a witness parameter `t ∈ [1, 3/2]` and a bound `R₀ ≥ 2`.
2. For every `ε > 0` there are `e₀ = e₀(ε) > 0`, a finite height order `A_𝒜` (uniform over moving rows and outer labels) and a constant `C = C(𝒜, ε, e, t, R₀)` such that the conclusion below holds whenever:
   * `0 < e < min{e₀, 10⁻³}`;
   * the height hypothesis of Lemma 8.2 holds, `(1 + T₁)^{A_𝒜} ≤ U^{ε/10}`;
   * `Z` is sufficiently large.
3. **Conclusion.** Let `d ∈ [d_min, d_max]` and `U = Z^d`. Let `(i, a)` be a bin with `5/6 ≤ δ = 2a − 1 ≤ 1`. Let `𝓑` be a set of rows of this bin that lies in one presentation/dyadic subdivision for this `t`. Its common witness length `r` then lies in `[0, R₀]`. Then

   `#𝓑 ≤ C · U^{e(r) − δr + ε} · (1 + T₁)^{A_𝒜}`,

   and, exactly,

   `e(r) − δr = 1 − δr` for `0 ≤ r ≤ 1`, and `e(r) − δr = 1 − α + (α − δ)r` for `r ≥ 1`.

**What it does not use.** The proof uses neither `δ ≤ α` nor any prime slot, prime supply, plain moment, `κ`, `Δ` or `β* ≤ 11/12`. The same statement and proof hold for every `1/50 < δ ≤ 1`, which is the range of Remark 19.3 (15457-15459). The condition `δ ≥ 5/6` only names the instance that the route uses.

**Exponent bookkeeping.**

| Stage | Exponent of `U` | Source | Gate |
|---|---|---|---|
| Lemma 17.6 with `D = U^r`, fixed `c`, loss `ε₀` | `max{1, (1+5(1+c)r)/6} + (1+r)ε₀` | 12374-12375 (`H/P = U^{1/6}H^{5/6}`), 15272-15273 | A0 |
| bound for `0 ≤ r ≤ R₀` | `≤ e(r) + 5cR₀/6 + (1+R₀)ε₀` | 15274 | A3 |
| `c = 3ε_m/(10 max{R₀,1})`, `ε₀ = ε_m/(4(1+R₀))` | `≤ e(r) + ε_m/2` | 15277-15280 | A4 |
| rowwise heights `\|t_u\| ≤ (3I+1)T₁` | factor `(3I+2)^A (1+T₁)^A` | 15262-15266 | A5 |
| division by the spike `\|M_r\|² ≫ U^{δr − ε_w}` | `e(r) − δr + ε_m/2 + ε_w` | 4531, 15281 | A6 |
| `ε_m = ε`, `ε_w = ε/2` | `e(r) − δr + ε` | 15285 | A6 |
| the two branches | `1 − δr` (`r ≤ 1`); `1 − α + (α−δ)r` (`r ≥ 1`) | 15286-15292 | A1, A2 |

**Inputs and their exact hypotheses.** These are quoted as stated in the paper; they are not re-proved here. The v2.1 statuses are those of SEP30_VERIFICATION_MAP_V2 Sec. 10.

| Input | Lines | Hypotheses (as stated) | Instance used | v2.1 |
|---|---|---|---|---|
| Lemma 4.5 (smooth calculus) | 1123-1210 | the parameter Sobolev inequality eq:parameter-sobolev; "rowwise choices of norm-twist heights of absolute value at most `T₁` cost a fixed power of `1+T₁`" (1148-1151) | rowwise `σ_u`, `t_u` (inside Lemma 17.6) | R |
| Lemma 8.1 (buffered bins) | 4281-4322 | retained row `u`; `0 < τ ≤ d_min/100`, `T₁ = Z^τ > 2`, `0 < e < 10⁻³`, `I = ⌈1/e⌉+2` (4270-4276) | the zero `ρ` with `a ≤ σ < a+e`, `\|γ\| ≤ 3iT₁` | R |
| Lemma 8.2 (pointwise dyadic estimates) | 4385-4417 | bounded nonnegative ranges for `r, m`; `ψ ∈ 𝒳_u`; untwisted profiles with uniformly bounded seminorms on a fixed annulus; pure twist height `≤ (3i+1)T₁`; added Mellin frequencies `≤ T₁/2`; `0 < e < e₀(ε)`; `(1+T₁)^{A_𝒜} ≤ U^{ε/10}`; `Z` large | the upper bounds `\|M_r\|² ≪ U^{δr+ε}`, `\|S_m\|² ≪ U^{δ min(m,1−m)+ε}`, used inside Prop 8.3 | R |
| Prop 8.3 (two saturated witnesses) | 4510-4547 | bin `(i,a)` with `a > 51/100`; the loss and height hypotheses of Lemma 8.2; `t ∈ [1, 3/2]`; `ε > 0`, after reducing preliminary losses | `\|M_r\|² ≫ U^{δr−ε}` (4531); `r ≤ t + O(1/log U)` (4521); one label and one dyadic pair per row; both twists at height `γ − ν` with `\|ν\| ≤ cT₁` (4537-4539) | R |
| Lemma 17.1 (marked inverse moment) | 9250-9269 | fixed bounded ranges for `m, r, z_i`; a bound for `\|I\|`; `c₁, c₂ > 0`; `r + 2z ≤ m − c₁` and `2r + 8z ≤ 3m − c₂` | `m = 1`, no slots, `Z = H`, `r = log_H D` with `H ≥ D^{1+c}`, which gives eq:raw-moment (12346-12358) | Rp |
| Lemma 17.2 (canonical marked estimate) | 9296-9340 | as stated there | inside the proof of Lemma 17.1 | Rp |
| Lemma 17.6 (sixth-power amplification) | 12362-12389 | `ν, W, ε_χ` and zero extensions as in Lemma 17.1, no prime slots; `U, D ≥ 1`; sum over `u` with `q_u ≍ U` and every prime valuation of `(u)` at most five; every fixed `c > 0`, `ε > 0`; `H = max(2U, D^{1+c})`, `P = (H/U)^{1/6}`; rowwise tests `W(y)y^{−σ_u+it_u}` with `σ_u` in a fixed compact interval and `\|t_u\| ≤ T₁`, at cost `(1+T₁)^A` | `D = U^r`, `0 ≤ r ≤ R₀`, `W = W_base`, `ν = ϑ`, `ε_χ = ς` | R (given Lemma 4.5) |

The derivation sits inside the proof of Prop 19.2 (15185-15446), whose status is Rp.

## 3. Proof of P1F.0, and where δ ≤ α or Δ ≤ 1/24 could enter

The proof follows 15248-15294. Each step names the lines it re-reads and says whether it uses `δ ≤ α` or `Δ ≤ 1/24`.

| Step | Lines | What happens | Uses `δ ≤ α`? | Uses `Δ ≤ 1/24`? |
|---|---|---|---|---|
| S0 | 15223-15228 | Fix one presentation/dyadic subdivision. There are `O_𝒜((log U)²)` choices. `r`, `m`, `D` and `D_* = U^t` are common. | no | no |
| S1 | 15249-15252 | Lemma 17.6 applies: the rows are sixth-power-free (valuations at most five), and the zero extensions are unchanged. The fixed label gives `ν = ϑ ∈ Θ` and `ε_χ = ς`. No slot is selected. | no | no |
| S2 | 15253-15260 | The common base profile is `W_base(y) = W₁(y) V_≤(Dy/D_*)`. Its seminorms are uniformly bounded, because `D ≪ D_*` and a derivative of the cutoff lives where `Dy/D_*` is in a fixed compact set. | no | no |
| S3 | 15260-15266 | Rowwise parameters: `σ_u = Re ρ_u ∈ [a, a+e) ⊂ [51/100, 1 + 10⁻³)`, which is compact. The twist is `t_u = −(γ_u − ν_u)` with `\|t_u\| ≤ (3I+1)T₁`. The cost `(1 + (3I+1)T₁)^A ≤ (3I+2)^A(1+T₁)^A` is a fixed constant times `(1+T₁)^A` (A5). Compactness needs only `a ≤ 1`, which holds for every bin. | no | no |
| S4 | 15268-15276 | eq:amplified-note with fixed `c` and loss `ε₀` gives `Σ_u \|M_u(U^r; W_{σ_u,t_u})\|² ≪ U^{max{1,(1+5(1+c)r)/6} + (1+r)ε₀}(1+T₁)^A` (A0). For `0 ≤ r ≤ R₀` the exponent is at most `e(r) + 5cR₀/6 + (1+R₀)ε₀` (A3). This is uniform as `r → 1`: no margin `1 − r` is needed. | no | no |
| S5 | 15277-15280 | Take `c = 3ε_m/(10 max{R₀,1})` and `ε₀ = ε_m/(4(1+R₀))`. Both are fixed before `U`. The two extra terms total `ε_m/2` when `R₀ ≥ 1` (A4). | no | no |
| S6 | 15281-15285 | Divide by the spike. All terms are nonnegative, so the sum over `𝓑` is at most the sum over all sixth-power-free `u` with `q_u ≍ U`. Each `u ∈ 𝓑` contributes at least `U^{δr − ε_w}` (Prop 8.3, 4531). Hence `#𝓑 ≪ U^{e(r) − δr + ε_m/2 + ε_w}(1+T₁)^{A_𝒜}`. With `ε_m = ε` and `ε_w = ε/2` this is the claim (A6). | no | no |
| S7 | 15286-15292 | The case display. For `r ≤ 1`, `e(r) = 1`. For `r ≥ 1`, `(1+5r)/6 − δr = 1 − α + (α − δ)r` identically in `δ` (A1, A2). Here `α` is the constant `5/6`, not a bound on `δ`. | no (notation only) | no |
| S8 | 15293-15294 | "This is not an application of the strict marked moment with the shrinking margin `1 − r`." Control FC7 shows why: Lemma 17.1 with `m = 1`, `z = 0` needs `r ≤ 1 − c₁` with `c₁` fixed. | no | no |

This proves P1F.0. ∎

**Where δ ≤ α does enter.** It first enters at 15303, in the next paragraph ("Because `δ ≤ α` and `r ≤ t + O(ε)`, this is at most `L(t)`"). That step turns the `r ≥ 1` branch into the long count `L(t)` and needs the factor `α − δ ≥ 0`. P1F.0 stops before it. P1F.1 replaces it with the opposite sign (Sec. 4).

The hypothesis `0 < δ ≤ α` also appears in the statement of Prop 19.2 (15188). But no line of 15222-15294 invokes it. The checks behind this:

* T3: the only line in the proof 15222-15446 that matches an inequality `δ ≤ α` (or `δ ≤ 5/6`) is 15303;
* T4, T5: lines 15222-15294, and the Sobolev paragraph 15136-15170 they rely on, contain none of `Δ`, `κ`, `1/24`, `5/6`, `β*` or `11/12`, and `α` occurs only at 15289;
* T8: the whole proof states no upper bound on `Δ` or `κ` beyond `κ ≤ 1` (15429).

Controls FC10, FC11 and FC14 plant such a use at 15270, 15245 and 15330, and the gates then fail.

**Review 2's statement is confirmed:** within the proof of Prop 19.2, the first use of `δ ≤ α` is at 15303.

**Caveats.** These come from the reading, not from the gates.

* The derivation relies on the "preceding Sobolev argument" (15163-15168, inside the paragraph 15136-15170) for the rowwise witness parameters. The rest of that paragraph is about slot coefficients, conjugation and Lemma 18.1's family condition. It contains no `δ`, `Δ`, `κ` or `α` (gate T5).
* Prop 8.3's saturation (`m ≤ 1/2 + O(ε)`, hence `r ≥ t − 1/2 − O(ε)`) uses `δ ≥ 1/50` (4675). That holds for every bin above the floor. P1F.0 does not use the lower bound on `r`; P1F.1 does.
* Remark 19.3 excludes the floor bin `a = 51/100` (15465-15466). High bins are never floor bins.
* SEP30_VERIFICATION_MAP_V2 (its Sec. 19.2 and Sec. 20.4 rows) lists two open items that touch this lemma:
  * the qualitative clauses at 15134-15170, in particular row-dependent witness profiles through Lemma 4.5;
  * "the no-slot endpoint estimate itself was not re-derived" (SEP30_DETECTOR_QUANTIFIERS §6.4(iii)).

  Sec. 3 re-derives the second item at the level of hypotheses and exponents (S0-S8). It does not close the first beyond reading S3 and the Sobolev step 15163-15168.

## 4. Lemma P1F.1 (high-bin row count)

**Lemma P1F.1 (PROPOSED; from PART1_FREE_ROUTE Sec. 2.1, unchanged by Review 2).** Fix `𝒜`, `d_min < d_max` and `t = 3/2`.

* For every `ε > 0` there are `e₀`, `A_𝒜` and `C` such that the following holds under the loss and height hypotheses of Lemma 8.2, for large `Z`.
* Let `d ∈ [d_min, d_max]` and `U = Z^d`. Let `(i, a)` be a bin with `5/6 ≤ δ = 2a − 1 ≤ 1`, and let `𝒞` be any set of rows of this bin with `q_u ≍ U` (for example one amplitude set of Lemma 20.1). Then

  `#𝒞 ≤ C · U^{1 − δ + ε} · (1 + T₁)^{A_𝒜}`.

No prime slot is selected. No plain moment, prime supply, `κ` or `Δ` is used.

*Proof.*

1. **Witnesses.** Apply Prop 8.3 with `t = 3/2` and loss `ε₁` to each `u ∈ 𝒞`. Partition `𝒞` by label and dyadic pair into at most `2|Θ| · O((log U)²)` subdivisions `𝒞_j`. On `𝒞_j` the common length `r_j` satisfies `1 − c₀ε₁ ≤ r_j ≤ 3/2 + O(1/log U)`. The constant `c₀` is absolute (4529, 4536); the lower bound is `t − 1/2 − O(ε)` with `t − 1/2 = 1` (B3).
2. **Count.** P1F.0 on `𝒞_j` with loss `ε₁` gives `#𝒞_j ≤ C U^{e(r_j) − δr_j + ε₁}(1+T₁)^A`.
3. **Case `r_j ≥ 1`.** `e(r_j) − δr_j = 1 − δ + (5/6 − δ)(r_j − 1) ≤ 1 − δ`, because `5/6 − δ ≤ 0 ≤ r_j − 1` (B1). No upper bound on `r_j` is needed.
4. **Case `1 − c₀ε₁ ≤ r_j < 1`.** `e(r_j) − δr_j = 1 − δ + δ(1 − r_j) ≤ 1 − δ + δc₀ε₁ ≤ 1 − δ + c₀ε₁` (B2). The last step uses `δ ≤ 1`.
5. **Sum.** The `O((log U)²)` subdivisions cost at most `U^{ε₁}` for large `Z`. So `#𝒞 ≤ C′ U^{1 − δ + (2 + c₀)ε₁}(1+T₁)^A`. Take `ε₁ = ε/(2 + c₀)`. ∎

**Where each hypothesis is used.** `δ ≥ 5/6` is used only in step 3 (FC1 fails without it). `δ ≤ 1` is used only in step 4 (FC3). `t = 3/2` is used in step 1 (FC2). Neither `Δ ≤ 1/24` nor `κ` is used anywhere.

This is the paper's argument at `δ = α` (15928-15941). There the factor `5/6 − δ` is zero; here it is negative.

## 5. Lemma P1F.2 (high-bin margin, with Review 2's correction)

Let `h = 13/16`, `ℓ = 1/6`, `l_y = 23/48` and `C₀ = −1/48` (15513-15514, 15734). Let `E(d)` be eq:common-high-exponent (15726-15736).

**Lemma P1F.2 (PROPOSED; PART1_FREE_ROUTE Sec. 2.2 with Review 2's correction 1).** Assume:

* `5/6 ≤ δ ≤ 1` and `a = (1+δ)/2`;
* `Δ` real (in the route, `0 < Δ ≤ 1/8`);
* `q ≤ δ/2` (in the route, `0 ≤ q ≤ δ/2`);
* `0 ≤ λ ≤ 527/300` and `R = 1 − δ + λ`;
* `ζ ≥ 0` (in the route, `0 < ζ < 1/48`).

Then:

1. for `0 ≤ d ≤ h`: `E(d) − Δ ≤ −1/48 − δ/16 − Δ + (13/16)λ`;
2. for `h < d ≤ h + ζ`: `E(d) − Δ ≤ −1/48 − δ/16 − Δ + (13/16)λ + (73/300 + λ)ζ`, and `(73/300 + λ)ζ ≤ 2ζ`;
3. at `λ = 0` and `d ≤ h`: `E(d) − Δ ≤ −7/96 − Δ`, and for `Δ ≥ 0` this is at most `−(51/64)Δ − 7/96`.

Since `∂E/∂R = d`, the same bounds hold for any `R′ ≤ 1 − δ + λ` when `d ≥ 0` (C14).

*Proof.* The two lines of eq:common-high-exponent agree (C1). With `R = 1 − δ + λ` they give the exact identity (C2)

`E(d) − Δ = (−1/48 − δ/16 − Δ) + (q − δ/2)/6 + (13/16)λ + (d − h)(33/50 − δ/2 + λ)`.

* **Second term.** `(q − δ/2)/6 ≤ 0`, because `q ≤ δ/2`. The amplitude cap comes from Lemma 19.1 (uniform for `a ≤ 1`, 15023) via 15064-15090. Without it the bound fails (FC5).
* **Slope.** `S(δ) = 33/50 − δ/2` decreases from `73/300` at `δ = 5/6` to `4/25` at `δ = 1` (C3). So `S + λ > 0`.
  * For `d ≤ h` the last term is `≤ 0`. This proves item 1 (vertex maximum 0, C4).
  * For `h < d ≤ h + ζ` the last term is `≤ (S + λ)ζ ≤ (73/300 + λ)ζ`. This proves item 2 (C5).
* **The `2ζ` cap.** `(73/300 + λ)ζ ≤ 2ζ` holds exactly when `λ ≤ 2 − 73/300 = 527/300` (C6). At `λ = 528/300` it fails (FC4). This is the only use of the upper bound on `λ`; item 1 needs only `λ ≥ −4/25`.
* **Item 3.** `−1/48 − δ/16` is largest at `δ = 5/6`, where it equals `−7/96`. The corners are `−7/96`, `−1/12`, `−19/96` and `−5/24` (C7). The comparison with `−(51/64)Δ − 7/96` holds on the whole box, with maximum difference 0 (C8). ∎

**Consistency with the paper.** At `d = h` and `λ = 0`, item 1 is the paper's eq:large-delta-endpoint, `E(h) ≤ C₀ + (3/4 − h)δ = −1/48 − δ/16` (15943-15946; C9).

**In the route, `λ` is tiny.** It collects the `O(ε)` row losses. Lean uses `λ = 78ε + ε_m ≤ 1/32` (Sec. 6), well inside `527/300` (C11).

## 6. Lean cross-reference

**What "kernel-checked" means here.**

* The declarations below are all in the import closure of `OAI.NumberTheory.DirichletL.Nonvanishing` (gate L2: 2,924 modules, matching SEP30_LEAN_CORRESPONDENCE).
* That closure built with 0 errors and 0 `sorry` warnings, and the exported 7/8 theorems print only the three standard axioms (LEAN_BUILD_ATTEMPT Addendum A; not re-run here).
* The quoted text is checked at the cited `file:line` by gate L1 (46 anchors), and each of the 17 files is byte-identical to its git blob at the ref (L0).

"Formally covered instance" means the following: the Lean statement, read in Lean's definitions, is the same inequality for that instance. It does not certify that Lean's `Witness`, `Fiber` and `FreeRow` objects are the paper's Prop 8.3 witnesses and subdivisions. That definitional match is the subject of SEP30_LEAN_CORRESPONDENCE and HECKE_LEAN_FIDELITY, and it was not re-checked here.

Paths below are relative to `upstream/lean/OAI/NumberTheory/DirichletL/`. Namespaces are under `OAI.SevenEighths`.

### 6.1 P1F.0 ↔ `HeckeDetectorNoSlotInverseCount.no_slot_inverse_count`

`Hecke/DetectorNoSlotInverseCount.lean:14`. Quoted, with the fixed data and profile hypotheses (lines 16-20) and the coefficient-transfer formula (lines 34-35) elided as `...`:

```lean
theorem no_slot_inverse_count
    (M : Ideal O) [NeZero M] (H : Subgroup (O ⧸ M)ˣ) ... (R εm : ℝ) (hR : 0≤R) (hεm : 0<εm) :
    ∃ c κ K₀ : ℝ,0<c ∧ c≤1 ∧ 0<κ ∧ 0≤K₀ ∧ ∀ᶠ U : ℝ in atTop,
      ∀ {Label : Type*} (rows : Finset FreeRow) (χ : FreeRow→Label→Character)
        (a ε tstar T allowance : ℝ) (i : ℕ), 1<U → 1/2≤a →
      ∀ (witness : ∀ u,Witness (χ u) U a ε tstar T allowance i)
        (label : Label) (J K : Fin (dyadicLength U)),
      (∀ u∈rows,(witness u).label=label) →
      (∀ u∈rows,(witness u).left=J) → (∀ u∈rows,(witness u).right=K) →
      0≤Real.logb U ((2 : ℝ)^J.val) → Real.logb U ((2 : ℝ)^J.val)≤R →
      ∀ (data : RowData) (reverse : Bool) (C height : ℝ),0≤C → 0≤height →
      2*Real.pi*allowance+(3*i : ℕ)*T≤height →
      (∀ u∈rows,((Ideal.span {u.val}).absNorm : ℝ)≤U) →
      (∀ u∈rows,∀ I : Ideal O,idealCoeff (χ u label) I= ...) →
      (∀ n : ℕ,n≤2 → ∀ s∈Icc (0 : ℝ) 1,∀ t∈Icc (-height) height,
        let W := twistProfile (logTest
          (orientedProfile reverse (inverseTest U tstar (Real.logb U ((2 : ℝ)^J.val)))) n) s t
        RawMoment data W c κ C ∧ RawMoment data (scaleProfile W) c κ C) →
      (rows.card : ℝ)≤(12*(1+height)*(C*K₀))*
        U^(sourceExponent (Real.logb U ((2 : ℝ)^J.val))-
          (2*a-1)*Real.logb U ((2 : ℝ)^J.val)+2*ε+εm)
```

Here `sourceExponent r = max 1 ((1+5*r)/6)` (`Hecke/InverseAmplificationBudget.lean:10`), which is the paper's `e(r)`. The witness fields are `inverse_length_lower : tstar-1/2-76*ε≤r` and `inverse_spike : U^((2*a-1)*r-2*ε)≤‖polynomial ...‖^2` (`Hecke/DetectorWitnessRows.lean:26, 30`).

**Relation to P1F.0.**

* **Stronger in range.** It needs only `1/2 ≤ a`: there is no `a > 51/100`, no `δ ≤ α` and no upper bound on `δ`. Any `tstar` is allowed, and any `r ∈ [0, R]`. The subdivision is the common `label`, `J` (that is, `r`) and `K`.
* **Conditional interface.** The raw moment (the paper's eq:raw-moment, from Lemma 17.1 with `m = 1` and no slots) is a hypothesis, `RawMoment`.
  * In the Lean route it is discharged inside the closure by `ProbeDetectorInverseRawField.source_batch_inverse_raw` (`Detector/DetectorInverseRawField.lean:44`), separately for the balanced (`cB, kB`) and high (`cH, kH`) branches.
  * The amplification itself (the paper's Lemma 17.6) is proved inside: `HeckeInverseAmplification.no_slot_endpoint` (`Hecke/InverseAmplificationEndpoint.lean:11`) and `no_slot_rowwise_endpoint` (`Hecke/InverseAmplificationRowwise.lean:29`).
  * The choice of `c` and of the preliminary loss is `exists_amplification_budget` (`Hecke/InverseAmplificationBudget.lean:41`). It plays the role of 15277-15280 with different constants.
* **Different normalization.**
  * "Eventually in `U`" with an explicit constant `12(1+height)(C K₀)` replaces `≪` and `(1+T₁)^{A_𝒜}`; the height dependence also sits in `C`, which the discharge sets to `C·(1+height)^J`.
  * The spike loss is `2ε` and the moment loss is `εm`, against the paper's single `ε`.
  * The rows are `FreeRow`, nonzero elements with sixth-power-free ideal.

**Formally covered instance.** For every bin with `5/6 ≤ δ ≤ 1` (`a ≥ 1/2` holds), `tstar = 3/2` and `r ∈ [0, 2]`, the count `#𝓑 ≤ const · U^{e(r) − δr + 2ε + εm}` holds in Lean's normalization. In the Lean route the `RawMoment` hypothesis is discharged.

### 6.2 P1F.1 ↔ `HeckeDetectorRowCount.high_bin_count` and `HeckeDetectorHighCount.high_count_from_raw_moments`

`Hecke/DetectorRowCountEndpoint.lean:71`:

```lean
theorem high_bin_count {B C U δ r ε γ : ℝ}
    (hC : 0≤C) (hU : 1≤U) (hδ : 5/6≤δ) (hδ' : δ≤1)
    (hγ : 0≤γ) (hr : 1-γ≤r)
    (hI : B≤C*U^(max 1 ((1+5*r)/6)-δ*r+ε)) :
    B≤C*U^(1-δ+ε+γ)
```

* **Relation: same.** This is steps 3-4 of P1F.1, stated on the bound `B ≤ C·U^x`, with the witness deficit `γ` explicit.
* It uses `5/6 ≤ δ` and `δ ≤ 1` exactly where P1F.1 does: the `r ≥ 1` and `r < 1` branches (FC1, FC3).

`Hecke/DetectorHighCount.lean:12`:

```lean
theorem high_count_from_raw_moments ... (εm : ℝ) (hεm : 0<εm) :
    ∃ c κ K₀ : ℝ,0<c ∧ c≤1 ∧ 0<κ ∧ 0≤K₀ ∧ ∀ᶠ U : ℝ in atTop,
      ∀ (a ε T allowance Δ C height : ℝ) (i : ℕ),
      1<U → 5/6≤2*a-1 → a≤1 → 0≤ε → ε≤1/1000 → 0≤C → 0≤height →
      2*Real.pi*allowance+(3*i : ℕ)*T≤height →
      ∀ {Label Slot : Type*} (F : Fiber M H Label Slot U a ε (3/2) T allowance i),
      Moments F Δ c κ C height εm →
      (F.rows.card : ℝ)≤fiberConstant C height K₀*U^(1-(2*a-1)+78*ε+εm)
```

**Relation: specialized.**

* It is per fiber: one presentation/dyadic subdivision intersected with one amplitude bin.
* It fixes `tstar = 3/2` and `0 ≤ ε ≤ 1/1000`. Its loss is `78ε + εm`: the spike gives `2ε` and the deficit `γ = 76ε` comes from `inverse_length_lower` (B4).
* It carries more hypotheses than P1F.1 needs:
  * the fiber carries a slot system with supply `≥ 7/37` (`Hecke/DetectorRawFiber.lean:46`);
  * it assumes the whole `Moments` bundle.

  The proof uses only `moments.inverse_raw` (gate L3), and the Lean route discharges the other fields anyway.

The per-bin form is `ProbeHighRowFamily.high_adaptive_count_from_raw_moments` (`PrimeRows/NonfloorCount.lean:58`). It is packaged as the `high` field of `ProbeFinalAssembly.CountParameters` (`Detector/FinalAssemblyCountParameters.lean:39-47`): hypotheses `5/6<2*a-1 → a≤1`, bound `U^(1-(2*a-1)+78*ε+εm)` times `card Label · dyadicLength(U)² · card Bin`. That factor is the paper's sum over subdivisions (step 5).

* **One difference at the endpoint.** Lean routes `δ = 5/6` to the balanced branch (`cutoff_eq_high` needs `5/6 < δ`, `Hecke/DetectorAdaptiveCutoff.lean:27`).
* The route sends `δ = 5/6` to P1F.1, as the paper itself does at `δ = α` (15928-15946). Lean's balanced count at `δ = 5/6` is `R_* = 1 − δ` (the paper's 15987-15989) plus `Δ/4` and losses, and the balanced margin absorbs that. So the difference is bookkeeping at one grid value of `δ`.

**Formally covered instance.** Per fiber, at `t = 3/2`, for every `5/6 ≤ δ ≤ 1` and `0 ≤ ε ≤ 1/1000`: `#fiber ≤ const · U^{1 − δ + 78ε + εm}`. Per bin, the same holds for `5/6 < δ ≤ 1`.

### 6.3 P1F.2 ↔ `ProbeCentralExponent.high_source_margin` and `ProbeHighRowFamily.high_mixed_margin`

The exponent identity first. Lean's `relativeExponent δ d R q = -1/48+(2/3)*δ+q/6-(13/16)*(1-R)+(d-13/16)*(R+δ/2-17/50)` (`Detector/CentralExponent.lean:15-16`) is the second line of eq:common-high-exponent. Lean's `sourceExponent a d R q` equals `3/16 + relativeExponent (2a−1) d R q` and also equals `C(7/8) + E(d)` from the first line (gate C10).

`Detector/CentralExponent.lean:53`:

```lean
lemma high_source_margin (δ R q Δ loss ζ d : ℝ)
    (hq : q≤δ/2) (hR : R≤1-δ+loss)
    (hζ : 0≤ζ) (hd : d≤13/16+ζ)
    (hslo : 0≤R+δ/2-17/50) (hshi : R+δ/2-17/50≤2) :
    sourceExponent ((1+δ)/2) d R q-(3/16+Δ)≤
      -1/48-δ/16-Δ+(13/16)*loss+2*ζ
```

**Relation: stronger in `δ`, `Δ` and `q`, but with the cruder extension constant.**

* There is no hypothesis on `δ`, none on `Δ` and no lower bound on `q`. `R ≤ 1 − δ + loss` is an inequality.
* With `R = 1 − δ + λ`, the slope hypothesis `hshi` reads `λ ≤ 67/50 + δ/2`. On `[5/6, 1]` this is at least `527/300`, with equality at `δ = 5/6` (C12). So Review 2's uniform bound is exactly Lean's condition at the worst `δ`.
* With `ζ = 0` and `d ≤ 13/16` the lemma gives item 1 exactly.
* For `h < d ≤ h + ζ` it gives `+2ζ`. That is the route's "`≤ 2ζ`" form of item 2, not the sharper `(73/300 + λ)ζ`, which is not formalized and not needed.

`Detector/CentralMixedMargins.lean:38`:

```lean
lemma high_mixed_margin (δ q Δ loss ζ μ v d : ℝ)
    (hδ : 5/6≤δ) (hd : δ≤1) (hq : q≤δ/2)
    (hl : 0≤loss) (hl' : loss≤1/32)
    (hζ : 0≤ζ) (hv : v≤13/16+ζ) (hμ : 0≤μ) (hdv : d-v≤μ) :
    mixedSourceExponent ((1+δ)/2) v d (1-δ+loss) q-(3/16+Δ)≤
      -1/48-δ/16-Δ+(13/16)*loss+2*ζ+μ
```

**Relation: specialized.**

* It assumes `5/6 ≤ δ ≤ 1` and `0 ≤ loss ≤ 1/32`.
* It adds the mixed-dyadic slack `μ`. With `μ = 0` and `v = d`, `mixedSourceExponent` is `sourceExponent` (`Detector/CentralDyadicWeight.lean:46`), and the lemma is P1F.2 with `λ ≤ 1/32` and the `2ζ` cap.
* The Lean route applies it to every high bin at `loss = 78ε + εm` (`PrimeRows/NonfloorExponent.lean:33`), on the whole row band `Z^{1/100}` to `Z^{13/16+ζ}`. This is the route's "P1F.1 at every `d`", not the intermediate paragraph (FC6).

`Hecke/DetectorRowCountEndpoint.lean:88`, `high_bin_endpoint`, is item 1 at `d = h`. It is the paper's 15943-15946 with a loss, and the relation is **same** (C13).

**Formally covered instances.** Item 1 and the `2ζ` form of item 2 are covered for every `λ ∈ [0, 527/300]` by `high_source_margin`. The Lean route's own instance is `λ ≤ 1/32`, through `high_mixed_margin`.

### 6.4 Summary

| Paper | Lean declaration (file:line) | Relation |
|---|---|---|
| P1F.0 | `no_slot_inverse_count` (`Hecke/DetectorNoSlotInverseCount.lean:14`) | stronger range; raw moment as hypothesis, discharged at `Detector/DetectorInverseRawField.lean:44`; different normalization (`2ε + εm`, eventual `U`) |
| `e(r)` | `sourceExponent` (`Hecke/InverseAmplificationBudget.lean:10`) | same |
| 15277-15280 | `exists_amplification_budget` (`Hecke/InverseAmplificationBudget.lean:41`) | same role, other constants |
| P1F.1 steps 3-4 | `high_bin_count` (`Hecke/DetectorRowCountEndpoint.lean:71`) | same |
| P1F.1 per subdivision | `high_count_from_raw_moments` (`Hecke/DetectorHighCount.lean:12`) | specialized (`t = 3/2`, `ε ≤ 1/1000`, loss `78ε+εm`); extra unused hypotheses |
| P1F.1 per bin | `CountParameters.high` (`Detector/FinalAssemblyCountParameters.lean:39`), via `high_adaptive_count_from_raw_moments` (`PrimeRows/NonfloorCount.lean:58`) | specialized to `δ > 5/6` strictly; `δ = 5/6` is balanced in Lean |
| P1F.2 items 1-2 | `high_source_margin` (`Detector/CentralExponent.lean:53`) | stronger in `δ, Δ, q`; covers `λ ≤ 527/300`; `2ζ` cap only |
| P1F.2 in the route | `high_mixed_margin` (`Detector/CentralMixedMargins.lean:38`) | specialized (`λ ≤ 1/32`), plus slack `μ` |
| P1F.2 item 1 at `d = h` | `high_bin_endpoint` (`Hecke/DetectorRowCountEndpoint.lean:88`) | same |

## 7. Checks and what they authenticate

`python3 -I remark_19_3_checks.py <paper.tex> --lean <upstream/lean>` exits 0 when all gates pass and all controls fire. Without `--lean`, group L and FC13 are skipped (39 gates, 13 controls).

| Group | Result | What it authenticates | What it assumes |
|---|---|---|---|
| T0-T8 text | 9/9 | hash; 55 anchor strings at the cited lines; the theorem numbers of 14 cited nodes, recomputed from the TeX counters; the census of `δ ≤ α`, `Δ`, `κ`, `1/24`, `5/6` in the proof of Prop 19.2 and in the Sobolev paragraph 15136-15170; Remark 19.3 unlabeled | that the regexes catch the spellings used. Uses phrased only in words are found by reading. |
| A0-A7 (P1F.0) | 8/8 | every exponent step of 15268-15292, as exact identities, sign arguments and an exact sweep | the transcription of the paper's displays |
| B1-B6 (P1F.1) | 6/6 | the two-case inequality (identity plus vertex maximum), `t − 1/2 = 1`, and Lean's `78ε` | Prop 8.3's `O(ε)` constant is absolute (4536) |
| C1-C14 (P1F.2, Lean identities) | 14/14 | the two lines of eq:common-high-exponent agree; the P1F.2 identity; vertex maxima for items 1-2; the `527/300` threshold; corners; dominance; Lean's `sourceExponent`/`relativeExponent` equal the paper's `E(d)`; Lean's slope side conditions | multi-affinity, which the code checks before taking vertex maxima |
| G1-G2 grids | 2/2 | 3,198 and 26,460 exact rational points (sanity, not a proof) | — |
| L0-L3 Lean text | 4/4 | 17 file hashes against the git blobs; 46 quoted lines at the cited `file:line`; import-closure membership, with no imported OAI module missing; only `inverse_raw` is used in `high_count_from_raw_moments` | that the build record is accurate (not re-run) |
| FC1-FC14 controls | 14/14 fire | FC1 `δ < 5/6`; FC2 no `t = 3/2` witness; FC3 `δ > 1`; FC4 `λ > 527/300`; FC5 amplitude cap dropped; FC6 intermediate count in a high bin (`E(1/2) = 1/25`); FC7 Lemma 17.1 near `r = 1`; FC8 unamplified exponent (`+1/12`); FC9 fixed deficit `γ = 1/8` (`+3/256`); FC10, FC11, FC14 planted text uses; FC12 numbering; FC13 Lean anchor | — |

## 8. Known misreadings to avoid

1. **"Remark 19.3 is a proved lemma of the paper."** No. It is an unlabeled remark. P1F.0 is this note's statement of it, and its paper-level status is no better than Rp.
2. **"The derivation uses `δ ≤ α` because `α` appears in it."** No. At 15289, `α` is the constant `5/6` in an identity valid for every `δ`. The first use of `δ ≤ α` is 15303.
3. **"The Lean theorem proves P1F.0 as stated in the paper."** Only in Lean's normalization and objects. The raw moment is a hypothesis of the declaration, discharged elsewhere in the closure, and the witness and row objects were not matched line by line with Prop 8.3.
4. **"`λ ≤ 527/300` is a real restriction."** No. `λ` is an arbitrarily small loss; Lean uses `λ ≤ 1/32`. The bound only makes the `2ζ` cap correct.
5. **"P1F.1 needs no amplification."** No. The exponent `1 − δ` uses Lemma 17.6 on the `r ≥ 1` branch (FC8). Without it, the high-bin sign survives (PART1_FREE_ROUTE S1; Review 2 X10), but the count is weaker, and the balanced bins need the amplification anyway (Review 2 NC2).
6. **"This settles the Part-I-free route."** No. See [README.md](README.md). The composition needs a review independent of this model family.

## 9. Reproduction

```sh
# from the repository root
REF=31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6
P=standalone/2026-10-07-openai-quasi-riemann-import/upstream
mkdir -p "$HOME/r193" && git show $REF:$P/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex > "$HOME/r193/sep30.tex"
# optional, for group L: the whole Lean OAI tree at the same ref (read only; nothing is built)
git archive $REF $P/lean/OAI | tar -x -C "$HOME/r193"
cd research/exploratory/qrh-2026-10/proposed/PART1_FREE_7_8
python3 -I remark_19_3_checks.py "$HOME/r193/sep30.tex" --lean "$HOME/r193/$P/lean" --json remark_19_3_checks_output.json
```

The archive must hold the whole `OAI/` tree, because gate L2 walks the import graph from `Nonvanishing.lean` and fails if an imported module is missing. This exact sequence was run once for this note (into session scratch); it gave 43/43 gates and 14/14 controls.
