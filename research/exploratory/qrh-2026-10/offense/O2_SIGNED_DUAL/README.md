# O2: the signed dual at ρ < 1, where the Möbius sign really goes, and an amplifier ledger

```text
Status: PROPOSED (not reviewed). Labels per item: PROVED-HERE (complete elementary proof below, resting
  on the IMPORTED Oct 5 Poisson identity), CONDITIONAL (named inputs), HEURISTIC, EMPIRICAL (floating
  point, finite), OPEN. No zero-free region is proved. RH is open.
Scope: the sub-diagonal second moment Mom(1, rho), rho < 1, of the Oct 5 sextic Moebius family
  A_u(D) = sum_n mu(n) nu(n) chi_n(u) W(Nn/D) over Z[omega] (RUNG_STRENGTH.md), through its exact
  Poisson dual (Oct 5 prop:poisson-reduction). Questions: (1) exact signed dual and the size of the
  positivity loss; (2) can a Heath-Brown (HB00)-type Type I/II argument with mu against cubic Gauss
  sums give a power saving; (3) best exponent and the blocking term; (4) numerics.
Exact sources or dependencies:
  Oct 5 manuscript (external, unreviewed, IMPORTED), paper2.tex sha256 d9a8f15a...50d4d, lines
    773-1258 (lem:arithmetic, lem:poisson, lem:remove-exclusions, prop:poisson-reduction and its
    proof, eq:initial-column-output, eq:weighted), 1261-1640 (prop:canonical, prop:R, lem:cube-reduction,
    prop:transfer). Identities eq:crt-a, eq:convert1/2 are used as stated there.
  PR 910 Prop. 7.2 extraction law (IMPORTED, unreviewed) via RUNG_STRENGTH.md Prop. R'.
  DISPERSION_GRH_STEP.md section 4, Q_RHO_ANALYSIS.md sections 2-3 (claims re-examined here).
  PR 930 draft (origin/research/parity-and-cubic-fibers-20261012, head c07b9f653, unreviewed): only
    its chi_p = Q_p C_p split is mentioned in section 3; nothing is taken from it.
  Literature named in the task (HB00, HBP79, Dunn25, DR24) is used only at the level of the
    mechanism "twisted multiplicativity of Gauss sums -> cubic large sieve". HB00's X^{5/6+eps}
    bound and the cubic large sieve are quoted from DR24 arXiv v3 section 1 (local untrusted TeX copy,
    read as data); no claim below relies on them.
What was actually run (single-threaded, shared machine):
  python3 -I o2_ledger.py results/o2_ledger.json      (about 12 s; sympy exact rationals + exact checks)
  python3 -I signed_dual_numerics.py run_main.json 1000 2000 4000 8000 16000 24000 --rho 0.6 0.75 0.9
     (about 10 min; output copied to results/signed_dual_main.json)
Smallest remaining gap: (OD-g1) below: the coprime-pair dual (the g = 1 part of the exact signed
  dual, which carries no Moebius sign at all) at relative precision D^{-delta} below the full dual
  diagonal, with delta > (1 - rho)/6. Equivalently (via the principal rows) the principal member
  below 11/12. On the amplifier side: the amplified dual must close at H >= D L^t with t < 6/5;
  the Oct 5 reflection closes it only at t = 2.
```

RH remains unproved. The Oct 5 and Sep 30 manuscripts are external, unreviewed imports; anything
resting on them is CONDITIONAL/IMPORTED below.

## 0. Results in brief

| # | statement | label | exponent |
|---|---|---|---|
| G | **gcd-collapse form of the signed dual** (section 1.2): after the exact Poisson step, the Möbius variable `f` of eq:weighted sums out exactly; the only Möbius value left is `μ(g)` on `g = gcd(n₁, n₂)`, forced to divide the dual row `k`. Its Gauss-sum factors appear only as `|a(g)|² = 1`. | PROVED-HERE (given the imported identity eq:initial-column-output); identity checked [EXACT] on 400 cases with true sextic symbols | — |
| N | **No "μ against Gauss sums" exists in the signed dual.** In gcd form the surviving `μ(g)` multiplies the sextic character `conj χ_{z₁}(g) χ_{z₂}(g)`, i.e. an *original-family member* `A_{z₁⁵z₂}(G)` of conductor about `Z²`. So an HB00-type Type I/II argument (μ vs Gauss sums) has nothing to act on; the involution of Q_RHO_ANALYSIS is visible term by term. | PROVED-HERE (corollary of G) | — |
| L | **Leverage law for partial savings.** A saving `D^δ` below the positivity (row-blind) bound at `H = D^ρ` gives `σ = 1 − δ/2 − ρ/12`. It beats 11/12 iff `δ > (1 − ρ)/6`, and beats 7/8 iff `δ > 1/4 − ρ/6` (only possible for `ρ ≤ 9/10`). Conversely the principal rows force `δ ≤ 2 − ρ/6 − 2σ₀` when `|A₁(D)| ≍ D^{σ₀}`, so `δ > (1 − ρ)/6` **is equivalent to** `σ₀ < 11/12` at the same scale. | PROVED-HERE (elementary, given the imported extraction law) | threshold `(1 − ρ)/6`, not `1 − ρ` |
| H | **HB00-type routes give δ = 0.** Type I via Pólya–Vinogradov on `μ(f)` reaches even the positivity level only for blocks `F ≥ D^{2/3}`; blocks `F < D^{2/3}` carry 57–60 % of the positivity bound, and the `f = 1` block alone (no Möbius variable) carries 22–31 %. Primal Type II is capped at `D²` (row-blind) and its principal rows return `A₁`. Dual pointwise HB00 savings cannot help a mean square at or below its diagonal. A conditional import-assisted variant reaches dual-column ranges `Z ≤ D^{(12ρ+1)/31}` only. | PROPOSED (exponent bookkeeping, sympy) + [EXACT/FLOAT] block shares | δ = 0 |
| A | **Amplifier ledger (the construction attempted here).** Amplify the extraction rows by `B_u(L) = Σ_{ℓ∼L prime} μ(ℓ)χ_ℓ(u)` (Möbius signs are absorbable, and `|B_principal| = π_K(L)`). If the amplified dual closes at `H ≥ D·L^t`, then `σ = 11/12 + λ(5t − 6)/12`, `L = D^λ`. Gain iff `t < 6/5`. The Oct 5 reflection (prop:R with its `N(f)` factor) closes only at `t = 2` (σ = 11/12 + λ/3), and Cauchy–Schwarz over `ℓ` gives `t = 5/2`. A quadratic amplifier (`χ_p³`) has the same `t = 2`. **Lemma NRA**: no amplifier makes the amplified Gauss coefficients a finite-order modulation of theta coefficients of length `DL`, which is what `t = 1` would need. | ledger PROPOSED; Lemma NRA PROVED-HERE; `t < 6/5` OPEN | `11/12 − λ/12` at `t = 1` (CONDITIONAL on (AMP₁)) |
| E | **Numerics.** The signed dual `S = 𝓜_D − Z` is tiny: `|S|/H ≤ 0.71 %`, `|S| ≤ 6` for `D ≤ 24000`. It is consistent with an independent-row model, `|S| ≍ H^{1/2}`. Its ratio to the positivity proxy `P ≍ D log D` gives an empirical cancellation exponent `log(P/|S|)/log D ∈ [0.70, 1.59]`, against the `1 − ρ ∈ {0.1, 0.25, 0.4}` that Mom(1, ρ) needs and the `(1 − ρ)/6` that beats 11/12. HB00-type routes predict 0. | EMPIRICAL (floating point, finite) | — |

**Best result.** No exponent moves. The precise outcome is a reduction with an exponent attached:

* (L + G + H) Any proof of Mom(1, ρ)-type savings must beat the positivity bound by `D^δ`, `δ > (1 − ρ)/6`, on the **coprime-pair dual**

      (OD-g1)   (H/D²) Σ_{k≠0} Σ_{(z₁,z₂)=1} a(z₁) conj a(z₂) χ_{z₁}(k) conj χ_{z₂}(k) W₀ W₀ Φ̂  ≪  D^{1−δ},

  together with the analogous bound for the `g > 1` terms. (OD-g1) contains no Möbius function, and the
  required `δ` is exactly what the principal member's distance below 11/12 supplies. The beat-11/12 threshold
  is therefore `(1 − ρ)/6`, six times smaller than the `1 − ρ` stated in DISPERSION_GRH_STEP §4. This is a
  correction of the "required saving", not of its conclusion.
* (A) The one construction that is not visibly an involution is amplification of the extraction rows. It moves
  the exponent to `11/12 − λ/12` **iff** the amplified dual closes at `H ≥ D L^{t}` with `t < 6/5` (exact law
  `σ = 11/12 + λ(5t − 6)/12`). With the manuscript's own reflection it closes at `t = 2`. The blocking term is
  the factor `N(f)` in Oct 5 prop:R: the reflected length `𝓗² N(f)/X` grows with the cubic shift `ℓ⁴` that
  twisted multiplicativity of Gauss sums attaches to every amplifier prime.

## 1. The exact signed dual at ρ < 1

### 1.1 The imported identity and where positivity enters [TEX, IMPORTED]

Oct 5 prop:poisson-reduction (lines 1027-1251) is an exact identity for any `H` (the hypothesis
`H = D^{1+ϑ}` is used only in the final estimate). With `𝓜_D = D^{-1} Σ_u Φ(Nu/H)|A_u(D)|²`:

    𝓜_D = Z + Σ_ξ c_ξ 𝓢_ξ,    Z = (H/D) Φ̂(0) Σ*_g |W(Ng/D)|² ∏_{p|g}(1 − 1/Np) ≍ H,

    𝓢_ξ = (H/D²) Σ*_{(b,f)=1} μ(f) N(b) Σ_{k≠0} Σ*_{(m₁m₂,b)=1} a(m₁) conj a(m₂) χ_{m₁}(kf⁴) conj χ_{m₂}(kf⁴)
           · W₀(N(bfm₁)/D) conj W₀(N(bfm₂)/D) · Φ̂(H N(k) / (N(f)² N(m₁) N(m₂)))        (eq:initial-column-output)

with `a = a_ξ = conj(α) γ₂ ξ` and `W₀(x) = x^{-1/2} conj W(x)`. The positivity step is eq:weighted (line
1235): for each `b`, lem:smooth-mean-square is applied with row index `(f, k)` and row coefficient
`μ(f) 1_{(f,b)=1}`, and that coefficient is then bounded by 1 in absolute value. The dyadic block `(B, F)` has
dual rows `𝓗 = D²/(HB²)` and columns `X = D/(BF)`.

### 1.2 Proposition G (gcd collapse) — PROVED-HERE, given eq:initial-column-output

For each `ξ`, exactly,

    𝓢_ξ = (H/D²) Σ*_b N(b) Σ_{k≠0} Σ*_{g | k, (g,b)=1} μ(g) Σ*_{(z₁,z₂)=1, (z₁z₂,gb)=1}
            a(gz₁) conj a(gz₂) χ_{z₁}(k) conj χ_{z₂}(k)
            · W₀(N(bgz₁)/D) conj W₀(N(bgz₂)/D) · Φ̂(H N(k) / (N(g)² N(z₁) N(z₂))).          (G)

*Proof.* Fix `b`, `k`. A term of eq:initial-column-output vanishes unless `(m_j, kf) = 1`. On the support put
`n_j = f m_j`, which is squarefree, prime to `bS`, and divisible by `f`. The map `(f, m₁, m₂) ↦ (n₁, n₂, f)` is
a bijection onto triples with `f | gcd(n₁, n₂)` and `(n₁n₂, b) = 1`.
* By eq:crt-a, `a(fm) = a(f) a(m) χ_m(f)⁴` for coprime squarefree `f, m`. Since `|a(f)| = 1`,
  `a(m₁) χ_{m₁}(f)⁴ · conj(a(m₂) χ_{m₂}(f)⁴) = a(n₁) conj a(n₂)`.
* `N(f)² N(m₁) N(m₂) = N(n₁) N(n₂)` and `W₀(N(bfm_j)/D) = W₀(N(bn_j)/D)`.
* The remaining `f`-dependence is `Σ_{f | g} μ(f) χ_{n₁/f}(k) conj χ_{n₂/f}(k)` with `g = gcd(n₁, n₂)`,
  `n_j = g z_j`. Multiplicativity in the modulus gives `χ_{(g/f)z_j}(k) = χ_{g/f}(k) χ_{z_j}(k)`, so the sum is
  `χ_{z₁}(k) conj χ_{z₂}(k) Σ_{f|g} μ(f) 1_{(g/f, k)=1}`. With `g₁ = (g, k)`, the condition is `g₁ | f`, so the
  sum is `μ(g₁) Σ_{f' | g/g₁} μ(f') = μ(g) 1_{g | k}`. ∎

[EXACT] `o2_ledger.py` part C1 checks the collapse identity with the true sextic residue symbols on 400
random configurations (82 with nontrivial `g | k`); maximum error 1.5e-15, which is the rounding of `e^{2πi j/6}`.

**Corollary N (where the sign goes).** Write `k = g k'`. By eq:crt-a again, `a(gz₁) conj a(gz₂) =
a(z₁) conj a(z₂) χ_{z₁}(g)⁴ conj χ_{z₂}(g)⁴`, and `χ_z(gk')χ_z(g)⁴ = χ_z(k') conj χ_z(g)`. Hence

    𝓢_ξ = (H/D²) Σ_b N(b) Σ_{(z₁,z₂)=1} a(z₁) conj a(z₂) Σ_{k'≠0} χ_{z₁}(k') conj χ_{z₂}(k') · I_b(z₁, z₂, k'),

    I_b(z₁,z₂,k') = Σ*_{(g, bz₁z₂)=1} μ(g) conj χ_{z₁}(g) χ_{z₂}(g) W₀(N(bgz₁)/D) conj W₀(N(bgz₂)/D) Φ̂(H N(k')/(N(g) N(z₁) N(z₂))).

`g ↦ conj χ_{z₁}(g) χ_{z₂}(g)` is a sextic character of modulus `z₁z₂`. By eq:recip it equals
`ψ_{z₁⁵z₂}(g)` times fixed ray-class data. So **every surviving Möbius value sits inside a short member of the
original family, at a row of conductor about `N(z₁z₂)`**. The Gauss sums `a(z_j)` sit on the *other*
variables, and the Gauss-sum factors of `g` cancel as `|a(g)|² = 1`. This is the involution of
Q_RHO_ANALYSIS §2 made explicit term by term. It answers task item (2) negatively in its literal form: in the
exact signed dual there is no sum of `μ` (or `Λ`) against cubic Gauss sums. The Gauss-sum/Möbius pairing is
used up entirely by eq:convert2, which is how `a` was created.

Two further readings of (G):
* **No dual diagonal.** The terms `z₁ = z₂ = 1` (i.e. `n₁ = n₂ = g`) carry `μ(g) 1_{g|k}`. For `b = 1` they
  equal `(H/D²)Σ_g μ(g)|W₀(Ng/D)|²Σ_{k≠0, g|k}Φ̂ = Φ(0)·D^{-1}Σ_g μ(g)|W(Ng/D)|² + O(H/D)` (Poisson in
  `k' = k/g`, using `N(g) ≍ D > H`). This is a *principal Möbius sum*.
  Individual `b`-blocks therefore contain `A₁`-type sums that cancel only across `b` (they are the Ramanujan
  terms of the lattice count of `u` coprime to `g`). A blockwise bound must control `A₁` itself.
* **The g = 1 part has no sign at all.** It is the coprime-pair dual (OD-g1). Its diagonal is empty, and the
  positivity step is what re-creates the dual diagonal: removing `(z₁,z₂)=1` by `Σ_{v|(z₁,z₂)}μ(v)` and then
  bounding `|μ(v)| ≤ 1`.

### 1.3 Size of the positivity bound and the required saving

The diagonal (`m₁ = m₂`) of the positivity-bounded sum is, by the lattice count
`Σ_{k: (k,m)=1}Φ̂(H Nk/Y) ≈ (Y/H)Φ(0)φ(m)/N(m)`,

    P := Σ_{b,f}|μ(f)| (H N(b)/D²) Σ_k Σ_m |W₀|² Φ̂ ≈ Φ(0) Σ*_n (Nn/D)|W(Nn/D)|² Σ_{bfm = n} φ(m)/(N(b)N(m))
       = Φ(0) Σ*_n 2^{ω(n)} (Nn/D)|W(Nn/D)|²  ≍ D log D,

because `Σ_{bfm=n} φ(m)/(N b N m) = ∏_{p|n}(1/Np + 1 + 1 − 1/Np) = 2^{ω(n)}` ([EXACT], part C2). The target is
`𝓢 ≪ H D^ε`. So the full Mom(1, ρ) needs a saving `D^{1−ρ}` (up to logs) over positivity, as DISPERSION_GRH_STEP
§4 states: **confirmed**. But beating 11/12 needs much less (section 1.4).

### 1.4 Proposition L (leverage law) — PROVED-HERE, given the imported extraction law

Let `H = D^ρ`, `0 < ρ < 1`.
1. If `Σ_{Nu≤H}|A_u(D)|² ≪ D^{2−δ+ε}` (equivalently `𝓜_D − Z ≪ D^{1−δ+ε}`, i.e. a saving `D^δ` over `P`)
   for every smooth `W`, with `0 ≤ δ ≤ 1 − ρ`, then the PR 910 extraction law `σ = (m − ρ/6)/2` with
   `m = 2 − δ` gives `σ = 1 − δ/2 − ρ/12`. This is `< 11/12` iff `δ > (1−ρ)/6`, and `< 7/8` iff
   `δ > 1/4 − ρ/6`. Within `δ ≤ 1 − ρ` the latter is possible only for `ρ ≤ 9/10`. For a general target `σ*`
   the requirement is `δ > 2 − 2σ* − ρ/6`.
2. Conversely, the sixth-power rows give `Σ_{Nu≤H}|A_u|² ≥ c H^{1/6} |A₁(D)|²` (up to the `O(D/Y)` row
   differences of Oct 5 eq:A_u-vs-A_1). So if `|A₁(D)| ≥ D^{σ₀}` along a sequence, then `δ ≤ 2 − ρ/6 − 2σ₀`,
   and `δ > (1−ρ)/6` forces `σ₀ < 11/12`.

*Proof.* Item 1 is substitution: sympy part L1 asserts every identity listed. Item 2: substitute
`D^{2−δ} ≥ D^{ρ/6 + 2σ₀}` and solve. ∎

| ρ | δ to beat 11/12 | δ to beat 7/8 | full δ = 1 − ρ (gives 1/2 + 5ρ/12) |
|---|---|---|---|
| 1/2 | 1/12 | 1/6 | 1/2 (17/24) |
| 3/5 | 1/15 | 3/20 | 2/5 (3/4) |
| 3/4 | 1/24 | 1/8 | 1/4 (13/16) |
| 9/10 | 1/60 | 1/10 (= full) | 1/10 (7/8) |
| 99/100 | 1/600 | unreachable | 1/100 (73/80) |

**What this shows.** Near `ρ = 1` the needed saving is tiny, `(1 − ρ)/6`. But item 2 shows the saving is
*exactly* the principal member's margin below 11/12. Any partial-saving mechanism for the signed dual is
therefore a mechanism for `A₁(D)` itself; at the 11/12 boundary the principal rows saturate the bound. This is
the fixed point of RUNG_STRENGTH §4 item 2, now stated at the level of partial savings: the threshold is `δ*(ρ) = (1−ρ)/6`.

## 2. HB00-type routes (task item 2): what each gives and which term blocks

The model is HB00's argument for `Σ_p g̃(p)`: a Vaughan or Heath-Brown identity; Type I through the theta
function or Poisson; Type II through twisted multiplicativity `g̃(ab) = g̃(a)g̃(b) conj(a/b)₃`, then the cubic
large sieve. Three different placements were tried. For each I tried at least three repairs.

**R1. On the Möbius variable `f` of eq:initial-column-output.** For fixed `(b, k, m₁, m₂)` the `f`-sum is
`Σ_f μ(f) ψ(f) G(Nf)` with `ψ = conj(·/m₁)₃(·/m₂)₃` cubic of conductor `≤ X²`. This is μ against a cubic
*character*, not a Gauss sum.
* Repair (a), Type I via Poisson/PV in a smooth `f₂ ∼ F₂`, with trivial outer `(k, m₁, m₂)`. This gives
  `D⁴X/(H F F₂)`, which is `≤ D³/H` (the positivity level per dyadic F) iff `F²F₂ ≥ D²`, so only blocks
  `F ≥ D^{2/3}` (ledger L2).
* Repair (b), keep the `m`-large sieve: then the μ(f)-sum is outside a square, and Type II bilinear
  structure in `f = f₁f₂` factorizes, because `ψ` is multiplicative. There is no cross term to cancel.
* Repair (c), gcd form (G): the `f`-sum disappears identically, and only `μ(g)`, `g | k`, survives (Cor. N).

Blocking term: the blocks `F < D^{2/3}`, which carry 57–60 % of `P` (C3, exact enumeration at
`D = 10³, 10⁴, 10⁵`), and above all the `f = 1` block, which carries 22–31 % of `P` and has no Möbius
variable. **δ = 0.**

**R2. Heath-Brown identity in the primal family (k = 3, 4; Vaughan).**
* Type I with a smooth variable longer than `H^{1+ε}` vanishes on non-sixth-power rows (Poisson in the
  smooth variable modulo `u`, conductor `≤ H`).
* Type II `Σ_u |A(u)B(u)|²` with lengths `M N = D > H`. Every Hölder/large-sieve allocation
  `(Σ|A|^{2p})^{1/p}(Σ|B|^{2p'})^{1/p'}` is diagonal-sized only if `M^p ≤ H` and `N^{p'} ≤ H`, hence `D ≤ H`.
  Otherwise it is capped at `D²`, the row-blind cap (RUNG_STRENGTH §3a, applied to each factor).
* Repair via pointwise bounds on one factor: Pólya–Vinogradov gives `|B| ≪ H^{1/2}` for smooth `B`, which is
  diagonal-compatible only when `M ≤ D/H`, i.e. back to Type I.
* On the sixth-power rows every Type I/II piece reassembles `A₁(D)`.

Blocking term: Type II with both factors shorter than `H` does not exist when `ρ < 1`, and the principal rows
give `A₁`. **δ = 0**, and by Prop. L any `δ > 0` here would already be a statement about `A₁`.

**R3. HB00 pointwise in the dual.** The dual rows `B_h(X) = Σ a(n)χ_n(h)W` are "μ against sextic Gauss
sums" in disguise (eq:convert2), so HB00-type Type I/II gives pointwise savings `|B_h| ≪ X^{1−η}`. For
comparison, HB00's bound for primes is `Σ_{Nϖ≤X} g̃(ϖ) ≪ X^{5/6+ε}`, via the cubic large sieve
`A + B + (AB)^{2/3}`. Both are quoted from DR24 v3 §1 (eq:hb, HBinitstate) and were not read in HB00 itself.
A mean square needs `|B_h| ≈ X^{1/2}`. Pointwise `X^{5/6}` gives `Σ_h |B_h|² ≤ 𝓗X^{5/3}`, above the diagonal `𝓗X`.
The theta reflection gives `|B_h| ≪ X^{1/2+ε}` only for `N(h) ≲ X^{1/2}`, but the dual rows run up to
`𝓗 = D^{2−ρ} > X`. **δ = 0.**

**R4 (conditional variant, HEURISTIC).** Use Cor. N and bound the inner member sums `I_b` by a *uniform*
version of the imported 11/12 (premise: `|A_r(G)| ≪ G^{11/12} N(r)^{1/12}`, with representative norm
`N(z₁⁵z₂) = Z⁶`; this uniformity is an extrapolation of Prop. R′ and is not established). Trivial outer
summation gives `D^{−1/12} Z^{31/12}`, which is `≤ H` iff `Z ≤ D^{(12ρ+1)/31}` (ledger L4; at `ρ = 9/10` this is
`Z ≤ D^{59/155}`). The remaining blocks `Z > D^{(12ρ+1)/31}`, including `G = 1`, are untouched, so **δ = 0**.

Dunn25's bilinear estimate (a cubic metaplectic kernel beyond the 2/3 barrier) and the cubic large sieve
would enter only in Type II for R1/R3. In R1 Type II is vacuous (multiplicative `ψ`), and in R3 pointwise
savings are irrelevant. Their numerical strength therefore does not affect δ.

## 3. The construction: amplifying the extraction rows

Every exact move (Poisson, reflection, gcd collapse) is an involution, and Prop. L ties any saving to `A₁`.
The natural non-involutive device is an **amplifier** that is large exactly on the extraction rows.

**Setup.** Take `B_u(L) = Σ_{ℓ ∼ L} β(ℓ) χ_ℓ(u)` and bound the amplified moment `Σ_{Nu≤H}|A_u(D)B_u(L)|²`.
On the rows `u = v⁶` it is at least `H^{1/6}|A₁|²|Σβ|²`. If it has diagonal size `H·DL`, then with `L = D^λ`,
`H = D^h`:

    2σ = (5/6)h + 1 − λ.

**Which β are absorbable.** Poisson in `u` produces `γ_{-1}(nℓ)`. For `n, ℓ` coprime and squarefree,
`μ(n)β(ℓ)γ_{-1}(nℓ) ∝ a(nℓ)·μ(ℓ)β(ℓ)` (by eq:convert2 and twisted multiplicativity). So `β = μ` on primes is
absorbable with weight 1. Note `|Σ_{ℓ∼L prime} μ(ℓ)| = #{prime ideals of norm ∼ L}`, so the "parity" sign costs nothing in amplitude.
A quadratic amplifier `β(p)χ_p(u)³ = β(p)(u/p)₂` is also absorbable: the quadratic Gauss sum `γ₃(p)` is ray-class
data. This is the `Q_p` factor of PR 930's `χ_p = Q_p C_p` split (unreviewed draft PR; not otherwise used).

**Lemma NRA (no reflectable amplifier).** PROVED-HERE. Let `β ≢ 0` be supported on squarefree ideals prime
to `S` with `Nℓ ∈ [L, 2L]`, `L ≥ 2`, and let `c = (μ W(·/D)) * β`, with `W ≢ 0` smooth on `[1, 2]`. Fix a
finite family of ray-class characters `ξ` modulo a fixed modulus, constants `κ_ξ`, and a smooth compactly
supported `w` on `(0, ∞)`. Then for all `D ≥ D₀(w, W, modulus)` with `D > 4L`, the identity

    μ(m) c(m) = Σ_ξ κ_ξ ξ(m) w(Nm/(DL))     for all squarefree m prime to S

forces `β ≡ 0`. So there is no such identity.

*Proof.* Suppose the identity holds.
1. *The right side vanishes.* A prime `m` with `Nm > 2L` has only the factorizations `(m, 1)` and `(1, m)`.
   `β(1) = 0` and `β(m) = 0`, since `Nm > 2L`. So `c(m) = 0`, and
   `Σ_ξ κ_ξ ξ(m) w(Nm/(DL)) = 0` for all such primes.
   * If `w ≢ 0`, pick an interval on which `w ≠ 0`. By the prime ideal theorem for ray classes, every ray
     class contains primes of norm in `DL` times that interval once `D ≥ D₀`.
   * Hence `Σ_ξ κ_ξ ξ ≡ 0` on the ray class group, and the right side vanishes identically.
2. *So `c` vanishes on squarefree `m`.* It follows that `c(m) = 0` for every squarefree `m` prime to `S`.
3. *A nonzero value.* Choose `ℓ₀` in the support of `β` of minimal norm. Choose a prime `n ∤ ℓ₀S` with
   `W(Nn/D) ≠ 0`, so `Nn > D > 4L`.
   * Any factorization `nℓ₀ = n'ℓ'` with `β(ℓ') ≠ 0` has `Nℓ' ≤ 2L < Nn`, so `n ∤ ℓ'`. Hence `ℓ' | ℓ₀`.
   * Minimality of `Nℓ₀` then forces `ℓ' = ℓ₀`.
   * So `c(nℓ₀) = μ(n)β(ℓ₀)W(Nn/D) ≠ 0`, while `nℓ₀` is squarefree and prime to `S`.

This contradicts step 2. ∎

So any amplifier leaves a divisor-type weight `ν_β(m) = Σ_{ℓ|m} μ(ℓ)β(ℓ)W(N(m/ℓ)/D)` on the dual theta
coefficients (on squarefree `m`).
The reflection must then be applied factor by factor, with `ℓ` acting as an `f`-type cubic shift `χ_n(ℓ)⁴`.

**Ledger** (`o2_ledger.py` L3; sympy exact). If the amplified dual closes at `H ≥ D·L^t`, then

    σ(λ) = 11/12 + λ (5t − 6)/12,        gain iff t < 6/5.

| variant | where the amplified dual closes | σ |
|---|---|---|
| (a) Cauchy–Schwarz over `ℓ`, then Oct 5 prop:R (`𝓗 + 𝓗²N(f)/X` per `f = ℓ`) | `H ≥ D L^{5/2}` | `11/12 + 13λ/24` |
| (b) cross terms `ℓ ≠ ℓ'` free, prop:R as stated | `H ≥ D L²` | `11/12 + λ/3` |
| (q) quadratic amplifier: product `B_h(D)·Q'_h(L)`, reflect `B_h`, quadratic large sieve on `(r, p)` | `H ≥ D L²` | `11/12 + λ/3` |
| (c) hypothetical: reflected length `𝓗²/(XL)`, no `N(f)` growth, no cross-term loss | `H ≥ D L` | **`11/12 − λ/12`** |

For (b): the requirement `𝓗 + 𝓗²L/X ≲ XL` with `X = D` forces `𝓗 = (DL)²/H ≤ D`. The reflection "sees" only
the theta length `D`, while the dual row count scales as `(DL)²`.

**Remark (the reflectable quadratic amplifier is already inside the theta, and it is angular).** PROPOSED.
The completed sum eq:T is `Σ_{n,b} a(n) ᾱ(b)³ Ψ(b)³ / (√N(n) N(b)) · V_*(N(n)N(b)³/X)`, with
`Ψ_k(b)³ = χ_b(k)³ = (k/b)₂`. So the cube variable `b` *is* a quadratic amplifier, and it is reflected
together with `n` at total length `X` (reflected length `𝓗²/X`, no growth). This is the `t = 1` behaviour.
Its weights are forced to be `ᾱ(b)³/N(b)`, and `ᾱ(b)³ = (b̄/b)^{3/2}` is a Größencharakter of infinite order. So
`Σ_{Nb∼P} ᾱ(b)³ ξ(b) = o(P/log P)` for every finite-order `ξ` (Hecke's prime ideal theorem for
Größencharaktere): it never amplifies the principal rows. A primal quadratic amplifier with a nonzero mean
(variant (q)) has instead the weights `γ₃(p) w(Np/P)`, which do not match the theta coupling
`V_*(N(n)N(b)³/X)`. Its `p` must then ride outside the reflection, and the reflection closes only at `t = 2`.
The trade-off "reflectable ⇔ angular ⇔ no amplification" is the precise obstruction in the quadratic slot.
Lemma NRA is the precise obstruction in the sextic slot.

**The exact smallest statement (AMP_t), OPEN, with exponent.** For some fixed `t < 6/5` and all
`1 ≤ L ≤ D^{λ₀}`:

    Σ_{F≤N f<2F}^* Σ_{0<N k ≲ 𝓗} | Σ_{ℓ ∼ L} μ(ℓ) a(ℓ) χ_ℓ(k) Σ*_n a(n) χ_n(k f⁴ ℓ⁴) W(Nn/X) |²  ≪ D^ε (XFL)²
    whenever 𝓗 ≤ X F · L^{2−t}  (X = D/(BF) as in eq:initial-scales).

Under (AMP_t) and the imports, the zero-free half-plane is `Re s > 11/12 − λ₀(6 − 5t)/12`. `t = 1, λ₀ = 1/2`
already gives 7/8. (AMP_t) has rows ≤ columns (`𝓗 ≤ XFL^{2−t} < XFL`), so it is **not** blocked by the
row-blind barrier or by the orbit invariant of Q_RHO_ANALYSIS. Its obstruction is different: the `N(f)` factor
in prop:R, i.e. the level growth of the cubic theta under the shift `ℓ⁴`. Caveat: (AMP_t) for large `λ₀`
contradicts `A₁(D) = Ω(D^{1/2})`. At `t = 1` it must fail for `λ₀ > 5`, so it is a genuine constraint, not a
convenience.

## 4. Numerics (EMPIRICAL, floating point, finite)

`signed_dual_numerics.py`: `ν = 1`, `S = {2, λ}`, the bump `W` of moments/common.py, `Φ(x) = e^{−πx}`
(`Φ̂(0) = 2/√3`, `Φ(0) = 1`), rows `0 < Nu ≤ 6H`. `A_u(D)` is computed exactly from sextic residue symbols
(split primes via `ω ↦ r mod q`, inert primes in `F_{p²}`). `S = 𝓜_D − Z` is the exact signed dual
`Σ_ξ c_ξ𝓢_ξ`. `Off = 𝓜_D − Diag` uses the exact primal diagonal (with coprimality). `P` is the positivity
proxy of §1.3. `e = log(P/|S|)/log D` is the empirical cancellation exponent relative to positivity.

| D | ρ | H | 𝓜_D | Z | S = 𝓜_D − Z | Off/Diag | \|S\|/s_rand | P (proxy) | Prin | \|A₁(D)\| | e = log(P/\|S\|)/log D | 1 − ρ | (1 − ρ)/6 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000 | 0.60 | 63 | 5.193 | 5.639 | -0.4461 | -7.68e-02 | 0.96 | 394 | 0.321 | 6.3 | 0.982 | 0.40 | 0.067 |
| 2000 | 0.60 | 96 | 8.565 | 8.560 | 0.0049 | 1.47e-03 | 0.01 | 874 | 1.384 | 7.3 | 1.590 | 0.40 | 0.067 |
| 4000 | 0.60 | 145 | 12.860 | 12.874 | -0.0132 | -3.65e-04 | 0.02 | 1793 | 0.919 | 18.6 | 1.425 | 0.40 | 0.067 |
| 8000 | 0.60 | 220 | 18.716 | 19.253 | -0.5370 | -2.75e-02 | 0.63 | 3621 | 0.928 | 21.8 | 0.981 | 0.40 | 0.067 |
| 16000 | 0.60 | 333 | 28.721 | 29.342 | -0.6207 | -2.10e-02 | 0.59 | 7717 | 0.922 | 34.0 | 0.974 | 0.40 | 0.067 |
| 24000 | 0.60 | 425 | 38.101 | 37.495 | 0.6061 | 1.63e-02 | 0.51 | 11977 | 0.995 | 51.1 | 0.981 | 0.40 | 0.067 |
| 1000 | 0.75 | 178 | 15.343 | 15.892 | -0.5494 | -3.43e-02 | 0.70 | 394 | 0.332 | 6.3 | 0.952 | 0.25 | 0.042 |
| 2000 | 0.75 | 299 | 25.169 | 26.769 | -1.5994 | -5.97e-02 | 1.57 | 874 | 1.416 | 7.3 | 0.829 | 0.25 | 0.042 |
| 4000 | 0.75 | 503 | 43.919 | 44.669 | -0.7505 | -1.67e-02 | 0.57 | 1793 | 0.943 | 18.6 | 0.938 | 0.25 | 0.042 |
| 8000 | 0.75 | 846 | 73.145 | 74.126 | -0.9819 | -1.32e-02 | 0.59 | 3621 | 1.001 | 21.8 | 0.914 | 0.25 | 0.042 |
| 16000 | 0.75 | 1423 | 121.217 | 125.344 | -4.1268 | -3.29e-02 | 1.89 | 7717 | 1.114 | 34.0 | 0.778 | 0.25 | 0.042 |
| 24000 | 0.75 | 1928 | 170.079 | 170.217 | -0.1373 | -7.95e-04 | 0.05 | 11977 | 1.301 | 51.1 | 1.128 | 0.25 | 0.042 |
| 1000 | 0.90 | 501 | 44.233 | 44.790 | -0.5566 | -1.24e-02 | 0.42 | 394 | 0.339 | 6.3 | 0.950 | 0.10 | 0.017 |
| 2000 | 0.90 | 935 | 79.627 | 83.711 | -4.0840 | -4.88e-02 | 2.27 | 874 | 1.549 | 7.3 | 0.706 | 0.10 | 0.017 |
| 4000 | 0.90 | 1745 | 152.486 | 154.994 | -2.5080 | -1.62e-02 | 1.03 | 1793 | 1.190 | 18.6 | 0.792 | 0.10 | 0.017 |
| 8000 | 0.90 | 3257 | 284.437 | 285.388 | -0.9517 | -3.34e-03 | 0.29 | 3621 | 1.425 | 21.8 | 0.917 | 0.10 | 0.017 |
| 16000 | 0.90 | 6077 | 529.491 | 535.453 | -5.9618 | -1.11e-02 | 1.32 | 7717 | 1.680 | 34.0 | 0.740 | 0.10 | 0.017 |
| 24000 | 0.90 | 8754 | 771.494 | 772.741 | -1.2464 | -1.61e-03 | 0.23 | 11977 | 1.995 | 51.1 | 0.909 | 0.10 | 0.017 |

| ρ | fitted exponent of \|S\| in D (± s.e.) | of P | of H | fitted e(D) = log(P/\|S\|)/log D, mean |
|---|---|---|---|---|
| 0.60 | 2.17 ± 0.53 | 1.052 ± 0.009 | 0.60 | 1.19 |
| 0.75 | -0.41 ± 0.67 | 1.052 ± 0.009 | 0.75 | 0.92 |
| 0.90 | -0.21 ± 0.43 | 1.052 ± 0.009 | 0.90 | 0.81 |

The `|S|` fits are dominated by sign changes of `S` (for example `S = 0.005` at `D = 2000, ρ = 0.6`), so no growth
exponent of `|S|` is resolvable on this range. The robust statements are `max |S| = 5.96` over all 18 cells,
and `P ∝ D^{1.05}` (that is, `D log D`).


**Readings.**
* `|S|` stays below 6 while `H` grows to `9·10³`; `|S|/H ≤ 0.71 %` throughout. So the signed dual is far below
  its target `H`.
* `|S|` is the size of an **independent-row model**: if the `|A_u|²/D` were independent exponentials with the
  observed mean, `S` would fluctuate by `s_rand = Diag·(Σφ²)^{1/2}/Σφ ≈ 0.66·Diag/H^{1/2} ≍ H^{1/2}`. The
  observed `|S|/s_rand` lies in `[0.01, 2.27]` with median about 0.6. Under that model
  `e → 1 − ρ/2` (0.70 / 0.625 / 0.55). The finite values `e = 0.70–1.59` are inflated by the logarithms in `P`.
  Both exceed `1 − ρ` (needed for Mom(1, ρ)) and `(1 − ρ)/6` (needed to beat 11/12). HB00-type routes (§2)
  predict `e = 0`. The actual cancellation is the generic random-sign cancellation of RUNG_STRENGTH §5;
  nothing Möbius-specific is visible at this scale.
* `S < 0` in most cells: the coprimality-corrected `Z` slightly exceeds `𝓜_D`. The sixth-power rows contribute
  `Prin ≈ 0.3–2`. That is about what 18 rows of average size give, so there is no excess on the principal
  rows at this scale (`|A₁(D)| = 51 ≈ D^{0.39}` at `D = 24000`).
* Block shares of `P` (ledger C3, exact enumeration): `N f < D^{2/3}` carries 0.569 / 0.589 / 0.605, and
  `f = 1` carries 0.314 / 0.259 / 0.224, at `D = 10³ / 10⁴ / 10⁵`.

## 5. Re-examined claims

* DISPERSION_GRH_STEP §4 ("first loss is positivity, cost `D^{1−ρ}`"): **confirmed** for Mom(1, ρ) itself.
  **Refined**: to improve on 11/12 only `D^{(1−ρ)/6+}` is needed (Prop. L), and that is exactly the principal
  member's margin. **Sharpened**: by Prop. G the loss is not "μ(f) made positive" in any arithmetic sense. The
  exact identity has no Möbius variable outside the `g | k` terms. Positivity re-creates the dual diagonal by
  undoing the coprimality `(z₁, z₂) = 1`.
* "DR's route is circular": **confirmed, and the reason is visible term by term** (Cor. N). The surviving
  Möbius sums are original-family members of conductor `≍ Z²`. HB00/DR-type unconditional input (μ or Λ
  against Gauss sums) has no target in the exact signed dual.

## 6. What this note does not show

* Nothing about `A₁(D)` or any L-function is proved. Prop. G is an identity downstream of the imported,
  unreviewed eq:initial-column-output; Prop. L uses the imported, unreviewed extraction law.
* Lemma NRA excludes only *exact* finite-order modulation. It does not exclude an amplifier whose weight
  `ν_β` could be handled by some other analytic device.
* The amplifier ledger is exponent bookkeeping: logs, `D^ε`, cube removal (Oct 5 lem:cube-reduction) and
  the `F`-range are not tracked. Variant (q) assumes the quadratic large sieve applies to the product columns
  `(r, p)` after reflection, which was not checked against the reflected weights.
* R4 rests on an unestablished uniformity of the import in the row.
* Numerics: `D ≤ 24000`, one `W`, one `Φ`, `ν = 1`. `P` is the diagonal main term of the positivity bound,
  not the bound itself. Floating point, finite.

## 7. Single most promising next step

Attack (AMP_t) at its blocking term. Prove a version of Oct 5 prop:R for the *sum over* `ℓ` of `f`-shifted
completed sums, `Σ_k |Σ_{ℓ∼L} μ(ℓ)a(ℓ)χ_ℓ(k) T(X; k, ℓ)|²`, with reflected length growing slower than
`N(ℓ)` per prime. In exponent terms, the dual must close at `H ≥ D L^t`, `t < 6/5` (the payoff is
`λ(6−5t)/12`). The concrete question: after Patterson's transformation, does the cubic shift `ℓ⁴` cost the
full level factor `N(ℓ)` in the reflected length (prop:R's `N(f)`), or only `N(ℓ)^{1/5}`? The former is what
the manuscript proves.

## Files

* `README.md`: this note.
* `o2_ledger.py`: sympy ledger (L1–L4) and exact checks (C1 collapse identity, C2 weight identity, C3 block
  shares). Output: `results/o2_ledger.json`.
* `signed_dual_numerics.py`: signed dual, positivity proxy, principal-row share. Output:
  `results/signed_dual_main.json`, `results/signed_dual_main.log`.
