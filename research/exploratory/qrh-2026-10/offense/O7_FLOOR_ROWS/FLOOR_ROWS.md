# O7: the floor rows of the Sep 30 architecture, once the Gram loss is removed

```text
Status: PROPOSED. Exact-rational LP certificates in an exponent model of an external, unreviewed
  manuscript, plus exponent bookkeeping for one constructed cross-row decomposition. Each claim
  carries its own label: PROVED-HERE / PROPOSED / CONDITIONAL / HEURISTIC / EMPIRICAL / OPEN.
  Nothing here proves RH or any zero-free region.
Scope: the floor-bin step of [OAI-Sep30] (Lemma 10.4 / eq. (10.15) at the floor a0, the triangle
  inequality over zero-free rows), at Gram loss b/12 (manuscript) and at Gram loss 0 (the O3 target).
Exact sources or dependencies:
  [OAI-Sep30] OpenAI, "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8", 30 Sep 2026,
     scratchpad copy paper_sep30.tex: Lemma fixed-bin-contour (l. 5808-5925), balanced central
     estimate (l. 5926-6010), sextic large sieve (l. 4707-4720), Lemma 18.1 (plain fourth moment).
     EXTERNAL, UNREVIEWED. Everything resting on it is CONDITIONAL/IMPORTED.
  [OAI-Oct5] OpenAI, Oct 5 "11/12" manuscript (scratchpad paper2.tex), Prop. thm:ms (Moebius mean
     square). EXTERNAL, UNREVIEWED; used only as an IMPORTED input, labelled where used.
  ../../FLOOR_BIN_BARRIER.md (object, (FB) row, no-gain remark), ../../THRESHOLD_CALCULUS.md (low
     side), ../../scripts/{barrier_lp.py, floor_lp.py, threshold_calculus.py} (imported/copied,
     originals unchanged), ../O3_SEP30_X_OCT5/scripts/o3_barriers.py (Gram-zero convention).
What was actually run:
  scripts/floor_rows_lp.py   exact LP + rational dual certificates; Gram {b/12, 0} x energy {paper,
                             optimal} x floor {51/100, 1/2} x saving (floor only / every bin).
  scripts/floor_rows_scan.py same model with the exact delta -> delta0+ limit bin, and raised floors
                             a0 = (1+delta0)/2 with floor saving kappa*delta0.
  scripts/closed_forms.py    sympy closed forms on the LP active sets (checked against the LP).
  scripts/full_model_floor.py  full Part II float model (threshold_calculus imported unchanged and
                             monkeypatched in memory) with paper row counts; EMPIRICAL model values.
  Outputs: floor_rows_lp.out, floor_rows_scan.out, closed_forms.out, results/*.log|json.
Smallest remaining gap: the signed raised-floor estimate FB#(delta0, kappa) of Sec. 5 with
  kappa > 5/6 (any gain over 6/7 with Gram 0); kappa = 1 at delta0 = 1/3 gives 28/33. The constructed
  all-rows-minus-non-floor route reaches only kappa = 1/4 (CONDITIONAL), and every
  "approximate 1/L by a Dirichlet polynomial, bound the remainder absolutely" scheme is capped at
  kappa <= 1/2 (PROPOSED/HEURISTIC class barrier, Sec. 4).
```

RH remains unproved. "sigma0" below is the boundary that one external, unreviewed architecture
would deliver under the stated hypotheses. It is not a theorem.

## 0. Results

All values are exact LP optima with verified rational dual certificates (PROPOSED: they are exact
statements about the exponent model, which itself transcribes the manuscript's stated lemma
outputs; see hypothesis ARCH in FLOOR_BIN_BARRIER.md Sec. 4). "Gram 0" follows O3: the
`P_a^{1/6}` branch `b/6` of Prop. 15.2 is removed and the `P_a^2/Y'` branch `2b - ly` is kept.
Unless stated otherwise the energy lemma is the manuscript's and witnessed bins above the floor have
density-hypothesis counts `R = 1 - delta` ("DH-rows").

| floor-row input | Gram b/12 | Gram 0 |
|---|---|---|
| none (triangle inequality, any row counting), a0 = 51/100 | 167/192 = 0.869792 | **926/1077 = 0.859796** |
| none, floor lowered to a0 -> 1/2 | 13/15 = 0.866667 | **6/7 = 0.857143** |
| floor saving theta at a0 = 51/100, 0 <= theta <= 1/50 | (167-225 theta)/(192-225 theta) | (926-1200 theta)/(1077-1200 theta) -> 902/1053 = 0.856600 |
| constructed input of Sec. 2 (kappa = 1/4, CONDITIONAL) | 13/15 (no gain) | 6/7 (no gain) |
| FB#(delta0, kappa), raised floor a0 = (1+delta0)/2 | 13/15 for every kappa <= 1 | `2(9+13 delta0-12 kappa delta0)/(3(7+9 delta0-8 kappa delta0))`; gain iff **kappa > 5/6** |
| FB#(1/3, 1) (heuristic edge, Sec. 5.2) | 13/15 | **28/33 = 0.848485** |
| FB#(1/2, 1) (square-root cancellation) | 13/15 (paper energy); 106/123 = 0.861789 with hypothetical E\* (262/303 at delta0 = 2/5) | **38/45 = 0.844444** = Gram-0 low-side wall |
| NC(theta): saving theta in the floor and in every witnessed bin, a0 -> 1/2 | 13/15 | (6-8 theta)/(7-8 theta), = 38/45 from theta = 1/14 |

Main findings.

1. **With Gram 0 the floor binds at 926/1077 (6/7 after lowering the floor), and the geometry
   changes character.** The optimum sits on the kink `ly = 2 lx` of the kept Gram branch, so
   `lx < ly`. The density-hypothesis band then *decreases* in delta:
   `F_DH(delta) = F_DH(0) + delta (lx - ly)/2`. Two consequences (PROPOSED, exact):
   * lowering the floor is no longer equivalent to a floor saving (at a0 = 51/100 a floor saving
     theta = 1/50 gives 902/1053 < 6/7);
   * **a raised floor with a signed floor saving needs no saving in any witnessed bin.** Only
     counts above the floor are needed. This is unlike the Gram b/12 picture, where the whole
     near-critical band was co-binding.
2. **The exact threshold is kappa > 5/6.** Write the floor saving at floor height delta0 as
   `theta_F = kappa delta0`. Then `d sigma0 / d delta0 |_0 = (20 - 24 kappa)/147`. A floor saving
   proportional to the floor height helps iff `kappa > 5/6`. The factor `5/6` is
   `(1 - ly + h + ell)/(2h)` at the 6/7 geometry `(2/7, 4/7, 1/7)`: the cost of raising the
   reciprocal contour, the reflected numerator and the slot amplitude, per unit of row saving.
3. **The constructed cross-row decomposition (the task's angle) gives kappa = 1/4** (CONDITIONAL;
   Sec. 2). Its bottleneck is the mollifier remainder on the floor rows. Every scheme of the form
   "approximate `1/L` by a family-structured Dirichlet polynomial of length at most the conductor,
   bound the remainder absolutely" is capped at kappa <= 1/2 (Sec. 4; PROPOSED, with a HEURISTIC
   lower bound for the approximation error). Seven repairs were tried (Sec. 3). None reaches 5/6.
4. **Smallest statement (OPEN):** FB#(delta0, kappa) with kappa > 5/6; kappa = 1 gives
   `sigma0 = 2(9+delta0)/(3(7+delta0))`. Ratios-recipe heuristics with a sextic Gauss-sum bias of
   size `U^{2/3}` make it plausible exactly up to delta0 = 1/3, which gives **28/33** (HEURISTIC).
   With Gram b/12 no floor-row input of this type beats 13/15 (`kappa = 1` is exactly flat there).

## 1. The object and the exact targets

### 1.1 The floor sum

As in FLOOR_BIN_BARRIER.md Sec. 3.1, for a dyad `U = Z^d` and a retained point of
(eq:stage-central-contours) with `Re s = a0 + 16e`, `Re w = 1 - a0 - 6e`, `Re z = z0 = 17/50`:

  `S_F(U; s, w, z) = sum_{u in B_F} xi(u) q_u^{-z} L^S(w, chi_.(u)) H_{eta,u}(s, w, z) / L^S(s, eta chi_.(u))`,

where `B_F` is the set of retained rows with no zero of any presentation in `X_u` in
`Re >= a0 + 2e`, `|Im| <= 3(i+1) T1`. `xi` is nonprincipal at every prime of `S`. The trivial
bound, which is what [OAI-Sep30] uses (l. 5926-5945), is

  `|S_F| << U^{1 + delta0/2 - z0 + eps} Z^{...}`, `delta0 = 2 a0 - 1`.

The `U^{delta0/2}` comes from the functional equation:
`|L(w, chi_u)| = U^{delta0/2 + 6e} |L(1-w, chibar_u)| x (gamma ratio)`, *exactly in modulus*.
It sits in the root number factor `eps_u(w) = W(chi_u) q_u^{1/2 - w} (gamma ratio)`, whose phase is
a normalised sextic Gauss sum.

### 1.2 The exponent row

At the top dyad `d = h` with slot amplitude `x = 1/2` (FLOOR_BIN_BARRIER Sec. 1.2), a bin of real
part `a` (`delta = 2a - 1`) with row-sum exponent `R` closes iff

  `a(1 - ly) + h(R + delta/2 - 1/6) - ell/2 + delta ell/2 <= sigma0`,  `h = 1 - lx + ell`.

A signed saving `U^{-theta}` on the bin sum is `R -> R - theta`. The low side is
`sigma0 >= 5/6 - lx/3 - ly/2 - ell/6 + (g + E)/2`, with `E in {M, (2M+1+3ell)/4, 2M+ell-1}` and
Gram exponent `g in {0, b/6, 2b - ly}` (Gram b/12) or `g in {0, 2b - ly}` (Gram 0).

### 1.3 Exact LP values (PROPOSED; certificates in `floor_rows_lp.out`, `floor_rows_scan.out`)

* Gram 0, low side alone: 38/45 at `(4/15, 8/15, 1/5)` (paper energy); 5/6 (large-sieve-diagonal
  energy E\*).
* Gram 0, low side + floor with the triangle inequality: 926/1077 (a0 = 51/100) at
  `(0.2897, 0.5794, 0.1309)`, and 6/7 (a0 -> 1/2) at `(2/7, 4/7, 1/7)`. This agrees with O3's
  `o3_barriers.json` and with the full float model, 0.859811 (`results/full_zero_paper.log`; floor
  bin binding).
* Gram 0, floor saving theta at a0 = 51/100 with the `delta -> delta0+` DH limit bin included:
  `sigma0 = (926 - 1200 theta)/(1077 - 1200 theta)` on `[0, 1/50]`, then flat at 902/1053.
  The limit bin `R = 1 - delta0` takes over.
* Gram 0, a0 -> 1/2: a floor-only saving gains **nothing** (6/7 for every theta). The bins
  `delta -> 0+` have `R -> 1`.
* Gram b/12: reproduces 167/192, 13/15 and `(167-225 theta)/(192-225 theta)`
  (FLOOR_BIN_BARRIER.md). The raised floor with `kappa = 1` is exactly flat at 13/15 and
  `kappa < 1` is worse, because the optimum there has `lx = ly`.

### 1.4 Closed forms (PROPOSED; `closed_forms.py`)

On the active set {E = M branch, E = 2M+ell-1 branch, Gram kink `ly = 2 lx`, floor row}, valid for
`0 <= delta0 <= 1/2` (at 1/2 the middle energy branch also becomes active):

  `sigma0(delta0, kappa) = 2(9 + 13 delta0 - 12 kappa delta0) / (3(7 + 9 delta0 - 8 kappa delta0))`,
  geometry at `kappa = 1`: `lx = 2/(7+delta0)`, `ly = 4/(7+delta0)`, `ell = (1+delta0)/(7+delta0)`.

| delta0 | 0 | 1/50 | 1/10 | 1/6 | 1/4 | 1/3 | 1/2 |
|---|---|---|---|---|---|---|---|
| kappa = 1 | 6/7 | 902/1053 | 182/213 | 110/129 | 74/87 | 28/33 | 38/45 |
| kappa = 5/6 | 6/7 | 6/7 | 6/7 | 6/7 | 6/7 | 6/7 | 6/7 |
| kappa = 1/2 | 6/7 | 914/1065 | 194/225 | 122/141 | 86/99 | 34/39 | 50/57 |
| kappa = 1/4 | 6/7 | 920/1071 | 200/231 | 128/147 | 92/105 | 37/42 | 8/9 |

Every entry equals the LP value with the full DH band and the a-posteriori check of all bins with
`delta <= 5/6` and `beta* = max(s, a)`. For `kappa < 5/6` the best choice is `delta0 -> 0`, i.e.
6/7.

*Where 5/6 comes from.* At the 6/7 geometry `(2/7, 4/7, 1/7)`, `h = 6/7`, the floor row's
delta0-derivative is

  `(1 - ly)/2 + h(1/2 - kappa) + x ell = 3/14 + 3/7 - 6 kappa/7 + x/7`.

At the floor's worst slot amplitude `x = 1/2` this vanishes at `kappa = 5/6`. If the floor's
correction factor could be taken at amplitude `x = 0`, the threshold would drop to `3/4`. That is
still above the class cap of Sec. 4.

*Why witnessed bins need no saving here.* With `lx < ly` the DH band row is
`F(0) + delta (lx - ly)/2 - theta_NC h`, which is maximal at `delta0+`. A floor with
`theta_F = delta0` is exactly that limit bin. So once the floor carries a saving equal to its height,
every witnessed bin above it closes on its DH count alone. Under Gram b/12 the optimum has `lx = ly`,
the band is flat, and this mechanism is absent.

## 2. The constructed decomposition: all rows minus non-floor rows

This is the angle proposed for B1. Everything in this section is PROPOSED bookkeeping, CONDITIONAL
on the inputs named in each step. The exponent of a term is quoted relative to the trivial
`U^{1+delta0/2}`: a term `<< U^{1 + delta0/2 - kappa_j delta0}` "has kappa_j".

### 2.1 The decomposition

Let `M_u(s) = sum_{N(m) <= V} mu(m) eta(m) chi_m(u) N(m)^{-s} P(log N(m)/log V)` be a smoothed
truncated reciprocal, the Oct 5 object. It is defined for **every** row and is entire. Put
`g_u = xi(u) q_u^{-z} L(w, chi_u) H_u M_u(s)` and `f_u` = the floor summand. Then, exactly,

  `S_F = sum_{all u} g_u  -  sum_{u in NF} g_u  +  sum_{u in B_F} (f_u - g_u)`  =: I - III + II,

where NF is the set of retained rows not in `B_F`. No contour is moved for NF rows: `g_u` is entire,
so I and III are evaluated on the floor contour legitimately. This removes the obstruction of
FLOOR_BIN_BARRIER Sec. 3.4 item 2 (the poles of `1/L` for NF rows), at the price of term II.

### 2.2 Term I (all rows): no diagonal, and the front part is negligible

Split `L(w) = A_u(w) + eps_u(w) B_u(1-w)` by the approximate functional equation (lengths `U^{1/2}`).

* *Front part.* `A_u(w) M_u(s)` is a Dirichlet polynomial in `chi_.(u)` of length `<= U^{1/2} V`.
  For fixed `(n, m)`, `u -> xi(u) chi_{nm}(u)` is a ray character modulo `b* nm`. It is
  nonprincipal because `xi` is nonprincipal at `S`. After the sixth-power-free Moebius inversion and
  expansion of `H_u` (multiplicative in `u`), two-dimensional Poisson summation in `u` gives
  `O(U^{-A})` whenever `U^{1/2} V <= U^{1 - eps}`, i.e. `V <= U^{1/2 - eps}` (PROPOSED; standard).
  So **kappa_I(front) = infinity** for `V <= U^{1/2-eps}`.
* *Dual part.* This is `U^{delta0/2}` times a bilinear form
  `sum_k c_k sum_u xi(u) chibar_u(k) W(chi_u) (smooth)` with `N(k) <= U^{1/2} V`, where `W` is the
  normalised sextic Gauss sum. The needed input is

  **(G_kappa)** `sum_{u ~ U} xi(u) W(chi_u) sum_{N(k) <= K} c_k chibar_u(k) << U^{1 - kappa delta0 + eps} ||c||_{w}`
  for `K <= U^{1-eps}`, in the weighted norm the `B_u` coefficients carry.

  Status: OPEN. Kubota-Patterson theory gives a power saving for each fixed twist, with polynomial
  conductor dependence (literature recall, not re-verified). A uniform bilinear version at
  `K ~ U` is not established for sextic symbols. Heuristically the bias is `U^{2/3}`
  (the `1/2 + 1/n` rule; caveat for `n = 6` in FLOOR_BIN_BARRIER Sec. 3.2). That would give
  `kappa_I delta0 = 1/3 - delta0/2`, i.e. `kappa_I >= 1` iff `delta0 <= 1/3` (HEURISTIC).

### 2.3 Term II (floor rows, mollifier remainder): the bottleneck

`f_u - g_u = xi q^{-z} L(w) H (1 - L(s) M_u(s)) / L(s)`. On floor rows `|1/L(s)| <= U^eps` (buffered
bins, [OAI-Sep30] Lemma buffered-bins). By Cauchy-Schwarz,

  `|II| <= U^eps (sum_u |L(w)|^2)^{1/2} (sum_{all u} |1 - L(s) M_u(s)|^2)^{1/2}`.

* `sum_u |L(w)|^2 << U^{1 + delta0 + eps}`. This follows from Lemma 18.1 of [OAI-Sep30] by
  Cauchy-Schwarz (CONDITIONAL/IMPORTED).
* **(MS_mu)** `sum_u |1 - L(s) M_u(s)|^2 << U^{1 - mu delta0 + eps}` at `Re s = (1 + delta0)/2 + 16e`.
  The front part `sum_{V < n <= X V} lambda_n chi_u(n) n^{-s}`, with `lambda = 1 * mu 1_{<= V}`, has
  mean square `U V^{-delta0}`, provided the family large sieve is diagonal at length `X V`. The dual
  part `eps_u(s) B_u(1-s) M_u(s)` has `|eps_u(s)|^2 = U^{-delta0}` and mean square
  `U (U/X)^{delta0} U^{-delta0} = U X^{-delta0}`. With `X V <= U` the best is `X = V = U^{1/2}`,
  giving **mu = 1/2**. This needs the diagonal range at length `U` (CONDITIONAL on an [OAI-Oct5]-type
  mean square; the unconditional sextic large sieve `K + D + (KD)^{2/3}` (l. 4707) is diagonal only
  for `D <= K^{1/2}`, which forces `V = 1` and `mu = 0`).
* Hence **kappa_II = mu/2 = 1/4**.

### 2.4 Term III (non-floor rows): counts times moments

`|III| <= (#NF)^{1 - 1/4 - 1/(2m)} (sum |L(w)|^4)^{1/4} (sum |M_u|^{2m})^{1/(2m)}` by Hoelder. Here
`sum |M_u|^{2m} << U^{1+eps}` needs the diagonal range at length `V^m <= U`. With
`#NF << U^{1 - c delta0}`,

  `kappa_III = c (3/4 - 1/(2m))`;  `m = 2` (`V = U^{1/2}`): `kappa_III = c/2`.

* DH-rows give `c = 1`, which is beyond current technology for this family.
* The manuscript's unweighted count `R_un = 1 - 2 delta/3` (Prop. 19.2 last clause) gives `c = 2/3`
  (CONDITIONAL/IMPORTED).
* A 2k-th moment would replace 3/4 by `1 - 1/(2k)`.

The NF count enters only here. A Montgomery zero detector or Halasz-Montgomery-Huxley large values
can only improve `c` (Sec. 3, R5-R6).

### 2.5 Ledger

  `kappa = min(kappa_I, mu/2, c(3/4 - 1/(2m)))`, subject to `V <= U^{1/2}`, `V^m <= U`.

With the inputs at hand (Lemma 18.1 and the Oct 5-type diagonal range imported, DH-rows assumed,
(G_kappa) assumed with `kappa_I >= 1/4`): **kappa = 1/4**. This is a CONDITIONAL construction of a
genuine cross-row saving `theta_F = delta0/4`. At a0 = 51/100 it gives `theta_F = 1/200`, i.e.
920/1071 (Gram 0) and 1327/1527 (Gram b/12).

**It does not beat lowering the floor.** By Sec. 1.4, kappa = 1/4 < 5/6, so `delta0 -> 0` is better
and the value stays 6/7 (Gram 0) or 13/15 (Gram b/12). At a0 -> 1/2 every term is `O(delta0) -> 0`:
the scheme's saving is proportional to the distance of the contour from the critical line.

## 3. Repairs of the failing step (Term II, kappa_II = mu/2)

| # | repair | outcome (exponent) | label |
|---|---|---|---|
| R0 | subtract on the *global* line `Re s = beta* + 20e` (where all rows are holomorphic) via the manuscript's own probe identity | Through the contour lemma, `S_F(central) = S_all(global) - sum_{a > a0} S_a(central_a)`. This is the architecture's own bin decomposition read backwards: `S_all(global)` is the high-side quantity the bins were introduced to bound, so the route is circular. Evaluating the non-floor rows on the global line instead costs `(beta* - a)(1 - ly)` per bin, about `0.15` in the Z-exponent for the near-floor bins | PROPOSED |
| R1 | longer / unbalanced mollifier (front length X, dual U/X, mollifier V, `XV <= U`) | `max(V^{-delta0}, X^{-delta0}) >= U^{-delta0/2}`: mu = 1/2. Length beyond U leaves the diagonal range. Ideal mu <= 1 | PROPOSED (exact for this AFE) |
| R2 | detach the reciprocal contour (s at `a1 > a0`, smaller remainder `U^{-delta1/4}`; or w held at 1/2) | Re s costs `1` per unit when w is held, or `(1 - ly + h + ell)/2` per unit of delta1 at the endpoint. The remainder gains `h mu delta1/2`. Net loss for every geometry with `h <= 1` (THRESHOLD_CALCULUS "contour flexibility": affine, endpoint optimal) | PROPOSED |
| R3 | second-order (Neumann) approximant `M(2 - LM)`, remainder `(1-LM)^2/L` | `kappa_II = nu/2` if **(MS4_nu)** `sum_u |1 - L M|^4 << U^{1 - nu delta0}`. With the mollifier of R1, `nu <= 2 mu = 1`, so kappa <= 1/2. Needs nu > 5/3, and a twisted *mollified second moment* `sum_all xi L(w) L(s) M^2` over all rows (length `U V^2 > U`; not negligible by Poisson) | PROPOSED; inputs OPEN |
| R4 | Hoelder with the Oct 5 second moment of `1/L` and Lemma 18.1 | absolute values: theta = 0 (no-gain remark, FLOOR_BIN_BARRIER Sec. 3.3) | PROPOSED |
| R5 | smooth the floor indicator by a Montgomery zero-detecting polynomial | `1_NF <= sum_rho |D_u(rho)|^{2k}` is a nonnegative weight. It only bounds III (improves c) and cannot carry a sign. Term II is untouched | PROPOSED |
| R6 | large values (Halasz-Montgomery-Huxley) over the family | improves the NF count `c` only. `c = 2/3` (Ingham-type, from a fourth moment) or 1 (DH) gives `kappa_III <= c/2`. Not the bottleneck | PROPOSED |
| R7 | attack the dual part directly: `S_F^dual = U^{delta0/2} sum_{B_F} xi W(chi_u) B_u(1-w) H / L(s)` | kappa = 1 iff this signed sum is `<< U^{1 - delta0}`. That is Gauss-sum equidistribution against floor-row weights, i.e. (G_1) plus the restriction to `B_F`. Same subtraction problem, with the same remainder II | OPEN |

Also checked: raising the floor to make the mollifier remainder smaller (`mu delta0/2` grows with
delta0) does not help, because the threshold is a *ratio*: kappa_II = mu/2 is independent of delta0,
and Sec. 1.4 needs kappa > 5/6 at every delta0.

## 4. A class barrier: kappa <= 1/2 for approximate-then-bound schemes (PROPOSED; HEURISTIC lower bound)

Suppose `S_F` is split as (family-structured part) + (remainder bounded in absolute value). The
family-structured part replaces `1/L(s, eta chi_u)` by a Dirichlet polynomial in `chi_.(u)` of
length `N <= U`, so that Poisson or the diagonal large sieve applies over `u ~ U`. Then
`|remainder| ~ U^{1 + delta0/2} x (typical |1 - L(s) M_u(s)|)`. The factor `U^{delta0/2}` is the
exact modulus of the root number factor (Sec. 1.1), so no Hoelder rearrangement removes it.

For `Re s = (1 + delta0)/2` the typical size of `1 - L M` for an optimal length-N approximant is at
least the prime tail `(sum_{p > N} p^{-1-delta0})^{1/2} ~ N^{-delta0/2}`. This uses the
orthogonality of `chi_u(p)` over the family (HEURISTIC as a lower bound; the matching upper bound is
the large sieve). Hence `kappa <= (1/2)(log N/log U) <= 1/2`. Since the Sec. 1.4 threshold is
`5/6 > 1/2`, **no scheme of this class can improve sigma0 below 6/7** under Gram 0, at any floor
height. A k-th order Neumann expansion evades the barrier only through *signed* control of
`k`-fold products of L-values over all rows, which is a ratios/mollified-moment input.

## 5. The smallest statement

### 5.1 FB#(delta0, kappa) (OPEN; CONDITIONAL use)

For a fixed floor height `delta0 in (0, 1/2]`, put `a0 = (1 + delta0)/2`. Let `B_F` be the bin of
retained rows with no zero of any presentation in `X_u` in `Re >= a0 + 2e`, `|Im| <= 3(i+1)T1`
(Lemma 8.1 with floor `a0`). For every primitive target `eta`, every dyad `U = Z^d` with
`d in [d_*, h + zeta]` (top dyads; `d_* < h` set by the slope), uniformly at the retained points
`Re s = a0 + 16e`, `Re w = 1 - a0 - 6e`, `Re z = 17/50`, `|Im| <= c T1`:

  `| sum_{u in B_F} xi(u) q_u^{-z} L^S(w, chi_.(u)) H_{eta,u}(s,w,z) / L^S(s, eta chi_.(u)) |`
  `<<_eta U^{1 + delta0/2 - kappa delta0 - z0 + eps} Z^{ell(z0 - 1/2) + delta0 ell/2 + eps} (1 + T1)^{A_eta}`.

An integrated form (against the Mellin weights over the retained box) suffices.

**Consequence (PROPOSED, CONDITIONAL on ARCH, Gram 0 as in O3, DH-rows above `delta0`, and
FB#(delta0, kappa)):** zero-freeness in `Re s > sigma0(delta0, kappa)` of the Sec. 1.4 formula.
In particular:

* `kappa = 1`, `delta0 = 1/3`: **sigma0 = 28/33 = 0.848485**, geometry `(3/11, 6/11, 2/11)`;
* `kappa = 1`, `delta0 = 1/2`: **sigma0 = 38/45 = 0.844444**, which is the Gram-0 low-side wall;
* any `kappa > 5/6` gives a gain over 6/7; `kappa <= 5/6` gives none.

With the manuscript's Gram loss b/12 the same input gives **13/15** at best (flat for `kappa = 1`).
Below 13/15 one still needs NC(theta) and E\* (FLOOR_BIN_BARRIER Sec. 4).

### 5.2 How plausible is FB#? (HEURISTIC)

* *No diagonal.* `xi` is nonprincipal at `S`, so the ratios recipe has no first-part main term.
* *Gauss-sum bias.* The dual part carries `W(chi_u)`. With bias `U^{2/3}` for sextic Gauss sums,
  the dual contribution is `U^{2/3 + delta0/2}`. This is `<= U^{1 - delta0/2}` (kappa = 1) iff
  **delta0 <= 1/3**. Square-root behaviour (bias absent for this twist) would allow delta0 up to
  1/2.
* *Restriction to B_F.* Relative to a hypothetical full-family sum, the correction is
  `#NF x U^{delta0/2} = U^{1 - delta0 + delta0/2}` under DH. That is exactly the kappa = 1 target at
  every delta0. So kappa = 1 is the natural "the floor is no worse than a DH bin" strength:
  borderline, with only `eps`-room.
* So FB#(delta0, 1) is heuristically plausible for `delta0 < 1/3`, which gives `sigma0 -> 28/33` from
  above. That is the HEURISTIC edge of the floor-row route with Gram 0.

### 5.3 Reduced forms (what would prove FB# along the route of Sec. 2)

Along Sec. 2, `kappa = min(kappa_I, kappa_II, kappa_III)`. Each needs strictly more than 5/6:

* (G_kappa) with `kappa > 5/6`. OPEN.
* Term II needs signed control of the remainder, or a k-th order expansion with mollified
  2k-th moments of `1 - L M` saving `U^{-nu delta0}`, `nu > 5/3` (k = 2), together with twisted
  mollified moments of products of k + 1 L-values over all rows. OPEN, and the Sec. 4 barrier shows
  some such signed input is unavoidable.
* Term III needs `c (1 - 1/(2k) - 1/(2m)) > 5/6`.
  * DH counts (`c = 1`) need `1/(2k) + 1/(2m) < 1/6`, e.g. `k = m = 7`: a 14th moment of `L(w)`
    and `V <= U^{1/7}`.
  * PR 910's claimed `c = 3/2` (PR 910 eq. (6.7), not verified here) works with Lemma 18.1 alone
    (`k = 2`) once `m >= 3`: `(3/2)(3/4 - 1/6) = 7/8`. This forces `V <= U^{1/3}`, which lowers
    mu in Term II to `1/3`.

  Term III is therefore not the hard part. Term II is (Sec. 4).

## 6. Full-model check with the manuscript's row counts (EMPIRICAL)

`scripts/full_model_floor.py` reruns the float model of `threshold_calculus.py` (imported unchanged;
monkeypatched in memory) with Gram 0, the manuscript's row counts above the floor, a raised floor
`delta0` and floor saving `theta_F`. Results are in `results/full_zero_paper.log`; see the README for
the table. These are finite-grid Nelder-Mead values with a `2e-5` slack, not certificates.

## 7. Reproduction

```text
cd research/exploratory/qrh-2026-10/offense/O7_FLOOR_ROWS/scripts
python3 floor_rows_lp.py      # ~1 min, exact certificates
python3 floor_rows_scan.py    # ~2 min
python3 closed_forms.py       # seconds (sympy)
python3 full_model_floor.py zero paper 1/50 0 1/50 1/50 1/10 1/10 1/3 1/3   # ~1 min per point
```
