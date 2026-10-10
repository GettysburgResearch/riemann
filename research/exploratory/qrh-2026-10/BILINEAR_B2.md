# The low-side bilinear form of the 7/8 architecture: can a known estimate beat Cauchy–Schwarz?

```text
Status: PROPOSED assessment + IMPORTED statements (manuscript and literature) + model computation
  (FLOATING_RECONNAISSANCE for the manuscript's row counts; EXACT_RATIONAL LP certificates for the
  floor-bin barrier). Verdict: no known theorem gives a saving theta > 0 beyond Cauchy-Schwarz in
  the manuscript's ranges. No RH claim; no claim that the manuscript is correct.
Scope: the low (reflection) estimate of [OAI] Part II (Sections 6, 5, 14, 15); the payoff of a
  HYPOTHETICAL power saving Z^{-theta} in that estimate, inside the manuscript's own exponent model.
Exact sources or dependencies:
  [OAI] OpenAI, "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8" (30 Sep 2026),
        TeX source `git show pr908:standalone/2026-10-07-openai-quasi-riemann-import/upstream/
        preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`
        (pr908 = 31c706bb; file sha256 42a5ee0f...deac6a3). "TeX l. N" below = line N of that file.
        Treated as untrusted external data; unreviewed.
  [HB]  D. R. Heath-Brown, Kummer's conjecture for cubic Gauss sums, Israel J. Math. 120 (2000) 97-124
        (Theorem 2 = cubic large sieve, as quoted in [OAI] TeX l. 7491).
  [HBP] D. R. Heath-Brown, S. J. Patterson, The distribution of Kummer sums at prime arguments,
        J. reine angew. Math. 310 (1979) 111-130.
  [D]   A. Dunn, Metaplectic cusp forms and the large sieve, Algebra Number Theory 19 (2025) 1823-1880,
        arXiv:2403.13151 (Theorem 1.5 read from arXiv v4).
  [dFDH] A. de Faveri, A. Dunn, J. Hoffstein, Non-orthogonality of the cubic and quartic large sieves
        via Rankin-Selberg, arXiv:2607.07911 (July 2026; preprint, not refereed).
  [GL]  Goldmakher-Louvel quadratic large sieve; [BGL] Blomer-Goldmakher-Louvel n-th order sieve
        (both as quoted by [OAI] and [dFDH]); [DFI] Duke-Friedlander-Iwaniec, Invent. Math. 128 (1997);
        [KMS] Kowalski-Michel-Sawin, Ann. of Math. 186 (2017); [DKSZ] Dunn-Kerr-Shparlinski-Zaharescu,
        Adv. Math. 375 (2020). Statements of the last five are cited from memory or secondary quotation
        and were not re-read; nothing below depends on their exact exponents.
  Repository: THRESHOLD_CALCULUS.md (Sections 1-5), scripts/threshold_calculus.py, scripts/barrier_lp.py.
What was actually run: scripts/bilinear_b2.py (new): self-tests (exact low side reproduces 7/8 and
  11/12; agreement with threshold_calculus.low_threshold on 200 random geometries; the closure
  shortcut agrees with threshold_calculus.high_sup); exact LP barriers with rational certificates for
  theta in {0, 1/1000, 1/200, 1/100, 1/50, 1/20}; Nelder-Mead over (lx, ly, ell) of
  max(sigma_low - theta, H) with the manuscript's row counts, fine-grid re-verification.
  Literature: arXiv abstract/HTML pages of [D] and [dFDH]; ORA record of [HB].
Smallest remaining gap: an unconditional bound for the twisted first moments
  sum_m w(m) conj(chi_s(m)) B_m of the completed cubic-theta row, on average over the sextic moduli
  s ~ Y', better than the large sieve. No such bound is known; by Poisson in m it is a statement about
  the probe's own Poisson rows twisted by chi_s.
```

**RH remains unproved. Nothing here proves or disproves it.** All statements concern one external,
unreviewed proof architecture. "ϑ" is a *hypothetical* power saving; no ϑ > 0 is established.

## 0. Bottom line

1. **(IMPORTED) The form.** After an exact Mellin separation, the probe is
   `Q^{-1/2} Σ_m A_m B_m` over Eisenstein-integer rows `q_m ≍ Q = Z^{M'}`.
   * `A_m` is a smooth sum over moduli `q_s ≍ Y'` of sextic Gauss sums `g_{χ_s}(s, −m)`.
   * `B_m` is the completed cubic-theta row: normalized cubic Gauss sums `γ_2(c)` on indices
     `cn³` of norm `≍ Z^{1+ℓ'}`, twisted by the sextic symbol `χ_{cn³}(m)`.
   * The paper bounds `Σ|A_m|²` by an additive Gram bound and `Σ|B_m|²` by cubic reflection plus the
     Goldmakher–Louvel quadratic and Heath-Brown cubic large sieves. Cauchy–Schwarz in `m` combines
     them (§1).
2. **(PROPOSED) Coefficient-blind bilinear bounds cannot beat Cauchy–Schwarz here.** Every
   large-sieve-type bilinear inequality, applied to any natural splitting of the form, gives at best
   the Cauchy–Schwarz output. Most splittings give strictly worse: `ϑ` between `−19/48` and `0`
   (§2.1). A saving needs arithmetic input on *both* factors at once.
3. **(PROPOSED) No candidate applies.** Heath-Brown's cubic sieve, joint product-character sieves,
   Dunn's metaplectic bilinear sieve, Heath-Brown–Patterson Gauss-sum bilinear bounds, and
   Kloosterman-fraction or Kloosterman-sum bilinear bounds each fail on kernel shape, range, or
   level (§3). **Best provable `ϑ` from known theorems: 0.**
4. **(PROPOSED model) Payoff.** In the manuscript's own model (its row counts), a hypothetical
   uniform saving `ϑ` gives `σ(ϑ) ≈ 0.87498 − 0.8125 ϑ` for `ϑ ≤ 1/20`. The binding constraint stays
   the mid-depth row bin (`δ ≈ 0.396`, `x = 1/2`, `d ≈ h`). `13/15` needs `ϑ ≈ 0.0102`; `5/6` needs
   `ϑ ≈ 0.051` (§4).
5. **(HEURISTIC) The Gram excess looks genuine.** The manuscript's Gram excess `P_a^{1/6}` is exactly
   the bias term `A^{5/6}B^{1/3}` of [dFDH]'s conjectured sextic large-sieve norm. So even the
   `b/12` loss inside Cauchy–Schwarz is probably not removable by a better coefficient-blind sieve
   (§2.4).

## 1. The exact low-side form (IMPORTED from [OAI]; transcription checked against the TeX)

### 1.1 Notation

* `O = Z[ω]` and `q_a = |a|²` (TeX l. 566–584).
* `χ_c(a) = (a/c)_6` is the sextic symbol, extended by zero on nonunits. `χ_c²` is the cubic symbol
  and `χ_c³` the quadratic symbol (l. 626–640).
* `γ_j(c) = q_c^{-1/2} Σ_{v mod c} χ_c(v)^j e(v/c)` (l. 642). In particular `γ_2` is the normalized
  **cubic** Gauss sum. Also `g_ψ(c,k) = Σ_{d mod c} ψ(d) e(kd/c)` (l. 3359).

### 1.2 Probe and exact separation

The probe is `I_η(X,Y,Z)` (eq. `general-probe`, l. 3397–3407). Its completed row `T_{m,s,η}` is
defined at l. 3384. With `Q = q_{b*}XY` (l. 3456), Mellin inversion of the annular weight gives the
**exact** identity (eq. `low-separated`, l. 3470–3476):

    I_η = Q^{-1/2}/(2π) Σ_{σ∈T} ∫ Ŵ0(iv) Σ_{m≠0} Ω(q_m/Q) ξ(m) (q_m/Q)^{-iv} A_{m,σ,v}(Y) B_{m,σ}(Z) dv.

* **Gauss-sum factor** (l. 3461), sextic Gauss sums over moduli `s` of norm `≍ Y`:

      A_{m,σ,v}(Y) = Y^{-1} Σ_{s∈σ} W1(q_s/Y) χ_s(b*)/(τ ξ(s)) (q_s/Y)^{-1/2+iv} q_s^{-1/2} g_{χ_s}(s,−m).

  For `(m,s) = 1` and squarefree `s`, `g_{χ_s}(s,−m) = conj(χ_s(−m)) g_{χ_s}(s,1)`. So `A_m` is a
  sextic character polynomial in `m` with Gauss-sum coefficients of size `≍ Y^{-1}`.
* **Theta-row factor** (l. 3428; the central Mellin form is used):

      B_{m,σ}(Z) = Σ_θ a_θ Σ_{c sf, n} γ_2(c) conj(α(cn³)) (ν_σθ)(cn³) χ_{cn³}(m) q_c^{-1/2} q_n^{-1} V_G(q_c q_n³ / Z).

  Here `α(a) = a/|a|`, the `ν_σθ` are fixed ray characters, and `V_G` is the Gaussian with Mellin
  transform `e^{t²}`. The kernel `χ_{cn³}(m) = χ_c(m) χ_n(m)³` is sextic in `c` and quadratic in `n`.

Part II (compensated probe, eq. `compensated-probe-definition`, l. 6894; geometry (5.1), l. 6866)
applies the same separation to each rescaled slot subset `J`. There `d = Σ_{i∈J} ℓ_i`, with
`X' = XZ^{-d}`, `Y' = YZ^{-d}`, `Q = q_{b*}X'Y' ≍ Z^{M'}`, `M' = M − 2d`, `ℓ' = ℓ − d`. The marked
row `B^J_{m,σ}` (l. 8097) is completed at `Z q_{p_{J^c}} ≍ Z^{1+ℓ'}` with the marks `1_{p | cn³}`.

### 1.3 The norm of `A` (one additive large sieve each part)

* **Part I** (Lemma `balanced-additive-norm`, l. 3588). The planar additive large sieve
  (l. 3497: `Σ_{q_m≤Q}|Σ_j a_j e(m z_j)|² ≪ (Q + δ^{-2}) Σ|a_j|²`) is applied to the fractions
  `d/s`, which are `1/Y`-separated. This gives `Σ_{q_m≪Q} |A_m|² ≪ (Q + Y²)/Y`.
* **Part II** (Prop. `probe-gram`, l. 8340, eq. (8354)), with `P_a = Y'²/Q ≥ 1`:
  `Σ |A_m|² ≪ (1+|ν|)^J (Q/Y') (1 + P_a^{1/6} + P_a²/Y') Z^ε`.
  * The proof is Poisson in `m`, then complete Gauss-sum correlations.
  * The `P_a^{1/6}` term counts the *exceptional* dual frequencies `k = a⁶e`.
  * In Prop. 15.4, `P_a²/Y' ≪ P_a^{1/6}`, which gives (5.6) (l. 8610).

### 1.4 The norm of `B` (reflection, then a quadratic and a cubic large sieve)

* **Reflection.** Prop. `completed-reflection` (l. 1676; identity (l. 1763)) uses the
  Dunn–Radziwiłł cusp expansions. It turns the completed row into a dual sum over
  `μ ∈ λ^{-4}O` with kernel `V♯(q_μ X/q_c²)`, where `c = c_F · r` and `r` is the active radical.
  The residual squarefree row primes are active with exponent `j = 1`.
* **Row phase.** The row-dependent scalar is (l. 1832)
  `ζ ∝ conj(α(c))² Π_{p active} χ_p(σ_p)^{-2} ω_{p,j_p}`, with
  `ω_{p,1} = τ⁻_{p,1} τ⁺_{p,3} χ_p(ε_p)^{-3}`, a product of normalized sextic and quadratic Gauss
  sums. Its cross-prime part is `χ_p(c/p)^{2j+2}` (l. 2271). For two row primes this gives the
  cubic pair phase `(q/p)_3` (l. 7446).
* **Moving columns.** These are exactly `χ_R(nb³)³ = χ_R(nb)³`, a quadratic symbol in the residual
  row `R`, and `χ_P(n)^{-2}1_{(P,b)=1}`, a cubic symbol for the active marks `P` (l. 7466–7475).
* **Energy.** Lemma `hybrid-energy` (l. 7510, bound l. 7523) combines Goldmakher–Louvel
  (eq. (l. 2644): `Σ_a |Σ_b c_b χ_a(b)³|² ≪ (U+V) Σ|c_b|²`) with Heath-Brown's cubic large sieve
  (eq. (l. 7491): `≪ (U + V + (UV)^{2/3}) Σ|c_b|²`).
* **Result.** Lemma `reflected-energy` (l. 7747, `E_ref` at l. 7783; the norm `𝒩` at l. 7934) and
  Lemma `probe-row-norm` (l. 8111, bound (l. 8118)) give `Σ_{q_m≪Q} |B^J_m|² ≪ Z^{M'+ε}` at the
  paper geometry. In general this is `Z^{E_B(M',ℓ')}`, with
  `E_B = max(M', (2M'+1+3ℓ')/4, 2M'+ℓ'−1)` (THRESHOLD_CALCULUS §2).
* **Dual length.** The proof of Lemma 15.1 (l. 8195–8203) shows `T_d ≤ H − 3d + o(1) ≤ M'`. So at
  the paper geometry the reflected sum is never longer than the row range: the large-sieve diagonal
  `Q` is attained.

### 1.5 The Cauchy–Schwarz step (Prop. `probe-low`, l. 8564; CS at l. 8612)

    |Σ_m A_m B^J_m| ≤ (Σ|A_m|²)^{1/2} (Σ|B^J_m|²)^{1/2}
    ⇒ tuple output Q^{-1/2}[(Q/Y')P_a^{1/6}]^{1/2}[Z^{M'}]^{1/2} = r_J X'^{1/2} P_a^{1/12}  (l. 8615–8625).

There are `Z^d` rescaled tuples, each with coefficient `Z^{-3d/2}`. So the total exponent is
`lx/2 + b/12 − d` ((5.5), l. 8632), and the low estimate is `Z^{lx/2+b/12} = Z^{3/16}` ((5.10), l. 8571).

**Scales at the manuscript geometry** (`lx = 17/48`, `ly = 23/48`, `ℓ = 1/6`, `b = 1/8`,
`h = 13/16`), with exponents of `Z` at `d = 0`:

| quantity | exponent |
|---|---|
| row range `Q` (variable `m`) | `M = 5/6` |
| Gauss-sum moduli `Y'` (variable `s`) | `23/48` |
| `X'` | `17/48` |
| `P_a = Y'²/Q` | `1/8` |
| primal theta length (indices `cn³`) | `1 + ℓ = 7/6` |
| reflected dual length `T` | `T_d ∈ [1/2, 5/6]` (unmarked / all marks active) |
| Poisson dual (high-side rows `u`) | `h = 13/16` |
| CS output | `lx/2 + b/12 = 3/16` |

## 2. What a saving beyond Cauchy–Schwarz would have to be

### 2.1 Coefficient-blind inequalities reproduce CS at best (PROPOSED; elementary)

Take a bilinear inequality valid for *all* coefficients,
`|Σ_{x,y} a_x b_y K(x,y)| ≤ Δ^{1/2} ‖a‖‖b‖`. Testing with `b = δ_{y0}` forces
`Δ ≥ max_y Σ_x |K(x,y)|²`, which is at least the longer length when `|K| = 1` on coprime pairs. The
splittings of `S = Σ_m A_m B_m` give the following (exponents of `Z` for `|I| = Q^{-1/2}|S|`, `d = 0`):

| split (rows \| columns; kernel) | coefficient vectors | best `Δ` | output | `ϑ` vs CS (3/16) |
|---|---|---|---|---|
| `m` \| `s`; sextic `conj(χ_s(m))` | `w(m)B_m`; Gauss-sum weights `‖·‖² ≍ Y'^{-1}` | `≥ Q` | `≥ X'^{1/2}` = `17/96` | `≤ +1/96` (only the Gram excess; see §2.4) |
| same, with the sextic sieve `A+B+(AB)^{2/3}` ([BGL]) | same | `(QY')^{2/3} = Z^{7/8}` | `17/96 + 1/48` | `−1/96` |
| `m` \| reflected `t`; quadratic `χ_m(t)³` | `w(m)ε(m)A_m`; `b_t`, `‖b‖ ≍ 1` | `≥ Q` | `= ‖A‖‖B‖` | `0` |
| `m` \| primal `A = cn³`; sextic | `w(m)A_m`; theta coefficients | `≥ Z^{1+ℓ}` | `(1+ℓ−ly)/2 = 33/96` | `−5/32` |
| pairs `(s, cn³)` \| `m`; product character | `α'_s β_A`; smooth `w(m)` | `≥ Y'Z^{1+ℓ}` | `(1+ℓ)/2 = 7/12` | `−19/48` |
| pairs `(s, t)` (reflected) \| `m`; product character | `α'_s b_t`; `w(m)ε(m)` | `≥ Y'T` | `T_d/2` | `3/16 − T_d/2 ∈ [−11/48, −1/16]` |

So a saving beyond Cauchy–Schwarz cannot come from any large-sieve-type inequality, however sharp.
It needs *joint* arithmetic information on `A` and `B`. The CS bound is sharp exactly when
`A_m ∝ conj(B_m)`. It is beaten only if the specific Gauss-sum vector is shown to be nearly
orthogonal to the specific theta-row vector.

### 2.2 The needed input: twisted first moments of the theta row (PROPOSED reformulation)

Write `𝓑(ψ) = Σ_m w(m) ψ(m) B_m`. On coprime rows the probe is
`Σ_s α'_s 𝓑(conj χ_s)` up to fixed phases, with `|α'_s| ≍ Y'^{-1}`.

* The large sieve gives `Σ_s |𝓑(conj χ_s)|² ≪ (Q + Y') ‖B‖²`, and Cauchy–Schwarz over `s` turns
  this into exactly the CS output.
* A saving `ϑ` is therefore equivalent to `Σ_{s≍Y'} |𝓑(conj χ_s)|² ≪ Z^{-2ϑ} Q ‖B‖²` on average.
  That is cancellation in the **first moment of the theta row twisted by sextic characters**.

Opening `B_m` in primal form and applying Poisson in `m` shows what `𝓑(conj χ_s)` is: the sum
over `u` of the probe's own Poisson rows (the high side, with its `L(w, χ(u)) / L(x, ηχ(u))`
structure), twisted by `χ_s`. The additive phases cancel exactly. Opening `χ_{cn³}(m)` by Gauss sums
forces `x/A − d/s ≈ r/(As)`, and the weights `χ_s(d) conj(χ_A(x))` at the forced residues reduce to
`χ_s(−r) conj(χ_A(r))` times a fixed reciprocity character. So the unconditional input needed is
an unconditional statement about twisted averages of the very rows whose zeros the architecture
controls. (HEURISTIC; not circular, since a bound that holds unconditionally is still new information.)

### 2.3 Heuristic room (HEURISTIC)

If `A_m` and `B_m` were uncorrelated, `|Σ A_m B_m|` would be about `Q^{1/2}·rms(A)·rms(B)`. That
is a saving of `Q^{1/2}` over CS, far more than the `ϑ ≤ 1/20` modelled below. The probe also
contains the signal `Z^{C(β*)}`, so the true saving is capped by the zeros. In any case the obstacle
is proof, not truth.

### 2.4 The Gram excess `P_a^{1/6}` is probably genuine (HEURISTIC, supported by [dFDH])

[dFDH] prove `Ξ_3(A,B) ≫ (AB)^{-ε}(A + B + (AB)^{2/3})` unconditionally (their Theorem 1.1). They
conjecture `Ξ_n(A,B) = (AB)^{o(1)}(A + B + A^{1−1/n}B^{2/n} + A^{2/n}B^{1−1/n})` (their (1.9)), and
attribute the excess to Gauss-sum bias.

For `n = 6`, `A = Q` (rows `m`) and `B = Y'` (moduli `s`), the excess term is
`Q^{5/6}Y'^{1/3} = Q · P_a^{1/6}`. That is **exactly** the Gram excess of [OAI] (8354), and the
coefficients of `A_m` are Gauss sums, the biased family.

So the `b/12` inside the manuscript's low estimate is probably the true size of the factor norm. A
"better sextic sieve" would not remove it.

## 3. Candidate estimates (PROPOSED assessment; the statements quoted are IMPORTED)

| candidate | shape and hypotheses | applies here? | `ϑ` in the manuscript's ranges | exact obstacle |
|---|---|---|---|---|
| **Heath-Brown cubic large sieve** [HB, Thm 2], as a bilinear bound | `Σ_{a≤U}* Σ_{b≤V}* α_a β_b (b/a)_3 ≪ (UV)^ε (U+V+(UV)^{2/3})^{1/2} ‖α‖‖β‖`; arbitrary coefficients on squarefree indices | No | `0` at best; `−1/96` with the sextic analogue ([BGL] shape) in the `m` \| `s` split | The two factors meet only through `m`. The `m`–`s` kernel is sextic and the `m`–`t` kernel quadratic. The only cubic kernels are `χ_P(n)^{-2}` (marks vs dual, already used in Lemma 14.4) and the row self-phase `(q/p)_3` (not bilinear). Its diagonal is at least the longer length (§2.1). |
| **Joint large sieve over `m ↦ χ_s(m)χ_{cn³}(m)`** | `Σ_{(s,A)} |Σ_m c_m conj(χ_s)χ_A(m)|² ≤ Δ ‖c‖²` | Formally yes | `−19/48` (primal pairs); `−5/32` (sieve over `A` only); `−11/48` to `−1/16` (reflected pairs) | The diagonal is the number of product characters, about `Y'·Z^{1+ℓ}` (or `Y'T`), much more than `Q`. CS over pairs destroys the cancellation in the theta coefficients that the reflection exploits. |
| **Dunn** [D, Thm 1.5] | `ΣΣ_{ab≡u (v)} μ²(a) α_a β_b ρ_f(λ^{-3}ab) W(N(ab)/X) ≪ (XKN(v))^ε K^8 N(v)^4 ((AB)^{1/2} + A^{3/2}B^{1/4}) ‖μ²α‖_∞ ‖β‖_2`, `X ≍ AB`; `f` a fixed cubic metaplectic **cusp** form | No | none (`≤ 0` even for a hypothetical analogue) | (i) Our row is built from the **theta** function, which is residual and non-cuspidal; [D] treats cusp forms only. (ii) The kernel is a coefficient at a **product** `ab`; ours is a residue symbol coupling two different objects through the shared row `m`. (iii) The bound saves over the Rankin–Selberg trivial bound but lands at the large-sieve level `(AB)^{1/2}‖α‖_∞‖β‖_2`, i.e. CS level. |
| **Heath-Brown–Patterson** [HBP]; [HB] Thm 1 (bilinear sums of cubic Gauss sums) | Type II `Σ α_a β_b g̃(ab)`, reduced by twisted multiplicativity `g̃(ab) = g̃(a)g̃(b)·conj((a/b)_3)` to the cubic sieve; Type I = Kubota series | No | none | The `s`-sum in `A_m` is Type I (smooth weight, a single variable) for **sextic** Gauss sums. The reflected row carries a Gauss-sum-type phase `ε(m)` (§1.4). The CS-free form is then a Type I sum `Σ_m w ε(m) conj(χ_s(m)) χ_m(t)³` whose twist conductor `≍ Y'T ≥ Z^{47/48}` exceeds its length `Q = Z^{5/6}`. That is outside known Type I ranges (HEURISTIC: the error terms grow with the twist conductor; exponents not re-verified). Averaging over twists with a sieve returns to CS. There is no Type II factorization of `m` with separable coefficients. |
| **Kloosterman fractions / sums** ([DFI], [KMS], [DKSZ]) | `Σ α_m β_n e(a m̄/n)` and related | No | none | No Kloosterman structure occurs: the additive phases cancel exactly (§2.2). Kloosterman fractions would need an additive polynomial with non-multiplicative coefficients. |
| [GL] quadratic, [BGL] n-th order sieves | already used in the factor norms | n/a | `0` | [GL]'s `U+V` is optimal. By §2.4 the Gram excess matches the conjectured optimal sextic norm. |

**Best `ϑ` provable from a known theorem in the needed ranges: none (`ϑ = 0`).** No conditional
boundary is therefore produced by any imported estimate. §4 prices a *hypothetical* `ϑ`.

## 4. Payoff in the manuscript's own model (PROPOSED; `scripts/bilinear_b2.py`)

**Assumption B2(ϑ), the only change to the model.** In the CS step of Prop. 15.4 (l. 8612), the
bound `‖A‖‖B^J‖` is replaced by `Z^{-ϑ}‖A‖‖B^J‖`.
* The factor norms are unchanged.
* The saving is uniform in the geometry, in every rescaled subset (`d ∈ [0, ℓ]`), in `σ ∈ T` and
  in `v`.
* Hence `σ_low → σ_low − ϑ`.
* A saving measured in the row length, `Q^{-ϑ_Q}`, is the case `ϑ = ϑ_Q · min_d M'`; it is not
  modelled separately.

**Everything else is the manuscript's stated output, as in `threshold_calculus.py`:**
* row counts of Prop. 19.2;
* trivial floor bin at `a0 = 51/100`;
* `z0 = 17/50`, `t ∈ [1, 3/2]`, slope `5/6`;
* `κ = max(2β* − 1, 3/4)`;
* `ly ≥ lx`;
* the small-row condition;
* a priori bound `β* ≤ 11/12`.

For `σ0 ≤ 7/8` the high side closes iff `σ0 > H(geom) = sup{g(bin) : g(bin) ≥ a}`, with
`g = a + h(z0 − 1/6) − a·ly − ℓ/2 + xδℓ + d(R + δ/2 − z0)`. The self-tests confirm this agrees with
`threshold_calculus.high_sup`. Then `σ(ϑ) = inf_geom max(σ_low − ϑ, H)`.

The low side is exact: its bracket is convex in `d`, so the endpoints `d ∈ {0, ℓ}` suffice. It
reproduces 7/8 and 11/12 in Fractions.

| ϑ | σ(ϑ), paper counts (fine grid) | gain | gain/ϑ | binding | optimal `(lx, ly, ℓ)` | LP barrier, floor `51/100` (any counts) | LP barrier, floor `→ 1/2` |
|---|---|---|---|---|---|---|---|
| 0 | 0.874976 | — | — | bin `δ≈0.396, x=1/2, d≈h` | (0.35812, 0.47504, 0.16685) | 167/192 = 0.869792 | 13/15 = 0.866667 |
| 1/1000 | 0.874163 | 0.000813 | 0.813 | same bin | (0.35862, 0.47529, 0.16609) | 333691/384000 = 0.868987 | 3247/3750 = 0.865867 |
| 1/200 | 0.870914 | 0.004062 | 0.812 | same bin | (0.36043, 0.47647, 0.16309) | 66491/76800 = 0.865768 | 647/750 = 0.862667 |
| 1/100 | 0.866850 | 0.008126 | 0.813 | same bin | (0.36301, 0.47765, 0.15934) | 33091/38400 = 0.861745 | 322/375 = 0.858667 |
| 1/50 | 0.858727 | 0.016249 | 0.812 | same bin | (0.36738, 0.48078, 0.15184) | 16391/19200 = 0.853698 | 319/375 = 0.850667 |
| 1/20 | 0.834353 | 0.040623 | 0.812 | same bin | (0.38126, 0.48941, 0.12933) | 6371/7680 = 0.829557 | 62/75 = 0.826667 |

Readings:

* **Paper-count column (FLOATING).**
  * The geometry is optimized on a coarse grid and re-verified on a fine grid (241 × 26 × 19 bins).
  * Every entry sits about `2·10⁻⁵` above the true infimum: the `ϑ = 0` value is `0.874976`, versus
    PR 910's exact `(1507 − 2√921)/1653 ≈ 0.874957`.
  * The gains are differences and are robust.
  * The slope `0.8125 ± 0.0005` is constant over the whole range. Locally the problem is linear,
    with the same binding bin (fine-grid `δ = 0.39617`) and `R = 0.659646` throughout.
  * At `ϑ = 1/20` the prime supply `ℓ/h ≈ 0.173` is below Prop. 19.2's `7/37`. The model's
    supply-capped counts handle this (THRESHOLD_CALCULUS §7).
* **LP columns (EXACT_RATIONAL).** These are barriers for *any* row counts (floor bin + low rows
  shifted by `ϑ`), with certificates. At floor `→ 1/2` they reproduce `13/15 − 4ϑ/5`. At `51/100`
  the slope is about `0.805`. The paper-count values lie above them, as they must.
* **Thresholds (FLOATING).** In the paper-count model, `13/15` would need `ϑ ≈ 0.0102` and `5/6`
  would need `ϑ ≈ 0.051`.
* **Lemma-range obligations for `σ0 < 7/8`.** These are inherited from THRESHOLD_CALCULUS §7:
  * Lemmas 10.3–10.5 and the Euler region (7.15) are stated for `σ0 ≥ 7/8`;
  * Lemma 18.1 is used at `κ = 3/4` while the actual `2β* − 1` would be smaller;
  * Lemma 15.1's proof assumes `M + ℓ = 1`; the model uses the LP closed form instead.

  The a priori bound `β* ≤ 7/8` (Part II accepted) was rechecked at the `ϑ = 1/20` optimum; see the
  script output.

## 5. Verdict

1. **(PROPOSED) No `ϑ > 0` is provable from a known theorem in the manuscript's ranges.**
   * Large-sieve-type bilinear inequalities, including Heath-Brown's cubic sieve, [BGL], joint
     product-character sieves and [D]'s metaplectic sieve, cap out at the CS level (§2.1).
   * Gauss-sum bilinear technology ([HBP], [HB]) and Kloosterman technology ([DFI], [KMS], [DKSZ])
     have no matching structure (§3).
2. **(HEURISTIC) Even the in-CS Gram excess is probably genuine** (§2.4, [dFDH]).
3. **Conditional boundary.** Assume all of [OAI]'s stated lemma outputs (unreviewed), the
   lemma-range extrapolations listed in §4, and the *hypothetical* B2(ϑ). Then the architecture
   would give `σ(ϑ) ≈ 0.87498 − 0.8125ϑ` (`ϑ ≤ 1/20`, FLOATING). Since no imported estimate supplies
   `ϑ > 0`, the boundary justified by known theorems stays the manuscript's `7/8` (model `0.87496`).
4. **The input that would move it** is a sub-large-sieve bound for the twisted first moments
   `Σ_m w(m) conj(χ_s(m)) B_m` on average over `s ≍ Y'` (§2.2). By Poisson this is a twisted average
   of the high side's own rows. It lies outside every tool surveyed here.

## 6. What this note does not show

* It does not review the manuscript's reflection, Gram or energy lemmas. They are transcribed and
  used as stated.
* The §2.1 table is a statement about coefficient-blind inequalities on the listed splittings. It
  is not a theorem that no clever rearrangement exists.
* The Type I range claim in §3 (HBP row) is HEURISTIC.
* [dFDH] is a 2026 preprint, and its `n = 6` statement is a conjecture.
* The model values are FLOATING_RECONNAISSANCE. Only the LP columns are exact.
