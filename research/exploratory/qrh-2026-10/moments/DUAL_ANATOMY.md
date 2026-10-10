# Pair and dual anatomy of the sub-diagonal second moment

```text
Status: EMPIRICAL (finite, binary64, not certified) + PROPOSED (three elementary identities, §1,
  proved here, not reviewed) + HEURISTIC (§5 reading). RH is unsolved; nothing here bears on it directly.
Scope: the second moment M_2(D; H) = sum_{0 < N u <= H} |A_u(D)|^2 of the sextic Moebius family over
  Q(omega) (nu = 1, W the bump of common.py), sub-diagonal H = D^rho, rho in {0.5, 0.7, 0.9, 1.1},
  D in {500, 707, 1000, 1414, 2000, 2828, 4000}; explicit Poisson dual with a Gaussian row weight at
  D in {150, 300}. Coefficient controls: random signs on ideals, random multiplicative signs,
  conjugation-symmetric versions of both, lambda(n), and 1.
Exact sources or dependencies: RUNG_STRENGTH.md (§§3-5, the rho = 1 wall); moments/README.md and its
  addendum (results/subdiag_k1.*); FOURTH_MOMENT_A2.md §§4, 6 (dual diagonal, involution);
  A2_LITERATURE.md §§0, 5 (Dunn-Radziwill dispersion, Patterson bias risk). Code: common.py,
  eisenstein.py, moments.py (imported unchanged), sextic_kernel.c (compiled into a scratch directory).
What was actually run (4-core shared machine, nice -n 10, <= 2 BLAS threads):
  anatomy_pairs.py --D 500 707 1000 1414 2000 2828 4000 --K 200          ~4 min
  anatomy_galois.py --D 500 1000 2000 2828 --K 200                        ~15 s
  anatomy_dual.py --D 150 300 --rhos 0.5 0.7 0.9 --K 100                 ~4 min
  Outputs: results/anatomy_{pairs,galois,dual}.json (rounded to 4 significant digits), *.log.
  Checks: kernel A_u vs matrix A_u at 150 rows per D (max diff 6e-14); exact-symbol table
  self-test; Poisson identity pair by pair (rel. err <= 2e-8) and in total (|Off_direct - Off_dual|
  <= 2.4e-9 Diag); Galois prediction vs measured piece on sixth-norm rows (agree to all 4 printed digits).
Smallest remaining gap: no structured term carrying the cancellation was found. The off-diagonal
  cancels across pairs as it does for random signs, so a proof of Mom(1, rho), rho < 1, still needs an
  on-average GRH-type input (RUNG_STRENGTH §4). No secondary term was found that shrinks the dual diagonal.
```

## 0. Answer in brief

* **The off-diagonal is not small pair by pair.** `Σ_{n≠m} |a_n a_m S_H(n,m)|` is 0.36 to 12.6 times
  Diag, growing as ρ falls, and 13 to 1227 times `|Off|`. It is small because of cancellation *across*
  pairs.
* **The cancellation is random-type, not structured.** μ's `Off/Diag` sits inside the
  distribution of random ±1 signs in all 28 cells: mean z = −0.47, sd 1.34, worst z = −3.6 (D = 2828, ρ = 0.9).
  Against conjugation-symmetric random signs the values are −0.54 and 0.98. The same holds for λ.
  * In the eigenbasis of `S_H`, μ's energy profile equals that of random signs.
  * No pair class and no row class carries a μ-specific share beyond the random spread.
* **The "positive mean" exists and is trivial.** The W-weighted mean of `S_H(n,m)` over off-diagonal
  pairs is 0.7–2.1, against a spread of `0.92·√R` (R = 234–33264 rows).
  * It is the principal-row term `#(sixth-power rows) · |Σ_n a_n|²`, up to coprimality.
  * The constant coefficient 1 feels it: M₂/Diag = 1.7–3.4 at ρ = 0.5, falling to 1.03 at ρ = 1.1, more
    than 100 % of it from sixth-power rows.
  * Every mean-zero sign sequence removes it, so nothing about it is specific to μ.
* **One explicit secondary term was found; it does not cancel anything.** μ(n̄) = μ(n), so all
  same-norm pairs (partial Galois conjugates) are sign-coherent.
  * They contribute an exact, positive, predictable piece on the rows with `N u` a sixth power (§1.2,
    §3). It has relative size ≈ (⟨2^s⟩_W − 1)·#{sixth-norm rows}/R, and it decays like `H^{−5/6}`
    times a power of log D.
  * Random multiplicative signs with f(π) = f(π̄) carry exactly the same piece. μ's total
    off-diagonal is not visibly raised or lowered relative to that control: mean difference
    about −0.5σ, not significant.
* **The dual adds no structure.** The Poisson identity was verified, and the dual diagonal is
  `DD ≈ 1.3·(D/Y)·Diag`, as predicted.
  * The dual off-diagonal is spread over generic frequencies. The top 1000 |T(h)| overshoot the total,
    and the bulk cancels them.
  * Special dual frequencies (units × sixth powers, cubes, squares) carry ≤ 0.04·Diag, inside the
    control spread. No Patterson-type bias is visible at these sizes.
  * The Galois piece is the one structured term. In the dual it appears as a flat, delocalized
    correction over generic h with `N h ≲` the dual length. It *adds* to the dual asymptotic and does
    not cancel DD (HEURISTIC, §5).

## 1. Three elementary identities (PROPOSED, proved here)

Notation: `S_H(n,m) = Σ_{0<Nu≤H} χ_n(u) conj χ_m(u)`, so that `M₂ = Σ_{n,m} a_n a_m S_H(n,m)` for real `a`.
Rows are all nonzero `u ∈ Z[ω]`, as in moments.py.

**1.1 Unit orthogonality.** The row set is stable under `u ↦ εu` for each unit ε, and
`χ_n(εu) conj χ_m(εu) = (χ_n conj χ_m)(ε) · χ_n(u) conj χ_m(u)`. Hence `S_H(n,m) = 0` identically
unless `χ_n = χ_m` on the units.

On these columns χ_n(ζ) is equidistributed in μ₆. So about 5/6 of all pairs vanish exactly: 951 388 of
1 259 944 off-diagonal squarefree pairs at D = 4000. For unit-aligned pairs the six associates add
coherently, and `|S|²` is about `6R` (measured rms `|S|/√R` = 2.26–2.29, against `√6·0.93`). This is
trivial bookkeeping. It removes 5/6 of the pairs from Off, but it does not make the remaining
unit-aligned sum small.

**1.2 Galois coherence.** For squarefree ideals prime to 6, `N n = N m` iff `m` arises from `n` by
replacing some split primes π ∥ n, with π̄ ∤ n, by π̄. Then μ(m) = μ(n) and W(Nm/D) = W(Nn/D). Since
`conj χ_{π̄}(u) = χ_π(ū)` (apply complex conjugation to `u^{(Np−1)/6} ≡ ζ^k mod π̄`),

    Σ_{m : N m = N n} χ_n(u) conj χ_m(u) = 1_{(u,n)=1} · ∏_{π | n, π̄ ∤ n} (1 + χ_π(N u)).

On rows with `N u = j⁶` every factor is 2. For any coefficients constant on same-norm classes (μ, λ,
and f multiplicative with f(π) = f(π̄)), the same-norm pairs therefore contribute

    Off_gal = Σ_u Σ_n a_n² 1_{(u,n)=1} [∏(1 + χ_π(Nu)) − 1],
    Pred_gal (rows with N u = j⁶) = Σ_{N u = j⁶ ≤ H} Σ_n a_n² 1_{(u,n)=1} (2^{s(n)} − 1),

with `s(n) = #{π | n split, π̄ ∤ n}`. For H < 4096 the sixth-norm rows are exactly the 6 units,
the 6 elements 8ε of norm 64, and the 6 elements 27ε of norm 729 (r(j⁶) = 6 for j = 1, 2, 3). Random
signs on ideals keep only `m = n̄` in expectation; random signs on conjugation orbits keep the same.

**1.3 Exact Poisson dual (Gaussian rows).** With `g(u) = exp(−π N u / Y)`, `c = lcm(n, m)` and `Q = N c`,

    S_Y(n,m) = (2Y/(√3 Q)) Σ_{h ∈ Z[ω]} exp(−4πY N h/(3Q)) G_{n,m}(h).

Here `G = ∏_{p|c} G_p`, with:
* `G_p = χ_p(c/p) conj χ_p(h) τ_p` for p | n only;
* `G_p = conj χ_p(c/p) χ_p(h) τ_p⁻` for p | m only;
* `G_p` = the Ramanujan sum for p | (n, m).

τ_p and τ_p⁻ are the sextic Gauss sums with `e(z) = exp(4πi Im z/√3)`. This is standard lattice
Poisson summation plus CRT. `h = 0` contributes only for `n = m`, so `Off = Σ_{h≠0} T(h)`. The dual diagonal is

    DD = (2Y/√3) Σ_n a_n² N(n)^{−1} Σ_{h≠0, (h,n)=1} exp(−4πY Nh/(3 N n²))   ≈ 1.3·(D/Y)·Diag.

## 2. Pair anatomy (EMPIRICAL; results/anatomy_pairs.json)

`M₂/Diag` uses the exact diagonal `Σ a_n² #{u : (u,n) = 1, Nu ≤ H}`. The controls use K = 200 samples
each and are shown as mean ± sd. The columns are:
* rand: iid ±1 on squarefree ideals;
* rmf: random completely multiplicative signs;
* randc: iid on conjugation orbits {n, n̄};
* rmfc: multiplicative with f(π) = f(π̄).

| D | ρ | rows | μ | λ | 1 | rand | rmfc | z(μ vs rand) | Σ\|aaS\|/\|Off\| | Σ\|aaS\|/Diag |
|---|---|---|---|---|---|---|---|---|---|---|
| 500 | 0.5 | 84 | 0.986 | 0.965 | 1.72 | 0.996±0.106 | 1.022±0.171 | −0.10 | 180 | 2.5 |
| 500 | 0.9 | 966 | 0.974 | 0.968 | 1.02 | 1.002±0.023 | 0.993±0.023 | −1.18 | 26 | 0.7 |
| 1000 | 0.5 | 120 | 0.903 | 0.921 | 2.00 | 1.000±0.096 | 1.022±0.121 | −1.01 | 44 | 4.3 |
| 1000 | 0.9 | 1812 | 0.959 | 0.968 | 1.06 | 1.000±0.020 | 0.993±0.029 | −2.10 | 25 | 1.0 |
| 2000 | 0.7 | 744 | 0.931 | 0.924 | 1.31 | 1.000±0.035 | 1.008±0.052 | −1.94 | 52 | 3.6 |
| 2828 | 0.5 | 198 | 1.183 | 1.156 | 3.11 | 1.000±0.074 | 1.036±0.110 | +2.47 | 53 | 9.7 |
| 2828 | 0.9 | 4638 | 0.946 | 0.955 | 1.19 | 0.998±0.014 | 0.998±0.021 | −3.60 | 35 | 1.9 |
| 4000 | 0.5 | 234 | 0.964 | 0.973 | 3.43 | 1.003±0.066 | 1.037±0.092 | −0.59 | 347 | 12.6 |
| 4000 | 0.7 | 1200 | 0.990 | 0.999 | 1.39 | 0.999±0.029 | 1.013±0.041 | −0.28 | 570 | 5.5 |
| 4000 | 0.9 | 6342 | 0.989 | 0.988 | 1.14 | 1.000±0.012 | 1.002±0.017 | −0.91 | 212 | 2.3 |
| 4000 | 1.1 | 33264 | 1.004 | 1.004 | 1.04 | 1.001±0.006 | 1.003±0.008 | +0.46 | 307 | 1.0 |

All 28 cells are in the log and the JSON.

* **Random-type, not structured.** μ is below 1 in 19 of 28 cells, and the mean z is −0.47. The
  cells share columns across ρ and primes across D, so we do not read this as a signal.
* **Most pairs have no completion cancellation.** Pairs whose pair character
  `χ_{n'} conj χ_{m'}` (gcd removed) has conductor ≤ H do cancel pair by pair, with rms `|S|/√R` of
  0.25–0.33 at ρ ≥ 0.7. They are 0.1–0.4 % of the pairs and carry ≤ 2 % of Diag. All other pairs
  behave like random sums, with rms `|S|/√R ≈ 0.92`, or `√6·0.93` when unit-aligned.
* **Pair classes:**
  * shared prime (gcd);
  * conjugate-shared prime;
  * coprime unit-aligned;
  * non-aligned (≡ 0).

  For μ, the generic and unit-aligned classes stay within the random spread. Deviations up to 3.9σ
  occur only in the conjugate and gcd classes, which contain the Galois-coherent pairs (§3):
  * the conjugate class: μ gives +0.049 Diag at D = 4000, ρ = 0.5, against σ = 0.013;
  * gcd pairs `(g r, g r̄)`.
* **Row classes.** No row class (sixth, cube, square, generic) carries a μ-specific excess except the
  sixth-norm rows (§3). For the constant coefficient 1, the sixth-power rows carry more than all of
  Off: +2.59 Diag of +2.43 at D = 4000, ρ = 0.5.
* **Spectral view.** We normalise `a` and expand it in the eigenvectors of `S_H` (squarefree columns).
  The fraction of energy in the top 10 % of eigenvectors is 0.086–0.105 for μ, 0.095–0.099 for random
  signs, and 0.13–0.39 for 1 (D = 4000). μ is in generic position with respect to `S_H`, and that is
  all `M₂ ≈ Diag` means.

## 3. The Galois-coherent term (EMPIRICAL test of §1.2; results/anatomy_galois.json)

| D | ρ | Pred_gal/Diag | μ: Off/Diag | μ: Off_gal | μ: Off_rest | rmfc: Off (mean±sd) | randc: Off_gal (mean) |
|---|---|---|---|---|---|---|---|
| 500 | 0.5 | 0.138 | −0.014 | +0.044 | −0.058 | +0.033±0.155 | −0.003 |
| 500 | 0.9 | 0.024 | −0.026 | −0.007 | −0.019 | −0.005±0.023 | +0.002 |
| 1000 | 0.5 | 0.101 | −0.097 | +0.028 | −0.125 | +0.038±0.123 | +0.042 |
| 1000 | 0.9 | 0.013 | −0.041 | −0.008 | −0.034 | −0.008±0.030 | −0.000 |
| 2000 | 0.5 | 0.088 | −0.046 | +0.020 | −0.066 | +0.030±0.110 | +0.031 |
| 2000 | 0.9 | 0.013 | −0.028 | −0.010 | −0.019 | −0.009±0.026 | −0.002 |
| 2828 | 0.5 | 0.074 | +0.183 | +0.045 | +0.137 | +0.044±0.109 | +0.035 |
| 2828 | 0.9 | 0.009 | −0.054 | −0.004 | −0.050 | −0.003±0.022 | −0.001 |

The W-weighted mean of `2^{s(n)}` is 2.83 (D = 500) to 3.29 (D = 2828). It grows like a power of
log D.

* The prediction equals the measured same-norm contribution on the sixth-norm rows to all printed
  digits. This checks identity 1.2 numerically.
* On the other rows the same-norm pairs contribute `Σ a_n² [∏(1 + χ_π(Nu)) − 1]`. That is a character
  sum in `N u` with no main term, and it fluctuates around 0.
* μ and rmfc have *identical* `Off_gal`, because both are constant on same-norm classes.
* μ's remaining part `Off_rest` is negative in 12 of 16 cells. Over 16 cells `Off(μ) − mean Off(rmfc)`
  averages about −0.5σ. We do not claim that `Off_rest` compensates `Off_gal`.
* What the sixth-norm rows show directly: there, `A_u` is a Möbius sum over *rational norms* (a
  coefficient of `1/(ζ(s)L(s,χ_{−3}))`, twisted by a character that factors through the norm). Its
  cancellation is governed by the zeros of ζ_K, not by the family. These are 6–24 rows, too few to
  measure a trend.

## 4. Explicit dual (EMPIRICAL; results/anatomy_dual.json)

Gaussian rows, squarefree columns D < Nn < 2D, `#h` = 17 000–360 000 dual frequencies.

| D | ρ | Y | DD/Diag | Σ\|T(h)\|/Diag | Σ_pairs\|terms\|/Diag | μ Off/Diag | randc Off (mean±sd) | rand Off (mean±sd) | μ: sixth/cube/square h |
|---|---|---|---|---|---|---|---|---|---|
| 150 | 0.5 | 12.2 | 16.4 | 8.4 | 321 | +0.486 | +0.41±0.36 | −0.00±0.28 | −0.015/−0.016/−0.004 |
| 150 | 0.7 | 33.4 | 5.9 | 2.9 | 115 | +0.145 | +0.15±0.16 | −0.00±0.13 | −0.011/−0.011/+0.015 |
| 150 | 0.9 | 90.9 | 2.1 | 1.1 | 42 | −0.018 | +0.035±0.076 | −0.007±0.060 | −0.009/−0.006/+0.024 |
| 300 | 0.5 | 17.3 | 22.9 | 12.0 | 897 | +0.200 | +0.23±0.29 | +0.01±0.21 | +0.003/+0.028/+0.039 |
| 300 | 0.7 | 54.2 | 7.2 | 3.8 | 282 | +0.064 | +0.069±0.106 | +0.006±0.094 | +0.002/+0.020/+0.022 |
| 300 | 0.9 | 169.6 | 2.3 | 1.2 | 90 | +0.031 | +0.022±0.057 | +0.004±0.045 | +0.003/+0.013/+0.011 |

* `DD·Y/(D·Diag)` = 1.27–1.33 in every cell. The dual diagonal is `≍ (D/H)·Diag`, as stated in the task.
* The dual off-diagonal is diffuse. At D = 150, ρ = 0.5:
  * the 10, 100 and 1000 largest |T(h)| sum to 0.11, 0.63 and 1.09 Diag;
  * all 127 302 frequencies sum to 0.49 Diag.

  The bulk of small terms cancels the overshoot. No small set of h carries the off-diagonal.
* **Special dual frequencies.**
  * Units × sixth powers, cubes and squares carry ≤ 0.04 Diag in every cell. The controls have
    sd 0.006–0.026 there.
  * Each single unit frequency carries |T| ≤ 0.003 Diag.
  * So no Patterson-type bias (Kubota pole, A2_LITERATURE §5 "risk to check") is visible at
    D ≤ 300 with the Möbius coefficients. This is a tiny range.
* **μ tracks randc, not rand**, under the Gaussian weight.
  * There the 6 unit rows carry a fraction `6e^{−π/Y}/(2Y/√3)` ≈ 10–36 % of the total row weight, so
    the Galois term (§1.2) on the unit rows dominates Off at small Y.
  * In the dual this term sits in generic h with `N h` up to about the dual length. Example: the
    randc N(h) bin [0.3, 1)·(dual length) has +0.30 ± 0.11 at D = 150, ρ = 0.5. It is the flat Poisson
    image of a few rows.

## 5. Reading (HEURISTIC)

1. **What carries the cancellation.** The unit-aligned pairs (1/6 of all) cancel each other with
   random-type signs. Equivalently, on the row side, `Σ_u (|A_u|² − diag_u)` is a sum of R mean-zero,
   roughly independent terms, so `|Off|/Diag ≈ R^{−1/2}`. Nothing in the pair, row, spectral or dual
   anatomy distinguishes μ from random ±1 signs at D ≤ 4000, apart from the Galois term. That term is
   shared by every Galois-invariant multiplicative sign pattern.
2. **Secondary main term.** The one explicit structured term is `Pred_gal`.
   * It is positive and of relative size about `(⟨2^s⟩ − 1)·r(j⁶)-rows/R ≍ H^{−5/6}(log D)^{O(1)}`.
   * On the dual side it would appear as a smooth "main-term correction" spread over the dual
     diagonal region. That is the shape of the Dunn–Radziwiłł correction.
   * It does not cancel the dual diagonal. It is an extra positive term that a dispersion asymptotic
     for this family must include, harmless for Mom(1, ρ) because it decays.
   * A Patterson-bias term at cube or square dual rows was looked for and not seen.
3. **Consequence for a proof.** The needed cancellation has no visible structured carrier. It is the
   generic statement that μ is in generic position relative to the row vectors `(χ_n(u))_u`. Random
   signs achieve this in expectation trivially; μ is deterministic. Proving it for μ is the
   on-average-GRH content identified in RUNG_STRENGTH §4. This anatomy found no shortcut around it.
   Finite numerics cannot exclude a structured term that appears only at larger D or for other W.

## Files

| file | role |
|---|---|
| `anatomy_common.py` | column sets (squarefree and all primary n), symbol matrices from the eisenstein tables, row classes, gcd/conjugate masks, pair conductors, kernel build into a scratch directory |
| `anatomy_pairs.py` | §2: pair, row, dual-length and spectral anatomy; controls rand, rmf, randc, rmfc, λ, 1 |
| `anatomy_galois.py` | §3: same-norm (Galois) split and the prediction `Pred_gal` |
| `anatomy_dual.py` | §4: exact Poisson dual with Gaussian rows, by dual-frequency class and N(h) bin |
| `results/anatomy_{pairs,galois,dual}.json`, `results/anatomy_{pairs,dual}.log` | outputs (rounded) |
