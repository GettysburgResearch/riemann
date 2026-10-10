# Relaxed and nested induction for the cubic transfer of Lemma 18.1

```text
Status: EXPLORATION. Exponent ledgers only. The nested-comparison ordering (Sec. 4) is PROPOSED,
  not in the paper and not proved. The (2,1) forcing check (Sec. 5) is a structural argument
  backed by finite exact or floating local computations. Every bound below is CONDITIONAL on the
  unverified parts of Lemma 18.1. No moment bound is proved. RH is not addressed.
Scope: case 1 (z = 0) of Lemma 18.1 (lem:plain) of the external, unreviewed OpenAI manuscript
  "The Quasi-Riemann Hypothesis" (30 Sep 2026), transferred to cubic Hecke characters over
  Q(omega) as in CUBIC_FOURTH_MOMENT_TRANSFER.md. This note covers four things: (1) the relaxed
  induction with loss eta, written out step by step; (2) its optimal eta in the paper's induction
  order and in a nested order; (3) whether the proposed (2,1)-residue forcing survives extraction,
  t-allocation and positivity; (4) a literature check for cubic fourth moments.
Exact sources or dependencies:
  pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, standalone/2026-10-07-openai-quasi-riemann-
    import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
    sha256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-hashed).
    Read as untrusted data: l. 7042-7120 (Fourier lemmas), 12880-13060 (induction order,
    comparison), 13110-13360 (first transform), 13596-13700 (second transform), 14312-14810
    (Theta rows, centred cancellation, completion).
  CUBIC_FOURTH_MOMENT_TRANSFER.md, reviews/LEMMA18_1_REVIEW.md.
  scripts/cubic_fourth_moment_ledger.py (sha256 5c79445b...8380d5), imported read-only.
  a2/eis.py (sha256 87ca11d9...798e65), imported read-only.
  Literature: arXiv API listings and arXiv e-print sources (grep only) of 0804.2233, 2410.03048,
    2607.07911 and 2610.04045 (Sec. 7).
What was actually run:
  python3 -I scripts/cubic_relaxed_induction.py  -> 39/39 PASS, about 14 s, one process.
    Output: results/cubic_relaxed_induction_output.txt. It re-runs the old ledger (31/31) on
    import.
  Three arXiv API searches, two id lookups, four e-print downloads (read with grep and sed only).
Smallest remaining gap: the best exponent, theta = 1, needs one new ordering step that the paper
  does not contain. The centred stage at width M must accept the reflected comparison rectangle
  as input. That rectangle is an admissible datum of the same width with total length
  A_comp < A, and it is the same input class the paper already feeds to its uncentred stage. On
  top of this, every unverified common-support step of the paper must hold for n = 3, with no loss
  of order M. Without nesting the best value is 53/51; with the (2,1) forcing it is 1, with zero
  slack.
```

RH is unsolved, and nothing here bears on it directly. "Closes" means only that the affine
exponent ledgers balance. All lengths are in units of `log Z`. `M = m + q`, `A = n_1 + n_2`,
`θ = 1/n`, and the final application has `q = 0`, `X = Z^m`.

## 0. Summary

1. **Relaxed induction in the paper's order.** Comparisons may call only the uncentred stage.
   The optimal loss is exactly `η = 2/51`; it is both necessary and sufficient [S1-S4].
   * The bound would be `X^{53/51+ε}`.
   * With no forcing at all, so `κ_2 = 2/3`, it is `η = 1/12`.
   * With the (2,1) forcing it is `η = 0`, with zero slack.
2. **Nested comparisons (PROPOSED).** A comparison may instead call an earlier *centred* stage at
   the same width. The scheme then closes iff `η > θ - κ/2` [N7].
   * For the mechanical cubic transfer `κ = 5/6`, so it closes at `η = 0` with positive margin,
     **without the (2,1) repair**.
   * Two centred stages suffice: `s_0 = 2/3`, `s_1 = 19/21`, `s_2 = 158/147 > 1` [N1].
   * The best uniform margin at `A = M` is `11M/507` with two stages and tends to `M/12` with
     more stages [N8, N9].
3. **Quadratic calibration turns positive.** With nesting the quadratic model gives
   `K^{1+ε}` as a limit. That is Heath-Brown's bound, where the single-window model gave only
   `K^{7/6}` [N5, V3].
4. **The (2,1) forcing survives.** The forced residue is a property of the C-side child
   character at `p ∈ 𝔯`, fixed in the first transform. Second-transform allocations, `t`-labels
   and positivity never touch `p`. The finite checks confirm each algebraic link for n = 3
   [L1-L6]. The step is not needed under nesting; with it the margin limit becomes `M/6`.
5. **Literature.** No unconditional cubic fourth moment better than `X^{4/3+ε}` was found.
   * de Faveri's optimal large sieve (arXiv 2610.04045, 2 Oct 2026) coincides with Heath-Brown's
     for n = 3.
   * de Faveri-Dunn-Hoffstein (2607.07911) prove unconditionally that the operator norm is
     `≫ X^{4/3-ε}`.
   * David-de Faveri-Dunn-Stucky state that "an optimal fourth moment bound is not available in
     the cubic case".

## 1. The relaxed hypothesis

> **H(M; η).** For every admissible zero-slot datum of width `M` (cubic rows `k ∈ Z[ω]`,
> `ψ_k(n) = τ(n)(k/n)_3`, the paper's masks, moving supports and profiles, arbitrary bounded
> `n_1, n_2`) and every `ε > 0`:
> `Σ_{k ∈ R_0} |S_{ψ_k}(n_1;W_1) S_{ψ_k}(n_2;W_2)|² ≪_ε Z^{(1+η)M + ε}`.

The loss is proportional to `M`. Children have smaller width, so their absolute loss is smaller
[R2].

**Induction order.** Widths are taken in bands of length `σ/4`, in increasing order. Within a
band:

* `U`: the uncentred stage, for `A ≤ s_0 M` with `s_0 = 1 - θ + η`;
* `C_1, …, C_k`: centred stages, where `C_i` covers `A ∈ (s_{i-1}M, s_iM]`;
* reflection then supplies all other lengths.

The paper has `k = 1`, and its comparisons call only `U` (l. 14799: "A centered comparison
calls only the earlier uncentered stage in its band"). The nested version lets `C_i` call
`C_{i-1}`. There is no same-band cycle, because the stages are strictly ordered.

## 2. Step ledger: excess over `(1+η)M` (n = 3)

Terminal `O(σ, δ, ξ)` terms are listed but go into `ε`, not `η`. The script section is in
brackets.

| step (paper lines) | excess over `(1+η)M` | condition |
|---|---|---|
| base `M ≤ ρ` (12938-12950) | `A - q - ηM ≤ ρ + δ` | terminal |
| reflection to the padded core (12602-12830) | `n_i ≤ M/2 + ξ`, `A ≤ M + δ` | none (η-free) |
| zero frequency (13180-13190) | `m - (1+η)M ≤ -ηM` | none |
| first-transform ledger (13350-13409) | `(B_c+B_d-(c+d-2p-R))/2 + (x_C+x_D)/2 - ηM`, where `x` is each norm's excess over its unrelaxed target [R1] | `B_c = ((3c-4d-2R)/6)_+` fits the budget [old B8]; each norm fits its target `+ηM` |
| Gauss-row zero `h = 0` (13572-13594) | `2a_0/3 - 2s_0 - (a_0 - s_0) ≤ 0` [old E1] | none |
| diagonal `j = 0` (old-eq:2.12) | `(A-M) - d - (K_0-K) - w_o - B_c + g - ℓ - ηM ≤ δ + 5σ/3 + δ_fr - ηM` [R4] | `A ≤ M + δ` |
| non-exceptional children (old-eq:2.13-2.14) | `η(M'-M) = η(J - g - g_2 + t_2) ≤ -ησ` [R2, R2b] | width drop `≥ σ` |
| exceptional rows, uncentred (old-eq:2.15-2.16) | `A - (2/3+η)M - F_1 - F_2` [R3] | `F_1, F_2 ≥ 0`, so **(U)** `A ≤ (2/3+η)M` |
| exceptional rows, centred (old-eq:2.18-2.19) | `A - (2/3+η)M - F_1 - F_2 - (L-v)_+ ≤ A - (2/3+η)M - κL` | **(C)** `κL ≥ A - (2/3+η)M` |
| comparison (12940-13010) | bound of the reflected rectangle, total `A_comp = M - A + 2L + ξ` | **(R)** `A_comp` lies in a range already proved at width `M` |
| caps | comparison sides `≥ L`; reflected comparison stays in the core | `L ≤ A/2`, `L ≤ A - M/2` |

Here `F_1 + F_2 ≥ κ v` with `v = c + w + min(c_2, d_2)` and `κ = min(κ_1, κ_2, 1)`. The values
for the cubic transfer are:

* `κ_1 = 5/6`, attained at the first-transform primes `(2,1)`; `κ_1 = 1` with the (2,1) forcing.
* `κ_2 = 1` with the nonunit `i = 1` device (residue 1 mod 3, the analogue of l. 14354), or
  `2/3` without it.

The max over `v` of `-κv - (L-v)_+` is `-κL` for `κ ≤ 1`.

**Closing condition.** Every `A ∈ (s_0 M, (1+δ)M]` needs an `L` satisfying (C), (R) and the caps.

* **Single window:** (R) reads `M - A + 2L ≤ s_0 M`.
* **Nested:** (R) reads `M - A + 2L ≤ s_{i-1} M`, where

      s_i = max{A : ∃L, (A - s_0)/κ ≤ L ≤ min((s_{i-1} - 1 + A)/2, A/2, A - 1/2)}   (M = 1).

## 3. Optimal η in the paper's order (single window)

At `A = M` the window is `[(θ-η)/κ, (1-θ+η)/2]`. It is nonempty iff

    η ≥ η_S(θ,κ) = ((2θ - κ(1-θ))/(2+κ))_+ .

The window shrinks as `A` grows, so `A = M` is the binding point.

| family | `κ` | `η_S` | `L` at `A = M` | bound |
|---|---|---|---|---|
| sextic (paper) | 2/3 | 0 | `[1/4, 5/12]` | `X^{1+ε}` |
| cubic, mechanical (paper's devices only) | 5/6 | **2/51** | `{6/17}` | `X^{53/51+ε}` |
| cubic, no forcing anywhere | 2/3 | 1/12 | `{3/8}` | `X^{13/12+ε}` |
| cubic + (2,1) forcing | 1 | 0 (zero slack) | `{1/3}` | `X^{1+ε}` |
| quadratic | 1 | 1/6 | `{1/3}` | `K^{7/6+ε}` |

**`2/51` is exactly right for this order.**

* At `η = 2/51 - t/10⁶` (`t = 1…2000`) the `A = M` window is empty [S3].
* At `η = 2/51` every `A` on a 1201-point exact grid of `[s_0, M]` has a nonempty window [S4].
* `L` must depend on `A`.
* No other step binds: the diagonal, the children and the zero frequency all have excess
  `≤ -ηM` plus terminal terms.

Within this order it **cannot be improved** without a larger `κ` or a larger centred saving.

## 4. Nested comparisons (PROPOSED): optimal η

**The device.** At a centred `A`, the comparison rectangle `(L, A-L)` is reflected to
`(L, M-A+L)`, which has total `A_comp = M - A + 2L`. The paper bounds it by the uncentred stage,
so it needs `A_comp ≤ s_0`. Logically it only needs H at width `M` and total `A_comp`. If
`A_comp` lies in an earlier centred range, the earlier centred stage applies.

* The reflected rectangle is an admissible datum. `|S_{ψ̄}(n;W)| = |S_ψ(n;W̄)|`, so it is again a
  product of two `ψ_k`-sums; the row-dependent dual scale is boxed into `O(log² Z)` unit boxes
  exactly as in the paper.
* The caps keep it in the padded core.

**Result** [N1-N7]. The recursion `s_i` passes `1` in finitely many stages iff `η > θ - κ/2`. So

    η_N(θ,κ) = (θ - κ/2)_+ ,   with margin up to (κ/2 - θ)M at A = M when κ > 2θ.

| family | `κ` | `η_N` | stages at `η = 0` | margin limit at `A = M` |
|---|---|---|---|---|
| sextic (paper) | 2/3 | 0 | 1 (`s_1 = 7/6`) | `M/6` |
| **cubic, mechanical** | 5/6 | **0** | **2** (`2/3 → 19/21 → 158/147`) | `M/12` |
| cubic, no forcing anywhere | 2/3 = 2θ | 0 (only as a limit) | never at `η = 0`; `η = 10⁻³` needs 7 stages, `10⁻⁴` needs 11 | 0 |
| cubic + (2,1) forcing | 1 | 0 | 2 (`s_1 = 1`, `s_2 = 4/3`) | `M/6` |
| quadratic | 1 = 2θ | 0 (only as a limit) | never at `η = 0`; `η = 10⁻³` needs 250 stages | 0 |

**Explicit cubic chain at `A = M` without the (2,1) forcing** [N10, N11, P1-P3]:

* Start from `n_1 = n_2 = M/2` and take `L_1 = 21M/50`.
  * The comparison rectangle `(21/50, 29/50)` reflects to `(21/50, 21/50)`, total `21M/25`.
  * The centred margin is (C) `= -M/60`.
* At `21M/25`, take `L_2 = 23M/100`.
  * The comparison rectangle `(23/100, 61/100)` reflects to `(23/100, 39/100)`, total
    `31M/50 ≤ 2M/3`. That is uncentred with margin `7M/150`.
  * The centred margin is (C) `= -11M/600`.
* On the explicit (2,1) path the maxima of the exceptional excess are `-M/60` and `-11M/600`. The
  single window at `L = M/3` had `+M/18`.
* The same `L_1, L_2` still work at `A = M + M/100`.
* The best uniform margin is `11M/507` with two stages, `202M/4299` with three, and tends to
  `M/12` [N8, N9].

**What the device assumes** (the only new logical content):

* (i) The centred stage at width `M`, as proved in Sec. 18.6-18.7, applies to every admissible
  datum with total `≤ M + δ`, not only to original inputs. The paper's own uncentred stage is
  used this way already.
* (ii) `L` depends on `A` and the stage.
* (iii) The loss bookkeeping takes `k` same-width calls. Each adds `C_*ξ`, and the comparison
  bound enters through `|S|² ≤ 2|Δ|² + 2|comp|²`, so the losses are a maximum plus `O(kξ)`.

I found nothing in l. 12903-12938 or 14779-14810 that forbids this. It is a reordering, not a new
estimate. It has not been checked against the unverified bookkeeping of Sec. 18.4-18.6.

**Calibration.** For n = 2, `κ = 1 = 2θ` is critical, and the nested model gives `K^{1+ε}` as a
limit. That matches Heath-Brown's quadratic large sieve, which is itself proved by an iteration
with ε-losses. The transfer note's negative calibration (`K^{7/6}`) was an artefact of the single
window. This supports, but does not prove, that the nested reading is the natural one.

## 5. The (2,1)-residue forcing: does it survive?

**Claim (PROPOSED, argued below).** Let `p ∈ 𝔯` be a first-transform common prime with
`i - j ≡ 1 (mod 3)`, where `i = v_p(C)` and `j = v_p(D)`. Then a C-norm child row `h'` can be
exceptional only if `v_p(h') ≡ 1 (mod 3)`. The count therefore gains `Z^{-(1/3)log_Z q_p}`.

**Where the residue comes from.**

* The bridge gives the C side the moving character `τ_C(a) = τ(a)χ_a(𝔢𝔯)ξ_𝔯(a)`, with
  `ξ_𝔯 = Π χ_p^{i_p-j_p}` (l. 13228-13271).
* Cubic reciprocity has no phase for primary elements, so `χ_a(p) = χ_p(a)` [L1: 5852 pairs].
* The CRT phase of the bridge holds verbatim for n = 3 [L3]. Hence the C-side factor at `p` is
  `χ_p(a)^{1+i-j}`, which is `χ_p(a)²` at `(2,1)` [L3b].
* The second transform gives `F(D_2a, E_2b; j) ∝ χ_a(j)\overline{χ_b(-j)}` (l. 13690-13695). For
  cubic coprime primes this is exactly `F(u,v;j) = χ_u(j)\overline{χ_v(-j)}` [L4], so the sign is
  `χ_u(j)`, not its conjugate.
* The child u-character at `p` is therefore `χ_p(u)^{1+i-j+v_p(j)}`. Computed with actual
  symbols, it is unramified at `p` iff `v_p(j) ≡ 1 (mod 3)` [L5, `t = 0…6`].
* The C-side residue is 1 exactly for `i - j ≡ 1`, and the D side has the mirror pattern [L5b].
* `p` is a genuine 𝔯-prime: its row mean is 0 [L6a]. The local Gauss sum mod `p²` reduces to
  modulus `p` [L6b]. The cubic `eq:gauss-local` holds at `N p = 7, 13` [L2].

**Survival through each later operation.**

* **Complete common-support extraction (second transform).** The paper itself says (l. 14317-14326):
  * every prime of the full displayed moving support (which includes 𝔯) is a common column zero;
  * every genuine second allocation therefore has radical disjoint from it.

  The columns `a, a'` of `N_C` are coprime to `CD`. That holds also for the artificial
  noncoprime pairs of `𝒞_1`, which are "individually disjoint from CD" (l. 13306-13308). So no
  second-transform prime equals `p`, and the factor `χ_p(u)^{1+i-j}` is carried unchanged into
  `τ_1(u)`.
* **`t`-allocation.** The `t`-labels and the frozen extraction scalars `c_{t,J}(h')` live at
  second-transform common or unit primes, which are disjoint from `p`. They multiply the row
  sum by scalars and do not change the u-character at `p`.
* **Positivity.**
  * The h-ball enlargement `K → K+g` and the added row `h = 0` change only nonnegative
    `h`-weights, not the `u`-coefficients.
  * The "rows admitted after positivity" (l. 14387-14391) occur at the unit primes `t_2`, which
    are second-transform primes. The paper explicitly takes no forcing there.
  * The forcing at `p` is not a row restriction that positivity could relax. It is a
    *character* statement: a row with `v_p(h') ≢ 1` has an inducing character ramified at `p`,
    so it is non-exceptional and is counted by the induction hypothesis.
* **Fixed-ray phases.** `p ∉ S`, so the finitely many ray characters at `S` do not interact with
  it. For n = 3 the reciprocity bicharacter is trivial on primary elements.

**Verdict on the repair.** It survives. It is an instance of the paper's own sentence (l. 14359-14363):
"at every prime outside 𝒮, exceptional induction prescribes a single residue class … determined
by the frozen moving character". The paper uses this sentence only for `G_cV_id`.

* **Residual risk.** Some unverified step of l. 13192-13349 might replace the u-dependent factor
  at `p` by an absolute value. That would also destroy the "children are plain Hecke sums"
  structure the paper relies on.
* **Effect.** The step raises `κ_1` to 1, giving zero slack in the single window and margin
  `M/6` when nested. Under nesting it is **optional**.

## 6. What the result would be

> **CONDITIONAL statement.** Assume:
> * the scheme of Lemma 18.1, case 1, is correct, in particular its unverified common-support
>   bookkeeping (l. 13192-13349, 13686-13933) and Lemmas smooth-calculus, kernel-seminorms and
>   logarithmic-control;
> * its cubic transfer holds (steps 2-6 of Sec. 8);
> * the nested comparison ordering of Sec. 4 is admissible.
>
> Then `Σ_{c ≡ 1 (9) sf, N c ≤ X} |L(1/2+it, χ_c)|⁴ ≪_ε X^{1+ε}(1+|t|)^{O(1)}`.
>
> * **θ = 1**, with exponent margin `11M/507` (two stages) up to `M/12` at the balanced point.
> * The (2,1) forcing is not needed.
> * Without the nested ordering: `θ = 53/51`, or `θ = 1` with zero slack if the (2,1) forcing of
>   Sec. 5 is added.

This would be the first Lindelöf-on-average cubic fourth moment, and it would be new. It is
**not** established here. Its weight raises the stakes of an expert line check of Lemma 18.1.

## 7. Literature (primary sources only)

| source | what it gives for the cubic fourth moment |
|---|---|
| Heath-Brown cubic large sieve, quoted verbatim in Baier-Young 0804.2233 (eq. HBcubic) and de Faveri 2610.04045 (eq. BGL_bound) | `(M + N + (MN)^{2/3})`. At `M = N = X` this gives `X^{4/3+ε}` |
| de Faveri, arXiv **2610.04045** (v1, 2 Oct 2026), Thm 1.1 | optimal n-th order large sieve `A + B + A^{1-1/n}B^{2/n} + A^{2/n}B^{1-1/n}`. **For n = 3 this equals Heath-Brown's bound**, so there is no gain for the fourth moment. The applications are second moments (Thm 1.2: cubic second moment ordered by conductor `≪ X^{1+ε}`; Thm 1.3: secondary term `X^{5/6}`) and zero density |
| de Faveri-Dunn-Hoffstein, arXiv **2607.07911** (Jul 2026) | the cubic and quartic large sieves are not perfectly orthogonal, **unconditionally**. The operator-norm lower bound is `≫ X^{4/3-ε}` at `A ≍ B ≍ X` (source l. 209). The large-sieve route is capped at `X^{4/3}` |
| David-de Faveri-Dunn-Stucky, arXiv **2410.03048** (v2) | mollified second moment, and a Lindelöf-on-average second moment of cubic Dirichlet series. Source text: "the cubic large sieve is *not* perfectly orthogonal, so an optimal fourth moment bound is not available in the cubic case" |
| Baier-Young, arXiv **0804.2233** (JNT 2010), "Mean values with cubic characters" | cubic *Dirichlet* characters over Q (a thinner family): first moment asymptotic; second moment `≪ Q^{6/5+ε}`; Hecke variant `M^{3/2+ε}`; large sieve `Δ(Q,M)`. **No fourth moment** |
| Gao-Zhao, arXiv 2104.09909 | sharp upper bounds for all moments of cubic and quartic Dirichlet families **under GRH** |

The search covered:

* `abs:"fourth moment" AND abs:cubic` (10 hits);
* `abs:cubic AND abs:"large sieve"` (14 hits);
* `abs:cubic AND abs:Hecke AND abs:moment` (16 hits), all read to 2610.*.

**No unconditional cubic fourth-moment bound better than `X^{4/3+ε}` was found.** The usual
alternative, Weyl-type pointwise times the Lindelöf-on-average second moment, also gives
`X^{4/3}`; this is my estimate and was not taken from a source. Journal-only papers outside
arXiv were not searched.

Consistency: the non-orthogonality results concern general coefficients. The scheme uses the
divisor-type structure (every child is a reflectable plain Hecke sum), so `θ = 1` contradicts
none of them.

## 8. Verdict

**Explicit θ.**

* `θ = 53/51` in the paper's order, with `2/51` exactly optimal there.
* `θ = 1` with the (2,1) forcing, at zero slack.
* `θ = 1` with margin `M/12` (limit) under the PROPOSED nested ordering, with no new forcing.

All are CONDITIONAL.

**Exact list of unproved steps for θ = 1 (nested route):**

1. All unverified parts of Lemma 18.1 for n = 3:
   * the first transform with common support, l. 13192-13349;
   * the second-transform extraction, l. 13686-13933;
   * Lemmas smooth-calculus, kernel-seminorms and logarithmic-control, l. 1123-1600;
   * the coefficient lemmas.
2. Cubic finite Fourier lemmas. `eq:gauss-local` [L2] and full correlation [L4] were spot-checked
   for small primes. Complete-support correlation at prime powers was not checked.
3. The Kummer and fixed-numerator-ray lemma with `μ_3`, and the count `Z^{(m'-f)/3}`.
4. The cubic allowance `B_c = ((3c-4d-2R)/6)_+` (ledger checked, old [B8]).
5. The nonunit `i = 1` forcing (residue 1 mod 3), the analogue of l. 14354.
   * It is needed for `κ = 5/6`.
   * Without it, `κ = 2/3 = 2θ`, which gives θ = 1 only as a limit with zero margin.
6. **New:** the nested comparison ordering (Sec. 4, items (i)-(iii)).

Not needed: the (2,1) forcing of Sec. 5. It is optional and survives on the argument above.

**Smallest statement whose failure breaks θ = 1.** For n = 3, uniformly over every
common-support allocation and with `L ≤ M/2`, the centred exceptional deficit must satisfy

    E - r ≤ A - 2M/3 - (5/6)L + O(σ + ξ),

and the centred stage must accept reflected comparisons as input.

* A uniform loss of size `cM` inside the bookkeeping, with `c ≥ 1/12`, breaks the nested route.
* With only the paper's order, any `c > 0` breaks it, unless one accepts `θ = 53/51` or uses the
  (2,1) forcing.

## 9. Files

* `scripts/cubic_relaxed_induction.py`: sections [R], [S], [N], [P], [L], [V]. Exact rationals,
  except the floating Gauss sums in [L2], [L3] and [L6b], which are labelled.
* `results/cubic_relaxed_induction_output.txt`: its output (39/39).
