# O7_FLOOR_ROWS: a way through the floor-row wall of the Sep 30 "7/8" architecture

```text
Status: PROPOSED (exponent model of an external, unreviewed manuscript; exact-rational LP
  certificates; one constructed cross-row decomposition with CONDITIONAL inputs). Per-claim labels
  below. Nothing here proves RH or any zero-free region. The Sep 30 ("7/8") and Oct 5 ("11/12")
  OpenAI manuscripts are external, unreviewed imports; everything resting on them is
  CONDITIONAL/IMPORTED.
Scope: the floor-bin step (Lemma 10.4 / eq. (10.15) at the detector floor, triangle inequality over
  zero-free rows) of [OAI-Sep30] Part II, at Gram loss b/12 (manuscript) and Gram loss 0 (O3 target:
  P_a^{1/6} branch removed, P_a^2/Y' branch kept, as in ../O3_SEP30_X_OCT5/scripts/o3_barriers.py).
Exact sources or dependencies: see FLOOR_ROWS.md header ([OAI-Sep30] paper_sep30.tex l. 4707-4720,
  5808-6010; Lemma 18.1; [OAI-Oct5] paper2.tex Prop. thm:ms; ../../FLOOR_BIN_BARRIER.md;
  ../../THRESHOLD_CALCULUS.md; ../../scripts/{barrier_lp,floor_lp,threshold_calculus}.py unchanged).
What was actually run: scripts/floor_rows_lp.py, floor_rows_scan.py (exact LP + rational dual
  certificates), closed_forms.py + check_closed_vs_lp.py (sympy; 30/30 exact matches),
  counts_needed.py (exact), full_model_floor.py (float Part II model, EMPIRICAL).
  Outputs: *.out, results/*.log|json. Single-threaded; each run under 7 minutes.
Smallest remaining gap: FB#(delta0, kappa) (FLOOR_ROWS.md Sec. 5.1) with kappa > 5/6, OPEN.
  The constructed route gives kappa = 1/4 (CONDITIONAL), and approximate-then-bound schemes are
  capped at kappa <= 1/2 (PROPOSED/HEURISTIC).
```

RH remains unproved. "sigma0" is the boundary one external architecture would deliver under the
stated hypotheses.

## Best results

**Gram 0 (O3).** With the floor-row input FB#(1/3, 1) and the count
`R(delta) <= 19/20 - 17 delta/20` above the floor (DH at `1/3+`), sigma0 = **28/33 = 0.848485**.
This is CONDITIONAL on the manuscript's Part II outputs (ARCH), on Gram 0, on that count, and on
FB#. FB# is OPEN; it is heuristically plausible exactly up to delta0 = 1/3. Square-root strength,
FB#(1/2, 1), gives **38/45 = 0.844444**, which is the Gram-0 low-side wall.

**Gram b/12 (manuscript).** No floor-row input of this type beats **13/15** with the manuscript's
energy lemma (`kappa = 1` is exactly flat there). Only with the hypothetical energy bound E\* and
`delta0 > 1/3` does it go lower: 106/123 = 0.861789 at FB#(1/2, 1).

**Constructed input (all rows minus non-floor rows, CONDITIONAL).** It gives floor saving
`theta_F = delta0/4` (kappa = 1/4): 920/1071 (Gram 0) or 1327/1527 (Gram b/12) at a0 = 51/100.
This is **worse than simply lowering the floor**, which gives 6/7 (Gram 0) or 13/15 (Gram b/12).

LP entries are PROVED-HERE as statements about the LP model (exact rational dual certificates) and
PROPOSED as statements about the manuscript, through the transcription hypothesis ARCH.

| floor-row input | Gram b/12 | Gram 0 | label |
|---|---|---|---|
| none (triangle inequality, any counting), a0 = 51/100 | 167/192 | 926/1077 = 0.859796 | PROPOSED (exact LP) |
| none, floor lowered a0 -> 1/2 | 13/15 | 6/7 = 0.857143 | PROPOSED (exact LP) |
| floor saving theta <= 1/50 at a0 = 51/100 (DH above) | (167-225θ)/(192-225θ) | (926-1200θ)/(1077-1200θ) -> 902/1053 | PROPOSED |
| constructed kappa = 1/4 input (Sec. 2 of FLOOR_ROWS.md) | 13/15 | 6/7 | CONDITIONAL |
| FB#(delta0, kappa), a0 = (1+delta0)/2, DH above | 13/15 (kappa <= 1) | `2(9+13δ0-12κδ0)/(3(7+9δ0-8κδ0))`; gain iff kappa > 5/6 | PROPOSED formula; FB# OPEN |
| FB#(1/3, 1) | 13/15 | **28/33** | CONDITIONAL; HEURISTIC edge |
| FB#(1/2, 1) (square-root) | 13/15 | **38/45** (= low wall) | CONDITIONAL |
| saving theta in floor and every witnessed bin, a0 -> 1/2 | 13/15 | (6-8θ)/(7-8θ), 38/45 from θ = 1/14 | PROPOSED |

Float full-model cross-checks (EMPIRICAL, `results/`):
* Gram 0 with DH counts: 0.848489 at FB#(1/3, 1) and 0.844448 at FB#(1/2, 1), matching 28/33 and
  38/45.
* Gram 0 with **the manuscript's own row counts**: the floor binds at 0.859811 (= 926/1077 + slack).
  Remove the floor, either by FB#(1/50, 1) (0.858174) or by the free floor-lowering (0.858203), and
  the witnessed bins near `delta ~ 0.14` bind at about **0.8582**.
* Raised floors (delta0 = 1/5, 1/4, 1/3) do not close with manuscript counts: the bins just above
  the floor fail. So with manuscript counts the floor input buys nothing beyond floor-lowering.
* Exact count needed for 28/33 (top dyad, geometry `(3/11, 6/11, 2/11)`):
  `R(delta) <= 19/20 - 17 delta/20` on `(1/3, 23/33]`. This is DH at `1/3+` and slightly weaker
  above (`counts_needed.out`).

## What is new here

1. **Gram 0 changes the geometry and the role of the floor** (PROPOSED, exact). The optimum sits on
   the kink `ly = 2 lx` of the kept Gram branch, so `lx < ly`, and the DH band
   `F(delta) = F(0) + delta (lx - ly)/2` decreases in delta. Two consequences follow:
   * a raised floor carrying a signed saving equal to its height needs **no** saving in any
     witnessed bin, only counts;
   * the exact gain condition is **kappa > 5/6**: `d sigma0/d delta0 = (20 - 24 kappa)/147` at 0.
2. **A constructed cross-row decomposition** (the B1 angle, made legitimate). Replace `1/L(s)` by the
   entire truncated reciprocal `M_u(s)` on all rows:
   `S_F = sum_all g_u - sum_NF g_u + sum_F (f_u - g_u)`.
   * The all-rows front part is negligible by Poisson, since `xi` kills the diagonal.
   * The dual part reduces to twisted sextic Gauss-sum averages (G_kappa), which are OPEN.
   * Non-floor rows are handled by Hoelder with Lemma 18.1 and DH counts.
   * The mollifier remainder on floor rows is the bottleneck: kappa_II = mu/2 = 1/4.

   Ledger: `kappa = min(kappa_I, mu/2, c(1 - 1/(2k) - 1/(2m)))`.
3. **Nine repairs** of the bottleneck were tried (FLOOR_ROWS.md Sec. 3):
   * subtraction on the global line through the probe identity (circular);
   * longer or unbalanced mollifier;
   * a detached reciprocal contour;
   * a second-order Neumann approximant;
   * Hoelder with the Oct 5 second moment;
   * zero-detector smoothing of the indicator;
   * large values;
   * a direct Gauss-sum attack;
   * height-aspect (hybrid) enlargement of the family.

   None reaches 5/6. A class barrier explains why: approximating `1/L` by a family-structured
   Dirichlet polynomial of length at most the conductor, then bounding the remainder absolutely,
   gives **kappa <= 1/2** (prime-tail variance `N^{-delta0/2}`; HEURISTIC lower bound).
4. **Smallest statement, with exponent.** FB#(delta0, kappa): the signed floor-bin sum at floor
   `a0 = (1+delta0)/2` is `<< U^{1 + delta0/2 - kappa delta0 - z0 + eps} Z^{...}`.
   * Any gain under Gram 0 needs **kappa > 5/6**.
   * kappa = 1 at delta0 = 1/3 gives **28/33**.
   * The saving is needed only on dyads `U = Z^d` with `d >= (37/62) h`, rising linearly in `1/d` to
     `delta0` at `d = h`.
   * The ratios recipe with a sextic Gauss bias `U^{2/3}` makes kappa = 1 plausible exactly for
     `delta0 <= 1/3` (HEURISTIC).
   * Reduced along the constructed route, the open inputs are (G_kappa) with kappa > 5/6, and a
     mollified fourth moment `sum |1 - L M|^4 << U^{1 - nu delta0}` with `nu > 5/3`. The second
     must be paired with a twisted mollified second moment over all rows.

## Next step

Attack FB#(1/3, 1) at its weakest joint: the dual (Gauss-sum) part
`sum_{u in B_F} xi(u) W(chi_u) B_u(1-w) H/L(s)`.
* First test the sextic bias exponent for the specific twist `xi` (Kubota-Patterson residue; does
  it vanish for `xi` nonprincipal at S?). If it vanishes, delta0 up to 1/2, i.e. 38/45, becomes
  heuristically admissible. The sibling folder `../O3b_NA_TEST/` contains Gauss-sum bias probes;
  they were not read or verified here.
* In parallel, the manuscript-count wall at about 0.8582 (bins at `delta ~ 0.14`) is a counts problem.
  PR 910-type joint moments would address it.

## Files

* [FLOOR_ROWS.md](FLOOR_ROWS.md): full analysis (object, LP, construction, repairs, class barrier,
  smallest statement).
* `scripts/floor_rows_lp.py`, `scripts/floor_rows_scan.py`: exact LP and certificates.
  `scripts/closed_forms.py`: sympy closed forms. `scripts/full_model_floor.py`: float full model.
* `scripts/check_closed_vs_lp.py`: closed form vs LP, 30/30 exact matches.
  `scripts/counts_needed.py`: the count requirement above the raised floor.
* `floor_rows_lp.out`, `floor_rows_scan.out`, `closed_forms.out`, `counts_needed.out`: run outputs.
* `results/full_zero_{DH,paper,paper_lowfloor,paper_raised2}.log` and `.json`: full-model runs.
  `full_zero_paper_raised.json` belongs to `full_zero_paper.log`.
* `scripts/run_after.sh`: sequential driver for the last two full-model runs.
