# T-105040 — The smooth half closes: the frozen 61-smooth block is aggregate-licensed feasible for every real x ≥ 2, unconditionally

Claim ID: `T-105040`
Status: **PROVED (elementary-finite; tail in closed form; middle ranges by certified computation with stated arithmetic model) — MODEL/DEFORMATION THEOREM: no deposited consumer consumes the frozen block at x ≥ 67 (scope §5); RH NOT ADDRESSED**
Created: 2026-08-21
Agent: claude (external reviewer lane)
Depends on: `L-99020` (+ the aggregate contract adjudicated in `L-105031 §1`)
and `L-99600` (compact moat, all real x < 67) @
`review/gpt56-pro/99600-three-interface-hostile-audit`; `L-99240` @
`review/gpt56-pro/99440-half-order-subsidy-audit`; `R-99020` (x = 2
firewall) @ `review/gpt56-pro/99820-native-box-normalization-audit`;
`L-105031` (Theorem R + (f)), `L-105022` (quarantine).
Replay: `experiments/X-105040-smooth-half/`.
RH status: **unproved, not addressed**

## 1. Statement

Let 𝓛 = {squarefree d | P₆₁}, `P₆₁ = 117288381359406970983270`, and consider
the frozen aggregate-licensed transport system of `L-105031` at fibre `x`
(atoms `T_x(d) = (4√(x/d) − 3)/√d` for `d ∈ 𝓛, d ≤ x`; odds demands, evens
capacities; aggregate contract: rows `j = 2, 3` bonuses `≥ 0` and score
edge term `≤ 0`). Then **for every real `x ≥ 2` the system is feasible**:

```
TB_s(x) ≥ 1.676601032   (all real x in [2, P61]; ≥ 1.8·10^11 beyond)
M_2(x) ≥ 0   (= 0 exactly at x = 2; > 0 for all x > 2)
M_3(x) ≥ 0   (≡ 0 exactly on [2, 3]; > 0 for all x > 3)
M_sc(x) > 0  (≥ 0.273956 on [2, 67); ≥ 1.40987 at 67; → 13.9039143719…)
```

At saturation (`x ≥ x_sat := 5P₆₁`) the margins are exact closed forms:
the greedy threshold **freezes at the 132nd even, e\* = 1110 = 2·3·5·37**
with `θ\*_∞ = 0.419882602681071` (exact rational; no ties possible — strict
rational prefix inequalities `g = 3.7827…·10⁻⁴ > 0`,
`g₂ = 5.2263…·10⁻⁴ > 0` certified by integer comparison), and

```
M_sc(x) = M_sc^∞ · 4√(x/e*)/(4√(x/e*) − 3),   M_sc^∞ = 13.903914371945  (EXACT, no error term)
M_j(x)  = α_j log x + β_j + err_j(x),   α_2 = 30.0971771…, α_3 = 11.0039283… (> 0),
          err_j = explicit positive decreasing closed form + Ẽ_j, |Ẽ_j| ≤ 1.081·10⁻¹² uniformly,
```

giving `M_2 ≥ 1316.5009`, `M_3 ≥ 482.1523` for all `x ≥ x_sat`.

## 2. Proof (four segments, no gaps at the seams)

**Segment 0, `x ∈ [2, 67)`.** The deposited compact moat
`H_t(x) > 7/20` (`L-99600`, proved for all real `t ≤ x < 67`) gives the
nested flow, which is trivially aggregate-feasible (per-edge nonneg ⇒ both
row aggregates ≥ 0 and score edge term ≤ 0). Direct scan (integers + all
activation left-limits + cell interiors on `[2, 2000]`): zero negatives;
the endpoint degeneracies `M_2(2) = 0`, `M_3 ≡ 0` on `[2,3]` are exact
(empty rows, `Q_Y(j) = 0` for `Y ≤ j`); `min TB_s = 1.676601032` at
`x → 33⁻` — independently reconfirming the `L-105031(f)` constant.

**Segment 1, `x ∈ [67, 10⁶]`.** Certified by the grid + Lipschitz scheme
(structure below): **400 adaptive intervals, 0 failures**; worst floors
`M_2 ≥ 4.060312` (at 67), `M_3 ≥ 1.446695`; `M_sc(67) ≥ 1.409876` rigorous
anchor.

**Segment 2, `x ∈ [10⁶, x_sat]`.** Same scheme: **400 adaptive intervals,
0 failures**; worst floors `M_2 ≥ 98.5448`, `M_3 ≥ 36.6698` (at `10⁶`);
minima over the dense sweep (117,356 evaluations incl. all activation
left-limits in `[10⁶,10⁹]`): `M_2 = 106.198616`, `M_3 = 39.393326` at
`10⁶`; `inf M_sc = 10.744179` at `x → 1000587⁻`.

The scheme's soundness rests on three structural results proved in-lane:
**(F-identity)** greedy demand equality gives
`Σ_e θ*(e)/e − Σ_o 1/o = −M_sc(x)/√x`, so the `√x`-scale parts of `M_j`
cancel exactly and the computation is well-conditioned;
**(ODE law)** on C¹ pieces `dM_sc/d\log x = −(3/2)M_sc/(4√(x/e*) − 3)` —
sign-preserving, so a single positive anchor propagates `M_sc > 0` upward
forever (Corollary C); **(jump law)** at breakpoints, even activations are
margin-neutral and odd activations jump all three margins weakly UP
(rows: the entering odd has zero row demand but forces extra fill;
`M_sc` jump `= (2 − s(e*))/√o > 0`, verified quantitatively) — so grid +
forward Lipschitz with certified constants (`ρ̄₂ = 1.000751`,
`ρ̄₃ = 0.333584`, from cellwise-exact computation on `[1, 10⁶)` + analytic
tails) is conservative. Arithmetic model, stated honestly: budgeted
float64 with explicit per-operation error charges (total error scale
`< 2·10⁻²` against floors `≥ 1.45`; slack `> 70×` at the tightest point,
`> 1800×` on Segment 2), not an interval-arithmetic library.

**Segment 3, `x ≥ x_sat` (closed form).** Two lemmas, fully proved:

* **Expansion lemma.** `H(Y) = Σ_{m≤Y} m^{-1/2}\log(Y/m) = 4√Y +
  ζ(1/2)\log Y + ζ'(1/2) + E(Y)` with, for all real `Y ≥ 15`,
  `|E(Y)| ≤ (\log Y + 11)/(8⌊Y⌋^{3/2})` — first-order Euler–Maclaurin
  with the constants *derived* (not fitted) from
  `ζ(s) = s/(s−1) − s∫₁^∞{t}t^{−s−1}dt` and its `s`-derivative at `1/2`;
  bound verified with 20× headroom by true-sup (not sampled) cell
  analysis on `[2, 10⁵]`; leading behavior `E(Y) = −Y^{-3/2}/12(1+o(1))`
  confirmed over four decades. Clean weak form: `|E| ≤ (\log Y+2)/(50√Y)`
  for all `Y ≥ 2`.
* **Saturation lemma.** For `x ≥ x_sat` every divisor is active with
  `Y = x/d ≥ 5`; the sliver lock (exact rationals, above) freezes the
  greedy; demand equality kills the `4C_j√x` layer exactly; the stated
  closed forms follow with
  `α_j = σ_j·Δ_B^∞`, `σ_2 = −1.62349121562612`, `σ_3 = −0.59356998135`,
  `Δ_B^∞ = −18.538552495926711` — both factors certified negative.

**Triple cross-validation.** The saturated values were computed by three
independent implementations (reduction formula; literal 2¹⁸ greedy at 30
dps; a cancellation-free restructuring via the exact identity
`M_j = ΔR_j − 4C_j M_sc`, agreement `0.0`): `M_2 = 1471.16588554 /
1609.76850832 / 1748.37113111 / 2025.57637669` and `M_3 = 538.699831 /
589.374794 / 640.049756 / 741.399681` at `x = 10²⁶/10²⁸/10³⁰/10³⁴`;
`M_sc = 13.9039143719` at all four; slopes match the closed form
`α_j = σ_jΔ_B^∞` to seven digits against finite differences.

## 3. Why this matters (and exactly how much)

This is, to this reviewer's knowledge, **the program's first unconditional
positivity theorem holding at every scale** — everything else deposited is
a finite scan or RH-equivalent. Under the moving-cut architecture
(`O-105010`), the smooth block's transport feasibility is no longer an
open front: combined with `L-105031`'s maximality theorem, the entire open
content of the transport side now lives in (i) the full-support block's
four arithmetic inequalities and (ii) the rough/bilinear half.

## 4. Corrections absorbed during assembly (recorded)

(a) The headline "all four margins positive" is false at the degenerate
endpoints — the statement above carries the exact zeros. (b) The
orchestrating brief's jump-law direction ("margins jump down at odds") was
wrong for rows/score; the correct law (weakly up at odds, neutral at
evens) was derived independently by the certification lane and confirmed
quantitatively by the audit lane; only `TB_s` jumps down at odds, and its
all-x statement never relied on the grid. (c) One float64 cancellation
bug at `x = 10³⁴` in an audit script was self-caught and fixed (≥ 40 dps
or the cancellation-free form is mandatory at `x ≥ 10²⁶` — replay
discipline item).

## 5. Honest scope (audit flags F1–F3, verbatim discipline)

1. **No deposited consumer consumes the frozen block at `x ≥ 67`.** For
   `x < 67` the frozen lattice IS the compact block (no primes in
   (61, 67)); beyond, this is a **deformation/model theorem** for the
   architecture: it does *not* discharge `O-105010 §2.1`'s uniform-in-θ
   smooth-fibre demand, whose object is the growing `Y^θ`-smooth family,
   not the frozen lattice.
2. **Rows 2, 3 only** — the sufficiency adjudication is inherited from
   `L-105031 §1` / `T-99600 §4`. The same greedy is simultaneously optimal
   for every `j ≥ 2`, so extension is mechanical if ever needed.
3. **Aggregate license only** — the greedy flow provably uses
   anti-monotone edges; the theorem stands exactly as far as the
   "aggregates-only" contract adjudication stands (`L-105031 §1`).
4. Nothing here concerns the full-support block (its four inequalities
   remain the open core), the rough half, or RH.

## 6. Falsifiers

A real `x` with a negative margin (interior dips are where it would
hide — the mesh analysis targets exactly those); failure of the `E`-bound
or of the `ζ'(1/2)` identification; instability of the `e* = 1110`
threshold (would contradict the exact rational prefix inequalities);
re-adjudication of the aggregate contract; greedy-vs-LP discrepancy on
frozen fibres.
