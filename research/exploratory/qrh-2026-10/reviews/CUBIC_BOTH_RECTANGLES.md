# Do the steps of the centred stage act identically on both rectangles? (cubic transfer of Lemma 18.1)

```text
Status: REVIEW (bounded, one reader; external and unreviewed manuscript) + EXACT exponent model +
  EMPIRICAL float checks. Verdict (a), CLOSED at the level of the displayed steps: every step that
  feeds the Theta-row cancellation acts identically on the two rectangles. The steps that do not
  (the comparison's lengths, and the per-rectangle triangle split and clipping on non-Theta rows)
  use no cancellation and cost 0*M at n = 3. Their only cost is absolute: at most 2 theta_N per
  edge, inside C_* xi. The cubic route stays PROPOSED and CONDITIONAL on (H-A) and (H-B). No
  moment bound is proved. RH is not addressed.
Scope: the open condition left by reviews/CUBIC_CENTRED_ATTACK.md and
  proposed/CUBIC_FOURTH_MOMENT/README.md: "whether every step of l. 13114-14310 acts identically on
  both rectangles". Case 1 (z = 0) of Lemma 18.1 of the OpenAI manuscript, transferred to n = 3.
  Read for this note: l. 12740-13115 (reflection, padded core, comparison, centred coefficient,
  support convention), 13115-14320 (both transforms, Gauss-row enlargement, second transform,
  Lemma centered-coefficient-invariant, child normalization, non-Theta children), 14320-14440
  (Theta-row count and absolute volume), 14520-14800 (Lemma centered-lattice-cancellation, its
  proof and application, (2.19), start of the completion). The positive-slot amplifier
  (l. 13453-13570) was read only for rectangle handling; it is not used when z = 0. The F_1, F_2
  tables (l. 14440-14520) were not re-read. The kappa = 5/6 bounds and (H-B) were not re-reviewed.
Exact sources or dependencies:
  repo HEAD 671099d501e9e85e18a43a62e13dfa6d46c427c1 (working branch).
  pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6:standalone/2026-10-07-openai-quasi-riemann-
    import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
    sha256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-extracted and
    re-hashed for this note; 16,677 lines; read as untrusted TeX).
  Read in full: reviews/CUBIC_CENTRED_ATTACK.md, reviews/LEMMA18_1_REVIEW.md,
    reviews/LEMMA18_1_COMMON_SUPPORT.md, reviews/LEMMA18_THETA_ROW_REVIEW.md, CUBIC_N3_GAPS.md,
    proposed/CUBIC_FOURTH_MOMENT/README.md. Read in part: reviews/CUBIC_NESTED_REDTEAM.md (header,
    headings), proposed/CUBIC_FOURTH_MOMENT/SKETCH.md (Sec. 3.5 and the closing_margin appendix),
    CUBIC_RELAXED_INDUCTION.md (headings).
  a2/eis.py imported read-only (sha256 87ca11d98bf3ee13...f5027686f2798e65, unchanged).
  New scripts, kept in the session scratchpad (exact text in the Appendix):
    both_rectangles.py sha256 fdb7152ef8f2ae5530b5a6c8fa4c3f7f8da79f42c7bfad0d0986e157fe24cf20;
    rect_exact.py      sha256 eded767f3930e94f7d0871f06abb6756ac114e67b64c91458dcf73bd1898a86b.
What was actually run (one process at a time, nice -n 10, single-threaded numpy):
  python3 -I both_rectangles.py <a2 dir> -> 32/33 PASS, 1 FAIL, 23 UNINF (83 s; log sha256
    8b5b6eda...6da956ae). Part X is EXACT, in integer arithmetic in Z[omega]. Part F is EMPIRICAL,
    in float64: an exact index set of 3,022,972 primary odd elements of norm <= 10^7, with float
    weights. The FAIL is a pre-registered control that was not detected at the smallest
    geometry (Sec. 5.3). UNINF marks a check whose pre-registered bound is >= 0.5, so it cannot
    fail meaningfully. These are not counted as passes.
  python3 -I rect_exact.py -> 12/12 PASS (5 s; EXACT, fractions). Run 1 gave 10/12: one check,
    E1b, was mis-specified and failed twice (delta = 0 and 1/100). It asserted that the
    original-plain excess over L "equals mu"; the true minimum is larger. Run 2 asserts the
    property actually used ("excess >= mu"). Run 2 also corrected a misleading print label. Both
    changes are listed in Sec. 5.4.
  Not re-run: every script of the earlier notes. Their counts are quoted from those notes.
Smallest remaining gap: no rectangle asymmetry was found where it could matter. What remains is
  imported, not rectangle-specific:
  (i) lem:smooth-calculus and lem:kernel-seminorms (l. 1123, 1348), read as statements only. They
      give the L^1 bound, uniform over sectors, of the one Fourier measure that separates the
      whole-product kernels and inverse roots. That the measure is rectangle-blind is structural:
      it is a function of whole-product norms on a box common to both rectangles (l. 13105,
      13325-13331, 13913-13915). Its size is the imported part.
  (ii) the manuscript's assertions that no clipping, supremum or one-rectangle omission occurs in
      the Theta branch (l. 12827-12828, 14086, 14703-14705, 14786). Here they are confirmed in the
      displayed text. At n = 3 they carry more weight than at n = 6, because even an O(theta_N)
      fixed-ratio asymmetry there would be fatal (Sec. 4.3).
  (iii) no human analytic number theorist has checked any of this.
```

RH is unsolved. This note does not prove or disprove RH, Lemma 18.1 or any moment bound. "Closed"
means: at the level of the displayed steps of the manuscript, the condition left open by the
centred attack holds in the precise sense the cubic route needs (Sec. 1.3), and the steps that
violate its literal wording cost nothing (Sec. 4). It does not mean that any step is proved. The
float numerics are EMPIRICAL and small-scale.

## 0. Verdict

**(a) Closed.** The literal condition, that *every* step of l. 13114-14310 acts identically on both
rectangles, is **false**, and the manuscript says so. On rows whose child character lies outside
`Θ`, l. 14119-14300 split the centred child into its two rectangles by the triangle inequality.
They then omit or clip each rectangle separately: "Different rectangles can have different
clipped totals" (l. 14156); "No common clipped reduction is used for the signed difference"
(l. 14179).

The literal condition is also not what the route needs. What it needs (Sec. 1.3) is narrower:
every operation **before the `Θ`/non-`Θ` row split, and every operation in the `Θ` branch**,
must act identically. That holds at every displayed step. There are exactly three asymmetries,
and none costs a multiple of `M` at `n = 3`:

| asymmetry | lines | cancellation used there? | cost at n = 3 (exact, units of M) |
|---|---|---|---|
| comparison lengths: `Y_1 = Z^L` is the shortest of the four plains | 12988-12990 | yes (it *sets* `r`) | 0 beyond the ledger: `min` of the four lengths is exactly `L` on every core input [E1] |
| triangle split, per-rectangle omission and clipping on non-`Θ` rows | 14119-14300 | no | 0·M; absolute `≤ 2θ_N < ξ/4` per edge (eq:centered-clipped-shell), inside `C_*ξ` [E4] |
| `Θ`-branch fallback when `r̃_1 ≥ r` or `r = 0`: an identically zero rectangle stays in the formal difference | 14701-14706 | no (absolute volume) | 0: already the `(r − r̃_1)_+ = 0` line of (2.18), (2.18h) |

The `n = 3` differences cannot create a new asymmetry: sextic versus cubic Gauss sums, the
quadratic twist `χ_p³`, the reciprocity laws, and the unit and conductor data. The reason is
structural (Sec. 3). Each of them is a function of a row, of frozen labels, or of a **whole**
column product `u = Π l_1 l_2`. Both rectangles are summed against the same such factor. The
rectangle label enters only through the smooth weight `D_𝐛`.

Lemma `centered-coefficient-invariant` (l. 13954) is therefore order-free, as the centred attack
said. Its rectangle content was traced here step by step (Sec. 2). With that, the
centred-attack statement in its Sec. 4 no longer needs its rectangle hypothesis (at the level of
the displayed steps): the `Θ`-row children satisfy (2.18) with `r = (L − v)_+`, with no loss `cM`, `c > 0`.

**What a failure would have cost, for scale** [E2, E3]. The cubic route needs the `Θ`-row main
terms to cancel to relative precision `Z^{−κ*}` with `κ* = (5/6)L`, which is
`215/612 ≈ 0.351M` at the top (`δ = 0`). A full mismatch leaves the deficit `A − 2M/3`. That is
`M/3` at `A = M`, which is `144/11 ≈ 13.1` times the tolerance `11/432` for a loss confined to
the centred deficit. Even a **fixed-ratio** mismatch (`κ = 0`), the size of one subunit-scale
clip, would be fatal in the `Θ` branch. The manuscript keeps every such operation out of that
branch (Sec. 4.3).

## 1. What "the two rectangles" are

### 1.1 Three different pairs

The proof manipulates three different pairs. Only the second is "the two rectangles".

| pair | index | what it is | may the two members differ? |
|---|---|---|---|
| **plains** | `i = 1, 2` | the two plain variables `l_1, l_2` (the two factors `S(X_1)`, `S(X_2)` of one product) | in scale (`X_1 ≠ X_2`) and profile (`W_1 ≠ W_2`); **not** in character, mask or norm power (l. 13965-13966) |
| **rectangles** | `ϱ ∈ {X, Y}` | the two terms of `D_𝐛` (old-eq:2.18a, l. 13018-13024): the original product `S(X_1)S(X_2)` and the comparison `S(Y_1)S(Y_2)`, with `Y_1 = Z^L`, `Y_2 = X_1X_2/Y_1` (l. 12988-13004) | only in the individual scales. The product `X_1X_2 = Y_1Y_2`, the profiles ("the same two profiles", l. 12954), the extracted `𝐛`, the character, mask and `t` must agree |
| **sides** | `j = C, D` (first transform), `u, v` (second) | the two factors of a squared norm: `Δ_k` and `\overline{Δ_k}`, then the two columns of the Gauss-row norm | yes: "The two sides of one squared Gauss norm may have different norm powers; their inducing characters differ by a member of `Θ`" (l. 13966-13968). The lattice saving is taken on one side only (l. 14694-14706) |

**Answer to the question in the task.** "The two rectangles" are neither the two factors of one
product of smoothed character sums (those are the plains) nor the two transforms' output boxes.
They are the two **equal-product boxes** `[X_1] × [X_2]` and `[Y_1] × [Y_2]` in the
`(log q_{l_1}, log q_{l_2})`-plane. Both lie on the same anti-diagonal
`log q_{l_1} + log q_{l_2} = A log Z`.

**Each side contains both rectangles.** The coefficient `A_C(a)` "contains the entire allocated
difference" (l. 13225-13226), and so does `B(u)` in the second transform (l. 13600-13601). So the
transforms never separate the rectangles: they act on one column coefficient whose smooth weight
is the signed difference.

### 1.2 What the cancellation uses

On a `Θ`-row child, after the live slots are fixed, the plain coefficient is
`ϑ(l_1)ϑ(l_2) 1_{(l_1l_2,𝔑_*)=1} q_{l_1l_2}^{it} D_𝐛(l_1,l_2)` (l. 13970-13976). The lattice
lemma writes the sum as `𝓛_1(U_1)𝓛_2(U_2) − 𝓛_1(V_1)𝓛_2(V_2)` (l. 14660-14664). Both product
main terms equal `c²_{ϑ,𝔑_*} T^{1+it} I_1(t) I_2(t)`, so they cancel. For that, every one of
the following must be the same in both rectangles:

* **(R1)** the character `ϑ`, the mask `𝔑_*` and the norm power `t`. Each is common to both plains
  and both rectangles.
* **(R2)** the profiles `W_1, W_2`, so that `I_1, I_2` agree.
* **(R3)** the product of the post-extraction scales: `U_1U_2 = V_1V_2 = T`.
* **(R4)** every non-smooth factor multiplying the coefficient. It must be a function of the
  row, of frozen labels, or of whole-product norms, and never of an individual plain norm.

**(R5)** All four scales must be at least `Z^r`. This condition is *intentionally asymmetric*:
the comparison's `Y_1 = Z^L` is the smallest scale, and it sets `r`.

The float control P1-OBS (Sec. 5) shows that (R3) is all that is needed of the extraction. The
same `𝐛` in both rectangles is sufficient, not necessary. A "cross" allocation `𝐛_X = (p, 1)`,
`𝐛_Y = (1, p)` keeps equal products, and it still cancels: rel `5·10⁻⁶`, against `6.0` when
only one rectangle is extracted.

### 1.3 The precise meaning of "acts identically"

For the `n = 3` transfer to suffer no loss of order `M`, an operation `𝒪` among those applied
between the centred input and a `Θ`-row child must satisfy:

> `𝒪` is linear in the smooth weight. On the term `W_1(q_{b_1}q_{l_1}/S_1)W_2(q_{b_2}q_{l_2}/S_2)`
> it acts by a rule that depends on `(S_1, S_2)` only through `S_1S_2`, which is common, or not at
> all. It multiplies by factors that are functions of the row, of frozen labels or of
> whole-column norms. It updates the scales of the two rectangles by the same divisor (or, more
> generally, by divisors with equal products).

Operations **after** the `Θ`/non-`Θ` split on non-`Θ` rows are exempt. There, the bound is
`|Δ'|² ≤ 2|S_X'|² + 2|S_Y'|²`, and each rectangle is estimated by the induction hypothesis at
the smaller width. No cancellation between the rectangles is used.

## 2. Step-by-step: l. 12940-14310 (and the Θ application to 14740)

Legend:

* **S**: symmetric (same operation, same parameters, on both rectangles).
* **S\***: symmetric because it acts on the whole column coefficient, which contains both
  rectangles.
* **A**: asymmetric.
* **"n = 3"**: what changes for the cubic family, and whether that change can act per rectangle.

| # | step (lines) | rectangle handling | sym. | n = 3 |
|---|---|---|---|---|
| 0a | reflection of long plains, coefficient mass in `d_0, h_0`, rowwise scale supremum (12780-12828) | done **before** centring (12825-12826); row-dependent scales are replaced by fixed box scales and their derivative profiles | n/a (precedes the rectangles) | cubic functional equation, `Γ(s)/Γ(1−s)`, `\|ε_k\| = 1` (CUBIC_CENTRED_ATTACK [R1]); row data only |
| 0b | comparison construction (12940-13010) | `Y_1 = Z^L`, `Y_2 = X_1X_2/Y_1`, "the same two profiles" (12954), exact product (12990) | **A by design** (lengths) | the cubic `L ≈ 0.42M` instead of `M/4`; `min` of the four lengths is still exactly `L` under the caps [E1] |
| 0c | centred coefficient `D_𝐛`, impossible allocations (13018-13029) | "the formal difference … is nevertheless retained" when one rectangle's profile is zero | S (formal) | none |
| 0d | aggregate support convention (13090-13110) | "Both rectangles use that same box" (13105) | S | order-free |
| 1 | row-ball majorant and the support "in either rectangle … fixed multiple of `X`" (13115-13122) | one product box, since `X_1X_2 = Y_1Y_2` | S | none |
| 2 | whole-dyad localization (13124-13178) | "depends only on the sector, never on a live column" (13141); sector = aggregate outer norms | S | none |
| 3 | zero frequency (13180-13191) | absolute count of powerful products; `\|A_C\| ≤` sum over both rectangles | S\* (bound, no cancellation) | `≡ 0 (mod 3)` still forces powerful; `O(X^{1+ε})` (CUBIC_N3_GAPS Sec. 3.1) |
| 4 | complete common support `C, D`, valuation allocation (13192-13208) | "the same ideals `𝔟_i` occur in the two terms of `D_𝐛`" (13203-13204) | S | `𝔯 = {3 ∤ i − j}` (CUBIC_N3_GAPS [A-B1]); acts on valuations of the **whole** product |
| 5 | row character `χ_C\bar χ_D = ξ_𝔯 1_{(k,𝔠/𝔯)=1}`, Möbius `𝔢` (13209-13224) | row factors; mask on every residual factor of the side | S | cubic `ξ_𝔯` primitive [A-B2] |
| 6 | Poisson in `k`, bridge (eq:first-poisson-bridge, 13226-13268) | linear in `A_C(a)\overline{A_D(b)}`, which contain the whole difference; Gauss sums `G(a,h)` of the **whole** column | S\* | cubic Gauss sums (Lemma G3); still functions of `a` only |
| 7 | CRT phases and reciprocity (13258-13276) | `χ_a(𝔢𝔯)`, `ξ_𝔯(a)`, `\bar R(a,b)`: characters on whole columns | S\* | `R ≡ 1` (cubic reciprocity, [S2]); fewer phases, none per rectangle |
| 8 | Möbius `s` on noncoprime pairs (13300-13306) | condition `s \| a, b` on whole columns | S\* | none |
| 9 | kernel and inverse-root separation (13307-13331) | kernel `Φ̂_1(R x/(y_1y_2))` in **whole-product** norms on "the common product annulus"; "no separate powers on the two plain variables or the two rectangles" (13330) | S | none (imported: kernel-seminorms) |
| 10 | Cauchy-Schwarz in `h`, `N_C` (13331-13348) | after the separation; "the two rectangles retain the same allocated plain powers, character, puncture, and norm power" (13347-13348) | S | none |
| 11 | Gauss-row enlargement, zero slots (13446-13452) | positivity: `N_C` ≤ the norm over a larger smooth ball; no row multiplication | S\* | none |
| 11' | amplifier (z > 0 only; 13453-13570) | "the same allocation updates `D_𝐛` in both rectangles" (13492); the row phase "multiplies both rectangles" (13539) | S | not used in case 1 |
| 12 | Gauss-row zero `h = 0` (13572-13594) | absolute bound, `\|B(u)\|` over both rectangles | S\* (bound) | cubes: `O(Y^{1/3})`, `s_0 ≤ a_0/3` (CUBIC_N3_GAPS Sec. 3.1) |
| 13 | second Poisson in `h`, exact `F(u,v;j)` (13596-13625) | `B(u)` contains the whole difference (13600-13601); kernel `Φ̂_2(Z^{K+g}q_j/(q_uq_v))` in whole columns | S\* | cubic correlations (Lemma FC3) are functions of `u, v` |
| 14 | diagonal `j = 0` (13626-13650) | absolute: `F(u,u;0) = φ(u)`, count `Y_col/q_s` | S\* (bound) | none |
| 15 | localization of `j ≠ 0` (13652-13684) | "genuine full `(u,v,j)` sum before any extraction"; common row weight `Ω_ret` | S | none |
| 16 | complete support `D_2, E_2`, local tables, row factor `χ_n(G_cV_id h')` (13686-13790) | extracted powers allocated as at step 4; each extracted prime punctures **all** residual factors on its side; row scalars | S | cubic tables [T1-T3]; unequal `j_0 = 3` case; whole column |
| 17 | `𝔱`-Möbius and factor allocation (13867-13933) | "replaces both `X_i, Y_i` by `X_i/q_p, Y_i/q_p`. It introduces no one-variable puncture" (13924-13926); "the product of the two new plain scales is equal in the two rectangles" (13931) | S | none (order-free; A5) |
| 18 | second kernel separation (13899-13916) | "common to them, to both rectangles, and to the row" (13915) | S | none (imported) |
| 19 | child characters `τ_1ρχ_n(G_cV_id h')`, `ρ,ρ' ∈ Θ` (13937-13950) | side data; the ratio `ρ/ρ'` relates **sides**, not rectangles | S | `ρ = ρ' = 1`, `χ_n(−1) = 1` |
| 20 | raw child normalization (13998-14090) | `T_j` is "the common formal pre-`𝔱` product of the two plain scales in its rectangles"; the divisor `q_{d_{j,i}}` divides "in both rectangles" (14043-14044); "No clipping has occurred" (14086) | S | none |
| 21 | `Θ`/non-`Θ` split by row (14104-14118) | the split is by **row** `h'`, so it is common to both rectangles. On `Θ` rows the code takes "a pointwise absolute product" of the two **sides**, each still a signed difference | S | `Θ_3` = 27 characters; the cube rows `(h') = 𝔥_0𝔳³` decide which rows are `Θ` rows, not how the rectangles are treated |
| 22 | non-`Θ` rows: triangle inequality, per-rectangle omission and clipping, induction call (14119-14300) | "first bound a centered child norm by the sum of the norms of its two rectangles" (14122-14123); "Omit a rectangle only when …" (14128); "Different rectangles can have different clipped totals" (14156) | **A** | order-free lengths; cost `≤ 2θ_N` (eq:centered-clipped-shell); calls the full case 1 at width `≤ M − σ` |
| 23 | `Θ` rows, uncentred volume (14392-14440) | absolute volume per side "at every positive formal scale, including subunit scales" (14400-14404) | S\* (bound) | count `Z^{(m'−f)/3}` |
| 24 | `Θ` rows, centred application of Lemma 18.3 (14681-14740) | first side: four formal post scales `≥ Z^{r−r̃_1}`; "No formal centered scale is clipped in this branch, and an identically zero rectangle remains in the formal difference" (14703-14705) | S (fallback **A**, but uses volume only) | none: Lemma 18.3 is order-free (CUBIC_CENTRED_ATTACK Sec. 2.1) |

**Three points of the table checked against the text.**

* **Step 4 (allocation).** The allocation records the exact valuation of each common prime in each
  plain variable "once for the coefficient" (13201-13203). Both rectangles share the variables
  `l_1, l_2`, so they share the allocation. Which rectangle's profile can actually be nonzero for
  that allocation is a property of the smooth weight only. That is the "impossible for one
  rectangle" clause (13027-13029), which keeps the formal term.
* **Step 9 and step 18.** These are the only places where a non-multiplicative function of the
  plain norms enters, namely the kernels and inverse roots. In both, the variables are the *whole*
  column norms `y_1 = q_a/(X/q_C)`, `y_2 = q_b/(X/q_D)` (first transform) and `q_{D_2}q_a`,
  `q_{E_2}q_b` (second). Their boxes are fixed by the product convention (13102-13105). That
  convention is the same for both rectangles, because `X_1X_2 = Y_1Y_2` and the same `𝐛` is
  divided out. Float control P2-CTRL shows what is excluded: a kernel in one plain norm,
  `K(q_{l_1}/√T)`, destroys the cancellation (rel `0.97`). The whole-product kernel `K(q_{l_1}q_{l_2}/T)`
  keeps it (rel `5·10⁻⁶`).
* **Step 21 versus step 22.** The asymmetric operations of step 22 come strictly after the row
  split. Step 22 applies to non-`Θ` rows only (14119-14300). The `Θ` rows are treated in
  14312-14740 with the formal, unclipped scales (14086, 14703, 14786). The reflection-time
  suprema are excluded from centred `Θ` differences by 12827-12828.

## 3. The four n = 3 differences, one by one

The task asks whether any asymmetry survives at `n = 3` because of the Gauss sums, the quadratic
twist, the reciprocity laws, or the unit and conductor data. The answer is the same for all four,
and for the same reason.

**Structural lemma (reading of l. 13072-13084 and steps 4-19).** Every arithmetic factor that the
transforms introduce has one of three forms:

1. a function of a row variable (`k`, `h`, `j`, `h'`) and of frozen labels;
2. a zero-extended character, Gauss sum or correlation of a **whole** column (`a`, `b`, `u`, `v`,
   or their residuals), which factors over `l_1, l_2` and the slots by complete multiplicativity
   (l. 13072-13082);
3. a mask on every residual factor of a side.

None of these depends on which rectangle a term comes from. The rectangle label appears only in
the smooth weight `D_𝐛`. So no arithmetic change, at any order `n`, can make a step act
differently on the two rectangles. It can only change *what* the common factor is.

| n = 3 difference | where it enters | form | per-rectangle? |
|---|---|---|---|
| cubic vs sextic Gauss sums `G(p^a, k)` (vanishing unless `3 \| a` at `k = 0`; `\|G\| = P^{(a−1)/2}` when `3 ∤ a`) | steps 6, 12, 13 | 2 | no |
| quadratic twist `χ_p³`: for `n = 6` the cube is the quadratic symbol [X1-CTRL]; for `n = 3` it is principal on units [X1], so an exponent `≡ 0 (mod 3)` gives the mask `1_{p∤·}` | steps 4, 5, 16, 19 (classification of `𝔯`, of `e_p`, of the `Θ` rows) | 2 or 3 | no. It changes which primes are `𝔯`-primes and which rows are `Θ` rows. Both are decided on the whole product or the row [X2] |
| reciprocity: sextic bicharacter `R(a,b)` split as `ρ(a)ρ'(b)` (13937-13948), vs cubic `R ≡ 1` | steps 7, 16, 19 | 2 (`ρ` is a ray character on the whole column) | no; at `n = 3` the factor is absent |
| units and conductor: `O^× = μ_6` in both cases; `χ_n(−1)` nontrivial for `n = 6`, trivial for `n = 3`; 27 `S`-numerator characters (mod 18) instead of `6^{\|S\|+1}`; conductor bound `C_k q_{𝔑_0,k} ≪ Z^M` (tame at good primes) | step 0a (reflection, before centring), step 19, the lattice classes in Lemma 18.3 | 1 or 2 | no; the lattice lemma's `c_{ϑ,𝔑_*}` is independent of the scale, so both rectangles get the same constant (l. 14638-14648) |

[X2] checks the one place where the convention matters. The column factor attached to `(l_1, l_2)`
must depend only on `l_1 l_2`, also when `l_1` and `l_2` share a prime and the row is divisible by
it. With the manuscript's zero extension ("a present prime whose total exponent is divisible by six
gives the zero-extended principal factor, not the constant one", l. 13080-13081, with `6 → 3`),
this holds exactly. There were 0 mismatches in 3,999 random (split, split', row) triples. The
wrong convention, "constant 1 at exponent `≡ 0 (mod 3)`", makes it split-dependent (233
mismatches). That control concerns plains, not rectangles. It shows that the full-product
property is a real requirement and that the cubic symbols meet it.

## 4. Quantification (EXACT, `M = 1`; rect_exact.py, 12/12)

The closing model is that of SKETCH Sec. 3.5. The centred `Θ`-row deficit is
`D(v) = A − 2/3 − (5/6)v − s(v)`, with `L = L_j(A) = (6/5)(A − 2/3 + μ)`. Closing needs
`max_v D ≤ −μ`, and the tolerance for a loss confined to (C) is `c* = (11 − 147δ)/432`.

### 4.1 The designed asymmetry (comparison lengths) costs nothing [E1]

* Under the caps, on every core input `n_1 ∈ [A − 1/2, 1/2]` (padded for `A > 1`), the minimum of
  the four plain lengths `min(n_1, n_2, L, A − L)` equals `L` exactly. The check uses grids of 200
  values of `A` per stage, with 21 values of `n_1` each, for `δ = 0` and `δ = 1/100`.
* The original plains exceed `L` by at least `4/51 ≈ 0.078` (`δ = 0`) and `707/10200 ≈ 0.069`
  (`δ = 1/100`). Both exceed `μ*` (`0.018`, `0.016`) [E1b].
* So the saving `r = (L − v)_+` of the cubic ledger is exactly what the asymmetric construction
  provides. The original rectangle never binds.
* Padding `ξ ≤ μ` keeps this.

### 4.2 The non-Θ asymmetry costs 0·M [E4]

The per-rectangle clipping enters only through `π_{j,ϱ} ≤ θ_N` and the paired bound
eq:centered-clipped-shell, `≤ 2θ_N`. The localization threshold
(eq:centered-localization-threshold) gives `2θ_N < ξ/4`. The edge cost
(eq:centered-child-edge-cost) is `δ_fr,2 + δ_fr,1/6 + η + 7θ_N/3`, inside `C_*ξ`. None of these
is a multiple of `M`. In the model, its coefficient of `M` is `0 < c*`.

**The `n = 3` question for this branch.** Does each rectangle's child have a valid induction
call? Yes. The child width is `≤ M − σ` (old-eq:2.13), and the completed smaller widths include
the unrestricted zero-slot assertion (l. 14209-14210, 14279-14280, 14797-14798). The cubic route keeps that
order; (H-B) only reorders centred stages *within* a width. So there is no loss.

### 4.3 What an asymmetry in the Θ branch would cost [E2, E3]

| model | requirement / loss | δ = 0 | δ = 1/100 |
|---|---|---|---|
| mismatch of relative size `Z^{−κ}`, saving `min((L−v)_+, κ)` | closes iff `κ ≥ κ* = (5/6)L = A − 2/3 + μ` (sharp on every grid `A`) | `κ*(top) = 215/612 ≈ 0.351` | `4393/12240 ≈ 0.359` |
| full mismatch (`κ = 0`), e.g. a fixed-ratio clip or one rectangle's own mask | deficit `A − 2/3` at `v = 0` | `1/3`, i.e. `144/11 ≈ 13.1 · c*` (`c* = 11/432`) | `103/300`, i.e. `14832/953 ≈ 15.6 · c*` |
| for comparison: all-stage bound | `c < 1/12` (red team [T3]) | exceeded | exceeded |

So the condition is all-or-nothing, as the centred attack said. A mismatch smaller than
`Z^{−0.351M}` in relative size is harmless. A larger one is fatal, and every natural asymmetric
operation (one-rectangle clip, extraction, mask or kernel) is of size `Z^0`. **In particular an
`O(θ_N)` asymmetry, harmless in the non-`Θ` branch, would be fatal in the `Θ` branch.** Float
control P5-CTRL makes this concrete: a fixed factor `e^{0.5}` on one scale of one rectangle
leaves rel `0.65`, against a common rel `≤ 2.75·10⁻³`.

This is why the three manuscript sentences in gap (ii) of the header are load-bearing for the
cubic route: 14086, 14703-14705 and 14786. In the sextic proof the same sentences are equally
necessary. Its tolerance is larger (`1/9` for a whole-deficit loss), but a full mismatch also
breaks it (`A − 5M/6` at `v = 0`, i.e. `M/6 > 0`).

### 4.4 Answer to item 3

No asymmetry was found that costs a multiple of `M`. The worst-case loss at `n = 3` from the
asymmetries that exist is `L = 0·M + O(θ_N)`, with `2θ_N < ξ/4` per edge. That is below the
tolerance `c* = (11 − 147δ)/432` for every `δ < 11/147`, and it is already budgeted in the
`C_*ξ` edge allowance. In the README's exponent model the loss is exactly `0`.

## 5. Numerics (both_rectangles.py; EMPIRICAL except Part X)

### 5.1 Design

* **Part X (EXACT).**
  * [X1] For 3,027 pairs `(u, p)`, with 77 primes of norm `≤ 400`, the cubic symbol computed
    independently as `u^{(Np−1)/3} mod p` equals `eis.sym_prime²`. Its cube is principal on units.
  * [X1-CTRL] The cube of the sextic symbol is the quadratic symbol; both values `±1` occur.
  * [X2] The full-product property, as in Sec. 3.
* **Part F (float).** This is a plain-level mini-pipeline of the operations of Sec. 2 that touch
  the smooth weight, applied to a centred `Θ`-row coefficient. It does not run the two transforms
  themselves. Their arithmetic is rectangle-blind by Sec. 3, and each of their identities is
  linear in the column coefficient. Check D of LEMMA18_1_COMMON_SUPPORT verified the bridge with
  general coefficients; CUBIC_N3_GAPS [A-B3], [C1], [E] verified the cubic factorizations.
  * **Index set.** All primary `z ≡ 1 (mod 3)` of odd norm `≤ 10⁷`: 3,022,972 ideals prime to 6.
  * **Character, mask, profiles.** `ϑ = 1`, with nonprincipal sanity cases `(2/·)_3` and
    `(2/·)_3(ω/·)_3`. The mask is `π_13 π_19`. The profiles are a real bump `W_1` and a complex
    tilted bump `W_2` on `[1/4, 4]`.
  * **Geometries.**
    * cubic `C_2` top: `A = M`, `L = 43/102`, `Z = 1.06·10¹¹`;
    * cubic `C_2` bottom: `A = 31/36`, `L = 0.2549`, unbalanced core `(1/2, 0.361)`,
      `Z = 3.3·10¹⁰`;
    * sextic: `A = M`, `L = 1/4`, `Z = 3.2·10⁸`.

    In each, `Z` is the largest value for which the longest plain window fits in the index set.
  * **Operations.** Each was run in its common form and in one asymmetric form (CTRL):
    * P1: extraction `𝐛_1 = π_7` with the residual punctured;
    * P2: a whole-product kernel. This is an exact finite sum `Σ w_k (q_{l_1}q_{l_2})^{iτ_k}`, so
      it is a whole-product function by construction and is **not** a test of
      lem:kernel-seminorms;
    * P3: one norm power `t = 2.5`;
    * P4: the `𝔱`-allocation `n_1 = π_7' l_1`;
    * P5: a clip-type scale change, run as a control only;
    * P6: all of P1-P4 together.
* **Pre-registered criteria**, fixed before the first run:
  * a common pipeline passes if `rel ≤ 40·2^{ω}/minscale`, the shape of Lemma 18.3 with the
    attack's constant;
  * a control is detected if `rel ≥ max(10 × the largest common rel in that geometry, 0.02)`;
  * a common check whose bound is `≥ 0.5` is reported UNINF and not counted.

### 5.2 Results (run 1, the only run of this script)

Cubic `C_2` top (`Z = 1.06·10¹¹`; all checks informative):

| pipeline | common rel | `r_obs` (`r_minscale`) | control rel |
|---|---|---|---|
| P0 baseline | `1.3·10⁻⁶` | 0.534 (0.422) | — |
| P1 extraction `π_7`, both rectangles | `1.1·10⁻⁴` | 0.360 (0.345) | X only: `6.0` |
| P1-OBS cross allocation (equal products) | `5.2·10⁻⁶` | 0.479 | — |
| P2 whole-product kernel | `5.1·10⁻⁶` | 0.480 (0.422) | kernel on plain 1: `0.97` |
| P3 one norm power, whole product | `1.1·10⁻⁵` | 0.448 (0.422) | on plain 1 only: `1.22` |
| P4 `𝔱`-allocation, both rectangles | `4.2·10⁻⁵` | 0.397 (0.345) | one-variable puncture in Y: `0.143` |
| P5 clip-type `e^{0.5}` on one scale of Y | — | — | `0.65` |
| P6 full pipeline (min scale 906) | `2.75·10⁻³` | 0.232 (0.268) | extraction in X only: `0.85`; kernel on plain 1 in Y: `0.98`; mask `+π_5` in Y: `0.083` |
| P7 nonprincipal `ϑ` | — | `\|S_ϱ\|/T' ≤ 3·10⁻⁸` | — |

Every common pipeline passes its bound. Every control is detected, at between 30 and about 2,200 times
the largest common rel (`2.75·10⁻³`).

* **Cubic `C_2` bottom** (min scale 480; with both extractions, 10):
  * P0, P2 and P3 pass (rel `8·10⁻⁴`, `3·10⁻³`, `1.5·10⁻²`). P1, P4, P6 and P7 are UNINF.
  * Seven of the eight controls are detected.
  * **FAIL: P4-CTRL** (rel `0.101` < `0.154`). See Sec. 5.3.
* **Sextic** (min scale 134): every common check is UNINF, and so the controls are UNINF too.
  For the record, the controls gave rel `0.16-6.0`, against common rels `3·10⁻⁴` to `4.5·10⁻²`
  (P6 `0.57` at min scale 3).

### 5.3 Reading, the FAIL, and limits

* **What the numerics show.** At the cubic top geometry, every operation of Sec. 2 that the
  manuscript applies in common form keeps the `Θ`-row main terms cancelling. The achieved
  `r_obs` is close to `log_Z(min scale)`, as Lemma 18.3 predicts. Each one-rectangle or one-plain
  variant leaves a non-cancelling term of main-term size. That includes the clip-type variant,
  which is why clipping must stay out of the `Θ` branch.
* **The FAIL.** P4-CTRL inserts a one-variable puncture at a prime of norm 7 in one rectangle. The
  predicted main-term mismatch is a fraction of about `1/7 ≈ 0.14`; it was observed as `0.143`
  at the top geometry. At the bottom geometry the largest common rel is `0.0154`, from P3 at
  min scale 480. So the pre-registered factor 10 would need `0.154`, and the observed `0.101`
  falls short. This is a scale limitation, not evidence that the symmetric operation fails: the
  common pipeline P4 is itself UNINF there. The criterion was not loosened. The FAIL stays in
  the log and is reported here.
* **Limits.**
  * Float64, finite scales: the largest min scale is `4.4·10⁴`.
  * The transforms are not run. Part F tests the property each operation must have (Sec. 1.3),
    not the manuscript's text. The text was checked by reading (Sec. 2).
  * No asymptotic statement is inferred from these numbers, and no exponent was fitted.
  * The sextic geometry is too small to be informative at this index-set size. The centred
    attack's Sec. 3.3 met the same limit.

### 5.4 Changes between runs (rect_exact.py only)

Run 1 gave 10/12, because two checks failed: E1b at `δ = 0` and at `δ = 1/100`. E1b asserted that
the smallest excess of the original plains over `L` *equals* `μ`. That was mis-specified.
`L_j(A)` is the **smallest** admissible `L`, so the cap `L ≤ A − 1/2 − μ` is not binding, and the
excess is larger: `4/51` and `707/10200`.

Run 2 asserts the property that the argument uses, "excess `≥ μ`", and passes. Run 2 also changed
the E1 print label from `(= mu = …)` to `(mu = …)`; the old label falsely suggested equality.
No other criterion was changed. Run 1's script has sha256 `09076e2c…13579f5b15`.

## 6. Corrections and observations for the earlier notes (no change to their conclusions)

1. **README and CUBIC_CENTRED_ATTACK, wording of the open item.**
   * "Every step of l. 13114-14310 acts identically on both rectangles" is literally false.
     l. 14119-14300 act per rectangle on non-`Θ` rows.
   * The correct condition is: identically on both rectangles at every step before the row split
     (l. 14108) and at every step on `Θ` rows. This holds at the level of the displayed text.
   * The per-rectangle steps cost `≤ 2θ_N`.
2. **CUBIC_CENTRED_ATTACK Sec. 1.2, list of operations.** "the absolute values" should be read as
   absolute values of **sides** on `Θ` rows (each side still a signed difference, l. 14111) and
   of rectangles only on non-`Θ` rows. The attack's [C-CTRL] already showed that a one-rectangle
   absolute value on `Θ` rows would be fatal.
3. **Robustness observation.** The lattice step needs equal products (R3), not literally the same
   `𝐛` in both rectangles (P1-OBS). This is not used by the manuscript, which uses the same
   `𝐛`. It shows that the requirement on the allocation is weaker than the wording "the same
   allocated plain powers" (13347).
4. **Where the cubic route is more fragile than the sextic proof on this question.** Nowhere in
   kind; both need exact symmetry on `Θ` rows. In degree, a full mismatch costs `M/3` against a
   tolerance `11/432` (cubic) versus `M/6` against `1/9` (sextic). The tightest quantitative
   point of the cubic route is still the `κ = 5/6` bound at `v = L` (CUBIC_CENTRED_ATTACK Sec. 4,
   item 2). This note does not touch it.

## 7. Status of the route after this note

The route is unchanged: PROPOSED, CONDITIONAL on (H-A) and (H-B), and OPEN.

* **Resolved.** The rectangle question is closed at the level of the displayed steps, so risk
  item 9 has no remaining rectangle-specific sub-question.
* **Still imported** (header gap (i)-(iii)):
  * the Fourier-measure lemmas;
  * the manuscript's own correctness in the lines read;
  * the absence of a human check.
* **Not reviewed here:** the `κ = 5/6` bounds (Lemmas 4.F, 4.G of SKETCH), the cubic functional
  equation for reflection, and (H-B).

## Appendix A: rect_exact.py (exact text that was run, run 2)

```python
"""Exact (Fraction) exponent model for the both-rectangles question, cubic route, M = 1.
Closing model of proposed/CUBIC_FOURTH_MOMENT/SKETCH.md Sec. 3.5:
  centred Theta-row deficit  D(v) = A - 2/3 - F(v) - s(v),  F(v) = (5/6) v  (kappa = 5/6 bound),
  lattice saving s(v) = (L - v)_+  when the two rectangles act identically,
  L = L_j(A) = (6/5)(A - 2/3 + mu),  closing needs  max_v D(v) <= -mu.
Questions:
  E1  the comparison asymmetry (Y_1 = Z^L is the shortest of the four plains) costs nothing: under
      the caps every original plain is >= L + mu, so min(four scales) = L exactly.
  E2  saving under a rectangle mismatch of relative size Z^{-kappa}: s(v) = min((L - v)_+, kappa).
      Closing holds for all v iff kappa >= kappa* = (5/6) L = A - 2/3 + mu.
  E3  full mismatch (kappa = 0, e.g. a fixed-ratio clip in the Theta branch): max_v D = A - 2/3,
      i.e. 1/3 at A = 1, against the (C)-only tolerance c* = (11 - 147 delta)/432.
  E4  the non-Theta asymmetries (per-rectangle clipping) enter only as absolute O(theta_N) terms:
      in units of M their coefficient is 0, so they are below any positive tolerance.
"""
from fractions import Fraction as F

ok = []


def rep(name, cond, detail=""):
    ok.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + name + ("   " + detail if detail else ""))


for delta in (F(0), F(1, 100)):
    mu = (11 - 147 * delta) / 612
    cstar = (11 - 147 * delta) / 432
    b1 = (4 + 7 * delta + 17 * mu) / 5
    top = 1 + delta
    stages = ((F(2, 3), b1), (b1, top))
    # E1: caps imply the four-scale minimum is L, for every core input n1 in [A - 1/2, 1/2]
    e1 = True
    worst_gap = None
    for (a0, a1) in stages:
        for k in range(1, 201):
            A = a0 + (a1 - a0) * F(k, 200)
            L = F(6, 5) * (A - F(2, 3) + mu)
            if not (L <= A / 2 and L <= A - F(1, 2) - mu):
                e1 = False                      # infeasible: caps fail (should not happen)
                continue
            lo_n = max(A - F(1, 2), F(0))
            for j in range(0, 21):
                n1 = lo_n + (min(F(1, 2), A) - lo_n) * F(j, 20)
                n2 = A - n1
                m4 = min(n1, n2, L, A - L)
                gap = min(n1, n2) - L
                worst_gap = gap if worst_gap is None else min(worst_gap, gap)
                if m4 != L:
                    e1 = False
    rep("E1 delta=%s: min of the four plain lengths is exactly L (Y_1) on every core input" % delta,
        e1, "smallest original-plain excess over L = %s (mu = %s)" % (worst_gap, mu))
    # run 1 asserted 'excess == mu' (mis-specified: L_j(A) is the SMALLEST admissible L, so the cap
    # L <= A - 1/2 - mu is not binding); run 2 asserts the property actually used: excess >= mu.
    rep("E1b delta=%s: that excess is >= mu (so a padding xi <= mu keeps Y_1 the shortest)" % delta,
        worst_gap >= mu, "min excess %s = %.4f vs mu = %.4f" % (worst_gap, float(worst_gap), float(mu)))

    # E2: mismatch tolerance kappa* = (5/6) L at each A; at the top it is A - 2/3 + mu
    e2 = True
    for (a0, a1) in stages:
        for k in range(1, 101):
            A = a0 + (a1 - a0) * F(k, 100)
            L = F(6, 5) * (A - F(2, 3) + mu)
            ks = F(5, 6) * L

            def maxD(kappa):
                vs = [L * F(i, 600) for i in range(0, 601)] + [L - kappa, L + F(1, 10)]
                vs = [v for v in vs if v >= 0]
                return max(A - F(2, 3) - F(5, 6) * v - min(max(L - v, F(0)), kappa) for v in vs)

            if not (maxD(ks) <= -mu and maxD(ks - F(1, 10 ** 6)) > -mu):
                e2 = False
    Ltop = F(6, 5) * (top - F(2, 3) + mu)
    kst = F(5, 6) * Ltop
    rep("E2 delta=%s: Theta-row cancellation must hold to relative Z^{-kappa*}, kappa* = (5/6)L "
        "(sharp on every grid A)" % delta, e2,
        "at the top A = %s: kappa* = %s = %.4f M" % (top, kst, float(kst)))

    # E3: full mismatch: max deficit A - 2/3 at v = 0; compare with c*
    full = top - F(2, 3)
    rep("E3 delta=%s: full rectangle mismatch leaves deficit %s = %.4f M at v = 0; tolerance c* = %s "
        "= %.4f M; ratio %s" % (delta, full, float(full), cstar, float(cstar), full / cstar),
        full > cstar)
    rep("E3b delta=%s: it also exceeds the all-stage bound 1/12" % delta, full > F(1, 12))

    # E4: non-Theta asymmetry = absolute 2 theta_N (<= xi/4 by eq:centered-localization-threshold):
    # coefficient of M is 0 < c*
    rep("E4 delta=%s: per-rectangle clipping (non-Theta branch) has M-coefficient 0 < c* = %s" % (delta, cstar),
        F(0) < cstar)

print("SUMMARY %d/%d" % (sum(ok), len(ok)))
```

Output (run 2, `exact2.log`):

```
PASS E1 delta=0: min of the four plain lengths is exactly L (Y_1) on every core input   smallest original-plain excess over L = 4/51 (mu = 11/612)
PASS E1b delta=0: that excess is >= mu (so a padding xi <= mu keeps Y_1 the shortest)   min excess 4/51 = 0.0784 vs mu = 0.0180
PASS E2 delta=0: Theta-row cancellation must hold to relative Z^{-kappa*}, kappa* = (5/6)L (sharp on every grid A)   at the top A = 1: kappa* = 215/612 = 0.3513 M
PASS E3 delta=0: full rectangle mismatch leaves deficit 1/3 = 0.3333 M at v = 0; tolerance c* = 11/432 = 0.0255 M; ratio 144/11
PASS E3b delta=0: it also exceeds the all-stage bound 1/12
PASS E4 delta=0: per-rectangle clipping (non-Theta branch) has M-coefficient 0 < c* = 11/432
PASS E1 delta=1/100: min of the four plain lengths is exactly L (Y_1) on every core input   smallest original-plain excess over L = 707/10200 (mu = 953/61200)
PASS E1b delta=1/100: that excess is >= mu (so a padding xi <= mu keeps Y_1 the shortest)   min excess 707/10200 = 0.0693 vs mu = 0.0156
PASS E2 delta=1/100: Theta-row cancellation must hold to relative Z^{-kappa*}, kappa* = (5/6)L (sharp on every grid A)   at the top A = 101/100: kappa* = 4393/12240 = 0.3589 M
PASS E3 delta=1/100: full rectangle mismatch leaves deficit 103/300 = 0.3433 M at v = 0; tolerance c* = 953/43200 = 0.0221 M; ratio 14832/953
PASS E3b delta=1/100: it also exceeds the all-stage bound 1/12
PASS E4 delta=1/100: per-rectangle clipping (non-Theta branch) has M-coefficient 0 < c* = 953/43200
SUMMARY 12/12
exit=0 wall=5s
```

## Appendix B: both_rectangles.py (exact text that was run, run 1)

<details>
<summary>both_rectangles.py (375 lines; sha256 fdb7152e…fe24cf20)</summary>

```python
"""Both-rectangles symmetry checks for the cubic (n = 3) transfer of Lemma 18.1, case 1.

EMPIRICAL / EXACT finite checks; nothing here is certified and nothing proves an asymptotic.

Part X (EXACT, integer arithmetic in Z[omega], a2/eis.py imported read-only):
  X1  cubic symbol: chi_p^3 = 1_{p does not divide u} (no quadratic twist); sextic chi_p^3 is the
      quadratic symbol (takes both values +-1).  Control: the sextic cube is NOT principal.
  X2  the column factor attached to (l1, l2) depends only on the full product n = l1 l2 (zero
      extension per prime exponent).  Control: 'constant-one at exponent = 0 mod 3' convention.
Part F (FLOAT, ordinary float64): a plain-level mini-pipeline of the operations that the two
  transforms apply to a centred Theta-row coefficient, each in a COMMON version (as the
  manuscript applies it) and a ONE-RECTANGLE / ONE-PLAIN version (control).  Statistic:
  rel = |S_X - S_Y| / |S_X| for principal theta.  PASS criteria fixed below BEFORE the run.

Run: nice -n 10 python3 -I both_rectangles.py <path to a2 directory>
"""
import math, sys, random, cmath
from fractions import Fraction as Fr
import numpy as np

A2 = sys.argv[1]
sys.path.insert(0, A2)
import eis as E  # read-only import

RESULTS = []


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ("   " + detail if detail else ""), flush=True)


# ----------------------------------------------------------------------------------------------
# Part X: exact
# ----------------------------------------------------------------------------------------------
def cubic_exp(u, p):
    """(u/p)_3 as exponent k mod 3 of omega, or None if p | u.  (u/p)_3 = (u/p)_6^2."""
    k = E.sym_prime(u, p)
    return None if k is None else (2 * k) % 6 // 2


def part_X():
    random.seed(20261010)
    ps = E.primes_upto(400)
    # X1
    ok_cubic, ok_cons, sext_vals, n_tested = True, True, set(), 0
    for p in ps:
        Np = E.norm(p)
        for _ in range(40):
            u = (random.randint(-500, 500), random.randint(-500, 500))
            if E.divides(p, u):
                continue
            n_tested += 1
            k6 = E.sym_prime(u, p)
            # independent: u^{(Np-1)/3} mod p must be the unit zeta^{2 k6} (cubic symbol = sextic^2)
            c3 = E.powmod(u, (Np - 1) // 3, p)
            z = E.UNITS[(2 * k6) % 6]
            if not E.divides(p, (c3[0] - z[0], c3[1] - z[1])):
                ok_cons = False
            # cube of the cubic symbol: u^{Np-1} = 1 mod p (principal on units)
            c9 = E.powmod(u, Np - 1, p)
            if not E.divides(p, (c9[0] - 1, c9[1])):
                ok_cubic = False
            # cube of the sextic symbol: u^{(Np-1)/2} mod p = +-1 (quadratic symbol)
            q2 = E.powmod(u, (Np - 1) // 2, p)
            if E.divides(p, (q2[0] - 1, q2[1])):
                sext_vals.add(1)
            elif E.divides(p, (q2[0] + 1, q2[1])):
                sext_vals.add(-1)
            else:
                sext_vals.add(None)
    check("X1 cubic symbol = (sextic symbol)^2, computed independently by powmod", ok_cons,
          "%d (u, p) pairs, %d primes of norm <= 400" % (n_tested, len(ps)))
    check("X1 cube of the cubic symbol is principal on units (no quadratic twist at n = 3)", ok_cubic)
    check("X1-CTRL cube of the sextic symbol is the quadratic symbol (takes both values +-1)",
          sext_vals == {1, -1}, "values seen: %s" % sorted(sext_vals, key=str))

    # X2: zero-extended product character, rectangle/plain split independence
    small = [p for p in ps if E.norm(p) <= 61][:8]

    def col_factor(exps, h, const_one=False):
        """product over primes of chi_p(h)^{e}; zero-extended: 0 if p | h and e > 0.
        const_one=True: the wrong convention 'exponent = 0 mod 3 gives the constant 1'."""
        tot = 0
        for p, e in exps.items():
            if e == 0:
                continue
            k = cubic_exp(h, p)
            if k is None:
                if const_one and e % 3 == 0:
                    continue
                return None
            tot += e * k
        return tot % 3

    mism_ok, mism_ctrl, trials = 0, 0, 0
    for _ in range(4000):
        prs = random.sample(small, 3)
        tot = {p: random.randint(0, 4) for p in prs}
        # two different splits of the same full product n into (l1, l2)
        s1 = {p: random.randint(0, tot[p]) for p in prs}
        s2 = {p: random.randint(0, tot[p]) for p in prs}
        h = (random.randint(-60, 60), random.randint(-60, 60))
        if random.random() < 0.5:                       # force h divisible by a prime of n
            h = E.mul(h, prs[0])
        if h == (0, 0):
            continue
        trials += 1

        def split_value(s, const_one):
            v1 = col_factor(s, h, const_one)
            v2 = col_factor({p: tot[p] - s[p] for p in prs}, h, const_one)
            return None if (v1 is None or v2 is None) else (v1 + v2) % 3

        if split_value(s1, False) != split_value(s2, False) or split_value(s1, False) != col_factor(tot, h):
            mism_ok += 1
        if split_value(s1, True) != split_value(s2, True):
            mism_ctrl += 1
    check("X2 column factor chi_{l1}(h) chi_{l2}(h) = chi_{l1 l2}(h) for every split (zero extension)",
          mism_ok == 0, "%d random (split, split', row) triples, mismatches %d" % (trials, mism_ok))
    check("X2-CTRL 'constant one at exponent = 0 mod 3' makes the factor split-dependent",
          mism_ctrl > 0, "mismatches %d / %d" % (mism_ctrl, trials))


# ----------------------------------------------------------------------------------------------
# Part F: float mini-pipeline
# ----------------------------------------------------------------------------------------------
def primary_odd(Nmax):
    As, Bs = [], []
    bmax = int(math.isqrt(4 * Nmax // 3)) + 3
    for b in range(-(bmax - bmax % 3), bmax + 1, 3):
        rad = Nmax - 3 * b * b / 4.0
        if rad < 0:
            continue
        r = math.sqrt(rad)
        lo, hi = math.ceil(b / 2 - r) - 1, math.floor(b / 2 + r) + 1
        a = np.arange(lo + ((1 - lo) % 3), hi + 1, 3, dtype=np.int64)
        As.append(a)
        Bs.append(np.full(a.shape, b, dtype=np.int64))
    a = np.concatenate(As); b = np.concatenate(Bs)
    N = a * a - a * b + b * b
    keep = (N <= Nmax) & (N % 2 == 1)
    a, b, N = a[keep], b[keep], N[keep]
    o = np.argsort(N, kind="stable")
    return a[o], b[o], N[o]


def divisible(a, b, p):
    c, d = E.conj(p)
    n = E.norm(p)
    return ((a * c - b * d) % n == 0) & ((a * d + b * c - b * d) % n == 0)


H = math.log(4.0)


def bump(u):
    x = u / H
    out = np.zeros_like(u)
    m = np.abs(x) < 1
    out[m] = np.exp(1.0 - 1.0 / (1.0 - x[m] ** 2))
    return out


def W1(y):
    return bump(np.log(y))


def W2(y):
    u = np.log(y)
    return bump(u) * np.exp(0.7j * u) * (1 + 0.3 * u)


class Lattice:
    def __init__(self, Nmax, mask_primes):
        self.a, self.b, self.N = primary_odd(Nmax)
        self.logN = np.log(self.N.astype(float))
        am, bm = self.a % 2, self.b % 2
        e2 = np.where((am == 1) & (bm == 0), 0, np.where((am == 0) & (bm == 1), 1, 2))
        ew = ((self.N - 1) // 3) % 3
        w = np.exp(2j * np.pi / 3)
        self.theta = {"1": np.ones(len(self.N), dtype=complex),
                      "t2": w ** e2, "t2w": w ** ((e2 + ew) % 3)}
        self.divp = {}
        for p in mask_primes:
            self.divp[p] = divisible(self.a, self.b, p)
        self.Nmax = Nmax

    def L(self, U, W, theta="1", mask=(), t=0.0, extra=None):
        """sum_l theta(l) 1_{(l, mask)=1} q_l^{it} W(q_l/U) * extra(log q_l) over ideals prime to 6."""
        lo = np.searchsorted(self.N, U / 4.0, side="left")
        hi = np.searchsorted(self.N, U * 4.0, side="right")
        assert U * 4.0 <= self.Nmax, (U, self.Nmax)
        sl = slice(lo, hi)
        y = self.N[sl] / U
        coef = self.theta[theta][sl] * W(y)
        if mask:
            keep = np.ones(hi - lo, dtype=bool)
            for p in mask:
                keep &= ~self.divp[p][sl]
            coef = coef * keep
        if t != 0.0:
            coef = coef * np.exp(1j * t * self.logN[sl])
        if extra is not None:
            coef = coef * extra(self.logN[sl])
        return coef.sum()


def omega_count(mask):
    return len(mask)


def part_F():
    # primes: two of norm 7, one of norm 13, two of norm 19, inert 5 (norm 25)
    ps = E.primes_upto(40)
    p7, p7b = [p for p in ps if E.norm(p) == 7]
    p13 = [p for p in ps if E.norm(p) == 13][0]
    p19, p19b = [p for p in ps if E.norm(p) == 19]
    p5 = [p for p in ps if E.norm(p) == 25][0]
    Nmax = 10_000_000
    lat = Lattice(Nmax, [p7, p7b, p13, p19, p19b, p5])
    print("lattice: %d primary odd elements of norm <= %d" % (len(lat.N), Nmax), flush=True)

    # Fourier (whole-product) kernel: K(y) = sum_k w_k y^{i tau_k}, a smooth function of log y
    taus = np.array([2 * np.pi * k / (2 * math.log(16.0)) for k in range(-4, 5)])
    wts = np.exp(-0.5 * (np.arange(-4, 5) / 2.0) ** 2)
    wts = wts / wts.sum()

    # geometries: (label, A/M, n1/M, n2/M, L/M); M = 1, so T = Z^A
    mu = Fr(11, 612)
    Lbot = float(Fr(6, 5) * (Fr(31, 36) - Fr(2, 3) + mu))
    geoms = [("cubic C2 top, A=M, L=43/102", 1.0, 0.5, 0.5, 43 / 102),
             ("cubic C2 bottom, A=31/36, L=%.4f" % Lbot, 31 / 36, 0.5, 31 / 36 - 0.5, Lbot),
             ("sextic, A=M, L=1/4", 1.0, 0.5, 0.5, 0.25)]

    # PRE-REGISTERED criteria (fixed before the first run):
    #  common pipeline : rel <= C 2^omega / minscale with C = 40 (the attack's K); if that bound
    #                    is >= 0.5 the check cannot fail meaningfully and is reported UNINF.
    #  control         : rel >= max(10 * (max common rel in this geometry), 0.02).
    C = 40.0
    summary = []
    for (gname, A, n1, n2, Lg) in geoms:
        top = max(n1, n2, A - Lg)                  # longest plain; its window must fit in Nmax
        Z = (Nmax / 4.2) ** (1.0 / top)
        X1, X2 = Z ** n1, Z ** n2
        Y1 = Z ** Lg
        Y2 = X1 * X2 / Y1
        T = X1 * X2
        print("\n== %s: Z = %.3g, T = %.3g, X = (%.3g, %.3g), Y = (%.3g, %.3g)" %
              (gname, Z, T, X1, X2, Y1, Y2), flush=True)

        base_mask = (p13, p19)                     # fixed common mask (e.g. a cube-row radical)
        q7 = 7.0                                   # norm of p7 (extraction) and of p7b (t-prime)

        def rect(s1, s2, theta="1", mask1=base_mask, mask2=base_mask, t1=0.0, t2=0.0,
                 ker=None, kerT=None, kerS=None):
            """one rectangle term after the pipeline; plain scales s1, s2 (already divided)."""
            if ker is None:
                return lat.L(s1, W1, theta, mask1, t1) * lat.L(s2, W2, theta, mask2, t2)
            tot = 0j
            for tau, w in zip(taus, wts):
                if ker == "whole":        # K(q_l1 q_l2 / kerT): the same power on both plains
                    tot += w * lat.L(s1, W1, theta, mask1, t1 + tau) \
                        * lat.L(s2, W2, theta, mask2, t2 + tau) * cmath.exp(-1j * tau * math.log(kerT))
                elif ker == "plain1":     # K(q_l1 / kerS): a kernel on ONE plain variable (control)
                    tot += w * lat.L(s1, W1, theta, mask1, t1 + tau) \
                        * lat.L(s2, W2, theta, mask2, t2) * cmath.exp(-1j * tau * math.log(kerS))
            return tot

        mE = base_mask + (p7,)                     # extraction punctures every residual factor
        U1, U2 = X1 / q7 / q7, X2                  # common pipeline: extract p7, then t-prime p7b
        V1, V2 = Y1 / q7 / q7, Y2
        Tp = U1 * U2
        t0 = 2.5
        P = []   # (name, S_X, S_Y, kind, minscale, omega)
        P.append(("P0 baseline D_b (b = 1), common mask, t = 0",
                  rect(X1, X2), rect(Y1, Y2), "common", min(X1, X2, Y1, Y2), 2))
        P.append(("P1 extraction b_1 = p7 in both rectangles, residual punctured",
                  rect(X1 / q7, X2, mask1=mE, mask2=mE), rect(Y1 / q7, Y2, mask1=mE, mask2=mE),
                  "common", min(X1 / q7, Y1 / q7, X2, Y2), 3))
        P.append(("P1-OBS cross allocation b_X = (p7,1), b_Y = (1,p7): equal products",
                  rect(X1 / q7, X2, mask1=mE, mask2=mE), rect(Y1, Y2 / q7, mask1=mE, mask2=mE),
                  "common", min(X1 / q7, Y1, Y2 / q7), 3))
        P.append(("P1-CTRL extraction in rectangle X only",
                  rect(X1 / q7, X2, mask1=mE, mask2=mE), rect(Y1, Y2, mask1=mE, mask2=mE),
                  "control", None, None))
        P.append(("P2 whole-product kernel K(q_l1 q_l2 / T)",
                  rect(X1, X2, ker="whole", kerT=T), rect(Y1, Y2, ker="whole", kerT=T),
                  "common", min(X1, X2, Y1, Y2), 2))
        P.append(("P2-CTRL kernel on plain 1 only, K(q_l1 / sqrt T)",
                  rect(X1, X2, ker="plain1", kerS=math.sqrt(T)),
                  rect(Y1, Y2, ker="plain1", kerS=math.sqrt(T)), "control", None, None))
        P.append(("P3 one norm power on the whole product, t = 2.5",
                  rect(X1, X2, t1=t0, t2=t0), rect(Y1, Y2, t1=t0, t2=t0),
                  "common", min(X1, X2, Y1, Y2), 2))
        P.append(("P3-CTRL norm power on plain 1 only",
                  rect(X1, X2, t1=t0), rect(Y1, Y2, t1=t0), "control", None, None))
        P.append(("P4 t-allocation n_1 = p7b l_1, l_1 unrestricted, both rectangles",
                  rect(X1 / q7, X2), rect(Y1 / q7, Y2), "common", min(X1 / q7, Y1 / q7, X2, Y2), 2))
        P.append(("P4-CTRL one-variable puncture at p7b in rectangle Y only",
                  rect(X1 / q7, X2), rect(Y1 / q7, Y2, mask1=base_mask + (p7b,)), "control", None, None))
        P.append(("P5-CTRL clip-type fixed-ratio change of one scale in rectangle Y only (x e^0.5)",
                  rect(X1, X2), rect(Y1 * math.exp(0.5), Y2), "control", None, None))
        fX = rect(U1, U2, mask1=mE, mask2=mE, t1=t0, t2=t0, ker="whole", kerT=Tp)
        fY = rect(V1, V2, mask1=mE, mask2=mE, t1=t0, t2=t0, ker="whole", kerT=Tp)
        P.append(("P6 full common pipeline (P1 + P4 + P2 + P3)", fX, fY, "common",
                  min(U1, U2, V1, V2), 3))
        P.append(("P6-CTRL full pipeline, extraction in X only", fX,
                  rect(V1 * q7, V2, mask1=mE, mask2=mE, t1=t0, t2=t0, ker="whole", kerT=Tp),
                  "control", None, None))
        P.append(("P6-CTRL full pipeline, kernel on plain 1 in Y only", fX,
                  rect(V1, V2, mask1=mE, mask2=mE, t1=t0, t2=t0, ker="plain1", kerS=math.sqrt(Tp)),
                  "control", None, None))
        P.append(("P6-CTRL full pipeline, mask differs by the inert prime 5 in Y only", fX,
                  rect(V1, V2, mask1=mE + (p5,), mask2=mE + (p5,), t1=t0, t2=t0, ker="whole", kerT=Tp),
                  "control", None, None))

        crel = []
        for (name, SX, SY, kind, ms, om) in P:
            if kind != "common":
                continue
            rel = abs(SX - SY) / abs(SX)
            bound = C * 2 ** om / ms
            robs = -math.log(rel) / math.log(Z)
            detail = ("rel=%.2e bound=%.2e minscale=%.0f r_obs=%.3f r_minscale=%.3f |S_X|/T=%.3e"
                      % (rel, bound, ms, robs, math.log(ms) / math.log(Z),
                         abs(SX) / T))
            if bound >= 0.5:
                RESULTS.append(("UNINF " + name, None))
                print("UNINF %s [%s]   %s" % (name, gname, detail), flush=True)
            else:
                check("%s [%s]" % (name, gname), rel <= bound, detail)
                crel.append(rel)
            summary.append((gname, name, rel, robs))
        ref = max(crel) if crel else 1.0
        for (name, SX, SY, kind, ms, om) in P:
            if kind != "control":
                continue
            rel = abs(SX - SY) / abs(SX)
            if not crel:
                RESULTS.append(("UNINF " + name, None))
                print("UNINF %s [%s]   rel=%.2e (no informative common check here)" % (name, gname, rel))
            else:
                check("%s [%s]" % (name, gname), rel >= max(10 * ref, 0.02),
                      "rel=%.2e  10 x max common rel=%.2e" % (rel, 10 * ref))
            summary.append((gname, name, rel, None))

        # nonprincipal theta in Theta_3: no main term in either rectangle
        for th in ("t2", "t2w"):
            SX = rect(U1, U2, theta=th, mask1=mE, mask2=mE, t1=t0, t2=t0, ker="whole", kerT=Tp)
            SY = rect(V1, V2, theta=th, mask1=mE, mask2=mE, t1=t0, t2=t0, ker="whole", kerT=Tp)
            ms = min(U1, U2, V1, V2)
            bound = C * 8 / ms
            det = "|S_X|/T'=%.2e |S_Y|/T'=%.2e bound=%.2e" % (abs(SX) / Tp, abs(SY) / Tp, bound)
            name = "P7 nonprincipal theta=%s: neither rectangle has a main term" % th
            if bound >= 0.5:
                RESULTS.append(("UNINF " + name, None))
                print("UNINF %s [%s]   %s" % (name, gname, det))
            else:
                check("%s [%s]" % (name, gname), abs(SX) / Tp <= bound and abs(SY) / Tp <= bound, det)
    return summary


def main():
    part_X()
    part_F()
    n_pass = sum(1 for _, ok in RESULTS if ok is True)
    n_fail = sum(1 for _, ok in RESULTS if ok is False)
    n_un = sum(1 for _, ok in RESULTS if ok is None)
    print("\n%d/%d PASS, %d FAIL, %d UNINF (uninformative at this scale, not counted as pass)"
          % (n_pass, n_pass + n_fail, n_fail, n_un))


if __name__ == "__main__":
    main()
```

</details>

## Appendix C: output of both_rectangles.py (run 1, `run1.log`)

<details>
<summary>run1.log (66 lines)</summary>

```
PASS X1 cubic symbol = (sextic symbol)^2, computed independently by powmod   3027 (u, p) pairs, 77 primes of norm <= 400
PASS X1 cube of the cubic symbol is principal on units (no quadratic twist at n = 3)
PASS X1-CTRL cube of the sextic symbol is the quadratic symbol (takes both values +-1)   values seen: [-1, 1]
PASS X2 column factor chi_{l1}(h) chi_{l2}(h) = chi_{l1 l2}(h) for every split (zero extension)   3999 random (split, split', row) triples, mismatches 0
PASS X2-CTRL 'constant one at exponent = 0 mod 3' makes the factor split-dependent   mismatches 233 / 3999
lattice: 3022972 primary odd elements of norm <= 10000000

== cubic C2 top, A=M, L=43/102: Z = 1.06e+11, T = 1.06e+11, X = (3.25e+05, 3.25e+05), Y = (4.44e+04, 2.38e+06)
PASS P0 baseline D_b (b = 1), common mask, t = 0 [cubic C2 top, A=M, L=43/102]   rel=1.30e-06 bound=3.60e-03 minscale=44408 r_obs=0.534 r_minscale=0.422 |S_X|/T=2.697e-01
PASS P1 extraction b_1 = p7 in both rectangles, residual punctured [cubic C2 top, A=M, L=43/102]   rel=1.07e-04 bound=5.04e-02 minscale=6344 r_obs=0.360 r_minscale=0.345 |S_X|/T=2.831e-02
PASS P1-OBS cross allocation b_X = (p7,1), b_Y = (1,p7): equal products [cubic C2 top, A=M, L=43/102]   rel=5.23e-06 bound=7.21e-03 minscale=44408 r_obs=0.479 r_minscale=0.422 |S_X|/T=2.831e-02
PASS P2 whole-product kernel K(q_l1 q_l2 / T) [cubic C2 top, A=M, L=43/102]   rel=5.09e-06 bound=3.60e-03 minscale=44408 r_obs=0.480 r_minscale=0.422 |S_X|/T=9.964e-02
PASS P3 one norm power on the whole product, t = 2.5 [cubic C2 top, A=M, L=43/102]   rel=1.14e-05 bound=3.60e-03 minscale=44408 r_obs=0.448 r_minscale=0.422 |S_X|/T=3.550e-02
PASS P4 t-allocation n_1 = p7b l_1, l_1 unrestricted, both rectangles [cubic C2 top, A=M, L=43/102]   rel=4.17e-05 bound=2.52e-02 minscale=6344 r_obs=0.397 r_minscale=0.345 |S_X|/T=3.853e-02
PASS P6 full common pipeline (P1 + P4 + P2 + P3) [cubic C2 top, A=M, L=43/102]   rel=2.75e-03 bound=3.53e-01 minscale=906 r_obs=0.232 r_minscale=0.268 |S_X|/T=8.162e-04
PASS P1-CTRL extraction in rectangle X only [cubic C2 top, A=M, L=43/102]   rel=6.00e+00  10 x max common rel=2.75e-02
PASS P2-CTRL kernel on plain 1 only, K(q_l1 / sqrt T) [cubic C2 top, A=M, L=43/102]   rel=9.73e-01  10 x max common rel=2.75e-02
PASS P3-CTRL norm power on plain 1 only [cubic C2 top, A=M, L=43/102]   rel=1.22e+00  10 x max common rel=2.75e-02
PASS P4-CTRL one-variable puncture at p7b in rectangle Y only [cubic C2 top, A=M, L=43/102]   rel=1.43e-01  10 x max common rel=2.75e-02
PASS P5-CTRL clip-type fixed-ratio change of one scale in rectangle Y only (x e^0.5) [cubic C2 top, A=M, L=43/102]   rel=6.49e-01  10 x max common rel=2.75e-02
PASS P6-CTRL full pipeline, extraction in X only [cubic C2 top, A=M, L=43/102]   rel=8.48e-01  10 x max common rel=2.75e-02
PASS P6-CTRL full pipeline, kernel on plain 1 in Y only [cubic C2 top, A=M, L=43/102]   rel=9.81e-01  10 x max common rel=2.75e-02
PASS P6-CTRL full pipeline, mask differs by the inert prime 5 in Y only [cubic C2 top, A=M, L=43/102]   rel=8.29e-02  10 x max common rel=2.75e-02
PASS P7 nonprincipal theta=t2: neither rectangle has a main term [cubic C2 top, A=M, L=43/102]   |S_X|/T'=8.68e-09 |S_Y|/T'=4.64e-10 bound=3.53e-01
PASS P7 nonprincipal theta=t2w: neither rectangle has a main term [cubic C2 top, A=M, L=43/102]   |S_X|/T'=2.76e-08 |S_Y|/T'=4.85e-09 bound=3.53e-01

== cubic C2 bottom, A=31/36, L=0.2549: Z = 3.3e+10, T = 1.14e+09, X = (1.82e+05, 6.29e+03), Y = (480, 2.38e+06)
PASS P0 baseline D_b (b = 1), common mask, t = 0 [cubic C2 bottom, A=31/36, L=0.2549]   rel=8.25e-04 bound=3.33e-01 minscale=480 r_obs=0.293 r_minscale=0.255 |S_X|/T=2.697e-01
UNINF P1 extraction b_1 = p7 in both rectangles, residual punctured [cubic C2 bottom, A=31/36, L=0.2549]   rel=4.90e-02 bound=4.67e+00 minscale=69 r_obs=0.125 r_minscale=0.175 |S_X|/T=2.831e-02
UNINF P1-OBS cross allocation b_X = (p7,1), b_Y = (1,p7): equal products [cubic C2 bottom, A=31/36, L=0.2549]   rel=4.27e-03 bound=6.67e-01 minscale=480 r_obs=0.225 r_minscale=0.255 |S_X|/T=2.831e-02
PASS P2 whole-product kernel K(q_l1 q_l2 / T) [cubic C2 bottom, A=31/36, L=0.2549]   rel=3.16e-03 bound=3.33e-01 minscale=480 r_obs=0.238 r_minscale=0.255 |S_X|/T=9.963e-02
PASS P3 one norm power on the whole product, t = 2.5 [cubic C2 bottom, A=31/36, L=0.2549]   rel=1.54e-02 bound=3.33e-01 minscale=480 r_obs=0.172 r_minscale=0.255 |S_X|/T=3.551e-02
UNINF P4 t-allocation n_1 = p7b l_1, l_1 unrestricted, both rectangles [cubic C2 bottom, A=31/36, L=0.2549]   rel=1.93e-02 bound=2.33e+00 minscale=69 r_obs=0.163 r_minscale=0.175 |S_X|/T=3.853e-02
UNINF P6 full common pipeline (P1 + P4 + P2 + P3) [cubic C2 bottom, A=31/36, L=0.2549]   rel=2.40e-01 bound=3.27e+01 minscale=10 r_obs=0.059 r_minscale=0.094 |S_X|/T=8.162e-04
PASS P1-CTRL extraction in rectangle X only [cubic C2 bottom, A=31/36, L=0.2549]   rel=5.97e+00  10 x max common rel=1.54e-01
PASS P2-CTRL kernel on plain 1 only, K(q_l1 / sqrt T) [cubic C2 bottom, A=31/36, L=0.2549]   rel=3.78e+00  10 x max common rel=1.54e-01
PASS P3-CTRL norm power on plain 1 only [cubic C2 bottom, A=31/36, L=0.2549]   rel=1.81e+00  10 x max common rel=1.54e-01
FAIL P4-CTRL one-variable puncture at p7b in rectangle Y only [cubic C2 bottom, A=31/36, L=0.2549]   rel=1.01e-01  10 x max common rel=1.54e-01
PASS P5-CTRL clip-type fixed-ratio change of one scale in rectangle Y only (x e^0.5) [cubic C2 bottom, A=31/36, L=0.2549]   rel=6.47e-01  10 x max common rel=1.54e-01
PASS P6-CTRL full pipeline, extraction in X only [cubic C2 bottom, A=31/36, L=0.2549]   rel=8.31e-01  10 x max common rel=1.54e-01
PASS P6-CTRL full pipeline, kernel on plain 1 in Y only [cubic C2 bottom, A=31/36, L=0.2549]   rel=1.49e+00  10 x max common rel=1.54e-01
PASS P6-CTRL full pipeline, mask differs by the inert prime 5 in Y only [cubic C2 bottom, A=31/36, L=0.2549]   rel=3.01e-01  10 x max common rel=1.54e-01
UNINF P7 nonprincipal theta=t2: neither rectangle has a main term [cubic C2 bottom, A=31/36, L=0.2549]   |S_X|/T'=6.97e-07 |S_Y|/T'=1.42e-08 bound=3.27e+01
UNINF P7 nonprincipal theta=t2w: neither rectangle has a main term [cubic C2 bottom, A=31/36, L=0.2549]   |S_X|/T'=8.42e-07 |S_Y|/T'=3.63e-08 bound=3.27e+01

== sextic, A=M, L=1/4: Z = 3.18e+08, T = 3.18e+08, X = (1.78e+04, 1.78e+04), Y = (134, 2.38e+06)
UNINF P0 baseline D_b (b = 1), common mask, t = 0 [sextic, A=M, L=1/4]   rel=3.43e-04 bound=1.20e+00 minscale=134 r_obs=0.407 r_minscale=0.250 |S_X|/T=2.697e-01
UNINF P1 extraction b_1 = p7 in both rectangles, residual punctured [sextic, A=M, L=1/4]   rel=1.61e-02 bound=1.68e+01 minscale=19 r_obs=0.211 r_minscale=0.151 |S_X|/T=2.831e-02
UNINF P1-OBS cross allocation b_X = (p7,1), b_Y = (1,p7): equal products [sextic, A=M, L=1/4]   rel=6.41e-03 bound=2.40e+00 minscale=134 r_obs=0.258 r_minscale=0.250 |S_X|/T=2.831e-02
UNINF P2 whole-product kernel K(q_l1 q_l2 / T) [sextic, A=M, L=1/4]   rel=9.89e-03 bound=1.20e+00 minscale=134 r_obs=0.236 r_minscale=0.250 |S_X|/T=9.964e-02
UNINF P3 one norm power on the whole product, t = 2.5 [sextic, A=M, L=1/4]   rel=4.47e-02 bound=1.20e+00 minscale=134 r_obs=0.159 r_minscale=0.250 |S_X|/T=3.550e-02
UNINF P4 t-allocation n_1 = p7b l_1, l_1 unrestricted, both rectangles [sextic, A=M, L=1/4]   rel=3.64e-02 bound=8.39e+00 minscale=19 r_obs=0.169 r_minscale=0.151 |S_X|/T=3.854e-02
UNINF P6 full common pipeline (P1 + P4 + P2 + P3) [sextic, A=M, L=1/4]   rel=5.74e-01 bound=1.17e+02 minscale=3 r_obs=0.028 r_minscale=0.051 |S_X|/T=8.114e-04
UNINF P1-CTRL extraction in rectangle X only [sextic, A=M, L=1/4]   rel=6.04e+00 (no informative common check here)
UNINF P2-CTRL kernel on plain 1 only, K(q_l1 / sqrt T) [sextic, A=M, L=1/4]   rel=5.44e-01 (no informative common check here)
UNINF P3-CTRL norm power on plain 1 only [sextic, A=M, L=1/4]   rel=3.72e-01 (no informative common check here)
UNINF P4-CTRL one-variable puncture at p7b in rectangle Y only [sextic, A=M, L=1/4]   rel=1.57e-01 (no informative common check here)
UNINF P5-CTRL clip-type fixed-ratio change of one scale in rectangle Y only (x e^0.5) [sextic, A=M, L=1/4]   rel=6.48e-01 (no informative common check here)
UNINF P6-CTRL full pipeline, extraction in X only [sextic, A=M, L=1/4]   rel=8.24e-01 (no informative common check here)
UNINF P6-CTRL full pipeline, kernel on plain 1 in Y only [sextic, A=M, L=1/4]   rel=1.40e+00 (no informative common check here)
UNINF P6-CTRL full pipeline, mask differs by the inert prime 5 in Y only [sextic, A=M, L=1/4]   rel=5.86e-01 (no informative common check here)
UNINF P7 nonprincipal theta=t2: neither rectangle has a main term [sextic, A=M, L=1/4]   |S_X|/T'=1.19e-06 |S_Y|/T'=1.69e-08 bound=1.17e+02
UNINF P7 nonprincipal theta=t2w: neither rectangle has a main term [sextic, A=M, L=1/4]   |S_X|/T'=1.29e-05 |S_Y|/T'=1.06e-07 bound=1.17e+02

32/33 PASS, 1 FAIL, 23 UNINF (uninformative at this scale, not counted as pass)
exit=0 wall=83s
```

</details>
