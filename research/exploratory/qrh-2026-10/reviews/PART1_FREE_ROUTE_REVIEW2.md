# Second review of the Part-I-free route (PART1_FREE_ROUTE.md)

```text
Status: REVIEW (bounded adversarial second review, exploration level). Verdict: "(A) with
  corrections". No obstruction was found in the parts read. The four corrections in Sec. 8 are
  editorial or concern what a gate authenticates; none changes the route or its conclusion. This
  is not an integration record. It does not certify the Sep 30 manuscript, and it says nothing
  about RH, which is unsolved.
Scope: the target note PART1_FREE_ROUTE.md at this branch head, its script part1_free_checks.py
  (SHA-256 cdec554e...884a9c4f) and outputs results/part1_free_*. Checked: (1) the census of
  every Part II use of an upper bound on Delta, kappa, delta or beta_*; ten riskiest (a) items
  against the cited lemmas' own hypotheses; (2) the (b) items, Remark 19.3 and the extended
  endpoint count; (3) the (c) item and the case split by row size; (4) the two proposed lemmas
  P1F.1-P1F.2; (5) the final contradiction and the order of choices for Delta in (0, 1/8].
  Not checked: the proofs of the analytic lemmas Part II cites (their statuses stay those of
  SEP30_VERIFICATION_MAP_V2.md), Part I, and every Lean claim of the note (Secs. 3.3 and 5).
Exact sources or dependencies:
  [OAI] Sep 30 paper.tex at 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, standalone/2026-10-07-
        openai-quasi-riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-
        2026/build/paper.tex, SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3
        (re-hashed). External, unreviewed, read as untrusted data. Line numbers refer to this file.
  Repo notes: PART1_FREE_ROUTE.md (target), SEP30_LEAN_CORRESPONDENCE.md Sec. 4,
        PART1_SUBSTITUTION.md, SEP30_VERIFICATION_MAP_V2.md, LEMMA18_1_CASE2_SEC188.md (kappa range).
What was actually run (python3 -I, one core, no Lean/Lake/comparator process):
  1. The target script, unmodified copy in session scratch, with --replay-junction:
     32/32 gates pass, 10/10 failing controls fire, J1 inner replay 83/84 (only P2 fails, as
     designed), 8/8 inner controls fire, 13 box substitutions, 69 s. Its stdout equals the stored
     results/part1_free_checks_stdout.txt line for line apart from timing. The committed results
     files were not overwritten.
  2. New: reviews/part1_free_review2_checks.py (SHA-256 7819cce9...9a86d19e), stdlib + sympy, exact:
     14/14 gates pass, 3/3 new failing controls fire, 3 informational rows. Output
     results/part1_free_review2_output.json and results/part1_free_review2_stdout.txt.
  3. Line-by-line reading of [OAI] 363-520, 1531-1600, 4270-4686, 5800-5896, 6015-6075,
     6175-6310, 6340-6400, 6806-6860, 8600-8660, 9090-9208, 12330-12476, 12520-12600,
     12825-12910, 14985-15700, 15700-16463, and greps of all of Part II.
Smallest remaining gap: Remark 19.3 (15448-15467). It is an unlabeled remark whose only
  justification is a pointer to the derivation at 15248-15294. I re-read that derivation and agree
  that it uses no delta <= alpha (the first such use is at 15303), but the remark has never been a
  numbered result, and nothing beyond this inspection supports it. Below it sit Prop 8.3's
  saturated witness at t = 3/2 and Lemma 17.6. NC3 shows that the O(eps) saturation is
  load-bearing: a fixed witness deficit of 7/65 already breaks the high-bin margin at delta = 5/6.
```

RH is unsolved. The 7/8 statement is a zero-free half-plane `Re s > 7/8`. It says nothing about the critical line. "Reviewed" here means a bounded agent review with the scope above.

## 0. Verdict

**(A) with corrections.** I tried to break the route at the five points the brief named and found no obstruction.

* **The census is complete.** My own census, with my own regex and my own explicit list of notation lines, gives the same 153 substantive lines as the note's census.
* **The (a) items hold as written.** Every one of the ten riskiest (a) items is covered by the cited lemma's actual hypotheses for `κ ≤ 1`, `δ ≤ 1` and `Δ ≤ 1/8`.
* **The high-bin extension works.** The extended endpoint count holds uniformly on `δ ∈ [5/6, 1]`, including `δ = 1` and rows with `r` down to `1 − O(ε)`. The intermediate-row paragraph is never applied to a high bin.
* **The order of choices survives `Δ` up to 1/8 unchanged.**

The corrections (Sec. 8) are:

1. a missing bound on the loss `λ` in P1F.2;
2. a more accurate description of what census gate T2 authenticates;
3. the observation that Lemma 17.6 is load-bearing in the balanced bins, so the note's S1 row must not be read as "the amplification can be dropped";
4. a precise status for Remark 19.3.

## 1. The census, re-derived

**Method.** I grepped Part II (6806-16463) for `\beta_*`, `\beta^*`, `\beta_\ast`, `\Delta`, `\kappa`, `\alpha`, `5/6`, `\frac56`, `\tfrac56`, `\frac{5}{6}`, `1/24`, `\frac1{24}`, `11/12`, the two bootstrap labels and `eleven-twelfths`. Subscripted symbols and `\bar\alpha` are excluded by the regex. I then removed 33 lines that I read as other notation, listed by explicit line number in the script:

* weights `y^{−5/6}`;
* the Gaussian `(s−5/6)²`;
* the geometry `M = 5/6`;
* Lemma 17.6's `H^{5/6}`;
* the sixth-power constants in Lemma 18.1 (14438-14501, 14760);
* the Laplacian at 10102;
* difference operators at 14824;
* other alphas.

I also grepped for word-only uses ("ceiling", "upper endpoint", "current Part II"), for alternative spellings (`\varkappa`, `\dfrac`, `0.83`), for "small"/"close to one" phrasing near `Δ`, and for any division by `1 − κ`, `1 − δ` or `α − δ` in Part II. None adds a use.

**Result (C1-C2).** There are 186 hit lines, 33 notation lines and 153 substantive lines. The 153 lines are identical, line by line, to the set in the note's T2 output. The only citation of Thm 3.1 in Part II is at 6812.

**Lines that carry a literal bound (C3).** Thirty-one substantive lines state a literal upper bound (`≤ 5/6`, `≤ 1/24`, `≤ α`, `= α`, `κ < 1`, `[3/4, 5/6]`). My reading of each:

| Lines | Literal bound | My reading | Note's item |
|---|---|---|---|
| 6817, 6819, 6825; 15099-15100; 15501-15502 | `Δ ≤ 1/24`, `κ ≤ 5/6`, `δ ≤ 5/6` | consequences of Thm 3.1 only; replace by `Δ ≤ 1/8`, `κ ≤ 1`, `δ ≤ κ` | U2, U3, U11, U19 |
| 12564, 12833, 12896 | `κ < 1` | case split inside Lemma 18.1; `κ = 1` has its own clause (12565, 12893-12895) | U7, U9 |
| 15104, 15107-15108 | "Since `κ < 1`"; `δ ≤ κ ≤ α` | false for `Δ > 1/24` as written; this needs edits E3 and E2 | U11 (b) |
| 15188, 15303, 15949, 15978, 15995, 16003, 16128, 16146 | `δ ≤ α`, `δ < α`, `δ ≤ 5/6` | hypotheses of Prop 19.2, Lemma 20.2 and the balanced and intermediate paragraphs; a high bin never enters them in the route | U13, U14, U25, U26, U28, U29 |
| 15464 | "requires neither `δ ≤ α` …" | Remark 19.3, the enabling statement | U18 |
| 15928, 15988, 16129, 16143, 16166, 16233 | `δ = α` | the endpoint case; read as `δ ≥ α` (edits E4-E6) | U24, U28, U29, U31 |
| 16165 | "uses `δ ≤ 5/6`" | the (c) item; Sec. 4 | U29 |
| 16241 | `κ ∈ [3/4, 5/6]` | the mesh is uniform on `[3/4, 1]` (12571-12573) | U32 |
| 16269 | `δ ≤ 5/6 < 1` | only `δ ≤ 1` is needed, and only selected (balanced) rows use it | U33 |

The note's classification of these lines agrees with mine.

**What gate T2 authenticates (NC1, NI1, NI2).** T2 assigns lines to items by line range, not one line at a time. Its notation filter also strips `\tfrac56` and `−\frac56(M|δ)` wherever they occur.

* A bound planted as `\delta\le\frac56` on line 10000 makes T2 fail. That is NC1, and it fires.
* The same bound spelled `\delta\le\tfrac56` passes T2 (NI1).
* `\Delta\le\frac1{24}` planted on line 13500, inside item U10 (12932-14906, about 2,000 lines), also passes T2 (NI2).

So T2 shows coverage by ranges. That T2 nevertheless missed nothing rests on the reading, mine included. This is correction 2.

## 2. Ten riskiest (a) items, checked against the cited lemma's hypotheses

| # | Item (note) | What could hide a `Δ ≤ 1/24` assumption | Cited statement and its actual range | Result |
|---|---|---|---|---|
| 1 | U7-U8, E3: Lemma 18.1 at `κ ∈ (5/6, 1]` | zero-free shift at `s_κ = β*`; `κ = 1` | "Let `3/4 ≤ κ ≤ 1`" (12532); "If `κ = 1`, no zero-free hypothesis" (12565); proof by absolute prime counting, `\|Q\| ≤ P^{1/2}` (12893-12895) | holds |
| 2 | U9-U10: Lemma 18.1 internals | constants tuned to `κ ≤ 5/6` | `z ≤ M/(6κ) ≤ 2M/9` uses `κ ≥ 3/4` (12932); `6κ−1 ≥ 7/2` (12949); `0 ≤ 6κ−1 ≤ 5` uses `κ ≤ 1` (14827); losses uniform on `[3/4, 1]` (12897-12898). LEMMA18_1_CASE2_SEC188 checked these on `[3/4, 1]` with a `κ = 11/10` control. | holds |
| 3 | U16: capacity comparison `≤ Δ/4` | the bound might need small `Δ` | uses `m ≥ 1/3`, `2q ≤ 1` and both denominators `≥ 4` (15398-15405). Exact: the increase is at most `(1000/1269)(Δ/4)` at `Δ = 1/1000` and decreases in `Δ` (X11). | holds for all `Δ ≥ 0` |
| 4 | U22: Lemma 10.3/10.4 contours with `a`, `β*` up to 1 | region one at `Re w = 1 − a − 6e`; `s` on `β* + 20e` | hypotheses are `σ_0 ∈ [7/8, 1)` and `β* > σ_0` (5810-5811, 6024-6025). `Re w ≥ −6e > −1/100` (5857). The `s` move to `β* + 20e` (5841) has no upper limit. | holds |
| 5 | U20: principal signal at `β* = 1` | `Re s = β* + e` beyond 1 | Lemma 10.5 requires `β* > σ_0` only; "This also covers `β* = 1`" (6300); the slot errors `ρ_i` need `x_r ≥ 7/8` only. | holds |
| 6 | U6, U23: small rows on `Re s = β* + e` | Euler region and local exponents | region one with `ε_0 = 3/8` needs only `β* ≥ 7/8` (9134); the exponents decrease in `x_r` (9139-9168). Lemma 10.6's hypotheses are `σ_0 ∈ [7/8, 1)` and `β* > σ_0`. `m_small = 63/800` has no `β*` in it. | holds |
| 7 | U13-U14, U25: Prop 19.2 with dynamic `κ ≤ 1` | supply margin, plain capacity | the inverse capacity `≤ 7/37` uses `r_* ≥ 23/37` (no `κ`); the plain capacity `≤ 2/27` uses `κ ≥ 3/4`; supply is `8/39 − 7/37 = 23/1443`; the decrements are "chosen using only `ε`, `Δ`" (15197-15199) | holds |
| 8 | U26-U27: Lemma 20.2 and eq:adaptive-endpoint | certificate tuned to `Δ` | the certificate (15994-16072) contains neither `κ` nor `Δ`. `Δ` enters only through `hΔ/4 − Δ = −(51/64)Δ` (16098-16101). | holds |
| 9 | U32-U33: `η_mesh`, `K`, `b_round`, pool | slot count or pool chosen with small `Δ` | `η_mesh` is uniform on `[3/4, 1]` (12571-12573); `2ℓ/K < min{η_mesh, b_round, 1/185}` (16246-16249); `1/185` comes from the supply gap, not from `Δ`. Pool `ℓ_* = σ_width/3` is internal to Lemma 18.1. `δ max w_i ≤ 2ℓ/K` needs `δ ≤ 1` (16265-16269). | holds |
| 10 | U30-U31: margins `m_hi`, `m_high`, `ζ`, `z_∞` | the `63/800` term; the `ζ` budget | `m_high := min{51Δ/64, 63/800}` (16223). With `Δ ≤ 1/24` the minimum is always `m_hi`; it switches only at `Δ = 42/425`. `ζ < min{1/48, m_high/16}` (16328) works because the high-bin slope is `≤ 73/300`. `z_∞` is chosen against `m_high` (16331-16334). "The other endpoint ranges have nonpositive ideal exponents" (16178-16179) holds for high bins: `−1/48 − δ/16 < 0`. | holds |

**Also checked.**

* Prop 8.3 and Lemma 8.2 up to `δ = 1`. The lower bound `(DN)^{2σ−1} ≥ U^{δ(r+m)}` uses `σ ≥ a` (4662). Saturation `m ≤ 1/2 + O(ε)` uses `δ ≥ 1/50` only (4675), so its constant is absolute. The Gamma exponent `−189/100` uses `σ ≥ 51/100`.
* Lemma 19.1 ("uniform for `51/100 ≤ a ≤ 1`", 15023).
* Lemma 4.9 (`a ∈ [1/2, 1]`; global clause for `b > 1`, 1591-1594).
* Prop 2.1 (needs only `Δ_0 > 0`; 400-502).
* The low estimate (8647-8648: no upper bound on `β*`).

**Calibration.** No constant in Part II was chosen with `Δ ≤ 1/24` in mind. No "for `Δ` small" phrasing occurs. Three constants are calibrated for the wider range, as the note says (its Sec. 7):

* `139/96 = 17/12 + (1/8)/4`;
* the slope `4/25 = 33/50 − 1/2`;
* the minimum in `m_high`, which is redundant when `Δ ≤ 1/24`.

## 3. The (b) items: Remark 19.3 and the extended endpoint count

**Is Remark 19.3 proved?** Only by reference. It is an unlabeled `remark` environment (15448-15467). Its justification is one sentence: the derivation of eq:no-slot-inverse-count "uses only the inverse spike from Proposition 8.3 and Lemma 17.6". I re-read that derivation (15248-15294):

* Lemma 17.6 is applied to the common base profile `W_base`, with `c` and `ε_0` chosen in terms of `R_0` (15268-15280).
* Dividing by the spike `\|M_r\|² ≫ U^{δr−ε}` then gives the count.
* The case display (15286-15292) is the identity `(1+5r)/6 − δr = 1 − α + (α − δ)r`, valid for every `δ` (X2).

The hypothesis `δ ≤ α` first appears at 15303, in the next paragraph. So the remark is correct as an observation. Its status can be no better than that of the Prop 19.2 derivation it points to (Rp in the v2 map) together with Prop 8.3 and Lemma 17.6 (both R). That is correction 4.

**Uniformity on `[5/6, 1]`.**

* The remark states the range `1/50 < δ ≤ 1` and `a > 51/100` (15457-15459), so `δ = 1` is included.
* Rows with `r < 1` use `e(r) = 1`. The count excess over `1 − δ` is then `δ(1 − r) ≤ δγ`, where `γ = c_0ε` is the witness deficit and `c_0` is absolute (4675).
* At `δ = 1` and `r = 1 − 76/1000`, the excess is exactly `76/1000`, attained on the `r < 1` branch (X3). This is `O(ε)` and is absorbed into `ε`.
* For `r ≥ 1` the excess is `(5/6 − δ)(r − 1) ≤ 0`, with no upper limit on `r` needed (X2).

**Exact margin, re-derived (X1, X4-X6).**

* From the first line of eq:common-high-exponent (15726-15730), with `a = (1+δ)/2`, `R = 1 − δ + λ` and `q = xδ`:

  `E(d) − Δ = −1/48 − δ/16 − Δ + dλ + (x − 1/2)δ/6 + (d − h)(33/50 − δ/2)`.

  The note writes the loss term as `(13/16)λ + (d − h)λ`, which is the same thing.
* Both correction terms are `≤ 0` on `δ ∈ [5/6, 1]`, `x ∈ [0, 1/2]`, `d ∈ [1/100, h]` (exact vertex maximum 0).
* The corners are `−7/96`, `−19/96`, `−1/12` and `−5/24`. The worst is `−7/96`, at `δ = 5/6`, `Δ = 0`.

All of this agrees with the note.

**The note's S1 row (no amplification).** Recomputed, `E(h) = 37/96 − 15δ/32`. It equals `−1/192` at `δ = 5/6` and vanishes at `37/45 < 5/6` (X10).

* So, for the sign in high bins, the amplification is indeed unnecessary. This is consistent with the paper: at `δ = α` it uses the amplified count (15931-15941) but never claims the amplification is needed there.
* It is not true that Lemma 17.6 can be dropped from the route. **NC2** replaces the amplified long count by the raw one in a balanced bin (slope `1 − δ` instead of `5/6 − δ`) and re-balances `t`. The result is `E(h) − Δ = +6167/1585200 ≈ +0.0039` at `δ = 23/50`, `x = 1/2`, `Δ = 0`; it is still positive at `Δ = 1/1000`. The amplified count gives `−101/74400` at the same point.
* Without amplification, the balanced margin returns only for `Δ > 0.0049` (NI3), so no proof that is uniform as `Δ → 0` survives.

So Lemma 17.6 remains load-bearing in the balanced bins and stays in the node set. This is correction 3.

## 4. The (c) item: the intermediate rows

The paper's intermediate paragraph (16146-16165) has the hypothesis "`d_min ≤ d ≤ 1/2` and `δ ≤ α`" in its first sentence.

* Its display recomputes exactly to `E(1/2) = −529/2400 + 25δ/96` (X8).
* That value is `−49/14400` at `δ = 5/6`, vanishes at `δ = 529/625`, and is `+1/25` at `δ = 1`. So it must not be used for a high bin.

**The case split in the route.**

| Row norm `U = Z^d` | Floor bin `a = 51/100` | Balanced `1/50 < δ < α` | High `α ≤ δ ≤ κ` (route) |
|---|---|---|---|
| `d < 1/100` | small rows, Lemma 10.6; saving `63/800` relative to `C(β*)`, no bins | same | same |
| `1/100 ≤ d ≤ 1/2` | `R = 1`; positive slope | `t = 1`, no slots, `R = 76/75 − 2δ/3` (16146-16165) | P1F.1: `t = 3/2`, no slots, `R = 1 − δ`; slope `33/50 − δ/2 ≥ 4/25`, so `E(d) ≤ E(h)` |
| `1/2 < d ≤ h` | same | selected primes, `R = R_* + Δ/4` (16128-16129) | same P1F.1 count |
| `h < d ≤ h + ζ` | slope `< 2` | slope `≤ 139/96 + 1/2 − 17/50 < 2` | slope `≤ 73/300 + λ` |
| `d > h + ζ` | large rows, `z_∞` | same | same |

* **High bins never use the intermediate paragraph.** The paper already routes `δ = α` this way: "At `δ = α`, the count used in eq:large-delta-endpoint and its positive slope already control every `d ≤ h`" (16166-16168).
* **The `t = 3/2` count is valid at every `d` with `d ≥ 1/100`.** Its height hypothesis `(1 + T_1)^A ≤ U^{ε/10}` is enforced by `τ_{0,η}` for `U ≥ Z^{d_min}` (15476-15489), the same as for the balanced bins.
* **The saving criterion (16348-16351) holds for high bins.** Relative to `C(7/8)`, their exponent is already below `−1/48 − δ/16` before `Δ` is subtracted.

## 5. The two proposed lemmas

**P1F.1 (high-bin row count).**

* *Statement.* It is correctly quantified: a fixed presentation/dyadic subdivision, witnesses from Prop 8.3 at `t = 3/2`, and the loss and height hypotheses of Lemma 8.2.
* *Proof.* It is Remark 19.3 plus the two-case inequality of X2-X3. It needs no prime slot, no plain moment and no `κ`.
* *What is new.* The analysis is not new; the statement is. It applies an unlabeled remark to bins that the paper as written never forms.

**P1F.2 (high-bin margin).** This is exact algebra and correct, with one omission. The second bullet claims `(73/300 + λ)ζ ≤ 2ζ`, which holds only for `λ ≤ 527/300` (X7). The statement says only `λ ≥ 0`. This is harmless because `λ` is an arbitrarily small loss, but the hypothesis should say so (correction 1).

**Do they need review?** Yes. Under AGENTS.md, a new composition of arguments needs its own review even when each step is elementary. This note is one bounded independent review of that composition at the head named above. It does not integrate the composition.

## 6. The final contradiction for Δ ∈ (0, 1/8]

**Prop 2.1.** It needs only `σ_0 = 7/8 < β*` and `0 < ω < Δ_0 = Δ`.

* With `ω = Δ/2` and `σ = m/2`, `ε_* = min{Δ/2, m/2} > 0`.
* The final step picks a target with a zero at `Re ρ > β* − ε_*`. Such a target exists by the definition of the supremum, also when `β* = 1` is not attained (400-502).

**Order of choices (Prop 20.3, 16219-16453).** In order:

1. `Δ` is fixed, since `β*` is a fixed number.
2. Then `m_lo`, `m_hi` and `m_high`, and half of each margin is reserved.
3. The moment losses and capacity decrement, costing `< m_high/8`.
4. `η_mesh`, uniform on `[3/4, 1]`.
5. `b_round`.
6. The even `K`, with equal slots `ℓ_i = ℓ/K` and disjoint supports `I_i ⊂ (1, 2)`.
7. `κ_P = 7/(96K)`.
8. The amplitude width, the powers and `e`.
9. `ζ`, then `z_∞`.
10. `m = (1/4)min{m_high, m_w, m_z, m_P}` and `ω = Δ/2`.
11. Only then the target, `τ_η`, `N_η` and `Z_{0,η}`.

Every pretarget choice may depend on `Δ` (16324), and each `ε` is chosen after `Δ`. Nothing here requires `Δ ≤ 1/24`:

* at `Δ = 1/8`, `m_high = 63/800` and each step is still well defined;
* the equal-slot construction does not mention `Δ` except through `m_high`.

I did not check the note's Lean comparison of slot devices (its Sec. 3.3).

## 7. Runs and controls

| Run | Result | What it authenticates | What it does not |
|---|---|---|---|
| Target script, `--replay-junction` (copy, scratch) | 32/32 gates, 10/10 controls; J1 83/84 with only P2 failing, 8/8 inner controls; stdout identical to the stored one apart from timing | the reported counts; the stored outputs come from this script | the census regex and ranges (see NC1, NI1-NI2); the transcription of the paper's formulas |
| C1-C3 (new) | 153 substantive lines, equal to the note's set | an independent census with explicit notation lines | uses phrased only in words beyond the greps listed in Sec. 1 |
| X0-X11 (new) | 14/14 | the hash; the exact identities and vertex maxima of Secs. 3-4, written from the TeX | the analytic lemmas |
| NC1 (new) | fires: T2 fails on a planted `\delta\le\frac56` at line 10000 | T2 does detect an out-of-range use | — |
| NC2 (new) | fires: an unamplified balanced count gives `E(h) − Δ = +6167/1585200` at `Δ = 0` | Lemma 17.6 is load-bearing in balanced bins | — |
| NC3 (new) | fires: a fixed witness deficit `γ = 1/8` gives `E(h) = +3/256` (`δ = 5/6`) and `+7/384` (`δ = 1`); the tolerated deficit is `7/65` and `4/39` | the `O(ε)` saturation of Prop 8.3 is load-bearing for P1F.1 | — |
| NI1-NI3 (informational) | `\tfrac56` spelling and range absorption pass T2; Δ threshold `≈ 0.0049` for NC2 | limits of T2; size of NC2 | — |

## 8. Corrections to PART1_FREE_ROUTE.md

1. **P1F.2 (Sec. 2.2), second bullet.** Add `λ ≤ 527/300` (for example `0 ≤ λ ≤ 1`), or state the extension cost as `(73/300 + λ)ζ` without the `≤ 2ζ`.
2. **Secs. 1 and 6, gate T2.** Replace "every substantive line lies in exactly one item" by "every substantive line lies in exactly one item's line range". Add that the notation filter strips `\tfrac56` globally, so the absence of a missed use rests on reading. This review's explicit-line census (C2) finds the same 153 lines.
3. **Sec. 6, S1.** Add that the amplification is needed in the balanced bins (NC2), so Lemma 17.6 cannot be dropped from the node set. "The amplified long count `L(t)` is still used" should read "is needed".
4. **Sec. 4, Remark 19.3.** Record that it is an unlabeled remark justified only by reference to 15248-15294, and give it a status no better than Rp, the status of the Prop 19.2 derivation it points to. The note's other claims about it (load-bearing; uses no `δ ≤ α`) are correct.

None of these changes the verdict, the node set (57 nodes plus Remark 19.3) or the margins.

## 9. Known misreadings to avoid

1. **"This review confirms the 7/8 theorem."** No. It confirms that, in the parts read, the Part-I-free composition is no weaker than Part II as written. The 57 remaining nodes keep their v2 statuses, four of them A. [Dated note: under map addendum v2.1 they keep their v2.1 statuses, 6 Rp and 2 I, with no A.]
2. **"Remark 19.3 is a proved lemma of the paper."** No. It is a remark whose correctness rests on inspecting a derivation inside Prop 19.2.
3. **"The amplification is unnecessary."** Only for the sign in the high bins. It is needed in the balanced bins (NC2).
4. **"T2 proves the census complete."** No. T2 checks coverage by line range; completeness rests on the reading (NC1, NI1, NI2).
5. **"The intermediate display covers `δ ≤ 1`."** No. It covers `δ ≤ 5/6`, and is positive beyond `529/625`.

## 10. Reproduction

```sh
cd research/exploratory/qrh-2026-10/reviews
P=standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints
git show 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6:$P/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex > /tmp/sep30.tex
python3 -I part1_free_review2_checks.py /tmp/sep30.tex      # under 1 s; reads results/part1_free_checks_output.json for C2
```
