# Threshold calculus for the 7/8 quasi-RH architecture: what sets 7/8, and what cannot be passed

```text
Status: PROPOSED (model-based mechanism analysis) + EXACT certificates for the stated linear barriers
Scope: the exponent architecture of an external, unreviewed manuscript; no statement about RH,
  and no claim that the manuscript is correct
Exact sources or dependencies: [OAI] OpenAI, "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane
  Re s > 7/8" (30 Sep 2026; sha256 in scripts/SOURCES.txt), Sections 2, 8, 10, 14-20; [K] Kintali (7 Oct 2026)
What was actually run: scripts/threshold_calculus.py (self-tests), scripts/energy_lp.py (scratch, LP
  verification of the energy closed form; reproduced in barrier_lp.py logic), scripts/barrier_lp.py
  (exact rational LP certificates), scripts/sensitivity.py (results/*.json)
Smallest remaining gap: every geometry other than the manuscript's needs the lemma-range obligations
  of Section 7; the barriers are barriers for THIS architecture's stated lemma outputs, not theorems
  about the true size of the probe.
```

## 0. Relation to prior repository work (read first)

This wave began without noticing that the same manuscripts had already been imported and analysed
on draft PRs and branches. The following are **prior** and are not claimed here:

* branch `claude/openai-math-riemann-analysis-w5copg`, `standalone/2026-10-07-openai-quasi-rh/`:
  * an exponent model with `σ0 = 1 − h/6 + b/12`;
  * the forced dual-length constraint and `σ0 = 11/12 − ℓ/4`;
  * the method's own optimum ≈ 0.87497;
  * "DH counts → 13/15";
  * the floor `5/6` when the energy and dual-length constraints are dropped;
  * "reaching 3/4 needs `h = 3/2`", i.e. ratios-type cross-row cancellation or a bilinear bound
    beating Cauchy–Schwarz;
* [PR 910](https://github.com/GettysburgResearch/riemann/pull/910): the exact envelope limit
  `(1507−2√921)/1653 ≈ 0.874957`, the conditional `139999/160000`, the joint-moment target (6.6),
  and the higher-moment route `1/2 + 5(1+θ)/(12k)` for the Oct 5 architecture;
* [PR 908](https://github.com/GettysburgResearch/riemann/pull/908): the byte-exact import, the
  conditional bridges, and "no bootstrap" for the repository's MHB32 energy map.

Our numerical optimum (0.874961) independently agrees with PR 910's exact limit.

**What this file adds:**

1. Exact rational certificates for the barrier statements (Barrier 1, Section 2; Section 5 LPs).
2. The floor-bin barrier as a function of the detector floor `a0`. It equals `167/192` at the
   manuscript's `a0 = 51/100` *for any row-count input*, which reconciles our 0.8698 with w5copg's
   13/15: their value corresponds to `a0 → 1/2`.
3. Robustness of 13/15 under perfect energy, row-by-row GLH and contour flexibility.
4. The quantitative bilinear-leverage law `13/15 − 4ϑ/5`.
5. The non-iterability of the 7/8 bootstrap itself (scenarios B and C).
6. A pricing of PR 910's joint moment (6.6) in this architecture: at most `7/8 − 167/192 = 1/192`.
7. The Kintali closed form (Section 8).

## 1. The bookkeeping in one formula

[OAI] Proposition 2.1 needs a probe with `|J| ≪ Z^{C(σ0)+ω}` and `|J − f| ≪ Z^{C(β*)−σ}`, where
`C(s) = s + lx/2 − 1 + h/6` (Definition 10.1), `X = Z^{lx}`, `Y = Z^{ly}`, prime-slot length `ℓ`,
dual (row) length `h = 1 − lx + ℓ`, `M = lx + ly`, `b = ly − lx`. If the low estimate is
`|J| ≪ Z^{θ_low}`, the boundary is

    σ0 = 1 − lx/2 − h/6 + θ_low.

* Part I (`lx = ly = h = 1/2`, `ℓ = 0`, `θ_low = 1/4`): `σ0 = 11/12`.
* Part II (`lx = 17/48`, `ly = 23/48`, `ℓ = 1/6`, `θ_low = lx/2 + b/12 = 3/16`): `σ0 = 7/8`.

On the high side, Lemma 10.4 (eq. 10.15) gives for a row bin with rightmost zero `a = (1+δ)/2`,
slot amplitude `q = xδ` (`0 ≤ x ≤ 1/2`), row norm `U = Z^d` and bin count `U^R`:

    E − Δ = a − β* + h(z0 − 1/6) − a·ly − ℓ/2 + qℓ + d(R + δ/2 − z0),   z0 = 17/50.

**σ0 cancels from `E − Δ`.** The high side therefore only constrains the admissible geometry; the
boundary itself is always the low-side number. This is why the two parts of [OAI] differ in their
low estimates and geometries rather than in their row counts.

## 2. The low side in closed form

Lemma 14.3 (eq. 14.14) bounds the reflected energy of the marked completed rows; Lemma 15.1
specializes it for row length `M' = M − 2d` and active-slot length `ℓ' = ℓ − d`. Maximizing (14.14)
over all admissible dyads is a union of six linear programs. We solved them for 335 random
`(M', ℓ')` and found exact agreement (to `2·10⁻¹⁶`) with

    E_B(M', ℓ') = max( M',  (2M' + 1 + 3ℓ')/4,  2M' + ℓ' − 1 ).

The manuscript's proof of Lemma 15.1 uses `M + ℓ = 1`. That is exactly the condition under which
the third branch (dual length exceeding row length) disappears. **Lifting `M + ℓ = 1` costs
`(M + ℓ − 1)/2` in the low estimate.** An earlier draft of our model omitted this branch and
"found" a spurious improvement; the LP check caught it.

With the Gram bound of Prop. 15.2 (`(Q/Y′)(1 + P_a^{1/6} + P_a²/Y′)`, `P_a = Z^b`) and Prop. 15.3's
tuple count, the low threshold is

    σ0_low(lx, ly, ℓ) = 1 − lx/2 − h/6 + max_{0≤d≤ℓ} { [−(ly−d) + max(0, b/6, 2b−ly+d) + E_B(M−2d, ℓ−d)]/2 − d/2 }.

This reproduces 7/8 and 11/12 exactly.

### Barrier 1 (exact): the low estimate can never certify less than 13/15

Using only the `d = 0` term and `max(0, b/6, …) ≥ b/6`:

    σ0_low ≥ 5/6 − (5/12)M − ℓ/6 + E_B(M, ℓ)/2.

Bound `E_B` below by the convex combination `(17/30)·M + (2/5)·(2M+1+3ℓ)/4 + (1/30)·(2M+ℓ−1)`.
The coefficients of `M` and `ℓ` then cancel identically, leaving

    σ0_low ≥ 5/6 + (1/2)(2/5 · 1/4 − 1/30) = 13/15

for **every** geometry. Equality holds at `lx = ly = 2/5`, `ℓ = 1/5`; this is also the LP optimum
(`scripts/barrier_lp.py`). If the reflected-energy bound were the large-sieve diagonal alone
(`E_B = max(M', 2M'+ℓ'−1)`), the infimum would be `5/6`. In any case `θ_low ≥ lx/2` gives
`σ0 ≥ 1 − h/6 = 5/6 + (lx − ℓ)/6`, a hard floor for this probe family. It comes from the
`z = 1/6` residue of `ζ_F(6z)`.

## 3. The high side reproduced exactly

The row count of Prop. 19.2 is a min-max over the detector parameter `t ∈ [1, 3/2]` (Prop. 8.3),
the row's witness split `(r, m = t − r)`, and four bounds:

* the inverse moment (Lemma 17.1, capacity `(1−r)/2`);
* the plain fourth moment (Lemma 18.1, capacity `(1−2m)/(6κ)`, `κ = 2β*−1`);
* sixth-power amplification (Lemma 17.6, slope `α = 5/6`);
* the unweighted plain moment.

Prime supply is capped at `ℓ/d`. We evaluate it exactly with piecewise-affine algebra
(`R_exact`, `R_closed`, `R_fast`, mutually consistent to `10⁻¹⁵`).

* At `κ = 3/4` it reproduces the paper's closed form `R* = 1 − δ + (α−δ)δP_x/(2J)` to machine
  precision.
* With the manuscript's geometry, the supremum of `E − Δ` over all bins, amplitudes and dyads
  (at `Δ → 0`) is `−2.28·10⁻⁴`. It is attained at `δ ≈ 0.386` (rightmost zero `a ≈ 0.69`),
  `x = 1/2`, `d = h = 13/16`. This matches the exact minimum of Lemma 20.2's quadratic. The paper
  proves the weaker valid bound `49/440640 ≈ 1.1·10⁻⁴`.

So **both sides are tight at 7/8**:

* the low side by construction;
* the high side within `2.3·10⁻⁴`, binding on rows with *mid-depth* zeros and maximal prime
  amplitude.

## 4. Experiments (results/*.json; Nelder–Mead over `(lx, ly, ℓ)`, fine re-verification)

> **Normalization of "DH counts"** (clarified by [SHORT_PROOF_FRONTIER.md](SHORT_PROOF_FRONTIER.md)).
> The model's `R = 1 − δ` is the density hypothesis for the **≈ U-member Kummer row family**. In the
> normalization of zero-density theorems for the *full* family of Hecke characters of `Q(√−3)`
> (`N ≪ (conductor)^{2A(1−σ)}`), it corresponds to `A = 1`, *stronger* than full-family DH
> (`A = 2`). Classical full-family inputs stall at `(7A−3)/(7A−2)`: 11/12 at `A = 2`, 29/31 for
> Hinz `A = 5/2`.

| Scenario | Inputs | Best σ0 | Binding constraint |
|---|---|---|---|
| A | manuscript lemmas, a priori `β* ≤ 11/12` | 0.874961 | mid-depth bin δ≈0.386, x=1/2, d=h |
| B | same, **iterated** from `β* ≤ 7/8` (κ ≥ 3/4 as Lemma 18.1 states) | 0.874960 | same bin |
| C | iterated, κ = 2β*−1 extrapolated below 3/4 | 0.874960 | same bin |
| D | density-hypothesis-quality counts `R = 1 − δ` | 0.869838 | floor bin (no zero right of 51/100) |
| F | DH counts **and** large-sieve-diagonal energy | 0.869838 | floor bin |
| G | trivial counts `R = 1` | infeasible below 11/12 | all bins |
| H | PR 910 joint moment (6.6) taken at face value: `R = 1 − δ·t`, `t ≤ 3/2` (also `t = 1`) | 0.869838 | floor bin |

Scenario H prices [PR 910](https://github.com/GettysburgResearch/riemann/pull/910)'s proposed
joint common-frequency moment. Even granted on the whole detector range, it buys only
`7/8 − 167/192 = 1/192 ≈ 0.0052` in this architecture. With
the detector floor also lowered toward 1/2 it buys at most `7/8 − 13/15 = 1/120`. The binding
constraint becomes the zero-free (floor) rows, which no zero-counting input can touch. By contrast,
in the Oct 5 architecture (moments of the sextic Möbius family), PR 910 §7 shows that the
conclusion `1/2 + 5ρ/12` improves without bound as the row/column ratio `ρ` decreases. However,
`ρ < 1` already needs an on-average GRH for the family, and row-blind inputs stop at 11/12
([RUNG_STRENGTH.md](RUNG_STRENGTH.md); [SYNTHESIS.md](SYNTHESIS.md)).

Single-lemma sensitivities are in Section 6.

Readings:

1. **7/8 is effectively optimal for the manuscript's own inputs.** Re-optimizing the geometry gains
   `4·10⁻⁵`, which is below the losses the manuscript reserves.
2. **The bootstrap is not iterable.** Feeding `β* ≤ 7/8` back in changes nothing, with or without
   extrapolating Lemma 18.1. The a priori bound enters only through `κ` (plain capacity) and the
   bin ceiling `δ ≤ 2β*−1`. The binding rows have `a ≈ 0.69`, far below any ceiling.
3. **Zero counting is necessary but not sufficient.** With trivial counts the architecture never
   closes. With perfect (DH-quality) counts it stalls near 0.8698.

## 5. The floor-bin barrier (exact, independent of any row-count input)

Rows whose twisted L-functions have no zero to the right of the detector floor `a0` cannot be
witnessed. They are counted trivially (`U^1` rows, each costing `U^{(2a0−1)/2}`). Their constraint
at the top dyad `d = h` is linear in the geometry:

    σ0 ≥ a0(1 − ly) − h/6 − ℓ/2 + (2a0−1)ℓ/2 + h(1 + (2a0−1)/2).

Adjoining it to the low-side rows gives exact LP barriers, with rational dual certificates verified
in fractions:

| Detector floor `a0` | Energy lemma | Barrier (any row counting) |
|---|---|---|
| 51/100 (manuscript) | manuscript | **167/192 ≈ 0.869792** at `lx = ly = 13/32`, `ℓ = 3/16` |
| 51/100 | large-sieve diagonal only | 167/192 (energy no longer binding) |
| 101/200 | either | 659/759 ≈ 0.868248 |
| → 1/2 | either | **13/15 ≈ 0.866667** at `lx = ly = 2/5`, `ℓ = 1/5` |

The `ly < lx` Gram regime gives the same values. At `a0 → 1/2` three constraints are simultaneously
tight:

* the zero-free (floor) rows on the Poisson side;
* the large-sieve diagonal `E_B ≥ M` on the reflected side;
* the dual-length branch `E_B ≥ 2M + ℓ − 1`.

**So 13/15 is the barrier of this architecture even with perfect zero counting and a perfect
reflected-energy bound.**

*Contour flexibility does not help.* For a bin with rightmost zero `a`, the central `w`-line can
sit anywhere in `[1−a, a]` with `s` on `Re s = a`. Phragmén–Lindelöf interpolation of the numerator
cost then makes the exponent affine in `Re w`, with slope `ly − d/2`, so an endpoint is optimal. At
`a0 → 1/2` the interval collapses to `{1/2}`.

At that limit the floor-bin cost is exactly "`U` rows, each of Lindelöf size". The 13/15 barrier
therefore holds even granting the **Generalized Lindelöf Hypothesis row by row**, together with
perfect zero counting and an optimal large sieve on the reflected side. It is a barrier for every
*pointwise* (row-by-row) treatment of the Poisson side combined with a Cauchy–Schwarz separation of
the reflected side.

Passing it requires at least one of:

1. **Cancellation across rows** for zero-free rows on the Poisson side. Their contribution is
   currently summed in absolute value. See [FLOOR_BIN_BARRIER.md](FLOOR_BIN_BARRIER.md).
2. **Cancellation beyond Cauchy–Schwarz in the low separation.** Any method that bounds `|J|` by
   (row ℓ²) × (additive ℓ²) inherits `E_B ≥ M`.
3. **A different probe.** The family floor is `5/6`; see [ALT_PROBES.md](ALT_PROBES.md).

### Leverage of a bilinear saving on the reflected side (exact LP)

The low estimate separates the probe as `Q^{-1/2} Σ_m A_m(Y) B_m(Z)`, where `A_m` is the additive
Gauss-sum polynomial and `B_m` the completed theta row, and then applies Cauchy–Schwarz. Suppose a
power saving `ϑ` beyond Cauchy–Schwarz were available uniformly in the geometry, with every
Poisson-side constraint (floor bin, rows treated pointwise) unchanged. The barrier LP then gives:

| ϑ | barrier, `a0 → 1/2` | barrier, `a0 = 51/100` |
|---|---|---|
| 0 | 13/15 ≈ 0.8667 | 167/192 ≈ 0.8698 |
| 1/100 | 322/375 ≈ 0.8587 | ≈ 0.8617 |
| 1/50 | 319/375 ≈ 0.8507 | ≈ 0.8537 |
| 1/20 | 62/75 ≈ 0.8267 | ≈ 0.8296 |
| 1/10 | 59/75 ≈ 0.7867 | ≈ 0.7893 |
| 1/4 | **2/3** at `lx = ly = 1/2`, `ℓ = 0` | ≈ 0.6713 |

The barrier is `13/15 − (4/5)ϑ` until the geometry degenerates to Part I. At `ϑ = 1/4` the only
remaining obstruction is the Poisson-side floor bin of the *Part I* probe, which sits exactly at its
signal offset `2/3`.

The reflected-side bilinear form is therefore the single highest-leverage input. Each unit of
saving there is worth `4/5` of a unit of boundary, whereas row-count improvements are capped by
the floor bin. Note that `Σ_m A_m B_m` *is* the probe; Poisson summation in `m` is what produces
the high side. A bilinear saving thus needs a genuinely intermediate treatment of the `m`-sum. For
example, the large sieve could be applied to the product character
`m ↦ χ_s(m) χ_{cn³}(m)` jointly, instead of separating `s` from `(c, n)`. (PROPOSED direction;
no such estimate is claimed.)

## 6. Single-lemma sensitivities

See `results/S*.json`; summary table filled from those runs:

| Change (all else manuscript) | Best σ0 |
|---|---|
| plain capacity `2m + 4κz ≤ 1` (was 6κ) | 0.874712 (gain 2.9·10⁻⁴) |
| inverse capacity `r + z ≤ 1` (was `r + 2z`) | (run in progress; see results/S2_invcap1.json when present) |
| amplification slope α = 3/4 (was 5/6) | 0.874514 (gain 4.9·10⁻⁴) |
| detector `t ≤ 2` (was 3/2) | not run (stopped for CPU) |
| central contour `z0 = 0.33` (was 17/50) | not run (stopped for CPU) |
| prime slots used for `d ≥ 0.05` (was 1/2) | not run (stopped for CPU) |

Every single-lemma improvement tried buys less than `5·10⁻⁴`. The 7/8 architecture is
rigid with respect to its moment constants. Large movements need the structural changes of
Section 5.

## 7. Lemma-range obligations for any other geometry

* Lemmas 10.3–10.5 are stated for `σ0 ∈ [7/8, 1)`. The principal Euler region (7.15) is stated for
  `Re x ≥ 7/8`, but its exponents `4 − 6x − 6z` and `1 − x − w − 6z` give normal convergence for
  `Re x > 2/3 + η`. Extension looks routine but is unverified.
* Lemma 18.1 is stated for `κ ∈ [3/4, 1]`.
* The proof of Lemma 15.1 uses `M + ℓ = 1`. Our general formula is the LP supremum of (14.14).
* Prop. 15.2 assumes `P_a ≥ 1`. Prop. 19.2 assumes prime supply `> 7/37` with a fixed margin; the
  model replaces this with supply-capped capacities.
* Prop. 8.3 uses `δ ≥ 1/50` to force `m ≤ 1/2 + O(ε)`. Lowering the floor `a0` needs
  `δ0`-dependent constants.

## 8. The Kintali variant in the same language

[K] uses the Part I probe, so its low side caps it at 11/12. Its comparison inequality with a
Hecke zero-density exponent `A` (`N ≪ (Q²T)^{A(1−σ)}`) is
`max_a [a + min(1, 2A(1−a))/2 − 1/3] = 7/6 − 1/(2A)`:

* `A = 5/2` gives `29/30`, and with [K]'s margin `1/80` the result is `47/48`;
* the density hypothesis `A = 2` gives exactly `11/12`.

So [K]'s route reaches 11/12 only with DH-quality Hecke density, and never passes it.

## 9. What this means for the repository

The architecture is a *two-representation* continuation principle with a family supremum. Its
limits are governed by three things:

* zero-free rows, which are counted, not cancelled;
* the large-sieve diagonal on the reflected side;
* the `ζ_F(6z)` pole at `1/6`.

None of these scale toward `1/2`. The method is therefore structurally a *quasi*-RH method: even
an idealized version stalls at 13/15, and the probe family at 5/6. Section 5's escape routes are
the concrete "unturned stones"; the companion notes assess each one.
