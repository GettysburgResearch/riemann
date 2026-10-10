# Red-team review: the nested comparison ordering for the cubic transfer of Lemma 18.1

```text
Status: REVIEW (adversarial, bounded) of an EXPLORATION note. Exponent-ledger level only.
  Verdict (a): no break found. The nested ordering is a well-founded reordering, and no hidden
  main term or obstruction makes X^{1+eps} false. Four corrections to the note are listed in
  Sec. 5. Everything stays CONDITIONAL on the external, unreviewed Lemma 18.1 scheme and on its
  n = 3 analogues. No moment bound is proved. RH is not addressed.
Scope: CUBIC_RELAXED_INDUCTION.md Sec. 4 (nested comparisons), with its script; the cubic
  substitutions of CUBIC_FOURTH_MOMENT_TRANSFER.md and its ledger; the quadratic calibration;
  obstructions from Gauss-sum bias (de Faveri-Dunn-Hoffstein, Patterson). Case 1 (z = 0) only.
Exact sources or dependencies:
  repo HEAD 7ac3cf7b38b74b5066ff445033b7b741dc3986db (branch claude/peaceful-faraday-ki4ewu).
  pr908:standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
    The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex, sha256 42a5ee0f...deac6a3
    (re-hashed). Read as untrusted data: l. 12477-12605, 12780-12830, 12903-13010,
    14312-14810, 14860-14940.
  Under review (sha256): CUBIC_RELAXED_INDUCTION.md 5ec47bca...b984;
    scripts/cubic_relaxed_induction.py 8dff31d4...a77d; CUBIC_FOURTH_MOMENT_TRANSFER.md
    f86b7e26...fc6d; scripts/cubic_fourth_moment_ledger.py 5c79445b...80d5. Context:
    reviews/LEMMA18_1_REVIEW.md 840aa73c...758d, reviews/LEMMA18_1_COMMON_SUPPORT.md
    0f2b54fc...a805.
  Primary literature: arXiv API metadata and e-print sources, fetched fresh and read with
    grep/sed only:
    * 2607.07911v2 (de Faveri-Dunn-Hoffstein), e-print sha256 5f60d984...b3fcc;
    * 2610.04045v1 (de Faveri), e-print sha256 7c80fd66...dbb9;
    * 2410.03048v2 (David-de Faveri-Dunn-Stucky), e-print sha256 ba8542c8...c8e1.
    Two arXiv searches: abs:cubic AND "fourth moment"; abs:cubic AND moment AND secondary.
What was actually run:
  python3 -I scripts/cubic_relaxed_induction.py -> 39/39 PASS (about 10 s; re-run, unchanged).
  An independent check script, written from the note's stated constraints and not from its
  code (Appendix; kept in the session scratchpad and not committed):
    nested_redteam_check.py (sha256 a750f17c...5456) -> 7/7 PASS, about 8 s.
  t1c.py (sha256 3d0c4efb...f325): finer uniform-margin search, about 39 s.
  Both are exact Fraction arithmetic on grids. By convexity, a grid check is exact on each
  stage interval (Sec. 1.4).
Smallest remaining gap: for n = 3, the centred stage of Lemma 18.1 must give the lattice saving
  r = (L - v)_+ with comparison length L up to about 0.42M, and F_1 + F_2 >= (5/6)v uniformly
  over every common-support allocation, with total loss below M/12. It must also accept a
  reflected comparison datum at the same width. This sits on top of every unverified step of
  the sextic Lemma 18.1 itself. That lemma would already beat the conjecturally optimal sextic
  large sieve (X^{7/6} at the balanced point).
```

RH is unsolved. This note does not prove or disprove anything about RH, about Lemma 18.1, or
about cubic moments. "Closes" means that affine exponent ledgers balance, nothing more.

## 0. Verdict and findings

**(a) The proposal survives scrutiny at ledger level.** I could not break the nested ordering,
and I found no hidden main term. In detail:

1. **The nested order is well-founded** (Sec. 1). Take the lexicographic order on
   (width band, stage index). Every call strictly lowers it. At `η = 0` the number of
   same-width stages is `k = 2`, independent of `Z`. Losses add per width level and do not
   compound. The quantifier order of l. 14866-14940 accommodates this once `C_*` is enlarged
   by the fixed factor `k + 1`.
2. **The ledger models the displayed steps of the TeX** (Sec. 2). I found no cubic step with an
   unmodelled loss. The Patterson-type Gauss-sum bias is not ignored. It is exactly the
   `Θ`-row excess `A - (1-θ)M` that drives the whole construction (Sec. 4.2).
3. **The quadratic calibration reproduces only the exponent `K^{1+ε}`** (Sec. 3). It does so at a
   degenerate critical point: at `η = 0` the centred stage makes zero progress. The quadratic
   family is perfectly orthogonal and has no Gauss-sum phases, so it cannot test the cubic
   obstruction.
4. **`X^{1+ε}` is not false.** It follows trivially from GLH. Root numbers drop out of every
   `|·|²` the scheme uses. The cubic large-sieve obstruction is real, but the scheme does
   not use a general-coefficient large sieve (Sec. 4).
5. **Four corrections to the note** (Sec. 5):
   * the uniform-in-`A` margin is smaller than quoted;
   * the `κ = 2/3` case is mis-classified relative to the quadratic calibration;
   * the "limit" cases need an unstated relation `δ < 3η/2`;
   * the premise "no Patterson bias in the sextic case" is false. The bias exists for every
     `n ≥ 3`, with excess `X^{1/n}` at the balanced point.

## 1. Legitimacy of the nested order

### 1.1 What the paper actually orders

* l. 12903-12921: bands of length `σ/4` in increasing width. Zero-slot bands come first.
  Within a band the paper proves "the uncentered assertion for `A ≤ 5M/6`, and then the
  padded core", and then reflection.
* l. 12983-12985: "every retained reflected comparison calls the previously proved
  uncentered assertion at this same width".
* l. 14534-14536: the uncentred stage is completed, after which "the comparisons constructed
  earlier may consequently use that stage".
* l. 14799-14804: "A centered comparison calls only the earlier uncentered stage in its band
  … Thus there is no same-band cycle."
* l. 14925-14938: the error envelope is `E_d = T_term + (d+1) C_*(η+ξ+ε_0)` with `d` the
  number of remaining strict calls. "A strict edge and its fixed number of same-band
  operations" costs one `C_*(…)`.

The restriction to the uncentred stage is a design choice of the sextic proof, where one stage
suffices. Nothing in the text uses it as a hypothesis elsewhere.

### 1.2 Explicit well-founded order

Nodes are `(β, j)`, where `β` is the band index and `j` is the stage:

* `j = 0`: `U`, totals `A ≤ s_0 M`;
* `j = 1…k`: `C_j`, totals `A ∈ (b_{j-1}, b_j]`;
* `j = k+1`: the reflection closure.

| call | source | target | strict decrease |
|---|---|---|---|
| child (second transform) | any `(β, j)` | `(β', ·)` with width `≤ M - σ/2`, so `β' ≤ β - 2` (l. 14782-14790) | first coordinate |
| comparison (proposed) | `(β, j)`, `1 ≤ j ≤ k` | `(β, j')`, `j' < j`, at the **same** width `M` | second coordinate |
| reflection closure | `(β, k+1)` | `(β, ≤ k)` | second coordinate |

The lexicographic order on `N × {0,…,k+1}` is well-founded. A chain has length at most
`(#strict levels)·(k+2)`. Check [T6] builds the call graph for 8, 16 and 32 bands and
`k = 1, 2, 3`. It confirms that the graph is acyclic and meets this bound (for example, length 64
for 32 bands and `k = 2`).

### 1.3 The three sub-questions

* **Is `C_{j-1}` at width `M` already proved when `C_j` calls it?** Yes.
  * Stages are proved for all widths of the band in the order `U, C_1, …, C_k`.
  * A comparison is at the identical width `M`.
  * The parameters do not interfere with this:
    * `L = L(A, j)` is a fixed piecewise-affine choice made with `ρ, σ, δ`;
    * `ξ` is chosen afterwards, at l. 14866-14889;
    * the paper's slot mesh `η` is irrelevant for `z = 0`.
  * `C_{j-1}` covers `R_0` rows only, and that is all the comparison needs. The paper bounds
    the comparison "on the original permissible rows" (l. 13005).
* **Does the centred proof depend on the comparison bound?** No. It depends only on the choice
  of `L`.
  * `Δ_k` (l. 12987-13008) depends on the rectangle `(Z^L, X_1X_2/Z^L)`, not on any bound for
    it.
  * The comparison bound enters only through `Σ_{R_0}|S|² ≤ 2Σ_{ball}|Δ|² + 2Σ_{R_0}|comp|²`.
  * Every call inside the `Δ` analysis goes to a child at a smaller band:
    * zero frequency, diagonal and `Θ` rows are terminal;
    * nonexceptional children are split by the triangle inequality into two plain-product
      data at width `M' ≤ M - σ/2`.
  * The only coupling is the trade-off in `L`: larger `L` gives more saving in (C) and a
    larger `A_comp` in (R). That is a constraint, not a cycle.
* **Do constants and losses compound? Is the stage count bounded?** They are bounded.
  * At `η = 0`, `κ = 5/6`, the stage count is `k = 2`, with `s = 2/3 → 19/21 → 158/147`.
  * Along a branch, each width level carries at most `k + 1` same-width calls. The envelope
    becomes `E_d = T_term + (d+1)(k+1)C_*(η+ξ+ε_0)`, so the paper's `ξ < ε/(16C_*D)` must
    become `ξ < ε/(16(k+1)C_*D)`.
  * Multiplicative constants grow like `2^{(k+1)D}`. That is independent of `Z`.
  * The profile types are closed under the iterated reflections. This finite set must be
    fixed through the enlarged depth before `C_ref` (l. 12790-12797). The set is finite
    because `k` is fixed.

**Admissibility of the reflected comparison as input.** The paper itself states the conjugation
device: after reflection, "conjugating that whole factor inside its absolute value replaces the
conjugate character by the original character and conjugates its profile" (l. 12785-12789).

* The reflected comparison is therefore again `|S_ψ(n_1;W_1) S_ψ(n_2;W_2')|` with the same
  `ψ_k`. The annular pieces have summable coefficients `O(2^{-j/2})` (l. 12780-12783).
* `C_{j-1}`'s own centring (l. 14538-14660) needs only the same character on both plains and
  smooth annular profiles. Both hold.
* The caps `L ≤ A/2` and `L ≤ A - M/2` keep the datum in the padded core. A short-side branch
  (`b < L`) gives a total `M - A + 2b ≤ M - A + 2L`, which is again in a proved range.
* This is the same input class the paper already feeds to `U`. **No circularity was found.**

### 1.4 Margins

The note quotes `11M/507 ≈ 0.0217M` as the best two-stage margin "at `A = M`". That is the
equalised margin of a chain starting at `A = M` ([T7] confirms `-2/51`, `11/507`).

A proof needs one fixed stage split and a margin uniform over the whole padded core. On each
stage interval the feasible set `{A : lo(A) ≤ hi(A)}` is convex: `lo` is a maximum of affine
functions and `hi` a minimum of affine functions. So a grid check that includes the interval's
endpoints is exact on that interval. The open endpoint at the previous stage boundary is
covered by that stage.

| range | best uniform margin, two stages | split `b_1` |
|---|---|---|
| `(2/3, 1]` | `≈ 0.0179 M` | `0.861` |
| `(2/3, 1.01]` | `≈ 0.0156 M` [T1] | `0.867` |

The margin is smaller than quoted but still positive. It absorbs `C_*ξ`, `δ` and the terminal
terms once these are chosen below it. The single window fails at `A = M` [T2].

## 2. Does the ledger model the paper?

Each inequality used by `cubic_relaxed_induction.py` corresponds to a displayed step. The
correspondences:

| script item | TeX | cubic substitution | verdict |
|---|---|---|---|
| [R1] first-transform ledger | l. 13384-13392, old-eq:2.5-2.6 | θ-free. `B_c` redesigned to `((3c-4d-2R)/6)_+` | `B_c` enters with a favourable sign in the diagonal, the child allowance `Δ_child` and `F_1`. Only the budget (2.6) constrains it, and old [B8] checks that budget prime by prime |
| [R2] children | old-eq:2.13 | θ-free | matches |
| [R3] exceptional rows | old-eq:2.15-2.16; count at l. 14365-14380 | `(h') = 𝔥_0𝔳³`, count `Z^{(m'-f)/3}` | matches |
| (C) centred | l. 14662-14770, (2.18)-(2.19) | `F_1 + F_2 ≥ κv`, `κ = min(5/6, 1)`; maximum at `v = L` | matches for every `L`. The lattice lemma needs all four scales `≥ Z^r`, which the caps provide |
| (R) comparison | l. 12947-12985, (3.11) | `A_comp = M - A + 2L + ξ` | matches |
| [R4] diagonal | old-eq:2.12 | θ-free; needs `A ≤ M + δ` | matches |
| [E1] Gauss-row zero | l. 13572-13594 | cubes: `2a_0/3 - 2s_0 ≤ a_0 - s_0` | fits, tight at `s_0 = a_0/3` with the crude count |
| threshold `2M/3` | intro l. 12593-12600; (2.15) with `F ≥ 0` | `(1-θ)M` | matches (see also Sec. 4.2) |
| nonunit `i = 1` device | l. 14349-14362 | `v_p(h') + 2 ≡ 0 (mod 3)`, so residue 1 and `θf = v_1/3` | the same saving as the paper uses |

**Cubic steps that could carry a different loss.** I checked each candidate:

* **Gauss-sum sizes.** Prime moduli give `|g| = √Np` for every order. At prime powers the
  `n`-dependence is which exponents are principal: `3 | a` for cubic, versus `6 | a` for
  sextic. That enters only through `r = 1_{3∤i-j}` in the first transform and the `3 | i`
  and `3 | j_0` rows of the `F_2` table. The ledger includes both ([B], [C]).
  * Not verified: the cubic complete-support correlation at prime powers, especially the
    unequal case `i > j_0` with `j_0 = 3`, which has no sextic counterpart below `j_0 = 6`.
  * `eq:gauss-local` is spot-checked in floating point at `Np = 7, 13`.
* **Number of exceptional rows.**
  * Kummer theory with `μ_3 ⊂ Q(ω)` gives a single residue class mod 3 per good prime. The
    units modulo cubes and the `S`-ray data give finitely many classes. So the count is
    `Z^{θ(m'-f)+ε}`.
  * Not re-proved: Lemma fixed-numerator-ray with valuations mod 3.
* **Patterson's cubic bias.** Present and modelled. See Sec. 4.2: it is not specific to
  `n = 3`.
* **Möbius steps.** The paper has four:
  * mask erasure (old-eq:2.1a-b);
  * the `𝔢`-mask;
  * the `s`-label;
  * the `𝔱`-allocation.

  All four are exact identities with `Z^ε` mass for every `n`. I found no Möbius step that
  absorbs an order-dependent term. The application to squarefree `c ≡ 1 (9)` needs only
  positivity (`R_sf ⊂ R_0`) and cubic reciprocity `χ_c(n) = χ_n(c)` for primary `n, c`. No
  Möbius inversion is needed there.
* **Root numbers.** The paper reflects only inside `|·|²` (l. 12785-12789) and never inside
  `Δ_k`. Cubic root numbers, which are normalised Gauss sums, therefore never appear
  non-absolutely.

**Not modelled (by design):** the analytic lemmas smooth-calculus, kernel-seminorms and
logarithmic-control; Sec. 18.8; and the coefficient lemma. Those are inherited unchanged.

## 3. Calibration: only the exponent, at a degenerate point

* **The nested quadratic chain at `η = 0` makes no progress.**
  * At `A > 1/2`, (C) requires `L ≥ A - 1/2` and (R) requires `L ≤ (A - 1/2)/2`. These are
    incompatible.
  * For `η > 0` each centred stage gains exactly `2η`: `s_i = 1/2 + (2i+1)η` [T5]. So about
    `1/(4η)` stages are needed, and the reachable set is capped at `1 + 2η` by `L ≤ A/2`
    [T4]. The padded-core slack must then satisfy `δ < 2η`.
  * This is legitimate: `η` is chosen first and `k(η)` is independent of `Z`. But it means the
    calibration is driven entirely by the relaxation. Any uniform loss `cM` with `c > 0` in
    the quadratic centred stage would break it.
* **The quadratic case is structurally different.**
  * The characters are real, and quadratic Gauss sums are `√N` times a fixed phase. The Poisson
    dual of a quadratic character sum is again such a sum, and root numbers are trivial.
  * The squarefree quadratic large sieve is perfectly orthogonal. David-de Faveri-Dunn-Stucky,
    2410.03048 l. 495-501: the fourth-moment bound "is owed to a perfectly orthogonal large
    sieve bound for primitive quadratic characters due to Heath-Brown". The paper cites a
    quadratic Hecke-family estimate of Goldmakher-Louvel (paper l. 131-133); I did not read it.
  * The cubic family is not perfectly orthogonal, unconditionally (2607.07911, Thm 1.1).
* **Conclusion.** Matching `K^{1+ε}` shows that the affine model is consistent with a known
  exponent. It cannot test whether centring defeats the Gauss-sum bias, which is the cubic
  difficulty. The note's sentence "this supports … the nested reading" (Sec. 4) overstates
  what the check shows.

## 4. Known obstructions

### 4.1 The fourth moment itself

* **Under GLH the target holds.** `S_ψ(n;W) ≪ Z^ε` for nonprincipal rows by Mellin
  inversion, so `Σ_{R_0}|S S|² ≪ Z^{m+ε}`. Hence `Σ_{Nc≤X}|L(1/2,χ_c)|⁴ ≪ X^{1+ε}`. A
  genuine term of size `X^{4/3}` (or any `X^{1+c}`) would contradict GLH. **So (c) "false"
  is excluded unless GLH fails.**
* **Root numbers in the AFE.** `L(1/2,χ)² = A + ε(χ)²B`, with `ε(χ_c)` a normalised cubic
  Gauss sum.
  * The upper bound uses `|L|⁴ ≤ 2|A|² + 2|B|²`, where `A` and `B` are divisor-coefficient sums
    with no Gauss sums.
  * In an asymptotic, the cross terms with `ε` and `ε²` produce Patterson-type lower-order terms.
    The cubic second moment has such a term: `X P_W(log X) + X^{5/6} Q_W(log X)`
    (2610.04045, Thm `cubic_secondary_term`; Diaconu's conjecture). By Cauchy-Schwarz these
    cross terms are at most the diagonal terms.
  * Expected shape: `X·P(log X)` (unitary family; CFKRS-type recipe, not re-derived here) plus
    lower-order terms.
* **Literature.** No unconditional cubic fourth moment below `X^{4/3}` was found, which matches
  the note. 2410.03048 l. 500-501: "the cubic large sieve is *not* perfectly orthogonal, so an
  optimal fourth moment bound is not available in the cubic case". That is a statement about
  the large-sieve route, not about the truth of the bound.

### 4.2 Inside the scheme: the bias is exactly the Θ-row excess

**The obstruction.** de Faveri-Dunn-Hoffstein (2607.07911v2, Thm `cubic_main`, l. 193-198)
prove unconditionally `Ξ_3(A,B) ≫ (AB)^{-ε}(A + B + (AB)^{2/3})`. Their extremal sequence is
`β_b = \overline{g̃_3(b)} H(N b/B)`. Its polar term is
`P_B(a) ≍ \overline{g̃_3(a)} N(a)^{-1/6} B^{5/6}` (l. 276-283, via DDDS Lemma 6.7). They
conjecture (l. 222-226) that for every `n ≥ 3`

    Ξ_n(A,B) = (AB)^{o(1)}(A + B + A^{1-1/n}B^{2/n} + A^{2/n}B^{1-1/n}).

de Faveri's 2610.04045 abstract describes his improved bound as "expected to be optimal in all
ranges". At `A = B = X` the extra term is `X^{1+1/n}`: `X^{4/3}` for cubic and `X^{7/6}` for
sextic. So **the bias is present for the sextic family too**; the task's premise that it is
absent there does not hold.

**Where the scheme meets it.** The first transform produces the Gauss-row norm
`N_C = Σ_{h~Z^K} |Z^{-a_0/2} Σ_a A_C(a) G(a,h)|²`. For squarefree `a` prime to `h`,
`G(a,h) = \bar χ_a(h) g̃(a)`. So `N_C` is an order-`n` large sieve with coefficients
`A_C(a)g̃(a)`: plain-smooth times a Gauss sum. That is exactly the DDH extremal shape.

Insert the conjectured polar term with exponents `1/2 + 1/n` and `N(h)^{-1/(2n)}` (proved for
`n = 3`). With no common support, `a_0 = A` and `K = 2A - m`, `q = 0`. The polar part of `N_C`
then exceeds the target `Z^{a_0}` by

    2a_0/n + K(1 - 1/n) - a_0  =  A - (1 - 1/n) M ,

which is **exactly the scheme's exceptional excess `A - (1-θ)M`** (old-eq:2.15 with
`F_1 = F_2 = 0`). Hence:

* The paper's threshold `5M/6`, and its cubic analogue `2M/3`, is precisely the point where the
  Patterson polar term of the Gauss-row norm fits. The ledger does not ignore the bias; its
  `θ` encodes it.
* For uncentred plain inputs with `A > (1-θ)M` the excess is genuine. That is why centring is
  needed. The DDH lower bound applies to these Gauss-row norms.
* Centring kills the leading polar term because it depends only on `T = X_1X_2`.
  * In the paper this is the lattice main term `c²T^{1+it}I_1I_2` (l. 14560-14600).
  * Heuristically, summing `g̃(h, l_1l_2)` over `l_2` (polar `X_2^{5/6}τ(·)`) and then over
    `l_1` (with `|g̃|² = 1`) gives `(X_1X_2)^{5/6}`, again a function of `T` only.
  * The two pictures agree.
* The cubic transfer must cancel a relative `Z^{-M/3}` at `A = M`, against `Z^{-M/6}` in the
  sextic proof. This needs `κL ≥ M/3`, so `L ≥ 2M/5`. The nested ordering exists to permit
  that.

**Consistency.** `θ = 1` would beat `Ξ_3`, and the sextic Lemma 18.1 already claims to beat
`Ξ_6`. Neither contradicts DDH, which concerns the worst coefficients. The scheme uses the
plain structure of its own coefficients. That is the same unverified claim already flagged in
reviews/LEMMA18_1_REVIEW.md, now with twice the bias to cancel.

## 5. Corrections to CUBIC_RELAXED_INDUCTION.md (none breaks it)

1. **Margin.** "Best uniform margin `11M/507`" holds only for a chain started at `A = M`. With
   one fixed stage split, uniform over `(2/3, 1+δ]`, the margin is about `0.018M`
   (`δ = 0`) or `0.0156M` (`δ = 0.01`) (Sec. 1.4).
2. **Classification of κ = 2/3.**
   * The note counts the quadratic "limit" (`κ = 2θ`) as giving `K^{1+ε}`. But it says that
     without the nonunit `i = 1` device (`κ = 2/3 = 2θ`) the cubic case gives `θ = 1` "only as
     a limit", and it lists that device as needed (Sec. 8, step 5).
   * Consistently, `κ = 2/3` also yields `X^{1+ε}`: `log_2(1/η)` stages, with the extra
     requirement `δ < 3η/2` [T4].
   * Step 5 is needed only for a positive margin (robustness against `O(M)` losses), not
     for the exponent.
3. **Unstated parameter relation.** In both limit cases the reachable range is capped below
   `1 + 3η/2` (cubic, `κ = 2/3`) or `1 + 2η` (quadratic) by the cap `L ≤ A/2`. The padded core
   `A ≤ M + δ` therefore needs `δ` below these. This is compatible with the paper's choices
   only if the relaxation `η` is fixed before `ρ, σ, δ`.
4. **Bookkeeping to add to Sec. 4 (iii).**
   * `ξ < ε/(16(k+1)C_*D)`.
   * The finite set of profile types must be closed under `k` nested reflections before
     `C_ref` is fixed.
   * Losses add over the `k + 1` same-width calls per level and do not multiply in the
     exponent.
5. **Premise.** The bias is present for every `n ≥ 3`: excess `X^{1/n}` at the balanced point,
   `X^{1/6}` for sextic. The cubic case differs in size, not in kind (Sec. 4.2).

The uniform-loss tolerance is confirmed [T3]. Under nesting, `κ = 5/6` closes for any extra
centred loss `cM` with `c < 1/12`, and fails at `c = 1/12`.

## 6. What remains for θ = 1 (nested route), in order of weight

1. **Lemma 18.1 itself (sextic), as a whole.** It is an unreviewed external claim that would
   beat the conjecturally optimal sextic large sieve. Our two bounded reviews found no error.
   They imported Lemmas kernel-seminorms, smooth-calculus and logarithmic-control, Sec. 18.8,
   the coefficient lemma and the centred-coefficient invariant.
2. **The n = 3 centred stage with `L` up to about 0.42M.**
   * It must deliver `r = (L - v)_+`.
   * It must satisfy `F_1 + F_2 ≥ (5/6)v` uniformly over all common-support and
     `𝔱`-allocations, which needs the redesigned `B_c`.
   * Its total loss must stay below `M/12`.
3. **Cubic finite lemmas:**
   * complete-support correlation at prime powers, including the unequal case `j_0 = 3`;
   * fixed-numerator-ray and Kummer with `μ_3`;
   * `eq:gauss-local` beyond spot checks;
   * the nonunit `i = 1` residue (for margin only).
4. **The nested ordering.** Logically sound. It needs only the restatements in Sec. 5, items
   3 and 4.

**Smallest statement whose failure breaks θ = 1:** for n = 3 and every centred input in the
padded core, the exceptional deficit must satisfy
`E - r ≤ A - 2M/3 - (5/6)L + O(σ + ξ)` with `L ≤ 0.42M`. Equivalently, the Patterson polar
part of every centred Gauss-row norm must cancel to relative precision `Z^{-(A - 2M/3)}`.

## Appendix: `nested_redteam_check.py` (exact text that was run)

```python
"""Independent red-team checks of the PROPOSED nested comparison ordering (exponent ledger only).
Written from the constraints as stated in CUBIC_RELAXED_INDUCTION.md Sec. 2/4, not from its code.
Units: M = 1.  theta = 1/n, s0 = 1 - theta + eta.  For a centred input of total A, comparison L:
  (C)  kappa*L - (A - s0) >= mu          (exceptional deficit, margin mu)
  (R)  s_prev - (1 - A + 2L) >= mu       (reflected comparison lands in an already proved range)
  caps 0 <= L <= A/2,  L <= A - 1/2 - mu (reflected comparison stays in the padded core).
EXACT_RATIONAL except where a float is printed."""
from fractions import Fraction as F
import itertools, sys

def window(A, kap, s0, sprev, mu):
    lo = max(F(0), (A - s0 + mu) / kap)
    hi = min((sprev - 1 + A - mu) / 2, A / 2, A - F(1, 2) - mu)
    return lo, hi

def covers(kap, s0, stages, Atop, mu, grid=600):
    """stages = [b_1 < b_2 < ... < b_k = Atop]: stage C_i covers (b_{i-1}, b_i] with b_0 = s0 and may call any
    proved range [0, b_{i-1}] (nested) -- check every grid A has a window with margin mu."""
    bounds = [s0] + list(stages)
    for i in range(1, len(bounds)):
        a0, a1 = bounds[i - 1], bounds[i]
        for t in range(1, grid + 1):
            A = a0 + (a1 - a0) * F(t, grid)
            lo, hi = window(A, kap, s0, bounds[i - 1], mu)
            if lo > hi:
                return False
    return True

def best_two_stage(kap, theta, eta, Atop):
    s0 = 1 - theta + eta
    best = None
    for b1n in range(820, 905, 1):             # split point b1 in [0.820, 0.904]
        b1 = F(b1n, 1000)
        lo_mu, hi_mu = F(-1, 10), F(1, 10)
        for _ in range(30):                      # bisection on mu (monotone)
            mid = (lo_mu + hi_mu) / 2
            if covers(kap, s0, [b1, Atop], Atop, mid, grid=120):
                lo_mu = mid
            else:
                hi_mu = mid
        if best is None or lo_mu > best[0]:
            best = (lo_mu, b1)
    return best

out = []
def rep(name, ok, extra=""):
    out.append((name, ok)); print(("PASS " if ok else "FAIL ") + name + ("  " + extra if extra else ""))

th3, k56 = F(1, 3), F(5, 6)
# [T1] uniform two-stage margin over the WHOLE padded core (2/3, 1 + 1/100], not only at A = M
mu, b1 = best_two_stage(k56, th3, F(0), F(101, 100))
rep("[T1] cubic kappa=5/6, eta=0: two centred stages cover (2/3, 1.01] with a uniform positive margin",
    mu > F(1, 100), "mu ~ %.4f M at split b1 = %s (note's A=M value 11/507 = %.4f)" % (float(mu), b1, 11 / 507))
# [T2] one centred stage cannot cover A = 1 at eta = 0 (single window), any margin >= 0
rep("[T2] cubic kappa=5/6, eta=0: single window fails at A = M (window empty)",
    (lambda w: w[0] > w[1])(window(F(1), k56, F(2, 3), F(2, 3), F(0))))
# [T3] uniform O(M) loss c added to every centred deficit: nested route survives iff c < 1/12
def closes_with_loss(c, kap=k56, s0=F(2, 3), kmax=60, Atop=F(1)):
    s = s0
    for _ in range(kmax):
        # largest A with nonempty window (margin 0), loss c in (C)
        cand = []
        cand.append(((2 / kap) * (s0 - c) + s - 1) / (2 / kap - 1))
        cand.append(((s0 - c) / kap) / (1 / kap - F(1, 2)))
        cand.append(((s0 - c) / kap - F(1, 2)) / (1 / kap - 1))
        new = max(s, min(cand))
        if new >= Atop:
            return True
        if new - s < F(1, 10 ** 9):
            return False
        s = new
    return False
rep("[T3] extra centred loss c*M: closes for c = 1/12 - 1/1000, fails for c = 1/12 + 1/1000 and c = 1/12",
    closes_with_loss(F(1, 12) - F(1, 1000)) and not closes_with_loss(F(1, 12) + F(1, 1000)) and not closes_with_loss(F(1, 12)))
# [T4] 'limit' cases need delta (padded-core excess) below a multiple of eta: sup reachable A
def sup_reach(theta, kap, eta, kmax=20000):
    s0 = 1 - theta + eta
    s = s0
    for _ in range(kmax):
        cand = [((2 / kap) * s0 + s - 1) / (2 / kap - 1), (s0 / kap) / (1 / kap - F(1, 2))]
        if kap < 1:
            cand.append((s0 / kap - F(1, 2)) / (1 / kap - 1))
        new = max(s, min(cand))
        if new - s < F(1, 10 ** 12):
            return new
        s = new
    return s
e = F(1, 1000)
r23 = sup_reach(th3, F(2, 3), e)
rq = sup_reach(F(1, 2), F(1), e)
rep("[T4] limit cases cap: cubic kappa=2/3 reaches at most 1 + 3eta/2, quadratic at most 1 + 2eta (eta = 1e-3)",
    abs(r23 - (1 + F(3, 2) * e)) < F(1, 10 ** 9) and abs(rq - (1 + 2 * e)) < F(1, 10 ** 9),
    "sup A: %s, %s -> padded-core delta must be < 3eta/2 resp. 2eta" % (float(r23), float(rq)))
# [T5] quadratic at eta = 0: the centred stage makes NO progress; with eta > 0 each stage gains exactly 2 eta
s = F(1, 2) + e
gains = []
for _ in range(5):
    lo_hi = None
    new = ((2) * (F(1, 2) + e) + s - 1) / (2 - 1)
    gains.append(new - s); s = new
rep("[T5] quadratic: s_i = 1/2 + (2i+1) eta, i.e. each centred stage gains exactly 2 eta; zero gain at eta = 0",
    all(g == 2 * e for g in gains) and window(F(1, 2) + F(1, 10 ** 6), F(1), F(1, 2), F(1, 2), F(0))[0]
    > window(F(1, 2) + F(1, 10 ** 6), F(1), F(1, 2), F(1, 2), F(0))[1])
# [T6] well-founded order: nodes (band b, stage j), j = 0 (U), 1..k (C_j), k+1 (reflection closure)
def call_graph(nb, k):
    E = []
    for b in range(nb):
        for j in range(k + 2):
            for bb in range(max(0, b - 4), b - 1):  # children drop width >= sigma/2 = two bands of sigma/4
                for jj in range(k + 2):
                    E.append(((b, j), (bb, jj)))
            if 1 <= j <= k:
                for jj in range(0, j):              # nested comparison: same width, strictly earlier stage
                    E.append(((b, j), (b, jj)))
            if j == k + 1:
                for jj in range(0, k + 1):
                    E.append(((b, j), (b, jj)))
    return E
import collections
def longest_path(nb, k):
    E = call_graph(nb, k)
    adj = collections.defaultdict(list)
    for u, v in E:
        adj[u].append(v)
    memo, onstack = {}, set()
    def lp(u):
        if u in memo:
            return memo[u]
        if u in onstack:
            raise RuntimeError("cycle")
        onstack.add(u)
        r = 1 + max([lp(v) for v in adj[u]], default=0)
        onstack.discard(u); memo[u] = r
        return r
    sys.setrecursionlimit(100000)
    return max(lp((b, j)) for b in range(nb) for j in range(k + 2))
ok = True
rows = []
for nb in (8, 16, 32):
    for k in (1, 2, 3):
        L = longest_path(nb, k)
        rows.append((nb, k, L))
        strict = (nb + 1) // 2
        if L > strict * (k + 2):
            ok = False
rep("[T6] call graph acyclic; longest chain <= (#strict levels) * (k + 2)", ok, str(rows))
# [T7] rational check of the note's equalised margins at A = M (depth 1, 2) from the closed recursion
def eq_margin(depth, kap=k56, s0=F(2, 3)):
    al, be = F(1), F(0)
    for _ in range(depth):
        al, be = 1 - al + 2 * (al - s0) / kap, -be + 2 * (be + 1) / kap
    return (s0 - al) / (1 + be)
rep("[T7] equalised margins at A = M: depth 1 -> -2/51, depth 2 -> 11/507", eq_margin(1) == -F(2, 51) and eq_margin(2) == F(11, 507))
print("SUMMARY %d/%d" % (sum(o for _, o in out), len(out)))
```

Output:

```
PASS [T1] ... uniform positive margin  mu ~ 0.0155 M at split b1 = 867/1000 (note's A=M value 11/507 = 0.0217)
PASS [T2] cubic kappa=5/6, eta=0: single window fails at A = M (window empty)
PASS [T3] extra centred loss c*M: closes for c = 1/12 - 1/1000, fails for c = 1/12 + 1/1000 and c = 1/12
PASS [T4] ... sup A: 1.0015, 1.002 -> padded-core delta must be < 3eta/2 resp. 2eta
PASS [T5] quadratic: s_i = 1/2 + (2i+1) eta, ...; zero gain at eta = 0
PASS [T6] call graph acyclic; ... [(8, 1, 12), (8, 2, 16), (8, 3, 20), (16, 1, 24), (16, 2, 32), (16, 3, 40), (32, 1, 48), (32, 2, 64), (32, 3, 80)]
PASS [T7] equalised margins at A = M: depth 1 -> -2/51, depth 2 -> 11/507
SUMMARY 7/7
```

`t1c.py` repeats [T1] with 400-point grids per stage and a split search over `[0.840, 0.899]`.
It gives a margin of `0.01794` at split `0.861` for `A ≤ 1`, and `0.01555` at split `0.867`
for `A ≤ 1.01`.
