# The low-side bilinear form at small scale: true size against Cauchy–Schwarz and the large sieve

```text
Status: EMPIRICAL (finite, binary64, NOT certified) + exact-symbol validations (FLOATING checks
  against independent direct sums). Mechanism discovery only. Finite ladders prove nothing
  asymptotic. No RH claim, and no claim about the correctness of the external manuscript [OAI].
Scope: the separated low-side form Q^{-1/2} sum_m w(m) xi(m) A_m B_m of [OAI] (TeX l. 3461,
  3428/2818-2829, 3470-3476, CS at l. 8612), at a fixed height, with nu = 1 and the
  simplifications of Sec. 1. Two geometries, primal theta length Z <= 4.99e5. A-side Gram
  study at row length Q <= 1e5 and 0.01 <= P_a <= 100.
Exact sources or dependencies: [OAI] 30 Sep 2026 TeX (pr908 copy; untrusted, unreviewed);
  ../BILINEAR_B2.md (object, CS step, Gram excess, [dFDH] reading); ../moments/eisenstein.py
  (residue tables, PrimeIdeal), ../moments/common.py (W, PrimeData), ../a2/eis.py (exact
  symbols and direct Gauss sums), all imported unchanged. New: b2_kernel.c (compiled into the
  scratchpad only), b2_common.py, b2_ladder.py, b2_gram.py, b2_fit.py.
What was actually run (4-core shared machine, nice -n 10, <= 2 processes):
  gamma_2 table for all 78,548 primary primes with N <= 1e6 (direct O(p) sums, 217 s, cached in
    the scratchpad);
  b2_ladder.py --validate                                     -> results/b2_validate.json
  b2_ladder.py results/b2_ladder_d0.json d0 3162 ... 499000   (6 rungs, ~3 min)
  b2_ladder.py results/b2_ladder_dl.json dl 10000 ... 499000  (5 rungs, ~1 min)
  b2_gram.py   results/b2_gram.json 10000 30000 100000        (24 cells, ~5 min)
  b2_fit.py on both ladders.
Smallest remaining gap: everything here is at Z <= 5e5 (Q <= 1.2e4, Y' <= 219, P_a <= 4.1 in
  the bilinear ladder). The measured random-type size of the form says nothing about a provable
  bound. The B2 input stays open: an unconditional sub-large-sieve bound for
  sum_s |sum_m w(m) conj(chi_s(m)) B_m|^2 that works for the actual theta row.
```

**RH remains unproved. Nothing here proves or disproves it.** All numbers are finite and
EMPIRICAL. They describe one model of one external, unreviewed proof step.

## 0. Answer in brief

1. **The true bilinear form is far below Cauchy–Schwarz at every measured scale, with a decay
   rate that matches random phases.**
   * In geometry d0, `|S|/‖A‖‖B‖` (rms over 16 heights) falls from 0.075 to 0.0102 as `Z` goes
     from 3.2e3 to 5.0e5. The fitted slope is `−0.351` in `log Z`.
   * The random-phase prediction is `−½·d log(#rows)/d log Z = −0.357`.
   * `|S|/U ≈ 0.7–1.2` throughout. Here `U = (Σ w²|A_m|²|B_m|²)^{1/2}` is the size of a sum of
     uncorrelated terms. So `S` is a sum of essentially uncorrelated terms.
   * In the paper's own `Z` units this is the full heuristic saving `Q^{1/2}` of BILINEAR_B2
     §2.3. It is not a small `ϑ`.
2. **The twisted first moments are at the diagonal size, not the large-sieve size.**
   * `L = Σ_s |𝓑(χ̄_s)|²` equals the diagonal `D = Σ_s Σ_m |χ_s(m)|²|b_m|²` to within
     0.83–1.18 at every rung.
   * Measured against the sharp coefficient-blind large-sieve constant of the same configuration
     (`λ_max` of the character Gram matrix), `L/(λ_max‖b‖²)` falls from 0.012 to 0.0023. That is
     roughly `#s/#rows`.
3. **None of this is specific to the Gauss-sum structure.** In every cell the true Gauss sums
   are inside the spread of the controls:
   * `γ_2(c)` replaced by iid phases (two draws);
   * the Kummer cube-root choice of `γ_2(p)` re-randomised, keeping twisted multiplicativity;
   * `γ_1(s)` replaced by iid phases (eight draws).

   This holds for `|S|/CS`, `|S|/U`, `L/D` and `‖B‖²`. For example, at the top rung
   `‖B‖²/row` is 0.0539 (true) against 0.0540 (iid).
4. **The Gram excess is visible, Gauss-sum specific and small. Its growth in `P_a` is not
   resolved.**
   * For `P_a ≥ 20`, `Σ w|A_m|²` exceeds its diagonal by +2.3 % to +4.1 % with the true sextic
     Gauss sums, at z = 4–17 against iid phases. The phases give 1.000 ± 0.003.
   * At smaller `P_a` the deviations are ≤ 1.2 % and of both signs.
   * The excess does not grow between `P_a = 32` and `P_a = 100`, whereas `P_a^{1/6}` grows
     from 1.78 to 2.15.
   * So the `P_a^{1/6}` term of (8354) is present at most with a small constant (≤ 0.03 in these
     units). A `P_a^{1/6}` law can be neither confirmed nor excluded: over the accessible range
     `P_a^{1/6}` changes by a factor of only 1.2.
   * In the bilinear ladder itself (`P_a ≤ 4.1`) the true `‖A‖²` is at its diagonal
     (0.98–1.02), apart from 1.13 at the smallest rung.

**Reading.** At these scales Cauchy–Schwarz loses roughly the full `(#rows)^{1/2}`, and so does
the large sieve over `s`. The loss is generic: random phases on the same supports lose exactly
as much. The numerics therefore point to no arithmetic mechanism that a proof could exploit, and
to no hidden conspiracy (a correlation between `A` and `B`) that would make CS sharp. The
obstruction in BILINEAR_B2 remains one of proof, not of truth, at least up to `Z = 5·10⁵`.

## 1. The model (definitions extracted from the TeX; simplifications listed)

Notation is that of BILINEAR_B2 §1.1: `χ_c(a) = (a/c)_6` is zero-extended; `e(z) = exp(4πi Im z/√3)`;
`γ_j(c) = q_c^{-1/2} Σ_{v mod c} χ_c(v)^j e(v/c)`. "Primary" means ≡ 1 mod 3. All ideals are
prime to 6 and represented by their primary generators.

**The form.** The form (TeX l. 3470–3476 at height `v`) is

    S_v = Σ_{m ≠ 0} w(m) ξ(m) (q_m/Q)^{-iv} A_{m,v} B_m,
    A_{m,v} = Y^{-1} Σ_{s sf} W(q_s/Y) (q_s/Y)^{-1/2+iv} γ_1(s) conj χ_s(−m),
    B_m     = Σ_{c sf, n} γ_2(c) conj α(c n³) χ_c(m) χ_n(m)³ q_c^{-1/2} q_n^{-1} V(q_c q_n³/Z).

* **`A`.** By TeX l. 3461, `q_s^{-1/2} g_{χ_s}(s,−m) = γ_1(s) conj χ_s(−m)` for squarefree `s`.
  This holds for all `m`, since both sides vanish when `(m,s) ≠ 1`. It was checked against direct
  Gauss sums (§2).
* **`B`.** `B` is `𝒞_V(Z; m, ν)` (eq. `unmarked-central-completion`, TeX l. 2818–2829) with `ν = 1`.
  It is the `ν = 1` member of the family `B_{m,σ} = Σ_θ a_θ 𝒞_{V_G}(Z; m, ν_σθ)` (l. 3438–3446).
  `n` runs over all primary `n` prime to 6, which may share primes with `c`.
* **`ξ`.** `ξ` is the primitive character mod `2λ` of l. 3349: the order-3 character of
  `(O/2)^×` times the quadratic character of `(O/λ)^×`. It forces `(m,6) = 1`.

**Simplifications.** All are fixed-data or smooth-weight changes. The paper's norm bounds
(Gram, row norm) are uniform over them.

| paper | here | why harmless (or not) |
|---|---|---|
| ray decorations `χ_s(b*)/(τξ(s))`, class `σ`, `ν_σθ`, `a_θ`, `η` | dropped (`ν = 1`; all `s`) | fixed finite-order ray characters. The bounds being tested are uniform in them. A different member of the same family could carry a coherent main term; not tested |
| `s` all primary moduli | squarefree `s` only | keeps `A` a sextic character polynomial (BILINEAR_B2 §1.2). Non-squarefree `s` contribute only on rows sharing primes with `s` |
| `V_G` (Mellin `e^{t²}`, log-Gaussian) | `V = W`, the bump of moments/common.py on (1,2) | smooth, compactly supported, satisfies the reflection hypotheses. Avoids `c` up to `~e⁵Z` |
| `Ω(q_m/Q)`, `Ŵ_0(iv)` integral | `w(m) = W(q_m/Q)`; separate forms at heights `v = 9j`, `j = 0..15` | the CS step is applied at each fixed `v`. The 16 heights are used only as statistical replicas |
| marked rows `B^J` (l. 8097) | unmarked row, two length ratios (below) | the marks add a sum over slot primes `p` of size `Z^{ℓ}` with `χ_p(m)`. Not modelled |

**Geometries.** `Z` here is the primal theta length (the scale in `V(q_c q_n³/Z)`).

* **d0.** The paper's `d = 0` exponents (`Q = Z_p^{5/6}`, `Y' = Z_p^{23/48}`, theta length
  `Z_p^{7/6}`), re-expressed in the theta length: `Q = Z^{5/7}`, `Y' = Z^{23/56}`,
  `P_a = Z^{3/28}`. This keeps the ratio of row range to theta conductor.
* **dl.** The paper's fully rescaled `d = ℓ` (unmarked) geometry: `Q = Z^{1/2}`, `Y' = Z^{15/48}`,
  `P_a = Z^{1/8}`.

**Quantities.**
* `CS = (Σ w|ξ|²|A|²)^{1/2}(Σ w|ξ|²|B|²)^{1/2}` is the paper's step.
* `U = (Σ w²|A B|²)^{1/2}` is the uncorrelated size.
* `b_m = w ξ (q_m/Q)^{-iv} B_m` and `𝓑(χ̄_s) = Σ_m conj χ_s(−m) b_m`.
* `L = Σ_s |𝓑|²` is the twisted second moment. `D = Σ_s Σ_m |χ_s(m)|²|b_m|²` is its value
  in expectation for random `b`.
* `λ_max` is the top eigenvalue of `G_{ss'} = Σ_{m∈supp} conj χ_s χ_{s'}(m)`. It is the exact best
  constant of the coefficient-blind large sieve for this configuration, so `L ≤ λ_max‖b‖²` is the
  large-sieve prediction.
* `gramA = Σ w|A|² / Σ_m w Σ_s |a_s|² 1_{(m,s)=1}` measures the Gram excess.

**Controls (same supports and moduli).**
* `rand_c1`, `rand_c2`: `γ_2(c)` replaced by iid uniform phases per squarefree `c`. The phase is
  shared by all `n`.
* `rand_cuberoot`: `γ_2(p) ↦ γ_2(p)ω^{u_p}` with iid `u_p ∈ {0,1,2}`, extended to composite `c`
  multiplicatively. This keeps `γ_2³ = μα` and twisted multiplicativity and randomises only the
  Heath-Brown–Patterson cube-root choice.
* `A` side: `γ_1(s)` replaced by iid phases (8 draws in the ladder, 12 in the Gram study).

**Method.**
* `γ_2(p)` is computed by direct `O(p)` summation for every prime with `N ≤ 10⁶`.
  `γ_2(c)` for composite `c` comes from `γ_2(ab) = γ_2(a)γ_2(b)χ_b(a)⁴`.
* `χ_c(m)` for large `c` uses sextic reciprocity:
  `χ_c(m) = χ_c(ζ)^u · R(m',c) · χ_{m'}(c)` for `m = ζ^u m'`.
  * `χ_c(ζ) = ζ^{Σ(N_p−1)/6}`.
  * `R` is a ±1 table on classes mod 4, built from exact symbols.
  * `χ_{m'}(c)` is read from the residue tables of the row primes.
* The `B_m` loop is in C (OpenMP, 2 threads), with four weight vectors per pass.

## 2. Validation (results/b2_validate.json)

| check | range | result |
|---|---|---|
| `γ_2(p)` (C) vs `a2/eis.py` direct sum | 60 split + 4 inert primes, N ≤ 3000 | max dev 2.8e-15 |
| `γ_2(p)³ = −α(p)` | all 2265 primes N ≤ 2·10⁴ | max dev 7.3e-14 |
| composite `γ_2(c)` vs direct | 25 squarefree `c`, N ≤ 2500 | 9.0e-16 |
| `γ_1(s)` (prime + twisted multiplicativity) vs direct | 18 `s` | 5.0e-15 |
| reciprocity table `R`: a sign, a function of the classes mod 4 | 6000 prime pairs, all 144 class pairs filled | 0 violations |
| `R` on composite and non-squarefree coprime pairs | 2801 pairs, N ≤ 6000 | 0 failures |
| unit code `χ_p(ζ) = ζ^{(N_p−1)/6}` | 200 primes | 0 failures |
| kernel `B_m` vs exact-symbol direct sum (no reciprocity) | 30 rows, Z = 3000 | 5.6e-16 |
| `q_s^{-1/2}g_{χ_s}(s,−m) = γ_1(s)conj χ_s(−m)` by direct Gauss sum | 5 `s` × 5 rows | 4.6e-15 |

## 3. The bilinear ladder (results/b2_ladder_d0.json, results/b2_ladder_dl.json)

### 3.1 Geometry d0 (`Q = Z^{5/7}`, `Y' = Z^{23/56}`)

The `|S|/CS` and `|S|/U` columns are rms over 16 heights. The controls show `rand_c1` with true `A`.

| Z | Q | Y' | P_a | rows | #s | #c | `|S|/CS` true | `|S|/CS` rand_c1 | `|S|/U` true | `L/D` true | `L/D` rand_c1 | `L/(λ‖b‖²)` true | `‖B‖²`/row true / rand |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3162 | 316 | 27 | 2.31 | 570 | 7 | 896 | 0.0749 | 0.0552 | 1.23 | 1.18 | 0.94 | 0.0119 | 0.0506 / 0.0510 |
| 10000 | 720 | 44 | 2.69 | 1320 | 9 | 2826 | 0.0267 | 0.0292 | 0.69 | 0.88 | 1.13 | 0.0053 | 0.0514 / 0.0580 |
| 31623 | 1638 | 71 | 3.08 | 2964 | 23 | 8952 | 0.0217 | 0.0258 | 0.83 | 0.94 | 0.97 | 0.0062 | 0.0581 / 0.0572 |
| 100000 | 3728 | 113 | 3.43 | 6732 | 32 | 28311 | 0.0135 | 0.0171 | 0.79 | 1.03 | 1.06 | 0.0042 | 0.0544 / 0.0527 |
| 199526 | 6105 | 150 | 3.69 | 11046 | 42 | 56539 | 0.0152 | 0.0133 | 1.13 | 1.09 | 0.96 | 0.0036 | 0.0542 / 0.0546 |
| 499000 | 11751 | 219 | 4.08 | 21210 | 60 | 141358 | 0.0102 | 0.00877 | 1.06 | 0.93 | 1.02 | 0.0023 | 0.0539 / 0.0540 |

**Fitted slopes of `|S|/CS` in `log Z` (b2_fit.py).** `#rows ∝ Z^{0.713}`, so the random-phase
prediction is `−0.357`.

| B \ A | true `γ_1` | rand0 | rand1 |
|---|---|---|---|
| true `γ_2` | **−0.351** | −0.377 | −0.332 |
| rand_c1 | −0.336 | −0.343 | −0.343 |
| rand_c2 | −0.366 | −0.440 | −0.338 |
| rand_cuberoot | −0.402 | −0.366 | −0.341 |

* The true slope sits in the middle of the eleven control slopes, which range from −0.332 to −0.440.
* Per rung, `|S|/U` for the true pair is 1.23, 0.69, 0.83, 0.79, 1.13, 1.06. The controls give
  0.59–1.53.
* The s-route large-sieve bound `‖α‖(λ_max‖b‖²)^{1/2}` is 1.42–1.53 times CS in this
  normalisation. It is no better than CS, because `λ_max ≈ #rows` and the bump weights enter
  squared in `b`.

### 3.2 Geometry dl (`Q = Z^{1/2}`, `Y' = Z^{15/48}`; 5 rungs, `Z = 10⁴ … 4.99·10⁵`)

* `#rows ∝ Z^{0.505}`, so the random prediction is `−0.252`.
* True `|S|/CS`: 0.104, 0.064, 0.053, 0.047, 0.045 (slope −0.21). The eleven control slopes
  range from −0.10 to −0.34.
* For the true pair, `|S|/U = 0.84–1.11` and `L/D = 0.83–1.34`. The controls give 0.67–1.44 and
  0.60–1.43.
* This geometry has very few moduli (`#s = 5–18`) and only 180–1284 rows, so it is noisier. It
  shows the same picture.

### 3.3 What the ladder does and does not say

* **Power saving at small scale: yes, and it is the full random one.** Over the d0 range,
  `|S|/CS ≈ Z^{−0.35}` (`≈ Q^{−1/2}`). In the paper's `Z_p` units that is `ϑ ≈ 0.42`.
  BILINEAR_B2 §4 prices a hypothetical `ϑ` only up to 1/20. A finite fit is not a theorem, and
  six rungs over 2.2 decades cannot exclude a crossover at larger scales.
* **Structure-specific: no.** Every statistic of the true object is inside the control spread.
  Re-randomising only the Kummer cube roots changes nothing measurable. Neither does destroying
  `γ_2` completely. The theta row's arithmetic does not show up in the twisted first moments at
  these sizes.
* **The row norm is at its diagonal size.** `‖B‖²` per row is the same for the true and the iid
  rows (0.054). Lemma 15.1's bound `Σ|B_m|² ≪ Z^{M'+ε}` is therefore attained at the trivial
  diagonal constant here. No Patterson-type main term is visible. This fits `conj α(c)`
  removing the `X^{5/6}` term (COEFF74 / README "P": only `k = 0` has it).
* **Not shown.** Whether a different member of the fixed family (`ν_σθ ≠ 1`, ray class `σ`) or
  the marked rows `B^J` carry a coherent term. Whether the decay persists at `Z ≥ 10⁶`. Whether
  the signal part of the probe (zeros) would ever dominate. In a zero-free model it is invisible
  at these sizes.

## 4. The Gram excess (results/b2_gram.json)

The table gives `gramA − 1` (true `γ_1`), the iid-phase mean ± sd (12 draws, 8 heights) and the
z-score. The `P_a^{1/6}` and `P_a²/Y'` columns are the paper's bracket terms in (8354).

| Q | Y' | P_a | #s | true − 1 | iid − 1 (± sd) | z | `P_a^{1/6}` | `P_a²/Y'` |
|---|---|---|---|---|---|---|---|---|
| 1e4 | 100 | 1.0 | 28 | +0.0049 | −0.0011 ± 0.0043 | 1.4 | 1.00 | 0.01 |
| 1e4 | 398 | 15.8 | 119 | +0.0045 | +0.0049 ± 0.0127 | 0.0 | 1.58 | 0.63 |
| 1e4 | 631 | 39.8 | 173 | +0.0255 | −0.0003 ± 0.0100 | 2.6 | 1.85 | 2.51 |
| 3e4 | 290 | 2.8 | 82 | −0.0008 | −0.0005 ± 0.0053 | −0.1 | 1.19 | 0.03 |
| 3e4 | 486 | 7.9 | 135 | +0.0097 | +0.0005 ± 0.0051 | 1.8 | 1.41 | 0.13 |
| 3e4 | 813 | 22.0 | 230 | **+0.0381** | −0.0013 ± 0.0032 | **12.1** | 1.67 | 0.60 |
| 3e4 | 1361 | 61.7 | 384 | +0.0280 | +0.0013 ± 0.0063 | 4.2 | 1.99 | 2.80 |
| 1e5 | 316 | 1.0 | 88 | +0.0077 | −0.0002 ± 0.0015 | 5.1 | 1.00 | 0.003 |
| 1e5 | 562 | 3.2 | 156 | **−0.0123** | +0.0002 ± 0.0027 | **−4.6** | 1.21 | 0.018 |
| 1e5 | 1000 | 10.0 | 286 | +0.0054 | −0.0014 ± 0.0025 | 2.8 | 1.47 | 0.10 |
| 1e5 | 1778 | 31.6 | 501 | **+0.0413** | +0.0003 ± 0.0024 | **17.1** | 1.78 | 0.56 |
| 1e5 | 3162 | 100.0 | 894 | +0.0233 | −0.0002 ± 0.0020 | 11.6 | 2.15 | 3.16 |

All 24 cells are in the JSON. At `P_a < 1`, every `|true − 1|` is below 0.009.

* **Gauss-sum specific: yes.** The iid controls stay at `1 ± 0.003`. The true sextic Gauss
  sums give a reproducible positive off-diagonal of 2–4 % for `P_a ≳ 20`. It peaks near
  `P_a ≈ 20–30` at both `Q = 3·10⁴` and `Q = 10⁵`.
* **Size: small.** Writing the excess as `c·P_a^{1/6}` gives `c ≈ 0.01–0.025`. It does not
  grow from `P_a = 32` to `P_a = 100`, while `P_a^{1/6}` and the paper's `P_a²/Y'` term (3.16 at
  the last cell) do. So both bracket terms of (8354) are far above the measured off-diagonal in
  this range.
* **Sign.** Some cells have significant *negative* deviations (−1.2 %, z = −4.6). That is
  structure, but not a monotone "bias" term. A Galois-pair (`s`, `s̄`) coherence of the kind found
  in moments/DUAL_ANATOMY §1.2 is a plausible source. It was not dissected (HEURISTIC).
* **The dFDH reading of BILINEAR_B2 §2.4.** The data are compatible with a Gauss-sum-biased
  excess term that is present but small, and incompatible with a large one. They cannot test
  the `P_a^{1/6}` *order*.

## 5. Interpretation for B2 (PROPOSED reading of EMPIRICAL data)

* **Truth.** In the model and range tested, the quantity the B2 input needs,
  `Σ_{s≍Y'} |Σ_m w χ̄_s(m) B_m|²`, is at the diagonal size `#s·‖b‖²`. That is a factor
  `≈ #rows/#s` (here 10–350) below the large sieve. The full form is at the square-root
  (uncorrelated) size, far below CS. So a uniform `ϑ > 0` is consistent with everything
  measured. In fact the measured saving is the maximal random one.
* **No mechanism.** The saving is not carried by the Gauss-sum or theta structure. Random
  phases on the same supports reproduce it to within noise. A proof of B2 therefore cannot
  expect help from a visible arithmetic cancellation (no structured term was found to exploit).
  It needs a genuinely new bound for twisted first moments of the theta row, which is what
  BILINEAR_B2 §2.2 already identified. Equally, no structured *obstruction* to such a bound
  appears at these sizes.
* **CS is not sharp here.** The CS step is sharp only when `A_m ∝ conj B_m`. Nothing in the
  data approaches that: `|S|/CS ≤ 0.075` everywhere, and `≤ 0.015` for `Z ≥ 10⁵`.

## 6. Files

| file | content |
|---|---|
| `b2_kernel.c` | `gauss2_split` (cubic Gauss sums at split primes) and `eval_B` (theta rows via reciprocity) |
| `b2_common.py` | families (`c`, `n`, `s`, rows), exact-symbol helpers, reciprocity table, `γ_1`, `γ_2` |
| `b2_ladder.py` | bilinear ladder (`d0`, `dl`), controls, `--validate` |
| `b2_gram.py` | `‖A‖²` vs diagonal across `P_a` |
| `b2_fit.py` | log-log slopes |
| `results/b2_validate.json`, `results/b2_ladder_d0.json`, `results/b2_ladder_dl.json`, `results/b2_gram.json` | outputs (all < 40 KB) |

Reproduce, from this directory. `B2_SCRATCH` sets the build and cache directory; the first run
builds the `γ_2` table, about 4 minutes for `N ≤ 10⁶`.

```
python3 -I b2_ladder.py --validate
python3 -I b2_ladder.py results/b2_ladder_d0.json d0 3162 10000 31623 100000 199526 499000
python3 -I b2_ladder.py results/b2_ladder_dl.json dl 10000 31623 100000 199526 499000
python3 -I b2_gram.py results/b2_gram.json 10000 30000 100000
python3 -I b2_fit.py results/b2_ladder_d0.json results/b2_ladder_dl.json
```
