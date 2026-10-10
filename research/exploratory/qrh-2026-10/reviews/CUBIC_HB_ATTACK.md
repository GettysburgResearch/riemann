# Adversarial attack on hypothesis (H-B): the nested comparison order for the cubic fourth moment

```text
Status: REVIEW (adversarial, bounded, one agent) of a PROPOSED, CONDITIONAL exploration object.
  Verdict (a): no break found at the level of the manuscript's displayed steps. No moment bound is
  proved. Everything stays CONDITIONAL on (H-A), i.e. on the external, unreviewed Lemma 18.1
  scheme carried to n = 3. RH is not addressed.
Scope: hypothesis (H-B) of proposed/CUBIC_FOURTH_MOMENT/SKETCH.md Sec. 3.3-3.6 (risk item 8),
  case 1 (z = 0) only. The three named failure modes: (i) row-dependent dual scales, (ii) profile
  closure, (iii) clipping in xi. Also well-foundedness and the closing margin. The analytic core
  (A1-A7: transforms, coefficient lemma, lattice lemma) is NOT re-reviewed here.
Exact sources or dependencies:
  repo HEAD ddd8e8f614d0077962ce9db90ea0d406a9b99a72 (working branch of this session).
  pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6:standalone/2026-10-07-openai-quasi-riemann-
    import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
    sha256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-hashed; read as
    untrusted data). Read for this note: l. 1123-1152, 12477-12600, 12602-12830, 12831-13110,
    13930-14000, 14119-14160, 14302-14312, 14505-14537, 14538-14694, 14695-14830.
  Under attack: proposed/CUBIC_FOURTH_MOMENT/SKETCH.md Sec. 1.3, 3.1-3.6, 5, Appendix.
  Context read: proposed/CUBIC_FOURTH_MOMENT/README.md (all notes), reviews/CUBIC_NESTED_REDTEAM.md
    Sec. 0-1.4 and 5.
What was actually run:
  python3 -I reviews/cubic_hb_checks.py -> 27/27 PASS, under 1 s, single core
    (script sha256 8128366d2987b96613f13adc5e508d826c6f299e483dba70bf518cd570fd7b3a;
     output reviews/cubic_hb_checks.out, sha256 27789c4eaefaa264877592f7f29a4a679dbaaa2f789e04a7dd6695613d60c6b5).
  Exact Fraction arithmetic plus one sympy (1.14.0) gamma identity. Seven of the 27 are failing
  controls, deliberately broken variants: W1c, W2c, M1c, N1c, N1c2, P1c, C1c. All seven were
  detected. No other script was rerun. No Lean, lake or comparator process was started.
Smallest remaining gap: (H-B) adds nothing beyond the manuscript's own "reflect, take suprema,
  then centre" path (l. 12810-12830, 12912-12913, 14797-14798) except three things: one more
  reflection per width level, a smaller xi (xi <= mu*(delta) rho/2), and comparisons that call a
  same-width centred stage. So the route fails here only if the centred stage (A5 with A2-A4)
  is invalid on reflected padded-core data. That would already break Lemma 18.1 case 1 itself
  (risk items 9 and 12). The cubic reflection additionally needs Lemma 4.K (risk item 7) and the
  profile-uniformity clause over a bounded, Z-dependent family of annular profiles (A8).
```

RH is unsolved. This note does not prove or disprove RH, Lemma 18.1, or any cubic moment bound.
"Closes" means that affine exponent ledgers balance and a finite call graph is acyclic, nothing
more. Manuscript line numbers refer to the pr908 `paper.tex` above.

## 0. Verdict

**(a) No break found.** (Bounded review by one agent, at the level of the displayed steps.)

1. **The main finding is structural.** The manuscript already applies its centred stage to
   reflected data.
   * The padded core is reached by reflecting every factor longer than `M/2` (l. 12810-12823).
   * "Reflection then supplies all zero-slot lengths" (l. 12912-12913, 14797-14798).
   * "Reflection and scale suprema are taken before centering" (l. 12824-12830).
   * So "the centred stage accepts a datum produced by reflection plus rowwise supremum" is
     already a hypothesis of the sextic proof.
   * The nested order's reflected comparison datum `D'` is exactly the reflection closure `R`
     applied to the comparison product. In the sextic proof that same reflection is sent to `U`
     (l. 12950-12985).
2. **Each of the three failure modes is handled by a device the manuscript already uses on the
   `R → C` path** (Sec. 2). (H-B) adds three things:
   * one more reflection per width level: three in a nested branch, against two already present
     in the manuscript (S1, P2);
   * a smaller `ξ`: `ξ ≤ μ*(δ)ρ/2`, not `ρ/30` (N1, N1c2);
   * comparisons that call a same-width centred stage `C_{j−1}`. They do not call only `U`.
3. **Well-foundedness holds** (Sec. 3). The measure `Φ(β, j) = 4β + j` drops by at least 5 on every
   child call and by at least 1 on every comparison and reflection call. This was checked on exact
   call graphs (W1, W2).
4. **The closing margin survives unchanged** (Sec. 4). An exact LP recomputes
   `μ*(δ) = (11 − 147δ)/612` and `c*(δ) = (11 − 147δ)/432`. The nested order's extra losses
   are of three kinds:
   * one `ξ` per comparison call, entering (R) only;
   * powers of `log Z` and `Z^{ε₁}`, which go into `ε`;
   * terminal losses, which also go into `ε`.

   None of them is a multiple of `M`.
5. **Two precision corrections** (Sec. 5), neither a break:
   * profile closure is needed through `k + 1 = 3` reflections per width level, not `k`
     (correcting RT correction 4);
   * for padded-core inputs the short-side branch is vacuous whenever `ξ ≤ μM`.

## 1. (H-B) stated exactly

Source: SKETCH.md Sec. 3.1-3.3, with the manuscript's definitions.

**Datum.** A datum is a zero-slot product `S_{ψ_k}(n_1; W_1) S_{ψ_k}(n_2; W_2)` at width
`M = m + q`. Its parts:
* cubic rows `k`, with `ψ_k(n) = τ(n)(k/n)_3` zero-extended;
* moving support of norm `≤ Z^q`;
* a fixed extra mask;
* `Θ`;
* smooth profiles on fixed windows.

`H(M; 0)`: `Σ_{k∈R_0} |S S|² ≪ Z^{M+ε}` (SKETCH 3.1; manuscript l. 12548-12553).

**Nodes and stages.** Bands of width `σ/4` in `M`. Nodes are `(β, j)`:

| `j` | stage | inputs covered (units of `M`) |
|---|---|---|
| 0 | `U` | all lengths with `A ≤ 2/3` (no core restriction; manuscript l. 12911, sextic `5/6`) |
| 1 | `C_1` | padded core (`n_i ≤ 1/2 + ξ`), `2/3 < A ≤ b_1` |
| 2 | `C_2` | padded core, `b_1 < A ≤ 1 + δ` |
| 3 | `R` | any bounded lengths. Reflect each factor `> 1/2` once (l. 12810-12823) |

**The order.** Lexicographic on `(β, j)`. Within a band, stages are proved for all widths of the
band in the order `U, C_1, C_2, R`. Calls:

| call | from | to |
|---|---|---|
| child (second transform) | any `(β, j)` | width `≤ M − σ/2`, so band `≤ β − 2` |
| comparison (**new**) | `C_j`, `j ≥ 1` | the stage `j' < j` that covers `A_comp`, at the same width. The manuscript has only `j' = 0` (l. 14799-14800) |
| reflection closure | `(β, 3)` | `(β, ≤ 2)` |

**Reflected comparison datum.** At `C_j`, given a core input of lengths `(n_1, n_2)` and total `A`,
the comparison is built in four steps.
* **Comparison product.** `L = L_j(A) = (6/5)(A − 2/3 + μ)`. The comparison is
  `S(Z^L; W_1) S(X_1X_2/Z^L; W_2)`: the same character, mask and profiles, and an equal product of
  scales (l. 12950-12955, 12987-12990).
* **Reflection.** Its longer factor (length `A − L > 1/2`) is reflected (l. 12733-12754). This
  gives the following:
  * the root number `ε_k`;
  * a row-dependent coefficient sum over `d_0, h_0`;
  * row-dependent dual scales `Y = C_k q_{d_0}/(X q_{h_0})` (old-eq:2.1d, l. 12750-12754);
  * the profile `W_2^♯`, with `𝓜W^♯(s) = 𝓜W(1−s)Γ(s)/Γ(1−s)` (l. 12700-12704).
* **Processing.** The reflected factor is then:
  * put in absolute value, which removes `ε_k`;
  * bounded by its coefficient mass `Z^{ε₁}` (l. 12757-12760);
  * replaced by a rowwise supremum over its scale, which costs `O((log Z)²)` unit boxes and
    derivative profiles (l. 12780-12783; parameter-Sobolev l. 1143-1150);
  * split into fixed annuli with summable coefficients (l. 12766-12779);
  * conjugated back to `ψ_k^0` (l. 12784-12789);
  * clipped to declared length `≤ M − (A − L) + ξ` (eq. centered-reflection-length, l. 12797-12807).
* **Result.** Each resulting term `D'` is a natural, row-independent-scale datum at width `M`,
  with lengths `(L, n' ≤ 1 − A + L + ξ)` and total `A' ≤ 1 − A + 2L + ξ`.

**What the inductive hypothesis provides at each level.** When `C_j` at width `M` runs, three
results are already available:
* `H` for every datum at every width in bands `≤ β − 1`, since earlier bands are complete;
* `U` and `C_{j'}` (`j' < j`) at every width of band `β`;
* the base case `M ≤ ρ`.

`C_j` uses them only in two ways:
* children, through the transform ledgers;
* the separate bound `Σ_{R_0}|comp|² ≤ (log Z)^{O(1)} Z^{ε₁} Σ_{boxes} Σ_{R_0}|D'|²`, which
  feeds `|S|² ≤ 2|Δ|² + 2|comp|²` (l. 12991-13008).

The centred analysis of `Δ` uses only the choice of `L`, not the comparison's bound.

## 2. The three failure modes

For each mode the table lists where the centred stage uses the property of its input, and
whether `D'` has it at `n = 3`.

### 2.1 (i) Row-dependent dual scales

| where the centred stage uses row-independent scales | line(s) |
|---|---|
| comparison scales `Y_1 = Z^L`, `Y_2 = X_1X_2/Y_1` fixed for all rows | 12987-12990 |
| `D_𝐛` is one fixed function, `X_1X_2 = Y_1Y_2` | 13017-13024 |
| `Δ` enlarged to the whole smooth row ball before Poisson ("never applied to an indicator selecting exceptional or nonexceptional rows") | 13003-13010 |
| plain profile types and endpoints `B_i` fixed "before the current row, divisor, and live labels" | 14126-14128 |
| suprema before centering; none on a Θ-row centred difference | 12824-12830 |
| common character on the full product (multiplicativity) | 13056-13072; Lemma at 13954-13987 |

**Does `D'` have the property?** The raw reflected factor does not:
* its scale `Y = C_k q_{d_0}/(X q_{h_0})` depends on the row through the conductor `C_k` and the
  row radical `𝔑_{0,k}`;
* its coefficients `μ(d_0)ψ_k^*(d_0)\overline{ψ_k^*(h_0)}` and the root number `ε_k` depend on the row;
* it is defined only on `R_0`, since the functional equation needs `ψ_k^*` nonprincipal;
* its character is `\overline{ψ_k^0}`.

But the nested order never centres the raw form. Before `C_{j−1}` is called, five steps act on it:
* the absolute value removes `ε_k`;
* the coefficient mass bound removes `d_0, h_0` (l. 12757-12760, 12780);
* the rowwise supremum over its scale, by parameter-Sobolev (l. 1143-1150), gives a sum over
  `O((log Z)²)` row-independent boxes `I` with derivative profiles. Every row's own scale lies in
  one box, and the bound sums over all boxes;
* conjugation restores `ψ_k^0` in both factors (l. 12784-12789), so the coefficient is
  `ψ_k^0(l_1l_2)·(profiles)`. That is the common-character form (l. 13056-13072);
* the post-supremum `D'` is a plain product defined for every row in the ball, so the enlargement
  at l. 13003-13010 is legitimate.

The centred stage `C_{j−1}` then builds its own comparison from `D'`'s row-independent box scales.
Its equal-product identity is therefore exact.

**This is the manuscript's own order.** It is exactly the order "reflection and scale suprema are
taken before centering" (l. 12824-12825). The manuscript uses that order on its `R → C` path.

**Decision: has the property** (after the manuscript's own devices; cost `(log Z)^{O(1)} Z^{ε₁}`,
which goes into `ε`).

**Load-bearing at `n = 3`.**
* The conjugation step: control C1c shows that `ψ(l_1)\overline{ψ(l_2)}` is not a function of
  `l_1l_2`. This was checked on an exact toy, the cubic character mod 7.
* The cubic functional equation and conductor bound `C_k q_{𝔑_{0,k}} ≪ Z^M` (Lemma 4.K, the
  analogue of old-eq:2.1c, l. 12684-12698). It is still only sketched (risk item 7).

### 2.2 (ii) Profile closure

| where the centred stage uses the admissible profile class | line(s) |
|---|---|
| lattice lemma: "smooth profiles on fixed annuli"; Poisson needs `f_t` supported on a fixed annulus | 14550-14552, 14610-14617 |
| main term `I_i(t) = ∫W_i(y)y^{it}dy`, needs the same profiles in both rectangles | 13037-13045, 14566-14569 |
| `H_N` includes "the two plain profile windows, `log C_ref`", support enlargements through `D` stages | 13090-13096 |
| `C_ref ⊇ max(1, B)` for retained profile types | 12790-12797 |
| subunit plain scale in `[1/B_i, 1]`, dilated to one with bounded seminorms | 14156-14159, 12671-12676 |
| constants use finitely many seminorms, polynomial in heights (uniformity clause) | 12573-12578 |

**Does `D'` have the property?** Its profiles are of four kinds:
* `W_1`, unchanged;
* the conjugate of an annular piece `φ_j(y) = ψ(y)W_2^♯(2^{−j}y)`, on a fixed window;
* `D_y`-derivatives of these, from the supremum;
* dilations of these, from subunit rescaling.

`W^♯` is smooth, bounded at zero with an expansion in nonnegative integral powers, and rapidly
decreasing (l. 12709-12717). So the pieces have uniformly bounded seminorms in `j`, polynomial in
the height (l. 12716-12731), and coefficients `O(2^{−j/2})`.

**A second reflection** (`C_{j−1}`'s comparison may put its longer length on the reflected
profile) stays in the same class. On the Mellin side reflection is an involution:
`G(s)G(1 − s) = 1` with `G(s) = Γ(s)/Γ(1 − s)` [P1]; control P1c shows that a wrong gamma
factor is not involutive. Each reflection raises the needed seminorm order by a fixed amount
(l. 12726-12731).

**Count.** Along one width level a profile lineage is reflected at most `k + 1 = 3` times: `R`,
then `C_2`'s comparison, then `C_1`'s comparison [P2]. The manuscript's own path already does
this twice [S1]. For example `(0.45, 0.6)` goes through four steps:
* `R` reflects `0.6`, so `A* = 0.86` lies in the core above `5/6`;
* `C` builds the comparison `(1/4, 0.61)`;
* the factor `0.61` is reflected again, giving `A_comp = 0.65`;
* the result goes to `U`.

**One caveat: the family is not finite.** There are `O(log Z)` annular pieces, so the profile
family is bounded but `Z`-dependent, not finite. The phrase "finite set of profile types"
(SKETCH 3.6, RT correction 4) should read "a family with uniformly bounded seminorms on finitely
many fixed windows". The manuscript's own `R → C` path needs the same reading, so this is not new
to (H-B). It rests on the uniformity clause (A8; reviews/CUBIC_PROFILE_UNIFORMITY.md).

**Decision: has the property**, given A8 and fixed depth.

### 2.3 (iii) Clipping in ξ

| where the centred stage uses clipping or ξ bookkeeping of its inputs | line(s) |
|---|---|
| declared reflected length `n_ref ≤ M − n + ξ`, after "the permitted clipping and box enlargement" | 12795-12807 |
| comparison length includes "the clipped reflected scale and the paired unreflected box multiplier in this same ξ"; target must have strict margin `≥ ξ` ("Choose `ξ ≤ ρ/30`") | 12961-12985, 14799-14800 |
| padded core `n_i ≤ M/2 + ξ`, `A ≤ M + 2ξ ≤ M + δ` | 12810-12823 |
| Θ branch: "No formal centered scale is clipped"; "Exceptional raw scales remain formal and are not clipped" | 14703-14705, 14786 |
| non-Θ rows: rectangles clipped separately, `≤ 2θ_N` per edge, `C_*ξ < σ/2` | 14119-14180, 14782-14793 |
| "all four plain lengths are at least `L`" for the lattice lemma | 14686-14687 |

**Does `D'` have the property?**

* **The clipping is external.** `D'` is clipped once, when it is formed: upper annuli are cut at
  `Z^{ξ/2}`, subunit scales go to one, and box enlargement and `C_ref` enter the declared length.
  The result is a fixed representation with exact box scales and fixed-window profiles.
  `C_{j−1}` builds its comparison from that representation. Its Θ-branch equal-product identity
  then holds exactly in formal scales, and no internal formal scale is clipped. The formal
  requirement at l. 14703-14705 and 14786 concerns scales created inside the centred analysis, and
  those are untouched.
* **Range and core membership** (exact, check N1, every sub-box `n'' ∈ [0, n']`):
  * The bounds for `D'` are `n' ≤ 1 − A + L + ξ ≤ 1/2 + ξ − μ` (by the cap `L ≤ A − 1/2 − μ`),
    `L ≤ 1/2`, and `A' ≤ b_1 − μ + ξ ≤ b_1` iff `ξ ≤ μM`.
  * With `ξ = μ*/2` the minimum slacks are `11/1224` in (R) at `C_2`, and `11/510` in (R) at
    `C_1` applied to `D'` (`δ = 0`).
  * At `ξ = μ*` both slacks are exactly 0.
  * At `ξ = 2μ*` the chain fails, as the control N1c requires.
* **The `ξ` does not accumulate along the chain.** Each stage is a statement about all core data
  with total in its range. One comparison call adds one `ξ`, and the target's margin absorbs it.
  `C_1`'s comparison of `D'` lands at `≤ 2/3 − μ + ξ` whatever the history of `D'`.
* **Smaller `ξ` (nested-specific).** The manuscript's `ξ ≤ ρ/30` is calibrated to its strict
  margin `M/15` or `M/6` (l. 12978-12981). The nested margin is `μ*M ≈ 0.018M`, and at
  `M = ρ = 1` the choice `ξ = 1/30` breaks the chain (control N1c2). SKETCH 3.2 already demands
  `ξ ≤ min(ρ/30, μ*ρ/2, …)`, which suffices because `M ≥ ρ` above the floor.
* **Four plain lengths `≥ L`.** For any padded-core input with `ξ ≤ μM`,
  `min(n_1, n_2) ≥ A − 1/2 − ξ ≥ L + (μ − ξ) ≥ L`. This uses the cap. So the short-side branch
  (l. 12952) is vacuous in the core. It holds for `D'` and every sub-box (N1, N2).
* **Box enlargement** (`I + [−1,1]` in parameter-Sobolev) changes scales by a factor `e`, that is
  by `O(1/log Z)` in length, which is inside `ξ`.

**Decision: has the property**, given `ξ ≤ μ*(δ)ρ/2` and `2ξ ≤ δ`.

## 3. Well-foundedness

**Measure.** `Φ(β, j) = 4β + j ∈ N`, with `β = ⌊M/(σ/4)⌋`.

| call | decrease of `Φ` | reason | check |
|---|---|---|---|
| child (any stage, including both rectangles of `Δ` after the triangle inequality on non-Θ rows, l. 14119-14123) | `≥ 4·2 − 3 = 5` | actual width `≤ M − σ + C_*ξ ≤ M − σ/2` (l. 14782-14790), so `β' ≤ β − 2` | W2 (exact, 401 widths × 3 offsets) |
| separate comparison bound `C_j → C_{j'}`, `j' < j` | `≥ 1` | (R): `A_comp ≤ b_{j−1}`, and the caps keep `D'` in the core (Sec. 2.3) | N1 |
| reflection closure `R → (β, ≤ 2)` | `≥ 1` | `A* ≤ M + 2ξ ≤ M + δ`, the top of `C_2` | — |
| Θ rows, zero frequency, diagonal, Gauss-row zero | terminal | no call | — |

The comparison rectangle inside `Δ` is never called as a separate node. Its children are strict,
because the transforms act identically on both rectangles (reviews/CUBIC_BOTH_RECTANGLES.md).

**Exact call graphs** (W1), for 8, 16 and 32 bands at `k = 2`:
* `Φ` strictly decreases on every one of 384, 1776 and 7632 edges;
* the graphs are acyclic;
* the longest chain is 16, 32 and 64 nodes, which equals `4·(⌊(#bands − 1)/2⌋ + 1)`.

**Controls.**
* W1c: allowing a comparison to land in its own stage, which is what a failure of (R) would mean,
  creates a cycle and breaks the decrease of `Φ`. Detected.
* W2c: `C_*ξ = 7σ/8` breaks the band drop. Detected.

## 4. Closing condition and margin under the nested losses

**Recomputation.** The margin was recomputed as an exact two-variable LP in `(μ, b_1)`, using the
stage-endpoint constraints of SKETCH 3.5 (feasibility on each stage interval is exact at its
endpoints, since `lo` is a maximum of affine maps and `hi` a minimum). Vertices were enumerated
with Fractions. This is independent of the SKETCH appendix code.

| `δ` | LP max `μ` | `(11 − 147δ)/612` | optimal `b_1` | (C)-only tolerance `c*` | `(11 − 147δ)/432` |
|---|---|---|---|---|---|
| 0 | 11/612 | 11/612 ✓ | 31/36 | 11/432 | 11/432 ✓ |
| 1/100 | 953/61200 | ✓ | 3121/3600 | 953/43200 | ✓ |
| 1/50 | 403/30600 | ✓ | 1571/1800 | — | — |
| 1/20 | 73/12240 | ✓ | 641/720 | — | — |

Control M1c: `μ* + 10⁻⁶` is infeasible for every `b_1 ∈ 31/36 ± 0.02` on a 4001-point grid.

**Extra losses of the nested order, and where they enter.**

| loss | lines | enters | effect on margin |
|---|---|---|---|
| `ξ` per comparison call (clipping, box enlargement, `C_ref`) | 12797-12807, 12961-12985 | (R), once per call, not cumulative | needs `ξ ≤ μ*M`; ensured by `ξ ≤ μ*ρ/2` |
| coefficient mass `Z^{ε₁}`, `(log Z)²` boxes, annular sum `O(1)` per reflection (3 per level) | 12757-12783 | multiplicative constants and `Z^{O(ε₁)}` | none; into `ε` |
| derivative profiles from the supremum; seminorm order per reflection | 1143-1150, 12726-12731 | constants (uniformity clause) | none |
| `(k + 1)` same-width calls in the envelope | 14925-14938 | `ξ < ε/(16(k+1)C_*D)` | none; into `ε` |
| terminal `T = O(σ + δ + ξ + θ_N)` in each stage's Θ-row bound | 14526-14534, 14757-14776 | (C), terminal, not compounded | none; into `ε` |

No extra loss is a multiple of `M`, so `μ*(δ) = (11 − 147δ)/612` stands. Strictly, (C) needs no
margin, because `T` is terminal. The margin is consumed only by `ξ` in (R) and by the caps.
The SKETCH demands `μ` in every constraint, which is conservative. The tolerance
`c*(δ) = (11 − 147δ)/432` for a hidden loss confined to the centred deficit is unchanged
(reviews/CUBIC_ALLOCATION_LOSS.md qualifies which losses it covers).

## 5. Precision corrections (not breaks)

1. **Profile closure depth.** RT correction 4 says the profile types must be "closed under `k`
   nested reflections". The count is `k + 1` per width level, compounded through the `D` levels
   (P2). The manuscript itself needs 2 (S1). Also replace "finite set" by "uniformly bounded
   family on finitely many fixed windows" (Sec. 2.2).
2. **Short-side branch.** For padded-core inputs with `ξ ≤ μM` it never fires (Sec. 2.3). The
   SKETCH caps row ("all four plain lengths `≥ L`") holds automatically and needs no separate
   branch.
3. **SKETCH 3.3 table, row `U`.** `U` has no padded-core restriction. `C_1` does have one, which
   the SKETCH table states only for `C_2`. `D'` is in the core by the cap `L ≤ A − 1/2 − μ`.

## 6. Verdict and register line

**Verdict: (a) no break found** (bounded, one agent, displayed-step level).
* None of the three failure modes is new to (H-B).
* Each is met by the manuscript's own `R → C` devices:
  * (i) the order "suprema before centering" plus conjugation (l. 12780-12789, 12824-12830);
  * (ii) reflection bounds and the uniformity clause (l. 12700-12731, 12573-12578);
  * (iii) one `ξ` per call, absorbed by the target's margin (l. 12797-12807, 12978-12985).
* The nested order needs one more reflection per level and `ξ ≤ μ*(δ)ρ/2`.

**Updated risk-register line for item 8:**

| # | step | status | evidence | most likely failure mode |
|---|---|---|---|---|
| 8 | Nested order (H-B), Secs. 3.3-3.6 | **attacked twice, no break** (bounded agent reviews; no human check). Reduced to the manuscript's own reflect-then-centre path (l. 12810-12830, 12912-12913, 14797-14798) plus one extra reflection per width level, and `ξ ≤ μ*(δ)ρ/2` | RT (a); CUBIC_HB_ATTACK (a), 27/27 with 7 failing controls detected; exact `μ*`, `c*` and call graphs | it fails only if the centred stage (A5 with A2-A4) is invalid on reflected padded-core data. That would break Lemma 18.1 case 1 itself (items 9, 12). Cubic-specific inputs: Lemma 4.K (item 7) and the uniformity clause A8 over the bounded annular profile family |

## 7. Not done (OPEN)

* The internal steps of A2-A5 on a reflected input were not re-derived line by line. The argument
  is the structural identity with the manuscript's `R → C` path, together with the input-class
  checks above.
* Lemma 4.K (the cubic row functional equation and conductor bound) was not reviewed.
* The seminorm order growth per reflection was not quantified. Only its finiteness at fixed depth
  is used.
