# Lane D — Derivations (density transfer, effective corollary audit, conditional theorem)

Setting: L-105062 §0. `Xi_k` real entire, parity `(-1)^k`, order ≤ 1, all zeros in
`|Im t| <= 1/2` (strip lemma, PROVED), square-variable genus-0 Hadamard product
(L-105062 §1): `Xi_k(t) = c t^m prod_nu (1 - t^2/tau_nu^2)`, absolutely and
locally uniformly on C, `sum |tau_nu|^{-2} < infinity`, `{±tau_nu}` = nonzero
zeros with multiplicity, one representative per ±-pair.

## D0. Complex partial-fraction layer (extension of [I-PF] off the real axis)

**Lemma D0.** For every `w in C` with `Xi_k(w) != 0`:
```
(Xi_k'/Xi_k)(w) = m/w + Sum_nu [ 1/(w - tau_nu) + 1/(w + tau_nu) ],
```
the ±-grouped sum absolutely convergent; moreover the IMAGINARY parts are
absolutely summable UNGROUPED:
`Sum_{zeta in Z(Xi_k)} |Im(1/(w - zeta))| <= (|Im w| + 1/2) Sum_zeta 1/|w-zeta|^2 < infinity`
(exponent of convergence of the zeros ≤ order ≤ 1 < 2, and `w` is at positive
distance from the zero set), so `Im (Xi_k'/Xi_k)(w) = Sum_zeta Im(1/(w-zeta))`
with any rearrangement.

Proof. Identical to L-105061 Lemma 2.1 with the compact `K ⊂ C \ Z(Xi_k)`
complex instead of real: partial products of the Hadamard product converge
locally uniformly on C, Weierstrass passes the log-derivative to the limit off
zeros, and `2w/(w^2 - tau^2) = 1/(w-tau) + 1/(w+tau)`. For the ungrouped
imaginary part: `|Im(1/(w-zeta))| = |Im w - Im zeta|/|w-zeta|^2 <=
(|Im w| + 1/2)/|w-zeta|^2` by the strip lemma, and `Sum 1/|w-zeta|^2 < infinity`
by the convergence exponent; absolute convergence licenses ungrouping and
regrouping of the imaginary part. QED.

## D1. ATTRACTION LEMMA (Jensen-disk confinement on the ladder)

Notation: the zero multiset of `Xi_k` = real zeros `{t_n}` (with mult; incl. the
origin with mult `m`) ∪ conjugate pairs `{zeta_j = x_j + i y_j, conj zeta_j}`
(`0 < y_j <= 1/2`; pairs at `±x_j` are distinct pairs; mult counted). The OPEN
JENSEN DISK of pair `j` is `D_j := {t : (Re t - x_j)^2 + (Im t)^2 < y_j^2}`.

**Lemma D1.** Let `w = u + iv` with `v != 0` be a zero of `Xi_{k+1}`. Then
EITHER `Xi_k(w) = 0` (and then `w` is a non-real zero of `Xi_k`, same location,
`Xi_{k+1}`-multiplicity = `Xi_k`-multiplicity − 1), OR there is a pair `j` of
`Xi_k` with `w in D_j`, i.e.
```
(u - x_j)^2 + v^2 < y_j^2   —   in particular  y_j > |v|  and  |u - x_j| < y_j <= 1/2.
```

Proof. By conjugation symmetry take `v > 0`. Assume `Xi_k(w) != 0`; then
`(Xi_k'/Xi_k)(w) = 0`, so `Im(Xi_k'/Xi_k)(w) = 0`. By Lemma D0, ungroup and
regroup the imaginary part as: origin+real-zero terms, and conjugate-pair terms.
For a real zero `t_n` (any sign): `Im(1/(w-t_n)) = -v/|w-t_n|^2 < 0`; origin
term `Im(m/w) = -mv/|w|^2 <= 0`. For a pair `j`:
```
Im[ 1/(w - zeta_j) + 1/(w - conj zeta_j) ]
  = (y_j - v)/|w - zeta_j|^2 - (y_j + v)/|w - conj zeta_j|^2
  = 2v [ (y_j^2 - v^2) - (u - x_j)^2 ] / ( |w - zeta_j|^2 |w - conj zeta_j|^2 ),
```
by the algebra `c1/(a+c1^2) - c2/(a+c2^2) = (c2-c1)(c1 c2 - a)/((a+c1^2)(a+c2^2))`
with `c1 = y_j - v`, `c2 = y_j + v`, `a = (u-x_j)^2` (note
`|w - zeta_j|^2 = a + c1^2`, `|w - conj zeta_j|^2 = a + c2^2`). Setting the
total to zero and dividing by `2v > 0`:
```
Sum_j m_j [ (y_j^2 - v^2) - (u - x_j)^2 ] / (|w-zeta_j|^2 |w-conj zeta_j|^2)
   = m/(2|w|^2) + (1/2) Sum_n m_n / |w - t_n|^2 .          (D1★)
```
The right side is STRICTLY positive: `Xi_k` has at least one real zero
(`N_k^r(T) >= N_0^r(T) - k -> infinity` by L-105062 Thm 3 iterated + Hardy's
theorem [EXTERNAL-CLASSICAL, already consumed by L-105062]). Hence at least one
term on the left is strictly positive: `(u-x_j)^2 + v^2 < y_j^2`. QED.

Remarks. (i) For polynomials this is Jensen's theorem on Jensen disks
[stated Jensen 1913, proved Walsh 1920 — EXTERNAL-CLASSICAL ancestry,
literature-unverified in-container]; the proof above is self-contained for the
ladder class modulo L-105062 §1, so nothing is consumed from the literature
here. (ii) The lemma re-proves the strip lemma for non-real derivative zeros
(disks have radius ≤ 1/2 centered on R) — consistency. (iii) It also re-proves
Laguerre–Pólya heredity qualitatively: no pairs at rung k ⇒ no non-real zeros
at rung k+1 except at multiple zeros, which are then real. (iv) Numeric
verification: `test_attraction.py` (400 random + 150 iterated-ladder polynomial
configs, 0 violations; max nonreal-zero disk occupancy observed 4) and
`test_t3_mp.py` (Xi-like truncated product of 30 true zeta ordinates + planted
pair (25, 0.4), 60 dps: exactly 4 non-real derivative zeros, all strictly
inside the planted disks, margin 0.106). RECORDED INCIDENT: float64 roots at
degree 63 produced 36 spurious "violations" at impossible heights (|Im| up to
11, excluded a priori by Gauss–Lucas); all vanish at 60 dps — high-precision
classification mandatory, same pattern as L-105063 §3's replay discipline.

## D2. Rung density transfer

Counts: `N_k(eta, T) := #{zeros of Xi_k : Im t >= eta, 0 < Re t <= T, mult}`
for `eta in (0, 1/2]`. (By conjugation the `|Im| >= eta` count is `2 N_k(eta,T)`
plus imaginary-axis zeros, which have `Re t = 0` and are excluded throughout,
as in all repo counts.)

**Lemma D2.0 (unit-window count, every rung).** For every `k` there is an
explicit `c_k` with
`n_k(u) := #{zeros of Xi_k : Re t in (u, u+1], mult} <= c_k log(u + 3)` for all
`u >= 0`. Proof: for `u >= max(T_k^{(1)}, a_k)` this is L-105062 §2.3's Fact-J
count verbatim (center `u + 1 - 4i`, radii (6, 21), lower bound Cor A.2, upper
bound the disk growth estimate): `n_k(u) <= (14 + k) log(u+2)`. For
`u < max(T_k^{(1)}, a_k)` the total count `N_k(max(T_k^{(1)}, a_k) + 1)` is a
finite number (zeros of a nonzero entire function in a compact); absorb it into
`c_k`. The constants inherit L-105062's tower-largeness in k — harmless at
fixed k (honesty: finite-height use for k >= 1 at small u is again vacuous;
only the asymptotic in T is claimed). QED.

**Theorem D2 (one-rung transfer).** For every `k >= 0` there is `C_k` with, for
all `T >= 1` and all `eta in (0, 1/2]`:
```
N_{k+1}(eta, T) <= N_k(eta, T) + C_k log(T + 3) * ( N_k(eta, T + 1) + 1 ).
```

Proof. Partition the counted zeros `w` (`Im w >= eta`, `0 < Re w <= T`, mult):
(i) `Xi_k(w) = 0`: `w` is a non-real zero of `Xi_k` at the same point with
`Xi_k`-mult `mu >= 2` and `Xi_{k+1}`-mult `mu - 1 < mu`; summing over such
sites contributes `<= N_k(eta, T)`.
(ii) `Xi_k(w) != 0`: by Lemma D1, `w in D_j` for some pair `j` of `Xi_k` with
`y_j > Im w >= eta` and `|x_j - Re w| < y_j <= 1/2`, so
`x_j in (-1/2, T + 1/2]`. Assign each such `w` (with its multiplicity) to one
such `j`. The number assigned to a fixed `j` is at most the number of
`Xi_{k+1}`-zeros in `D_j ⊂ {Re t in (x_j - 1/2, x_j + 1/2]}`, i.e.
`<= n_{k+1}(x_j - 1/2) + n_{k+1}(x_j) <= 2 c_{k+1} log(T + 3)`. The number of
admissible `j` is `<= N_k(eta, T + 1) + nu_k` where `nu_k :=` #pairs of `Xi_k`
with `x_j in (-1/2, 0]` `<=` #zeros of `Xi_k` with `|Re t| <= 1/2` — a finite
k-constant (parity mirrors them into `[0, 1/2)`). Absorb `nu_k` and constants:
total `(ii) <= C_k log(T+3)(N_k(eta, T+1) + 1)`. QED.

**Theorem D3 (o(T) density on every rung).** EXTERNAL-CLASSICAL input
[transcribed, literature-unverified in-container]: Selberg (1946):
`N(sigma, T) << T^{1 - (1/4)(sigma - 1/2)} log T` uniformly for
`1/2 <= sigma <= 1`; fallback Carlson (1920): `N(sigma,T) << T^{4 sigma (1 -
sigma) + eps}` — either suffices. Coordinate match (laneB1 §0): a zero of
`Xi_0` at `t` with `Im t >= eta` is a zeta zero `rho = beta + i gamma` with
`beta = 1/2 - Im t <= 1/2 - eta`, `gamma = Re t`; by `xi(s) = xi(1-s)` the
count equals the `beta >= 1/2 + eta` count: `N_0(eta, T) = N(1/2 + eta, T)`.
Then for every fixed `k >= 0`, `eta in (0, 1/2]`:
```
N_k(eta, T)  <=  prod_{j<k} (1 + 2 C_j log(T + k + 3)) * ( N_0(eta, T + k) + k )
             <<_{k, eta}  T^{1 - eta/4} (log T)^{k + 1}  =  o(T).
```
Proof: iterate D2 with `T`-arguments `T, T+1, ..., T+k` (each step's additive
`+1` absorbed into the product bound as displayed: from
`N_{j+1}(eta, S) <= (1 + C_j log(S+3))(N_j(eta, S+1) + 1)`), then the base
case. QED.

This beats the trivial `N_k(eta,T) <= N_k(T) ~ T log T/2pi` by the power
saving; it is the "high zeros of high derivatives need off-line zeros of zeta
itself" transfer, with a log-factor toll per rung.

**Corollary D4 (verified-height propagation, effective, unconditional given a
zero verification).** If `Xi_0` has no non-real zeros with `|Re t| <= X`
(equivalently: every zeta zero with `|gamma| <= X` is on the critical line —
the classical verification input, EXTERNAL at whatever height is certified;
the repo's own X-105061/laneB1 winding counts certify small X in-container),
then for every `k >= 0`, `Xi_k` has no non-real zeros with
`|Re t| <= X - k/2`. Proof: induction. A non-real zero `w` of `Xi_{k+1}` with
`|Re w| <= X - (k+1)/2` is (D1) either a non-real zero of `Xi_k` at the same
point — excluded by induction since `X - (k+1)/2 <= X - k/2` — or lies in a
disk `D_j` of a `Xi_k`-pair with `|x_j| < |Re w| + 1/2 <= X - k/2` — excluded
by induction. QED.
(Loss exactly 1/2 per rung; with the classical verification height
`X ~ 3 * 10^{12}` [EXTERNAL, literature-unverified] the ladder is non-real-free
essentially to that height on every fixed rung. This is deliverable 2's honest
salvage — see D6.)

## D5. Weight localization: high pairs carry o(N_0) of W_k

**Lemma D5.0 (Rolle gap-doubling).** [Hostile-review completion: the doubling
clause below omits the degenerate case where the produced zero of the
derivative coincides with a single midpoint zero; it closes in three lines
via closedness of the real zero set — if the candidate interval contained no
other zero, the midpoint zero would be isolated at distance exactly half the
gap on both sides, and the Rolle argument re-run on either half-interval
produces a distinct zero, contradiction.] Let `u < u'` be consecutive distinct real
zeros of `Xi_{k+1}`. Then the open interval `(u, u')` contains at most one
distinct real zero of `Xi_k`. Consequently, if every interval of length `L`
inside `[A - 3L, B + 3L]` contains a real zero of `Xi_k`, then every interval
of length `2L` inside `[A, B]` contains a real zero of `Xi_{k+1}`; iterating,
`maxgap_{k}([T, 2T]) <= 2^k maxgap_0([T/2, 3T])` for `T` large (crude but
sufficient). Proof of the first claim: two distinct `Xi_k`-zeros
`t < t'` in `(u, u')` give (L-105062 Thm 3) a real `Xi_{k+1}`-zero in
`(t, t') ⊂ (u, u')`, contradicting consecutiveness. QED.

EXTERNAL-CLASSICAL input [transcribed, literature-unverified]: Hardy–
Littlewood (1921): for every `eps > 0` and `X` large, `zeta` has a
critical-line zero in `[X, X + X^{1/4 + eps}]`; hence
`maxgap_0([T/2, 3T]) << T^{1/4 + eps}` and by D5.0
`maxgap_k([T, 2T]) <<_k T^{1/4 + eps}`. In particular the right endpoint `b`
of the T-overhanging gap of `Xi_k` satisfies `b <= T + O_k(T^{1/4+eps}) <= 2T`
for `T >= T_k^{gap}`.

**Theorem D5 (localization).** Fix `k >= 0`, `eta in (0, 1/2]`. Define
`W_k^{high(eta)}(T)` := the sub-sum of `W_k(T)` (T-105060 §2) restricted to
pairs with `y_j >= eta`. Then
```
W_k^{high(eta)}(T) <= (c_k log(2T+3) + 1) * ( N_k(eta, 2T+1) + nu_k )
                   <<_{k, eta} T^{1 - eta/4} (log T)^{k+2} = o(N_0(T)),
```
hence `w_k = limsup W_k / N_0` is UNCHANGED if `W_k` is restricted to pairs
with `y_j < eta`. Consequently `w_k` — the entire open burden of the descent
ladder T-105060 — is carried by near-real pairs: for every `eta > 0`, only
pairs with `y_j < eta` matter asymptotically.

Proof. Each pair `j` with `y_j >= eta` contributes, per overhung gap, weight
`min(1, g^2/4y_j^2) <= 1`; the gaps it overhangs all meet the open interval
`I_j = (x_j - y_j, x_j + y_j)` of length `2 y_j <= 1`, and an interval meeting
`r` distinct real zeros meets at most `r + 1` gaps, so the number of gaps
overhung is `<= n_k^r(I_j) + 1 <= c_k log(|x_j| + 3) + 1` (Lemma D2.0). Which
pairs can appear? A gap `G = (a, b)` in the list `𝒢_k(T)` has `a < T`; the
overhang condition requires `x_j - y_j < b`. For every gap except the
T-overhanging one, `b <= T` so `x_j <= T + 1/2`; for the T-overhanging gap,
`b <= 2T` (D5.0 + Hardy–Littlewood, `T >= T_k^{gap}`) so `x_j <= 2T + 1/2`.
Pairs with `x_j > 0` and `y_j >= eta` number `<= N_k(eta, 2T + 1)`; mirrored
pairs (`x_j <= 0`) can only overhang gaps meeting `(0, T]` if `x_j > -1/2`
(such gaps have `a >= 0`... more precisely `a >= 0` since gaps are components
of `R minus` the FULL symmetric real-zero set and those meeting `(0,T]` with
`a < 0` are the origin gap, `|a| = t_1 <= first zero`, absorbed in `nu_k`
pairs with `x_j >= -t_1 - 1/2` — a finite k-constant). Multiply and apply D3.
QED.

(Sanity: this does NOT bound `w_k` — near-real pairs with `y_j < eta` can
still carry unbounded weight; it localizes the problem, complementing
[THRESHOLD] which says near-real pairs are exactly the ones whose per-gap
weight saturates at 1.)

## D-Littlewood (route (a) assessed — honest record)

Littlewood's lemma on `[0,T] x [eta, 1]` with the height-1 line integral
computable via Sub-lemma A (the `Im t = -1` line is `Re s = 3/2`, right of the
strip; conjugate symmetry handles `+1`) gives
`int_eta^1 N_k(sigma', T) dsigma' = (1/2pi)[int_0^T log|Xi_k(t + i eta)| dt -
int_0^T log|Xi_k(t - i)| dt] + O_k(log T)`-type identities. The height-1
integral has main term `int log|xi(3/2 + ix)| dx + k int log|ell| + O(T)`,
computable. The `eta`-line integral admits an UPPER bound with the SAME
Stirling main term plus `O(T)` (growth bounds), so the difference is `O_k(T)`
and one gets at best `N_k(eta', T) <= O_k(T)/(eta' - eta)` — i.e. `<< T/eta`:
beats `T log T` by one log only. Route (b) (Theorems D2/D3) is strictly
stronger (`o(T)` with power saving), so route (a) was NOT completed beyond
this assessment; no claim is deposited from it. (Recorded so successors do not
re-attempt it expecting more.)

## D6. Deliverable 2 — the census exclusion form is VACUOUS (honest audit)

Question posed: does the X-105061 census (`extra(G) = 0` for all gaps below
`T_0 = 500`) yield an EXCLUSION REGION for off-line zeta zeros via dipole
geometry? ANSWER: NO. The proved threshold (L-105061 Lemma 3.3) runs
`extra >= 1 ==> weight >= 1`; its contrapositive constrains gaps with LOW
weight, and observing `extra = 0` constrains NOTHING about pairs. The missing
converse — "a deep pair FORCES extra critical zeros" — is FALSE:
counterexample family `F = (t^2 - 1)(t^2 + a^2)`, `a > 1`: pair `(0, a)`
present with overhang weight `min(1, 4/(4a^2)) = 1/a^2 < 1`, yet
`F' = 2t(2t^2 + a^2 - 1)` has exactly the one Rolle-forced real zero in the
gap `(-1, 1)`: `extra = 0` (verified, test_attraction.py T4, a = 2, weight
1/4). Differentiation can even REALIZE pairs silently (`t^2 + 1 -> 2t`: pair
gone, no real-zero surplus anywhere). So `X_k(T_0) = 0` implies no constraint
on off-line zeros, and the census methodology's only exclusion content is its
embedded total-count (winding) verification — equivalent to classical zero
verification, nothing new. DELIVERABLE 2'S EXCLUSION FORM IS DROPPED.

SALVAGE (what IS true and effective at finite height): Corollary D4. Given the
classical verification height `X` (no off-line zeta zeros to height `X`),
every rung `Xi_k` is non-real-zero-free for `|Re t| <= X - k/2`,
unconditionally, with loss exactly `1/2` per rung. This converts the census's
OBSERVED all-real behavior at `T <= 500`, `k <= 3` from data into a theorem
(any in-container verification to height 500 + D4 covers `k <= 3` to height
498.5), and scales to the literature height. Direction of information flow:
rung 0 upward — the census cannot flow information downward to zeta.

## D7. Deliverable 3 — the repulsion-conditional proportion theorem (draft)

Mean real gap: `gbar(x) := 2pi / log(x/2pi)` for `x > 2pi e` (RvM on every
rung, L-105062 Cor 2.1).

**Hypothesis PR(theta, eps; K, eta)** ("near-line pair repulsion at exponent
theta"): `theta in [0,1)`, `eps > 0`, `K in N`, `eta in (0, 1/2]`: there is
`T*` such that for every `k <= K`, every `lambda >= 1`, and all `T >= T*`:
```
P_k(lambda; T) := #{pairs (x_j, y_j) of Xi_k, mult : x_j in (0, T],
                    y_j <= min(lambda * gbar(x_j), eta)}  <=  eps * lambda^theta * N_k(T).
```
(Only the range `y_j <= eta` is hypothesized — D3/D5 discharge `y_j > eta`
unconditionally. RH would give `P_k = 0`; PR is strictly weaker.)

**Interface [I-W] (lane W compression, ASSUMED — exact pinned form):** there
are constants `C_1, C_2, T_W` such that for all `k <= K`, `T >= T_W`:
```
W_k(T) <= C_1 * P_k(1; T') + C_2 * Sum_{pairs: gbar(x_j) < y_j <= eta, x_j <= T'} gbar(x_j)/y_j
          + W_k^{high(eta)}(T) + o(N_0(T)),      T' := 2T + 1.
```

**Theorem D7 (conditional).** Assume (i) [I-DIPOLE] with per-rung constants
`A'_k` (proved `= max(6, 2k)` on the L-105063 regimes; ASSUMED on the residual
regimes R-C1/R-C2), (ii) [I-W], (iii) PR(theta, eps; K, eta), and
EXTERNAL-CLASSICAL (iv) Conrey 1983 (`kappa_k -> 1`), (v) Selberg 1946
density (through Theorem D3), (vi) Hardy–Littlewood 1921 gaps (through D5).
Then for every `K' <= K - 1`... precisely: for every `K` as in PR,
```
1 - kappa_0 <= (1 - kappa_{K+1}) + (6 + 2K) * C(theta) * (C_1 + C_2) * eps * (K + 1),
      C(theta) := 2 * (1 + 2^theta / (1 - 2^{theta - 1}))
      [hostile-review fix: the factor 2 the proof requires was missing from
      this display; T-105065 §2(a) already carries the correct form].
```
If moreover PR(theta, eps; K(eps), eta) holds for EVERY eps > 0 with
`K(eps) -> infinity` chosen so that `1 - kappa_{K(eps)+1} <= eps` (possible by
(iv)) and `(6 + 2K(eps)) * (K(eps) + 1) * eps -> 0`, then `kappa_0 = 1`:
100% of zeta's zeros lie ON the critical line (asymptotic proportion — NOT
RH; RH would need every zero, and nothing here addresses it).

Proof. Fix `k <= K`. Bound `w_k`: by [I-W], the first term is
`<= C_1 eps N_k(T)` (PR at `lambda = 1`). Second term, dyadically over
`lambda in [2^m, 2^{m+1})`, `m >= 0`, up to `2^M gbar ~ eta`: each pair in
band `m` contributes `gbar/y <= 2^{-m}`, and the band count is
`<= P_k(2^{m+1}; T') <= eps 2^{(m+1)theta} N_k(T')`; summing,
`<= eps N_k(T') * 2^theta Sum_m 2^{m(theta-1)} = eps N_k(T') * 2^theta/(1 -
2^{theta-1})`. Third term: `o(N_0(T))` by Theorem D5. Divide by `N_0(T)`,
limsup, using `N_k(T')/N_0(T) -> 2` — wait: `N_k(2T+1)/N_0(T) -> 2T log 2T /
(T log T) -> 2`. So
`w_k <= 2 C(theta) (C_1 + C_2) eps` (the constant 2 absorbed into C(theta):
redefine `C(theta) := 2(1 + 2^theta/(1-2^{theta-1}))`). By T-105060(c) with
per-rung `A'_k <= 6 + 2K` for `k <= K`:
`1 - kappa_0 <= (1 - kappa_{K+1}) + Sum_{k<=K} A'_k w_k
 <= (1 - kappa_{K+1}) + (6 + 2K)(K+1) * C(theta)(C_1+C_2) eps`. QED.

HONESTY: (a) three assumed layers ([I-DIPOLE]-residual, [I-W], PR) — this is a
CONDITIONAL theorem whose value is the exact interface algebra; (b) the
`(K^2 eps)`-shape means PR must supply eps decaying faster than `K^{-2}` along
the Conrey sequence — a quantitative Conrey rate (his kappa_K explicit) would
make the trade-off explicit; (c) `kappa_0 = 1` is NOT RH; (d) no circularity:
PR concerns pair heights `y_j` (vertical), the conclusion concerns the real
proportion; D3 consumed only classical zeta density.
