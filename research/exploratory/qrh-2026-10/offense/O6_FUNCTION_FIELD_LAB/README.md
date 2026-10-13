# O6: a function-field laboratory for the sextic Möbius family

```text
Status: EXPLORATION. Labelled claims: EXACT (integer / finite-field / cyclotomic-integer arithmetic,
  finite ranges), PROVED-HERE (short derivations in §2, not reviewed), EMPIRICAL (finite exact data read
  as trends), HEURISTIC, OPEN, LIT (primary source read). Nothing here bears on RH over Q, which is
  unsolved. No zero-free region over Q is claimed. The OpenAI Sep 30 / Oct 5 manuscripts are external,
  unreviewed imports; "Oct 5" below means paper2.tex (scratchpad copy, lines 301-660 and 1632-1915 read
  for Steps 3-5 and the reflection).
Scope: the Oct 5 family A_u = sum_n mu(n) chi_n(u) transplanted to F_q[T], q prime, q = 1 mod 6
  (q = 7, 13, 19, 31, 37; q = 13 also for the quartic family). Truth (the moments), the Step 3 pipeline
  (Poisson in u, Gauss-sum dual, Moebius absorption, Ramanujan blocks, positivity, dual mean square),
  the leverage rows, and a search for a lab mechanism for Mom(1, rho < 1).
Exact sources or dependencies: RUNG_STRENGTH.md, LEVERAGE_FAMILIES.md, DISPERSION_GRH_STEP.md,
  Q_RHO_ANALYSIS.md, moments/DUAL_ANATOMY.md (all in qrh-2026-10/); Oct 5 paper2.tex Steps 3-5 (read).
  LIT: J. Hoffstein, Invent. Math. 107 (1992) 61-86 (GDZ scan PPN356556735_0107 LOG_0009, sha256
  e82a32c6...5fc0c; pages 61-64 read as images: introduction and statement of results only).
  Sawin-Shusterman arXiv:1808.04001 (abstract only). Weil/Deligne RH over finite fields, Hasse-Davenport,
  Stickelberger/Pellet: classical, used only through identities that are checked EXACTLY below.
What was actually run (single-threaded, shared 4-core machine, every run < 20 min):
  lab_core.c (C, exact Z[omega] with __int128): q=7 (rows deg<=6, d<=30), q=13 (deg<=4, d<=24),
  q=19 (deg<=4, d<=20), q=31, 37 (deg<=3, d<=20); validate_core.py (brute force, q=7, d<=4, rows deg<=3:
  all 16 cells equal); gauss_exact.py (Z[zeta_N] exact: q=7 all 343 squarefree n of deg<=3; q=13 93 n);
  leverage_check.py (q=7, d<=4); dual_energy.c (q=7 d=4,5; q=13 d=3,4; q=19 d=3); ledger.py (q=7 d=2
  all M, d=3 M=2..4); pipeline_table.py, tables.py. Outputs in results/.
Smallest remaining gap: no lab mechanism proves Mom(1, rho < 1) without the Riemann hypothesis for the
  family members (Weil). The one genuinely new lab input (Pellet: mu(n) = (-1)^deg n chi_2(disc n),
  which makes every Gauss sum and mu itself a character of a polynomial in the coefficients of n) has
  no known number-field analogue (§6).
```

## 0. Findings in brief

1. **The Oct 5 Step 3 algebra is exact in the lab, and the Möbius absorption is an identity of
   Hasse–Davenport type.** (EXACT; §2.) For monic squarefree `n` of degree `d`,

       g_n(chi_n^j) = mu(n) (-g_j)^d chi0^j(Res(n, n')),            g_j = Gauss sum of chi0^j over F_q,

   checked in `Z[zeta_N]` for every `j = 1..5`, all 343 squarefree `n` of degree ≤ 3 over `F_7` and 93
   over `F_13`. Consequences, all EXACT on the same sets:
   * the Oct 5 identity `γ₁γ₂ = μ α G` holds with `α(n) = (−J/√q)^{deg n}` (`J = J(χ0², χ0²)`): the
     Jacobi-sum Hecke character becomes a pure **degree character**, unramified;
   * the cubic family absorbs μ into **one sextic Gauss sum** (`μγ₂ / γ₋₁` depends on `deg n` only);
   * the quartic family over `F_13` absorbs μ into `conj γ(χ₄)` (`μγ(χ₄)/conj γ(χ₄)` depends on `deg n` only);
   * controls: every identity fails without μ, at every `n` with `μ(n) = −1` (175/175, 56/56, ...).

   In the lab the "Möbius parity" that the absorption pays for is visible: it is the Hasse–Davenport sign
   `(−1)^{deg P − 1}` per prime, and **μ itself is a quadratic character of the discriminant**
   (Pellet/Stickelberger): `μ(n) = (−1)^d χ₂(disc n)`, EXACT for all 2401 squarefree monic `n` of degree
   ≤ 4 over `F_7`.
2. **Truth (EXACT integers).** `M₂(d; m) / Diag` is *not* ≈ 1 in the lab at small `q`. It is ≈ 1 only for
   rows of degree ≤ 2. Rows of degree 3–4 are **special members** whose Frobenius eigenvalues are
   repeated (`|A_u(d)|²/q^d ∈ {0, 1, (d+1)²}` for every degree-3 row over `F_13`), and they make the ratio
   grow polynomially in `d` at fixed row degree (e.g. q = 7, m = 6: ratio 2.1 at ρ = 1, 6.5 at ρ = 1/2,
   75 at ρ = 0.2). The excess does not shrink with `q` (q = 13, 19, 31, 37 all show it). This is
   harmless for exponents (Mom(1, ρ) is a `q^{o(d)}` statement) but it is a real **secondary term from
   small-conductor members**, the lab analogue of polylog factors. (EMPIRICAL on exact data; the
   finite-monodromy explanation is HEURISTIC.)
3. **Where the pipeline loses (EXACT ledger at small d).**
   * Poisson in `u` + Gauss sums + absorption: **no loss** (exact identity; replayed term by term at q = 7,
     d = 2 for all M, and d = 3 for M = 2..4, see §3).
   * The dual mean square is **diagonal-sized** at every sub-diagonal cell measured:
     `E/DD = 1.0028, 1.0094` (q = 7, d = 4, ρ_eff = M/d = 1/2, 3/4), `0.984, 0.988, 0.994` (q = 13, d = 3).
   * Hence positivity costs **exactly the dual diagonal**, `P/Diag = q^{d−M}·(E/DD)`: 49.2 and 7.07 against
     the predicted 49 and 7 (q = 7, d = 4), 167, 12.8, 0.994 against 169, 13, 1 (q = 13, d = 3).
   * The signed dual (= the truth, by the exact identity) is tiny: `Off/Diag = −0.0176` (q = 7, d = 4,
     M = 3) and `−0.0059` (q = 13, d = 3, M = 3). Signed saving over positivity: `κ = 0.77` and `0.67` in
     units of `log q^d`.
   * So **positivity is the first and dominant loss, and it is exactly `D^{1−ρ}`**: nothing else in Step 3
     loses at ρ < 1. The reflection cannot recover it (§4): the dual rows that matter have `deg h > d`,
     where the theta reflection lengthens the sum.
4. **Theta structure of the dual (EXACT data, LIT context).** The dual sums
   `B_h(d) = Σ_n χ0(Res(n,n')) conj χ_n(h)` vanish identically for `deg h = 1` and are 100×–300× below their
   diagonal at `deg h = 2` (q = 7, 13, 19); at the unit row `h = 1` they carry a large "Patterson" bias
   (`|B_1(4)|² = 36·7⁵` against 2058 columns at q = 7). This is Hoffstein's mechanism (LIT, read): over
   `F_q(T)` the Gauss-sum Dirichlet series are rational, and the theta coefficients come from the
   numerator. It acts only where `deg h ≲ d/2`, i.e. on the super-diagonal side.
5. **Mechanism search (§6).** No lab mechanism proves Mom(1, ρ < 1) without RH for the members.
   * The exact degree-generating series (`Σ_d A_u(d) x^d = 1/L(x, ψ_u)`) only restate the problem: the
     growth rate of `M₂` in `d` is the location of the inverse roots.
   * The only genuinely new input in the lab is Pellet's identity. It turns `A_u(d)` into a single
     multiplicative character sum over `F_q^d` of the polynomial `disc(n)³·Res(n, u)`. Deligne's theorem
     (Weil II) on that variety then controls everything for `q` large relative to `d`. That is a
     geometric mechanism with no number-field analogue known to us (OPEN / HEURISTIC).
   * The Sawin–Shusterman char-`p` refinement (μ mimicked by Dirichlet characters on special subspaces)
     is the strongest version (LIT, abstract only). It too has no Z-analogue.

**Most promising next step.** Measure, in the lab, the *block-signed* dual
`Σ_f μ(f)·Block(e, f)` at ρ < 1 for `d = 4, 5` (ledger.py is ready; it needs a C port), and test whether
the cancellation between Möbius blocks is carried by the Pellet character `χ₂(disc)`. If it is, the
number-field question becomes concrete: find a substitute for "μ is a quadratic character of a
discriminant" acting on the dual Möbius variable `f` only.

## 1. The lab

* `q` prime, `q ≡ 1 (mod 6)`, `g` the least primitive root, `χ0(a) = ζ₆^{log_g a}` (order 6 on `F_q^*`).
* Columns: monic `n ∈ F_q[T]`, `deg n = d`. Rows: `u ∈ F_q[T]`, `deg u ≤ m`, either monic or all
  (`|A_{cu}| = |A_u|` for `c ∈ F_q^*`, so the two differ by the factor `q − 1`).
* Sextic symbol: `χ_n(u) = (u/n)₆ = χ0(Res(n, u))`, using `(u/P)₆ = χ0(N_{F_P/F_q}(u mod P))` and
  `N(u mod P) = Res(P, u)`. Reciprocity is `χ_n(u) = χ0(−1)^{deg n·deg u} ψ_u(n)`, where
  `ψ_u(n) = χ0(Res(u, n))` is a Dirichlet character mod `u`.
* Family: `A_u(d) = Σ_{deg n = d} μ(n) χ_n(u) = χ0(−1)^{d·deg u}·[x^d] 1/L(x, ψ_u)`.
  `L(x, ψ_u)` is a polynomial of degree `< deg u` unless `u = v⁶`. Rows `deg u ≤ ρd` play `N u ≤ D^ρ`,
  with `D = q^d`.
* Moments: `M₂(d; m) = Σ_{u monic, deg u ≤ m} |A_u(d)|²`. The exact diagonal is
  `Diag = Σ_u #{n squarefree, deg n = d, (n, u) = 1}`, from `(1 − qx²)/(1 − qx) / Π_{P|u}(1 + x^{deg P})`.
* `lab_core.c` computes `L(x, ψ_u)` exactly in `Z[ω]` from its Euler product over primes `P`,
  `deg P < deg u`. It inverts the series to degree `d_max` (`__int128`) and accumulates `M₂` and
  `Diag` as integers.
* **Validation (EXACT).** `validate_core.py` recomputes `M₂` and `Diag` from the definition, i.e. a
  brute-force Möbius sum with resultants, for q = 7, `d ≤ 4`, rows of exact degree `k ≤ 3`. All 16 cells
  agree.

## 2. Exact identities (PROVED-HERE derivation + EXACT checks)

**2.1 Gauss sums.** For `A = F_q[T]/(n)`, `n` squarefree, `A` is étale: `χ_n(x) = χ0(N_A x)`. The residue
`res(x/n)` is the coefficient of `T^{d−1}` in `x`, and it equals `Tr_A(x/n'(θ))` (Euler's partial fractions).
Substituting `x ↦ x·n'(θ)` and applying Hasse–Davenport on each factor `F_{q^k}` gives

    g_n(χ_n^j) := Σ_{x mod n} χ_n(x)^j e(res(x/n)) = χ0^j(Res(n, n')) · Π_{P|n} (−(−g_j)^{deg P})
               = μ(n) (−g_j)^{deg n} χ0^j(Res(n, n')).                                          (HD)

EXACT check (`gauss_exact.py`, `Z[ζ_N]` reduced mod `Φ_N`): 343/343 (q = 7), 93/93 (q = 13, sextic),
93/93 (q = 13, quartic), every `j`. Control: dropping μ fails at every `n` with `μ(n) = −1`.

**2.2 Absorption.** From (HD) and the Hasse–Davenport product formula over `F_q`:
* `g_n(χ)g_n(χ²) = μ(n)(−J)^{deg n} conj(χ_n(4)) g_n(χ³)`, `J = J(χ0², χ0²)`. EXACT: 343/343 and 93/93.
  Normalized, this is the Oct 5 eq:gj `γ₁γ₂ = μαG`, with `α(n) = (−J/√q)^{deg n}`. The `−J` equals the
  primary `π | q` (the classical Jacobi-sum sign `J = −π`), so **α is the Frobenius angle of the CM curve,
  raised to the degree**: an unramified, infinite-order Hecke character.
* **Pellet**: `χ0³(Res(n, n')) = χ₂(Res(n, n')) = (−1)^d μ(n) χ₂(−1)^{d(d−1)/2}`, i.e.
  `μ(n) = (−1)^d χ₂(disc n)`. EXACT: 2401 squarefree monic `n` of degree ≤ 4 over `F_7`. The quadratic
  factor `G(n)` of Oct 5 is therefore a function of `deg n` alone (Gauss's evaluation, lab form).
* **Cubic family** (row symbol `χ²`, LEVERAGE_FAMILIES S6): `μ(n)g_n(χ²) = c_d·g_n(χ⁵)` with `c_d`
  depending on `d` only. EXACT: 340/340 (q = 7), 90/90 (q = 13); fails without μ (168/168, 41/41).
* **Quartic family** (q = 13, `χ₄` of order 4): `μ(n)g_n(χ₄) = c'_d·conj g_n(χ₄)`. EXACT: 90/90;
  fails without μ (41/41).

So in the lab all three absorptions of LEVERAGE_FAMILIES hold. The cubic family's single-sextic-Gauss-sum
absorption, open over Q only at the level of the theta coefficient (S6), is an identity here, and so is
the quartic one. The binding question in the lab is never absorption. It is the size of the dual.

**2.3 Leverage rows** (`leverage_check.py`, q = 7, `d ≤ 4`, EXACT):
* `A_{v⁶}(d) = [x^d](1 − qx)Π_{P|v}(1 − x^{deg P})^{−1}`: verified for `v = T+1`, `T²+1`. In particular
  `A_1(d) = 0` for `d ≥ 2`. **`F_q[T]` has no zeta zeros, so the principal-row extraction is vacuous in
  the lab.** It becomes meaningful only for a twisted target `ν = ψ_w`, i.e. for the member rows `w v⁶`.
* `A_{wv⁶}(d) = Σ_j χ_v(w)^j A_w(d−j)` (RUNG_STRENGTH Prop. R′ step 3), verified for three `(w, v)`
  with `deg u = 8, 9`.
* **Lab Prop. R (exact):** `Σ_d A_w(d)x^d = 1/L(x, ψ_w)` is rational, so `limsup |A_w(d)|^{1/d}` is
  *equal* to the largest inverse root. The Mellin step of Prop. R is an equivalence here. By Weil it is
  `√q`, so the lab truth for each member is `σ = 1/2`. The extraction from a diagonal-sized `M₂` returns
  `1/2 + 5ρ/12`, whatever the true member size. **The extraction loses `5ρ/12` even when fed the exact
  truth.** This is not a pipeline defect; it is the leverage law.

## 3. Truth: the moments (EXACT integers; ratios printed)

`R(d; m) = M₂/Diag` over monic rows of degree ≤ m (`results/tables.md`; selected cells):

| q | m | d = m (ρ = 1) | ρ ≈ 3/4 | ρ ≈ 1/2 | ρ ≈ 1/4 | d = 30 or 24 or 20 |
|---|---|---|---|---|---|---|
| 7 | 2 | 1.000 | 0.982 (d=3) | 0.982 (d=4) | 0.982 (d=8) | 0.982 |
| 7 | 5 | 1.000 (d=5) | 3.535 (d=10)... see table | — | — | 20.5 |
| 7 | 6 | 2.12 (d=6) | 2.84 (d=8) | 6.53 (d=12) | 37.0 (d=24) | 74.6 |
| 13 | 4 | 2.51 (d=4) | 4.87 (d=6)* | 8.09 (d=8) | 51.5 (d=16) | 190.6 |
| 19 | 4 | 2.65 (d=4) | — | 9.71 (d=8) | 70.9 (d=16) | 147.0 (d=20) |
| 37 | 3 | 2.89 (d=4) | — | 4.73 (d=6) | 13.9 (d=12) | 34.1 (d=20) |

(*`d = 6` is ρ = 2/3.) Exact integers for every `(d, m)` are in `results/core_q*.txt`, columns
`d k rows M2_k Diag_k max_k`.

* **Rows of degree ≤ 2 are diagonal-sized** (ratio 0.98–1.0). Their `L` has degree ≤ 1.
* **Rows of degree 3 and 4 are special.** At q = 13, every degree-3 row has `|A_u(8)|²/q⁸ ∈ {0, 1, 81}`
  (130 rows with 81 = (d+1)², 702 with 1, 1365 with 0). At q = 7, 13, 19, 31, 37 the maximum over
  degree-3 rows is exactly `(d+1)² q^d`: `L(x, ψ_u) = (1 − αx)²` for some members. For degree-4 rows
  the maximum is `binom(d+2, 2)² q^d` at q = 13, 19 (triple root) and `(d+1)² q^d` at q = 7.
  HEURISTIC reading: the rank-2 (resp. 3) sextic Kummer local systems of `y⁶ = u(T)` with `deg u = 3, 4`
  have finite (hypergeometric) monodromy, so their Frobenius eigenvalues are `√q` times roots of unity
  times a fixed angle. Random-matrix (Katz–Sarnak) behaviour is not available at these degrees.
* **Consequence.** At fixed row degree the ratio grows like a power of `d`. It does not decrease with `q`
  (q = 31, 37 at m = 3 match q = 13). The lab "truth" is diagonal-sized only up to factors polynomial in
  `d`, i.e. `q^{o(d)}`, carried by a few small-conductor members. That is exactly the precision in which
  Mom(1, ρ) is stated, so this does not contradict it. It does mean the clean `M₂ ≈ Diag` seen over
  `Q(ω)` (RUNG_STRENGTH §5, ratios 0.88–0.95) is **not** a law of the family. It is what the family
  looks like when no member has clustered zeros. (EMPIRICAL; uniformity in `d` is not proved here.)
* **What proves Mom(1, ρ) in the lab** (LIT-level standard argument, not re-derived here): Weil's RH for
  each `L(x, ψ_u)` plus the explicit formula with short prime sums (Altug–Tsimerman type) gives
  `|A_u(d)| ≤ q^{d/2 + O(d/ log_q d)}` uniformly for `deg u ≤ Cd`. Hence `M₂ ≤ q^{d(1+ρ) + o(d)}`. This is
  the "GRH ⇒ Mom(1, ρ → 0)" direction of RUNG_STRENGTH §2, and it uses RH for every member.

## 4. The Step 3 pipeline, measured (EXACT)

**4.1 The exact dual.** (PROVED-HERE, standard finite Fourier analysis on `F_q[T]/(Q)`.) Rows `u ∈ V_M`
(`deg u < M`, `q^M` rows). Write `n₁ = ga`, `n₂ = gb`, `(a, b) = 1`, `deg a = deg b = δ`, and let
`V_M^⊥ = V_{d+δ−M}` under `⟨u, h⟩ = e(res(uh/Q))`. With (HD) and `χ_a(b)conj χ_b(a) = χ0(−1)^δ` (lab
reciprocity), all Gauss sums and all μ's cancel into

    M₂ = Σ_g q^{M−d} Σ_{h ∈ V_{d+δ−M}} c_g(h) I(g, h),
    I(g, h) = Σ_{(a,b)=1} β_h(a)χ_a(g) · conj(β_h(b)χ_b(g)),     β_h(a) = χ0(Res(a, a')) conj χ_a(h),

where `c_g(h) = Σ_{e | (g,h)} μ(g/e)|e|` is the Ramanujan sum and `f = g/e` is the Oct 5 Möbius variable.
`ledger.py` evaluates both sides exactly. Primal = dual at q = 7, d = 2 for all M = 1..4, and at d = 3
for M = 2, 3, 4 (see `results/ledger_q7_d*.log`). The `ω`-part of the dual total is 0, as it must be.

**4.2 Positivity and the dual mean square.** The Oct 5 positivity step (eq:weighted) bounds the blocks by
the full dual mean square, here `E(K) = Σ_{h ∈ V_K}|B_h|²` with `B_h = Σ_n β_h(n)` and `K = 2d − M`.
`DD(K)` is its diagonal. `dual_energy.c` computes both exactly; `pipeline_table.py` combines them with the
truth.

| q | d | M | rows q^M | ρ_eff = M/d | Off/Diag (truth = signed dual) | P/Diag (after positivity) | q^{d−M} | E/DD | κ |
|---|---|---|---|---|---|---|---|---|---|
| 7 | 4 | 2 | 49 | 0.50 | −1 (all rows have `L ≡ 1`) | 49.16 | 49 | 1.0028 | 0.50 |
| 7 | 4 | 3 | 343 | 0.75 | **−0.0176** | **7.07** | 7 | **1.0094** | 0.77 |
| 7 | 4 | 4 | 2401 | 1.00 | +1.386 (special rows) | 1.90 | 1 | 1.905 | 0.04 |
| 7 | 5 | 5 | 16807 | 1.00 | +1.104 | 1.35 | 1 | 1.346 | 0.02 |
| 13 | 3 | 1 | 13 | 0.33 | −1 (`L ≡ 1`) | 167.2 | 169 | 0.984 | 0.67 |
| 13 | 3 | 2 | 169 | 0.67 | −1 (`L ≡ 1`) | 12.85 | 13 | 0.988 | 0.33 |
| 13 | 3 | 3 | 2197 | 1.00 | **−0.0059** | **0.994** | 1 | **0.994** | 0.67 |

Here `P = q^{M−d}E` and `κ = log(P/|Off|)/log q^d`. Rows with `−1` have `M₂ = 0` exactly: every row of
degree ≤ 1 has `L(x, ψ_u) = 1`.

Reading (EXACT on these cells; the trend is EMPIRICAL):
* **The dual mean square is diagonal-sized** whenever the dual has more rows than columns
  (`E/DD ∈ [0.984, 1.010]`). This is the lab version of A2_LITERATURE §5 and DUAL_ANATOMY §4, where the
  Q-side gives `DD ≈ 1.3(D/Y)Diag`.
* **Positivity therefore costs exactly `q^{d−M}`**, i.e. `D^{1−ρ}`: the dual diagonal, which the exact
  identity does not contain (§4.1 has `(a, b) = 1`).
* **The signed dual is the truth**, and the truth is tiny wherever the rows are generic (−1.8 %, −0.6 %).
  The saving of the signed dual over positivity is `κ ≈ (1 − ρ) + κ₀`, where `κ₀` is the truth's own
  random-type cancellation (≈ 0.5 here).
* **Positivity is the only loss in Step 3.** Poisson, the Gauss sums and absorption are exact; the dual
  mean square is not larger than its diagonal. Steps 4–5 (reflection and quadratic large sieve) can only
  add the factor `𝓗/X` of DISPERSION_GRH_STEP §4, because:
* **The reflection acts on the wrong rows.** The per-degree dual energies (`results/de_*.txt`) are:

  | q, d | deg h = 0 (h unit) | 1 | 2 | 3 | 4 | 5 |
  |---|---|---|---|---|---|---|
  | 7, 4: `E_k/DD_k` | 294 (bias) | 0 | 0.023 | 1.24 | 0.86 | 1.0017 |
  | 7, 5 | 0 | 0 | 0.0033 | 0.106 | 1.55 | (running) |
  | 13, 3 | 156 (bias) | 0 | 0.083 | 0.988 | 0.983 | — |

  `B_h(d)` vanishes, or nearly vanishes, for `deg h ≤ d/2`. That is the region where the theta
  reflection (Hoffstein: rational Gauss-sum series, polar term = theta coefficient) leaves only the polar
  term. But at ρ < 1 the dual rows run up to `deg h = 2d − M > d`. There the energy is diagonal, and the
  reflection maps length `d` to `2 deg h − d > d`. The reflection helps exactly on the ρ > 1 side.
* At ρ ≥ 1 (`M ≥ d`) the truth is **not** small in the lab (`Off/Diag = +0.4…+1.4`). This comes from the
  special members of §3. In the dual it sits in the unit row `h ∈ F_q^*` (the "Patterson bias"
  `|B_1(d)|²`, e.g. `36·7⁵` at q = 7, d = 4) and in `deg h = d − 1`.

## 5. Function-field structure: Hoffstein, and the alternative pipelines

* **Hoffstein 1992 (LIT; pp. 61–64 read).**
  * Over `F_q(T)` "a Dirichlet series is a power series, and any power series with a functional equation
    and known polar behavior can be expressed as a rational function". The theta residues are then
    expressed through the numerator.
  * For `deg m ≤ n − 1` the `n`-th order theta coefficient `a(m)` is "essentially an average of Gauss
    sums" (Thm 4.2).
  * For `3 ≤ n ≤ 6`, Cors. 4.6–4.9 reduce it to "a single Gauss sum multiplied by a certain
    generalization of a Jacobi sum".
  * Patterson's quartic conjecture is proved over `F_q(T)`.
  * The author warns: for `n = 4` and `deg p = 1` one has `a(p) = 0`, so "the relation between
    coefficients and Gauss sums is true, but vacuous", and "it is easy to be misled" when transferring
    to number fields.

  We did not read §§1–5 or the Corollaries themselves, so **the sextic coefficient formula (Cor. 4.9,
  n = 6) is not verified here**.
* **Lab consistency with that warning (EXACT data, §4.2).**
  * The sextic-family dual sums vanish identically at `deg h = 1`: `E₁ = 0` at q = 7 (d = 3, 4, 5),
    q = 13 (d = 3, 4) and q = 19 (d = 3).
  * This is the lab counterpart of `a(p) = 0` for `deg p = 1`.
* **Cubic family with sextic absorption (§2.2): absorption EXACT, reflection not run.**
  * In the lab the absorbed dual coefficient is `χ0⁵(Res(n, n'))`, an order-6 "discriminant character".
  * Pellet gives its quadratic part as `χ₂(Res(n, n')) = ±μ(n)` (a function of `deg n` times μ).
  * So after one more absorption the post-reflection quadratic twist of LEVERAGE_FAMILIES §3.2 would be
    a twist by `μ` itself (up to degree factors). That is the parity problem reappearing in the dual
    (HEURISTIC).
  * Whether the sextic-theta reflection produces a quadratic twist **in the row `h`**, as Oct 5 needs,
    was **not computed** (OPEN; see §7).
* **Quartic family (q = 13): absorption EXACT** (§2.2). Its reflection was not run.

## 6. Mechanism search: what the lab has that Q does not

1. **Rational generating series in the degree** (EXACT): `Σ_d A_u(d)x^d = 1/L(x, ψ_u)`. Also
   `Σ_d M₂(d; m)x^d = Σ_u` (Hadamard square), a rational function with poles at `1/(α_i conj α_j)`. Its
   radius is `1/q` iff every member satisfies RH. **So rationality restates Mom(1, ρ → 0) as GRH for the
   family. It gives no independent proof.**
2. **Degree functional equations** (HEURISTIC; not computed). The `x ↔ 1/(qx)` symmetry of `L(x, ψ_u)`
   makes `1/L(x₁, ψ_u)·1/L(x₂, conj ψ_u)` transform by `(q x₁ x₂)^{−(deg u−1)}·ψ_u(−1)`: the root numbers
   cancel in the second moment.
   * Hence the double series `Z(x₁, x₂, y) = Σ_u y^{deg u}/(L(x₁, ψ_u)L(x₂, conj ψ_u))` should satisfy a
     functional equation `(x₁, x₂, y) ↦ (1/(qx₂), 1/(qx₁), y/(q x₁ x₂))` with no Gauss sums.
   * Poisson in `u` (y-direction) introduces sextic Gauss sums, i.e. 6-fold Kubota series in the dual
     variable.
   * Whether the group generated is finite (which would make `Z` rational with computable denominator,
     DGH/Bucur–Diaconu style, **and would evaluate `M₂` at ρ < 1 exactly without RH for individual
     members**) is OPEN.
   * This is the single concrete lab question whose positive answer would be a new mechanism. Its
     number-field analogue would be a multiple Dirichlet series for the *second moment of `1/L`* over the
     sextic family.
3. **Pellet's identity** (EXACT): `μ(n) = (−1)^{deg n}χ₂(disc n)`.
   * With it, `A_u(d) = (−1)^d Σ_{a ∈ F_q^d} χ0(disc(n_a)³·Res(n_a, u))` is one character sum over affine
     space.
   * `M₂` is a character sum over a variety of dimension `2d + M`. Weil II gives it at
     `q^{(2d+M)/2}·(Betti)`, far below `Diag ≈ q^{d+M}`, once `q` is large in terms of `d` (Katz-type
     equidistribution). That is a proof of Mom(1, ρ) in the large-`q` limit **from Weil II**, which
     contains RH for every member, so it is not RH-free.
   * At fixed `q` the Betti numbers grow and this route needs the Sawin–Shusterman refinement (LIT,
     abstract only): μ "mimicked by Dirichlet characters on special subspaces", giving a Möbius level of
     distribution close to 1. That is beyond what pointwise RH gives.
   * **Number-field analogue: none known to us.** Over Z there is no polynomial whose quadratic character
     is μ, and no `p`-th-power subspaces. This is the parity barrier in its sharpest form.
4. **Answer to the prize question.** In the lab the sub-diagonal second moment is true, and the known proofs
   all go through RH for the members (Weil, or Weil II on the Pellet variety). No exact identity,
   rationality, or degree functional equation found here proves Mom(1, ρ < 1) by itself. The one open lab
   avenue is the finite-group question in item 2.

## 7. Comparison with the Q side, and what was not done

| quantity | lab (F_q[T], this note) | Q(ω) (moments/, a2/) |
|---|---|---|
| `M₂/Diag`, generic rows, ρ < 1 | 0.98–1.0 (rows deg ≤ 2); 0.98 (q = 7, d = 4, M = 3); 0.994 (q = 13, d = 3) | 0.88–0.95 (RUNG_STRENGTH §5), random-sign-like (DUAL_ANATOMY) |
| special members | finite-monodromy rows, polynomial excess in `d` | none seen at `D ≤ 64000` |
| dual mean square / its diagonal | 0.984–1.009 | 0.97–1.14 (A2_LITERATURE §5) |
| positivity cost | exactly `q^{d−M}` | `≈ 1.3 D/Y` (DUAL_ANATOMY §4) |
| signed dual / diagonal | −1.8 %, −0.6 % | within random spread, `≤ 0.18` |
| absorption | exact identity (HD + Pellet) | exact at primes; theta coefficient needed (S6 open for cubic) |

**Not done.**
* The full Ramanujan-block positivity ledger (`T1`, `T2` in ledger.py) beyond `d = 3`.
* Any computation of the lab theta reflection: the functional equation of `Σ_d B_h(d)x^d`, and the
  post-reflection twist in `h`.
* Hoffstein §§1–5 and his `n = 6` corollary.
* The multiple-Dirichlet-series group of §6.2.
* Rows of degree ≥ 7 at q = 7, where Katz–Sarnak behaviour should take over. These are needed to separate
  special-member effects from genuine sub-diagonal behaviour at fixed ρ.

## Files

| file | role |
|---|---|
| `lab_core.c` | exact `A_u(d)` for all monic rows `deg u ≤ m`, all `d ≤ d_max`; `M₂`, `Diag`, max |
| `ffcommon.py` | exact `F_q[T]` arithmetic (resultants, Möbius, primes) |
| `validate_core.py` | brute-force replay of lab_core and of Pellet |
| `gauss_exact.py` | (HD), eq:gj, cubic (S6) and quartic absorption, in `Z[ζ_N]` |
| `leverage_check.py` | sixth-power rows and member rows `w v⁶` |
| `dual_energy.c` | dual sums `B_h(d)` and their mean square, by `deg h` |
| `ledger.py` | exact primal = dual identity, Ramanujan blocks, positivity ledger (small `d`) |
| `tables.py`, `pipeline_table.py` | tables from the outputs |
| `results/` | core outputs (`d k rows M2 Diag max`), dual energies, ledgers, identity checks |

Reproduction: `gcc -O2 -o lab_core lab_core.c && ./lab_core 7 6 30 > results/core_q7_m6_d30.txt`
(about 10 min on the shared machine); `gcc -O2 -o dual_energy dual_energy.c && ./dual_energy 7 4 6`;
`python3 gauss_exact.py 7 6 3`; `python3 ledger.py 7 2`; `python3 pipeline_table.py
results/core_q7_m6_d30.txt results/de_7_4.txt`.
