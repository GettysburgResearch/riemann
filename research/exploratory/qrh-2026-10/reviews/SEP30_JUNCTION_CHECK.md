# Row-count junction of the 30 Sep 2026 OpenAI 7/8 manuscript: exact hypothesis check

```text
Status: EXPLORATORY review instrument (bounded; external, unreviewed manuscript). Exact-rational
  verification of the QUANTITATIVE hypotheses at every lemma invocation in the row-count junction
  (target 3 of SEP30_VERIFICATION_MAP.md). This is not a verdict on any analytic lemma, and it is not
  an integration record. RH is unsolved; nothing here bears on it directly.
Scope: paper.tex lines 15015-15062 (Lemma 19.1), 15095-15184 (selection prose), 15185-15446
  (Prop 19.2), 15920-15993 and 16073-16111 (endpoint prose), plus the frequency-range lines
  16114-16126 where the mesh and supply for d in [1/2, h+zeta] are stated. Hypotheses were read from
  the statements of Prop 8.3 (4510-4545), Lemma 8.2 (4385-4404), Lemma 17.1 (9250-9269),
  Lemma 17.2 (9296-9340), Lemma 17.6 (12362-12392), Lemma 18.1 (12531-12579) and Lemma 19.1
  (15015-15025). Qualitative hypotheses (coefficient classes, Theta membership, rowwise test
  parameters, seminorms, heights) are listed, not verified.
Exact sources or dependencies:
  [OAI] paper.tex at pr908 (31c706bb), standalone/2026-10-07-openai-quasi-riemann-import/upstream/
        preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
        SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (rechecked by the
        script, together with 17 label anchors at the cited lines). Read as untrusted data.
  Our model: scripts/threshold_calculus.py (float cross-check only). Prior replay: PR910_REPLAY.md
  (Lemma 20.2 certificate). Hypotheses of 18.1: LEMMA18_1_REVIEW.md.
What was actually run:
  nice -n 10 python3 -I reviews/sep30_junction_check.py <paper.tex>   (one process, about 3 min)
  -> 84 exact gates (22 sympy identities over Q, the rest Fraction branch-and-bound or exact
     rational arithmetic), 8 failing controls, 1 float cross-check (not a gate). Output:
     reviews/sep30_junction_check_output.json. Final run: 84/84 gates pass, 8/8 controls fail as
     designed, exit 0.
Smallest remaining gap: every quantitative hypothesis instance in the junction holds exactly
  (Section 3). The first unverified load-bearing step is qualitative. Lemma 18.1 case 2 must apply to the
  conjugated product of two plain witnesses and the selected physical slots, whose witness profiles
  carry row-dependent parameters (sigma_u, gamma_u - nu). Lemma 18.1's statement has no rowwise-test
  clause; the prose supplies one through Lemma 4.5 (smooth-calculus) at 15163-15167. The analogous
  extension of Lemma 17.1 is asserted only inside the proof of Lemma 17.6 (12466-12468). The family
  condition R_z (15168-15170) and the Theta-combination slot coefficients (15134-15162) are also
  asserted in prose.
```

## 1. Verdict

**Certified (exact rational), within the quantitative scope.** Every lemma invocation in the junction satisfies the length, capacity, range, supply and mesh hypotheses of the invoked statement on the whole parameter box. The box is δ ∈ (1/50, 5/6], x ∈ [0, 1/2], t ∈ [1, 3/2], Δ ∈ (0, 1/24] and d ∈ [1/2, h+1/48), together with the witness lengths (r, m) of Prop 8.3. The Δ/4 capacity comparison (15392-15405) is correct, with room to spare. **No violating parameter point exists.** All eight failing controls produce exact counterexamples as designed. Each control removes one restriction the manuscript relies on, which shows that restriction is load-bearing.

The margins are uniform in the sense the lemmas require, with one qualification. **Lemma 18.1 is invoked exactly on its boundary**: `n1+n2+6κz = M` and `β* = (1+κ)/2`. The statement is non-strict, so this is permitted and is not a violation. The manuscript's own ν0-decrement would give a positive margin at negligible cost.

| Invoked result (instance lines) | Hypothesis | Margin (exact) | Where tight | Gate |
|---|---|---|---|---|
| Lemma 17.1 (15232-15236, 15364-15386) | `r + 2z ≤ m − c1`, m = 1 | `c1 = 2ν0` exactly (the decrement) | identity | I10, M2 |
| | `2r + 8z ≤ 3m − c2` | `c2 = 9/37`; excess `2(r − 23/37) + 8ν0 ≥ 8ν0` | t = 1, x = 1/2, r = 23/37, full capacity | M1, B2a |
| | bounded ranges | `r ∈ [23/37, 1]`, `z ≤ 7/37` | – | M3, M4 |
| Lemma 17.1 → 17.2 (12216-12287) | canonical margin | `c* = min(c1,c2)/2 = ν0`; both initial margins `≥ 3c̄/4` | – | I22 |
| Lemma 18.1 case 2 (15172-15179, 15237) | `n1+n2+6κz ≤ M`, n1 = n2 = m, M = 1 | **0** (equality at z = z_P(m)); `(1−μ)(1−2m)` for a whole-slot fraction μ | μ = 1 | I2, P1 |
| | `κ ∈ [3/4,1]` | `κ − 3/4 = 2Δ > 0`, `1 − κ ≥ 1/6` | Δ → 0 | P2 |
| | `β* ≤ (1+κ)/2` | 0 (equality, by definition of κ) | always | I3 |
| | mesh `z_i ≤ η` | base-U length `ℓ_i/d ≤ 2ℓ_i` for d ≥ 1/2 | d = 1/2 | P4 |
| | (robust variant, z_P − ν0) | `6κν0 ≥ 9ν0/2` | – | P5 |
| Lemma 18.1 case 1 (15312, 15428, 15441) | none (z = 0) | – | – | C4, C6, C8 |
| Lemma 17.6 (15248-15311, 15421, 15931) | bounded r, no slots, valuations ≤ 5 | `r ∈ [1/2 − O(ε), 3/2 + O(1/log U)]`; loss `= ε_m/2` | – | H3, I21, C3, C5 |
| Prop 8.3 (15211, 15228, 15929, 15965) | `t ∈ [1, 3/2]`, `a > 51/100` | `t − 1 = δP_x/(2J) ≥ 0`, `3/2 − t = (α−δ)D_x/(2J) ≥ 0` | δ = α (closed endpoint) | E1, E2, H1 |
| Lemma 19.1 (15016, 15067) | `51/100 ≤ a ≤ 1` | `a = (1+δ)/2 ∈ [51/100, 11/12]` | δ = 1/50 | H2 |
| Supply (15388-15391, 16114-16126) | `ℓ/d` exceeds 7/37 by a fixed amount | `23/1443` (d ≤ h); `2/185` (d < h + 1/48) | d = h; d → h+1/48 | Q1-Q3 |
| Capacities (15385-15387) | inverse ≤ 7/37, plain ≤ 2/27 | exact | t = 1, x = 1/2 | M3, P3 |
| Δ/4 comparison (15392-15405) | increase ≤ Δ/4 | slack `≥ (83/972)Δ`; worst ratio increase/(Δ/4) = 160/243 | δ = 5/6, x = 1/2, m = 1/3, Δ → 0 | I9, K1-K3 |
| Lemma 20.2 (15994-16072) | `−E* ≥ 49/440640` | certified (322 boxes); also `≥ 228/10⁶` | true min ≈ 2.2815e-4 | E8, E9 |
| Endpoint (16080-16106) | `E* + hΔ/4 − Δ ≤ −49/440640 − (51/64)Δ` | exact | – | I17, I18, E11 |

## 2. The invocations, with parameters

Notation and conventions:
* The base is U = Z^d.
* The row width is m_row = M = 1. The twist ν is fixed, so q = 0 (15240-15242).
* The geometry is `lx = 17/48`, `ly = 23/48`, `ℓ = 1/6`, `h = 13/16`, `C(s) = s − 11/16` (15511-15519).
* `κ = 3/4 + 2Δ` and `β* = 7/8 + Δ` (6816).
* `α = 5/6`, `a = (1+δ)/2` and `q = xδ`.
* The witness lengths satisfy `t − 1/2 − O(ε) ≤ r ≤ t + O(1/log U)`, `m ≤ 1/2 + O(ε)` and `r + m ≥ t − O(1/log U)` (eq:saturated-witness, 4527).

| # | Lines | Invoked | Instance |
|---|---|---|---|
| 1 | 15016-15025 | Lemma 19.1 (under Lemma 8.2) | every main slot; `a ∈ [51/100, 11/12]`. Output `|Q_i| ≤ P_i^{δ/2+ϑ}` after choosing e and ε1 *after* the mesh (15067-15071), hence `g_i ≤ δ/2`, `q ∈ [0, δ/2]`, `x ∈ [0, 1/2]`. |
| 2 | 15104-15107 | Lemma 18.1 (zero-free clause) | `κ = 2β* − 1`, so `β* = (1+κ)/2`, with equality. |
| 3 | 15110-15132 | selection | requested z ≤ ℓ/d. Whole positive slots of total ≤ z give gain `≥ 2qz − δ max w_i`. Decrement ν0 where a strict inequality is needed. |
| 4 | 15172-15183 | Lemma 18.1 / 17.1 capacities | `z_P(m) = (1−2m)/(6κ)` from `2m + 6κz ≤ 1`; `z_M(r) = (1−r)/2`. |
| 5 | 15211, 15228 | Prop 8.3 | any `t ∈ [1, 3/2]`, `δ > 1/50`. |
| 6 | 15232-15236 | Lemma 17.1 | m_row = 1, inverse length r, slots z. Count `1 − δr − 2qz`. |
| 7 | 15237-15241 | Lemma 18.1 case 2 | n1 = n2 = m, M = 1, slots z. Count `1 − 2δm − 2qz`. |
| 8 | 15248-15294 | Lemma 17.6 | no slots, `D = U^r`, `r ∈ [0, R0]`, `c = 3ε_m/(10 max(R0,1))`, `ε0 = ε_m/(4(1+R0))`. |
| 9 | 15297-15311 | Lemma 17.6 | r ≥ 1, giving count `1 − α + (α−δ)r ≤ L(t)`. |
| 10 | 15312-15315 | Lemma 18.1 case 1 | m ≥ 1/2, giving count `1 − 2δm ≤ 1 − δ`. |
| 11 | 15364-15386 | Lemma 17.1 | `r ∈ [r*(t), 1 − 2ν0)`, `z = (1−r)/2 − ν0`, so `c1 = 2ν0` and `c2 = 9/37`. |
| 12 | 15364-15405 | Lemma 18.1 case 2 | `r ≤ r*(t)`, `m ∈ [t − r*(t), 1/2)` ⊂ [1/3, 1/2), `z = z_P(m)` at the actual κ. |
| 13 | 15420-15432 | Lemma 17.6 (e(r) = 1) / Lemma 18.1 case 1 | zero-capacity neighbourhoods `1 − r ≤ 2ν0`, `1 − 2m ≤ 6κν0`. |
| 14 | 15434-15444 | Lemma 17.6 / Lemma 18.1 case 1 | no slots, t = 1, giving `1 − 2δ/3`. |
| 15 | 15927-15946 | Prop 8.3 at t = 3/2; Lemma 17.6 | δ = α. `R = 1 − δ` and `E(h) ≤ −1/48 − δ/16`. |
| 16 | 15948-15992 | Prop 19.2 | `t = 1 + δP_x/(2J)`, `R* = R_short(t) = L(t)`. |
| 17 | 15994-16072 | Lemma 20.2 | `δ ∈ [0, 5/6]`, `x ∈ [0, 1/2]`. |
| 18 | 16073-16111 | Prop 19.2 + Lemma 20.1 | `R ≤ R* + Δ/4 + ε_row`, coefficient of R is d = h. |
| 19 | 16114-16126 | supply and mesh | `d ∈ [1/2, h + ζ]`, `ζ < 1/48`. |

### Hypotheses of the invoked statements (as stated)

* **Prop 8.3** (4510-4545):
  * `a > 51/100`;
  * the loss and height hypotheses of Lemma 8.2;
  * `t ∈ [1, 3/2]`.
* **Lemma 8.2** (4385-4404):
  * bounded nonnegative ranges for r and m;
  * ψ ∈ X_u;
  * bounded profile seminorms;
  * twist height ≤ (3i+1)T1, and extra Mellin frequencies ≤ T1/2;
  * `e < e0(ε)` and `(1+T1)^A ≤ U^{ε/10}`.
* **Lemma 17.1** (9250-9269):
  * bounded ranges for `m, r, z_i ≥ 0`, and a bound on |I|;
  * fixed `c1, c2 > 0` with `r + 2z ≤ m − c1` and `2r + 8z ≤ 3m − c2`;
  * slots on disjoint prime sets outside S, with `q_p ≍ Z^{z_i}` and coefficients `|a_i(p)| ≤ 1` independent of u;
  * one common ν in the inverse and in all slots;
  * no mesh condition.
* **Lemma 17.2** (9296-9340): not invoked directly in the junction. Its hypotheses are (eq:invariant), `q_{r_ρ} ≤ Z^{F0−M−z0−c*}` and `3M + 6z0 + c* ≤ 4F0`. It is reached through 17.1's initialization with `c* = min(c1,c2)/2` and `η, τ_init ≤ c̄/100` (12270-12287).
* **Lemma 17.6** (12362-12392):
  * as for 17.1, but with no slots;
  * `q_u ≍ U`, with valuations ≤ 5;
  * a fixed c > 0;
  * r in a bounded nonnegative range;
  * rowwise tests `(σ_u, t_u)` with `|t_u| ≤ T1` are explicitly allowed.
* **Lemma 18.1** (12531-12579):
  * `κ ∈ [3/4, 1]` and bounded `n1, n2 ≥ 0`;
  * slot supports pairwise disjoint, with coefficients that are fixed Θ-combinations;
  * mesh `z_i ≤ η(ε, ranges)`, uniform in κ;
  * case 1: z = 0 on R_0;
  * case 2: z > 0 on R_z, with `n1 + n2 + 6κz ≤ M` **(non-strict)**, plus `β* ≤ (1+κ)/2` if κ < 1;
  * `M = m + q`.
* **Lemma 19.1** (15015-15025): the hypotheses of Lemma 8.2, with the prime-annulus frequency in the allowance. It is uniform for `a ∈ [51/100, 1]`.

## 3. What the checks establish

1. **Crossing geometry** (B1, B2), certified exactly on the box:
   * `D_x ≥ 37/18`, `7/9 ≤ P_x ≤ 2` and `D_x − P_x ≥ 1`;
   * `35/54 ≤ J ≤ 5/2`;
   * `23/37 ≤ r*(t) ≤ 1` and `1/3 ≤ t − r*(t) ≤ 1/2`.

   Each bound is tight at a vertex. Monotonicity reduction finds the vertex exactly.
2. **Lemma 17.1 instances** (M1-M4, I10, I22). On the inverse branch the second condition holds with `c2 = 9/37` for every whole-slot length z' ≤ z_M(r). The first condition is the decrement itself: `1 − r − 2z = 2ν0`. These margins are fixed before U, as Lemma 17.1 requires. Through the initialization they give the canonical margin `c* = ν0`.
3. **Lemma 18.1 instances** (I1-I3, P1-P5). The instance sits on the boundary of (old-eq:3.9). The exact factorization is `1 − 2m − 6κμz_P(m) = (1−μ)(1−2m)`. Equality is allowed. This review did not check whether the *proof* of Lemma 18.1 uses (old-eq:3.9) only in its closed form. If strictness were needed, the selection prose's own ν0-decrement (15124-15130) gives margin `6κν0 ≥ 9ν0/2` at count cost `2qν0 ≤ 5ν0/6` (P5).
4. **Δ/4 comparison** (I9, K1-K3). The identity `2q(1−2m)(2/9 − 1/(9/2+12Δ)) = 24q(1−2m)Δ/((9/2)(9/2+12Δ))` holds. The increase is at most `(40/243)Δ` on `q ≤ 5/12`, `m ≥ 1/3`, so the slack is at least `(83/972)Δ`. The manuscript's crude chain (`2q ≤ 1`, `1 − 2m ≤ 1/3`, both denominators ≥ 4) gives exactly 1/4 and is valid. **`m ≥ 1/3` is load-bearing.** Without it, at m = 0 the increase is `(40/81)Δ > Δ/4` (FC3). The direction is also confirmed: using the baseline capacity at the actual κ would violate Lemma 18.1 by `8Δ(1−2m)/3` (FC5). The Δ/4 term is genuinely needed: without it the plain bound fails at the crossing (FC7).
5. **Prop 19.2 case cover** (C1-C8, C1a-C3a). For every (δ, x, t, Δ) and every witness pair in the Prop 8.3 region, the estimate the proof selects is at most `max(R_short(t), L(t)) + Δ/4`, up to the O(ν0) zero-capacity terms. The branches are plain (via the decomposition derived here, C1a), inverse, long, m ≥ 1/2, zero capacity, and no-slot t = 1. A direct 6-variable branch-and-bound of the plain branch, without the decomposition, was time-boxed. It ended undecided because the bound is tight on a codimension-2 face. No counterexample appeared in 30,000 boxes. This attempt is informational, not a gate.
6. **Endpoint** (E1-E11, I12-I19):
   * the cutoff satisfies `t ∈ [1, 3/2]`;
   * `R* = R_short(t) = L(t)`, with `1 − δ ≤ R* ≤ 1`;
   * `R* + Δ/4 ≤ 139/96`, and the slope is `≥ 4/25`;
   * the extension cost is < 2;
   * at δ = α, `E(h) ≤ −1/48 − δ/16`;
   * Lemma 20.2 is re-certified independently of (20.9);
   * the adaptive endpoint inequality (eq:adaptive-endpoint) holds exactly.
7. **Lipschitz bounds behind 16074-16075** (L0-L5). All four are exact; the denominator is a positive multiple of J² with J ≥ 35/54:
   * `dt/dδ = αP_xD_x/(2J²)`;
   * `|dt/dδ| ≤ 2` and `|dt/dx| ≤ 1/4`;
   * `|dR*/dδ| ≤ 2` and `|dR*/dx| ≤ 1/10`;
   * `0 ≤ dr*/dt ≤ 1`.

## 4. Remarks (no violation)

* **R1 (boundary use).** Lemma 18.1 is applied with zero margin in both its length condition and its zero-free condition. Both are stated as non-strict, so the instance is inside the hypotheses. A reviewer of Lemma 18.1's proof should confirm that the closed condition suffices. The comparison ledger in LEMMA18_1_REVIEW §2.3 should then be read on the closed region.
* **R2 (cosmetic, 16139-16141).** R* is at most 1, not just 17/12, so `R* + Δ/4 ≤ 97/96`. The printed 139/96 is valid but loose.
* **R3 (cosmetic, 16133).** The exact minimum of `33/50 − δ/2` on δ ≤ 5/6 is 73/300. The stated 4/25 is valid.
* **R4 (slack).** In our model, `threshold_calculus.R_fast` at κ = 3/4 + 2Δ exceeds R* by at most about 0.0077Δ on a grid. This is FLOATING_RECONNAISSANCE, not a gate. The Δ/4 allowance is therefore very conservative. The `−(51/64)Δ` endpoint margin does not depend on it being sharp.
* **R5 (quantifier order).** The order is ε, then ν0 (and with it c1 = 2ν0, c2 = 9/37, c* = ν0), then the constants of Lemma 17.1, then U. This matches "capacity decrements and slot mesh chosen using only ε, Δ and the bounded real ranges" (15200-15203). The mesh is chosen before e and ε1 (15067-15071), and Lemma 18.1's mesh is uniform in κ.

## 5. Failing controls (each must yield an exact counterexample)

| Control | Removed restriction | Exact witness |
|---|---|---|
| FC1 | r ≥ r*(t) on the inverse branch | t = 1, r = 1/2, z = 1/4: `2r + 8z = 3`, so c2 = 0 |
| FC2 | x ≤ 1/2 | x = 1, t = 1: `r* = 1/2 < 23/37` |
| FC3 | m ≥ 1/3 in the Δ/4 comparison | δ = 5/6, x = 1/2, m = 0: increase = (40/81)Δ |
| FC4 | d ≤ h + 1/48 | d = 9/10: `ℓ/d = 5/27 < 7/37` |
| FC5 | actual κ in Lemma 18.1 (baseline capacity used instead) | m = 5/12, Δ = 1/48: `1 − 2m − 6κz = −1/108` |
| FC6 | Lemma 20.2 margin raised to 229/10⁶ | δ = 595/1536, x = 1/2 |
| FC7 | the Δ/4 term | δ = 5/12, x = 1/4, t = 5/4, Δ = 1/48 (scaled deficit −5/1152) |
| FC8 | sanity: J ≥ 1 | δ = 5/6, x = 1/2: J = 35/54 |

Final run: **84/84 gates pass and 8/8 failing controls fail as designed (exit 0).** The float cross-check F1 also passes, but it is not a gate.
* Script SHA-256: `30573564aa1a8910ab2bececbb678cd528fc397da80c4ab8c5fcb30875d24efc`.
* Output JSON SHA-256: `1e5572132db5b972baf18637438c101e4a6a512d01b5a88e207169ad2a5aacce`.
* The JSON records float timings and the time-boxed direct C1 attempt, so its bytes are not reproducible. Its verdicts are.

## 6. Not checked

* The analytic truth of Lemmas 8.2, 17.1, 17.2, 17.6, 18.1 and 19.1, and of Prop 8.3.
* The coefficient-class and family conditions: the Θ-combinations, the R_z membership via ramification outside S, and conjugation invariance (15134-15170).
* The rowwise witness parameters for Lemmas 17.1 and 18.1 (15163-15167; 12466-12468).
* The height bookkeeping of Lemma 8.2: e0, A and T1. Only the arithmetic of the ceiling τ0 was checked (H5).
* The positivity extension from sixth-power-free rows to all rows `q_u ≪ U`.
* Lemma 20.1 itself.
* The quantifier order of Prop 20.3.

## 7. Reproduction

```text
cd research/exploratory/qrh-2026-10/reviews
git -C ../../../.. show pr908:standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/\
The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex > /tmp/paper.tex
nice -n 10 python3 -I sep30_junction_check.py /tmp/paper.tex   # writes sep30_junction_check_output.json
```

The script needs sympy. The float cross-check also needs numpy and `../scripts/threshold_calculus.py`. Exit status 0 means every gate passed and every control failed as designed. Without the TeX path, the source-binding gates S0 and S1 are skipped.
