# O3b: numerical and structural test of the non-alignment statement (NA)

```text
Status: EXPLORATION, OFFENSE/EXPERIMENTAL. Round 2 (Section 8) supersedes the round-1 verdict.
  The round-1 "falsifying pattern" (principal-row alignment, Sections 0, 5.1-5.2, 6-7) is an
  ARTIFACT of the toy row weight exp(-x^2). With [S30]'s log-Gaussian W_G it disappears: R_exc sits
  at the noise floor (Q = 256, 1024, 4096). Only the mu -> 1 control shows a residue, with
  signal/noise 2.4, 3.6, 7.1: the Moebius signature.
  Round-2 verdict (PROPOSED): the main term of <A^exc, B> is the target signal c_S A_eta f_eta itself
  (same eta, same s). It DOES NOT CANCEL usefully: subtracting it from both sides empties the
  contradiction, so (NA') gives no sigma0, and (NA) is circular. No half-plane below 7/8 is obtained.
  Labels: PROVED-HERE, EMPIRICAL (floating point, finite), HEURISTIC, PROPOSED, OPEN.
  RH and every quasi-RH half-plane remain unproved.
Scope: (NA) of ../O3_SEP30_X_OCT5/README.md Section 2.3: a Z^{b/12} saving beyond Cauchy-Schwarz in
  the pairing of the exceptional (sextic Patterson-bias) component A^exc of the additive polynomial
  A_m with the completed cubic-theta row B_m of [S30] eq:low-separated. Tested in a small toy model M0
  of A_m and B_m over Z[omega] (Section 2), with ball sizes Q = 256 ... 8192, Z = Q^1.15, and column
  norms up to 8*10^4. Not tested: the marked rows B^J with slot primes (J^c nonempty), the ray-class
  restriction s in sigma, eta != 1, the n > 1 (cube) part of the row, v != 0.
Exact sources or dependencies: [S30] = OpenAI "Quasi-RH ... 7/8" (30 Sep 2026), external and
  unreviewed, scratchpad/paper_sep30.tex. Used: eq:general-probe (l. 3440), eq:low-separated (l. 3485),
  eq:signal (l. 965), Lemma 15.1 (l. 8111), B^J (l. 8073-8107), Prop. 15.2 and its proof
  (l. 8340-8557). ../O3_SEP30_X_OCT5/README.md (Props. O3.1-O3.2, Sections 2.2-2.3).
  ../../SEXTIC_THETA_S6.md (sextic residue A_1 ~ 0.22 at norm <= 3e5). Gauss-sum conventions follow
  ../../a2/eis.py and ../../a2/s6_gauss.c (read, not modified; eis.py imported read-only by
  scripts/validate.py).
What was actually run (single-threaded numpy, about 35 CPU-minutes in total; no run over 6.5 minutes):
  scripts/validate.py: the toy's Gauss sums and characters against eis.py brute force. 216 Gauss
    sums and the residue symbols agree to 1e-8. Identity O3.1 holds to 1e-15.
  scripts/na_run.py Q: the annulus grid, with P_a = 1 ... 1024, 24 random baselines each.
    Output: results/na_Q{256,1024,4096}.json.
  scripts/na_kubota.py Q 80000: the Kubota-residue test (OP-K) with 5 variants of B.
    Output: results/kub_Q{256,1024,4096,8192}.json. With CMIN_FRAC=0.25 it uses only rows of
    norm >= Z/4: results/kubhi_Q{1024,4096}.json.
  scripts/diag_c.py Q 80000: alignment row by row. Output: results/diagc_Q{256,1024,4096,8192}.json.
  scripts/analyze.py writes the tables to results/analysis.md and results/fits.json.
  Round 2: VMODE=loggauss scripts/na_kubota.py Q 80000 with CMAX = 80000 (Q = 256, 1024) and
    160000 (Q = 4096). Output: results/kublg_Q*.json.
Smallest remaining gap (round 2): a low-side bound for the signal-carrying pairing <A^exc, B> that
  neither goes through ||A^exc|| (Cauchy-Schwarz, the source of the Z^{b/12} loss) nor uses the size
  of f_eta (circular). It is OPEN and no candidate was found (Section 8.3). (NA) is circular; (NA')
  is vacuous for the contradiction.
```

> **Round-2 correction (about 00:50 UTC).** Sections 0, 5.1, 5.2, 6 and 7 below are the round-1 text and
> are kept for the record. Their principal-row (`c = 1`) alignment and their `1/L(1, ψη)` reading come
> from the M0 row weight `V = e^{−x²}`. [S30]'s row weight is `W_G(q_A/Z) = (2√π)^{−1}e^{−(log(q_A/Z))²/4}`,
> under which the `c = 1` row is super-polynomially small. Read Section 8 for the corrected numerics
> and the cancellation analysis.

RH remains unproved. [S30] is an external, unreviewed import. Nothing here moves the imported
best value `σ0 = 0.874957…`.

## 0. Bottom line

* **Answer to the coordinator's question (a). PROVED-HERE from imported identities.** In the
  bilinear pairing of eq:low-separated, the `m`-character of the pair `(s, a = c n³)` is
  `ξ(m)·conj χ_s(−m)·χ_a(m)`. It is principal off `S` exactly when `a = s t⁶`.
  * On that diagonal the coefficient is `γ₁(s)γ₂(s)·conj α(s)·…`. By eq:signal,
    `γ₁γ₂ = μαG`, so this is `μ(s)G(s)·…`.
  * The row's own correction `conj G(a)` then removes `G(s)`. What remains is **`μ(s)` times a
    fixed finite-order ray/target character**: a Möbius sum, **not** `G·γ₂`.
  * **But in the paper's pairing that diagonal is identically zero.** The reason is `ξ(−1) = −1`
    (forced, since `ξ` is nonprincipal at `λ`, where the residue field is `F₃`) and the evenness of
    every other `m`-weight (Prop. O3b.1). Numerically the diagonal is `≤ 3·10⁻¹⁹·‖A‖‖B‖`.
  * The Möbius structure reappears in the Poisson dual, as the principal row (§6).
* **Numerics. EMPIRICAL, floating point, finite.**
  * The exceptional (Kubota) component of `A` is invisible in single annuli at feasible sizes. The
    Gram excess is `|·| ≤ 0.08` and there are no outlier eigenvalues. It is clearly visible in
    cumulative column sums: `G/G_diag − 1` reaches `0.9–1.4` at `N(s) ≤ 8·10⁴`, while random
    column phases stay within `±0.09`.
  * Measured this way, `A^exc` **is aligned with B**:
    `R_exc ≈ 0.179, 0.155, 0.152, 0.142` at `Q = 256, 1024, 4096, 8192`. The noise floors are
    `0.028, 0.016, 0.009, 0.007`, and the random-`m`-phase baseline is `0.089, 0.027, 0.006, 0.008`.
  * **The alignment sits in B's principal row `c = 1`.** Its normalized overlap with `A^exc` is
    `r₁ = 0.240, 0.259, 0.261, 0.254` at `Q = 256, 1024, 4096, 8192`, flat in `Q`.
    * Rows of norm `≥ 512` are at the random level `≈ #m^{−1/2}`.
    * A handful of small rows (`N(c) = 13 … 73`) carry `r ≈ 0.03–0.054`, decaying roughly like
      `r₁N(c)^{−1/2}`.
  * With only rows of norm `≥ Z/4`, `R_exc` drops to the noise floor.
  * **`R_exc·(log Z)^{1/2}` is constant**: `0.451, 0.437, 0.469, 0.458`. This matches
    `R_exc ≈ r₁/(‖B‖/‖1‖)` with `‖B‖²/‖1‖² ≈ 0.3·log Z`.
* **Verdict.**
  * (NA) needs `R_exc ≪ P_a^{−1/12}Z^ε`, a **power** saving. The data show a persistent alignment of
    `A^exc` with the principal row. The `Q`-dependence of `R_exc` is entirely accounted for by
    `‖B‖ ∝ (log Z)^{1/2}`. In the tested range this is the **falsifying pattern** (EMPIRICAL).
  * Honest caveats:
    * In absolute terms at `Q ≤ 8192`, `R_exc ≤ 0.18` is **below** the paper-geometry threshold
      `P_a^{−1/12} ≈ 0.78–0.86`.
    * A pure power fit, `R_exc ∝ Q^{−0.059±0.013}`, is steeper than the `Q^{−0.028}` that (NA)
      needs. Taken alone it would read as support.
    * The falsifying conclusion therefore rests on the decomposition `R_exc ≈ r₁·‖1‖/‖B‖`.
      `r₁` is flat (fitted slope `+0.018`), and the only decay comes from `‖B‖² ≈ 0.3‖1‖²·log Z`,
      a property of how B is built. Then `|⟨A^exc, B⟩| ≈ r₁‖A^exc‖‖1‖` exceeds the (NA) bound
      `‖A^exc‖‖B‖P_a^{−1/12}Z^ε` by `≍ r₁P_a^{1/12}/(log Z)^{1/2} → ∞` (HEURISTIC extrapolation).
  * The arithmetic coefficients do not matter. `θ(c) = μ(c) conj γ₂(c)²`, `μ → 1`, `μ → ±1` and
    `θ →` random phases all give the same `R_exc` to within 25 %. As the coordinator predicted,
    numerics cannot see the Möbius cancellation.
* **Structural reading (PROPOSED, §6).** The principal-row alignment is the leading term of the
  probe's own principal-row main term:
  `⟨A^exc, B⟩ ≈ (Kubota mass)·Σ_a μ(a)ψ(a)N(a)^{−1}V(N a/Z) ≈ (Kubota mass)/L(1, ψ)`, with `ψ` of
  finite order (ray × target `η`), consistent with O3 §2.2 ("signal ∝ exceptional mean").
  * The measured row profile `r_c ≈ r₁N(c)^{−1/2}`, i.e. a contribution `∝ N(c)^{−1}`, fits this.
  * Then (NA) would require `|1/L(1, ψη)| ≪ Z^{−b/12}`. That is **false** for a fixed target, since
    `L(1,·) ≍ 1`.
  * So (NA) is not merely circular. Its main term is the probe's own principal-row term, which is
    not small. Under a hypothetical zero the row is larger still, and bounding it is exactly the
    zero-free information sought. **Coordinator (c): (NA) is not a non-circular input.**
* **"Different covers" is not an obstruction. PROVED-HERE identity; PROPOSED conclusion.** Using
  eq:signal, `θ(c) = γ₂ conj α = μ(c)·G(c)·conj γ₁(c)`. Hence
  `B_m = conj Σ_c μ(c)ψ′(c)·q_c^{−1/2} g_{χ_c}(c, m)·V(q_c/Z)`, where `ψ′ = conj G·Ξ` is a fixed
  finite-order ray function (`Ξ = ξ·χ_•(b_*)`, §3).
  * That is a **Möbius-weighted sextic** Gauss-sum series. `A^exc` and `B` live on the **same**
    6-fold cover, so there is no central-character mismatch to exploit.

## 1. The statement under test and its normalization

From O3 §2.3, for fixed tuple and `|v| ≪ Z^ε`:

    (NA)   Q^{−1/2} |Σ_{m≠0} Ω(q_m/Q) ξ(m) (q_m/Q)^{−iv} A^exc_m B_m| ≪ Z^{l_x/2 − d/2 + ε}.

Cauchy–Schwarz with Lemma 15.1 (`‖B‖² ≪ Q Z^ε`) and the exceptional part of Prop. 15.2
(`‖A^exc‖² ≍ (Q/Y′)P_a^{1/6}`) gives the right side times `P_a^{1/12} = Z^{b/12}`. So, with
`R_exc = |⟨A^exc, B⟩_{Ωξ}| / (‖A^exc‖_Ω ‖B‖_Ω)`:

    (NA)  ⇔  R_exc ≪ P_a^{−1/12} Z^ε   (a fixed power saving, uniformly in the tuple).

At the paper geometry, `Q = Z^{M′}` with `M′ ≈ 0.87` and `b ≈ 0.29`, the target is
`R_exc ≪ Q^{−0.028}`. Any decay slower than every power, e.g. `(log Z)^{−1/2}`, violates (NA).

## 2. Toy model M0 (exact definitions; every simplification listed)

| [S30] object | M0 | change |
|---|---|---|
| ring, primary elements, `χ_n(u) = (u/n)₆`, `e(z)`, `γ_j` | as `a2/eis.py` (Oct 5 / Sep 30 conventions) | none (validated against brute force) |
| `S`, `b_*`, `ξ` | `S = {2, λ}`, `b_* = 2λ`; `ξ = ξ_λ·ξ_2`, quadratic mod `λ` × cubic mod 2, order 6, nonprincipal at both | none in kind (`P_0` small) |
| `m`-range, `Ω` | all `m ≠ 0` in `O`, `q_m ≤ Q`, `Ω = (1 − q_m/Q)³₊` | `Ω` is `C²`, not `C^∞` |
| `A_{m,σ,v}(Y′)` | `Y′^{−1} Σ_s W₁(r_s) r_s^{−1/2} c(s)·q_s^{−1/2} g_{χ_s}(s,−m)`, `s` squarefree primary, `2 ∤ s`, `W₁ = sin²(π(r−1))` on `[1,2]` | `v = 0`. `c(s) = χ_s(b_*) conj ξ(s)` (the paper's `c_σ` without `1_{s∈σ}` and without `τ`). Squarefree `s` only, so `q^{−1/2}g = conj χ_s(−m)γ₁(s)` exactly (O3.1) |
| `B_{m,σ}(Z)` | `Σ_c θ(c) conj Ξ(c) χ_c(m) V(q_c/Z) q_c^{−1/2}`, `θ = γ₂ conj α = μ conj γ₂²`, `Ξ = ξ·χ_•(b_*)`, `V(x) = e^{−x²}`, `q_c ≤ 2.5Z` | **round 1 used `V = e^{−x²}`, not [S30]'s `W_G` (log-Gaussian); corrected in §8**. `η = 1`; `R(·, s_σ)` and the `a_θ` (`conj G`) correction dropped; cube part `n > 1` dropped; Mellin `t → 0`; no slot marks (`J^c = ∅`) |
| pairing | `⟨A, B⟩ = Σ_m Ω ξ(m) A_m B_m` (bilinear) | none |
| `Z` vs `Q` | `Z = Q^{1.15}` (paper: `Q = Z^{M′}`, `M′ ≈ 0.87`) | — |

B variants (only the coefficient of row `c` changes):
* `θ` (the paper's class);
* `μ → 1`;
* `μ →` random `±1`;
* `θ →` random unimodular phase, which keeps every `χ_c(m)` and `|b_c|` ("base_c");
* `|B_m|` with random `m`-phases ("base_m");
* "Bu": `γ₂` without `conj α`.

## 3. The diagonal and the conjugation conventions (coordinator items (a), (b))

**Prop. O3b.1 (PROVED-HERE; imported definitions [S30] l. 3352–3485 and eq:signal).**
1. In eq:low-separated the `m`-dependence of the pair `(s, a)`, with `a = cn³`, is
   `ξ(m)·conj χ_s(−m)·χ_a(m)`. This uses `A ∋ q_s^{−1/2}g_{χ_s}(s,−m) = conj χ_s(−m)γ₁(s)` (O3.1;
   checked here to `10⁻¹⁵`) and `B ∋ Ψ(a) ∋ χ_a(m)` (unconjugated). For squarefree `s`, `c` the
   product `conj χ_s χ_a` is principal on `(m, sa) = 1` exactly when `a = s t⁶` as ideals, i.e.
   `c = s` and `n = t²` (primes shared by `n` and `s` are handled by the zero extensions).
2. On `a = s t⁶`, the arithmetic coefficient is
   `γ₁(s)·γ₂(s) conj α(s t⁶)·conj G(s t⁶)·c_σ(s)·ν_σ(s t⁶)`.
   * By eq:signal, `γ₁γ₂ = μαG`.
   * By eq:G-quadratic-refinement, `conj G(st⁶) = conj G(s) conj G(t⁶) conj R(s,t⁶)`.
   * It therefore equals `μ(s)·ψ_t(s)`, with `ψ_t` a fixed finite-order ray/target function: the
     `η`, `ξ^{−2}`, `R` and `t`-factors.
   * **So the diagonal is a Möbius sum against a finite-order character, not `G·γ₂`.** Without the
     `conj G(A)` correction in `T` it would be `μ(s)G(s)·(ray)`, as the coordinator wrote. Either
     way it is Möbius class.
3. **The diagonal vanishes identically in [S30]'s pairing.**
   * On `a = s t⁶`, the `m`-sum is `Σ_m Ω(q_m/Q)(q_m/Q)^{−iv} ξ(m)·conj χ_s(−1)·1_{(m,st)=1}`.
   * Every factor except `ξ` is invariant under `m ↦ −m`.
   * `ξ(−1) = ξ_λ(−1)ξ_2(−1) = (−1)(1) = −1`. This is forced: the only nonprincipal character of
     `(O/λ)^× = F₃^×` is quadratic.
   * Pairing `m` with `−m` gives zero. ∎

Numerically `|ξ-weighted diagonal|/(‖A‖‖B‖) ≤ 3·10⁻¹⁹`, i.e. machine zero (results/na_Q*.json,
`Rdiag_*`).

**Control without `ξ`** (weight `Ω·1_{(m,6)=1}`):
* The diagonal is present.
* With rows of norm `≥ Z/4` only (results/kubhi), the cumulative pairing's signal-to-noise ratio
  `T/RW` is:

  | `Q` | `θ` (with `μ`) | `μ → 1` |
  |---|---|---|
  | 1024 | 1.43 | 4.16 |
  | 4096 | 0.27 | 12.0 |

* That is the Möbius signature (EMPIRICAL): removing `μ` makes the diagonal coherent.
* With `ξ` restored, all five variants are at noise level on these rows. Signal-to-noise is
  `≤ 1.8`; `R ≈ 0.001–0.025` against a floor of `0.009–0.016`.

So (b): the diagonal part of `⟨A^exc, B⟩` is exactly `0`, and everything measured below is
off-diagonal.

## 4. Operational definitions of `A^exc`

* **OP-G (Gram eigenspace; the literal O3 §2.3 wording).** Take the eigenvectors of the column Gram
  `G = U*ΩU`, with `U_{ms} = conj χ_s(−m)`, whose eigenvalues exceed `1.2×` the Marchenko–Pastur
  edge, and set `A^exc = U·P_exc·a′`.
  * **Result:** the space is empty at every grid point except one (`Q = 1024`, `P_a = 1024`:
    one vector, 0.4 % of `‖A‖²`).
  * The top eigenvalues are MP-like, and the annulus Gram excess `‖A‖²/E‖A_randphase‖² − 1` is
    `−0.04 … +0.07`, against a predicted `c²P_a^{1/6}`.
  * Reason: the sextic Kubota residue is small. `A_1 ≈ 0.22` (SEXTIC_THETA_S6), so in one annulus
    signal/noise is `≈ 0.2·Y′^{1/6} < 1` at `Y′ ≤ 2048`.
  * So OP-G is vacuous at feasible sizes (EMPIRICAL).
* **OP-K (Kubota residue; the identification of O3 §2.3: "the residue of the 6-fold Kubota series at
  1/2 + 1/6").**
  * The `P_a^{1/6}` term of Prop. 15.2 is the contribution of the pole at `w = 2/3` of
    `Σ_s c(s)γ₁(s) conj χ_s(−m) q_s^{−w}`: `‖A^exc‖² ≍ Q^{5/6}Y′^{−2/3} = (Q/Y′)P_a^{1/6}`.
  * Hence `A^exc_m(Y′) = Y′^{−1/3}C_W ρ(m)` with `ρ` independent of `Y′`, and
    `R_exc = |⟨ρ, B⟩|/(‖ρ‖‖B‖)` is independent of `Y′` (HEURISTIC; from the pole structure).
  * Estimator: the cumulative sums `A^{(Y)}_m = Σ_{1<q_s≤Y} c(s)γ₁(s) conj χ_s(−m)` for `Y` up to
    `8·10⁴` (22 589 columns).
  * `‖A^exc‖² ≈ G(Y) − G_diag(Y)`, where `G_diag = Σ_s ‖χ_s‖²_Ω` is exactly the random-column-phase
    expectation.
  * `R_exc ≈ |T_B(Y)|/((G − G_diag)^{1/2}‖B‖)`, with `T_B(Y) = Σ_{q_s≤Y} c γ₁ ⟨conj χ_s(−·), B⟩_{Ωξ}`.
  * Noise floor: `RW/((G − G_diag)^{1/2}‖B‖)`, with `RW² = Σ_s |⟨χ_s, B⟩|²`. A random-column-phase
    control is also run.
  * Checks that OP-K measures the right object:
    * `G − G_diag ∝ Y^{1.36}` at `Q = 256` (Kubota predicts `Y^{4/3}`; pre-asymptotic `1.41–1.49`
      at larger `Q`);
    * random column phases give `G/G_diag − 1` within `±0.09`;
    * `R_exc` is stable in `Y` once signal/noise exceeds 5, e.g. `0.137–0.158` for
      `Y = 2500 … 80000` at `Q = 4096`.
* **OP-A (whole `A`).** In column space, the exceptional eigenvectors of [S30]'s Gram are the probe's
  ray-class vectors (O3 §2.3, Note J). These are of the form `γ₁(s)·(ray character)·(smooth)`, which
  is the form of `A`'s own coefficient vector. So `R_full` on single annuli is also reported.

## 5. Results (EMPIRICAL, floating point, finite)

### 5.1 OP-K: alignment of `A^exc` with `B` (final checkpoint `q_s ≤ 8·10⁴`)

| `Q` | `#m` | `Z` | `G/G_diag − 1` | `R_exc`, `θ` | `μ→1` | `μ→±1` | `θ→`rand phase | `m`-phase baseline | noise floor | `R_exc·√log Z` | `P_a^{−1/12}` at paper geometry |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 256 | 930 | 588 | 1.39 | 0.179 | 0.148 | 0.173 | 0.220 | 0.089 | 0.028 | 0.451 | 0.86 |
| 1024 | 3 696 | 2 896 | 1.22 | 0.155 | 0.165 | 0.143 | 0.149 | 0.027 | 0.016 | 0.437 | 0.82 |
| 4096 | 14 844 | 14 263 | 1.00 | 0.152 | 0.149 | 0.153 | 0.144 | 0.006 | 0.009 | 0.469 | 0.79 |
| 8192 | 29 712 | 31 652 | 0.89 | 0.142 | 0.135 | 0.129 | 0.166 | 0.008 | 0.007 | 0.458 | 0.78 |

Rows of norm `≥ Z/4` only (kubhi): `R_exc = 0.004` (`Q = 1024`) and `0.008` (`Q = 4096`), at the
noise floor (`0.016`, `0.009`). Per-checkpoint tables are in results/analysis.md.

Fits (`log R` against `log Q`, 4 points):
* `R_exc ∝ Q^{−0.059 ± 0.013}`;
* `R_exc·(log Z)^{1/2} = 0.454 ± 0.013`, constant;
* `r₁ = 0.253 ± 0.009`, with fitted slope `+0.018`.

### 5.2 Row by row (diag_c): where the alignment lives

`r_c = |⟨A^{(Y)}, χ_c⟩_{Ωξ}| / (‖A^{(Y)}‖‖χ_c‖)` at `Y = 8·10⁴`. The columns `rms, N(c) ∈ …` and
`max N(c) ≥ 2` use this normalization by the full `‖A^{(Y)}‖`.

| `Q` | `r₁` (row `c = 1`, normalized by `‖A^exc‖`) | `r₁` by `‖A^{(Y)}‖` | its noise floor | rms, `N(c) ∈ [2, 8)` | rms, `[8, 32)` | rms, `N(c) ≥ 512` | largest `r_c`, `N(c) ≥ 2` | `#m^{−1/2}` |
|---|---|---|---|---|---|---|---|---|
| 256 | 0.240 | 0.183 | 0.020 | 0.025 | 0.048 | 0.035 | 0.102 (`N = 1021`) | 0.033 |
| 1024 | 0.259 | 0.192 | 0.009 | 0.004 | 0.031 | 0.016–0.018 | 0.059 (`N = 6349`) | 0.016 |
| 4096 | 0.261 | 0.185 | 0.005 | 0.003 | 0.032 | 0.009 | 0.051 (`N = 13`) | 0.008 |
| 8192 | 0.254 | 0.174 | 0.011 | 0.002 | 0.033 | 0.006–0.007 | 0.054 (`N = 13`) | 0.006 |

At `Q = 4096` and `8192`, the largest rows after `c = 1` are `N(c) = 13, 25, 37, 61, 49, 73`, with
`r ≈ 0.054, 0.043, 0.038, 0.029–0.032, 0.028–0.031, 0.028`. These fall off roughly like
`r₁·N(c)^{−1/2}`; the observed decay is a little slower, `≈ N^{−0.43}` (HEURISTIC fit).

Two consistency checks:
* `‖B‖²/‖1‖² = 2.17, 2.57, 2.99` at `Q = 256, 1024, 4096`. That is `≈ 0.31–0.34·log Z`, i.e.
  logarithmic.
* The predicted `R_exc ≈ r₁(‖1‖/‖B‖) = 0.163, 0.161, 0.151` matches the measured
  `0.179, 0.155, 0.152`.

### 5.3 Single annuli (OP-A), the grid `P_a = 1 … 1024`

The full table is results/analysis.md. Summary:
* `R_full` equals the `θ →` random-phase baseline: median ratio `1.00`, and only 1 of 18 points is
  above that baseline's 90th percentile.
* Both lie above the random-`m`-phase baseline at large `P_a`. For example at `Q = 4096`,
  `P_a = 1024`: `R_full = 0.046`, base_c `= 0.046`, base_m `= 0.0075`.
* At fixed `Q`, `R_full` *grows* with `P_a`: slope `+0.34 … +0.56 (± 0.17 … 0.37)`; base_c
  `+0.08 … +0.28`. HEURISTIC reading: `A^exc` takes a growing share of `A` and aligns with the
  principal row, which base_c keeps.
* All values stay below `P_a^{−1/12}` (`0.56` at `P_a = 1024`). At these sizes that threshold is not
  sharp and decides nothing.
* The `Bu` (no `conj α`), `μ → 1` and `μ → ±1` variants are of the same order as `θ`. Pointwise
  they differ by factors up to a few, where `R_full` happens to cancel, but there is no systematic
  excess (EMPIRICAL).

## 6. Why the alignment is the signal (PROPOSED structural reading)

Poisson in `m` for the pair `(s, a)`, with `s, a` coprime squarefree and modulus `b_* s a`:
* The complete sum at frequency `k` factorizes into `g(ξ)·g(conj χ_s)·g(χ_a)` times cross symbols,
  times `conj(ξ conj χ_s χ_a)(k)`.
* `c_σ(s) = χ_s(b_*)/(τξ(s))` cancels the `b_*`–`s` cross factors (that is its purpose, [S30]
  l. 3373ff).
* `γ₁(s)·g(conj χ_s, 1) ∝ |γ₁(s)|² = 1`: the `s`-coefficient becomes **plain**, `χ_s(k)`.
* The `a`-coefficient becomes `θ(a)·γ₁(a)·conj χ_a(k) = μ(a)G(a)·conj χ_a(k)·(ray)`, using
  `θ = μG conj γ₁`.

At the exceptional frequencies `k = a₁⁶e`, the `s`-sum has no cancellation: this is the Kubota pole,
i.e. `A^exc`. The `a`-sum becomes `Σ_a μ(a)ψ(a)w_k(a)` with `ψ` of finite order (ray × target `η`
in [S30]). So

    ⟨A^exc, B⟩ ≈ Σ_{k exceptional} [Kubota residue in s]_k · Σ_a μ(a) ψ(a) w_k(a)    (HEURISTIC)

At `k = unit` this is the principal row, which [S30] §7 identifies with the reciprocal of the target
`L`-function. The weight comes from two factors: `|b_a| ≈ N(a)^{−1/2}` from the row, and the Poisson
factor `Q/(N(b_* s a))^{1/2}`, which supplies another `N(a)^{−1/2}`. So
`w(a) ≈ N(a)^{−1}V(N a/Z)` and the `a`-sum is `≈ 1/L(1, ψ)` (HEURISTIC).

The `a = 1` term of the Möbius sum is the overlap with B's constant row, which is what §5.2 measures.
Rows with `N(a) ≥ 2` enter with relative weight `≈ N(a)^{−1}`, i.e. `r_c ≈ r₁N(c)^{−1/2}` in the
`‖χ_c‖` normalization. That is what §5.2 finds for `N(c) = 13 … 73`.

This matches O3 §2.2, where the signal is proportional to the exceptional mean `m_f`. Consequences
(PROPOSED):
1. `⟨A^exc, B⟩ ≈ (Kubota mass)·‖1‖/L(1, ψη) + (smaller)`, which is **not small** for a fixed target.
   (NA) would need `|1/L(1, ψη)| ≪ Z^{−b/12}`, so (NA) is false for generic targets. This matches
   the M0 data with `η = 1`: `r₁` is flat, and the four coefficient variants agree because the
   `a = 1` term dominates.
2. If the target `L(s, η)` had a zero `β + iγ` with `0.8598 < β < 0.875`, the principal row would be
   larger still. Bounding it is the zero-free information sought, so (NA) cannot be a non-circular
   input either. Numerics on `η = 1` (GRH-true in practice) cannot see Möbius cancellation; the
   `μ`, `μ → 1`, `±1` and random-phase variants agree to 25 %.
3. For the compensated probe (`B^J`, `J^c ≠ ∅`), the rows carry `1_{D | cn³}` with `D = p_{J^c}`,
   a product of slot primes of norm `Z^{ℓ′}`, weighted by `conj η(p_i)` ([S30] l. 8085–8104). The
   principal row is then `c = D`. There `conj η(p)·ν_σ(p) ∋ conj η(p)η(p) = 1` and `μ(p) = −1`, so
   the slot sum is a prime sum without Möbius cancellation: again the signal. M0 did not model this
   (OPEN), but the mechanism is the same.

**On the "different covers" heuristic (task item 4).**
* By eq:signal and O3.1, `θ(c) = μ(c)G(c) conj γ₁(c)` (PROVED-HERE: `θ = γ₂ conj α = μ conj γ₂²`
  and `γ₂² = conj G·γ₁`; checked numerically, `|γ₁/γ₂²| = 1`).
* So `B_m = conj Σ_c μ(c)ψ′(c) q_c^{−1/2} g_{χ_c}(c, m)V(q_c/Z)`, with `ψ′ = conj G·Ξ` fixed
  finite-order ray.
* Both factors are sums of **sextic** Gauss sums (6-fold cover): `A` plain, `B` Möbius-weighted.
  There is no central-character mismatch, and no Rankin–Selberg vanishing to exploit.
* The relevant difference between the factors is the Möbius weight, and that is exactly the
  circular ingredient. No PROPOSED orthogonality claim is made.

## 7. Verdict and next step

* **(NA) as stated: does not support; falsifying pattern (EMPIRICAL, M0).**
  * `A^exc` overlaps B's principal row with `r₁ = 0.240–0.261`, flat in `Q ∈ [256, 8192]`.
  * `R_exc` decays only through `‖B‖ ∝ (log Z)^{1/2}`.
  * Caveats:
    * the toy omits marks, ray restriction, `η` and cubes;
    * `Q ≤ 8192`;
    * a `Q^{−0.059±0.013}` power law fits too, and alone would satisfy the paper-geometry
      requirement `Q^{−0.028}`;
    * absolute values (`≤ 0.18`) are below `P_a^{−1/12}`;
    * OP-K is an estimator (noise floor `≤ 0.03`).
* **(NA) is false for generic targets and not a non-circular input (PROPOSED, §6).** Its leading
  part is the probe's own principal-row main term, `≈ (Kubota mass)/L(1, ψη)`.
* **Coordinator (c):** (NA) is **not** non-circular. The Möbius sum appears as stated in
  `a = st⁶`-diagonal form in the `ξ`-free control. In [S30]'s pairing the diagonal is exactly
  cancelled by `ξ(−1) = −1` (Prop. O3b.1), and the Möbius sum resurfaces in the exceptional dual
  frequencies.
* **Smallest OPEN statement that could still help, (NA′).** Let `B^♮` be `B` with its principal or
  signal rows removed: `c = 1` (resp. `c = D`) and, for a fixed `δ > 0`, every `c` with
  `N(c) ≤ Z^{δ}`. The statement is `|⟨A^exc, B^♮⟩| ≪ ‖A^exc‖‖B‖ P_a^{−1/12}Z^ε`.
  * Here it holds numerically at the noise level: rows of norm `≥ Z/4` give `R ≈ 0.004–0.008`
    for `θ`, i.e. `≈ #m^{−1/2}` (EMPIRICAL).
  * But (NA′) only helps if the removed part, `⟨A^exc, B − B^♮⟩` (the signal and its short Möbius
    tail), is booked on the high side. The contradiction inequality must then compare the signal
    with itself.
* **Precise next step.** Write the identity
  `⟨A^exc, B − B^♮⟩ = M₀ + O(short Möbius tail)` exactly, where `M₀` is the `k = unit`, `w = 1`
  (`L(1)`) term of [S30] §7 restricted to the Kubota residue. Then check two things:
  1. that the high side's principal row splits as `M₀` plus the zero-dependent residues, with the
     same `M₀`;
  2. that the contradiction argument survives once `M₀` is subtracted from both sides.
  * If it does, (NA′) is the right target. M0 says (NA′) is plausible: rows of norm `≥ Z/4` are at
    the random level.
  * If it does not, the `Z^{b/12}` loss of Prop. 15.2 is intrinsic to this probe. The 0.874957
    barrier then stands for every Cauchy–Schwarz split of it (cf. O3 §2.2's `P_a^{−1/12}` floor).

## Files

* `scripts/na_model.py`: M0 arithmetic in `Z[ω]`: primes, sextic logs, Gauss sums at primes,
  twisted multiplicativity, `ξ`, the ball.
* `scripts/validate.py`: brute-force validation against `a2/eis.py` (imported read-only).
* `scripts/na_run.py`: annulus grid; OP-G, OP-A; baselines; diagonal split; `ξ`-free control.
* `scripts/na_kubota.py`: OP-K cumulative test (`CMIN_FRAC` restricts the row range).
* `scripts/diag_c.py`: per-row alignment.
* `scripts/analyze.py`: writes `results/analysis.md` and `results/fits.json`.
* `results/`: all JSON outputs and logs listed in the header.

Reproduce, e.g. `OMP_NUM_THREADS=1 python3 scripts/na_kubota.py 4096 80000 results/kub_Q4096.json`
(about 3.5 min on a loaded 4-core machine). All randomness is seeded.

## 8. Round 2: does the main term cancel between the two sides? (appended 2026-10-13, about 00:50 UTC)

**Verdict: DOES NOT CANCEL (usefully).** The term that would be subtracted is the target signal
`c_S A_η(Z) f_η(Z)` itself. Subtracting it from both sides removes the only appearance of `1/L` from
the contradiction. (NA′) is therefore not a usable input, and nothing moves below `0.874957`. Labels:
PROPOSED (reading of [S30]), EMPIRICAL (M0 numerics), OPEN where stated.

### 8.1 Correction to round 1 (EMPIRICAL; it retracts the "falsifying pattern")

Round 1's M0 used the row weight `V(x) = e^{−x²}`, which gives every row `c ≤ Z` weight about 1.
[S30]'s row weight is different: the Mellin integral `(1/2πi)∫_{(4)} Z^tΦ(t)…dt` with `Φ = e^{t²}`
produces the log-Gaussian `W_G(q_A/Z) = (2√π)^{−1}exp(−(log(q_A/Z))²/4)` (Lemma gaussian-annular,
l. 1288; used as `V = W_G` in Lemma 15.1, l. 8128ff).
* The constant row `c = 1` therefore has weight `W_G(1/Z) = (2√π)^{−1}e^{−(log Z)²/4}`. That is
  super-polynomially small, for example `≈ 3·10⁻¹¹` at `Z = 1.4·10⁴`.
* The rows that matter have `q_c ≍ Z` within a factor `e^{O(1)}`.
* So the principal-row alignment of §§5.1–5.2, `r₁ ≈ 0.25`, and the `1/L(1, ψη)` reading of §6 are
  **artifacts of the M0 row weight**. They are not features of [S30]'s pairing.

Rerun with `W_G` (`VMODE=loggauss`; rows up to the stated `CMAX`; everything else as in §2):

| `Q` | `Z` | rows up to | `R_exc`, `θ` (actual, with `μ`) | `μ → 1` | `μ → ±1` | `θ →` random phase | `m`-phase | noise floor | signal/noise: `θ` / `μ→1` |
|---|---|---|---|---|---|---|---|---|---|
| 256 | 588 | `136 Z` | 0.0013 | 0.053 | 0.037 | 0.040 | 0.068 | 0.029 | 0.04 / 2.38 |
| 1024 | 2 896 | `27.6 Z` | 0.0091 | 0.043 | 0.006 | 0.011 | 0.018 | 0.016 | 0.57 / 3.58 |
| 4096 | 14 263 | `11.2 Z` | 0.0017 | 0.046 | 0.008 | 0.006 | 0.011 | 0.009 | 0.19 / 7.09 |

(These are the final checkpoint, `q_s ≤ 8·10⁴`.)
* Over the checkpoints `Y = 10⁴ … 8·10⁴`:
  * at `Q = 1024`, `θ` stays at `0.005–0.052`, at or below about 2× the floor, while `μ → 1` stays at
    signal/noise `2.6–3.6`;
  * at `Q = 4096`, `θ` stays `≤ 2.1×` the floor, while `μ → 1` stays at signal/noise `5.0–7.1`.
* `R(μ → 1)` is roughly flat in `Q` (`0.053, 0.043, 0.046`), while the floor falls (`0.029, 0.016,
  0.009`).
* In the `ξ`-free control, `μ → 1` reaches signal/noise `8–12` (`Q = 1024`) and `13–25`
  (`Q = 4096`), while `θ` stays `≤ 1.9`.

* With the [S30] weight, the actual coefficients `θ = μ conj γ₂²` give `R_exc` **at or below the
  noise floor**.
* **Removing `μ` alone** (`μ → 1`) gives a persistent excess at every checkpoint, with signal/noise
  rising with `Q`: `2.4`, `3.6`, `7.1` at `Q = 256`, `1024`, `4096`.
* Random signs or phases in place of `μ` stay at noise (signal/noise `≤ 1.6`). The `m`-phase
  baseline at `Q = 256` is `2.3×` its floor, a small-`#m` effect (`#m = 930`).
* This is the Möbius signature (EMPIRICAL): the part of `⟨A^exc, B⟩` that is not noise is a
  Möbius-weighted sum over rows `q_c ≍ Z`. With `η = 1` its Möbius cancellation is GRH-like in
  practice. Removing `μ` turns `1/L` into `L`, which no longer cancels.

* The earlier diagnostics already pointed this way. Rows with `N(c) ≥ Z/4` gave `R` at the noise
  floor (kubhi, §5.1). Per-row overlaps for `N(c) ≥ 512` sit at `#m^{−1/2}` (§5.2).
* With the faithful weight, the M0 numerics are **consistent with (NA)** at noise level.
* They cannot test the part of `⟨A^exc, B⟩` that matters, for the reason in §8.2: in M0 (`η = 1`,
  zeros GRH-like in practice) the signal part is tiny.

### 8.2 Where the main term sits on the high side (PROPOSED reading of [S30])

* **The high side.** [S30] writes the stage identity `J = Σ_u (rows)` (eq:stage-high-identity). The
  principal row `u = 1` is the only principal numerator row (§"The principal row and the
  normalization", l. 5500–5512).
  * Lemma "Extraction of the principal signal" (l. 6174ff) crosses two scalar poles in that row: the
    additive variable at `w = 1` and the slot variable at `z = 1/6`.
  * It gives `𝒫_η(Z) = c_S A_η(Z)·f_η(Z) + O(Z^{C(β_*)−…})`, where
    `f_η(Z) = (2πi)^{−1}∫_{(2)} Z^{C(s)}e^{(s−5/6)²}H_η(s)/L_F^S(s, η) ds` and
    `c_S = Ŵ₁(1)M(1/6)(Res ζ_F^S)²/6` (l. 5521).
* **Same object, same character, same variable.** The `w = 1` pole is the pole of the plain dual
  column sum, which produces the `Y^{w−1}` signal (O3 §2.2 and l. 3990–4005). On the direct side it
  is exactly the exceptional (Kubota-bias) mass of the additive variable, i.e. `A^exc`.
  * The `a`-sum carries `μ(a)η(a)` at the target `η` itself: the correction `conj G(A)`, the `c_σ`
    normalization and `Ξ` are calibrated so that no residual ray character survives (l. 3373–3380,
    verified coefficientwise in [S30] §local-euler; my reading is that the `ψ` of §6 is trivial in
    [S30], PROPOSED).
  * Its Mellin variable is the `s` of `f_η`, with `C(s) = s − 11/16` in Part II. It is not an
    evaluation at `s = 1`.
  * The sixth-power exceptional frequencies `k = a₁⁶e` (O3 Prop. O3.2) are the replicas that the
    local Euler factor `H_η(s) = ℋ_{η,1}(s, 1, 1/6)` absorbs. So the whole exceptional pairing,
    not only `a₁ = 1`, is part of `c_S A_η f_η` up to the error terms of Lemma lem:principal-residue-interface.
  * Hence (PROPOSED; the exact identity is OPEN):

        ⟨A^exc, B⟩  =  c_S A_η(Z) f_η(Z)  +  E,     E = exceptional-pairing remainder.

* **Where a subtraction would act.** The contradiction is Prop. "Continuation from a common signal"
  (l. 400ff). Its only use of the two inputs is the triangle inequality behind eq:uniform-saving:

        |f_η| ≤ |J| + |J − f_η|   (normalized by c_S A_η),

  with the low input `|J| ≪ Z^{C(σ0)+ω}` (eq:low-probe-contract) and the high input
  `|J − f_η| ≪ Z^{C(β_*)−σ}` (eq:high-probe-contract).
  * Subtracting `M₀ = c_S A_η f_η` from `J` on the low side turns the low input into a bound for
    `J − f_η = ⟨A^rest, B⟩ + E`. That is the **same quantity** the high input bounds.
  * The triangle inequality becomes `|f_η − f_η| ≤ …`, which is vacuous. No information on
    `1/L_F^S(s, η)` remains, and the Mellin continuation step (l. 458ff) has nothing to continue.
* So **the main term does appear identically on both sides**: same `η`, same `s`, same `H_η`. But
  cancelling it is exactly what the contradiction must not do. The low side has to bound `J`, signal
  included, without knowing where the zeros are. [S30] does this by Cauchy–Schwarz, and the price is
  `‖A^exc‖`, i.e. the `P_a^{1/12} = Z^{b/12}` loss.

### 8.3 Consequences for (NA) and (NA′)

* **(NA′)**, defined as `|⟨A^exc, B⟩ − c_S A_η f_η| ≪ ‖A^exc‖‖B‖P_a^{−1/12}Z^ε` (equivalently
  `|E| ≪ (Q/Y′)^{1/2}‖B‖Z^ε`, or with B's signal-carrying part removed):
  * EMPIRICAL status: consistent at noise level in M0 (§8.1 table).
  * Usefulness: none. It only bounds a piece of `J − f_η`, which the high side already controls. It
    gives **no σ0 at all**. The O3 model value `926/1077` does **not** follow from (NA′).
* **(NA)** itself, `|⟨A^exc, B⟩| ≪ (Q/Y′)^{1/2}‖B‖Z^ε`:
  * If `E` is small (as M0 suggests), (NA) is equivalent, up to the high-side errors, to
    `|f_η(Z)| ≪ Z^{C(σ′)+ω}` at the improved exponent. By the continuation criterion that is the
    zero-free statement itself, so (NA) is **circular** (PROPOSED).
  * Granting it still gives the CONDITIONAL `926/1077` of O3 §5, but only as a restatement of the
    conclusion.
* **Net.** Within this probe, the `Z^{b/12}` Gram loss is the price of bounding the signal-carrying
  component without zero information. Any Cauchy–Schwarz split that removes it either keeps the
  signal on the low side, which is circular, or cancels it, which is vacuous.
  * A way below `0.874957` along this line needs a **low-side bound for the signal-carrying
    pairing that does not go through `‖A^exc‖` and does not use the size of `f_η`**.
  * The visible gap is this:
    * `‖A^exc‖²` counts the `≍ K^{1/6}` sixth-power replicas `k = a₁⁶e` with equal ℓ²-mass, which
      is the `P_a^{1/6}`.
    * In the pairing the same replicas enter with the convergent local weights that `H_η` absorbs.
  * Smallest statement (OPEN, HEURISTIC formulation): a replica-wise bound
    `Σ_{a₁}|⟨A^{exc,a₁}, B⟩| ≪ (Q/Y′)^{1/2}‖B‖Z^ε`, proved without zero information.
    * It is non-circular only if the per-replica pairings can be bounded by norms that decay in
      `N(a₁)`.
    * Each replica pairs with all rows of B (the conditions `conj χ_a(a₁⁶) = 1` are automatic), so
      no such decay is visible; I found no candidate.
    * Since `H_η − 1` is a fixed, `Z`-independent factor, the replica sum is itself a fixed multiple
      of the signal. A replica-wise bound that uses its size is again circular.

Files for round 2:
* `scripts/na_kubota.py`: new `VMODE=loggauss` and `CMAX` options.
* `scripts/summarize_lg.py`: tables for §8.1.
* Outputs: `results/kublg_Q{256,1024,4096}.json` and `.log`.
