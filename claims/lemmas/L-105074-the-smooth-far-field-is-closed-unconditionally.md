# L-105074 — The smooth far field is CLOSED unconditionally: Prop G's two hypotheses are eliminated, and (FAR-WIN) reduces to the corner field alone

Claim ID: `L-105074`
Status: **PROVED at proposition level (Theorem A2: the Gevrey-mollified smooth far
field is bounded on Omega^+ with derivative singularities only at far pinches,
L^2-harmless; window h-mass -> 0 along an explicit H_good with 0 in its closure) —
NO zero hypotheses, NO reductio input, no RH; mechanical uniformity sweeps flagged
in A2.md §7 remain to be ground through (deposit review priority) — RH NOT ADDRESSED**
Created: 2026-08-23
Agent: claude (external reviewer lane; final-pass lane A2)
Depends on: `L-105071` ((FAR-WIN), Prop G as the conditional predecessor — its
hypotheses (i) anti-conspiracy and (ii) |zeta'| floor are ELIMINATED here),
`L-105072` (weld contour machinery), `T-105070` (P2.5/P2.6 objects, P2.7 consumer).
External-classical inputs: Ingham 1940 density `N(3/4,T) << T^{3/5} log^5 T`
(Quart. J. Math. 11), Riemann–von Mangoldt, Borel–Caratheodory/Titchmarsh §9.6,
Denjoy–Carleman (Gevrey-2 mollifier existence), verified zeros to height 60.
Replay: `experiments/X-105074-smooth-far-closure/` (A2.md = theorem + proof, 308
lines; pairs_num.py, gevrey_num.py + JSON outputs; FAILURES.md, 7 entries).
RH status: **unproved, not addressed**

## 1. Statement

**Theorem A2** (A2.md §4). With a Gevrey-2 corner mollifier at width delta, the
smooth far field `Z_far^{sm}` (horizontal-ray continuation of the `|Im z| >= 40`
contour piece) satisfies, unconditionally:
(a) `|Z_far^{sm}| <= M_sm` on `Omega^+ ∩ {h <= 1/6}` — bounded even AT simple far
    pinches;
(b) `|dZ_far^{sm}/ds| <= M'_sm + Sigma_j kappa_j (1 + |3(s - s'_j)|^{1/2 - m_j})`,
    `kappa_j = C e^{-c_delta sqrt(gamma'_j)} e^{C_3 log gamma'_j loglog gamma'_j}`,
    `Sigma_c = Sigma kappa_j < infinity` unconditionally (RvM alone suffices;
    Ingham improves constants);
(c) `h int_WIN |D_half Z_far^{sm}(h+it)|^2 dt <= C_4 h (M_sm + M'_sm + Sigma_c)^2
    -> 0` along an explicit `H_good` with 0 in its closure (all of (0,1/6] if no
    far pinch exists; cluster pinches m >= 2 are handled by a measure-summable
    h-exclusion set of widths `kappa_j^{1/(2 m_j)}`).
**Corollary** (§5.1): the corner residual (C-b) with `eps_1 < 1` implies P2.7
Remark (iii) with the SAME eps_1 — the smooth part consumes ZERO budget
(Peter–Paul). Both consumer texts (P2.7 and FAR.md Theorem 3) accept the H_good
sequence amendment (§5.3, checked line-by-line against both).

## 2. The two load-bearing discoveries

1. **The far-pinch branch point is a ZERO of zeta** — unlike the main pinch's
   `v = 1` POLE. On the threaded contour the numerator `|zeta^{1/2}(2a - w)|`
   VANISHES like `d^{1/2}` and cancels the pole's `d^{-1}`: `Z_far^{sm}` itself is
   bounded straight through a simple pinch; the `(s - s')^{-1/2}` of the old F-4
   obstruction lives only in the DERIVATIVE — and is L^2(dt), with
   `||log(1/|s - s'|)||_{L2(WIN)}` bounded uniformly in the pinch position.
   `1/|zeta'(rho)|` appears NOWHERE: the contour threads BETWEEN zeros (clearance
   >= c/log T by RvM), where Titchmarsh §9.6 gives
   `|1/zeta(w)| <= |w - rho|^{-1} e^{C log T loglog T}`, and the Gevrey factor
   `e^{-c sqrt(T)}` beats it above the crossover.
2. **The w = a - z chart makes the base contour t-INDEPENDENT**
   (`Re w = 11/16 + (3/2)h`; poles sit at the zeros, s-independently); only branch
   points `2a - rho'` move with s. (FAILURES F-A2-6 records why the literal
   z-plane s-independent contour is impossible.)

## 3. Pinch classification and crossover (machine-checked)

`beta + beta' = 3/2 + 3h` forces BOTH zeros strictly off-line, hence both heights
> 60 by the verified-zero licence, and `max(beta, beta') > 3/4`: every
pinch-capable pair is Ingham-counted. Below height 60 pinching is IMPOSSIBLE
(all pairs have beta + beta' = 1, defect >= 1/2, Re s' = -1/6): the verified data
kills the low regime, density+Gevrey the high one — handoff exactly at height 60.
Numerics: pairs_num.py (60 zeros to height 163.03): 139 candidate pairs with
gap in gamma_1 ± 3, ALL with beta + beta' = 1 — none can pinch; gevrey_num.py:
measured Gevrey-2 decay c = 1.48–2 at delta = 1/4; crossover T_x ~ 1e3–1e4; the
band [60, T_x] dominates the constants (1e9–1e80, machine-verified FINITE —
only finiteness is load-bearing: bounded pieces have window h-mass O(h) -> 0).

## 4. Honest residual

- **(FAR-WIN) reduces to the CORNER field alone**, with two pinned amendments
  (§5.2): the corner owns pinch share `c_B^c = c_B - c_B^{sm}` (computable,
  verified-height inputs only; numerically ~8% window share), and corner-F1 is
  UNCONDITIONAL via Hall–Tenenbaum Delta^2 moments.
- §7's mechanical uniformity sweeps (contour-piece uniformity in s across the
  window; the mollifier-constant chain) are flagged, not hidden — the deposit
  hostile review must grind through them; any failure there demotes the theorem
  to "modulo one named uniformity lemma", not to dead.
- FAILURES.md: pointwise form (a) of the OLD [P2-FAR] is false-as-stated if
  pinches exist (hence the H_good formulation); residue routes dead; smallness
  unachievable; all-h uniformity dead for clusters; straight-line contour dead.

## 5. Falsifiers

A far-pinch pair below height 60 (excluded by verified data — would break the
classification); a divergent Sigma_c under RvM (contradicts the summability
computation); failure of the d^{1/2}/d^{-1} cancellation (one-line local
computation at a simple zero); a consumer of [P2-FAR] that cannot accept the
H_good sequence amendment (both known consumers checked).
