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
