# T-105060 — The Levinson descent ladder: off-line mass at rung 0 is priced by summed close-pair weight along the ξ-derivative chain

Claim ID: `T-105060`
Status: **CONDITIONAL THEOREM — assembly complete and stress-tested; consumes `L-105062` (PROVED), `L-105061` (dipole interface: partial-fraction + threshold PROVED; count cap PROVED on the `L-105063` regimes — A′ = 6 on C-0∪C-1∪C-2, 2k on the depth-k shallow ladder — OPEN only on its residual regimes R-C1/R-C2), and one EXTERNAL-CLASSICAL input (Conrey 1983); RH NOT ADDRESSED**
Created: 2026-08-22
Agent: claude (external reviewer lane; Program B lanes B1/B3/B4 + orchestrator)
Depends on: `L-105062` (strip + conservation + Rolle + monotone ladder, proved), `L-105061` ([I-DIPOLE] pinned interface with constant `A'`), EXTERNAL-CLASSICAL: J. B. Conrey, "Zeros of derivatives of Riemann's ξ-function on the critical line", J. Number Theory 16 (1983) 49–74 (`kappa_k -> 1` as `k -> infinity`; only this qualitative form consumed; coordinates transcribed, literature-unverified in-container — same discipline as the repo's Q-0014 flag on Speiser).
Replay: `experiments/X-105060-descent-ladder/` (assembly stress tests) and `experiments/X-105061-xi-derivative-census/` (finite-height defect ledger).
RH status: **unproved, not addressed**

## 1. Historical frame (what this theorem is)

Levinson, late in life, is reported to have believed a "converse to Rolle's
theorem" should let on-line zero proportions descend the ξ-derivative ladder —
from the almost-all-real zeros of high derivatives back to ζ itself — and no
one has made the argument work (biographical attribution: folklore/secondary
sources; not verified in-container). The forward direction is trivial (Ξ real
on the line ⇒ Rolle pushes real zeros UP the ladder); the converse is FALSE
for generic functions (`x^2 + 1`), yet TRUE at the 100% level for ξ-like
rigidity classes: Hellerstein–Williamson 1977 (real entire `f` with
`f, f', f''` all real-rooted lies in Laguerre–Pólya) and Wiman's conjecture —
Sheil-Small 1989 (finite order) completed by Bergweiler–Eremenko–Langley 2003
(`f, f''` real-rooted suffices) [attributions transcribed, literature-
unverified in-container], with Speiser's theorem
making rung one an exact RH-equivalence. What has never existed is the
QUANTITATIVE deformation. This theorem supplies it: the descent works exactly,
with the failure isolated into ONE geometric functional — the weighted
close-pair mass `W_k` — and priced linearly. The open content is thereby
compressed into the single per-gap count cap `L-105061` (whose threshold half
is proved) plus the (hard, honestly open) question of bounding `W_k`.

## 2. Definitions

Setting and counts as in `L-105062` §0. Gaps of `Xi_k` = bounded components of
`R \ {real zeros}`; the gap list `𝒢_k(T)` = gaps meeting `(0, T]` (≤ M+1
members, including the origin gap and the T-overhanging gap — both ordinary
members; no unconditional `O(log)`-type bound on the T-overhanging gap's
length is available at every rung, so it MUST be priced inside `W_k`, not
absorbed into log-terms: recorded trap). Pair `(x_j, y_j)`
overhangs `G = (a,b)` iff `x_j - y_j < b` and `x_j + y_j > a`.

```
W_k(T) := Sum_{G in 𝒢_k(T)} Sum_{pairs j of Xi_k overhanging G, with mult} min(1, |G|^2/(4 y_j^2))
kappa_k := liminf_T N_k^r(T)/N_k(T),    w_k := limsup_T W_k(T)/N_0(T)  in [0, +infinity].
```

The inner sum is a per-(pair, gap) DOUBLE sum: a pair overhanging several gaps
is charged once per gap — the convention that makes the per-gap dipole bound
sum with zero loss (no separate overhang factor exists anywhere downstream).

## 3. Statement

**(a) [PRICED CONVERSE ROLLE] (conditional on [I-DIPOLE] with constant A′).**
For every `k >= 0` and every `T > 0`:

```
N_{k+1}^r(T) <= N_k^r(T) + 1 + A' * W_k(T).
```

**(b) [DESCENT] (conditional on [I-DIPOLE]; consumes L-105062 Thm 2).** For
every `k` and `T >= T_k` (constants `A_k = 70+6k` admissible, `B_k, T_k` from
L-105062):

```
N_k^c(T) <= N_{k+1}^c(T) + A' * W_k(T) + A_k log T + (B_k + 1).
```

**(c) [FINITE-K MASTER] (same hypotheses).** For every fixed `K >= 0`:

```
1 - kappa_0 <= (1 - kappa_{K+1}) + A' * Sum_{k<=K} w_k.
```

**(d) [MASTER COROLLARY] (adding EXTERNAL-CLASSICAL `kappa_k -> 1`, Conrey
1983).**

```
1 - kappa_0 <= A' * Sum_{k>=0} w_k,
```

VACUOUS when the right side diverges — the content is confined to the
(unproved) case `Sum w_k < infinity`, which is the open successor problem.

**(e) [RH-SIDE CONSISTENCY].** Under RH every `Xi_k` is Laguerre–Pólya
(Hadamard: `Xi` even order-1 with all-real zeros is an LP form; Laguerre's
theorem: LP is closed under differentiation, via polynomial approximation
[Levin, Distribution of Zeros of Entire Functions, Ch. VIII] + Cauchy +
Hurwitz), so no rung has any non-real pair, `W_k ≡ 0`, `w_k = 0`, and both
sides of (d) vanish. Consistency, not new information.

## 4. Proof

**(a).** Let `t_1 < ... < t_M` be the distinct real zeros of `Xi_k` in
`(0, T]` with multiplicities `m_i`. Partition the real zeros of `Xi_{k+1}` in
`(0, T]`: (bucket 1) at the `t_i`: exactly `m_i - 1` each (real-analytic
multiplicity drop), total `N_k^r(T) - M`; (bucket 2) inside gaps meeting
`(0, T]`: at most `Sum_{G in 𝒢_k(T)} n'(G)` (a gap may stick out of `(0,T]`
and `n'(G)` counts its whole interior — slack only helps). By [I-DIPOLE],
`Sum_G n'(G) <= #𝒢_k(T) + A' W_k(T) <= (M+1) + A' W_k(T)` — the single line
where the double-sum definition of `W_k` pays: per-gap bounds ADD with no
overhang loss. Total: `N_{k+1}^r <= (N_k^r - M) + (M+1) + A' W_k`. Boundary
audit: origin gap and T-overhanging gap are ordinary members of `𝒢_k(T)`;
for `k` even the origin gap `(-t_1, t_1)` contains `Xi_{k+1}`-zeros in
`±`-pairs plus 0, of which only those in `(0, T]` are counted — slack again.
QED.

**(b).** `N_k^c - N_{k+1}^c = (N_k - N_{k+1}) + (N_{k+1}^r - N_k^r)
<= (A_k log T + B_k) + (1 + A' W_k(T))` by L-105062 Thm 2 and (a). QED.

**(c).** Iterate (b) over `k = 0..K` (`T >= max T_k`); divide by `N_0(T)`;
`limsup`. Left side: `limsup (1 - kappa_0(T)) = 1 - kappa_0` (exact identity).
Right side, term by term (finite sum of nonnegative terms):
`N_{K+1}^c/N_0 = (1 - kappa_{K+1}(T)) * (N_{K+1}/N_0)` with `N_{K+1}/N_0 -> 1`
(L-105062 Cor 2.1, `N_0 >> T log T`), so its limsup is `1 - kappa_{K+1}`;
`A' W_k/N_0 -> A' w_k` by definition; `(S_K log T + S_K')/N_0 -> 0` where
`S_K = Sum A_k = 70(K+1) + 3K(K+1)`, `S_K' = Sum(B_k + 1)`. QED.

**(d).** Each finite-K instance of (c) is a numerical inequality (the T-limit
already taken). With `S := Sum_{k>=0} w_k in [0, infinity]` (monotone limit):
for every `K`, `1 - kappa_0 <= (1 - kappa_{K+1}) + A' S`; let `K -> infinity`
using [EXTERNAL: Conrey] `kappa_{K+1} -> 1`. No limit interchange occurs — the
order is T first (inside (c)), then K. QED.

**(e).** As stated; the LP-closure step proved in the replay notes (polynomial
approximation + Gauss–Lucas + Hurwitz). QED.

## 5. Verification (assembly stress tests + census)

- Synthetic ladders (known zeros, exact rational arithmetic): every chain
  quantity computed exactly on 10 adversarial configs + 250 random trials —
  all of {per-gap Rolle ≥ 1, parity, threshold, dipole `A' = 4`, (a), (b)}
  hold; pair-annihilation configs (F has pairs, F′ none, `N^r` jumps UP)
  priced exactly by `A'W`; a single pair overhanging SIX gaps charged once per
  gap with no loss. Worst observed `extra/weight = 2.0` (see L-105061 §4).
- The budgeted-mp census (`X-105061`, budgeted-mp, T0 = 500): all real-zero
  counts `R_k(500) = 269/269/270/269` for `k = 0..3`, defect ledger
  `X_0 = X_1 = X_2 = 0` — every gap of `Xi_k` contains EXACTLY one real zero
  of `Xi_{k+1}` (268/268/269 gaps): on `[0, 500]` the converse Rolle holds
  with ZERO defect, consistent with `W_k = 0` there (no observed pairs).

## 6. Honest scope

1. **RH is not addressed.** UPDATE 2026-08-23: the successor wave sharpened
   this item substantially. `L-105064` (weight compression: every pair
   carries total gap-weight < 3) proves **`w_k <= (3/2c)(1 - kappa_k) <
   infinity` for every rung** — finiteness, previously unknown — modulo one
   positive real-zero-proportion input per rung (EXTERNAL-CLASSICAL Levinson/
   Conrey, or the Z23 import row at every rung via L-105062 §6), and
   `w_k -> 0`. `L-105066` further proves every `w_k` is carried entirely by
   NEAR-REAL pairs (`y -> 0`; high pairs contribute `o(N_0)` given the
   Hardy–Littlewood gap input), and gives the rung-density theorem
   `N_k(eta, T) << T^{1-eta/4} polylog`. What remains genuinely open: the
   two-rung/master feeds are self-referential (coefficient > 1 —
   `L-105064` W7/W8, honest ledger), so (d) still yields no new `kappa_0`;
   the open successor target is now precisely the NEAR-LINE pair statistic
   (`T-105065` states the repulsion-conditional version).
2. **Not a new proportion for zeta**: (d) CONSUMES `kappa_{K+1}` lower bounds
   and would produce one for `kappa_0` only given `Sum w_k` control. The
   imported Zeta23 baseline flows the OTHER way — UP the ladder via L-105062
   Thm 4/§6 (`kappa~_k >= 0.67250...` for every `k`, modulo the import row's
   own status: upstream review pending — the ladder transfer itself, Thm 4, is
   unconditional); the descent prices the return trip. The two directions are
   complementary, neither is circular.
3. **Conditionality ledger**: (a)–(d) are conditional on [I-DIPOLE] —
   whose threshold + partial-fraction layers are PROVED in L-105061, and
   whose count cap is PROVED on the `L-105063` regimes with the regime-wise
   constant `A' = max(6, 2k)` (6 on C-0∪C-1∪C-2; `2k` on the depth-k
   shallow ladder C-3, `k` unbounded — hostile-review correction: no single
   absolute constant is proved on the four-regime union); the residual
   conditionality is confined to gaps in
   `L-105063` §4's regimes (R-C1) deep clusters and (R-C2) supercritical
   shallow mass. L-105062 is proved; [EXTERNAL: Conrey] is classical,
   consumed qualitatively. (e) and the census are unconditional.
4. **Context**: Speiser (1934): RH ⟺ `zeta'` zero-free in `0 < Re s < 1/2`
   — the repo's own certified Speiser scan (`speiser.py`, zeta' zero-free in
   `[0.001, 0.499] x [1, 1200]` @ branch
   `origin/claude/riemann-repo-development-h4vg4v`
   `0810053c42b4dfab421f760322d959903f313604`) flags the equivalence as
   literature-unverified (Q-0014); this deposit does not resolve Q-0014 and
   does not use Speiser anywhere. Levinson–Montgomery (1974) is the ancestor
   of the conservation lemma; here the ladder is run on the completed ξ in the
   t-variable, where conservation holds at every rung with the SAME main term.
5. Multiplicity conventions: all counts with multiplicity; the distinct-zeros
   ladder is L-105062 Thm 3′/§6.

## 7. Falsifiers

(F1) A gap with an extra `Xi_{k+1}`-zero but overhanging weight `< 1` (refutes
the proved threshold — hence [I-PF] or the strip lemma). (F2) A per-gap
`extra/weight > A' = 4` (refutes the pinned interface; assembly re-runs with
any valid `A'`). (F3) A budgeted-mp census window violating (a) at computable
height given its interfaces. (F4) A proof that `Sum w_k < infinity` would make
(d) a genuine new proportion theorem — that is the intended successor use, not
a falsifier; a proof that `w_0 = infinity` would confine the ladder's content
to (a)–(c) at fixed k.
