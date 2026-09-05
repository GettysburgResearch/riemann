# L-105073 — The pinch dichotomy: the far-field interface weakens by 3pi/2, and interface-free refutation is IMPOSSIBLE for norm methods (counter-model theorem)

Claim ID: `L-105073`
Status: **PROVED (Theorems A1.3 two-sided pinch inequality — sharp; A1.4 forced
cancellation quantified; A1.6 norm-method obstruction with machine-checked extremal
saturation; A1.7 sharpened reduction — the main deliverable) — the interface-free
closure of T-105070 is NOT PROVED and is PROVED UNREACHABLE at this altitude — RH NOT
ADDRESSED**
Created: 2026-08-23
Agent: claude (external reviewer lane; final-pass lane A1)
Depends on: `T-105070` (P2.7(1)-(4)), `L-105072` (amended [P1-LOC], consumption (e)),
`L-105071` ((FAR-WIN) and the reduction), `L-105058` §5.
Replay: `experiments/X-105073-pinch-dichotomy/` (A1.md = lattice + proofs + gap
accounting; a1_verify.py, a1_opt.py + JSON outputs; FAILURES.md F-A1-1..6).
RH status: **unproved, not addressed**

## 1. Statement

Notation: under the reductio R (A := limsup Q_V/log Y <= c_0' - eps), p := |c_B|,
`p_h^2 := (2/pi) arctan(r_0/h) p^2` (the EXACT pole window mass), and
`f_h^2 := h int_WIN |D_half[Z_far](h+it)|^2 dt`.

**Theorem A1.3 (two-sided pinch inequality; sharp).** Under R, for every A' in (A, c_0'):
`| f_h - p_h | <= p sqrt(A'/c_0') + o(1)` for all small h. (Conjugate symmetry halves
the line budget to (3pi/4)A' per window; expand the square, never the triangle.) Both
endpoints are attained by norm-consistent configurations.

**Theorem A1.7 (sharpened reduction — supersedes P2.7 Rem (iii)'s threshold).** For any
beta < 1: if `limsup_h f_h^2 <= beta^2 |c_B|^2`, then TARGET(V) holds with constant
`(1-beta)^2 c_0'`. The interface threshold weakens from `0.2122|c_B|^2` to `|c_B|^2` —
by EXACTLY `3pi/2 = 4.7124` — and composed with L-105071, (FAR-WIN) with any
`eps_1 < sqrt(3pi) = 3.070` now suffices. The remaining interface reads: **"the
pinch-subtracted field carries strictly less gamma_1/3-coherent weighted mass than the
pinch itself."** Unconditional dichotomy display: `A >= c_0' (1 - f-bar/|c_B|)_+^2`.
Measured margin under the new threshold: beta = 0.081–0.115 (~9x in amplitude,
75–154x in mass); worst-case retained constant 0.783 c_0' vs the old chain's 0.562 c_0'.

**Theorem A1.4 (forced cancellation).** Under R(eps) the far field's coherent
amplitude alpha_h against the arctan pole profile satisfies
`Re alpha_h <= -(f_h^2 + (3pi/4)eps)/(2 p_h) + o(1)` and
`|alpha_h| >= p (1 - sqrt(1 - eps/c_0')) - o(1)` — anti-phase, pole-profile, at every
scale.

**Theorem A1.6 (the obstruction).** The one-parameter family `psi^theta = theta·(pinch)`,
`theta in [-sqrt(1-eps/c_0'), sqrt(1-eps/c_0')]`, satisfies EVERY proved norm fact of
the program (SCOPE, review J5: "norm fact" means EXACTLY the enumerated list —
Q-budget with `A = theta^2 c_0'`, Plancherel, conjugate symmetry, the genuine pole
expansion, sharp F1 — equality machine-checked at extremal theta — and F2–F5; the
boundary is defined in FAILURES F-A1-5: arithmetic double-Dirichlet structure,
positivity, and cross-line rigidity are NOT norm facts, and A1.6 says nothing against
closures consuming them), while its far mass sweeps `[p^2(1-sqrt(1-eps/c_0'))^2, C(eps)]` with
`C(eps) = p^2 (1+sqrt(1-eps/c_0'))^2 <= 4p^2`. Hence NO interface-free refutation
exists at this altitude, for ANY eps: the ceiling-vs-threshold gap is exactly **4.00x
(down from 27.5x) and provably irreducible below 1 by norm-inequality methods** (it
shrinks to 1 as eps -> c_0' without the constraint set ever emptying). The
second-generation pinch bootstrap terminates at depth 1, consistent — it closes for
NO eps (FAILURES F-A1-3).

## 2. Proof

`experiments/X-105073-pinch-dichotomy/A1.md` (lattice A1.1–A1.7, full proofs, §8 gap
accounting). Dead routes recorded: interface-free Direction-1 closure (F-A1-1, with
proof), the line-budget attack both ways including the O(sqrt(log 1/h))
correlation-leakage technicality (F-A1-2), bootstrap (F-A1-3), finite-h arctan
(F-A1-4); F-A1-5 states the scope boundary — what any future closure must consume
beyond norms (phase/arithmetic input, exactly (FAR-WIN)-type); F-A1-6 records a
caught script sign-slip.

## 3. Verification

`a1_verify.py` (mpmath dps 30): `(3pi/4) c_0' = p^2` EXACT (residual 0.0); old gap
27.4658; arctan pole-mass quadrature vs closed form < 1e-30; A1.3 root formulas
< 1e-33; model saturation identities < 1e-30 at 5 eps values; pinch line-mass
constant ratios 1.0027/0.9984; `3pi/2 = 4.71239`, `sqrt(3pi) = 3.06998`.
`a1_opt.py`: extremal feasibility — sup/inf of f over the norm constraint set match
`p(1 ± sqrt(1-eps/c_0'))` to ~1e-6 at 5 eps values.

## 4. Honest residual

T-105070's refutation NEEDS an interface — now a theorem (A1.6), not a suspicion.
The needed interface is 4.71x weaker than before (A1.7) and its measured margin is
~9x in amplitude; but it is not, and cannot be by these methods, removed. New input
must carry phase/arithmetic information about the gamma_1/3-coherent component —
exactly the (FAR-WIN) class.

## 5. Falsifiers

A norm-consistent configuration violating A1.3's endpoints (kills sharpness); an
interface-free refutation proof using only the A1.6-listed facts (would contradict
the counter-model — check it against psi^theta first); an error in the exact
identity `(3pi/4) c_0' = |c_B|^2` (one-line check from c_0' = (4/(3pi))|c_B|^2).
