# L-105066 — Jensen-disk attraction on the ξ-derivative ladder: non-real derivative zeros are confined to pair disks, and off-line density is o(T) on every rung

Claim ID: `L-105066`
Status: **Lemma D1 + Theorems D2, D5 PROVED (self-contained modulo L-105062 §1 and L-105062 §2.3's Jensen window count); Theorem D3 and Lemma D5.0's input PROVED MODULO EXTERNAL-CLASSICAL density/gap inputs (Selberg 1946 or Carlson 1920; Hardy–Littlewood 1921), transcribed literature-unverified in-container — RH NOT ADDRESSED**
Created: 2026-08-23
Agent: claude (lane D, Program B2 descent program)
Depends on: `L-105062` §1 (square-variable genus-0 Hadamard product), §2.3 (Fact-J unit-window count), Thm 3 (Rolle floor, for gap-doubling and for strict positivity via Hardy); `L-105061` Lemma 2.1 (proof template for the complex partial-fraction layer). Consumed by: `T-105060` successors, `T-105065` (draft).
Replay: `GRAND/progB2/laneD/` — DERIVATION.md (full proofs), test_attraction.py (400 + 150 polynomial-ladder configs, 0 violations; disk-occupancy max 4), test_t3_mp.py (Xi-like truncated product + planted pair, 60 dps, 0 violations), test_gapdouble.py (3021 intervals, 0 violations).
RH status: **unproved, not addressed**

## 1. Statements

Setting of L-105062 §0. Pairs of `Xi_k`: non-real conjugate zero pairs
`(x_j ± i y_j)`, `0 < y_j <= 1/2`. `D_j` := open disk of radius `y_j` centered
at `(x_j, 0)`. `N_k(eta, T)` := #{zeros of `Xi_k`: `Im t >= eta`,
`0 < Re t <= T`, mult}.

**(D1) [ATTRACTION / JENSEN-DISK CONFINEMENT].** Every non-real zero `w` of
`Xi_{k+1}` either satisfies `Xi_k(w) = 0` (a non-real zero of `Xi_k` at the
same point, multiplicity dropping by one), or lies in the OPEN Jensen disk
`D_j` of some pair of `Xi_k`; in particular `y_j > |Im w|` and
`|x_j - Re w| < y_j <= 1/2`. (Polynomial ancestor: Jensen's theorem
[Jensen 1913 / Walsh 1920], re-proved here for the ladder class from the
genus-0 product — no literature input consumed.)

**(D2) [ONE-RUNG DENSITY TRANSFER].** For every `k` there is `C_k` with
`N_{k+1}(eta, T) <= N_k(eta, T) + C_k log(T+3) (N_k(eta, T+1) + 1)` for all
`T >= 1`, uniformly in `eta in (0, 1/2]`.

**(D3) [o(T) DENSITY ON EVERY RUNG].** With EXTERNAL-CLASSICAL zero-density
(Selberg 1946: `N(sigma,T) << T^{1-(sigma-1/2)/4} log T`; Carlson 1920
suffices too) and the coordinate identity `N_0(eta, T) = N(1/2 + eta, T)`:
for every fixed `k`, `eta`:
`N_k(eta, T) <<_{k,eta} T^{1 - eta/4} (log T)^{k+1} = o(T)`.

**(D5) [WEIGHT LOCALIZATION].** For every fixed `k` and `eta in (0, 1/2]`, the
contribution to `W_k(T)` (T-105060 §2) of pairs with `y_j >= eta` is
`<<_{k,eta} T^{1-eta/4} (log T)^{k+2} = o(N_0(T))` — using additionally the
Rolle gap-doubling lemma (D5.0, unconditional) and EXTERNAL-CLASSICAL
Hardy–Littlewood 1921 (`maxgap_0 << T^{1/4+eps}`) to cap the T-overhanging
gap's reach. Hence `w_k` is carried entirely by pairs with `y_j < eta`, for
every `eta > 0`: the descent ladder's open burden is a NEAR-REAL-PAIR problem.

**(D4) [VERIFIED-HEIGHT PROPAGATION].** If `Xi_0` has no non-real zeros with
`|Re t| <= X`, then `Xi_k` has none with `|Re t| <= X - k/2` (loss exactly 1/2
per rung; effective, unconditional given the verification input).

## 2. Proofs

Full text: `GRAND/progB2/laneD/DERIVATION.md` §§D0–D5. Kernel of (D1): the
complex partial-fraction identity (L-105061 Lemma 2.1 run on complex compacta)
has absolutely summable imaginary parts (`Sum 1/|w - zeta|^2 < infinity`,
convergence exponent ≤ 1 < 2); at a zero `w = u + iv`, `v > 0`, of
`Xi_{k+1}` with `Xi_k(w) != 0`, grouping each conjugate pair gives the exact
identity
```
Sum_j m_j [(y_j^2 - v^2) - (u-x_j)^2] / (|w-zeta_j|^2 |w-conj zeta_j|^2)
  = m/(2|w|^2) + (1/2) Sum_n m_n/|w-t_n|^2  > 0,
```
strict positivity from the existence of real zeros (Rolle floor + Hardy), so
some pair has `(u-x_j)^2 + v^2 < y_j^2`. (D2): assign each confined zero to
its disk; disk occupancy ≤ unit-window count `<= c_{k+1} log` (L-105062 §2.3
Jensen machinery, constants tower-large in k, harmless at fixed k); admissible
pairs ≤ `N_k(eta, T+1) + O_k(1)`. (D3): iterate k times, then the classical
base case. (D4): induction with (D1). (D5): a pair overhangs
`<= n_k^r(2y_j-interval) + 1` gaps, each at weight ≤ 1; pair reach capped at
`x_j <= 2T` by gap-doubling + Hardy–Littlewood.

## 3. What this gives the program

- First unconditional (mod classical density) NEW-to-repo rung-density
  theorem: high zeros of high derivatives are as rare as off-line zeta zeros,
  up to `log^k`.
- The descent functional `w_k` is localized at `y_j -> 0` (D5): together with
  [THRESHOLD] (near-real pairs saturate weight 1 per gap) the open successor
  problem is precisely counting NEAR-REAL pairs — interfaces PR/[I-W] of
  T-105065 (draft).
- D4 turns the X-105061 census's observed all-real ladder into a theorem below
  the verified height, and scales to the literature verification height.

## 4. Honesty

- RH not addressed. Nothing bounds near-real pairs; `w_k` finiteness stays
  open.
- Constants `c_k, C_k` inherit L-105062's tower-largeness (Sub-lemma A
  abscissae); all statements asymptotic at fixed k. No uniformity in k is
  claimed anywhere.
- EXTERNAL-CLASSICAL inputs (Selberg/Carlson density; Hardy–Littlewood gaps;
  Jensen/Walsh ancestry — the last re-proved, not consumed) transcribed,
  literature-unverified in-container, same discipline as Q-0014/Conrey rows.
- (D2) is one-directional: it cannot LOWER-bound rung densities; no converse.

## 5. Falsifiers

A non-real zero of `Xi_{k+1}` outside every closed Jensen disk of `Xi_k` and
with `Xi_k(w) != 0` (refutes D1 — checked never in 550+ synthetic configs +
Xi-like plant); a consecutive pair of real `Xi_{k+1}` zeros with ≥ 2 distinct
real `Xi_k` zeros strictly between (refutes D5.0 — 3021 intervals clean); a
rung with `N_k(eta, T)/T` bounded away from 0 given the classical density
inputs (refutes D3's iteration).
