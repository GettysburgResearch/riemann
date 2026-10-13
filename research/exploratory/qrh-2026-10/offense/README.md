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

Results are summarized here as each line reports. An adversarial review of the PROVED-HERE claims and of this index is in [REDTEAM.md](REDTEAM.md). Its corrections are applied below.

## Synthesis (coordinator; PROPOSED reading of the line reports, not reviewed)

**No exponent moved.** No line produced a half-plane below 7/8, or below 11/12 in the Oct 5
architecture, except conditionally on statements listed below. RH remains unproved.

**What the wave established (PROPOSED reading).** Every remaining wall examined sits on the principal member or on a principal-row main term:
* *Oct 5 side.*
  * The `rho < 1` dual has no diagonal: Q_RHO_ANALYSIS, and O2 Prop G, which collapses the dual
    Moebius variable to `mu(gcd)` times sextic characters.
  * What remains is a coefficient-specific saving `delta > (1 − rho)/6` (O2 Prop L), the same as
    `kappa < 5/6` in O5's kappa-law.
  * Its principal rows impose the same inequality on `A_1` (the extraction law read backwards). That is a consistency check, not by itself a proof of circularity (REDTEAM).
  * For the amplifier designs tried on the Oct 5 tools, the cost is `kappa = 1`, because the reflected column count grows (O4, both rounds; O2's Moebius-signed variant also loses).
  * The cubic family needs a summation formula or a large sieve for the single sequence
    `mu gamma_2 xi` (O1). By Poisson that is the cubic family's own moment.
* *Sep 30 side.* The Gram loss `P_a^{1/6}` sits on the sextic-bias (exceptional) component of the
  additive polynomial (O3).
  * On the `m`-diagonal of the low pairing, the coefficient product is
    `gamma_1 gamma_2 conj(alpha) = mu G` (O3b, PROVED-HERE from imported identities, confirming the
    coordinator's derivation). It is a Möbius sum against a ray/target character.
  * In the paper's pairing, however, this diagonal contributes nothing: those terms carry the
    `m`-character `xi(m) chi_s(−1) 1_{(m,s)=1}`, and `xi` is primitive and nonprincipal mod `b_*`.
    The paper inserts it precisely to exclude the zero Poisson frequency (Sep 30 l. 3345-3374).
    O3b finds the diagonal identically zero in its toy model with `S = {2, lambda}`; with the
    paper's full `S`, the robust statement is "negligible" (REDTEAM item 1). The coordinator's
    earlier "the diagonal is the probe's signal, so (NA) is circular" was wrong in mechanism.
  * The alignment that defeats (NA) sits in the cubic-theta row's **constant row** `c = 1`. Its
    overlap with the bias component is flat in `Q` (about 0.25 at `Q = 256` to `8192`; EMPIRICAL).
    Structurally it is a main term `≈ (Kubota mass)/L(1, psi eta)` (PROPOSED).
  * So **(NA) is false as stated in the tested range**: it would need `1/L(1) << Z^{−b/12}` for a
    fixed target.
  * The narrower (NA′), with that row removed, holds at noise level. It helps only if the same main
    term cancels against the high side (O3b round 2).
* *Finite numerics show no visible obstruction* (EMPIRICAL, floating point, finite; not evidence
  for the asymptotic statements, AGENTS.md):
  * the signed dual is small relative to the positivity proxy at `D <= 45000` (O2). The
    log-ratios O2 reports do not resolve an exponent: `S` changes sign;
  * `mu gamma_2 xi` shows no BGL excess for `X <= 10^5` (O1);
  * amplified moments are close to diagonal size at `D <= 8000` (O4);
  * the sub-diagonal moments are close to diagonal size at `D <= 64000` (RUNG_STRENGTH §5).

**The sharpest open statements, ranked by payoff per unit of plausibility.**

| statement | what it asks | payoff | why it is not obviously circular | source |
|---|---|---|---|---|
| (LS*_kappa) | cubic large sieve for the single sequence `mu gamma_2 xi` with excess `(H X)^kappa` | `kappa < 4/7` beats 11/12; `8/15` gives 7/8; `1/2` gives 5/6 | the only known obstruction to an optimal cubic sieve (Gauss-sum bias, dFDH/DR) is harmless for this sequence by O1 Prop 5. Prop 5 is PROPOSED, bounds only a hypothetical pole's main term, and rests on the dFDH abstract for "only known obstruction". Its pole exponent should be 2/3, not 7/12, giving `X^{1/3} H^{1/3}`, still `<= X` (REDTEAM item 5). Finite numerics are consistent with `kappa = 1/2`. It is still equivalent to the cubic family's own moment, so it needs `mu`-specific input | O1 §7 |
| Statement B | a summation formula with row conductor `N(h)^2` for `n -> mu gamma_2 xi` against cubic characters | **8/9** with the known (BGL) cubic sieve; 5/6 with a quadratic post-twist | a GL(2)-type object on the 6-fold cover would supply it via (S6). O1 round 2: (S6) is **locally consistent** at every unramified prime (the KP/Hecke relations leave `tau(mp)` free; n = 3 is reproduced numerically, n = 4 matches the literature only; consistency was tested against the j-orbit relations at fixed `m`, not against the dependence on `m`'s class at `p` that (S6) prescribes), but its global form (S6-glob) is overdetermined and is contradicted by the published numerics for the one sextic theta computed ([BH]). Statement B asks for less than (S6-glob) | O1 §§7, 8A |
| (AMP_t) | amplified dual closing at `H >= D L^t` | `t = 1`: 7/8 at `lambda = 1/2` | rows <= columns, so neither the row-blind nor the orbit-invariance barrier applies | O2 |
| kappa-law / Prop L | saving `delta > (1−rho)/6` over positivity at one `rho < 1` | any such `delta` beats 11/12 | needs coefficient-specific large values for generic rows | O2, O5 |
| (NA) + FB#(1/3, 1) | Sep 30: non-alignment of the bias component, plus a signed floor-row saving | 926/1077; then 28/33 only with additionally DH-strength row counts for bins above `delta = 1/3`, which O7 calls beyond current technology (with the manuscript's own counts: about 0.8582) | **(NA) falsified as stated** in the tested range (O3b); (NA′) survives at noise level and is usable only if its main term cancels against the high side (O3b round 2) | O3, O3b, O7 |

## Results so far (updated as lines report)

| line | outcome | best number | label | sharpest remaining target |
|---|---|---|---|---|
| O1 | cubic family (`c = 2/3`): absorption makes its dual exactly a 6-fold Kubota coefficient with numerator `−h^4` (Lemma 1, floating-point check at 519 cases); the Kubota functional equation keeps the numerator, so the row conductor is `N(h)^4` and reflection never helps (Lemma 2, imports the CG10 FE); the class move `j -> n−2−j` keeps parity, so the quadratic class is unreachable without a 6-fold theta (Lemma 3); Kubota routes give 1, Rankin-Selberg over the index gives 13/12, WMDS is closed for the mean square without an exponent; numerically `mu*gamma_2*xi` shows **no** BGL excess (0.85-0.97 of diagonal, `X <= 10^5`) while `gamma_2` shows the predicted bias | ledger `sigma(kappa) = (9 kappa − 2)/(6 kappa)` (valid for `kappa >= 1/2`): `kappa = 1/2` gives **5/6**, `8/15` gives 7/8, `< 4/7` beats 11/12 | PROPOSED + IMPORTED (FE) + EMPIRICAL | (LS*_kappa), a cubic large sieve for the single sequence `mu gamma_2 xi` with `kappa < 4/7` (equivalent by Poisson to the cubic family's own `Mom(1, 3 − 1/kappa)`, so it needs `mu`-specific input); Statement B, a summation formula with row conductor `N(h)^2` (with the known cubic sieve: **8/9**; with a quadratic post-twist: 5/6) |
| O2 | the hoped-for "mu against Gauss sums" arrangement does not occur: **Prop G** (gcd collapse, PROVED-HERE given eq:initial-column-output; floating-point check on 400 cases) sums the dual Moebius variable out to `mu(g) 1_{g|k} chi_{z1}(k) conj chi_{z2}(k)`, so the only sign left multiplies sextic characters (short members of the original family), and HB00-type Type I/II routes give `delta = 0`; **Prop L**: a saving `D^delta` over the positivity bound gives `sigma = 1 − delta/2 − rho/12`, so beating 11/12 needs only `delta > (1 − rho)/6` (7/8: `delta > 1/4 − rho/6`); the signed dual is small numerically (`|S|/H <= 0.71%`, `D <= 45000`; no asymptotic exponent is resolvable) | no exponent moved | PROVED-HERE (given imports) + EMPIRICAL | (AMP_t): an amplified dual closing at `H >= D L^t` gives `11/12 + lambda(5t − 6)/12`; `t = 1` gives 7/8 at `lambda = 1/2`; rows <= columns, so neither the row-blind nor the orbit-invariance barrier applies (OPEN). Needs a transformation reflecting the amplifier prime together with the theta variable (`s < −3/5`). Round 2: applying absorption a second time, to the residual `mu(g)`, is idempotent. `mu(g) 1_{g|k}` is only the inclusion-exclusion of the primal row mask (the family's `mu` was already absorbed), and Pellet's identity has no number-field version acting on `g` alone. The binding statement is (OD-g1), the coprime-pair dual (no visible `mu`, still equivalent to the original by Poisson), with `delta > (1 − rho)/6` |
| O3 | the Sep 30 Gram-loss sum (Prop 15.2) is a **squared cubic Gauss sum** family (class `theta^2`: `gamma_1 = G gamma_2^2`), not a Moebius × finite-order family, so Oct 5 does not apply; the `P_a^{1/6}` loss is the sextic-bias (exceptional) component | `926/1077 ≈ 0.8598` if (NA) holds; any partial saving beats `0.874957` | CONDITIONAL on (NA) + Sep 30 lemmas; exact LP certificate | (NA): non-alignment of the sextic-bias component of `A_m` with the cubic-theta row `B_m`, saving `Z^{b/12}`. O3b: (NA) is false as stated (a flat overlap with B's constant row, main term ≈ 1/L(1, psi eta)); (NA′) without that row holds at noise level |
| O4 | amplification in the Oct 5 pipeline costs `kappa = 1` (break-even needs `kappa < 1/6`); with a prime amplifier the amplified dual is exactly the manuscript's `E(H, X, F)` with `f = l` inside the square; designs (a)-(f) tried, none below 1/6; amplified moments are close to diagonal size numerically (`[0.972, 1.024]`, 120 cells; `|kappa_emp| <= 0.004` in §5.1, up to 0.0145 in §5.2) | break-even law PROVED-HERE (if the amplified moment is `<< H D L^{1+kappa}` at `H = D L^{1+delta}`): `|A_1| << D^{11/12 + lambda(kappa + 5 delta/6 − 1/6)/2}` | PROVED-HERE (ledger) + CONDITIONAL (Oct 5 lemmas) + EMPIRICAL | TM(eta, s): saving `N(l l')^{−eta}`, `eta > 5s/12`, in row-twisted mean squares; round 2 (the `j = 4` channel): the reflection does turn the factor at `l` into a Ramanujan sum (reflected length grows by `N(l)`, not `N(l)^2`), but a cubic row character `chi_l(k)^4` survives; any coefficient-blind joint large sieve has norm at least the reflected column count `L^2 𝓗^2/D`, so `kappa < 1/6` would need a bound `L^{17/6}` below it (PROVED-HERE, elementary). That is the `rho = 1` wall on the reflected side, equivalent to TM(5/12, 1) |
| O7 | Sep 30 floor rows: raising the floor to `a0 = (1+delta0)/2` with a signed floor-row saving FB#(delta0, kappa) gives the exact model LP `sigma0 = 2(9 + 13 delta0 − 12 kappa delta0)/(3(7 + 9 delta0 − 8 kappa delta0))`, an improvement over 6/7 iff `kappa > 5/6`; the "all rows minus non-floor rows" route works on paper but only gives `kappa = 1/4` (the 1/L-to-polynomial error on floor rows); class barrier `kappa <= 1/2` for polynomial-approximation schemes | with Gram loss 0 (i.e. O3's (NA)) and FB#(1/3, 1) and DH-strength row counts: **28/33 ≈ 0.8485**; square-root floor saving reaches the Gram-0 wall 38/45 ≈ 0.8444; with the Gram loss `b/12` and the manuscript's energy lemma, nothing beats 13/15 (106/123 under a hypothetical energy bound); closed form stated for `delta0 <= 1/2` at `kappa = 1` | exact LP inside the imported model (PROVED-HERE in the model) + CONDITIONAL + HEURISTIC | FB#(1/3, 1), on top of (NA) |
| O3b | numerical and structural test of (NA) in a toy model over `Z[omega]` (Gauss sums checked against `eis.py`): the `m`-diagonal is a Moebius sum but contributes nothing; the bias component's overlap with the cubic-theta row is carried by the constant row `c = 1` (0.240-0.261, flat for `Q = 256`-`8192`), with structure `≈ (Kubota mass)/L(1, psi eta)`; controls (`mu -> 1`, random signs) agree within 25% | (NA) falsified as stated in the tested range | PROVED-HERE (diagonal identity, given imports) + EMPIRICAL + PROPOSED | (NA′): (NA) with B's principal rows removed holds at noise level; it helps only if that main term cancels against the high side (round 2) |
| O6 | function-field lab over `F_q[T]`, `q = 7, 13, 19, 31, 37` (exact arithmetic): Poisson in `u`, Gauss sums and absorption lose nothing; absorption is a Hasse-Davenport identity with a pure degree character for `alpha`; positivity is the first and dominant loss, exactly `D^{1−rho}`; the dual's unit row shows the Patterson exponent 5/6 exactly; at the accessible sub-diagonal sizes, rows are CM or trivial members (finite monodromy), so these are not yet tests on generic members; sampled generic members (row degree 7, 3000 rows, exact per row) give `M_2/Diag = 0.91-0.96` for `rho in [0.7, 1.17]`, close to the `Q(omega)` values | no exponent | EXACT (finite ranges) + EMPIRICAL + HEURISTIC | the only lab mechanism is Pellet's identity `mu(n) = (−1)^{deg n} chi_2(disc n)` (with Deligne, Sawin-Shusterman); no number-field analogue on the dual variable alone (O2 round 2, item 5). Next: the block ledger on generic members (row degree `>= 7`), and whether the double series `sum_u y^{deg u}/(L(x_1, psi_u) L(x_2, conj psi_u))` has a finite group of functional equations (OPEN) |
| O5 | 18 mechanisms triaged: 14 DEAD with exact killing terms, 3 ALIVE as corollaries/target, 1 OPEN (Weil positivity) | kappa-law `11/12 − eta(5/6 − kappa)/2`; `p^6` lifting gives `kappa = 5/6` exactly (threshold); Kummer-field corollaries `zeta_F != 0` on `Re s > 7/8` for `F` in abelian extensions of `Q(sqrt(-3))` (REDTEAM: K1 OK; K2 OK, though its effective Chebotarev error probably needs `log^2`; O5's lifting "Prop L" is OK with a proof slip, and its name collides with O2's Prop L) | PROPOSED / CONDITIONAL on Oct 5 resp. Hecke 7/8 | `kappa < 5/6` at one `eta > 0` (coefficient-specific large values on generic rows) |
