# The short-proof frontier: Part II with classical zero-density counts only

```text
Status: PROPOSED (model-based mechanism analysis). EXACT rational LP certificates for the stated
  linear barriers; FLOATING_RECONNAISSANCE Nelder-Mead confirmations. External manuscripts unreviewed.
Scope: the Part II (prime-slot) exponent architecture of [OAI], as transcribed in
  scripts/threshold_calculus.py, with every witnessed row count replaced by a count derived from a
  zero-density theorem for the FULL family of finite-order Hecke characters of Q(sqrt(-3))
  (Kintali-style). No statement about RH. No claim that [OAI] or [K] is correct.
Exact sources or dependencies:
  [OAI] OpenAI, "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8" (30 Sep 2026),
        TeX from `git show pr908:standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
        The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex` (PDF sha256 in
        scripts/SOURCES.txt): Lemma 8.1 (buffered bins), Prop. 9.2 (eq. sextic-row-count),
        Lemma 5.x (unmarked completed-row moment, eq. unmarked-completed-moment), Prop. 6.3 (balanced
        low estimate), Def. 10.1, Lemma 19.1 (bin prime bound), Lemma 20.1 (eq. common-high-exponent).
  [K]   Kintali, "A Short Proof of the Quasi-Riemann Hypothesis" (7 Oct 2026; sha256 in SOURCES.txt),
        eq. (16), Lemma 2, Sec. 4.3; as checked in reviews/KINTALI_REVIEW.md.
  [Hinz] J. Hinz, Acta Arith. 31 (1976) 167-193, Satz A and Satz B. Statements only, as recorded
        in reviews/KINTALI_REVIEW.md Sec. 1.2 (scan sha256 5349862b...). Proofs not read.
  Huxley-type exponents (constant 12/5; sigma-dependent 3/(3 sigma - 1)): NOT located as published
        theorems for Hecke characters of Q(sqrt(-3)) in the conductor aspect. Treated as hypothetical inputs.
  Repository: scripts/threshold_calculus.py, scripts/barrier_lp.py (imported, unmodified);
        THRESHOLD_CALCULUS.md, FLOOR_BIN_BARRIER.md.
What was actually run: scripts/short_proof_frontier.py (new):
  `lp`    - exact LP with rational dual certificates and rational primal points, 9 count inputs,
            uncapped / capped (M + ell <= 1) / optimal energy;
  `check` - full threshold_calculus model at every LP optimum (241 bins x 26 amplitudes x 19 dyads,
            plus the exact kink bin, beta_prev = 1);
  `run`   - Nelder-Mead over (lx, ly, ell) for every scenario, 7 starts each, about 15-30 s per run.
  Results are in results/SPF_*.json. All runs used nice -n 10 and at most 2 processes.
Smallest remaining gap: the frontier value 29/31 (Hinz) sits at lx = ly = 16/31 > 1/2, ell = 0. It
  needs the Part I high-expansion specializations ([OAI] Sec. 10.5-11, [K] Sec. 4) re-run at
  h = 15/31, plus [OAI] Lemma 5.x at row exponent 32/31 (stated for general bounded M, but not
  specialized there). Neither was checked. Inside the manuscript's own range M + ell <= 1 the
  value is 29/30, which is exactly Kintali's.
```

RH is not touched here. Every number below is the boundary that one external, unreviewed proof
architecture would deliver if its lemmas' stated output exponents hold at the indicated geometry.

## 0. Answer

**Classical counts cannot take the Part II architecture below 11/12.** With full-family density
exponent `A`, the frontier is

| input (full Hecke family, `N << (Q^2T^2)^{A(1-σ)}`) | published? | crossing `a*` | `σ0`, `M+ℓ` free (exact) | geometry `(lx, ly, ℓ)` | `σ0`, `M+ℓ ≤ 1` (exact) |
|---|---|---|---|---|---|
| Hinz, [K]'s linear form `R = min(1, 5(1−a))`, `A = 5/2` | yes (Hinz 1976) | 4/5 | **29/31 ≈ 0.935484** | (16/31, 16/31, 0) | 29/30 ≈ 0.966667 |
| Hinz exact, `min(3/(2−σ), 2/σ)` (Satz A alone gives the same) | yes | 4/5 | 29/31 | (16/31, 16/31, 0) | 29/30 |
| Huxley-type constant `A = 12/5` | not for this family | 19/24 | 69/74 ≈ 0.932432 | (19/37, 19/37, 0) | 23/24 ≈ 0.958333 |
| `A = 7/3` | hypothetical | 11/14 | 40/43 ≈ 0.930233 | (22/43, 22/43, 0) | 20/21 ≈ 0.952381 |
| `A = 9/4`; also σ-dependent Huxley shape `3/(3σ−1)`, σ ≥ 3/4 | hypothetical | 7/9 | 51/55 ≈ 0.927273 | (28/55, 28/55, 0) | 17/18 ≈ 0.944444 |
| `A = 2`: density hypothesis for the full family | conjectural | 3/4 | **11/12** | (1/2, 1/2, 0) | 11/12 |
| `A = 3/2` (beyond full-family DH) | hypothetical | 2/3 | 19/21 ≈ 0.904762 | (10/21, 10/21, 1/21) | 19/21 |
| `A = 18/17` at σ = 19/36 | hypothetical | 19/36 | **7/8** | (5/12, 5/12, 1/6) | 7/8 |
| `A = 1` (= threshold_calculus `counts='DH'`) | hypothetical | 1/2 | 167/192 ≈ 0.869792 (floor bin) | (13/32, 13/32, 3/16) | 167/192 |

In closed form (`a* = 1 − 1/(2A)` for constant `A`):

* **`A ≥ 2`, `M + ℓ` free:** `σ0 = (1 + 6a*)/(3 + 4a*) = (7A − 3)/(7A − 2)`, at `lx = ly = (4A − 2)/(7A − 2)`, `ℓ = 0`.
* **`A ≥ 2`, `M + ℓ ≤ 1`:** `σ0 = a* + 1/6 = 7/6 − 1/(2A)`. This is exactly [K]'s formula: the prime slots buy nothing.
* **`A ≤ 2`:** `σ0 = (36a* − 5)/(36a* − 3) = (31A − 18)/(33A − 18)`, at `ℓ = (1−2δ*)/(5+6δ*)`, `lx = ly = (1−ℓ)/2`, `M + ℓ = 1`. Here `δ* = 2a* − 1`. Once `a* ≤ 51/100` the value floors at `167/192`.

Every entry was matched against an exact LP certificate (Section 3), and every entry except the
`7/8` row was also matched by the full model.

**Verdict.**

1. **Hinz.** "Part II + Hinz" gives `29/31 ≈ 0.9355`. That beats [K]'s `29/30` only through a
   change of probe lengths, which stays to be checked. It is `15/248 ≈ 0.060` above `7/8`.
2. **Other classical inputs.** No full-family density input that is known, or even conjectured
   short of something beyond DH, gets below `11/12`. DH for the full Hecke family gives exactly
   `11/12`.
3. **Reaching `7/8`.** That needs `N(σ) << Q^{1+ε}` for the `≈ Q²`-member family already at
   `σ ≥ 19/36`, i.e. "`A = 18/17`" there. That is far beyond DH, which gives `Q^{17/9}` at that `σ`.
4. **Prime slots.** At the frontier the optimal slot length is `ℓ* = 0` for every `A ≥ 2`. The
   "short Part II" therefore collapses to a Part I probe with rebalanced scales `X = Y = Z^{16/31}`.

## 1. Dictionary: model `R(δ, x, κ, S)` ↔ Kintali's `R(a)` (task 1)

**What the model's `R` is.**

* **Bins** ([OAI] Lemma 8.1). Every retained row `u` (sixth-power-free, `q_u ≍ U = Z^d`) gets a
  bin `(i, a)` on the grid `51/100 + eZ`, and `δ = 2a − 1`. If `a > 51/100`, some presentation
  `ψ ∈ X_u` (`ψ(n) = ν(n)χ_n(u)^ς`, `ν ∈ Θ`) has a zero of its primitive inducing `L`-function
  with `a ≤ Re ρ < a + e` and `|Im ρ| ≤ 3iT_1`.
* **Counts** ([OAI] Prop. 9.2). For any set `B` of rows in one bin,
  `#B << U^{R(δ)+ε}(1+T_1)^{A_A}`. The floor bin has the elementary count `#B << U`.
* **High side** ([OAI] Lemma 20.1). It consumes exactly such counts, `#C << U^{R+ε}(1+T_1)^{A_A}`,
  for any pointwise set `C` with slot-amplitude mean `q ∈ [0, δ/2]`. It feeds them into
  `F = a − β* + h(z0 − 1/6) − a·ly − ℓ/2 + qℓ + d(R + δ/2 − z0)` (eq. common-high-exponent).

So `R` is the exponent of the number of rows with norm `≍ U` and a zero right of `a`, relative to
the trivial count `U`. The extra arguments `(x, κ, S)` record how the manuscript produces `R`:
* `x`: amplitude `q = xδ`;
* `κ`: Lemma 18.1 capacity;
* `S = ℓ/d`: prime supply.

A classical count needs none of them.

**Kintali's `R(a)`** ([K] (16)) is the same object. The model at Part I geometry `(1/2, 1/2, 0)` gives

    F = a − β* + (1/2)(17/50 − 1/6) − a/2 + d(R + a − 1/2 − 17/50) = a/2 − β* + 13/150 + d(R + a − 21/25),

which is [K]'s `E(d, a)` verbatim. Hence `R_model(δ) = R_K((1+δ)/2)`.

**From a density theorem to `R`.**

* A row in a non-floor bin owns a zero of a primitive finite-order Hecke character `ψ*`, with
  conductor norm `<< U` and `Re ρ ≥ a`.
* Only `O(1)` rows map to one `ψ*` ([K] Lemma 2, checked in KINTALI_REVIEW.md Sec. 2; `Θ` is finite).
* A density theorem for the full family `{χ : Nq ≤ Q}` with `Q ≍ U` therefore gives

      R_A(a) = min(1, 2A(σ=a)·(1 − a)) = min(1, A(1 − δ))   (constant A).

* The height factor `(T_1²)^{A(1−a)}` is a fixed power of `T_1 = Z^τ`. It is absorbed in
  `(1+T_1)^{A_A}`, which Lemma 20.1 allows "fixed before τ".
* Hinz's implied constants depend only on `K`, so the count is uniform in bins, dyads and targets.

**Normalization warning.** The full family has `≈ U²` members; the rows are a sparse subfamily of
`≈ U`. threshold_calculus's `counts='DH'` (`R = 1 − δ = 2(1 − a)`) is DH for the row family, which
is **`A = 1`** in the full-family normalization. DH for the full Hecke family is `A = 2`, i.e.
`R = min(1, 4(1 − a))`, trivial for `a ≤ 3/4`. The model's 0.8698 "DH" value is thus far stronger
than any full-family density statement.

For comparison, the manuscript's own Part I count is non-classical. It is the row-family sextic
large sieve, Prop. 9.2:

    R(a) = min(1, max(3/2 − a, 7/3 − 2a)).

| `a` | Prop. 9.2 | Hinz | row-family DH |
|---|---|---|---|
| 2/3 | 1 | 1 | 2/3 |
| 3/4 | 5/6 | 1 | 1/2 |
| 4/5 | 11/15 | 1 | 2/5 |
| 7/8 | 5/8 | 5/8 | 1/4 |
| 9/10 | 3/5 | 1/2 | 1/5 |

Prop. 9.2 is already non-trivial on `(2/3, 3/4]`, where every full-family estimate up to DH is
trivial. Hinz overtakes it only for `a > 7/8`.

## 2. Why the frontier depends only on the crossing `a*`

The input `R_A(a) = min(1, 2A(a)(1 − a))` equals `1` up to the crossing `a*`, defined by
`2A(a*)(1 − a*) = 1`.

* **Hinz** (either form, or Satz A alone): `a* = 4/5`.
* **Full-family DH:** `a* = 3/4`.

Every bin with `51/100 < a < a*` is counted trivially, exactly like the floor bin. With `R = 1` and
worst amplitude `q = δ/2`, `F` at the top dyad `d = h` increases in `a`. Beyond `a*`, `F` decreases,
because `R` falls with slope `−2A < −1/2·(1 − ly + ℓ)/h`. So the binding object is the bin at `a*`:

    (H_a*)  σ0 ≥ a*(1 − ly) + h(5/6 + δ*/2) − ℓ/2 + δ*ℓ/2,   h = 1 − lx + ℓ,  δ* = 2a* − 1.

This is the floor-bin constraint of FLOOR_BIN_BARRIER.md with the floor moved from `51/100` to
`a*`. **A classical count acts as an effective detector floor at `a*`.** Two consequences:

1. **No cost to raising the floor.** One may put the detector floor of Lemma 8.1 at `a*` instead of
   `51/100`; the LP value does not change (checked).
2. **Low side.** Adjoin (H_a*) to the low-side rows of THRESHOLD_CALCULUS.md Sec. 2. For
   `ℓ ≥ 0`, `lx ≤ ly`:

       (L1) σ0 ≥ 5/6 + (lx+ly)/12 − ℓ/6           [E = M]
       (L3) σ0 ≥ 1/3 + 7(lx+ly)/12 + ℓ/3          [E = 2M + ℓ − 1]

   (H_a*) has a positive `ℓ`-coefficient `c − 1/2 + δ*/2` (with `c = 5/6 + δ*/2`), even with `q = 0`.

What follows depends on which side of `3/4` the crossing lies:

* **`a* ≥ 3/4`.** (L1) and (L3) can tie only on `M + ℓ = 1`, where (H_a*) exceeds them. The LP
  instead takes `ℓ = 0` and `lx = ly = L > 1/2`, balancing (H_a*) against (L3).
  * Hinz certificate:
    `(58/93)·(L3) + (35/93)·(H_{4/5})` gives `σ0 ≥ 29/31 + (35/558)(ly − lx) + (52/93)ℓ ≥ 29/31`.
  * Adding the manuscript's hypothesis `M + ℓ ≤ 1` (Lemma 15.1) pins `(1/2, 1/2, 0)`:
    `(H_{4/5}) + (29/30)·(cap) + (19/10)·(ℓ ≥ 0) + (1/6)·(lx ≤ ly)` gives `29/30`.
* **`a* < 3/4`.** All three rows tie on `M + ℓ = 1` with `ℓ > 0`. This is the
  `(13 − 18τ)/(15 − 18τ)` law of FLOOR_BIN_BARRIER.md Sec. 1.5 with `τ = −δ*`.
  * 7/8 certificate:
    `(11/16)(L1) + (1/8)(L3) + (3/16)(H_{19/36}) + (1/32)(lx ≤ ly)`.

In [K]'s language, the uncapped comparison is a one-parameter extension of [K]'s inequality.
[K]'s `max_a [a + R(a)/2 − 1/3]` is the `L = 1/2` case of

    σ0(L) = max{ low(L), (1 − L)·max_a [2a + R(a) − 2/3] },
    low(L) = 1/3 + 7L/6  (L ≥ 1/2),

minimized at `L = (4A − 2)/(7A − 2)`.

## 3. What was run, and the results

`scripts/short_proof_frontier.py` imports threshold_calculus and barrier_lp without modifying them.

* It subclasses `Inputs` as `DensityInputs(Afun, label)`.
* It wraps `threshold_calculus.R_bin` at runtime. Every counts mode it does not own falls through
  to the original.
* Counts: floor bin trivial; other bins `R = min(1, 2A(a)(1 − a))`.

**Exact LP (`lp`).** The rows are:
* the three low-side branches (`barrier_lp.low_rows`);
* validity and small rows;
* the floor;
* the crossing bin;
* descending-branch bins on a `1/400` grid up to `a = 13/15 ≤ σ0`;
* optionally the cap.

Certificates are rational duals, checked in `Fraction`s, together with rationalized primal points
checked against every row. All 9 inputs reproduce the closed forms of Section 0 exactly, both with
and without the cap. With `energy='optimal'` (large-sieve diagonal only) the values are identical.

**Full model at the LP optima (`check`).** This uses 241 bins × 26 amplitudes × 19 dyads plus the
kink bin, with `β_prev = 1`.

* Uncapped: `σ0_low` equals the LP value to `10^{-12}`. `sup F ∈ [−3·10^{-4}, 0]`, attained at the
  kink bin `δ*`, `d = h`. The nonzero values are grid offsets; `F = 0` exactly at `δ*`.
* Capped: `σ0_low = 11/12` and `sup F = +1/20` (Hinz), i.e. boundary `11/12 + 1/20 = 29/30`.

**Nelder–Mead (`run`).** These use `β_prev = 1`: no a priori zero-free region, so nothing from
[OAI] Part I is used.

| scenario | model `σ0` | LP | geometry found |
|---|---|---|---|
| hinz_linear / hinz_exact | 0.935516 | 29/31 = 0.935484 | (0.5161, 0.5161, 4e-5) |
| huxley_12_5 | 0.932464 | 69/74 = 0.932432 | (0.5135, 0.5135, 4e-5) |
| A_7_3 | 0.930265 | 40/43 = 0.930233 | (0.5116, 0.5116, 4e-5) |
| A_9_4 / huxley_sigma | 0.927305 | 51/55 = 0.927273 | (0.5091, 0.5091, 4e-5) |
| A_2_DH | 0.916698 | 11/12 = 0.916667 | (0.5000, 0.5000, 4e-5) |
| A_3_2 | 0.904765 | 19/21 = 0.904762 | (0.4762, 0.4762, 0.0476) |
| hinz_linear, optimal energy | 0.935516 | 29/31 | same |
| hinz_linear, effective objective | 0.935492 | 29/31 | (0.5161, 0.5161, 0) |
| hinz (both forms), cap `M+ℓ≤1`, effective objective | 0.966667 | 29/30 | (1/2, 1/2, 0) |
| huxley_sigma, cap, effective objective | 0.944444 | 17/18 | (1/2, 1/2, 0) |

The `+3·10^{-5}` offsets are the optimizer's `2·10^{-5}` penalty slack.

**Two pitfalls, fixed in the script.**

1. **The δ-grid misses the kink.** threshold_calculus's coarse `δ`-grid (41 points) misses the kink
   at `δ*`. A first Hinz run "found" 0.93335 at a geometry where the fine check gave
   `sup F = +5.7·10^{-3}`, i.e. it did not close. `high_sup_kink` adds the kink bin.
2. **The penalty objective fails under the cap.** `optimise`'s penalty objective presumes the low
   side sets `σ0`. Under the cap the high side binds above it, so the objective fails. Mode `eff`
   minimizes `σ0_low + max(0, sup F)` and re-verifies at that `σ0`.

## 4. The energy input: what was assumed

The low side is the manuscript's, `energy='paper'`. That is the closed form of the supremum of
[OAI] (14.14),

    E_B = max(M′, (2M′+1+3ℓ′)/4, 2M′+ℓ′−1),

with the Lemma 15.1 hypothesis `M + ℓ = 1` lifted by the LP-verified third branch, plus the
Prop. 15.2 Gram bound (THRESHOLD_CALCULUS.md Sec. 2). No other energy change was assumed.

At every classical frontier point (`A ≥ 2`) only the branch `E = 2M − 1` binds, together with
`E = M` at `A = 2`. The reflected-kernel branch `(2M+1+3ℓ)/4` of Lemma 14.3 never binds, so
`energy='optimal'` gives the same values. At `ℓ = 0` these two branches are exactly the
manuscript's **Part I** bound:

* [OAI] Lemma 5.x (unmarked completed-row moment) gives
  `Σ_{q_m ≤ Z^M} |C_V(Z^N; m)|² << Z^{O/2 + max(M−O, 2M−O−N)+ε}`. It is stated for bounded ranges
  of `M ≥ 0`, `N`, and its worst dyad is `O = 0`.
* It is paired with the additive norm `(Q + Y²)/Y ≤ 2Q/Y` of Prop. 6.3's proof.
* With `X = Y = Z^L` and `N = 1` this gives `|I_η| << Z^{(3L−1)/2+ε}` for `L ≥ 1/2`, hence
  `σ0_low = 1/3 + 7L/6`. That is the model's (L3).

So the frontier assumes **no new energy input**: only Prop. 6.3's proof re-run at `X = Y = Z^{16/31}`.

[K]'s "short energy argument" (Lemma 4, with the large sieve (14)) is the `L = 1/2` instance of
this pairing. Whether [K]'s own short proof extends to `L = 16/31` was not checked. [OAI]'s
Lemma 5.x does, as stated.

## 5. Which Part II lemmas are still needed (task 3)

At the classical frontier, `ℓ* = 0` for every `A ≥ 2`, even if the slot amplitude were free
(`q = 0`; LP checked). (H_a*) and (L3) both increase in `ℓ`. Therefore:

| [OAI] Part II component | needed with classical counts? |
|---|---|
| Sec. 12–14 compensated probe, marked completion, whole-index prime-slot reflection, Lemma 14.3 | **No** (`ℓ = 0`); replaced by the Part I unmarked moment (Lemma 5.x) at row exponent `2L` |
| Sec. 15 compensated low estimate (Lemma 15.1, Prop. 15.2 Gram, Prop. 15.3 tuples) | **No**; Prop. 6.3's proof at `X = Y = Z^L` |
| Sec. 16 local compensation, dynamic local errors | **No**; Part I scalar Euler identity (Sec. 7) suffices |
| Sec. 17 inverse moment with prime factors, Lemma 17.6 amplification | **No** |
| Sec. 18 Lemma 18.1 (fourth moment with short prime factors; `κ ≥ 3/4` range) | **No**; and no a priori `β* ≤ 11/12` is needed (`β_prev = 1`) |
| Sec. 19.1 Lemma 19.1 (prime bound in a bin, `q ≤ δ/2`) | **No** at `ℓ = 0` (needed only if `ℓ > 0`, worst `q = δ/2` suffices) |
| Sec. 19.2 selected slots, Prop. 19.2 row counts; Sec. 8.2 saturated witnesses; Sec. 9 sextic large sieve | **No**; replaced by Hinz 1976 Satz A + [K] Lemma 2 |
| Lemma 8.1 buffered bins | **Yes**, but the floor may sit at `a* = 4/5` at no cost |
| Euler local factors (7.14)/(7.15), regions `D_1`, `D_2` | **Yes, simplified.** With the floor at `a*`, `D_1` is needed only for `Re s ≥ a* + O(e)` instead of `51/100`; `D_2` (`Re s ≥ 7/8`) contains the frontier `29/31` |
| Def. 10.1, Lemmas 10.3–10.4 (stated for general `lx, ly, ℓ`) | **Yes**, as stated |
| Part I specializations: principal row, row envelope at `d = h`, small/large rows (Sec. 10.5–11) | **Yes, re-run at `h = 15/31`**: the main unchecked obligation |
| Probe identities and cubic-theta reflection ([OAI] Sec. 4–7, Prop. 5.1; [K] Sec. 2, Lemma 3, App. A–B) | **Yes**: shared, unverified core (KINTALI_REVIEW.md Sec. 5) |

If a beyond-DH full-family input were available (`a* < 3/4`), `ℓ* > 0` and the following return:
* Sec. 12–16;
* Lemma 19.1, used with the worst amplitude.

Lemmas 17–18 and Prop. 19.2 would still be unnecessary.

## 6. Verdict, and the remaining non-classical inputs

1. **Frontier.** `σ0(A) = (7A − 3)/(7A − 2)` for `A ≥ 2`:
   * Hinz `29/31`;
   * Huxley-type `69/74`;
   * `7/3` gives `40/43`;
   * `9/4` gives `51/55`;
   * DH gives `11/12`.

   Within the manuscript's `M + ℓ ≤ 1`, the frontier is [K]'s `7/6 − 1/(2A)`. **None is below
   11/12.** Prime slots never help with classical counts.
2. **Why 11/12 is a wall for full-family inputs.** The rows are `≈ U` of `≈ U²` characters, so a
   full-family count drops below the trivial `U` only where `N(σ) ≤ Q`. That needs `σ ≥ 3/4` under
   DH. Rows with rightmost zero in `[51/100, 3/4)` are then counted trivially, and that effective
   floor alone forces `σ0 ≥ 11/12` (Section 2).
3. **Distance to 7/8.** Hinz is `15/248 ≈ 0.060` above. Even DH is `1/24` above. Reaching `7/8`
   needs `N(σ) << Q^{1+ε}` for `σ ≥ 19/36` (`A = 18/17` there).
4. **What carries Part II below 11/12.** It is the **row-family** counts: the sextic large sieve
   restricted to the sparse row family (Sec. 8.2, 9), refined by the slot moments (Sec. 17–19).
   These are exactly the non-classical inputs a short proof would remove.
5. **Non-classical inputs remaining in "Part II + Hinz".** At `29/31` (or `29/30` capped):
   * the probe and its two exact representations;
   * the cubic-theta weak reflection;
   * [OAI] Lemma 5.x at row exponent `32/31`;
   * the Part I high-expansion specializations at `h = 15/31`.

   The density input itself is classical (Hinz Satz A; Satz B is not load-bearing, since it gives
   the same `a* = 4/5`).
6. **A by-product, PROPOSED and unverified.** [K]'s own `29/30` would improve to `29/31` by taking
   `X = Y = Z^{16/31}` instead of `Z^{1/2}`. The conditions are exactly the two "re-run"
   obligations above.

**Known misreadings to avoid.**

* threshold_calculus's `counts='DH'` is not "the density hypothesis" in [K]'s sense (Section 1).
* `29/31` is not a theorem. It is the model value under transcribed lemma exponents at an
  unspecialized geometry.
* The `A ≤ 2` rows are hypothetical inputs, not results.

## 7. Reproduction

```text
cd research/exploratory/qrh-2026-10/scripts
python3 -I short_proof_frontier.py lp                       # exact LP table, certificates (~2 s); writes ../results/SPF_lp.json
python3 -I short_proof_frontier.py check                    # full model at LP optima (~2 min)
python3 -I short_proof_frontier.py run hinz_linear          # Nelder-Mead (~20 s); also: hinz_exact huxley_12_5 huxley_sigma A_7_3 A_9_4 A_2_DH A_3_2
python3 -I short_proof_frontier.py run hinz_linear optE     # optimal (large-sieve diagonal) energy
python3 -I short_proof_frontier.py run hinz_linear cap1 eff # manuscript range M + ell <= 1, effective-boundary objective
```
