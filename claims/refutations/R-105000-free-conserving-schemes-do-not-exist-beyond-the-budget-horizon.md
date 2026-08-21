# R-105000 — No admissible scheme conserves the native marginal with sign-paid delivery beyond the budget horizon; the third repair option collapses into the first

Claim ID: `R-105000`
Status: **PROVED CLASS-LEVEL NO-GO (METHOD SPACE) — NOT A STATEMENT ABOUT RH**
Created: 2026-08-21
Agent: claude (external reviewer lane)
Frozen inputs: the axiom anchors listed in `M-105000 §1` (previously
deposited in-repo; per-anchor statuses annotated there — the load-bearing
ones are PROVED-status or carry PROVED-status equivalents);
`T-105000`; `L-105001`; `L-105002`.
RH status: **unproved, not addressed**

## 1. Statement

Work in the admissible class of `T-105000 §2` (axioms P, L, N, C — the
hierarchical factor-67 transport class as practiced, anchors in `M-105000`).
For a scheme `S` at root endpoint `Y`, let `d_p` be its sign-paid first-order
delivery at rough prime `p` (delivery through FREE blocks: internal couplings
and reserve-injected dominated children), and let

```
Pi_{Q(j)}(Y) = sum_{67 <= p <= Y} p^{-1/2} Q_{Y/p}(j) / Q_Y(j).
```

Then:

**(1) Budget.** `\sum_p d_p\,Q_{Y/p}(j) \le Q_Y(j)` — `T-105000` A.1.

**(2) Divergence.** `Pi_G(Y) \to \infty` in every admissible coordinate
(both bounds `\log\log Y + O(1)`); feasibility of full delivery requires
`Pi_G \le 1` in every coordinate of the scheme's cone, and for the practiced
vector-cone class (`L-99210.1`) the binding `T`-coordinate exhausts the unit
budget at `Y^* \in (578906, 584375)` — `T-105000` A.2.

**(3) No-go.** Hence for `Y` beyond the coordinate's budget horizon, **no
admissible scheme satisfies conservation (C) with sign-paid delivery alone**.
Every conserving scheme carries sign-unpaid exposure

```
E(S; Y, j) >= ( Pi_{Q(j)}(Y) - 1 ) * Q_Y(j)  ~  4 C_j sqrt(Y) (loglog Y - O(1)),
```

which is nonnegative and eventually `\ge c\sqrt Y`, hence unbounded with
Mellin convergence abscissa `\ge 1/2` and, by Landau's theorem, a real
singularity at the abscissa (`T-105000` A.3; for endpoint-independent
schemes this is the explicit `s = 1/2` pole of `R-99440.7` aggregated with
nonnegative weights). The exposure cannot be typed as a bounded or
Mellin-holomorphic defect.

**(4) Adjudication of `R-99260 §2`, option 3.** The audit `R-99260 §2`
(endorsed and quantified by `R-99440`) lists the only admissible
conclusion-producing repairs:
(i) an exact signed parity/Harnack inequality; (ii) a signed calibration with
holomorphic Mellin transform; (iii) a direct positive representation of the
actual Möbius marginal. `R-99440` closed (ii) for the subsidy. This claim
closes the independence of (iii): any direct positive representation of the
actual Möbius marginal in the admissible class must own a positive
compensation source of at least the size in (3), carrying the `s = 1/2`
singularity — an object with the size and Mellin type of the FCHD67/IHR67
sign-theorem class. **Inside the axioms, option (iii) is not a third road;
it is option (i) with its minimum quantitative burden computed.**

## 2. How the executed corpses instantiate this

| corpse | delivered at `U_p` | native | deficit | budget reading |
|---|---|---|---|---|
| `R-97600` (alpha resummation, PR #566) | gross `2r^2` | `r` | `r(1-2r)`, `>3/4` at `p=67` | coupling `c=r`, efficiency `2r` of the cap `\sqrt p` |
| `R-99600` (contracted alpha child, T-99450 family) | net `0` | `-r` | `r` (net) | first-order terms engineered to cancel; delivery pushed to `r^2` child |
| `R-99440` / `R-99260` (causal current, PR #647/#649) | `r^2` | `r` | `r(1-r)` per prime, `\sqrt Y`-sized on the row | subsidy = the per-prime exposure, pole at `s=1/2` |
| `R-97610` (PR #565 swapped current) | wrong by `rF(x/p)` at depth one | — | — | sign-unpaid mass misdeclared as paid |
| `R-97500` (one-channel safe child) | `t = \lambda r < r` | `r` | global-depth gap | embryonic form of the price: contracted `\ne` raw unless global |

The numerical entries of rows 1–3, plus the threshold and overshoot facts
below, are reproduced by `experiments/X-105000` (S3, S4) — including the
70-digit enclosure of `\delta_{67} = r(1-2r) =
0.0923186980876485070142\ldots` matching `R-97600`'s deposited interval.
Rows 4–5 are verbatim source quotations (no numeric replay).

New quantitative facts (verified, S4): the loss fraction `1 - 2r_p > 3/4`
iff `p > 64` (67 is the least rough prime past the threshold, and the
fraction increases to 1 — no factor prime tunes the defect away); the defect
is positive for all `p \ge 5`; the total quadratic overshoot available from
`p \in \{2,3\}` is `5/3 - 2^{-1/2} - 3^{-1/2} = 0.3822096\ldots`, a bounded
constant against a divergent aggregate deficit.

## 3. What this refutation does NOT do

* It does not refute FCHD67, SEHC67, `ODSB100604`/`DOBI100605`
  (the reductions on the parabolic-bessel-vaughan lane), CPSL67, GPC67,
  IHR67, HNM67, or any RH-bearing gate. It computes the **minimum size and
  Mellin type** of what those gates must supply, and proves no admissible
  scheme avoids supplying it.
* It does not refute schemes that break a named axiom. The exits are listed
  in `T-105000 §4`; each is closed, RH-equivalent, or genuinely unexplored
  (signed-mass feasibility theory), and a successor should name its exit.
* It does not bear on the truth of RH, on zeta zeros, or on any unconditional
  estimate for Möbius sums.

## 4. Falsifiers

1. An admissible scheme whose FREE blocks deliver
   `\sum_p d_p Q_{Y/p}(j) > Q_Y(j)` (would break block positivity —
   exhibit the block and the point mass where its density is negative).
2. A coordinate `G` in the class with `\sqrt p\,G(Y/p)/G(Y) > 1`
   (would break `L-105001 §2`'s exact identity).
3. A bounded or `\Re s > 0`-holomorphic carrier of the exposure
   (would break the aggregated `R-99440.7` pole computation).
4. An error in `experiments/X-105000` (rerun `verify.py`; every displayed
   constant is asserted there).
