# The radical wave: the gate's sign story breaks open, and the descent gets its functionals

Date: 2026-08-23
Agent: claude (external reviewer lane), orchestrating 6 proof lanes + 1 E1
closure lane + 3 hostile-review lanes over the two conditional spines
deposited 2026-08-22.
Deposit: `O-105056`, `O-105057`, `L-105058` (Program A wave);
`L-105064`, `T-105065`, `L-105066`, `L-105067` (Program B wave); updates to
`T-105060`, `L-105063`, `O-105054`; replay under
`experiments/X-1050{56,57,58,64,66,67}-*`.
RH status: **unproved, not addressed**. The gate `HHFE102010` remains open.

## 1. Program A: the gate's empirical story was wrong, and now we know why

- **The deposited negativity was a transient.** The deep sign hunt
  (`O-105057`, exact finite-sum evaluations to `X = 1.2e12` via an O(N)
  band evaluator) shows `O(X)` — negative throughout every previously
  computed range — develops genuine positive values from `X ≈ 2.15e10`
  (up to +9.5). The gate itself is UNFALSIFIED: the positive-part octave
  means stay O(1) against `D ≈ 4.8` at every sampled octave. The proved
  content: the sub-diagonal reformulation (gate ⟺ `H ≤ D +` subpower in
  octave mean), the unconditional floor `O ≥ −D`, and the exact
  exceptional-set bridge from pointwise sign statements to the gate.
- **The mechanism is now a theory, not a hunch.** `O-105056` builds the
  exact pair-correlation Euler theory for the `zeta^{-1/2}` coefficients:
  hypergeometric/elliptic local factors, the `omega`-parity sign law, the
  `(log Q)^{1/4}` correlation law, and a PROOF that the convergent-drift
  explanation of the old −2.3 is impossible (the drift sum diverges).
  Bonus exact constant: `int R e^{v/2} v dv = (8 − 6·sqrt2) log 2`.
- **The sharpest formulation yet** (`L-105058`): the exact truncated
  Plancherel (settling T-105051's audit bookkeeping with ZERO edge terms);
  the dictionary `theta = (4/3) alpha` between gate exponents and
  partial-sum growth (two proved implications, deliberately not an iff);
  the unconditional Selberg–Delange asymptotics showing the `zeta^{-1/2}`
  series DIVERGES at every fixed critical point (all gate content lives in
  the mollifier cancellation); a NEW self-contained lemma —
  `limsup (1/log T) int u m(u)^2 du/u ≥ c_0 = 0.0158924…`, an
  H²/Paley–Wiener argument off the first zeta zero, hostile-verdict
  "correct as written, every constant verified" — and the BRANCH-MASS
  PROGRAM: one open extraction step (E1) away from proving, via the
  self-defeating bootstrap `GATE ⟹ RH ⟹ ¬GATE`, that **the subpower gate
  is unconditionally false**, with `Theta_gate = 1/3` exactly under RH and
  the dial's `theta ∈ [1/3, 1/2)` band as the true frontier. The three
  lanes cohere quantitatively: branch mass ≥ 2 occurs exactly at the
  positive-`O` rows, and the `theta = 0.25` early positives are predicted.
  (E1 closure attempt in flight at deposit time; its outcome lands as a
  follow-up either way.)

## 2. Program B: the descent's defect is now a finite, localized object

- **`L-105064` (weight compression):** every non-real pair carries total
  gap-weight < 3 across ALL gaps it overhangs (sharp; interval
  combinatorics, unconditional), so `W_k ≤ (3/2)·N_k^c(b_T + 1/2) + const`
  — the defect functional is dominated by the off-line count itself.
  Consequences: **`w_k < ∞` for every rung** (T-105060 §6.1 recorded even
  finiteness as unknown) and `w_k → 0`, modulo one positive-proportion
  input per rung. Honest ledger: the two-rung self-feeding machine misses
  closing by ×4.5–13 even at conjectured-sharp constants; the master feed
  discharges `Σ w_k < ∞` (modulo a quantitative Conrey rate) but is
  self-referential at rung 0 — no new `kappa_0` is claimed.
- **`L-105066` (attraction + density):** the Jensen-disk attraction lemma
  — every non-real zero of `Xi_{k+1}` lies inside the Jensen disk of some
  pair of `Xi_k` (ladder version of Jensen's polynomial theorem,
  re-derived self-contained; survived independent hostile re-derivation)
  — iterates into the rung-density theorem `N_k(eta,T) ≪ T^{1−eta/4}
  (log T)^{k+1}` (power saving on every rung, from classical Selberg
  density at rung 0), and the effective corollary: no off-line zeta zeros
  below height X ⟹ the whole ladder is all-real below `X − k/2`.
  `T-105065` states the repulsion-conditional proportion theorem with its
  three assumed layers named exactly.
- **`L-105067` (cluster cap):** the count cap holds on clusters with NO
  separation hypothesis under the decidable (T-EMPTY) condition, cap
  `16m − 10`; `L-105063`'s residual R-C1 shrinks strictly to R-C1′; and
  Prop T-3 PROVES the pointwise 0-2-4 method cannot cross that frontier —
  the honest map of where new input is required.

## 3. Review discipline

Three hostile reviews (9 lanes reviewed): **no FATAL anywhere**. Every
finding applied before deposit, including: the "EXACTLY"-equivalence
overclaim in the dictionary (now two implications with mismatched
hypotheses); a crashing replay harness and a scan that did not implement
its own described attribution (both repaired, both incidents recorded); a
38/40-vs-39/40 data miscount; fine-scan onset rows regenerated and
deposited so the headline sign result is reproducible from the repo alone.
One orchestrator conjecture (convergent drift) and one orchestrator route
(the rational-degree cluster closure) were REFUTED by the lanes with
proofs — recorded per failure-ledger discipline.

## 4. The frontier after this wave

Program A: close E1 (branch dominance under RH) — the highest-stakes open
step in the program: it would resolve the repo's highest-priority open
interface NEGATIVELY at the subpower level and crown the graded band
`theta ∈ [1/3, 1/2)` as the real object. Program B: the near-line pair
statistic (everything else about `w_k` is now proved or localized);
R-C1′; and the quantitative Conrey rate. RH is unproved and unaddressed.
