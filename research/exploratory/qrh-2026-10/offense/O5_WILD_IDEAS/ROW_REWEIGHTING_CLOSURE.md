# No reweighting of Oct 5-type inputs beats 11/12: rows, scales, heights, kernels

```text
Status: PROPOSED (Prop. W and Lemmas W1-W4 are elementary and proved here; not reviewed)
  + exact rational bookkeeping (triage_exponents.py, all asserts pass). No zero-free region is
  proved; RH is unsolved. Everything resting on the Oct 5 manuscript is IMPORTED/CONDITIONAL.
Scope: extraction arguments for the principal member A_1(D) of the Oct 5 sextic Moebius family
  that combine, with nonnegative weights, (i) second-moment bounds over any dyadic row ranges,
  (ii) any column scales D' and smooth weights W, (iii) archimedean twists N(n)^{-it} or angular
  Groessencharacter twists as extra rows, (iv) positive-definite kernels across scales,
  (v) a family-wide pointwise bound (e.g. the imported 7/8), (vi) row-multiplicity zero-density
  counts. Covers seeds 3, 6 and 8 of the O5 brief and the "own ideas" N-a, N-c, N-d.
Exact sources or dependencies: RUNG_STRENGTH.md (leverage law, Prop. R, Prop. R', rho = 1 wall);
  DISPERSION_GRH_STEP.md Sec. 3(c) (zero-density bootstrap); DETECTOR_DENSITY.md (Sep 30 inner
  detector f(sigma)); LEVERAGE_FAMILIES.md Sec. 2.3; Oct 5 manuscript paper2.tex (IMPORTED,
  unreviewed): eq:intro-ms, eq:intro-extraction.
What was actually run: python3 -I triage_exponents.py (sympy, exact rationals, ~2 s); output in
  triage_exponents.out. python3 -I kappa_window.py (moments/ C kernel, binary64, ~1 min; EMPIRICAL,
  finite) -> kappa_window.json.
Smallest remaining gap: a coefficient-specific bound at a SINGLE sub-diagonal row range,
  sum_{N u <= D^(1-eta)} |A_u(D)|^2 << D^(2 - (1-kappa) eta), with kappa < 5/6 for some eta > 0
  (the kappa-law, Sec. 3). Prop. L (Sec. 3, PROPOSED, conditional on Oct 5 as stated) shows that
  lifting by p^6 already gives kappa = 5/6 for every eta < 6/11, and that kappa = 5/6 is a fixed
  point of lifting; nothing known supplies kappa < 5/6.
```

RH remains unproved. The 11/12 and 7/8 statements are external, unreviewed claims (the 7/8 Lean
statement is kernel-checked under the trust assumptions in `reviews/LEAN_BUILD_ATTEMPT.md`).

## 1. The question

The Oct 5 extraction uses one row range (`H = D^{1+θ}`), one column scale `D`, one weight `W`
and counting measure on rows. Seeds 3, 6, 8 ask whether *combining* many such inputs (multi-scale
large values, hybrid row × scale or row × height families, Größencharacter twists, zero density
with multiplicity) moves the exponent. This note proves that, for every combination built from
the currently available inputs by positivity, the answer is no, and isolates the single
statement that would be needed.

## 2. Proposition W (PROPOSED, proved here)

**Inputs.** For all `x ≥ 0`, all scales `D' ∈ [D^{1/2}, D]`, every smooth `W` on `[1,2]`:

* (I1) `S_x(D', W) := Σ_{N u ∼ D^x} |A_u(D'; W)|² ≪ D'^{1+ε} max(D^x, D'^{1+θ})` (Oct 5 at
  `ρ ≥ 1`, IMPORTED; positivity from the range `D'^{1+θ}` below it);
* (I2) `|A_u(D'; W)| ≪ D'^{σ₀+ε} (N u)^ε` for every row (family-wide pointwise input);
* (I3) hybrid rows `(u, t)`, `|t| ≤ D^τ`, with the twist `N(n)^{−it}`, and the hybrid bound
  `Σ_u ∫ |A_{u,t}|² dt ≪ D^{1+ε}·max(D^{x+τ}, D)` (a hybrid large sieve at its optimal shape;
  this is *granted*, not known, so the conclusion is stronger than needed).

**Extraction schemes.** Choose nonnegative weights `ω` on (range, scale, weight, height), drop all
non-principal terms by positivity, and use `A_{v^6}(D') = A_1(D') + O(D'/N v)` on the principal rows
(Oct 5 eq:A_u-vs-A_1).

**Proposition W.** Every such scheme gives at best `A_1(D) ≪ D^{min(σ₀, 11/12)+ε}`. The same holds
with the zero-density input (Z2) of DISPERSION_GRH_STEP §3(c) for every `A ≥ 2`.

*Proof.* Four lemmas.

**Lemma W1 (mediant).** For nonnegative `a_i`, positive `b_i`: `Σ a_i / Σ b_i ≥ min_i a_i/b_i`.
So a weighted sum of extraction inequalities `P_i |A_1|² ≤ B_i` never beats the best single one.

**Lemma W2 (one range).** Range `x` has `≍ D^{x/6}` principal rows (`u = ε v⁶`). With (I1) at `D' = D`,
`|A_1(D)|² ≤ D^{1 + max(x,1) − x/6}`. The exponent `(1 + max(x,1) − x/6)/2` equals `1 − x/12`
for `x ≤ 1` (decreasing) and `1/2 + 5x/12` for `x ≥ 1` (increasing), so its minimum is `11/12`
at `x = 1` (sympy: `D1 best over all dyadic ranges (x=1): 11/12`).

**Lemma W3 (other scales, kernels, heights).**
* *Scales.* A bound at scale `D' < D` controls `A_1(D')`, not `A_1(D)`. A zero `ρ₀ = β + iγ` of
  `L(s, ν)` makes `A_1(D') ≍ D'^β` along a positive-density set of `log D'`, so each scale yields
  the same constraint `β ≤ 11/12`. Scale invariance of W2 (all exponents are homogeneous in
  `log D'`) means no scale is better. Coherent combination over `J` scales gains at most `J²`,
  and in `[D^{1/2}, D]` the effectively independent scales number `J ≪ D^ε` (the Mellin transform of
  `log D' ↦ A_u(D')` is band-limited to `|Im s| ≪ D^ε` by the decay of `Ŵ`). So the gain is
  `D^{ε}` (sympy: coherence exponent gain 0).
* *Positive-definite kernels across scales* act as Mellin multipliers `κ(t) ≥ 0`. The diagonal and
  the zero's contribution are both reweighted by `κ`: the diagonal becomes
  `≍ D H ∫ |Ŵ(1/2+it)|² κ(t) dt`, the zero term `≍ H^{1/6} D^{2β} |Ŵ(ρ₀)|² κ(γ)`. This is the
  same as replacing `W` by a weight `W_κ`, and Prop. R / eq:power-savings already range over all
  `W`. The ratio, hence the exponent, is unchanged.
* *Diagonal-free cross moments.* `Σ_u A_u(D) conj A_u(4D)` has no diagonal (disjoint column
  supports), and its dual diagonal also vanishes. But its principal part
  `H^{1/6} A_1(D) conj A_1(4D)` is not sign-definite, so it cannot be isolated by positivity; any
  Hermitian completion `Σ_u |Σ_j c_j A_u(D_j)|²` restores the diagonals `Σ_j |c_j|² S(D_j)`, and
  W1 plus the coherence count above apply. (Own idea N-a: DEAD at exactly this step.)
* *Heights / angular twists.* Rows `(u, t)` are principal only for `u = ε v⁶` and `|t| ≪ 1`:
  `A_{1,t}` is not `A_{1,0}` for `|t| ≫ 1`. With `D^{h+τ}` rows, the threshold `h + τ ≥ 1`, and
  `D^{h/6}` principal rows, the boundary is `(1 + h + τ − h/6)/2`, which on `h + τ = 1` equals
  `1 − h/12 ≥ 11/12` (sympy: `M4 hybrid`). Angular twists `α^k`, `|k| ≤ H^τ`, give leverage
  `c = 1 − 1/(6(1+τ)) > 5/6` (sympy: `M9`).

**Lemma W4 (pointwise and density inputs).**
* (I2) in Hölder form gives `σ₁ = (σ₀(k−1) + 11/12)/k`, whose fixed point is `11/12`; at
  `σ₀ = 7/8` the output exceeds the input by `1/(24k)` (sympy: `M2`). With (I2) used directly, the
  answer is `σ₀` itself. Mixed moments (`j` factors at scale `D`, `k − j` at `D'`) have the same
  homogeneous bookkeeping.
* (Z2) with DH (`A = 2`) and `β* = 7/8` gives `7/8 + ρ/24` (sympy). Its fixed point is
  `1 − 1/(6A)`; any (Z2) with `A(σ)(1−σ) < 1/6` at some `σ < 11/12` *contains* the
  conclusion, because the `Q = 1` member (`ψ_u` principal) has multiplicity `≍ H^{1/6}`. So (Z2)
  cannot be proved from general-coefficient large values. For reference, if it held, Huxley-type
  `A = 3/(3σ−1)` would give `19/21`, Ivić-type `A = 3/(2σ)` would give `9/10`, and a Ford-type
  `58.05(1−σ)^{3/2}` only `0.9798`.

Combining W1–W4: the best scheme is a single range `x = 1` at scale `D` (11/12) or the pointwise
input (`σ₀`). ∎

**A structural coincidence (EXACT; reading of DETECTOR_DENSITY).** The Sep 30 inner detector counts
rows with a zero right of `σ` as `≪ U^{f(σ)}`, `f(σ) = (31 − 32σ)/(21 − 12σ)`. If those rows are counted
with multiplicity in the sextic Kummer family (not checked here), the principal member's `U^{1/6}` rows
are excluded exactly when `f(σ) < 1/6`, i.e. `σ > 11/12` (sympy: `f = 1/6` at `11/12`; `f(7/8) = 2/7`,
`f(13/15) = 49/159`). Under multiplicity counting, both architectures therefore meet the leverage
wall at the same point. This is consistent with W4 and gives nothing below 11/12.

## 3. What survives: the κ-law (a minimal target)

Replace "diagonal size at `ρ < 1`" by a partial saving. Suppose that for some `η ∈ (0, 1)`

    (Κ_{η,κ})   Σ_{N u ≤ D^{1−η}} |A_u(D)|² ≪ D^{2 − (1−κ)η + ε}   for every smooth W.

Positivity from the Oct 5 range gives `κ = 1`, Prop. L below gives `κ = 5/6`, and Mom(1, 1−η) is
`κ = 0`. Extraction gives (sympy)

    σ(η, κ) = 11/12 − η (5/6 − κ)/2.

**Prop. L (lifting gives κ = 5/6 for free; PROPOSED, proof below, conditional on Oct 5
prop:ms, IMPORTED).** Assume the Oct 5 mean square as stated: for each fixed `ϑ ∈ (0, 1/10]` and smooth
`W`, `Σ_{0<N u ≤ x^{1+ϑ}} |A_u(x)|² ≪_{ϑ,W,ε} x^{2+ϑ+ε}` for all large `x`.
* (i) For every fixed `η ∈ (0, 6/11)` and `ε > 0`,

      Σ_{0 < N u ≤ x^{1−η}} |A_u(x)|² ≪_{η,ε,W} x^{2 − η/6 + ε},

  i.e. (Κ_{η, 5/6}). Extraction from it returns exactly 11/12.
* (ii) The same holds for every `η ∈ (0, 1)` under (Oct5⁺): the bound `≪ x^{1+ε}H` for **all**
  `H ≥ x^{1+ϑ}`. This is the natural all-`H` form; the manuscript states only `ϑ ≤ 1/10`.

*Proof.* Let `R = x^{1−η}`, fix a small `θ > 0`, and put `Y = (x^{1+θ}/R)^{1/6} = x^{(η+θ)/6}`. Let `𝒫` be
the `J ≍ Y/log Y` primary primes `p ∤ 6` with `Y/2 < N p ≤ Y`. The exact separation identity of
Prop. R′ step 3 (it uses only `μ(pm) = −μ(m)` and `χ_n(p⁶) = 1_{p∤n}`) gives, for every row `u` and
every `p`,

    A_u(x) = A_{up⁶}(x) − ν(p)ψ_u(p) A_{up⁶}(x/N p),     |ν(p)ψ_u(p)| = 1.

So `|A_u(x)|² ≤ 2|A_{up⁶}(x)|² + 2|A_{up⁶}(x/Np)|²`. Average over `p ∈ 𝒫` and sum over `N u ≤ R`.
* The rows `up⁶` have norm `≤ R Y⁶ = x^{1+θ}`, and each arises from `≪ x^{ε}` pairs `(u, p)` (divisor
  bound).
* First term: by Oct 5 at scale `x` with `ϑ = θ`, it is `≪ J^{−1} x^{2+θ+ε}`.
* Second term: the scales `x' ∈ [x/Y, 2x/Y]` satisfy `x^{1+θ} ≤ x'^{1+θ'}`, with
  `θ' = (1+θ)/(1 − (η+θ)/6) − 1 + o(1)`. For `η < 6/11` and `θ` small, `θ' ≤ 1/10`, so positivity and
  Oct 5 at scale `x'` with the fixed `ϑ = θ'` bound it by
  `≪ J^{−1} x'^{2+θ'+ε} = J^{−1} x^{2+θ−(η+θ)/6+o(1)}`, smaller than the first term.
  Under (Oct5⁺) the same bound holds for every `η < 1`.
* Total: `≪ x^{2+θ+ε}/Y = x^{2 + θ − (η+θ)/6 + ε}`. Since `θ` is arbitrary, this gives
  `x^{2−η/6+ε'}`. Extraction (W2) with `κ = 5/6` gives `σ(η, 5/6) = 11/12`. ∎

*Remarks.*
* Prop. L is strictly stronger than summing Prop. R′'s pointwise bounds `(N u)^{1/12} D^{11/12}` over
  the window, which gives `D^{3 − 7η/6}`.
* It is also stronger than positivity (`κ = 1`): the sub-diagonal mean squares are already
  nontrivial at 5/6-strength, *conditionally on Oct 5*. The excess over diagonal is at most
  `D^{5(1−ρ)/6}` at `ρ = 1 − η`, for `η < 6/11`.
* **Lifting is a fixed point** (exponent bookkeeping; the scale condition of (i) is assumed to hold
  at each step). Lifting from window `1 − η` into a window `1 − η'` that satisfies
  (Κ_{η', κ'}) gives the exponent `2 − (η − η')/6 − (1 − κ')η'`. At `κ' = 5/6` this is `2 − η/6` again.
  If some window had `κ₀ < 5/6` at `η₀`, lifting would propagate it: `κ(η) = 5/6 − (η₀/η)(5/6 − κ₀)`.
  The resulting boundary `11/12 − η₀(5/6 − κ₀)/2` is the same as the κ-law at `η₀` directly. So one
  window with `κ < 5/6` suffices, and the lifting machinery cannot manufacture it.

**Numerics on one window (EMPIRICAL, binary64; `kappa_window.py`, `kappa_window.json`; ~1 min).**
* Setup: `M_window / Diag_window` on `D^{1−η}/2 < N u ≤ D^{1−η}`, with
  `D ∈ {2000, 8000, 32000}` and `η ∈ {0.1, 0.2, 0.3, 0.5}`.
* μ gives 0.83–0.96. Three iid random-sign controls on the same columns give 0.84–1.01, and μ is
  inside their spread.
* The implied `κ̂ = log(M/Diag)/(η log D)` lies in `[−0.09, −0.02]`. It is negative only because
  the naive diagonal ignores coprimality.
* So in this finite range the window data are consistent with `κ ≈ 0`, far below 5/6. As everywhere
  in this folder, finite data are not evidence of provability; what is missing is a mechanism.

* **Any `κ < 5/6` at any `η > 0` beats 11/12.** One needs to save only a `1/6`-fraction of the
  sub-diagonal gap, not all of it.
* The imported 7/8 bound used pointwise gives `κ = 3/(4η)`. That is `< 5/6` only for `η > 9/10`,
  and then `σ = 31/24 − 5η/12 ≥ 7/8`: the import reproduces itself, nothing more.
* Every mechanism in the O5 triage that survives to a statement gives `κ ≥ 5/6` (positivity: 1;
  lifting, Prop. L: 5/6) or is equivalent to (Κ) (Poisson involution, Q_RHO_ANALYSIS). A proof of (Κ) with `κ < 5/6` still has to
  beat the single-row barrier of RUNG §3(a) at the conductor-graded level:
  `|A_w(D)| ≪ D^{1/2 + 5ρ/12 + ω/12}` for `N w = D^ω` (RUNG §4 item 2, heuristic extrapolation).
  At `ρ = 9/10` and `ω ≥ 0` this is *implied* by the 7/8 import. So the import already pays the
  small-conductor (pointwise) part of the 7/8-strength rung, and only the generic large-values part
  (RUNG §4 item 3) is missing. This is the sharpest form found here of "what is missing is a
  mechanism, not evidence".

## 4. Verdicts recorded

| scheme | verdict | killing term |
|---|---|---|
| reweighting row ranges | DEAD | mediant (W1) + `min_x` at `x = 1` (W2) |
| multi-scale large values (seed 3) | DEAD | `J ≪ D^ε` independent scales; coherence gain `J²` |
| hybrid `u × D`, `u × t` (seed 3) | DEAD | `1 − h/12 ≥ 11/12` on `h + τ = 1` |
| Größencharacter twists (seed 8) | DEAD | `c = 1 − 1/(6(1+τ))`; twist exponent `j` unchanged |
| cross-scale diagonal-free moment (N-a) | DEAD | principal part not sign-definite; Hermitian completion restores diagonals |
| Mellin-multiplier kernels | DEAD | same as changing `W` |
| pointwise 7/8 bootstrap (seed 2b) | DEAD | `σ₁ − σ₀ = (11/12 − σ₀)/k > 0` for `σ₀ < 11/12` |
| zero density with multiplicity (seed 6) | DEAD (circular) | `Q = 1` term: `H^{1/6} ≤ H^{A(1−σ)}` |
| κ-law (Κ) with `κ < 5/6` | OPEN target (κ = 5/6 PROPOSED via Prop. L) | coefficient-specific large values for generic rows; a restricted mean square on the thin lifted set |
