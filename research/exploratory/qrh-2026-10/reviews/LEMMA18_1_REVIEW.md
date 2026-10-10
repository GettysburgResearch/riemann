# Bounded review: Lemma 18.1 (`lem:plain`, "Fourth moment with short prime factors") of the OpenAI 7/8 manuscript

```text
Status: REVIEW (bounded; external manuscript) + EMPIRICAL checks
Scope: Lemma 18.1 of "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8" (OpenAI,
  30 Sep 2026, unreviewed). Statement (paper.tex l. 12477-12601) and proof (Sec. 18.1-18.8,
  l. 12602-14973), read with the focus on case 1 (z = 0). Reconstructed: the reductions,
  the induction order, the comparison/centering step, both finite Poisson transforms in the
  coprime squarefree model, the Gauss-row enlargement, the width-decrease identity, the
  exceptional (Theta) row count and centered lattice cancellation, and the loss bookkeeping of
  Sec. 18.8. Checked mechanically: 14 displayed exponent identities and local inequalities, and
  the prime-power Gauss formula. NOT checked line by line: the complete-common-support
  allocations of both transforms (l. 13192-13349, 13686-13933), Lemmas smooth-calculus,
  kernel-seminorms and logarithmic-control (l. 1123-1600), the positive-slot amplifier and
  greedy slot removal (case 2) beyond its ledger, and the downstream use in Prop. 19.2.
Exact sources or dependencies:
  pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6; file standalone/2026-10-07-openai-quasi-riemann-
    import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex
    (sha256 42a5ee0f...deac6a3). All line numbers below refer to this file.
  Prior flag: origin/claude/openai-math-riemann-analysis-w5copg,
    standalone/2026-10-07-openai-quasi-rh/README.md, Sec. 8 item 5.
  Literature (abstract-level unless stated): Heath-Brown, cubic large sieve (Israel J. Math. 2000);
    Baier-Young, arXiv 0804.2233 (J. Number Theory 2010); Blomer-Goldmakher-Louvel, arXiv 1112.1650
    (n-th order large sieve, second moment; sextic statements read as quoted in Gao-Zhao 2201.01885);
    Gao-Zhao arXiv 2201.01885 (Thm 1.1, Lemma 2.9, Cor 1.4 read via ar5iv) and arXiv 2104.09909;
    David-de Faveri-Dunn-Stucky arXiv 2410.03048; Diaconu-Ion-Pasol-Popa arXiv 2607.27131;
    Dunn-Radziwill arXiv 2109.07463 (Ann. of Math. 200 (2024)).
  Numerics reuse numerics/eisenstein.py unchanged (sha256 bc6af658...e584ae9, w5copg copy).
What was actually run (one process at a time on the shared machine):
  python3 -I lemma18_ledger.py   -> 14/14 PASS (sympy identities + exact Fraction local tables)
  python3 -I lemma18_local.py    -> 283 prime-power Gauss sums vs eq:gauss-local, max rel dev 2e-16
  python3 -I lemma18_moments.py results/lemma18_bal.json 1e3,3e3,1e4,3e4,1e5,3e5 bal 65536
  python3 -I lemma18_moments.py results/lemma18_sq.json 1e6,3e6 sq 131072           (205 s)
  python3 -I lemma18_moments.py results/lemma18_long.json 1e3,3e3,1e4,3e4 long 8192  (30 s)
  python3 -I lemma18_moments.py results/lemma18_long_1e5.json 1e5 long 8192          (321 s)
  (A first `bal` run that also attempted K = 1e6 was stopped; its K <= 3e5 output is the
   lemma18_bal.json kept here.)
Smallest remaining gap: no error found, but the full common-support bookkeeping was not verified.
  The first step not independently verified is the first transform with nontrivial common support
  (l. 13192-13349). This covers the complete extraction of C, D, the artificial coprime extension
  with the Moebius label s, and the separation of the kernel and inverse roots before
  Cauchy-Schwarz, which must keep the centered coefficient intact. The target (old-eq:2.5)
  with its -s_0 and B_c terms rests on these steps. The same applies to the second-transform
  analogue (l. 13686-13933). Case 1 would be a new theorem (Section 1), so it needs a complete
  expert line check before Prop. 19.2 can be relied on.
```

RH is unsolved. This note does not prove or disprove any zero-free region. It does not certify
Lemma 18.1. The numerics in Section 4 are EMPIRICAL. A finite range is not a theorem.

## 0. The statement under review

Paper.tex l. 12531-12579. The rows are elements `k ∈ O = Z[ω]` with `0 < N k ≪ Z^m`, and
`ψ_k(n) = τ(n) χ_n(k)`. The plain polynomials are `S_ψ(n; W) = Z^{-n/2} Σ_l ψ(l) W(N l / Z^n)`,
with `l` running over all ideals, not only squarefree ones. `M = m + q`. The claim is

    Σ_{k ∈ R_z} |S(n1) S(n2) Q|² ≪ Z^{M+ε}.

There are two cases:

* **Case 1** (`z = 0`, `R_0` = nonprincipal rows): there is no restriction on the lengths `n1, n2`.
* **Case 2** (`z > 0`, `R_z` = rows whose inducing character is outside `Θ`): requires
  `n1 + n2 + 6κz ≤ M`, `κ ∈ [3/4, 1]`, and `β_* ≤ (1+κ)/2` when `κ < 1`.

The lemma feeds the plain-witness counts of Prop. 19.2 (`prop:detector-counts`, l. 15185; uses at
l. 15106-15441). It is used only for the 7/8 result, not for 11/12.

**What case 1 says.** By Mellin inversion, `S_ψ(n) = (2πi)^{-1} ∫ L(1/2+s, ψ) Z^{ns} W̃(s) ds`.
With `q = 0` and `n1 = n2 ≈ m/2`, case 1 is therefore a Lindelöf-on-average **fourth moment**:

    Σ_{N k ≤ K} |L(1/2+it, χ_·(k))|⁴  ≪ K^{1+ε}   (smoothed, t bounded),

The sum is over the full sextic family, about `3.6 K` rows with conductors up to `≍ K`. The family
includes the thin quadratic-type (`k = t c³`) and cubic-type (`k = t c²`) subfamilies, with
multiplicity `(K/N c)^{1/6}` from sixth powers. Two remarks:

* Under GLH for this family, case 1 is immediate, because `S ≪ Z^ε` pointwise. It is
  unconditional only if the proof below is correct.
* The `n2 = 0` sub-case is a second moment.

## 1. Literature context

| result | family | moment / tool | strength | conditional? |
|---|---|---|---|---|
| Heath-Brown 2000 | cubic symbols over Q(ω), squarefree | large sieve `(M+N+(MN)^{2/3})(MN)^ε‖a‖²` | conjectured `M+N` | no |
| Dunn-Radziwiłł, Ann. Math. 2024 (2109.07463) | cubic | the `(MN)^{2/3}` term is **sharp up to X^{o(1)} for general coefficients** | — | **under GRH** (abstract) |
| Blomer-Goldmakher-Louvel (1112.1650) | n-th order Hecke, K ⊃ μ_n | large sieve for n-th order characters; second moment | sextic large sieve of the same shape as Heath-Brown (quoted as Gao-Zhao Lemma 2.9); `Σ|L(1/2,χ_c)|² ≪ y^{1+ε}` for sextic, squarefree `c` (quoted as BGL Cor. 1.4 by Gao-Zhao) | no |
| Baier-Young (0804.2233, JNT 2010) | cubic Dirichlet chars over Q | 1st moment asymptotic; `Σ|L(1/2,χ)|² ≪ Q^{6/5+ε}`; cubic/sextic large sieve over Q | upper bound | no |
| Gao-Zhao (2201.01885) | sextic Hecke over Q(ω), squarefree `c ≡ 1 (36)` | 1st moment `A Ŵ(1) y + O(y^{6/7+ε})`; 1-level density | asymptotic | density/non-vanishing under GRH |
| Gao-Zhao (2104.09909) | cubic & quartic Dirichlet | all moments `k ≥ 0` | sharp upper bounds | **GRH** |
| David-de Faveri-Dunn-Stucky (2410.03048) | cubic Hecke over Q(ω), squarefree `q ≡ 1 (9)` | mollified 2nd moment asymptotic with power saving; Lindelöf-on-average 2nd moment of cubic Dirichlet series; positive-proportion non-vanishing | asymptotic | no |
| Diaconu-Ion-Paşol-Popa (2607.27131, 29 Jul 2026) | r-th order Hecke, r ≥ 3, fields ⊃ μ_{2r} | asymptotics for 1st and 2nd twisted moments (multiple Dirichlet series) | asymptotic | no condition stated in the abstract |

Consequences for case 1:

* **Second moment.** The `n2 = 0` analogue is essentially known for squarefree sextic moduli
  (BGL). Via the large sieve with `N = √K` it is of Lindelöf strength, since `(MN)^{2/3} = K`.
  Lemma 18.1 extends it to all rows and to moving twists. That is a mild extension.
* **Fourth moment.** No unconditional Lindelöf-on-average fourth moment for any cubic, quartic or
  sextic family was found.
  * The BGL/Heath-Brown large sieve at `M = N = K` gives only `K^{4/3+ε}`.
  * The 2026 multiple-Dirichlet-series paper stops at the second moment. Its hypothesis
    `K ⊃ μ_{2r}` excludes the sextic family over `Q(ω)`, since `r = 6` would need `μ_12`. That
    reading is from the abstract only.
  * Conditionally, GLH gives case 1 trivially. GRH gives sharp moment bounds by the
    Soundararajan-Harper method; this is proved for cubic/quartic Dirichlet families (Gao-Zhao).
    The sextic Hecke analogue was not located, though it is expected to go through.
  * **Case 1 would therefore be a new unconditional result.** It goes beyond the sextic large
    sieve (BGL) and is the first of its kind for a higher-order family.
* **Dunn-Radziwiłł.** Their result does not refute case 1. It concerns general coefficients
  (essentially Gauss-sum-type ones) and is conditional on GRH. Section 2 explains where the
  proof uses the special structure of the coefficients: every child is again a product of two
  smooth Hecke-character sums, so it can be reflected.

## 2. Structural reconstruction of the proof

**2.1 Reductions (l. 12602-12830).**

* Fixed extra masks are erased by Möbius inversion with `Z^ε` mass (old-eq:2.1a-2.1b).
* Each plain factor longer than `M/2` is reflected once by the primitive Hecke functional
  equation: `C_k = 3Q_k/(2π)²`, gamma quotient `Γ(s)/Γ(1-s)`, root number of modulus one.
* The conductor bound is `C_k q_{R_0,k} ≪ Z^M` (old-eq:2.1c). It holds because the sextic
  characters are tame at good primes, and the S-part is a finite ray family.
* This leaves the *padded zero-slot core*: `n_i ≤ M/2 + ξ`, `A = n1 + n2 ≤ M + δ` (old-eq:2.1h).
* Row-dependent reflected scales are handled by a rowwise supremum over `O((log Z)²)` unit boxes.

The reflection formula and its constants are standard, and the formula as written is correct.

**2.2 Induction order (l. 12903-12938, 14779-14807).**

* Induction is on the width `M`, in bands of length `σ/4`. All zero-slot bands come first, then
  the positive-slot bands.
* Within a band, `A ≤ 5M/6` is proved first, uncentered. Then the rest of the core is proved by
  centering, then the rest of the lengths by reflection.
* Base case: at `M ≤ ρ`, counting absolutely gives `Z^{m+A} ≤ Z^{M+ρ+δ}`. This uses `A ≤ M + δ`
  from the reflection.

**2.3 Comparison and centering (l. 12940-13010).**

* Set `L = M/4`. If `A > 5M/6` and one plain is shorter than `L`, reflect the other.
* Otherwise subtract the comparison rectangle `(Y1, Y2) = (Z^L, X1X2/Z^L)`, which has the same
  product of scales. Bound the comparison separately after reflecting its long factor:
  `A_comp ≤ 3M/2 - A + ξ ≤ 2M/3 + ξ` (z = 0), or `≤ 23M/30` and `A_comp + (6κ-1)z ≤ 14M/15`
  (z > 0).
* The difference `Δ_k` is then extended to the full smooth row ball by positivity.

I checked these margins (`lemma18_ledger.py`). The maxima are `1063/1400 < 23/30` and
`647/700 < 14/15` on the grid.

**2.4 First transform (l. 13114-13409).**

Poisson in the row `k` runs modulo the full product of both column variables (old-eq:first-poisson-bridge).

* **Zero frequency.** It needs every exponent `≡ 0 (mod 6)`, so the product is powerful. Its
  contribution is `O(Z^{m+ε})`.
* **Nonzero frequencies.** These give `Z^{m-A}` times a bilinear form in Gauss sums.
* **Cauchy-Schwarz in `h`.** This leads to the Gauss-row norm
  `N_C = Σ_{h ~ Z^K} |Z^{-(A-c)/2} Σ_a A_C(a) G(a,h)|²`, with
  `K ≈ K_0 = 2A - c - d + R + E - m`.
* **Target.** `N_C ≪ Z^{A-c+q̃+B_c-s_0+ε}` (old-eq:2.5). The ledger closes by
  `B_c + B_d ≤ c + d - 2p - R` (old-eq:2.6). I verified this prime by prime for all
  `1 ≤ j ≤ i < 200`.
* **Coprime squarefree model.** I re-derived the normalization `H/(X q_e √q_r)` and the phase
  `\overline{R(a,b)}` by hand in this case.

**2.5 Gauss-row enlargement (l. 13411-13594).**

* By positivity, the `h`-ball is enlarged from length `K` to `K + g`, with `g = J_+ + σ`. In the
  zero-slot case there is no amplification.
* In the positive-slot case only, an amplifier `h → hp⁶` over a prime pool of size `Z^{σ/3}` gains
  `Z^{-ℓ}`. I checked the local valuation `1, 6, 7` coefficients against Lemma
  `prime-power-fourier`.

**2.6 Second transform (l. 13596-14310).**

* Poisson in `h` (Lemma full-correlation) gives the exact `F(u,v;j)`.
* **Diagonal** (`j = 0`): `F(u,u;0) = φ(u)`, which gives `Z^{K+g-ℓ-s_0}`. The excess over the
  allowance is `A - M + 5σ/3 + δ_fr` (old-eq:2.12; the identity was checked symbolically). This is
  the "columns" term. It is harmless only because `A ≤ M + δ` after reflection.
* **Off-diagonal.** Complete common-support extraction produces two independent *children*, at
  row width `m' = 2a_0 - K - g - g_2 - V` and total width
  `M' = m' + q' = M + J - g - g_2 + t_2 ≤ M - σ` (old-eq:2.13; checked symbolically). Their allowed
  exponent is `M' + Δ_child`, with `Δ_child ≥ w + ℓ` (old-eq:2.14).
* I re-derived each line of the exponent table at l. 13846-13855 and its sum at l. 13861.
* I re-derived the local correlation bounds (l. 13742-13751) from `eq:correlation-local`.
  * Unit, equal multiplicity: `P^{i-1}`.
  * Nonunit: `P^{i-1}(P-1) ≤ P^i`.
  * Unequal: `P^{j_0-1}(P-1)`.
  * These justify the factor `Z^{g_2 - t_2}`.

**2.7 Rows of the child whose inducing character lies in Θ (l. 14312-14777).**

* **Count.** Membership in Θ forces `v_p(h')` into one residue class mod 6 at every good prime
  (Kummer theory and reciprocity). So `(h') = h_0 v⁶`, and the count is
  `≪ Z^{(m'-f)/6+ε}` (eq:exceptional-row-count).
* **Uncentered exceptional excess.** Bounding these rows by volume gives the excess
  `A - 5M/6 - F_1 - F_2` (old-eq:2.15-2.16; identity checked), with
  `F_1 ≥ 2(c+w)/3 - 3σ` and `F_2 ≥ 2b_2/3` (old-eq:2.17; the `F_2` table was re-derived from the
  definition and checked for `i < 120`). **This is the origin of the `A ≤ 5M/6` threshold:**
  sixth-power rows are sparse, about `Z^{M/6}`, while each can be as large as the volume `Z^A`.
* **Centered case.** In the centered case the two rectangles share character, mask and norm power
  (`lem:centered-coefficient-invariant`). So the volume main terms `c² T^{1+it} I_1 I_2`, which
  depend only on `T = X1X2 = Y1Y2`, cancel. What remains is `T Z^{-r}` with `r = (L - v)_+`
  (lem:centered-lattice-cancellation; its proof is standard lattice Poisson plus Möbius, and I
  found nothing wrong).
* **Deficit.** The resulting deficit is `A - 5M/6 - 2v/3 - (L - v)_+ ≤ (A - M)_+ ≤ δ`
  (old-eq:2.19; checked on a grid).
* **No slack.** The numerology is tight at three points:
  * equality holds at `v = L` in (2.19);
  * `F_2 = 2b_2/3` holds exactly at nonunit primes of multiplicity one, where the paper keeps the
    weaker count with `f` instead of `2f`;
  * `F_1 ≥ 2c/3` is tight when `J < 0`.

  Any further loss at these points would break the centered stage.

**2.8 Completion (l. 14779-14973).**

* Each strict call lowers the width by at least `σ/2` after the `C_*ξ` clipping and frequency
  errors. So the depth is at most `D - 2`, with `D = 2 + ⌈2M_max/σ⌉`.
* Errors combine as follows. One terminal loss `T_term = ρ + δ + ρ/6 + 3σ + 5σ/3` occurs per
  branch. Each edge costs `C_*(η + ξ + ε_0)`, with `ξ, η, ε_0 < ε/(16 C_* D)`.
* The terminal (diagonal and exceptional) losses are a maximum, not a sum along the branch.
  I found this accounting consistent.

### Where the saving comes from; termination

* **The two transforms extract no cancellation.** They compose to the identity up to the positive
  enlargement `g`. In the coprime squarefree model the recursion reads

      Σ(M) ≲ Z^m (1st zero freq.) + Z^{A+g} (2nd diagonal) + Z^g Σ_child(M-g) + (Θ rows).

  This is Heath-Brown's recursive large-sieve mechanism.
* **Why the recursion closes here.** Every child is again a product of two plain sums of a Hecke
  character, with conductor `≤ Z^{M'}`. So the child can be **reflected** to total length
  `≤ M' + δ`. This keeps every stage in the "columns ≤ rows" regime, where the diagonal
  `Z^{A+g}` costs only the one-time loss `g ≈ σ`. For general coefficients the same recursion
  leaves an uncontrolled columns term `Z^g N`, which is where `(MN)^{2/3}` comes from.
* **The genuine power savings are arithmetic counts.** These are:
  * the powerful-product zero frequency;
  * the sparsity of sixth-power exceptional rows (the `5M/6` threshold);
  * the centered lattice cancellation `Z^{-r}`, with `r` up to `L = M/4`. It covers the remaining
    excess `A - 5M/6 ≤ M/6 + δ`.
* **The width strictly decreases.** `M' - M = J - g - g_2 + t_2 ≤ -σ`, since `g ≥ J + σ` and
  `g_2 ≥ t_2`. The induction terminates.
* **Remark, not checked.** A rough version of the same numerology for the cubic family (threshold
  `2M/3`, comparison length chosen in `[A - 2M/3, (A - M/3)/2]`) is not obviously infeasible
  when the extraction terms are ignored. If the scheme is sound, it might also bear on the open
  cubic fourth moment. That raises the stakes of a line-by-line check. The cubic `F_1, F_2`
  analogues were not worked out.

### First step I could not verify

**l. 13192-13349.** This is the nonzero-frequency bridge with nontrivial common support. It covers:

* the allocation of each common prime's valuations to plains and slots, with freezing;
* the artificial residual summand `C_1` with the full Möbius sum over `s`;
* the claim that one Fourier coefficient measure separates the coupled kernel
  `Φ̂_1(H q_h/(q_e q_r q_a q_b))` and the inverse roots. That measure must be common to all live
  labels and to both rectangles, so that the centered coefficient `D_b` and a single whole-product
  norm power survive into `N_C`.

The target (old-eq:2.5), including its `-s_0` and `B_c` terms, depends on these. I checked only
the coprime squarefree instance and the exponent ledgers, and found no error. The second-transform
analogue (l. 13686-13933) and the supporting Lemmas `smooth-calculus` and `kernel-seminorms` were
likewise not verified.

## 3. Verdict

**Cannot tell. The proof is structurally plausible, and no concrete gap was found in what was
checked.**

* The architecture is coherent. The width decrease, the `5M/6` threshold, the centered cancellation
  and the loss accounting all check out at the level of the displayed exponents, with zero slack
  at the tight points listed in 2.7.
* The decisive analytic input is reflection of every child. This is compatible with
  Dunn-Radziwiłł, since it uses structure that general coefficients lack.
* Case 1 would be a new unconditional fourth-moment theorem for a higher-order family. A result
  of that weight should not be relied on, including for Prop. 19.2 and thus the 7/8 claim, until
  an expert has checked the common-support bookkeeping of Sections 18.4-18.6 line by line.

## 4. EMPIRICAL check of case 1 on the actual sextic family

**Setup.**

* Exact sextic symbols (`numerics/eisenstein.py`; its self-test passed).
* `τ = 1`, `S = {(2), (λ)}`.
* Columns: all ideals prime to 6, including non-squarefree ones, with `χ_l(k) = Π χ_p(k)^{v_p(l)}`
  zero-extended.
* Rows: all elements `0 < N k ≤ K`.
* Weight: `W(y) = exp(4 - 1/((y-1)(2-y)))` on (1,2).
* `R_0` excludes the rows `k = t c⁶` with `χ_·(t)` trivial.

**Statistics.**

* The reported mean is `Σ_{R_0} |S_k(N1) S_k(N2)|² / #rows`.
* `ratio` divides it by the exact generalized diagonal
  `Σ_{l~l'} a_l a_{l'} Π_{p|ll'}(1 - 1/Np)`.
* `princ/R0` is the contribution of the excluded principal rows relative to the `R_0` sum.

**Results (`results/*.json`).**

| K | rows | (N1, N2) | mean over R_0 | ratio to diagonal | principal / R_0 |
|---:|---:|---|---:|---:|---:|
| 1e4 | 36 294 | (100, 100) = \|S(√K)\|⁴ | 0.01327 | 0.985 | 0.015 |
| 3e4 | 108 786 | (173, 173) | 0.01308 | 0.997 | 0.012 |
| 1e5 | 362 796 | (316, 316) | 0.01398 | 0.998 | 0.011 |
| 3e5 | 1 088 346 | (548, 548) | 0.01374 | 0.998 | 0.015 |
| 1e6 | 3 627 558 | (1000, 1000) | 0.01399 | 0.999 | 0.018 |
| 3e6 | 10 882 656 | (1732, 1732) | 0.01403 | 0.997 | 0.022 |
| 1e4 … 3e5 | | (K^{1/4}, K^{3/4}) | 0.0035 … 0.012 (window-dependent) | 0.993 – 1.000 | 0.02 – 0.03 |
| 1e3 | 3 642 | (K, K) | 0.01387 | — | 7.2 |
| 1e4 | 36 294 | (K, K) | 0.01244 | — | 120 |
| 1e5 | 362 796 | (K, K) | 0.01257 | — | 1192 |

**Reading.**

* **|S(√K)|⁴.** The balanced fourth moment is flat. The fitted exponent between 1e4 and 3e6 is
  about +0.01. It equals the diagonal to within 1.5% at every `K ≥ 1e4`.
* **Large sieve comparison.** The large sieve bound `K^{1/3}` would mean a factor of about 6.7 over
  this range. Nothing of the sort appears, but that is an upper bound and is not expected to be
  attained.
* **Second moment.** `mean |S(K)|²` is 0.0807, 0.0824, 0.0783, 0.0781, 0.0785 for `K = 1e3 … 1e5`.
* **Long lengths `N1 = N2 = K`.** These are beyond the padded core and need reflection. The
  moment is also flat, at about 0.0125.
* **Structured subfamilies.** The quadratic-type, cubic-type and bounded-conductor rows carry at
  most a few per cent of the `R_0` sum, and their share falls with `K`. The top 10 rows carry
  `< 0.1%` at `K ≥ 1e6`.
* **Principal rows.** Excluded from `R_0`, they are already about 2% of the `R_0` sum at `A = m`,
  and their share grows. At `A = 2m` they dominate by a factor growing like `K^{1.1}` over the range (the volume count predicts `K^{7/6}`). This is the
  `Z^{m/6+A}` volume effect behind the `5M/6` threshold and the need for centering: on the full
  row ball the claimed bound is false for `A > 5M/6`.

**Limits.** These numbers are consistent with case 1 and with GRH-type heuristics. They do not test
the proof. They cannot distinguish `K^ε` from a constant, and they cannot rule out effects beyond
`K = 3·10⁶`. They are floating point and not certified.

## 5. Files

* `lemma18_ledger.py` checks the exponent identities and local inequalities (14/14 PASS).
* `lemma18_local.py` spot-checks `eq:gauss-local` with exact symbols.
* `lemma18_moments.py` computes the empirical moments.
* `results/lemma18_bal.json`, `results/lemma18_sq.json`, `results/lemma18_long.json` and
  `results/lemma18_long_1e5.json` hold the raw outputs.
