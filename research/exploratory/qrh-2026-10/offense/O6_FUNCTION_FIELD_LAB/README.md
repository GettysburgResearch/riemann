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
  leverage_check.py (q=7, d<=4); dual_energy.c (q=7 d=3,4,5; q=13 d=3,4; q=19 d=3); ledger.py (q=7 d=2
  M=1..4, d=3 M=1..5); theta_series.c (q=7 d<=8, deg h<=2; q=13 d<=6, deg h<=1); lab_sample.c
  (random rows of one degree, exact per row: q=7 m=7 N=3000, m=8 N=400, m=9 N=80; q=13 m=7 N=150);
  dual_sample.c (random dual rows, exact per row, q=7 d=7); pipeline_table.py, tables.py,
  sample_table.py, row_anatomy.py; Round 2 (§8): lab_mds.c (q=7, deg u<=5, d<=38), mds_test.py,
  pole_census.py (deg u = 3..6), 16 random degree-7 rows. Outputs in results/ (about 0.25 MB).
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
2. **Truth (EXACT integers), and a lab-specific degeneracy.** `M₂(d; m)/Diag` is *not* ≈ 1 in the lab
   for row degree `m ≤ 6`. Among those rows it is ≈ 1 only for degree ≤ 2.
   * Rows of degree 3–6 are **CM members**. The `ψ`-eigenspace of `H¹(y⁶ = u)` has `h^{0,1} = ⌈m/6⌉ − 1 = 0`,
     hence finite monodromy (HEURISTIC, Deligne–Mostow-type count).
   * Their Frobenius angles lie in cosets `θ₀ + (1/N)Z`, and they have repeated roots. Census at q = 13,
     degree 3: `|A_u(8)|²/q⁸ ∈ {0, 1, 81}` (EXACT).
   * They make the ratio grow polynomially in `d` and do not fade as `q` grows. Examples at q = 7, m = 6:
     2.1 at ρ = 1, 6.5 at ρ = 1/2, 75 at ρ = 0.2.
   * Generic members (infinite monodromy) start at row degree 7. Sampled with exact per-row arithmetic
     (§3.1; q = 7, `m = 7`, 3000 rows), they give `M₂/Diag = 0.91–0.96` for ρ ∈ [0.7, 1.17] and
     1.01–1.07 for ρ ∈ [0.39, 0.58]. That is the `Q(ω)` picture (0.88–0.95). The ratio drifts slowly up
     as ρ → 0 (1.22 ± 0.08 at ρ = 0.29), as expected from heavy-tailed per-member constants. At
     `m = 8` (400 rows) the values are 1.05–1.13 for ρ ∈ [0.73, 1.14] and 1.3–1.5 (± 0.2) at
     ρ = 0.5–0.67 (EMPIRICAL).
   * This is harmless for exponents (Mom(1, ρ) is a `q^{o(d)}` statement). It has no number-field
     analogue, since Hecke L-functions have no Hodge type, and it means the lab must be run at row
     degree ≥ 7 to say anything about generic members.
3. **Where the pipeline loses (EXACT ledger at small d; §4).**
   * Poisson in `u`, the Gauss sums and the absorption lose **nothing**. The primal = dual identity was
     replayed in exact integers at q = 7, `d = 2` (M = 1..4) and `d = 3` (M = 1..5).
   * The dual mean square is **diagonal-sized** whenever the dual has more rows than columns:
     `E/DD ∈ [0.949, 1.009]` over 12 exact cells (q = 7, d = 3, 4, 5; q = 13, d = 3; q = 19, d = 3).
     Sampled at q = 7, d = 7, the values are `0.93 ± 0.06`, `1.08 ± 0.07` and `1.06 ± 0.08` at
     deg h = 7, 8, 9.
   * Hence positivity costs **exactly the dual diagonal**, `P/Diag = q^{d−M}·(E/DD)`. Examples:
     * 350, 49.2, 7.07 against the predicted 343, 49, 7 (q = 7, d = 4, M = 1, 2, 3);
     * 6.93 against 7 (q = 7, d = 5, M = 4);
     * 167, 12.8 against 169, 13 (q = 13, d = 3).
   * The block ledger at q = 7, `d = 3` separates two stages. Taking `|μ(f)|` over the Ramanujan blocks
     costs `T1/Diag` = 9.9, 1.24, 0.11 at ρ_eff = M/d = 1/3, 2/3, 1. Relaxing to mean squares then costs
     `T2/Diag` = 63.7, 7.8, 1.14, essentially all of it dual diagonal (64.7, 8.9, 1.26). The truths are
     `Off/Diag = −1, −1, −0.020`.
   * So **positivity is the first and dominant loss, and it is exactly `D^{1−ρ}`**. Nothing else in Step 3
     loses at ρ < 1. The reflection cannot recover it (item 4): the dual rows that matter have
     `deg h > d`, where the theta reflection lengthens the sum.
   * Caveat: at the accessible sub-diagonal sizes the lab truth is carried by degenerate members. Rows of
     degree ≤ 1 have `L ≡ 1`, so `M₂ = 0` and `Off = −Diag`. Rows of degree 2 have `|A_u|² = q^d`
     exactly. Rows of degree 3 are special (item 2). So "the signed dual is small" is exact but **not yet
     a test on generic members**.
4. **Theta structure of the dual (EXACT data; LIT context).** The dual sums are
   `B_h(d) = Σ_n χ0(Res(n,n')) conj χ_n(h)` (`theta_series.c`).
   * They **vanish identically for `deg h = 1`**: every `d ≤ 8` at q = 7, every `d ≤ 6` at q = 13.
   * At `deg h = 2` (q = 7), `Σ_h |B_h(d)|² = 6q^{2+⌊d/3⌋}` for `d = 1..8`. Against the diagonal
     `≈ q^{d+2}` this is a vanishing fraction.
   * At the unit row, `|B_1(d)|² = (q−1)² q^{e(d)}` with `e = 3, 5, 8, 10` at `d = 3, 4, 6, 7`
     (`|B_1(1)|² = q²`), and `B_1(d) = 0` at `d = 2, 5, 8`. This is identical at q = 7 (d ≤ 8) and
     q = 13 (d ≤ 6). So `|B_1(d)| ≍ q^{5d/6}`:
     **the Patterson cubic-theta bias exponent 5/6**, as it must be, since absorption turned the sextic
     Möbius dual into cubic Gauss sums.
   * This is Hoffstein's mechanism (LIT, read): over `F_q(T)` the Gauss-sum Dirichlet series are rational,
     and the theta coefficients come from the numerator. It acts only where `deg h ≲ d/2`, i.e. on the
     super-diagonal side.
5. **Mechanism search (§6).** No lab mechanism proves Mom(1, ρ < 1) without RH for the members.
   * The exact degree-generating series (`Σ_d A_u(d) x^d = 1/L(x, ψ_u)`) only restate the problem: the
     growth rate of `M₂` in `d` is the location of the inverse roots.
   * The only genuinely new input in the lab is Pellet's identity. It turns `A_u(d)` into a single
     multiplicative character sum over `F_q^d` of the polynomial `disc(n)³·Res(n, u)`. Deligne's theorem
     (Weil II) on that variety then controls everything for `q` large relative to `d`. That is a
     geometric mechanism with no number-field analogue known to us (OPEN / HEURISTIC).
   * The Sawin–Shusterman char-`p` refinement (μ mimicked by Dirichlet characters on special subspaces)
     is the strongest version (LIT, abstract only). It too has no Z-analogue.
   * **Round 2 (§8): no finite-group multiple Dirichlet series for the second moment of 1/L.** The `y^k`
     coefficients of `Σ_u y^{deg u}/(L(x₁,ψ_u)L(x₂,conj ψ_u))` have `x`-denominators of exact recurrence
     order 1, 2, 7, 14 and ≥ 20 for `k = 1..5`, with new cyclotomic poles at each `k`. Members of degree 7
     have generic (non-torsion) pole angles. The control (moments of `L`) is rational with two polar lines
     on the same slice.

**Most promising next step.**
1. Run the Step 3 ledger (`ledger.py`, ported to C) on **generic members**: row degree ≥ 7, so
   `d ≥ 8` at ρ < 1.
2. Measure there the block-signed dual `Σ_f μ(f)·Block(e, f)` against the Pellet character `χ₂(disc)`.

Every sub-diagonal cell in this note has CM or trivial members on the row side. Only generic members can
show whether the Möbius-block cancellation has a structured carrier. If it is carried by
`μ = (−1)^d χ₂(disc)`, the number-field question becomes concrete: find a substitute for "μ is a quadratic
character of a discriminant" that acts on the dual Möbius variable `f` alone.

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
  primary `π | q` (the classical Jacobi-sum sign `J = −π`; classical, not re-checked here), so **α is the Frobenius angle of the CM curve,
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

| q | m | ρ = 1 (d = m) | ρ ≈ 3/4 | ρ = 1/2 | ρ = 1/4 | largest d |
|---|---|---|---|---|---|---|
| 7 | 2 | 1.000 | 0.980 (d=3) | 0.982 (d=4) | 0.982 (d=8) | 0.982 (d=30) |
| 7 | 5 | 1.397 | 1.883 (d=7) | 3.535 (d=10) | 10.21 (d=20) | 20.45 (d=30) |
| 7 | 6 | 2.122 | 2.843 (d=8) | 6.525 (d=12) | 37.01 (d=24) | 74.62 (d=30) |
| 13 | 4 | 2.507 | 2.842 (d=5, ρ=0.8) | 8.085 (d=8) | 51.50 (d=16) | 190.6 (d=24) |
| 19 | 4 | 2.652 | 3.174 (d=5, ρ=0.8) | 9.714 (d=8) | 70.86 (d=16) | 147.0 (d=20) |
| 31 | 3 | 1.933 | 2.868 (d=4) | 4.673 (d=6) | 13.70 (d=12) | 33.48 (d=20) |
| 37 | 3 | 1.945 | 2.890 (d=4) | 4.726 (d=6) | 13.91 (d=12) | 34.06 (d=20) |

Exact integers for every `(d, m)` are in `results/core_q*.txt`, with columns
`d k rows M2_k Diag_k max_k` (rows of exact degree `k`). `results/tables.md` has the full grids.

* **Rows of degree ≤ 2 are diagonal-sized** (ratio 0.98–1.0). Their `L` has degree ≤ 1.
* **Every row of degree 3 to 6 is a CM member (finite monodromy)** (EXACT census at degree 3, q = 13;
  root census at degree 4–5; HEURISTIC in general).
  * EXACT census: at q = 13, every degree-3 row has `|A_u(8)|²/q⁸ ∈ {0, 1, 81}`: 130 rows give
    `81 = (d+1)²`, 702 give 1, and 1365 give 0.
  * At q = 7, 13, 19, 31, 37 the maximum over degree-3 rows is exactly `(d+1)² q^d`, i.e.
    `L(x, ψ_u) = (1 − αx)²`. Over degree-4 rows the maximum is `binom(d+2, 2)² q^d` at q = 13, 19
    (a triple root).
  * EMPIRICAL (13 random squarefree rows of degree 4–5 at q = 7, 13, 19, roots computed from exact
    character sums): every inverse root is `√q·e^{2πiθ}` with `θ ∈ θ₀ + (1/N)Z`. Examples:
    `N = 3, 5, 6, 9`; `θ₀` recurs across rows, e.g. −0.4275 and 0.1281 at q = 13.
  * Explanation (HEURISTIC; the Chevalley–Weil / Deligne–Mostow Hodge count, not re-derived in
    detail): the `ψ`-eigenspace of `H¹` of `y⁶ = u(T)`, `deg u = m`, has local exponent 1/6 at the `m`
    roots and `{−m/6}` at ∞. Hence `h^{0,1} = ⌈m/6⌉ − 1`, which is **0 for m ≤ 6**.
  * A definite unitary local system with integral structure has finite monodromy. So for every member of
    conductor degree ≤ 6 the Frobenius eigenvalues are a CM Weil number times roots of unity, and
    repeated roots occur with positive frequency, independent of `q`.
  * Row anatomy (`row_anatomy.py`, q = 7, all 16 807 rows of degree 5, EXACT): the median of
    `|A_u(d)|²/q^d` is exactly 0 or 1 at `d = 5, 7, 10, 12, 14`, and the top 10 % of rows carry 47–85 %
    of `M₂` (`results/row_anatomy_q7_deg5.txt`).
  * Generic (Katz–Sarnak, `U(p, q')`) behaviour starts only at `deg u ≥ 7`. That is beyond the
    exhaustive runs (q = 7 would need 823 543 rows of degree 7); §3.1 samples it.
  * **There is no number-field analogue**: `L(s, ψ_u)` over `Q(ω)` is a GL(1) Hecke L-function, with no
    rank and no Hodge type. So the lab at row degree ≤ 6 is *more* degenerate than the Q-side family.
* **Consequence.** At fixed row degree the ratio grows like a power of `d` and does not decrease with `q`
  (q = 31, 37 at m = 3 match q = 13).
  * The lab "truth" in the accessible range is diagonal-sized only up to factors polynomial in `d`
    (`q^{o(d)}`), carried by CM members with clustered Frobenius angles.
  * That is the precision in which Mom(1, ρ) is stated, so this does not contradict it.
  * It does mean the exhaustive runs cannot test "M₂ ≈ Diag" for generic members. The clean ratios
    0.88–0.95 over `Q(ω)` (RUNG_STRENGTH §5) have no lab counterpart below row degree 7; §3.1 supplies
    one by sampling.
  * (EXACT census and maxima; the trend in `d` is EMPIRICAL; uniformity in `d` is not proved here.)

### 3.1 Generic members: row degree ≥ 7 (sampled rows, exact per row)

`lab_sample.c` draws uniformly random monic rows `u` of one exact degree `m`. For each it computes
`L(x, ψ_u)` exactly, from the complete character sums over monic `n` of degree `< m`, then
`A_u(d)` for all `d ≤ d_max` in `Z[ω]`, and the exact coprime count. The row average is a Monte Carlo
estimate (EMPIRICAL; standard errors from the sample variance). It was validated against the exhaustive
run at q = 7, m = 4: the coprime fraction agrees to 4 digits, and `M₂/Diag` agrees within sampling error.

q = 7, `m = 7`, N = 3000 rows (`results/samp_q7_m7.txt`):

| d | 6 | 7 | 8 | 9 | 10 | 12 | 14 | 16 | 18 | 20 | 22 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ρ = m/d | 1.17 | 1.00 | 0.88 | 0.78 | 0.70 | 0.58 | 0.50 | 0.44 | 0.39 | 0.35 | 0.32 | 0.29 |
| `M₂/Diag` | 0.913 | 0.929 | 0.915 | 0.956 | 0.927 | 1.018 | 1.009 | 1.032 | 1.070 | 1.123 | 1.147 | 1.216 |
| ± s.e. | 0.026 | 0.028 | 0.028 | 0.030 | 0.029 | 0.035 | 0.042 | 0.045 | 0.050 | 0.061 | 0.068 | 0.076 |
| max `|A|²/q^d` | 17.6 | 14.2 | 21.6 | 24.3 | 17.4 | 18.5 | 30.6 | 28.2 | 30.5 | 37.9 | 45.5 | 47.7 |

q = 7, `m = 8`, N = 400 rows (`results/samp_q7_m8.txt`; larger error bars):

| d | 7 | 8 | 9 | 10 | 11 | 12 | 14 | 16 | 18 | 20 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ρ = m/d | 1.14 | 1.00 | 0.89 | 0.80 | 0.73 | 0.67 | 0.57 | 0.50 | 0.44 | 0.40 | 0.33 |
| `M₂/Diag` | 1.05 | 1.06 | 1.08 | 1.13 | 1.10 | 1.33 | 1.37 | 1.53 | 1.69 | 1.80 | 2.08 |
| ± s.e. | 0.10 | 0.11 | 0.11 | 0.13 | 0.13 | 0.17 | 0.21 | 0.23 | 0.31 | 0.36 | 0.48 |

Two smaller runs (`results/samp_q13_m7.txt`, `results/samp_q7_m9.txt`; all cells in
`results/samples_table.md`):
* q = 13, `m = 7`, N = 150: `M₂/Diag` = 1.09–1.21 (± 0.14–0.19) for ρ ∈ [0.7, 1.17], and 1.07–1.31
  (± 0.17–0.24) for ρ ∈ [0.5, 0.64].
* q = 7, `m = 9`, N = 80: 1.15–1.28 (± 0.27–0.30) for ρ ∈ [0.75, 1.12], and 1.25–1.51 (± 0.33–0.59) for
  ρ ∈ [0.5, 0.69].

Both are consistent with diagonal size within 1–2 standard errors. Neither resolves the drift.

* **Once the members are generic the lab looks like `Q(ω)`.** `M₂/Diag` is 0.91–0.96 for
  ρ ∈ [0.7, 1.17]. RUNG_STRENGTH §5 has 0.88–0.95 over `Q(ω)` against a naive diagonal; ours is exact,
  which lowers the diagonal and raises the ratio by a few percent. There is no excess at ρ < 1 down to
  ρ ≈ 0.5.
* Below ρ ≈ 0.45 (m = 7), resp. ρ ≈ 0.7 (m = 8), a slow rise appears: 1.07 at ρ = 0.39 and 1.22 at
  ρ = 0.29 for m = 7; 1.33–1.53 at ρ = 0.5–0.67 and 2.1 ± 0.5 at ρ = 0.33 for m = 8. Each cell is at
  1–3 standard errors and the cells are correlated (EMPIRICAL). With 400 rows the m = 8 tail is not
  resolved. At fixed `u`, `|A_u(d)|²/q^d` has the Cesàro mean
  `Σ_j Π_{k≠j}|e^{iθ_j} − e^{iθ_k}|^{−2}`. That mean is 1 on Haar average but heavy-tailed, so a slow
  drift toward the tail is expected as `d/m` grows. This is the lab form of the `D^ε` in Mom(1, ρ).
* The per-row maximum grows roughly linearly in `d` (14 → 48). There are no CM-type `binom(d+N, N)²`
  rows.

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
`ledger.py` evaluates both sides exactly. Primal = dual at q = 7, `d = 2` for all M = 1..4, and at
`d = 3` for all M = 1..5 (`results/ledger_q7_d*.log`). The `ω`-part of the dual total is 0, as it must be.

**Block ledger** (q = 7, `d = 3`, EXACT). The quantities, all in units of `Diag`:
* `T1 = Σ_{e,f}|Block(e, f)|`: positivity in the Möbius variable `f`, with coprime pairs `(a, b)`;
* `T2 = Σ_{e,f} q^{M−d}|e| Σ_{e|h} |Σ_a β_h(a)χ_a(ef)|²`: the Oct 5-type mean square;
* `T2diag`: its `a = b` part (the dual diagonal).

| M | ρ_eff = M/d | rows | truth Off/Diag | T1/Diag | T2/Diag | T2diag/Diag | q^{d−M} |
|---|---|---|---|---|---|---|---|
| 1 | 1/3 | 6 | −1 (M₂ = 0) | 9.86 | 63.7 | 64.7 | 49 |
| 2 | 2/3 | 48 | −1 (M₂ = 0) | 1.24 | 7.82 | 8.94 | 7 |
| 3 | 1 | 342 | −0.0200 | 0.106 | 1.14 | 1.26 | 1 |
| 4 | 4/3 | 2400 | +0.680 | 0.680 | 0.840 | 0.160 | 1/7 |
| 5 | 5/3 | 16806 | +0.720 | 0.720 | 0.840 | 0.020 | 1/49 |

At ρ > 1 one block carries everything (`T1 = |Off|`) and the dual diagonal is negligible. At ρ ≤ 1 the
mean square is its own dual diagonal (`T2 ≈ T2diag ≈ 1.3 q^{d−M}`, the same `1.3` as DUAL_ANATOMY's
`DD ≈ 1.3(D/Y)Diag` over Q(ω); the coincidence of constants is not explained here). The signed sums cancel
it.

**4.2 Positivity and the dual mean square.** The Oct 5 positivity step (eq:weighted) bounds the blocks by
the full dual mean square, here `E(K) = Σ_{h ∈ V_K}|B_h|²` with `B_h = Σ_n β_h(n)` and `K = 2d − M`.
`DD(K)` is its diagonal. `dual_energy.c` computes both exactly; `pipeline_table.py` combines them with the
truth.

| q | d | M | rows q^M (deg u ≤ M−1) | ρ_eff = M/d | Off/Diag (truth = signed dual) | P/Diag (after positivity) | q^{d−M} | E/DD | κ |
|---|---|---|---|---|---|---|---|---|---|
| 7 | 3 | 1 | 7 | 0.33 | −1 (`L ≡ 1`) | 47.4 | 49 | 0.949 | 0.66 |
| 7 | 3 | 2 | 49 | 0.67 | −1 (`L ≡ 1`) | 6.72 | 7 | 0.960 | 0.33 |
| 7 | 3 | 3 | 343 | 1.00 | −0.0200 | 0.980 | 1 | 0.980 | 0.67 |
| 7 | 4 | 1 | 7 | 0.25 | −1 (`L ≡ 1`) | 349.9 | 343 | 1.0021 | 0.75 |
| 7 | 4 | 2 | 49 | 0.50 | −1 (`L ≡ 1`) | 49.16 | 49 | 1.0028 | 0.50 |
| 7 | 4 | 3 | 343 | 0.75 | **−0.0176** | **7.07** | 7 | **1.0094** | 0.77 |
| 7 | 4 | 4 | 2401 | 1.00 | +1.386 (special rows) | 1.90 | 1 | 1.905 | 0.04 |
| 7 | 5 | 4 | 2401 | 0.80 | **+0.963** (special rows) | **6.93** | 7 | **0.9905** | 0.20 |
| 7 | 5 | 5 | 16807 | 1.00 | +1.104 | 1.35 | 1 | 1.346 | 0.02 |
| 13 | 3 | 1 | 13 | 0.33 | −1 (`L ≡ 1`) | 167.2 | 169 | 0.984 | 0.67 |
| 13 | 3 | 2 | 169 | 0.67 | −1 (`L ≡ 1`) | 12.85 | 13 | 0.988 | 0.33 |
| 13 | 3 | 3 | 2197 | 1.00 | **−0.0059** | **0.994** | 1 | **0.994** | 0.67 |
| 13 | 4 | 4 | 28561 | 1.00 | +1.678 (special rows) | 1.97 | 1 | 1.971 | 0.02 |
| 19 | 3 | 1 | 19 | 0.33 | −1 (`L ≡ 1`) | 359.2 | 361 | 0.9921 | 0.67 |
| 19 | 3 | 2 | 361 | 0.67 | −1 (`L ≡ 1`) | 18.9 | 19 | 0.9945 | 0.33 |
| 19 | 3 | 3 | 6859 | 1.00 | −0.0028 | 0.997 | 1 | 0.9972 | 0.67 |

Here `P = q^{M−d}E`, the `(e, f) = (1, 1)` block relaxed to a full mean square, and
`κ = log(P/|Off|)/log q^d`. Rows with `−1` have `M₂ = 0` exactly: every row of degree ≤ 1 has
`L(x, ψ_u) = 1`. For `M > d` (not shown) `P` is not an upper bound for `Off`: there the off-diagonal sits
in the blocks with `g ≠ 1` (see the block ledger above). `results/pipeline_table_q*.json` has all cells.

**Larger d (sampled dual rows, each `B_h` exact; `dual_sample.c`, q = 7, d = 7, 705 894 squarefree
columns, 250 random monic `h` per degree):** `E_k/DD_k` = 0.61 ± 0.05 (deg h = 6), 0.93 ± 0.06 (deg h = 7),
1.08 ± 0.07 (deg h = 8), 1.06 ± 0.08 (deg h = 9). The sub-diagonal dual (deg h ≥ d) stays diagonal-sized at `D = 7⁷`
(EMPIRICAL, Monte Carlo over `h`). Below `deg h = d` the theta suppression of item 4 sets in.

Reading (EXACT on these cells; the trend is EMPIRICAL):
* **The dual mean square is diagonal-sized** whenever the dual has more rows than columns
  (`E/DD ∈ [0.949, 1.010]`, 12 cells). This is the lab version of A2_LITERATURE §5 and DUAL_ANATOMY §4,
  where the Q-side gives `DD ≈ 1.3(D/Y)Diag`.
* **Positivity therefore costs exactly `q^{d−M}`**, i.e. `D^{1−ρ}`: the dual diagonal, which the exact
  identity does not contain (§4.1 has `(a, b) = 1`).
* **The signed dual is the truth.** It is small where the rows have `deg L ≤ 1` (−2.0 %, −1.8 %, −0.6 %,
  −0.3 %) and of order Diag where special degree-3 rows enter (+96 %, q = 7, d = 5, M = 4). The saving of
  the signed dual over positivity is `κ ≈ (1 − ρ_eff) + κ₀`, where `κ₀ = log(Diag/|Off|)/log q^d` is the
  truth's own cancellation (0.52–0.67 on the trivial-member cells, ≈ 0 on the special-member cells).
* **Positivity is the only loss in Step 3.** Poisson, the Gauss sums and absorption are exact; the dual
  mean square is not larger than its diagonal. Steps 4–5 (reflection and quadratic large sieve) can only
  add the factor `𝓗/X` of DISPERSION_GRH_STEP §4, because:
* **The reflection acts on the wrong rows.** The per-degree dual energies (`results/de_*.txt`) are:

  | q, d: `E_k/DD_k` | deg h = 0 (h unit) | 1 | 2 | 3 | 4 | 5 | 6 |
  |---|---|---|---|---|---|---|---|
  | 7, 4 | 294 (bias) | 0 | 0.023 | 1.24 | 0.86 | 1.0017 | 1.0020 |
  | 7, 5 | 0 | 0 | 0.0033 | 0.106 | 1.55 | 0.931 | — |
  | 13, 3 | 156 (bias) | 0 | 0.083 | 0.988 | 0.983 | — | — |
  | 13, 4 | 2028 (bias) | 0 | 0.0064 | 1.14 | — | — | — |
  | 19, 3 | 342 (bias) | 0 | 0.055 | 0.994 | 0.992 | — | — |

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
   * This was the single concrete lab question whose positive answer would have been a new mechanism.
     **Settled negatively in §8**: the `y^k` coefficients have `x`-poles at the members' zeros, a set that
     is not contained in any fixed finite set (EXACT recurrence orders 1, 2, 7, 14, ≥ 20 for `k = 1..5`;
     generic angles at `k = 7`).
3. **Pellet's identity** (EXACT): `μ(n) = (−1)^{deg n}χ₂(disc n)`.
   * With it, `A_u(d) = (−1)^d Σ_{a ∈ F_q^d} χ0(disc(n_a)³·Res(n_a, u))` is one character sum over affine
     space.
   * The off-diagonal of `M₂` is then a character sum over the `(2d + M)`-dimensional space of triples
     `(n, n', u)`. A Deligne-type bound with total Betti number `B(d)` gives `|Off| ≤ B(d) q^{(2d+M)/2}`.
     That is below `Diag ≈ q^{d+M}` iff `B(d) ≤ q^{M/2} = q^{ρd/2}` (HEURISTIC bookkeeping; the
     degenerate locus `n = n'` must be removed first).
   * General Betti bounds grow like `(Cd)^{2d+M}`. So this route proves nothing at fixed `q`. It works
     only for `q` large in terms of `d`, and it rests on Weil II, which contains RH for every member: it is
     not RH-free.
   * The Sawin–Shusterman char-`p` refinement (LIT, abstract only) controls such Möbius sums at fixed `q`
     in special situations: μ "mimicked by Dirichlet characters on special subspaces", giving a Möbius
     level of distribution close to 1, beyond what pointwise RH gives. Whether it reaches this family
     was not examined.
   * **Number-field analogue: none known to us.** Over Z there is no polynomial whose quadratic character
     is μ, and no `p`-th-power subspaces. This is the parity barrier in its sharpest form.
4. **Answer to the prize question.** In the lab the sub-diagonal second moment is true, and the known proofs
   all go through RH for the members (Weil, or Weil II on the Pellet variety). No exact identity,
   rationality, or degree functional equation found here proves Mom(1, ρ < 1) by itself. The finite-group
   question of item 2 is answered negatively in §8.

## 7. Comparison with the Q side, and what was not done

| quantity | lab (F_q[T], this note) | Q(ω) (moments/, a2/) |
|---|---|---|
| `M₂/Diag`, ρ < 1 | generic members (row degree 7, sampled): 0.92–1.07 for ρ ∈ [0.39, 0.88]; row degree 8: 1.08–1.5 ± 0.2 for ρ ∈ [0.5, 0.89]; trivial members (degree ≤ 2): 0.98–1.0 | 0.88–0.95 (RUNG_STRENGTH §5, naive diagonal), random-sign-like (DUAL_ANATOMY) |
| special members | every member of conductor degree 3–6 is CM (finite monodromy): polynomial excess in `d` | none possible in the same sense (GL(1) Hecke L-functions); none seen at `D ≤ 64000` |
| dual mean square / its diagonal | 0.949–1.009 (exact, d ≤ 5); 0.93–1.08 ± 0.07 (sampled, d = 7, deg h ≥ d) | 0.97–1.14 (A2_LITERATURE §5) |
| positivity cost | exactly `q^{d−M}` | `≈ 1.3 D/Y` (DUAL_ANATOMY §4) |
| signed dual / diagonal | −1.8 %, −0.6 % | within random spread, `≤ 0.18` |
| absorption | exact identity (HD + Pellet) | exact at primes; theta coefficient needed (S6 open for cubic) |

**Not done.**
* The full Ramanujan-block positivity ledger (`T1`, `T2` in ledger.py) beyond `d = 3`.
* Any computation of the lab theta reflection: the functional equation of `Σ_d B_h(d)x^d`, and the
  post-reflection twist in `h`.
* Hoffstein §§1–5 and his `n = 6` corollary.
* The multiple-Dirichlet-series group of §6.2.
* Exhaustive rows of degree ≥ 7. They were only sampled (§3.1), and the dual side was not run there.
* A proof of the Hodge count `h^{0,1} = ⌈m/6⌉ − 1` and of finite monodromy for `m ≤ 6`. It is used
  heuristically and is supported only by the root census.
* A sextic-family check of the `q = 7` coincidence `6 = q − 1` (`χ0` is the Teichmüller character). The CM
  phenomenon also appears at q = 13 and 19, so it is not caused by that coincidence.

## 8. Round 2: is there a finite-group "multiple Dirichlet series" for the second moment of 1/L?

```text
Status: EXPLORATION; EXACT (integer / rational Berlekamp-Massey) + FLOAT root census (numpy roots of exact
  integer polynomials) + HEURISTIC structural reading.
Scope: Z(x1, x2, y) = sum_{u monic} y^{deg u} / (L(x1, psi_u) L(x2, conj psi_u)) over F_7[T] (and the
  control W(x1, x2, y) = sum_u y^{deg u} L(x1, psi_u) L(x2, conj psi_u)); y-degree k <= 6, x-degrees <= 38.
Exact sources or dependencies: §1 lab; lab_mds.c (lab_core + first moments + control sums), mds_test.py
  (BM over Q), pole_census.py, lab_sample.c (degree-7 rows). No literature re-read for this section.
What was actually run: lab_mds 7 5 38 (all 19 608 monic u, deg u <= 5; exact); lab_core dump for deg u <= 6
  (137 257 rows) reused; pole_census.py on k = 3..6; 12 + 4 random rows of degree 7 (q = 7, 13).
Smallest remaining gap: the 2-variable functional-equation group itself was not computed. What is shown
  is that the y^k-coefficients of Z have x-poles outside any fixed finite set, which rules out a
  rational Z (hence the DGH/Bucur-Diaconu finite-group mechanism) under the no-cancellation assumption
  stated in item 4.
```

**Verdict: NO SECOND FE IN THE TESTED RANGE, and a structural obstruction to a finite group.**

The test object is the diagonal slice of `Z`. Write `t = x₁x₂`, so the `y^k t^d` coefficient is
`s_k(d) = Σ_{deg u = k} |[x^d] 1/L(x, ψ_u)|²` (exact integers, `results/mds_q7_m5_d38.txt`). A rational
`Z = P/Q` would force every `y^k` coefficient to have its poles in the fixed finite set `{Q(x₁, x₂, 0) = 0}`.

1. **Control (moments of L) behaves like a finite-polar-divisor object (EXACT, 15 cells, k ≤ 5,
   e ≤ 4).** `Σ_{deg u = k} |[x^e] L(x, ψ_u)|² = q^k (q^e − q^{e−1})` for every `k > e`, and the
   coefficient is 0 for `e ≥ k` (L is a polynomial). So the control diagonal is the rational function
   `q y (1 − q t y) / ((1 − q y)(1 − q² t y))`, with two polar lines. This is consistent with the finite-group
   picture. The full 2-variable group for sextic *positive* moments was **not** reconstructed.
   Background, not re-read: for order-`n` twists the finite-group (Weyl group) series of
   Brubaker–Bump–Friedberg–Hoffstein carry `n`-th order Gauss-sum weights.
2. **Reciprocal case: the x-denominators of the `y^k` coefficients grow with `k` (EXACT, Berlekamp–Massey
   over Q, 39 terms; certified when `2·order + 2 ≤ 39`).** In `u = q t`:

   | k | rows | minimal recurrence order of `s_k(d)` | reduced denominator |
   |---|---|---|---|
   | 2 | 49 | 2 | `(1 − u)`, plus a transient |
   | 3 | 343 | 7 | `(1 − u)³(1 + u)(1 + u + u²)` |
   | 4 | 2401 | 14 | `(1 − u)³(1 + u)²(1 + u²)(1 − u + u²)(1 + u + u²)²` |
   | 5 | 16807 | **≥ 20** (39 terms cannot certify more) | — |
   | 6 | 117649 | ≥ 16 (31 terms) | — |

   At q = 13 (31 terms): orders 1, 2 for `k = 1, 2`, and ≥ 16 for `k = 3, 4` (`results/mds_test_q13.txt`).
   The control closed form of item 1 also holds exactly at q = 13 (`k ≤ 4`, 10 cells).

   The y-direction at fixed `d` is harmless. `s_k(d)/q^k` is constant from `k = 2` for `d = 1` (value 6)
   and from `k = 3` for `d = 2` (value 36). So each fixed-`d` y-series is a polynomial plus a `(1 − qy)` geometric tail: orthogonality in `u`.
3. **Pole census (FLOAT roots of exact integer `L`-polynomials, `results/pole_census_q7.txt`).** Poles of
   the `y^k` coefficient on `|t| = 1/q` are at `t = 1/(α_i conj α_j)`, `α_i conj α_j = q·e^{2πiφ}`. The
   orders of the roots of unity `e^{2πiφ}` are:
   * k = 3: {1, 2, 3} and k = 4: {1, 2, 3, 4, 6}. These match the exact factorizations above.
   * k = 5: {1, 2, 3, 4, 5, 6, 9, 12}. k = 6: the same set on `|t| = 1/q`.
   * At k = 6 the even members (trivial zero `1 − x`) add poles on `|t| = q^{−1/2}` at the irrational
     CM angle `θ₀`. So the polar set grows with `k`.
4. **Generic members (k = 7) destroy finiteness (FLOAT census, 12 random rows at q = 7, 4 at q = 13;
   `results/generic_L_q*_deg7.txt`).**
   * The pair angles `φ = arg(α_i conj α_j)/2π` are non-torsion: 0–5 of 30 per row are rational with
     denominator ≤ 60, and the rest vary from row to row.
   * A sum of rational functions has every pole of its summands unless residues cancel at coinciding
     poles. Here the poles are row-dependent and continuously distributed (HEURISTIC: no cancellation
     across the ≈ 10⁵ distinct members).
   * So the `y⁷` coefficient has of order `(#members)·30` distinct poles. `Z` is not rational and has
     no finite set of polar divisors.
5. **Candidate transformations (b).**
   * Per member, the x-FE `(x₁, x₂, y) ↦ (1/(q x₂), 1/(q x₁), y/(q x₁x₂))` (with `y ↦ χ0(−1)y`) holds for
     primitive odd `ψ_u` as an identity of rational functions. The root numbers cancel
     (`ε(ψ)ε(conj ψ) = ψ(−1)`).
   * It gives no coefficient identity for `1/L`: the power series at `x = 0` and `x = ∞` differ. It is
     also broken at family level by imprimitive members. Even the control fails it at family level without
     correction weights: `Σ_{deg u=3}|c_u(0)|² = 343` but `q^{−2}Σ|c_u(2)|² = 294`.
   * The only y-direction FE is Poisson in `u` (§4.1). It maps the `μ(n₁)μ(n₂)` weights to the dual
     weights `χ0(D_{n₁}) conj χ0(D_{n₂})` (the `B_h` family). That is a different series, so **Z has no
     second FE onto itself**.
6. **Reading.**
   * For moments of `L`, every `y^k` coefficient is a polynomial in `x`. All poles of the series come
     from the `y`-summation, which is why a finite group can close up.
   * For moments of `1/L`, every member contributes its own zeros as `x`-poles already at fixed `k`.
   * In the CM range (`k ≤ 6`) these collapse onto a slowly growing cyclotomic set. That is a lab
     artifact. From `k = 7` on they are generic.
   * So the Diaconu–Goldfeld–Hoffstein / Bucur–Diaconu rationality mechanism does not apply to the
     sub-diagonal second moment of `1/L` in the lab. This removes the one open lab avenue of §6, item 2.
   * Number-field analogue: the same statement holds a fortiori. The `y`-coefficients of
     `Σ_u y^{deg u}/(L L)` have poles at all zeros of all members.

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
| `theta_series.c` | `B_h(d)` as a function of `d` for all monic `h` of small degree (theta structure) |
| `lab_sample.c`, `dual_sample.c` | random rows (resp. dual rows) of one degree, exact per row (generic members) |
| `lab_mds.c`, `mds_test.py`, `pole_census.py` | §8: first moments and control sums, exact Berlekamp–Massey, pole census |
| `tables.py`, `pipeline_table.py`, `sample_table.py`, `row_anatomy.py` | tables from the outputs |
| `results/` | core outputs (`d k rows M2 Diag max`), dual energies, ledgers, identity checks |

Reproduction: `gcc -O2 -o lab_core lab_core.c && ./lab_core 7 6 30 > results/core_q7_m6_d30.txt`
(about 10 min on the shared machine); `gcc -O2 -o dual_energy dual_energy.c && ./dual_energy 7 4 6`;
`python3 gauss_exact.py 7 6 3`; `python3 ledger.py 7 2`; `python3 pipeline_table.py
results/core_q7_m6_d30.txt results/de_7_4.txt`.
