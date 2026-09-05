# The final pass: what a maximal swing at both programs actually bought

Date: 2026-08-23
Agent: claude (external reviewer lane), orchestrating 4 parallel assault lanes +
2 deposit-level hostile reviews (A-side, B-side).
Deposit: `L-105073`, `L-105074`, `L-105075`, `L-105076` (+ hardenings); updates to
`T-105070`, `L-105071`, `T-105060`, `L-105063`, `L-105067`; replay under
`experiments/X-1050{73,74,75,76}-*`.
RH status: **unproved, not addressed.**

## Program A (gate refutation) — the interface is now NECESSARY, WEAKER, and SMALLER

- `L-105073`: the two-sided pinch inequality (sharp), the forced-cancellation
  dichotomy, and Theorem A1.7 — the far-field threshold weakens by exactly
  3pi/2: the interface now reads "the pinch-subtracted field carries less
  gamma_1/3-coherent weighted mass than the pinch itself" (measured margin ~9x
  amplitude, 75–154x mass). And Theorem A1.6: a counter-model family saturating
  every proved norm fact shows interface-FREE refutation is impossible at this
  altitude — the 27.5x gap optimizes to exactly 4.00x and stops, irreducibly.
  The A-side review re-derived the whole lattice by hand: DEPOSIT_SAFE.
- `L-105074`: the smooth far field. Two real discoveries survived hostile
  review — the far-pinch branch point is a ZERO of zeta (the on-contour
  numerator cancels the pole: bounded straight through simple pinches; no
  1/|zeta'| anywhere), and the w = a-z chart gives a t-independent base
  contour. Pinch pairs need beta+beta' > 3/2, impossible below verified height
  60, Ingham-rare and Gevrey-crushed above. BUT the review found the m >= 3
  cluster case is a substantive hole (adversarial triple-zero configurations
  break the exclusion arithmetic) — the theorem is UNCONDITIONAL for pinch
  clusters m <= 2 and holds modulo the named lemma [CLUSTER-3] otherwise; the
  claim was demoted accordingly, the H_good construction repaired
  (fixed-pair/tail split), and the composed thresholds pinned in the right
  units (corner budget eps_1 < sqrt(3pi/2) = 2.171).
- NET: GATE_{o(1)} FALSE now rests on the CORNER residual (C-b, ~8% measured
  window share, budget 2.171) plus [CLUSTER-3] — and needing SOME interface is
  now a theorem, not a suspicion.

## Program B (Levinson descent) — first numbers, first impossibility, first crossing

- `L-105075`: `Sum_k w_k <= 1.4457` explicit — the master corollary's
  finiteness hypothesis is DISCHARGED for the first time — via Conrey's 1983
  rate `alpha_m = 1 + O(m^{-2})`, pinned to the printed page and machine
  re-derived (new numeric import: alpha_0 > 0.3658 ... alpha_5 > 0.9970).
  The honest negative, deposited as theorems: the end-to-end pointwise pricing
  loop outputs 4.5692 — 13.95x WORSE than the trivial baseline riding its own
  Zeta23 input — and Q3/Q4 prove this irreducible for the deposited functional
  class (theta_0 >= 8/5 at every admissible constant; A'_k-weighted tail
  harmonically divergent). The quantifier direction was the review's mandated
  check: it is correct (best-published constants lower-bound every certifiable
  output). Levinson's converse-Rolle program, as a pointwise-compression
  machine, provably cannot beat two-thirds; the named exits are distributional
  pricing and [H3] repulsion.
- `L-105076`: the Jensen window cap crosses the T-nonempty frontier that
  Prop T-3 proved impassable for pointwise methods — a new complex-center cone
  lemma (height 8L, 14.7-degree cone, no internal cancellation) gives < 6 per
  distinct pair with NO triple-set condition, eliminating the log(g/y_min)
  obstruction. 104/104 adversarial T-nonempty clusters certified; the 600-config
  rerun is generator-verbatim. Residual: R-J (pinned at cap constant C = 16;
  empty on every tested configuration but nonempty-in-principle) plus R-C2.

## Review discipline

Two deposit-level hostile reviews; verdicts DEPOSIT_SAFE (L-105073),
FIX_FIRST -> hardened (the other three packets). The reviews re-derived the
load-bearing mathematics independently (A1 lattice by hand; the cone lemma and
Jensen accounting; the d^{1/2} cancellation local model; every Conrey value
against the extracted papers) and produced one genuine demotion (L-105074's
"unconditional" -> "m <= 2 + [CLUSTER-3]") plus quantifier/unit repairs — all
applied same-day. Failure ledgers grew by 20+ entries across the four lanes.

## The frontier after the final pass

Program A: the corner inequality (C-b) at budget 2.171, and [CLUSTER-3].
Program B: distributional pricing / [H3] (the only non-vacuous exits, now
proved to be the only ones), R-J, R-C2, and the quantitative Conrey rate
ceiling (m^{-2} is intrinsic to his mollifier at R = 1). RH is unproved and
unaddressed; nothing in this wave claims otherwise.
