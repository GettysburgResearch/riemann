# T-105065 — Repulsion-conditional proportion: near-line pair rarity prices the full descent

Claim ID: `T-105065`
Status: **CONDITIONAL THEOREM (three assumed layers, named exactly; assembly algebra proved) — RH NOT ADDRESSED**
Created: 2026-08-23
Agent: claude (lane D, Program B2)
Depends on: `T-105060` (c) (descent master, itself conditional on [I-DIPOLE]); `L-105063` (regime-wise `A'_k = max(6, 2k)`); `L-105066` (draft: D3 density + D5 localization); EXTERNAL-CLASSICAL: Conrey 1983 (`kappa_k -> 1`), Selberg 1946 / Carlson 1920 (zero density), Hardy–Littlewood 1921 (gap bound) — all transcribed, literature-unverified in-container.
Replay: `GRAND/progB2/laneD/DERIVATION.md` §D7.
RH status: **unproved, not addressed**

## 1. Hypotheses (exact interfaces consumed)

`gbar(x) := 2pi/log(x/2pi)` (mean real gap; RvM on every rung, L-105062
Cor 2.1). Fix `eta in (0, 1/2]`.

**[H1] = [I-DIPOLE]** with per-rung constants `A'_k`: PROVED with
`A'_k = max(6, 2k)` on the L-105063 regimes C-0∪C-1∪C-2∪C-3; ASSUMED on the
residual regimes (R-C1) deep clusters and (R-C2) supercritical shallow mass
(L-105063 §4). [If a successor proves the residual with a different constant
sequence, it substitutes verbatim.]

**[H2] = [I-W(eta)]** (lane-W compression interface, ASSUMED — pinned form):
constants `C_1, C_2, T_W` with, for all `k <= K`, `T >= T_W`, `T' := 2T + 1`:
```
W_k(T) <= C_1 P_k(1; T') + C_2 Sum_{pairs: gbar(x_j) < y_j <= eta, 0 < x_j <= T'} gbar(x_j)/y_j
          + W_k^{high(eta)}(T) + o(N_0(T)).
```
(The last two terms are UNCONDITIONALLY `o(N_0(T))` by L-105066 D5 — they are
kept in the interface so lane W need not re-prove them.)

**[H3] = PR(theta, eps; K, eta)** (near-line pair repulsion, ASSUMED):
`theta in [0, 1)`: there is `T*` with, for all `k <= K`, `lambda >= 1`,
`T >= T*`:
```
P_k(lambda; T) := #{pairs (x_j, y_j) of Xi_k, mult : x_j in (0,T],
                    y_j <= min(lambda gbar(x_j), eta)} <= eps lambda^theta N_k(T).
```
RH would give `P_k ≡ 0`; PR is strictly weaker and is the kind of statement
pair-correlation / repulsion technology targets. Only `y_j <= eta` is
hypothesized; larger `y_j` are discharged unconditionally (L-105066).

**[H4] EXTERNAL-CLASSICAL:** Conrey 1983 (`kappa_k -> 1`, qualitative only);
Selberg 1946 or Carlson 1920 (through L-105066 D3); Hardy–Littlewood 1921
(through L-105066 D5).

## 2. Statement

**(a)** Under [H1]–[H4], for every `K` admissible in [H3], with
`C(theta) := 2 (1 + 2^theta/(1 - 2^{theta-1}))`:
```
1 - kappa_0 <= (1 - kappa_{K+1}) + (6 + 2K)(K + 1) C(theta) (C_1 + C_2) eps .
```

**(b)** If [H3] holds for every `eps > 0` with `K = K(eps) -> infinity`
satisfying `1 - kappa_{K(eps)+1} <= eps` (possible by Conrey) and
`K(eps)^2 eps -> 0`, then `kappa_0 = 1`: asymptotically 100% of zeta's
nontrivial zeros lie on the critical line. **This is a proportion statement,
NOT RH** (RH requires every zero; proportion 1 admits `o(N(T))` exceptions).

## 3. Proof

Fix `k <= K`. By [H2] then [H3]: first term `<= C_1 eps N_k(T')`. Second term
dyadically: bands `lambda in [2^m, 2^{m+1})`, `0 <= m <= log_2(eta/gbar(T'))`;
per-pair contribution `gbar/y <= 2^{-m}`, band count
`<= P_k(2^{m+1}; T') <= eps 2^{(m+1)theta} N_k(T')`; sum
`<= eps N_k(T') 2^theta/(1 - 2^{theta-1})`. Third and fourth terms
`o(N_0(T))`. Divide by `N_0(T)`; `N_k(T')/N_0(T) -> 2` (RvM on every rung);
limsup: `w_k <= C(theta)(C_1 + C_2) eps`. Feed T-105060 (c) with per-rung
constants `A'_k <= 6 + 2K` (`k <= K`):
`1 - kappa_0 <= (1 - kappa_{K+1}) + Sum_{k <= K} A'_k w_k` gives (a). For (b)
let `eps -> 0` along the assumed sequence. QED.

## 4. Honest scope

1. **Three assumed layers.** [H1]-residual, [H2], [H3] are all open. The
   theorem's content is the exact interface algebra: it reduces a proportion-1
   statement for zeta to (i) closing two technical dipole regimes, (ii) a
   per-pair weight compression of the type lane W is building, and (iii) a
   quantitative near-line pair repulsion with any exponent `theta < 1` and
   `eps = o(K^{-2})` along the Conrey sequence.
2. **The `K^2 eps` trade-off** is where a QUANTITATIVE Conrey rate would pay:
   Conrey's `kappa_K` lower bounds are explicit in the literature; importing a
   rate would convert (b) into an explicit `eps(theta)`-threshold statement.
   Not done here (qualitative Conrey only, per the T-105060 discipline).
3. **Not RH**, and not a new unconditional proportion: `kappa_0 = 1` under
   hypotheses. No circularity: [H3] constrains vertical pair heights `y_j`;
   the conclusion is the horizontal (real-proportion) count; the classical
   density input enters only for `y_j > eta`.
4. Multiplicity conventions as in T-105060; all counts with multiplicity.

## 5. Falsifiers

An in-regime violation of [H1] (see L-105063 §5); a configuration family with
`W_k` exceeding [H2]'s form by more than `o(N_0)` (would re-pin the interface
shape — the assembly reruns with any per-(pair,gap) dominating shape, as in
T-105060); a proof that `P_k(1; T) >> N_k(T)` for all large `k` (would show
near-line pairs are generically DENSE on high rungs — [H3] false as stated,
and the descent route would need the weight, not the count); an unconditional
proof of [H3] for some `theta < 1`, `eps -> 0` (not a falsifier but the
intended successor use — it would make (b) unconditional modulo [H1]/[H2]).
