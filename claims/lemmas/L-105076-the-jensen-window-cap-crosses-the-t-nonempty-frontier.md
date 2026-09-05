# L-105076 — The Jensen window cap: < 6 per distinct pair on T-nonempty clusters, crossing the frontier Prop T-3 proved impassable for pointwise methods

Claim ID: `L-105076`
Status: **PROVED (cone Lemma B2.1; Theorem B2 window cap with explicit constants,
under the stated window admissibility + (DOM) mass-dominance hypothesis; the
log(g/y_min) obstruction of R-C1 is ELIMINATED) — R-C1' NOT closed unconditionally:
it shrinks to R-J ⊊ R-C1' (stopping-recursion failures; empty on all 104 adversarial
T-nonempty clusters tested) — RH NOT ADDRESSED**
Created: 2026-08-23
Agent: claude (external reviewer lane; final-pass lane B2)
Depends on: `L-105067` (cluster cap under T-EMPTY; Prop T-3 frontier proof — this
lemma crosses that frontier with a DIFFERENT method), `L-105066` (Jensen-disk
attraction), `L-105063` (regimes; [THRESHOLD]), `L-105061` ([I-PF]).
Replay: `experiments/X-105076-jensen-window-cap/` (B2.md = setup, cone lemma with
proof, Theorem B2 with full proof, stopping recursion, residual R-J, verification
tables; jensen_constants.py — 40-dps replay of every constant; disk_check.py +
disk_check_out.txt; FAILURES.md, 7 entries).
RH status: **unproved, not addressed**

## 1. Statement

Setting of L-105061/L-105067 (F = Xi_k, gap G, h' = (F'/F)'). For any admissible
window (c, L, S) — S = all zeros of F in D(c + 8iL, 19.79 L), horizontal offsets
<= L, pair heights <= L/4 — satisfying **(DOM)** (outside inverse-square mass
<= 0.0070 N_S / L^2):

**Theorem B2.** Jensen on `D(c + 8iL, rho = 8.246 L) ⊂ D(·, R = 2.4 rho)` applied
to `g = h' · prod_pairs q_j^2 · prod_reals (t - t_n)^2` gives

    Z_mult(h', K_span ∩ G) <= 5.813 p_S + 2.850 nu_S + 0.839

(p_S = distinct pairs, nu_S = distinct real zeros in S; multiplicities FREE — pole
orders are 2 regardless). **The theorem never references T_K**: it applies with no
triple-set condition, i.e. it crosses exactly the frontier `L-105067` Prop T-3
proved impassable for the pointwise 0-2-4 method. For m_K = 1 it reproduces
LEMMA A's constant 6 (floor 6.65).

**Cone Lemma B2.1 (the new tool).** At height 8L above the cluster every S-term of
`-h' = Sum m_w (t - w)^{-2}` lies in a 14.7-degree cone, so
`|h'(t*)| >= 0.0140 N_S / L^2 - background` with NO possible internal cancellation;
(DOM) guards the background. The complex center is what kills the log: the recorded
R-C1 obstruction — the unabsorbable `log(g/y_min)` — is eliminated; NOTHING in the
bound scales with any scale ratio (verified with y spanning 1e-4 g to 0.49 g inside
single windows).

The tasked per-y-scale Whitney telescoping DEGENERATES (FAILURES F2) — honest
record: executing it collapsed to the single complex-center disk, which is strictly
stronger; the telescoping survives only as the position-space STOPPING RECURSION
(inflate the window until (DOM) or exhaustion; each swallowed zero pays O(1) and
raises N_S).

## 2. Verification (disk_check.py; 40-dps constants in jensen_constants.py)

(a) Every L-105067 §3(b) family certifying T_K != EMPTY — equal-scale mult-ratio,
unit-mult edge injector, 13-unit-pair cluster — at g = 8/32/128 plus an
endpoint-hugging variant: **13/13 certified, cone floor never fails**, true Z = 2
always; at m = 13 the bound is 82.1 vs T-1's 16m - 10 = 198.
(b) Rerun of the X-105067 600-config generator: 1062 clusters, **91/91 T-nonempty
clusters certified, 0 violations** (971 T-empty also clean); bound/M_K min 1.66,
median 6.65, max 49.97.
Constants replayed: 5.81288, 2.84991, 0.83845, theta_bg = 0.0070027,
cone cos = 0.96724667. (Review K7: last-digit drift across files — all values
round safely UP to the quoted 5.813 / 2.850 / 0.839; theta_bg's drift is in
the safe direction.)

## 3. Honest residual

- **R-J ⊊ R-C1'**: clusters whose stopping recursion cannot reach (DOM) at cost
  O(W(G)) — concretely gap-scale clusters (span >~ 0.08 sqrt(M) · clearance) in
  zero-dense neighborhoods, and clusters forced to swallow shallow pairs of weight
  << 1 at cost 5.813 each. EMPTY on all 104 adversarial T-nonempty clusters
  tested; the reachable troubles are catalogued (FAILURES F4/F5 — the
  uniform-field annulus race is won 5.5x at H = 8 for non-increasing density,
  unproved for superpolynomially growing fields).
- **R-C2** (supercritical shallow mass): untouched.
- Consequence for `T-105060` (with the qualifier B2.md §5 carries — review
  correction K2): the count cap is now proved on separated regimes (L-105063),
  T-EMPTY clusters (L-105067), AND clusters admitting stopped windows WHOSE
  certified bound satisfies `5.813 p_S + 2.850 nu_S + 0.839 <= C·W(G)` with the
  cap constant PINNED at `C = 16` (matching L-105067's cap scale; on the 104
  tested adversarial clusters the ratio bound/M_K had median 6.65, max 49.97 —
  the max exceeding 16 means some tested windows certify only at larger C, so
  R-J is defined RELATIVE to C = 16 and is nonempty-in-principle at that
  pinning even where the recursion stops). Conditionality confined to
  (R-J at C = 16) ∪ (R-C2).
- Refuted routes on record: real-center Jensen (both logs isolated — refuted),
  per-y-scale Whitney telescoping (degenerate), pole-centered Jensen (log returns
  via pair separations), H = 4 cone (loses the annulus race), unconditional
  stopping termination (believed FALSE in the abstract class — stated).

## 4. Falsifiers

An admissible window with (DOM) violating the cap (exact arithmetic, check
confinement first); a T-nonempty cluster from the §3(b) families or the 600-config
generator violating certification (would contradict 104/104); an error in the cone
angle or theta_bg (independently re-derivable, closed forms in
jensen_constants.py); a proof that R-J is nonempty on a positive-proportion set of
gaps (would restore R-C1'-scale conditionality — the honest risk).
