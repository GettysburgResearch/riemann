# The Levinson descent ladder: converse Rolle made quantitative, with the defect isolated and priced

Date: 2026-08-22
Agent: claude (external reviewer lane), orchestrating 4 proof/census lanes +
2 recovery lanes for Program B.
Deposit: `T-105060`, `L-105061`, `L-105062`; replay under
`experiments/X-105060-descent-ladder/` and
`experiments/X-105061-xi-derivative-census/`.
RH status: **unproved, not addressed**.

## 1. The idea

Levinson's unfinished program: a "converse to Rolle" pulling on-line zero
proportions DOWN the ξ-derivative ladder (ξ‴ → ξ″ → ξ′ → ξ). The forward
direction is trivial; the converse is false generically but true at the 100%
level for ξ-like rigidity classes (Hellerstein–Williamson; Sheil-Small; Bergweiler–
Eremenko–Langley), and nobody has ever produced the quantitative version. This
deposit produces it — as a conditional theorem whose single open input is one
per-gap geometric lemma, with everything else proved:

- **L-105062 (PROVED)**: every rung Ξ_k keeps its zeros in the strip
  |Im t| ≤ 1/2 (Gauss–Lucas through the genus-0 square-variable Hadamard
  product); total zero counts are ladder-invariant to O_k(log T) with explicit
  constants (Riemann–von Mangoldt on every rung); Rolle floor with
  multiplicity; and the **monotone ladder**: the asymptotic on-line proportion
  never decreases under differentiation. Corollary (consuming the repo's
  Z23-UPSTREAM import row): **at least 67.25% of the zeros of EVERY derivative
  ξ^(k) are distinct points on the critical line** — status inherited from the
  import row (repo-side exact-SHA review pending; the ladder transfer itself
  is unconditional) — the imported baseline rides the ladder to every rung.
- **L-105061 (interface)**: the exact partial-fraction layer
  (Ξ_{k+1}/Ξ_k)′ = −Σ m_n/(t−t_n)² + Σ φ′_j — PROVED; the **threshold lemma**
  — any gap holding an extra critical zero has overhanging close-pair weight
  ≥ 1 — PROVED; the per-gap **count cap** (extra(G) ≤ A′·weight, pinned
  A′ = 4, empirical sharp constant 2) — OPEN, with a recorded obstruction
  ledger (monotone-run counting is false; second-Rolle regress does not
  terminate; Jensen disks over-charge tiny pairs) and 260+ exact-arithmetic
  configurations with zero violations.
- **T-105060 (CONDITIONAL on the count cap)**: the priced converse Rolle
  N_{k+1}^r ≤ N_k^r + 1 + A′·W_k; the descent inequality
  N_k^c ≤ N_{k+1}^c + A′·W_k + O_k(log T); and the **master corollary**
  (adding only Conrey 1983's κ_k → 1 as external classical input):

      1 − κ_0 ≤ A′ · Σ_{k≥0} w_k

  — the off-line proportion of zeta zeros is bounded by the total weighted
  close-pair density along the ξ-derivative ladder. RH ⟹ every W_k ≡ 0
  (Laguerre–Pólya closure), so the inequality is exactly the quantitative
  shadow of the LP rigidity. If Σw_k < ∞ were ever proved, (d) becomes a new
  proportion theorem; that is the isolated successor problem.

## 2. The census (unconditional, budgeted-mp, T₀ = 500)

`X-105061`: all real zeros of Ξ, Ξ′, Ξ″, Ξ‴ on [0, 500] located and
sign-certified at dps 35 with explicit error budgets (tightest margin 2.3e21×
budget; near-region monotonicity certificates ≥ 39.7×; fail-closed replay
`verify.py` → ALL PASS): counts **269 / 269 / 270 / 269**, and the defect
ledger **X₀ = X₁ = X₂ = 0** — every gap of Ξ_k contains EXACTLY one zero of
Ξ_{k+1}. To height 500 the converse Rolle holds with zero defect; the ladder
is perfectly rigid as far as certified computation can see. R₀(500) = 269
matches a recount by an independent counting method (mpmath nzeros,
Turing/Backlund argument principle — same underlying zeta implementation as
the evaluator); per-zero agreement with the
classical table is ≤ 1.3e-15. Honest arithmetic model: budgeted
multiprecision, not an interval library; one correction recorded (bracket
width target 1e-20 unreachable at t ~ 500; certified widths ≤ 2.7e-14).

## 3. Process incidents (recorded per failure-ledger discipline)

Two dedicated proof lanes on the count cap terminated by exceeding the
per-response output ceiling mid-derivation — the lemma reliably provokes
unbounded single-pass derivations. The interface is deposited honestly OPEN
with its proved halves and obstruction map; the next attempt is decomposed
(single-pair case → bounded cooperation → assembly) precisely to avoid this
failure mode. A third structured attempt is being dispatched.

## 4. Relation to the rest of the program

Program A (same-day deposit `T-105050`..`M-105055`) compressed the transport
program's open core into one gate with a graded dial; Program B here gives the
zero-side mirror: a second, logically independent conditional spine whose open
core is one finite-geometry lemma plus one density functional. The two
programs share no repo-internal inputs (both consume classical zero-free-region
facts) — a deliberate portfolio split. Nothing
in either addresses RH.

## 5. Addendum (2026-08-23): the count cap closes on the separated regimes

The third, decomposed attempt on the count cap succeeded where two monolithic
attempts had died: `L-105063` proves `extra(G) ≤ 6·W(G)` for every gap in the
regimes {no overhang; isolated site; deep pairs with disjoint (2+√3)-fattened
intervals + subcritical shallow mass; all-shallow ladder}, by level-2
confinement to the deep sites plus a per-site convex-comparison/concavity-split
argument with exact constants (κ = (11+5√5)/64, κ₆ = 1). The extremal
in-regime configuration realizes extra/W = 16/15 (so the linear-in-W cap is
the correct shape; any valid constant ≥ 16/15, conjectured sharp value 2,
proved 6). `T-105060`'s conditionality is now confined to two precisely-
described residual regimes — deep clusters and supercritical shallow mass —
both numerically tame (never more than 2 extra zeros per deep site in 600
residual scans). RH remains unproved and unaddressed.
