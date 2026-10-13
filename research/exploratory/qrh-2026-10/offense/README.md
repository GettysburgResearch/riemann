# Offense wave (2026-10-12): constructive attacks on the quasi-RH walls

```text
Status: EXPLORATORY index. Each subfolder carries its own labels (PROVED-HERE / PROPOSED /
  CONDITIONAL / HEURISTIC / EMPIRICAL / OPEN). Nothing here proves RH or any zero-free region.
  The OpenAI manuscripts (Sep 30 "7/8", Oct 5 "11/12") remain external, unreviewed imports.
Scope: six parallel constructive attacks on the two walls identified by the qrh-2026-10 wave:
  the rho = 1 wall of the Oct 5 ladder (boundary 1/2 + c*rho/2, c = 5/6), and the 13/15-167/192
  walls of the Sep 30 architecture.
Exact sources or dependencies: ../RUNG_STRENGTH.md, ../LEVERAGE_FAMILIES.md,
  ../DISPERSION_GRH_STEP.md, ../Q_RHO_ANALYSIS.md, ../THRESHOLD_CALCULUS.md, ../FLOOR_BIN_BARRIER.md;
  Oct 5 paper2.tex and Sep 30 paper.tex at pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6.
What was actually run: see each subfolder.
Smallest remaining gap: see each subfolder; summary table below is updated as results land.
```

RH remains unproved.

## Why this wave

The previous wave located the walls exactly. This wave tries to break them. The two levers of the
Oct 5 ladder are the row/column ratio `rho` and the leverage `c` (the principal member's
multiplicity exponent is `1 - c`): the boundary is `1/2 + c*rho/2`.

| lever | value now | value that beats 7/8 | value for a wide margin |
|---|---|---|---|
| `rho` (sextic family, `c = 5/6`) | 1 (Oct 5) | `< 9/10` | `1/2` gives 17/24 |
| `c` (at `rho = 1`) | 5/6 (sextic) | `< 3/4` | `2/3` (cubic family) gives 5/6 |
| principal weight (amplifier, `rho_eff = 1`) | 1 | amplifier cost `kappa < 1/6` | — |

## The six lines

| folder | attack | target |
|---|---|---|
| [O1_CUBIC_FAMILY_REFLECTION](O1_CUBIC_FAMILY_REFLECTION/) | cubic row family (`c = 2/3`); absorption into one sextic Gauss sum is exact; replace the missing sextic theta by Kubota Eisenstein series / A2 Weyl group multiple Dirichlet series / Rankin-Selberg averages | 5/6 at `rho = 1` |
| [O2_SIGNED_DUAL](O2_SIGNED_DUAL/) | keep the dual Moebius sign at `rho < 1` using the bilinear kernel built into twisted multiplicativity of Gauss sums (Heath-Brown 2000 / Heath-Brown-Patterson / Dunn type Type I/II), which is not an involution of the Poisson/theta toolbox | any `rho < 1` |
| [O3_SEP30_X_OCT5](O3_SEP30_X_OCT5/) | feed the Oct 5 Moebius mean square (no BGL excess) into the Sep 30 Gram/large-sieve losses; floor rows by all-rows-minus-non-floor; Sep 30 Lemma 18.1 into the Oct 5 fourth-moment rung | first half-plane below 7/8 from the imports |
| [O4_AMPLIFIER](O4_AMPLIFIER/) | raise the principal member's weight with an amplifier instead of shortening rows | `kappa < 1/6` |
| [O5_WILD_IDEAS](O5_WILD_IDEAS/) | at least 12 further mechanisms, triaged with exponent bookkeeping; the best two developed | — |
| [O6_FUNCTION_FIELD_LAB](O6_FUNCTION_FIELD_LAB/) | the whole Oct 5 pipeline over `F_q[T]`, where RH is known: exact per-step losses at `rho < 1`, and tests of the O1/O2 mechanisms | a mechanism with a number-field analogue |

## Coordinator note: what the exact dual says the crack must look like

From [../DISPERSION_GRH_STEP.md](../DISPERSION_GRH_STEP.md) §4 (exact algebra, not reviewed): at
`rho < 1` the Poisson dual contains **no** dual diagonal. It cancels exactly through
`sum_{v|z} mu(v) = 1_{z=1}`. What must be small is each block's dual **off-diagonal**, at relative
precision `H/L = D^{rho-1}` below the dual diagonal. Every move in the Oct 5 toolbox is an
involution on the pair (rows, columns) that preserves the deficit `1 - rho`
([../Q_RHO_ANALYSIS.md](../Q_RHO_ANALYSIS.md)). So a crack must come from an input that is
**not** such an involution. Candidates:

* the bilinear kernel `conj((m/n)_3)` that twisted multiplicativity
  `gamma_2(mn) = gamma_2(m) gamma_2(n) conj((m/n)_3)` attaches to any factorization of the column
  variable (O2);
* a reflection with a different twist parity (O1);
* a change of the principal weight (O4);
* spectral input (Kuznetsov) on the cover (O5).

Results are summarized here as each line reports.

## Results so far (updated as lines report)

| line | outcome | best number | label | sharpest remaining target |
|---|---|---|---|---|
| O1 | cubic family (`c = 2/3`): absorption makes its dual exactly a 6-fold Kubota coefficient with numerator `−h^4` (Lemma 1, floating-point check at 519 cases); the Kubota functional equation keeps the numerator, so the row conductor is `N(h)^4` and reflection never helps (Lemma 2, imports the CG10 FE); the class move `j -> n−2−j` keeps parity, so the quadratic class is unreachable without a 6-fold theta (Lemma 3); WMDS and Rankin-Selberg routes give 1 and 13/12; numerically `mu*gamma_2*xi` shows **no** BGL excess (0.85-0.97 of diagonal, `X <= 10^5`) while `gamma_2` shows the predicted bias | ledger `sigma(kappa) = (9 kappa − 2)/(6 kappa)`: `kappa = 1/2` gives **5/6**, `8/15` gives 7/8, `< 4/7` beats 11/12 | PROPOSED + IMPORTED (FE) + EMPIRICAL | (LS*_kappa), a cubic large sieve for the single sequence `mu gamma_2 xi` with `kappa < 4/7` (equivalent by Poisson to the cubic family's own `Mom(1, 3 − 1/kappa)`, so it needs `mu`-specific input); Statement B, a summation formula with row conductor `N(h)^2` (with the known cubic sieve: **8/9**; with a quadratic post-twist: 5/6) |
| O3 | the Sep 30 Gram-loss sum (Prop 15.2) is a **squared cubic Gauss sum** family, not Moebius, so Oct 5 does not apply; the `P_a^{1/6}` loss is the sextic-bias (exceptional) component | `926/1077 ≈ 0.8598` if (NA) holds; any partial saving beats `0.874957` | CONDITIONAL on (NA) + Sep 30 lemmas; exact LP certificate | (NA): non-alignment of the sextic-bias component of `A_m` with the cubic-theta row `B_m`, saving `Z^{b/12}`. Circularity check pending in O3b (its diagonal may be the probe's own Moebius signal) |
| O4 | amplification in the Oct 5 pipeline costs `kappa = 1` (break-even needs `kappa < 1/6`); with a prime amplifier the amplified dual is exactly the manuscript's `E(H, X, F)` with `f = l` inside the square; designs (a)-(f) tried, none below 1/6; amplified moments are diagonal-sized numerically (`[0.972, 1.024]`, 120 cells, `|kappa_emp| <= 0.004`) | break-even law PROVED-HERE: `|A_1| << D^{11/12 + lambda(kappa + 5 delta/6 − 1/6)/2}` | PROVED-HERE (ledger) + CONDITIONAL (Oct 5 lemmas) + EMPIRICAL | TM(eta, s): saving `N(l l')^{−eta}`, `eta > 5s/12`, in row-twisted mean squares; round 2 (the `j = 4` channel): the reflection does turn the factor at `l` into a Ramanujan sum (reflected length grows by `N(l)`, not `N(l)^2`), but a cubic row character `chi_l(k)^4` survives; any coefficient-blind joint large sieve has norm at least the reflected column count `L^2 H^2/D`, so `kappa < 1/6` would need a bound `L^{17/6}` below it (PROVED-HERE, elementary). That is the `rho = 1` wall on the reflected side, equivalent to TM(5/12, 1) |
| O7 | Sep 30 floor rows: raising the floor to `a0 = (1+delta0)/2` with a signed floor-row saving FB#(delta0, kappa) gives the exact model LP `sigma0 = 2(9 + 13 delta0 − 12 kappa delta0)/(3(7 + 9 delta0 − 8 kappa delta0))`, an improvement over 6/7 iff `kappa > 5/6`; the "all rows minus non-floor rows" route works on paper but only gives `kappa = 1/4` (the 1/L-to-polynomial error on floor rows); class barrier `kappa <= 1/2` for polynomial-approximation schemes | with Gram loss 0 (i.e. O3's (NA)) and FB#(1/3, 1) and DH-strength row counts: **28/33 ≈ 0.8485**; square-root floor saving reaches the Gram-0 wall 38/45 ≈ 0.8444; with the Gram loss `b/12`, nothing beats 13/15 | exact LP inside the imported model (PROVED-HERE in the model) + CONDITIONAL + HEURISTIC | FB#(1/3, 1), on top of (NA) |
| O5 | 18 mechanisms triaged: 14 DEAD with exact killing terms, 3 ALIVE as corollaries/target, 1 OPEN (Weil positivity) | kappa-law `11/12 − eta(5/6 − kappa)/2`; `p^6` lifting gives `kappa = 5/6` exactly (threshold); Kummer-field corollaries `zeta_F != 0` on `Re s > 7/8` for `F` in abelian extensions of `Q(sqrt(-3))` | PROPOSED / CONDITIONAL on Oct 5 resp. Hecke 7/8 | `kappa < 5/6` at one `eta > 0` (coefficient-specific large values on generic rows) |
