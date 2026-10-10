# A Part-I-free paper route for the Sep 30 7/8 manuscript

```text
Status: PROPOSED (bounded paper-level review, exploration level). Verdict (A): Part II as written,
  plus the extended endpoint count written out in Sec. 2, proves the 7/8 statement from beta_* <= 1
  alone. This is a new composition of arguments. Under AGENTS.md it needs its own independent
  review. It is not an integration record, and it is not a claim about RH, which is unsolved.
Scope: every place where Part II of [OAI] uses an upper bound on Delta, kappa or delta (Sec. 1);
  the extended endpoint count and margin for bins 5/6 <= delta <= 1 (Sec. 2); the final
  contradiction and the order of choices for Delta in (0, 1/8] (Sec. 3); the resulting node set
  (Sec. 4). Out of scope: the proofs of the analytic lemmas that Part II cites (their statuses are
  those of SEP30_VERIFICATION_MAP_V2.md), Part I itself, and the Lean development beyond the
  declarations named here.
Exact sources or dependencies:
  [OAI]  Sep 30 paper.tex at pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6,
         standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
         The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
         SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-hashed by the
         script). External and unreviewed; read as untrusted data. Line numbers refer to this file.
  [LEAN] upstream/lean/OAI/NumberTheory/DirichletL at the same ref (read-only scratch copy):
         Detector/FinalAssemblyCountParameters.lean, Detector/CentralMixedMargins.lean,
         Detector/CentralExponent.lean, Detector/FinalAssemblyHigh.lean, Hecke/DetectorHighCount.lean,
         Hecke/DetectorRowCountEndpoint.lean, Hecke/DetectorWitnessRows.lean, ParametersHighData.lean,
         Detector/RayPoolDisjoint.lean. Read only; no Lean, Lake or comparator process was started.
  Repo notes read: SEP30_LEAN_CORRESPONDENCE.md (Sec. 4 item 1), PART1_SUBSTITUTION.md,
         SEP30_VERIFICATION_MAP_V2.md, SEP30_JUNCTION_CHECK.md, SEP30_DETECTOR_QUANTIFIERS.md Sec. 6,
         THRESHOLD_CALCULUS.md Sec. 3-4, and the Lemma 18.1 reviews (kappa range only).
What was actually run:
  python3 -I reviews/part1_free_checks.py <paper.tex> --replay-junction  (stdlib + sympy, exact)
  -> results/part1_free_checks_output.json and results/part1_free_junction_replay.json.
  Result: 32/32 exact gates pass (text census, sympy identities, multi-affine vertex maxima, a
  2,838-point exact grid, and the junction replay J1); 10/10 failing controls fire; 2 sensitivity
  rows are informational. J1 re-runs sep30_junction_check.py (SHA-256 30573564...d24efc) in a
  temporary copy with its 13 Delta boxes widened from (0, 1/24] to (0, 1/8]: 83/84 of its gates
  pass, the one failure is P2 (kappa <= 5/6, as designed), and 8/8 of its controls fire.
  Total run time 67 s on one core. Stdout: results/part1_free_checks_stdout.txt.
  Line-by-line reading of [OAI] 370-387, 398-502, 1531-1600, 4201-4420, 4505-4600, 5575-5640,
  5805-5900, 6015-6175, 6800-6870, 8636-8655, 8852-8910, 9100-9150, 12355-12460, 12528-12592,
  12825-12905, 15060-16470.
Smallest remaining gap: the composition itself. Its only new mathematical content is the
  two-case inequality of Sec. 2.1, which is exact algebra. Everything else is an instance of a
  statement the paper already makes for the range a <= 1, kappa <= 1 or delta <= 1. The smallest
  statement whose failure would sink the route is Prop 8.3's saturated witness at t = 3/2
  (r >= 1 - O(eps) with |M_r|^2 >> U^{delta r - eps}), together with Lemma 17.6, for bins with
  5/6 < delta <= 1. The paper already relies on the same pair at delta = 5/6.
```

RH is unsolved. The 7/8 statement is a fixed zero-free half-plane `Re s > 7/8`; it says nothing about the critical line. "Reviewed" below means a bounded agent review with the stated scope.

## 0. Summary

* **The question.** Part II of the Sep 30 manuscript starts from Part I's `β* ≤ 11/12` (6812-6830). That gives `Δ ≤ 1/24`, `κ ≤ 5/6` and the bin ceiling `δ ≤ 5/6`. The Lean proof uses only `β* ≤ 1`. Does the paper's own Part II text survive the weaker input?
* **The answer is yes, with one extension.** The weaker input is already in the paper: `1/2 ≤ β* ≤ 1` is stated at 386-387. With it, `Δ ∈ (0, 1/8]`, `κ ∈ (3/4, 1]` and `δ ≤ κ ≤ 1`.
* **What survives as written.** 117 of the 153 substantive Part II lines that mention one of these bounds are fine as written (Sec. 1). The analytic lemmas that Part II cites are already stated for the larger ranges:
  * Lemma 18.1 for `κ ∈ [3/4, 1]`, with a separate `κ = 1` clause;
  * Lemmas 8.1-8.3, 10.3, 16.1 and 19.1 for `a ≤ 1`;
  * Lemma 10.5 explicitly "also covers `β* = 1`" (6300);
  * Remark 19.3 (15448-15467) states the no-slot inverse count for `δ ≤ 1`, "independently of the current Part II bin ceiling".
* **What needs the extension.** Bins with `5/6 < δ ≤ κ` appear once `Δ > 1/24`. They need their own row count. The paper's endpoint argument at `δ = α = 5/6` (15928-15946) extends word for word to the whole interval `[5/6, 1]`, because `(1+5r)/6 − δr − (1−δ) = (5/6 − δ)(r − 1) ≤ 0` for `r ≥ 1` and `δ ≥ 5/6`. The resulting margin is `E(d) − Δ ≤ −1/48 − δ/16 − Δ ≤ −7/96 − Δ` for every `d ≤ h`. That is far more than the balanced margin `−49/440640 − (51/64)Δ`. This is the Lean `CountParameters.high` / `high_mixed_margin` route.
* **What breaks if misapplied.** The intermediate-row paragraph (16146-16165) uses `δ ≤ 5/6`. Applied to a high bin it fails for `δ > 529/625` (control FC4). It is not needed: high bins use the extended count at every row size, exactly as the paper already does at `δ = α` (16166-16168).
* **Order of choices.** Nothing is chosen in a way that silently needs `Δ ≤ 1/24`. The paper's equal slots `ℓ_i = ℓ/K` survive. One reading of the detector-quantifier note changes: `m_high = min{51Δ/64, 63/800}` equals `m_small` once `Δ > 42/425`. The paper defines `m_high` as that minimum, so the proof is unaffected. Lean's distinct slot lengths serve a different purpose (Sec. 3.3).
* **Verdict (A), PROPOSED.** Part II as written, plus the extended endpoint count of Sec. 2, proves 7/8 from `β* ≤ 1`. This is a Part-I-free paper route. It drops Thm 3.1 and the seven Part-I-only nodes, as the Oct 5 substitution does, and it needs no imported 11/12 theorem.

## 1. Every use of an upper bound on Δ, κ or δ in Part II

**How the list was made.** The script scans Part II (6806-16463) for `11/12`, `1/24`, `5/6`, `\kappa`, `\alpha`, `\Delta`, `\beta_*` and the bootstrap labels. That gives 282 lines.
* 129 of them use the same glyphs for other objects: `κ_F`, `κ_G`, `κ_i`, `κ_P`, `ᾱ(n)`, `α_j`, `Δ_H`, the weight `y^{−5/6}`, the Gaussian `(s−5/6)²`, the geometry `M = 5/6`, and the amplifier coefficient `\tfrac56` inside Lemma 18.1.
* The other 153 lines are assigned to exactly one of the items below (gate T2).
* PART1_SUBSTITUTION.md §1.2's list is a subset of these items.
* The only Part II citation of Thm 3.1 is at 6812 (gate T3).

**Categories.**
* **R**: replaced by `β* ≤ 1`.
* **(a)**: fine for `Δ ≤ 1/8` as written, possibly after a literal restatement of the bound.
* **(b)**: needs the extended high-bin count of Sec. 2 (Lean style).
* **(c)**: breaks if applied to bins with `δ > 5/6`; not needed once (b) is used.

| # | Lines | What it uses | Cat. | Reason / Lean counterpart for (b) |
|---|---|---|---|---|
| U1 | 6812-6815 | Thm 3.1 ⇒ `β* ≤ 11/12` | **R** | Replace by `β* ≤ 1`, which is stated at 386-387 (Euler convergence, and the set in (1.1b) has `Re ρ ≤ 1`). Lean: `HeckeZeroSupremum.beta_le_one`; `FinalAssemblyHigh.lean:115` (`hΔ1`). |
| U2 | 6816-6819 | eq:part-II-bootstrap: `0 < Δ ≤ 1/24`, `κ ≤ 5/6` | (a) | Restate as `0 < Δ ≤ 1/8`, `κ = 3/4 + 2Δ ≤ 1`. The equation is bookkeeping; its consumers are the items below. |
| U3 | 6821-6830 | eq:part-II-bin-ceiling: `δ ≤ κ ≤ 5/6`; endpoint `δ = 5/6` kept | **(b)** | `a ≤ β*` comes from the definition (4370-4383) and gives `δ ≤ κ ≤ 1`. Bins with `5/6 < δ ≤ κ` exist iff `Δ > 1/24` (A19). Lean: bins split by `2a−1 ≤ 5/6` (`counts.cB`) versus `> 5/6` (`counts.cH`), `FinalAssemblyHigh.lean`. |
| U4 | 6842 | `0 < ω < Δ` | (a) | Only `Δ > 0`. |
| U5 | 8647-8648 | low exponent below `C(β*)` by `Δ` | (a) | No upper bound. |
| U6 | 9110-9139 | Lemma 16.2 on `x_r = β* + e` | (a) | Only `β* ≥ 7/8` is used; the local exponents decrease in `β*` (A21). |
| U7 | 12532-12573 | Lemma 18.1 statement | (a) | Stated for `κ ∈ [3/4, 1]`; for `κ = 1` "no zero-free hypothesis is required" (12565). |
| U8 | 12581-12584 | `κ = 2β* − 1` "rather than … 5/6 supplied by the 11/12 bound" | (a) | The dynamic `κ` is kept anyway. If `Δ = 1/8` then `κ = 1` and the `κ = 1` clause applies. |
| U9 | 12833-12906 | (3.4)-(3.5): `s_κ ≥ β*` for `κ < 1`; absolute counting for `κ = 1` | (a) | "uniform in `κ ∈ [3/4,1]`" (12897-12898). |
| U10 | 12932-14906 | Lemma 18.1 internals: `6κ − 1 ≥ 7/2`, `0 ≤ 6κ − 1 ≤ 5`, `κ ∈ [3/4, 1]` | (a) | Only `3/4 ≤ κ ≤ 1`. The Lemma 18.1 reviews checked these on `[3/4, 1]` (LEMMA18_1_CASE2_SEC188, K1, S1, C7). |
| U11 | 15097-15108 | Sec 19.2 preamble: `Δ ≤ 1/24`, `κ ∈ (3/4, 5/6]`, "Since κ < 1 …", `δ ≤ κ ≤ α` | **(b)** | The Lemma 18.1 part is (a): for `κ < 1` equality holds, for `κ = 1` use the `κ = 1` clause. The clause `δ ≤ α` routes bins to Prop 19.2, and bins with `δ > α` go to Sec. 2 instead. Lean: `CountParameters.balanced` (`2a−1 ≤ 5/6`, `Δ ≤ 1/8`) versus `CountParameters.high` (`5/6 < 2a−1`, `a ≤ 1`). |
| U12 | 15175-15180 | `z_P(m) = (1−2m)/(6κ)` | (a) | Any `κ ∈ [3/4, 1]`. |
| U13 | 15185-15226 | Prop 19.2 statement: `0 < δ ≤ α`; `+Δ/4` | (a) | Used only for bins with `δ ≤ α`; `Δ` enters only through `Δ/4` (U16). |
| U14 | 15289-15311 | long branch "Because `δ ≤ α` …" | (a) | Inside Prop 19.2, where `δ ≤ α` is a hypothesis. |
| U15 | 15326-15341 | baseline capacity, derivative signs | (a) | Holds for every `Δ ≥ 0`. |
| U16 | 15398-15420 | eq:capacity-comparison `≤ Δ/4` | (a) | Holds for every `Δ ≥ 0` (A15; junction K1 replayed on `Δ ≤ 1/8`). |
| U17 | 15429 | `1 − 2m ≤ 6κν_0 ≤ 6ν_0` | (a) | Uses `κ ≤ 1`. |
| U18 | 15447-15466 | Remark 19.3: no-slot count for `1/50 < δ ≤ 1` | (a) | Already for `δ ≤ 1`. It becomes load-bearing (Sec. 4). Lean: `HeckeDetectorNoSlotInverseCount.no_slot_inverse_count`. |
| U19 | 15498-15504 | Sec 20 preamble restates U2-U3 | (a) | Restate as in U2; the ceiling as in U3. |
| U20 | 15614-15692 | principal signal on `Re s = β* + e` | (a) | Lemma 10.5 "also covers `β* = 1`" (6300); Lemma 4.9 covers `b > 1` (1593). |
| U21 | 15724 | Lemma 20.1: `R, q` may depend on `β*` | (a) | No bound. Lemma 20.1 is stated per bin, with no `δ ≤ 5/6`. |
| U22 | 15763 | "Its bin ceiling holds by eq:part-II-bin-ceiling" | (a) | Lemma 10.3 needs only `a ≤ β*` (5838) and `Re w = 1−a−6e ≥ −6e > −1/100` (5857), i.e. `a ≤ 1` (A20). |
| U23 | 15859-15882 | small rows on `Re s = β* + e`, relative to `C(β*)` | (a) | `m_small = 63/800` does not depend on `β*`. |
| U24 | 15926-15946 | endpoint argument at `δ = α`; eq:large-delta-endpoint | **(b)** | Extend to `α ≤ δ ≤ κ` (Sec. 2). Lean: `HeckeDetectorHighCount.high_count_from_raw_moments`, `HeckeDetectorRowCount.high_bin_count`, `high_bin_endpoint`, `ProbeCentralExponent.high_source_margin`. |
| U25 | 15949-15992 | balanced range `1/50 < δ < α`; `κ` dynamic | (a) | `κ ≤ 1` suffices; `Δ` enters only through `Δ/4`. |
| U26 | 15995-16072 | Lemma 20.2 on `0 ≤ δ ≤ 5/6` | (a) | Used only for `δ ≤ 5/6`. Lean: `Endpoint.balanced_endpoint_margin`. |
| U27 | 16087-16108 | eq:adaptive-endpoint `−49/440640 − (51/64)Δ` | (a) | An identity in `Δ` (A14); no upper bound. |
| U28 | 16128-16144 | frequency ranges: "For `δ = α`, use `R = 1 − δ`"; slope `≥ 4/25`; `R_* + Δ/4 ≤ 139/96` | **(b)** | Extend "`δ = α`" to `α ≤ δ ≤ κ`. The slope bound `33/50 − δ/2 ≥ 4/25` is the `δ ≤ 1` value (A9; on `δ ≤ 5/6` it would be 73/300). `139/96 = 17/12 + (1/8)/4` is exactly the `Δ ≤ 1/8` value (A16). Lean: `frequency_slope_bounds` (`δ ≤ 1`, `R ≤ 139/96`), `relative_extend`. |
| U29 | 16146-16168 | intermediate rows `d ≤ 1/2`: "the last inequality uses `δ ≤ 5/6`" | **(c)** | As written, `E(1/2) = −529/2400 + 25δ/96 ≤ −49/14400` holds exactly iff `δ ≤ 5/6`, and `E(1/2) > 0` for `δ > 529/625` (FC4). Not needed: high bins use `R = 1 − δ` at every `d`, as the paper already does at `δ = α` (16166-16168). Lean: `intermediate_source_margin` has `δ ≤ 5/6`; high bins use `high_mixed_margin` on all moderate rows (`Z^{1/100}` to `Z^{13/16+ζ}`). |
| U30 | 16174-16185 | `m_hi = 51Δ/64`; "the other endpoint ranges have nonpositive ideal exponents" | (a) | True for the extended range too: `−1/48 − δ/16 < 0`. |
| U31 | 16196-16233 | Prop 20.3: `m_high = min{m_hi, m_small}`; "the equality `δ = α` uses the separate no-slot bound" | **(b)** | The min is unchanged in form; it equals `m_small` for `Δ > 42/425` (A17). Read "the equality `δ = α`" as "bins with `δ ≥ α`". Lean: `Parameters.HighData`, `ProbeHighRowFamily.high_mixed_margin`. |
| U32 | 16241 | Lemma 18.1 mesh on "the compact closure `κ ∈ [3/4, 5/6]`" | (a) | Read `[3/4, 1]`; the mesh is uniform there (12573). |
| U33 | 16269 | "uses `δ ≤ 5/6 < 1`" for `δ max_i w_i < b_round` | (a) | `δ ≤ 1` suffices. Slots are selected only in bins with `δ ≤ α` anyway. |
| U34 | 16324 | choices depend on `Δ` | (a) | `Δ` is a fixed number; any `Δ > 0` works. |
| U35 | 16333-16350 | eq:saving-criterion `E(d) + ε_real ≤ Δ − ε_hi` | **(b)** | For high bins it follows from Sec. 2.2. Lean: `high_mixed_margin`, `balanced_mixed_saving`. |
| U36 | 16370-16446 | `ω = Δ/2`; the late-height hypothesis | (a) | Only `Δ > 0`. |
| U37 | 16454-16460 | final contradiction | (a) | Sec. 3.1. |

**Lemmas outside Part II that Part II invokes, checked for the larger range.** Each is stated for the range the route needs (anchor gate T1 checks the quoted text):

| Lemma | What the route needs | What the statement says |
|---|---|---|
| Lem 4.9 (1531-1600) | `L'/L`, `1/L` on `Re s ≥ b + v` with `b = β*` up to 1 | "first suppose `β* ≤ b ≤ 1` … If `b > 1`, Euler convergence" (1591-1594) |
| Lem 7.1 regions (4053-4058) | `w_r ≥ −1/100` at `a ≤ 1` | region one: `w_r ≥ −1/100`, `x_r + w_r ≥ 1 + ε_0` |
| Lem 8.1 (4281-4368) | bins up to `a = 1` | grid `a ∈ [51/100, 1]`; "allows a zero on the line one" (4338); `1/50 ≤ δ ≤ 1` (4372) |
| Prop 8.3 (4510-4547) | `t = 3/2` for any bin `a > 51/100` | "For every `t ∈ [1, 3/2]`"; `t − 1/2 − O(ε) ≤ r` (4529) |
| Lem 10.3, 10.4 (5809-6155) | `a ≤ 1` | `Re w ≥ −6e > −1/100` (5857); `σ_0 ∈ [7/8, 1)`, `β* > σ_0` |
| Lem 10.5 (6175-6301) | `β* = 1` allowed | "This also covers `β* = 1`" (6300) |
| Prop 16.1 (8853-9049) | `a ≤ 1` | "Let `51/100 ≤ a ≤ 1`" (8854) |
| Lem 17.6 (12362-12389) | `r` up to `3/2 + o(1)` | any bounded nonnegative `r`; no `δ` |
| Lem 18.1 (12531-12579) | `κ ∈ (3/4, 1]` | "Let `3/4 ≤ κ ≤ 1`"; `κ = 1` clause |
| Lem 19.1 (15015-15025) | `a ≤ 1` | "uniform for `51/100 ≤ a ≤ 1`" (15023) |
| Prop 2.1 (400-502) | `β* ∈ (7/8, 1]` | only `Δ_0 = β* − σ_0 > 0` |

## 2. The extended endpoint count (PROPOSED)

Throughout, assume the Part II contradiction hypothesis with the weaker input: `7/8 < β* ≤ 1`, so `Δ = β* − 7/8 ∈ (0, 1/8]` and `κ = 3/4 + 2Δ ∈ (3/4, 1]`. Write `α = 5/6`, `h = 13/16`, `ℓ = 1/6`, `l_y = 23/48`, `z_0 = 17/50`, `C_0 = −1/48`. Every retained bin has `δ = 2a − 1 ≤ κ ≤ 1` (4370-4383).

### 2.1 Row count for bins with α ≤ δ

**Proposed Lemma P1F.1 (high-bin row count).** Let `(i, a)` be a retained bin with `α ≤ δ = 2a − 1`. Let `U = Z^d` with `d_min ≤ d ≤ d_max`, and assume the loss and height hypotheses of Lemma 8.2. Fix a presentation/dyadic subdivision `ℬ` of the bin's rows, with witnesses from Prop 8.3 at `t = 3/2`. Then for every `ε > 0`, after reducing preliminary losses,

`#ℬ ≪_{𝒜,ε} U^{1−δ+ε} (1+T_1)^{A_𝒜}`.

No prime slot is selected. No plain moment, no prime supply and no value of `κ` is used.

*Proof.*
1. Prop 8.3 with `t = 3/2` gives a witness length `r` with `1 − c_0ε ≤ r ≤ 3/2 + O(1/log U)` and `|M_r|² ≫ U^{δr−ε}` (4512-4533; the lower bound is `t − 1/2 − O(ε) ≤ r` at 4529).
2. Remark 19.3 (15448-15467) says that eq:no-slot-inverse-count holds on such a subdivision whenever `a > 51/100` and `1/50 < δ ≤ 1`, with no `δ ≤ α` and no prime-supply hypothesis. That count is `#ℬ ≪ U^{e(r) − δr + ε}(1+T_1)^{A}`, with `e(r) = max{1, (1+5r)/6}` from Lemma 17.6. Its derivation (15248-15294) uses only Lemma 17.6 and the inverse spike; the case display at 15282-15292 is algebra valid for every `δ`.
3. If `r ≥ 1`, then `e(r) = (1+5r)/6` and
   `e(r) − δr = 1 − δ + (5/6 − δ)(r − 1) ≤ 1 − δ`,
   since `5/6 − δ ≤ 0 ≤ r − 1` (gates A2, A4, A5).
4. If `1 − c_0ε ≤ r < 1`, then `e(r) = 1` and
   `1 − δr = 1 − δ + δ(1 − r) ≤ 1 − δ + c_0ε` (gate A3).
5. Replace `ε` by `(1 + c_0)ε`. ∎

This is the paper's own argument at `δ = α` (15928-15941), where the factor `5/6 − δ` vanishes. For `δ > α` the factor is negative, so the same two cases give the same bound. Lean's form is `high_bin_count` (DetectorRowCountEndpoint.lean:71): from `r ≥ 1 − γ` and `5/6 ≤ δ ≤ 1` it concludes the exponent `1 − δ + ε + γ`, with `γ = 76ε` from `DetectorWitnessRows.inverse_length_lower` (`tstar − 1/2 − 76ε ≤ r`, `tstar = 3/2`) (gate A6).

### 2.2 Margin for bins with α ≤ δ

**Proposed Lemma P1F.2 (high-bin margin).** Let `α ≤ δ ≤ 1`, `0 ≤ Δ ≤ 1/8`, `0 ≤ q ≤ δ/2`, `λ ≥ 0`, `R = 1 − δ + λ` and `0 < ζ < 1/48`. Let `E(d)` be eq:common-high-exponent (15726-15734). Then

* for `d_min ≤ d ≤ h`: `E(d) − Δ ≤ −1/48 − δ/16 − Δ + (13/16)λ`;
* for `h < d ≤ h + ζ`: the same bound plus `(73/300 + λ)ζ ≤ 2ζ`.

In particular, at `λ = 0` and `d ≤ h`, `E(d) − Δ ≤ −7/96 − Δ`.

*Proof.* With `R = 1 − δ + λ`, the two lines of eq:common-high-exponent agree (gate A1) and give the exact identity (gate A7)

`E(d) − Δ = (−1/48 − δ/16 − Δ) + (q − δ/2)/6 + (13/16)λ + (d − h)(33/50 − δ/2 + λ)`.

* The second term is `≤ 0` because `q ≤ δ/2`. The amplitude cap comes from Lemma 19.1 (uniform for `a ≤ 1`) via 15064-15090.
* The slope `S = 33/50 − δ/2` lies in `[4/25, 73/300]` on `[5/6, 1]` (gate A9). So the last term is `≤ 0` for `d ≤ h` and `≤ (73/300 + λ)ζ` beyond `h`. ∎

Gates A10 and A11 check both claims as exact vertex maxima: the expressions are multi-affine, so the maximum over a box is attained at a vertex. Gate G2 sweeps 2,838 exact rational points, including the corners.

| corner | `δ = 5/6` | `δ = 1` |
|---|---|---|
| `Δ = 0` | `−7/96` | `−1/12` |
| `Δ = 1/8` | `−19/96` | `−5/24` |

(gate A12). The worst case over the whole range is `−7/96`, at `δ = 5/6`, `Δ = 0`.

**Comparison with the balanced bins.** For every `δ ∈ [5/6, 1]` and `Δ ∈ [0, 1/8]`,
`−1/48 − δ/16 − Δ ≤ −(51/64)Δ − 7/96` (gate A13).
So every high bin keeps more than `m_hi = (51/64)Δ ≥ m_high`, with a fixed extra `7/96`. The balanced bins have only `49/440640 + (51/64)Δ` (U27).

### 2.3 How Sec. 20 reads with P1F.1-P1F.2

These are literal edits. Each instantiates a statement the paper already makes.

| Edit | Where | Change |
|---|---|---|
| E1 | 6812-6819, 15097-15100, 15498-15503 | `β* ≤ 1` (386-387) in place of Thm 3.1; `0 < Δ ≤ 1/8`; `κ ∈ (3/4, 1]`. |
| E2 | 6825, 15107 | bin ceiling `δ ≤ κ ≤ 1`; bins with `δ ≥ α` exist only when `Δ > 1/24`. |
| E3 | 15104-15106 | "Since `κ < 1` …" becomes "if `κ < 1` the hypothesis holds with equality; if `κ = 1` (`Δ = 1/8`) Lemma 18.1 needs none". |
| E4 | 15928-15946 | "At the live upper endpoint `δ = α`" becomes "For every retained bin with `α ≤ δ`": Lemma P1F.1, then P1F.2 at `d = h`. |
| E5 | 16128-16168 | "For `δ = α`, use `R = 1 − δ`" becomes "for `α ≤ δ`". The intermediate paragraph (16146-16165) is applied only to `δ < α`. High bins use P1F.1-P1F.2 at every `d ∈ [d_min, h + ζ]`. |
| E6 | 16233, 16241, 16269 | "the equality `δ = α`" becomes "bins with `δ ≥ α`"; `κ ∈ [3/4, 1]`; "`δ ≤ 1`". |

No edit changes a lemma statement, and no edit adds an analytic input. E4-E5 are the "extended endpoint count" of the verdict.

## 3. The final contradiction for Δ ∈ (0, 1/8]

### 3.1 Prop 2.1 and Thm 1.1

* **Prop 2.1** (400-502) needs `σ_0 = 7/8 < β*`, `0 < ω < Δ_0 = Δ` and `σ > 0`, chosen before the target. It never uses an upper bound on `β*`. Its last step picks a target with a zero at `Re ρ > β* − ε_*`, which exists for any `β* ∈ (7/8, 1]`, including a supremum `β* = 1` that is not attained.
* **Prop 20.3** supplies `ω = Δ/2` and `σ = m/2` with `m = (1/4) min{m_high, m_w, m_z, m_P} > 0` for every `Δ > 0`.
* **The final paragraph** (16454-16463) then gives `β* ≤ 7/8`, and Prop 11.3 transfers this to all finite-order Hecke and Dirichlet L-functions. Neither step uses `Δ ≤ 1/24`.

### 3.2 The order of choices (Prop 20.3, 16196-16453)

Every quantity in SEP30_DETECTOR_QUANTIFIERS §6.2 was re-read with `Δ ∈ (0, 1/8]`.

| Quantity | Depends on | Effect of `Δ ≤ 1/8` |
|---|---|---|
| `m_lo = Δ`, `m_hi = 51Δ/64`, `m_small = 63/800` | `Δ`, geometry | none |
| `m_high = min{m_hi, m_small}` | the two above | equals `m_hi` iff `Δ ≤ 42/425`, and `m_small` above that (A17). The literal "`m_high = 51Δ/64`" in the detector note holds only for `Δ ≤ 42/425` (FC6). The paper's min is correct throughout. |
| high-bin margin | Sec. 2.2 | `≥ 7/96 + Δ > m_high`; it needs no allocation of its own beyond the shared `< m_high/8` losses |
| moment losses, capacity decrement (`< m_high/8`) | `m_high`, coefficient bounds | coefficients bounded as before; for high bins the row loss enters as `(13/16)λ` |
| `η_mesh` (Lemma 18.1) | losses, ranges | uniform on `κ ∈ [3/4, 1]` (12573); read 16241 as `[3/4, 1]` |
| `b_round`, `K`, `ℓ_i = ℓ/K` | `m_high`, `η_mesh` | `δ max_i w_i ≤ 2ℓ/K` needs only `δ ≤ 1` (16269) |
| `κ_P = 7/(96K)` | `K` | none |
| `e`, `ϑ`, `ε` | `m_high`, `m_w`, `m_z`, `m_P` | none |
| `ζ < min{1/48, m_high/16}` | `m_high` | the high-bin slope is `≤ 73/300 < 2` (A9) |
| `z_∞` | `ζ`, `m_high` | none |
| `ω = Δ/2`, `σ = m/2` | as above | positive for every `Δ > 0` |
| `τ_{0,η}`, `τ_η`, `N_η`, `Z_0` | target stage | none |

No parameter is chosen in a way that depends on `Δ ≤ 1/24`. All pretarget choices already depend on `Δ` (16324, "All these choices depend only on `Δ` and the pretarget slot system"). That is allowed, because `β*` is a fixed number and Prop 2.1 only needs `ω`, `σ` to be independent of the target.

The junction quantities that depend on `Δ` were re-run on `Δ ∈ (0, 1/8]` (Sec. 6, J1): the Lemma 18.1 instance condition (P1), the plain capacity (P3, P5), the `Δ/4` comparison (K1, B2e), the zero-capacity case (C6), `R_* + Δ/4 ≤ 139/96` (E5) and the adaptive endpoint (E11). All pass. The only failure is P2, the literal `κ ≤ 5/6`, which is the bound this route replaces.

### 3.3 Equal slots versus Lean's distinct slots

* **The paper's equal slots survive.** The paper takes `K` equal lengths `ℓ/K` with disjoint profile supports `I_i ⊂ (1, 2)` (16246-16261). That makes the prime windows disjoint for every `Z`. `K` depends on `Δ` only through `m_high`. Nothing in this construction uses `Δ ≤ 1/24`.
* **Lean's distinct lengths do a different job.** Lean asks for pairwise distinct `ℓ_j` (`HighData.slots_injective`). Its use is `RayPoolDisjoint.power_pools_eventually_disjoint`: prime pools at distinct power scales `Z^{ℓ_j}` are eventually disjoint. This is an alternative disjointness device, replacing the `I_i`.
* **Lean's Δ-dependence is a loss budget.** Lean's `t < Δ/4` with `ℓ_j ≤ t/200` plays the role of the paper's "losses below `m_high/8`".
* **Conclusion.** The Lean change is not forced by `Δ ≤ 1/8`, and the paper's equal-slot order of choices survives unchanged.

## 4. Verdict and the resulting node set

**Verdict (A), PROPOSED; bounded review.** Part II as written, plus the extended endpoint count written out here (Lemmas P1F.1-P1F.2 with edits E1-E6), proves the 7/8 statement of Thm 1.1 from `β* ≤ 1`. This is a Part-I-free paper route. Specifically:

* **No step needs `Δ ≤ 1/24`, `κ ≤ 5/6` or `δ ≤ 5/6` once high bins are routed to P1F.1.** The one exception is U1, the bootstrap sentence itself. The only text that fails when misapplied is U29, which the route does not apply to high bins.
* **No new analytic input.** P1F.1 uses Prop 8.3 at `t = 3/2`, Remark 19.3 and Lemma 17.6, exactly as the paper does at `δ = α`. P1F.2 is exact algebra.
* **The order of choices survives as written,** with equal slots.

**Load-bearing node set.** The starting point is the 65 nodes of SEP30_VERIFICATION_MAP.

* **Leave (8):** Thm 3.1 (A), Lemma 5.8 (U), Lemma 6.1 (U), Lemma 6.2 (U), Prop 6.3 (A), Lemma 9.1 (U), Prop 9.2 (U) and Prop 11.2 (A). This is the same set that leaves under the Oct 5 substitution (PART1_SUBSTITUTION §3.1). The imports BGL and Huxley/Baier-Bansal leave with them. Def 5.6 stays, through Lemma 5.7.
* **Stay (57):** as in the substitution column of the v2 map: R 43, Rp 5, I 5, A 4. The four A nodes are Lemmas 4.2, 4.3, 4.4 and 17.1. Their ranges widen (`a`, `κ`, `δ`, `Δ` up to 1, 1, 1, 1/8), and every one of them is stated for the wider range (Sec. 1, second table).
* **New obligations:**
  1. **`β* ≤ 1`.** This is stated at 386-387 and immediate from the definition. It is not a new node.
  2. **Remark 19.3** (15448-15467) becomes load-bearing; the v2 map listed it as not load-bearing. Bounded check here: its derivation (15248-15294) uses no `δ ≤ α`.
  3. **Lemma P1F.1** (Sec. 2.1), PROPOSED. It is a two-case inequality on top of Prop 8.3 and Remark 19.3.
  4. **Lemma P1F.2** (Sec. 2.2), PROPOSED. It is exact algebra on eq:common-high-exponent (gates A7-A13, G2).
  5. **The junction box widened to `Δ ≤ 1/8`.** Replayed here (J1).

**Comparison with the Oct 5 substitution.**

| | Paper as written | Oct 5 substitution | Part-I-free route (this note) |
|---|---|---|---|
| source of the bootstrap | Thm 3.1 + 7 Part I nodes | [O5] thm:main (imported) | `β* ≤ 1` (386-387) |
| `Δ`, `κ`, `δ` ceilings | `1/24`, `5/6`, `5/6` | `1/24`, `5/6`, `5/6` | `1/8`, `1`, `1` |
| Sep 30 numbered nodes on path | 65 | 57 | 57 + Remark 19.3 |
| new or imported material | none | [O5] thm:main and its proof chain; weakest point prop:R | Lemmas P1F.1-P1F.2 (about one page, here) |
| correlated risk | — | [O5] prop:R shares the cubic reflection input with Prop 5.1 | none added: P1F uses only Part II's own detector and moments |
| Lean analogue | none | none | `CountParameters.high`, `high_mixed_margin` |

The new route needs no imported 11/12 theorem. Under this route, the 11/12 result (Part I, or Oct 5) is no longer a dependency of 7/8 at all.

## 5. Lean correspondence for the (b) items

| Paper item | Lean declaration | Match |
|---|---|---|
| U1, E1: `β* ≤ 1` | `HeckeZeroSupremum.beta_le_one`; `FinalAssemblyHigh.lean:115` (`hΔ1 : beta − 7/8 ≤ 1/8`) | same input |
| U3, U11: bin split at 5/6 | `ProbeFinalAssembly.CountParameters.balanced` (`2a−1 ≤ 5/6`, `0 ≤ Δ ≤ 1/8`) and `.high` (`5/6 < 2a−1`, `a ≤ 1`, exponent `1−δ+78ε+ε_m`) | same split |
| U24, P1F.1 | `HeckeDetectorHighCount.high_count_from_raw_moments` (fiber at `tstar = 3/2`), `HeckeDetectorNoSlotInverseCount.no_slot_inverse_count`, `HeckeDetectorRowCount.high_bin_count`, `HeckeDetectorWitnessRows` field `inverse_length_lower` | same two cases; Lean's `γ = 76ε` is the paper's `O(ε)` |
| P1F.2 at `d = h` | `HeckeDetectorRowCount.high_bin_endpoint`; `ProbeCentralExponent.high_source_margin` (`−1/48 − δ/16 − Δ + (13/16)loss + 2ζ`) | identical bound (A7-A8) |
| U28, U35: all `d ≤ h + ζ` | `ProbeCentralExponent.relative_extend`, `frequency_slope_bounds` (`δ ≤ 1`, `R ≤ 139/96`), `ProbeHighRowFamily.high_mixed_margin` (`5/6 ≤ δ ≤ 1`, no bound on `Δ`) | same constants 4/25, 139/96 |
| U29 | `ProbeCentralExponent.intermediate_source_margin` (`δ ≤ 5/6`) | balanced only, as here |
| U31 | `Parameters.HighData` (`t < Δ/4`, distinct slots) | different disjointness device (Sec. 3.3) |

These are statement-level comparisons of the declarations named. No Lean proof was replayed here; the formal status is that of SEP30_LEAN_CORRESPONDENCE.

## 6. Checks run, and what they authenticate

`python3 -I reviews/part1_free_checks.py <paper.tex> --replay-junction` exits 0 when all of the following hold.

| Group | Result | What it authenticates | What it assumes |
|---|---|---|---|
| T0-T4 text | 5/5 | hash; 32 anchor strings at the cited lines; census of 282 Part II lines (153 substantive, each in exactly one item U1-U37); Thm 3.1 cited once in Part II (6812); Remark 19.3 unlabeled | that the census regexes and notation filters catch every relevant use. Uses phrased only in words (e.g. "the bin ceiling") are found through the labels and by reading, not by the regex. |
| A1-A22, A15a algebra | 23/23 | exact identities (sympy over Q) and exact vertex maxima of multi-affine expressions: the count inequality, the margin identity and its sign over the whole range, the corners, the dominance over `m_hi`, the `Δ/4` comparison for `Δ ≤ 1/8`, 139/96, the `m_high` switch at `42/425`, the `κ` range, the contour ranges | the transcription of the paper's formulas (eq:common-high-exponent, eq:no-slot-inverse-count) |
| G1-G2 grid | 2/2 | exact rational sweep (sanity, not a proof) | — |
| FC1-FC10 controls | 10/10 fire | each removes one restriction and produces an exact counterexample: `δ < 5/6` (FC1); no `t = 3/2` witness (FC2); the `t = 1` count in a high bin, `E(h) = 11/72` (FC3); the intermediate count in a high bin, `+1/25` at `δ = 1` (FC4); `Δ > 1/8` breaks 139/96 (FC5); the literal `m_high = 51Δ/64` (FC6); no subtraction of `Δ` (FC7); `κ ≤ 5/6` (FC8); `a > 1` leaves region one (FC9); the 73/300 slope at `δ = 1` (FC10) | — |
| S1a, S1-S2 sensitivity | S1a 1/1; S1-S2 informational | S1a is the exact identity behind S1; S1-S2 see below | — |
| J1 junction replay | 1/1 (inner: 83/84, only P2 fails, as expected) | sep30_junction_check.py (SHA-256 30573564aa1a8910ab2bececbb678cd528fc397da80c4ab8c5fcb30875d24efc) re-run in a temporary copy with every `Δ` box `(0, 1/24]` widened to `(0, 1/8]`. Its exact gates, including the branch-and-bound gates P1, P3, P5, K1, C6, E5 and E11, pass on the wider box. P2 (`κ ≤ 5/6`) fails, as designed, and all 8 of its failing controls still fire. | the junction script's own scope (quantitative hypotheses only) |

**The two suggested controls that do not fail.** The brief suggested "drop the amplification" or "use `e(r) = 1`" as failing controls. On `[5/6, 1]` neither fails, and this is reported as such.

* **S1, no amplification.** Use the raw moment eq:raw-moment (exponent `max{1, r}`) instead of Lemma 17.6. At `t = 3/2` the count is `R = (3/2)(1 − δ)`, and `E(h) = 37/96 − 15δ/32`. This is still `≤ −1/192` on `[5/6, 1]`; it vanishes at `δ = 37/45 < 5/6`. So the amplification is not needed for the sign in the high range. It only enlarges the margin, from `1/192` to `7/96` at `δ = 5/6`. This is a robustness observation about the high bins only. In the balanced range the amplified long count `L(t)` is still used.
* **S2, `e(r) = 1`.** This replaces the moment by a stronger, unproven one, so it can only lower the count. It is uninformative.

The failing controls FC1-FC4 are the informative ones: they show that `δ ≥ 5/6`, the `t = 3/2` witness, and the use of P1F.1 at every row size are each load-bearing.

## 7. Observations on the source

These are consistent with the text having been calibrated for `Δ ≤ 1/8` and `δ ≤ 1`. They are observations, not claims about the authors' intent.

* `R_* + Δ/4 ≤ 139/96` (16141) is exactly `17/12 + (1/8)/4`. With `Δ ≤ 1/24` the same chain gives `137/96` (A16).
* The slope bound `33/50 − δ/2 ≥ 4/25` (16133) is the `δ ≤ 1` value. On `δ ≤ 5/6` the exact minimum is `73/300`, as SEP30_JUNCTION_CHECK R3 noted (A9, FC10).
* The label of the `δ = α` display is `eq:large-delta-endpoint` (15946).
* Remark 19.3 is titled "Unselected inverse witnesses beyond the Part II bin ceiling" and states the count for `δ ≤ 1` (15448-15467), although nothing in the paper as written uses it.
* Lemmas 8.1, 10.3, 10.5, 16.1, 18.1 and 19.1 are all stated for `a ≤ 1` or `κ ≤ 1` (Sec. 1, second table).

## 8. Known misreadings to avoid

1. **"The paper proves 7/8 without Part I."** No. As written, it cites Thm 3.1 (6812). The claim here is that a stated set of literal edits plus about one page of new text (P1F.1-P1F.2) gives a route that does not. That route is PROPOSED and needs its own independent review.
2. **"The extension adds new analysis."** No. P1F.1 uses only Prop 8.3 at `t = 3/2`, Remark 19.3 and Lemma 17.6, the same inputs the paper uses at `δ = α`. P1F.2 is exact algebra.
3. **"The intermediate-row paragraph covers the high bins."** No. It fails for `δ > 529/625` (FC4). High bins must use P1F.1 at every `d`.
4. **"`m_high = 51Δ/64`."** Only for `Δ ≤ 42/425`. Prop 20.3 defines `m_high` as `min{51Δ/64, 63/800}`, which is what is used.
5. **"The Lean distinct slot lengths are needed for `Δ ≤ 1/8`."** No. They are a disjointness device; the paper's equal slots with disjoint supports `I_i` serve the same purpose (Sec. 3.3).
6. **"Verdict (A) certifies the 7/8 manuscript."** No. The 57 remaining nodes keep their v2 statuses, four of them A (Lemmas 4.2-4.4 and 17.1). Nothing here bears on RH.

## 9. Reproduction

```sh
cd research/exploratory/qrh-2026-10/reviews
P=standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints
git show 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6:$P/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex > /tmp/sep30.tex
python3 -I part1_free_checks.py /tmp/sep30.tex                       # T, A, G, F, S groups (seconds)
python3 -I part1_free_checks.py /tmp/sep30.tex --replay-junction     # adds J1 (minutes; widened junction replay)
```
