# O3: feeding the Oct 5 Möbius mean square into the Sep 30 architecture

```text
Status: NEGATIVE for the stated target (no half-plane below 7/8 obtained), with exact smallest
  statements and exponents. Labels per claim: PROVED-HERE (short algebra/logic written out, resting on
  IMPORTED manuscript identities), PROPOSED (reading of unreviewed manuscripts), CONDITIONAL, OPEN.
Scope: the exponent architecture of two external, unreviewed manuscripts (OpenAI, "Quasi-RH ... 7/8",
  30 Sep 2026 = [S30]; "... 11/12", 5 Oct 2026 = [O5]). Nothing here is about RH directly; RH and every
  half-plane below remain unproved. Any half-plane quoted is CONDITIONAL/IMPORTED.
Exact sources or dependencies: [S30] = scratchpad/paper_sep30.tex (16677 lines; line numbers below refer
  to it); [O5] = scratchpad/paper2.tex (3988 lines); ../../THRESHOLD_CALCULUS.md, ../../RUNG_STRENGTH.md,
  ../../AGENDA.md (B1, A1), ../../scripts/{threshold_calculus.py, barrier_lp.py} (imported unchanged);
  parallel branch origin/claude/riemann-hypothesis-research-3va81h, quasi-rh-wave FINDINGS.md and
  notes J, N, P, Q (read, not re-derived).
What was actually run: scripts/o3_barriers.py (exact rational LP certificates, Fractions; results/
  o3_barriers.json); scripts/o3_theta_opt.py and scripts/o3_b0_slice.py (Nelder-Mead
  re-optimisation of the imported threshold_calculus model with a Gram-loss dial and on the b = 0
  slice; floating point, finite; results/o3_theta_opt*.json/log, results/o3_b0_slice.json).
  About 2 CPU-minutes, single-threaded. No numerics on the sextic family itself.
Smallest remaining gap: the non-alignment statement (NA) of Section 2.3: a saving Z^{b/12} beyond
  Cauchy-Schwarz in the pairing of the sextic-bias (exceptional) component of the additive polynomial
  with the cubic-theta row. (NA) is NOT an instance of any Oct 5 mean square.
```

RH remains unproved. Both manuscripts are external and unreviewed.

## 0. Bottom line

* **No half-plane below 7/8 was obtained.** The best value stays at the imported
  `σ0 = 0.874957…` (Liu's re-optimisation; PR 910's closed form `(1507 − 2√921)/1653`), or `7/8`
  as stated in [S30]. That is CONDITIONAL/IMPORTED, and this note does not move it.
* **The premise fails at step (1), at a specific identity.** The sum carrying the `P_a^{1/6}` loss
  (the Gram sum of [S30] Prop. 15.2) is not a Möbius family. Its column coefficient is the
  **square of the cubic Gauss sum** (Prop. O3.1). After Poisson in the row variable its dual
  is the **plain** family, coefficient class `θ⁰` (Prop. O3.2). The `P_a^{1/6}` term is exactly
  the contribution of that plain family's sixth-power ("principal") rows. These rows are the
  analogue of [O5]'s rows `u = p⁶`, but they carry a plain sum `Σ 1` (size `N`, no cancellation)
  where [O5] has the Möbius sum `A_1(D)`. Möbius cancellation, which drives [O5], has nothing to act
  on here.
* **The [O5] mean square is already inside [S30].** [S30] Lemma 17.1 with no slots (`z = 0`)
  states `Σ_{q_u ≪ Z^m} |M_u(Z^r)|² ≪ Z^{m+ε}` for `r < m`. That is the [O5] Prop. 2.1 shape
  (rows > columns, Möbius × sextic, finite-order `ν`), and it is used in the Part II row counts.
  The general sextic large sieve (Lemma 9.1, `(KD)^{2/3}` term) feeds only Part I's row envelope.
* **Best CONDITIONAL value if the first unverified substitution held.** Grant the non-alignment
  statement (NA) of §2.3 (saving `Z^{b/12}`). The imported model then reaches
  `σ0 = 926/1077 ≈ 0.859796`. This number is an exact LP barrier, and the model optimum
  `0.859811` matches it to `1.5·10⁻⁵` (floating point, finite). The parallel branch's fuller
  model gives `0.86395`. (NA) is not supplied by [O5] or by any known theorem.
* **Steps (3) and (4) also fail, and each failure is located.** The "all rows minus non-floor
  rows" variant of the floor bin is a rearrangement of the identity used for the contradiction
  (Prop. O3.3). Every mean-square (unsigned) treatment of the floor rows stops at the triangle
  bound (Prop. O3.4). Lemma 18.1 is a plain-coefficient fourth moment and cannot give PR 910's
  `Mom(2, h)` with `h < 2` for the Möbius family (§4). Exponents for each are in §§2–4.

## 1. Step (1): where [S30] pays for a sextic sieve, and what the coefficients are

### 1.1 Inventory (PROPOSED reading of [S30])

| place in [S30] | sum | coefficient class | used in Part II? | general sextic sieve? |
|---|---|---|---|---|
| Prop. 15.2 (l. 8340–8557), Gram bound `(Q/Y′)(1 + P_a^{1/6} + P_a²/Y′)` | `Σ_{q_m≪Q} \|A_m\|²`, `A_m = Y′^{-3/2} Σ_s c_σ(s) W₁ r_s^{-1+iv} g_{χ_s}(s,−m)` (l. 3461, 8366) | column: sextic Gauss sum `γ₁(s) = G(s)γ₂(s)²` (Prop. O3.1); dual: **plain** (Prop. O3.2) | yes, via Prop. 15.3 (l. 8564–8650): the `b/12` loss | no. It is an additive Gram bound; its `P_a^{1/6}` term is the conjectured `n = 6` sieve term `M^{5/6}N^{1/3}` |
| Lemma 9.1 (l. 4707–4717), `K + D + (KD)^{2/3}` | inverse witness `Σ_k \|Σ_n c_n χ_n(k)\|²` | arbitrary `c_n` (applied to Möbius) | **no**: only Prop. 9.2, which feeds §10.5 (l. 5921) and the 11/12 conclusion (l. 6621) | yes |
| Lemma 14.2 (l. 7510–7531), `{N + L + (NL)^{2/3}}` | reflected energy | cubic-theta coefficients, class `θ = ᾱγ₂` | yes (Lemma 14.3 → 15.1) | cubic, not sextic; the coefficient class is not Möbius |
| Lemma 17.1 (l. 9250–9275) | `Σ_u \|M_u(Z^r)Q_u\|²` | **Möbius × sextic** (the [O5] shape) plus prime marks | yes (Prop. 19.2) | no: it *is* the [O5] mechanism (canonical family, Lemma 17.2, l. 9296–9345) |
| Lemma 17.6 (l. 12362) | amplified `Σ_u \|M_u(D)\|²`, `r > 1` | Möbius × sextic, `ρ < 1` | yes (slope `α = 5/6`) | no; it is the [O5] extraction run in reverse |
| Lemma 18.1 (l. 12531) | `Σ_k \|S S Q\|²` | **plain** × sextic | yes | no |

So the only general sextic large sieve in [S30] (Lemma 9.1) is idle in Part II. Wherever Part II
has a Möbius × sextic sum, it already uses the [O5]-type estimate (Lemma 17.1). The one large
direct-side loss (Prop. 15.2) sits on a sum that is not Möbius. Step (2) of the brief therefore
has no admissible substitution site. §2 checks this at the level of identities and tries repairs.

### 1.2 The coefficient class of the Gram sum

**Prop. O3.1 (PROVED-HERE from the imported identities [S30] (4.10)/eq:signal, l. 966–967).**
For squarefree primary `s` outside `S` and `(m, s) = 1`,

    q_s^{-1/2} g_{χ_s}(s, −m) = conj(χ_s(−m)) · γ₁(s),    γ₁(s) = G(s) γ₂(s)².

*Proof.* Substitute `d ↦ −m^{-1}d` in `g_{χ_s}(s,−m) = Σ_d χ_s(d) e(−md/s)` to get the first factor.
[S30] eq:signal gives `γ₂(s)³ = μ(s)α(s)` and `γ₁(s)γ₂(s) = μ(s)α(s)G(s)`, with `|γ₂(s)| = 1`.
Dividing gives `γ₁ = μαG/γ₂ = γ₂³G/γ₂ = Gγ₂²`. ∎

Thus, on squarefree columns,

    A_m = Y′^{-1} Σ_s c_σ(s) G(s) γ₂(s)² W₁(r_s) r_s^{-1/2+iv} conj(χ_s(−m)) + (non-squarefree s).

The column coefficient is `γ₂²`, the square of the normalized cubic Gauss sum. Equivalently it is
`μ(s) α(s) conj(γ₂(s)) G(s)`: Möbius times an infinite-order angular character times a conjugate
cubic Gauss sum. In the notation `θ = ᾱγ₂` (`θ³ = μ` up to `α`-powers) this is class `θ²`.
[O5]'s family `μ(n)ν(n)χ_n(u)` with finite-order `ν` is class `θ³`. Two hypotheses of [O5]
Prop. 2.1 fail:
* `ν` must be a fixed finite-order Hecke character, but here it is `α·conj(γ₂)·G`. The factor
  `conj(γ₂)` is not a Hecke character at all: it is a Fourier coefficient of the cubic theta.
* The angular factor `α` is a Grössencharacter of infinite order. PR 910 Prop. 4.4 covers norm
  twists `q^{it}`, not `α^j`.

No re-choice of the mollifier or detector touches this. The coefficient is forced by the Gauss
sum `g_{χ_s}(s, −m)`, which the Poisson side needs in order to manufacture `μ` through
`γ₁γ₂ = μαG` ([S30] §7, l. 3847ff).

**Prop. O3.2 (PROPOSED reading of the proof of [S30] Prop. 15.2, l. 8360–8557).** In the expanded
Gram sum the two Gauss sums pair as `γ₁(s₁)·conj(γ₁(s₂))`. Poisson in `m` contributes the
conjugate pair. Since `γ₁γ_{−1} = χ_s(−1)` ([O5] eq:g, l. 844) and `|γ₁| = 1`, the dual
coefficient is plain: a product of residue characters `χ_p(m_i)^{e_p}` with fixed phases, periodic
modulo `𝔯` (l. 8410–8437).
* For a nonexceptional frequency `k` the complete mean is zero (l. 8439–8449). These frequencies
  give the `P_a²/Y′` term.
* For the exceptional frequencies `(k) = a₁⁶e` (l. 8534–8555) the residual characters are
  principal. The residual sum is then a **plain** lattice count of size `N²`, `N = Y′/(C₀D₀)`.
  There are `≍ K^{1/6}` such `k` (`K = RP_a/C₀`), which gives `(Q/Y′)P_a^{1/6}`.

Compare [O5] (l. 285–297, 700–722). There the rows `u = p⁶` give `|A_{p⁶}(D)|² ≈ |A_1(D)|²`, and
`A_1(D)` is a **Möbius** sum, so its smallness is the whole content. Here the analogous rows give a
plain sum with nothing to cancel. Note J (parallel branch) proves the term sharp as stated.

## 2. Step (2): substitution attempts and repairs (all fail; exponents attached)

### 2.1 Direct substitution of [O5] into Prop. 15.2. Fails at the coefficient class

This is §1.2. The first violated hypothesis is "`ν` fixed finite order", because `conj γ₂(s)`
sits in the coefficient. Even after the dual is formed (Prop. O3.2), the family there is plain,
not Möbius.

### 2.2 Repair R1: Möbius-weight the additive variable (`c_σ(s) → μ(s)c_σ(s)`, or any multiplicative `f(s)`)

* **Direct side.** The exceptional rows now carry `|Σ_{n∼N} μ(n)ψ(n)|²`. These are
  `K ≍ P_a = Z^b` rows against `N ≍ Y′ = Z^{l_y}` columns, so `ρ = b/l_y ≈ 0.26 < 1`. That is the
  sub-diagonal regime (RUNG_STRENGTH §2–3), outside [O5] Prop. 2.1, which needs `ρ > 1`. It is
  GRH-on-average strength.
* **Poisson side.** The signal is lost. In the local factor (7.5) ([S30] l. 3990–4005) the
  `t = 0, k > 0` terms give `Σ_k ρ^k Q^{−wk}`. This is a pole at `w = 1` for `f = 1`, which
  produces the signal `Y^{w−1}`. For `f = μ` it becomes `1 − Q^{−w}`, with no pole.
* **General law.** Write `m_f` for the normalized exceptional mean of `f` (Note Q, imported
  identification). Then the direct side is `Z^{l_x/2}(1 + P_a^{1/6}m_f²)^{1/2}` and the signal is
  `∝ m_f`. **PROVED-HERE (elementary):** `m/(1 + Pm²)^{1/2}` is increasing in `m`, so with
  `|m_f| ≤ 1` the ratio of signal to direct bound is at most `(1 + P_a^{1/6})^{-1/2} ≍ P_a^{−1/12}`.
  The loss `Z^{b/12}` is therefore a floor for every additive coefficient.
* **Exponent:** `θ = b/12`, unchanged.

### 2.3 Repair R2: subtract the exceptional (bias) component. Reduces to (NA), OPEN

Split `A_m = A_m^{exc} + A_m^{rest}`, where `A^{exc}` is the projection onto the exceptional
eigenspace of the Gram operator. That eigenspace has dimension `≪ K^{1/6} q_C^ε` per `(C, R)`
shell (l. 8534–8545). Its eigenvectors are the probe's ray-class vectors (Note J).
* `A^{rest}` has Gram bound `(Q/Y′)(1 + P_a²/Y′)` (Prop. 15.2's own proof minus the exceptional
  shells), so `θ = 0` for it.
* The remaining piece needs the following statement.

**(NA) Non-alignment (OPEN; first unverified substitution).** Uniformly in the tuple and in
`|v| ≪ Z^ε`,

    Q^{-1/2} | Σ_{m≠0} Ω(q_m/Q) ξ(m)(q_m/Q)^{-iv} A^{exc}_{m,σ,v}(Y′) B^J_{m,σ}(Z) | ≪ Z^{l_x/2 − d/2 + ε}.

Cauchy–Schwarz plus Lemma 15.1 gives this with an extra factor `Z^{b/12}`, so (NA) asks for a
saving of exactly **`Z^{b/12}`**: `Z^{1/96}` at the paper geometry and `≈ Z^{0.024}` at the
`θ = 0` optimum.
* `A^{exc}` is the sextic Patterson-bias component: the residue of the 6-fold Kubota series at
  `1/2 + 1/6` (FINDINGS §3, Note P).
* `B_m` is a cubic-theta row of class `θ`.
* (NA) is therefore a Rankin–Selberg pairing between the residual sextic theta and a twisted cubic
  theta. It is not a mean square of a Möbius family, so [O5] cannot supply it.
* **Value if (NA) holds** (CONDITIONAL on (NA) and on [S30]'s lemmas extrapolated to the new
  geometry, THRESHOLD_CALCULUS §7): see §5.

### 2.4 Repair R3: Hölder in place of Cauchy–Schwarz. Fails, same exponent

`|Σ_m A_m B_m| ≤ ‖A‖_p ‖B‖_{p′}`. Only `ℓ²` information is available for `B` (Lemma 15.1). For
`p′ < 2` the only route is `‖B‖_{p′} ≤ Q^{1/p′−1/2}‖B‖₂`, and `‖A‖_p ≥ Q^{1/p−1/2}‖A‖₂`. The
product is at least the Cauchy–Schwarz bound unless `A^{exc}` is concentrated on a set of
`m`-density `Q^{-c}`. It is not: its `m`-dependence is through residue classes modulo `C`, and it
is spread over the ball. PROPOSED. Exponent: `θ = b/12`.

### 2.5 Repair R4: move to the regime `P_a ≤ 1` (`l_y ≤ l_x`)

* Prop. 15.2 is stated for `P_a ≥ 1`. For `P_a < 1`, Lemma 6.2 (additive sieve) already gives
  `Q/Y′` with no loss, so `θ = 0` is free.
* But the high side carries `−a·l_y`, which rewards larger `l_y`.
* Re-optimising the imported model on the slice `b = 0` (`scripts/o3_b0_slice.py`; floating point,
  finite) gives `σ0 = 0.875684`, at `l_x = l_y = 0.41803`, `ℓ = 0.16393`. That is **worse than
  7/8**. The `b < 0` side is outside the transcribed model.
* Exponent: no gain.

### 2.6 Repair R5 (cross-check): prime in the additive variable

Note Q (parallel branch) carried this through to a clean no-go. Not repeated here.

## 3. Step (3): the floor wall via "all rows minus non-floor rows"

**Prop. O3.3 (PROVED-HERE, logic).** Suppose the signed sum over all rows is evaluated by the
probe identity at the same scale `Z`, i.e. [S30] (7.4) with each row on its own admissible
contour. Then `Σ_{floor} Row_u = I − (principal) − Σ_{non-floor} Row_u`. Substituting this into the
contradiction inequality `|principal| ≤ |I| + |Σ_{u≠1} Row_u|` gives `0 = 0`. The variant carries
no information.

To be non-circular, the all-rows sum must come from an independent evaluation. Three were tried:
1. **A common contour for all rows at `Re x = a₀`.** Moving every row there crosses the zeros of
   every non-floor `L(x, ηχ_u)`. The residues involve `1/L′(ρ_u)`, for which no upper bound
   exists (no lower bound for `|L′|` at zeros; multiple zeros). The subtraction cannot be made
   uniform.
2. **The row-generating series** `Σ_u q_u^{-z} ξ̄(u) F_{η,u}(x,w,z)`, continued in `z`. At fixed
   `x` the terms of the non-floor rows have poles as soon as `Re x` passes their zeros. So
   continuing in `x` to the floor contour is itself zero-free information about the family, which
   is circular. Continuing only in `z` with `Re x > 1` never reaches the floor contour.
3. **A second scale `Z′`.** The floor rows enter with weights `Z^{x+z−1}`, which have distinct
   exponents. No linear combination of two scales cancels unknown row values.

**Prop. O3.4 (PROVED-HERE, elementary).** Any bound obtained from an unsigned mean value over all
rows is at least the triangle bound at the Lindelöf scale. Precisely: `Σ_{u∼U}|Row_u| ≤
U^{1/2}(Σ_u |Row_u|²)^{1/2}`, and a Lindelöf-on-average mean square `Σ_u|Row_u|² ≍ U·V²` (`V` the
typical size) returns `U·V`. That is the paper's floor cost `U^{1+δ₀/2}` at `V = U^{δ₀/2}`. The
[O5] mean square controls `Σ_u |M_u|²` and is of this type. It therefore reproduces the floor cost
and cannot move the wall (13/15 at `a₀ → 1/2`; THRESHOLD_CALCULUS §5).

**Smallest statement (OPEN; signed floor cancellation, AGENDA B1).**
`Σ_{u floor, q_u∼U} Row_u(Z) ≪ U^{1+δ₀/2−f+ε}·(paper normalization)` at `d = h`, for some `f > 0`.
The exact LP barriers below (`scripts/o3_barriers.py`, certificates verified in Fractions) are
barriers only, i.e. low side plus floor row. With paper counts the floor is not binding, and
`f > 0` alone gives nothing below `0.874957`.

| Gram loss | `a₀` | `f = 0` | `f = 1/100` | `f = 1/50` | `f = 1/20` | `f = 1/10` |
|---|---|---|---|---|---|---|
| `b/12` (paper) | 51/100 | 167/192 ≈ 0.869792 | 674/777 ≈ 0.867439 | 13/15 | 13/15 | 13/15 |
| `b/12` (paper) | 1/2 | 13/15 | 13/15 | 13/15 | 13/15 | 13/15 |
| `0` ((NA) granted) | 51/100 | **926/1077 ≈ 0.859796** | 934/1089 ≈ 0.857668 | 314/367 ≈ 0.855586 | 322/379 ≈ 0.849604 | 38/45 ≈ 0.844444 |
| `0` ((NA) granted) | 1/2 | 6/7 ≈ 0.857143 | 454/531 ≈ 0.854991 | 458/537 ≈ 0.852886 | 94/111 ≈ 0.846847 | 38/45 |

The first row reproduces THRESHOLD_CALCULUS (167/192, 13/15) and AGENDA B1 (`f ≥ 1/50` reaches
13/15). With the paper's Gram loss the floor saving saturates at 13/15, the low-side Barrier 1.
Below that, (NA) or a bilinear saving (B2) is needed first.

## 4. Step (4): does Lemma 18.1 give the Oct 5 rung `Mom(2, h)`, `h < 2`? No

* **Family mismatch (PROPOSED reading, l. 12531–12580).** Lemma 18.1 bounds
  `Σ_{k∈𝓡_z} |S_{ψ_k}(n₁)S_{ψ_k}(n₂)Q|² ≪ Z^{M+ε}`, where `S` is the **plain** polynomial
  `Z^{−n/2}Σ_l ψ_k(l)W` with `ψ_k(l) = ν(l)χ_l(k)`, class `θ⁰`.
  * AGENDA A1 needs `Σ_{Nu≤D^h} |A_u(D)|⁴ ≪ D^{2+h+ε}` for the **Möbius** sum `A_u`, class `θ³`.
  * Plain sums have Hecke functional equations, and Lemma 18.1's reflection reset (18.10) uses
    them. Möbius sums have none.
  * For `z > 0` Lemma 18.1 also carries `β* ≤ (1+κ)/2`.
* **Conversion by Heath-Brown's identity.** For `n ≤ y^k`,
  `μ = Σ_{j=1}^{k} (−1)^{j−1} C(k,j) M_y^{*j} * 1^{*(j−1)}` (PROVED-HERE: `1 − ζM_y` is supported
  on `n > y`). For `k = 2`, `A_u = −Σ_{d₁,d₂≤y} μμψ · S_u(D/d₁d₂)`, with Möbius pieces of
  total log-length `a + b ≤ 1`.
  * Bound the Möbius pieces pointwise by the imported zero-free region, `≪ D^{β*(a+b)+ε}`,
    uniformly in the conductor up to `D^ε`. Bound the plain piece by Lemma 18.1.
  * This gives `Σ_u|A_u|⁴ ≪ D^{2 + (4β*−2)(a+b) + h + ε}`, which at `a + b → 1` is
    `D^{4β* + h}`.
  * That is diagonal (`D^{2+h}`) only if `β* ≤ 1/2`. Larger `k` needs `2k`-th moments of plain
    sums, which are not in [S30].
* **Bootstrap.** Cauchy–Schwarz with [O5]'s second moment gives `M₄ ≤ max|A_u|²·D^{1+h}`.
  Extraction then gives `A_1 ≪ D^{(1 + 2β* + 5h/6)/4}`. At `h → 1` the fixed point is
  `β* = 11/12` (RUNG_STRENGTH §4 item 4, reproduced). No gain.
* **Smallest statement:** A1 itself, i.e. `Mom(2, h)` for some `h < 2` (`< 9/5` beats 7/8),
  worth `1/2 + 5h/24` (PR 910 Prop. 7.2, unreviewed; RUNG_STRENGTH Prop. R′). By Prop. R it
  implies a quasi-GRH for the whole family at `Re s > 1/2 + h/4`, so it cannot follow from a
  plain-coefficient moment plus the 7/8 input.

## 5. Report

**Best σ0.**
* **Achieved:** none below 7/8. The best stays the imported `(1507 − 2√921)/1653 ≈ 0.874957`
  (CONDITIONAL on [S30] and Liu/PR 910; unchanged here). The imported model re-run gives
  `0.874961` (floating point, finite).
* **CONDITIONAL:** `σ0 = 926/1077 ≈ 0.859796`. This is an exact LP barrier, attained to
  `1.5·10⁻⁵` by the model optimum `0.859811` at `(l_x, l_y, ℓ) ≈ (0.2897, 0.5794, 0.1308)`, binding
  on the floor bin. It rests on:
  1. (NA) at saving `Z^{b/12}`, OPEN;
  2. [S30] Lemmas 10.3–10.6, 14.3, 15.1, 15.2 minus its exceptional shells, 17.1, 17.6, 18.1,
     Prop. 19.2, extrapolated from the paper geometry `(17/48, 23/48, 1/6)` to this one (lemma
     ranges: THRESHOLD_CALCULUS §7; `M + ℓ = 1` holds, `P_a ≥ 1` holds);
  3. the 7/8 bootstrap input `κ = 2β* − 1` (imported).
  The parallel branch's fuller model (with intermediate-row and supply constraints) gives
  `0.86395` under the same (NA).
* Partial (NA): a saving of `Z^{κ}` with `κ = (1 − s)·b/12`, i.e. a Gram loss of `s·b/12`. The
  imported model re-optimised (`scripts/o3_theta_opt.py`; floating point, finite) gives:

  | Gram loss `s·b/12` | best σ0 (model) | binding constraint |
  |---|---|---|
  | `s = 1` (paper) | 0.874961 | mid-depth bin `δ ≈ 0.386`, `x = 1/2` |
  | `s = 1/2` | 0.869498 | floor bin (`δ = 1/50`, `R = 1`) |
  | `s = 1/4` | 0.864531 | floor bin |
  | `s = 0` | 0.859811 (LP barrier 926/1077) | floor bin |

  The parallel branch reports `0.8696` at `s = 1/2`, consistent. Any `κ > 0` improves Liu's value.
  The `s = 1/2` row already passes the floor-bin wall `167/192` of the paper Gram regime, because
  the wall itself moves with the Gram loss.

**First unverified substitution.** (NA), §2.3. It replaces Cauchy–Schwarz by a bound for the
pairing of the sextic-bias component of `A_m` with the theta row `B_m`. It is the first point
where [O5] was supposed to enter, and [O5] does not cover it (Prop. O3.1–O3.2).

**Smallest statement whose failure kills it.** (NA) with saving exactly `Z^{b/12}`. If (NA) fails
at every power, then by Note J (sharpness of Prop. 15.2) and §2.2 (signal ∝ exceptional mean) the
loss `θ = b/12` is forced for every Cauchy–Schwarz separation of this probe. The model then stays
at `0.874957`, and the floor and low-side walls `167/192` and `13/15` stay behind it.

**Most promising next step.**
* Formulate (NA) as a bound for the Rankin–Selberg pairing of the 6-fold-cover residual theta
  (Kubota residue at `2/3`) against the twisted cubic theta row.
* As a cheaper first test, compute `A_m^{exc}` explicitly from l. 8534–8555, i.e. the
  `K^{1/6}`-dimensional exceptional projection. Then measure numerically, at small `Z`,
  `|⟨A^{exc}, B⟩| / (‖A^{exc}‖·‖B‖)` against the `Q^{-1/2}`-type random benchmark. Persistent
  alignment would falsify (NA). This would be floating point, finite, and could falsify (NA) but
  never prove it.

## Files

* `README.md` (this note).
* `scripts/o3_barriers.py`: exact LP barriers with Gram and floor dials. It imports
  `../../../scripts/barrier_lp.py` unchanged. Output: `results/o3_barriers.json`.
* `scripts/o3_theta_opt.py`: re-optimisation of the imported `threshold_calculus.py` model with
  a Gram-loss scale. Outputs: `results/o3_theta_opt.json` and `.log` (scales 1 and 0), and
  `results/o3_theta_opt_half.log` / `results/o3_theta_opt_half_quarter.json` (scales 1/2 and 1/4).
* `scripts/o3_b0_slice.py`: repair R4, the `b = 0` slice. Output: `results/o3_b0_slice.json`.

All scripts import the wave's `../../../scripts/` modules unchanged, run single-threaded in under
2 minutes each, and write only inside this folder.
