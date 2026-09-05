# Lane 3 checkpoint 4 — SKELETON of T-105040 (draft text; NOT deposited)

# T-105040 — All-x feasibility of the frozen 61-smooth block under the aggregate license

Claim ID: `T-105040`
Status: **SKELETON — statement audited (Lane 3); [expansion lemma] and [cell
certification] not yet executed; DO NOT DEPOSIT until both are replay-locked**
Created: 2026-08-22
Agent: claude (external reviewer lane)
Depends on: `L-99020` (system + two-sort identity; the aggregate downstream
contract as adjudicated in `L-105031 §1`) @
`review/gpt56-pro/99600-three-interface-hostile-audit`; `L-99240.1–.2` (kernel
`γ_j`, row `Q_Y(j)`) @ `review/gpt56-pro/99440-half-order-subsidy-audit`;
`R-99020` (x = 2 firewall) @ `review/gpt56-pro/99820-native-box-normalization-audit`;
`L-105031` (Theorem R exact reduction; Lemmas 1–2 monotonicity; (f) frozen
balance `TB_s ≥ 1.676601032` all `x ∈ [2, P₆₁]`); `L-105022` (quarantine).
Replay: `experiments/X-105040-frozen-block-all-x/` (to be created).
RH status: **unproved, not addressed**

## 1. The frozen system

Fix the lattice `D = {squarefree d | P₆₁}`, `|D| = 2¹⁸`,
`P₆₁ = ∏_{p ≤ 61} p = 117288381359406970983270 ≈ 1.1729·10²³`. For real
`x ≥ 2` the active atoms are `d ∈ D, d ≤ x` with target
`T_x(d) = (4√(x/d) − 3)/√d`, score `s_x(d) = 5/4 + (3/4)/(4√(x/d) − 3)`, and
component rows `Q_{x/d}(j)/√d` (`Q` per `L-99240.2`). Odd-μ atoms are demands,
even-μ atoms capacities. The **aggregate license** (the adjudicated downstream
contract of `L-99020 §§2–3`, per `L-105031 §1`) admits flows on all pairs
subject to demand equality, capacity, and the three aggregates
`B_{x,2} ≥ 0`, `B_{x,3} ≥ 0`, score edge term `≤ 0`.

By Theorem R (`L-105031 §2`, index-set-agnostic — Lemma 0 below), aggregate
feasibility at fibre `x` is equivalent to the four arithmetic inequalities

```
TB_s(x) ≥ 0,   M_2(x) ≥ 0,   M_3(x) ≥ 0,   M_sc(x) ≥ 0,
```

where, with `θ*` the greedy prefix-fill usage fractions (smallest evens first),

```
TB_s(x) = 4√x A^s_x − 3 B^s_x,       A^s_x = Σ μ(d)/d,  B^s_x = Σ μ(d)/√d   (d ∈ D, d ≤ x)
M_j(x)  = Σ_e θ*(e) Q_{x/e}(j)/√e − Σ_o Q_{x/o}(j)/√o          (j = 2, 3)
M_sc(x) = (3/4)[ −B^s_x + Σ_e (1 − θ*(e))/√e ].
```

## 2. Theorem (statement)

**For every real `x ≥ 2` the frozen 61-smooth block is aggregate-licensed
feasible: `TB_s(x) ≥ 1.676601032` and `M_2(x), M_3(x), M_sc(x) ≥ 0`.
Moreover `M_2(x) > 0` for `x > 2`, `M_3(x) > 0` for `x > 3`, and
`M_sc(x) ≥ 0.273956` for all `x ≥ 2`; the row equalities `M_2(2) = 0` and
`M_3(x) = 0` on `[2, 3]` are exact (degenerate empty rows: `Q_Y(j) = 0` for
`Y ≤ j`).**

Asymptotics (proved as part of §3.4): for `x ≥ x_sat` the greedy threshold
freezes at the 132nd even `e* = 1110` with `θ*(e*) → 0.4198826`, and

```
M_j(x) = σ_j Δ₂ · log x + c_j + o(1),   M_sc(x) → 13.903914...,
σ_2 Δ₂ = 30.0993...,  σ_3 Δ₂ = 11.0039...,
σ_j = A_j/√j − B_j/√(j+1) + C_j(ζ(1/2) − Σ_{m ≤ j+1} m^{−1/2}),
Δ₂ = Σ_e θ*_∞(e)/√e − Σ_o 1/√o = −18.538552496...
```

## 3. Proof structure (four gates)

**Lemma 0 (frozen Theorem R).** Theorem R restricts verbatim to any sub-index
set: aggregates are affine in column sums; `ρ_j` is a nonincreasing function of
`k` for every `j ≥ 2` and `s` an increasing one (`L-105031` Lemmas 1–2, functions
of `Y = x/k` alone); the product flow realizes any admissible column profile
(`D > 0` for `x ≥ 2` since `d = 2` is active). Greedy `c*` is simultaneously
weakly optimal for all rows and the score; no ties (distinct divisors; `ρ_j = 0`
tail immaterial; `s` strict). [One page; already proved in substance in
`L-105031`, restated for the frozen index set.]

**Gate 1 — balance, all x: DONE.** `TB_s(x) ≥ 1.676601032` for all real
`x ∈ [2, P₆₁]` by the complete `2¹⁸`-cell enumeration (`L-105031(f)`,
`lattice.py`; on each cell `[d_i, d_{i+1})` TB is affine in `√x`, so cell
endpoints suffice; infimum at `x → 33⁻`), and `TB_s = 4√x·0.13158... − 3·B^s`
grows like `0.5263√x` for `x ≥ P₆₁`. Hence the greedy fill always completes.

**Gate 2 — [expansion lemma] (to be written; currently numerics-supported).**
Effective form of `H(Y) = Σ_{m ≤ Y} m^{−1/2} log(Y/m) = 4√Y + ζ(1/2) log Y +
ζ'(1/2) + E(Y)` with a PROVED bound `|E(Y)| ≤ c_E·Y^{−3/2}` (Euler–Maclaurin
with explicit remainder: the log-weight vanishes at `m = Y`, killing the
half-integer wobble, and the leading remainder is the EM boundary term
`f'(Y)/12 = −Y^{−3/2}/12` — measured `E(10³) = −2.635·10⁻⁶` vs predicted
`−(1/12)10^{−4.5} = −2.64·10⁻⁶`, with the `10^{3/2}` per-decade decay confirmed
over four decades). NOTE HONESTLY: today `ζ'(1/2)` enters as a
numerically identified constant; the deposit must derive it (standard:
differentiate the analytic continuation of `Σ m^{−s}`; `E` bound by
Euler–Maclaurin at second order). Corollary: the exact knot form of `Q_Y(j)`
(`L-99240.2`) becomes `Q_Y(j) = 4C_j√Y + σ_j log Y + τ_j + C_j E(Y)` for
`Y ≥ j + 2`, with `σ_j` as in §2 and explicit `τ_j`.

**Gate 3 — [cell certification], `2 ≤ x ≤ X₀` (finite computation, to be
executed).** On the finite mesh consisting of (i) activations `x = d`, (ii) knot
lines `x = m·d` (`m ≤ x/d` integer — the floor kinks of `Q`), and (iii) greedy
threshold-index changes (each cell's threshold comparator `4√x·a − 3b` is affine
in `√x`, so each of the finitely many index transitions crosses each cell at
most once), all three margins are piecewise-smooth in `x`; certify
`M_j, M_sc ≥ 0` cell-by-cell with interval arithmetic or endpoint values plus a
per-cell derivative bound. Use the JUMP LAW (audited, Lane 3): at activations
`M_2, M_3` jump weakly UP at odds and are continuous at evens, `M_sc` jumps
strictly UP at odds ( `= (1/√o)(2 − s(e*)) > 0` ) and is continuous at evens;
so only left-limits `x → d⁻` and interior cell behavior need certification —
activations never hurt rows/score. (`TB` has the opposite pattern — down `1/√o`
at odds — and is already closed by Gate 1.) Verified so far: no negative value
on `[2, 2000]` (integers + all activation left-limits + 41-point cells on
`[2,67)`); minima `M_sc ≥ 0.273956906` (at `x → 3⁻`), rows `≥ 0` with the §2
degeneracies.

**Gate 4 — [saturation lemma], `x ≥ X₀` (analytic, from Gates 2 + finitely many
sign checks).** For `x ≥ P₆₁` all `2¹⁸` atoms are active; each threshold
comparator is affine in `√x`, so the greedy threshold index changes at most
finitely often and freezes at index 132 (`e* = 1110`; the prefix-excess
`Σ_{132 smallest evens} 1/e − Σ_o 1/o = 5.226·10⁻⁴ > 0` certifies the limit
index). With `θ*` frozen up to `O(x^{−1/2})`, the exact identities

```
4√x·Δ₁ = 3Δ₂  (demand equality),   M_sc = −(3/4)Δ₂,   M_j = 3C_jΔ₂ + ΔR_j = ΔR_j − 4C_j·M_sc
```

reduce the margins to `M_j(x) = σ_jΔ₂ log x + c_j + O(x^{−1/2} + E-terms)` with
`σ_jΔ₂ = 30.0993 (j=2), 11.0039 (j=3)` and `M_sc → 13.903914`. Since the slopes
are positive and the constants certified at one anchor `x = X₀`, positivity for
all `x ≥ X₀` follows with explicit error control. [The `O(·)` constants must be
made explicit in the deposit; all displayed values independently verified at
`x = 10²⁶, 10²⁸, 10³⁰, 10³⁴`.]

## 4. Constants table (all independently recomputed, Lane 3)

| constant | value | source |
|---|---|---|
| `P₆₁` | 117288381359406970983270 | lattice product |
| min `TB_s`, all real `x ≥ 2` | 1.676601032 at `x → 33⁻` | L-105031(f), reconfirmed |
| `TB_s` slope beyond `P₆₁` | `0.5263√x` (`A^s = 0.1315873519`) | reconfirmed |
| `B^s_∞ = ∏(1 − p^{−1/2})` | +0.0022144006 | reconfirmed |
| min `M_sc`, all `x` scanned | 0.273956906 at `x → 3⁻` | Lane 3 scan |
| `M_sc(∞)` | 13.903914 | reconfirmed (= −(3/4)Δ₂) |
| `Δ₂` | −18.538552496 | Lane 3 |
| threshold even / index / `θ*` | 1110 / 132nd / 0.419882603 | reconfirmed |
| sliver (θ < 1) | 130941 of 131072 evens | reconfirmed |
| `σ_2, σ_3` | −1.623491, −0.593570 | closed form + numeric |
| slopes `σ_jΔ₂` | 30.0993, 11.0039 | reconfirmed (exactly affine increments) |
| `ζ(1/2), ζ'(1/2)` | −1.4603545088, −3.9226461392 | expansion lemma (Gate 2) |
| frozen margins at `x = 10⁶` | 106.1986 / 39.3933 / 10.7443 | reconfirms L-105031(f) |
| degeneracies | `M_2(2) = 0`; `M_3 ≡ 0` on `[2,3]` | exact, Lane 3 |

## 5. Honest scope (what this theorem does NOT say)

1. Nothing about the FULL-SUPPORT block (`all squarefree k ≤ x`): its four
   inequalities are the open core (`L-105031 §4`) — sign-uniformity of weighted
   Mertens-type sums — and are NOT addressed. The frozen block coincides with
   full support only for `x < 67`.
2. Nothing about the rough half: primes `> 61` never enter the lattice. The
   moving-cut architecture's smooth block (`O-105010 §2.1`) is a GROWING
   `Y^θ`-smooth family; **no deposited consumer consumes the frozen block at
   `x ≥ 67`** — this theorem is the deformation-family/limit statement for the
   `L-99020` alphabet continued past its ceiling, not a consumed interface, and
   it does not discharge O-105010's uniform-in-θ demand.
3. The license is exactly the `L-105031 §1` aggregate contract (rows `j = 2, 3`
   + score + `u ≥ 0`), whose adjudication (only aggregates consumed; the word
   "coefficientwise" in `L-99020.6` was the nested device) is INHERITED, not
   re-proved. If a re-audit demands per-edge nonnegativity, this theorem does
   not survive in that regime (the greedy flow provably carries anti-monotone
   edges); if it demands rows `j ≥ 4`, the same greedy `c*` is optimal for them
   and the theorem extends by adding margins — neither case is claimed.
4. The `R-99020` x = 2 firewall and sort discipline are preserved verbatim; the
   row sort is never a complete positive score packet (`M_2(2) = 0` is the
   degenerate boundary of exactly that firewall).
5. RH is not addressed. The theorem is elementary-finite: a finite lattice, one
   asymptotic expansion with effective remainder, and finite certifications.

## 6. Falsifiers

F1. Any real `x ≥ 2` with `M_2, M_3` or `M_sc < 0` (single interval-arithmetic
    cell suffices; the Gate 3 mesh is where it would hide — esp. interior dips
    between knots, which the jump law does NOT protect).
F2. Failure of the effective `|E(Y)| ≤ c_E·Y^{−3/2}` bound, or `ζ'(1/2)` mis-identified
    (would shift `σ_j` and the saturation constants).
F3. Threshold-index instability: infinitely many greedy-threshold changes as
    `x → ∞` (excluded by affine-in-`√x` comparators — if that argument is wrong
    the saturation lemma collapses).
F4. Contract re-adjudication (per-edge rows, or rows `j ≥ 4` consumed) — see §5.3.
F5. Any discrepancy between the greedy margins and a full pair-variable LP on
    the frozen lattice at any fibre (Theorem R falsifier; cross-checked to
    `8.3·10⁻¹³` at `≤ 94k` variables on full support in `lp_check.py`; rerun on
    frozen fibres).

## 7. Acceptance fixtures for the replay

1. `TB_s` cell-exact minimum `1.676601032` at `x → 33⁻` (2¹⁸ enumeration).
2. `M_2(2) = 0` exactly; `M_3(x) = 0` at `x = 2, 2.5, 3` exactly; `M_2(3⁻) =
   0.294016`, `M_sc(3⁻) = 0.273957` (left limits).
3. Jump table at `d = 7, 29, 33, 61`: `ΔTB = μ(d)/√d` (±1e-9); `Δm_sc(7) =
   +0.246091`; `Δm_2, Δm_3, Δm_sc = 0` at `d = 33` (even) within continuity drift.
4. Integer + left-limit sweep `[2, 2000]`: zero negatives; minima as in §4.
5. Frozen `x = 10⁶`: `M_2 = 106.1986`, `M_3 = 39.3933`, `M_sc = 10.7443`,
   threshold `e* = 899`, sliver 3289/3408.
6. Saturation: `M_2 = 1471.1659 / 1609.7685 / 1748.3711 / 2025.5764` and
   `M_3 = 538.6998 / 589.3748 / 640.0498 / 741.3997` at `x = 10²⁶/10²⁸/10³⁰/10³⁴`;
   `M_sc = 13.903914` at all four; threshold 1110 (132nd even), `θ* = 0.4198826`,
   sliver 130941; `B^s = 0.0022144006`; identity `M_j = ΔR_j − 4C_j M_sc` to
   `< 10⁻¹⁰`; increments exactly affine: `138.6026` (j=2) and `50.675` (j=3) per
   two decades.
7. Precision discipline: fixtures at `x ≥ 10²⁶` must run at ≥ 40 dps OR the
   cancellation-free restructuring (`M_j = 3C_jΔ₂ + ΔR_j` with the expansion
   branch never forming `4√Y`); naive float64 on the raw formula FAILS (loses up
   to 16 absolute digits; recorded Lane 3 incident: `M_2(10³⁴)` off by 5).
8. LP cross-check on frozen fibres at `x = 88, 10⁴ − ε, 10⁵` (Theorem R).
