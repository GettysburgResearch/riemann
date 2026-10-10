# L-105064 — Weight compression: every non-real pair carries total gap-weight < 3, and W_k is dominated by the off-line zero count

Claim ID: `L-105064`
Status: **PROVED (Lemmas W1–W2 and Theorem W4 are unconditional interval
combinatorics (proof below, self-contained); Lemma W5 / Corollaries W6–W8
consume a positive real-zero-proportion input per rung (EXTERNAL-CLASSICAL
Levinson 1974 for k=0, Conrey 1983 for k>=1; alternatively the repo-internal
L-105062 §6 constant 0.6725 modulo the Z23-UPSTREAM import row) — RH NOT
ADDRESSED**
Depends on: `L-105061` §1 (objects, overhang convention), `L-105062`
(strip lemma y<=1/2; Cor 2.1 RvM on every rung), `T-105060` §2 (W_k, w_k).
Replay: laneW NOTES.md + check scripts (this dir): 200000 random pointwise
configs, 20000 global-bookkeeping configs, 80000 census-gap configs
(X-105061 zeros.json, all four rungs) — zero violations; both sharpness
regimes of W2 realized numerically.
RH status: **unproved, not addressed**

## 1. Setting

`F = Xi_k`; real zeros `Z` (closed, discrete, `Z = -Z` by parity, unbounded
both ways); gaps = bounded components of `R \ Z` (all components bounded,
L-105061 §1). Non-real pairs `p = (x_p, y_p)`, `0 < y_p <= 1/2` (strip),
multiplicity `m_p`; both signs of `x` occur as distinct pairs; purely
imaginary pairs (`x = 0`) once. `I_p := (x_p - y_p, x_p + y_p)`. Overhang
(deposited convention): `p` overhangs `G = (a,b)` iff `x_p - y_p < b` and
`x_p + y_p > a` — i.e. iff the open intervals `I_p` and `G` intersect.
Per-(pair,gap) weight `q(G)^2`, `q(G) := min(1, |G|/(2 y_p))` (note
`min(1, u^2) = min(1,u)^2`). Define the pair's TOTAL weight

```
omega(p) := Sum_{gaps G : G ∩ I_p ≠ ∅} q(G)^2 ,
g_max(p) := max{|G| : G overhung by p}  (0 if none),
mu_p     := min(1, g_max(p) / (2 y_p)).
```

`W_k(T)` (T-105060 §2) charges `m_p q(G)^2` per (pair, gap in 𝒢_k(T)).

## 2. Pointwise compression

**Lemma W1 (run structure).** The gaps overhung by `p` form a finite
consecutive run. Call `G` CONTAINED if `G ⊆ I_p`, PROTRUDING otherwise.
Then (i) at most two overhung gaps are protruding; (ii) the contained gaps
are pairwise disjoint subintervals of `I_p`, so their lengths sum to
`<= |I_p| = 2 y_p`.

*Proof.* `Z ∩ cl(I_p)` is finite (discrete in compact), so `I_p \ Z` has
finitely many components; each overhung gap contains exactly one of them
(gaps are the maximal zero-free open intervals), whence finiteness and
consecutiveness. (i) A protruding overhung `G = (a,b)` has `a < x_p - y_p`
or `b > x_p + y_p`; in the first case `b > x_p - y_p` (overhang) forces
`x_p - y_p ∈ G`, in the second `x_p + y_p ∈ G`. Gaps are disjoint, so at
most one gap contains each endpoint of `I_p` — at most two protruding
(a single giant gap `G ⊇ I_p` contains both and is then the only overhung
gap). (ii) Immediate. QED.

**Lemma W2 (weight compression, sharp).** For every pair `p`:

```
omega(p) <= mu_p + 2 mu_p^2 <= 3 mu_p <= 3 .
```

*Proof.* Protruding gaps: at most two, each `q(G)^2 <= mu_p^2`. Contained
gaps: `q(G)^2 <= (|G|/2y_p) * q(G) <= (|G|/2y_p) * mu_p`; summing via
W1(ii) gives `<= mu_p`. Add. QED.

**Sharpness.** (a) `sup omega = 3`: real zeros at `x-y-L, x-y+eps,
x+y-eps, x+y+L` (`L >= 2y`) give `omega = 2 + ((2y-2eps)/2y)^2 → 3`;
`omega < 3` always. (b) Small-`mu` regime: `n = 2y/g` equal contained gaps
of length `g` plus two protruding length-`g` gaps give
`omega = mu + 2mu^2` exactly (ratio to the bound → 1). So neither the `mu`
term nor the coefficient of `mu^2` can be improved; `C_omega = 3` is the
sharp absolute constant. (c) Adversarial: giant gap `⊇ I_p`: `omega <= 1`.
Cluster of tiny gaps: `omega <= mu → 0`. Multiplicity: `omega` is per
distinct pair; all downstream sums charge `m_p * omega(p)`.

**Corollary W2' (high pairs carry vanishing weight).** If every gap meeting
`I_p` has length `<= Γ` then `omega(p) <= Γ/(2y_p) + Γ^2/(2y_p^2)`; in
particular `omega(p) <= Γ/y_p` when `Γ <= y_p`. Stated in ACTUAL local gap
lengths — no averaging assumption. (Under an a-priori local max-gap bound
`Γ ~ Λ * gbar(x_p)`, `gbar(x) = 2π/log(x/2π)`: `omega(p) = O(Λ gbar(x_p)/y_p)`
for `y_p >= Λ gbar(x_p)` — hypothesis NOT proved here.)

## 3. Global compression

**Lemma W3 (localization).** Let `t_1` = smallest positive real zero,
`b_T` = smallest real zero `> T`. Every gap meeting `(0,T]` is contained in
`(-t_1, b_T]`; hence every pair charged by `W_k(T)` has
`x_p ∈ (-t_1 - 1/2, b_T + 1/2)`.

*Proof.* `G = (a,b)` meets `(0,T]`: pick `u ∈ G ∩ (0,T]`; then `b > u > 0`,
`a < u <= T`. If `b > T`: `(a,b)` zero-free with `a <= T < b` makes `b` the
first zero above `T`, so `b = b_T`; else `b <= T < b_T`. If `a < -t_1`:
then `-t_1 ∈ (a, b)` (as `b > 0 > -t_1`), but `-t_1 ∈ Z` (parity) —
contradiction with `G` zero-free; so `a >= -t_1`. Overhang then forces
`x_p - y_p < b_T`, `x_p + y_p > -t_1`; use `y_p <= 1/2`. QED.

**Theorem W4 (W_k is dominated by the off-line count).** For all `k, T`:

```
W_k(T) <= Sum_{p : x_p ∈ (-t_1-1/2, b_T+1/2)} m_p (mu_p + 2 mu_p^2)
       <= (3/2) N_k^c(b_T + 1/2) + c_k^0 ,
c_k^0 := (3/2) N_k^c(t_1 + 1/2) + 3 P_k^0   (finite, T-independent),
```

`P_k^0` = purely-imaginary pair count (mult).

*Proof.* Interchange the finite nonnegative double sum defining `W_k(T)`:
per pair, the inner sum runs over a SUBSET of its overhung gaps, so it is
`<= omega(p) <= mu_p + 2mu_p^2 <= 3` (W2); the charged pairs are localized
by W3. Counting with multiplicity: pairs with `x ∈ (0, b_T + 1/2]` number
`N_k^c(b_T + 1/2)/2` (each contributes two strip zeros of equal real part);
`x = 0`: `P_k^0`; `x ∈ (-t_1 - 1/2, 0)`: mirrors (parity) of pairs with
`x ∈ (0, t_1 + 1/2)`, at most `N_k^c(t_1+1/2)/2`. Both corrections are
finite (zeros in a compact set). QED.

**Recorded trap honored.** No unconditional bound on `b_T - T` exists at any
rung (T-105060 §2): W4's argument is `b_T + 1/2`, NOT `T + 1`. The sketch
form `W_k <= (3/2)N_k^c(T+1) + O(1)` is FALSE-as-stated in general.

**Lemma W5 (b_T = O(T) from any positive proportion).** If
`kappa_k = liminf N_k^r/N_k >= c > 0` then `b_T <= (1/c + o(1)) T`.
*Proof.* No real zeros in `(T, b_T)` gives `N_k^r(b_T-) = N_k^r(T) <=
N_k(T)`; apply the liminf at `S ↑ b_T` and RvM (L-105062 Cor 2.1) on rung
`k`; `b_T > T` makes the log-ratio favorable. QED.
Inputs for `c`: `k=0` Levinson 1974 (`c = 0.34`, EXTERNAL-CLASSICAL);
`k>=1` Conrey 1983 per-rung proportions (EXTERNAL-CLASSICAL); or `c =
0.6725007...` at EVERY rung via L-105062 §6 (modulo Z23-UPSTREAM import).

## 4. Normalized consequences (what is bought, honestly)

**Corollary W6.** If `kappa_k >= c > 0` then
`w_k <= (3/(2c)) (1 - kappa_k)`. In particular **`w_k < ∞` for every `k`**
(new: T-105060 §6.1 had recorded that not even finiteness was known), and
`w_k → 0` as `k → ∞` (Conrey qualitative). With `c = 0.6725` (modulo
import): `w_k <= 2.2305 (1 - kappa_k)`.
*Proof.* W4 + W5 + RvM on rungs `k, 0`: `N_k(b_T+1/2)/N_0(T) <= (1+o(1))/c`;
`limsup N_k^c/N_k = 1 - kappa_k`. QED.

**Corollary W7 (two-rung machine — currently NOT closing).** From
T-105060(c) at `K=0` and W6: with `theta := 3A'/(2c_0)`, if `theta < 1`
then `kappa_0 >= 1 - (1 - kappa_1)/(1 - theta)`. Constants ledger:
closing needs `A' < 2c_0/3 = 0.448` (at `c_0 = 0.6725`). Proved regime
constant `A' = 6`: `theta ≈ 13.4`. Conjectured sharp `A' = 2`:
`theta ≈ 4.46`. Even `A' = 1` with no `1/c` loss: `theta = 3/2`. The
absolute constant `C_omega = 3` is pointwise sharp (§2), so closing the
loop requires the AVERAGE of `omega` over pairs to be small — by W2' this
holds exactly when hypothetical off-line zeros are predominantly HIGH
(`y_p >>` local gap lengths): a zero-distribution statement, recorded as
the open successor target.

**Corollary W8 (master feed).** `1 - kappa_0 <= (3A'/2) Sum_k (1-kappa_k)/c_k`.
[Hostile-review note: with the deposited PER-RUNG constant `A'_k = max(6, 2k)`
inside the sum, finiteness of the right side needs `Sum_k k(1-kappa_k) < inf`
— still implied by a quantitative `O(1/k^2)`-type Conrey rate, which remains
EXTERNAL-CLASSICAL and literature-unverified in-container.]
Modulo a quantitative Conrey rate with `Sum (1-kappa_k) < ∞`
(literature-unverified in-container) and the import row, the RHS is FINITE —
the hypothesis `Sum w_k < ∞` of T-105060(d) is then DISCHARGED — but the
`k = 0` term has coefficient `> 1`, so the inequality is self-referential
and yields NO bound on `1 - kappa_0`. Feeding W4 directly into descent (b)
is likewise wrong-direction (`3A'/2 > 1`). The compression's yield is
(i) finiteness `w_k < ∞`, (ii) `w_k → 0`, (iii) reduction of the whole
W-side to the pure off-line statistic `Sum_p m_p (mu_p + 2 mu_p^2)`.

## 5. Verification (this dir)

- 200000 random pointwise configs: `omega <= mu + 2mu^2` never violated;
  max ratio 0.986; sup-3 family reaches 2.99999995; both sharpness regimes
  realized (cluster ratio → 1). Giant-gap and tiny-cluster adversarial
  cases exact.
- 20000 synthetic global configs (symmetric zero sets, mirrored pairs with
  multiplicities, random `T`): the chain `W_k(T) <= Sum m_p(mu+2mu^2) <=
  3 * charged-mult` never violated; localization (every pair contributing
  to `W_k(T)` is charged) never violated.
- 80000 configs over the ACTUAL census gap structure (X-105061 zeros.json,
  rungs 0–3, synthetic pairs): zero violations; max observed `omega` at the
  strip cap over real gaps: 2.91 (rung 0, near a long gap at `x ≈ 376`).

## 6. Falsifiers

A pair configuration with `omega(p) >= 3` (refutes W2 — pure combinatorics,
so this would indicate a definition mismatch); a gap meeting `(0,T]` not
contained in `(-t_1, b_T]` (refutes W3); `W_k(T) > (3/2)N_k^c(b_T+1/2) +
c_k^0` on any synthetic or census configuration (refutes W4); a rung with
`kappa_k >= c > 0` and `limsup b_T/T > 1/c` (refutes W5).
