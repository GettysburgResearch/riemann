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

| Scenario | Inputs | Best σ0 | Binding constraint |
|---|---|---|---|
| A | manuscript lemmas, a priori `β* ≤ 11/12` | 0.874961 | mid-depth bin δ≈0.386, x=1/2, d=h |
| B | same, **iterated** from `β* ≤ 7/8` (κ ≥ 3/4 as Lemma 18.1 states) | 0.874960 | same bin |
| C | iterated, κ = 2β*−1 extrapolated below 3/4 | 0.874960 | same bin |
| D | density-hypothesis-quality counts `R = 1 − δ` | 0.869838 | floor bin (no zero right of 51/100) |
| F | DH counts **and** large-sieve-diagonal energy | 0.869838 | floor bin |
| G | trivial counts `R = 1` | infeasible below 11/12 | all bins |

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
reflected-energy bound.** Passing it requires at least one of:

1. **Cancellation across rows** for zero-free rows on the Poisson side. Their contribution is
   currently summed in absolute value. See [FLOOR_BIN_BARRIER.md](FLOOR_BIN_BARRIER.md).
2. **Cancellation beyond Cauchy–Schwarz in the low separation.** Any method that bounds `|J|` by
   (row ℓ²) × (additive ℓ²) inherits `E_B ≥ M`.
3. **A different probe.** The family floor is `5/6`; see [ALT_PROBES.md](ALT_PROBES.md).

## 6. Single-lemma sensitivities

See `results/S*.json`; summary table filled from those runs:

| Change (all else manuscript) | Best σ0 |
|---|---|
| plain capacity `2m + 4κz ≤ 1` (was 6κ) | (pending) |
| inverse capacity `r + z ≤ 1` (was `r + 2z`) | (pending) |
| amplification slope α = 3/4 (was 5/6) | (pending) |
| detector `t ≤ 2` (was 3/2) | (pending) |
| central contour `z0 = 0.33` (was 17/50) | (pending) |
| prime slots used for `d ≥ 0.05` (was 1/2) | (pending) |

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
