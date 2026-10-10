# Lane W PLAN (weight-compression lemma, L-105064 draft)
1. Read deposited context: T-105060, L-105061..63, laneB1/B3 notes; extract exact W_k def.
2. Fix notation: pair p=(x,y), interval I_p=(x-y,x+y), gaps = bounded components of R\Z_real.
3. Prove absolute bound omega(p) <= C_omega (interval combinatorics + min-cap); find sharp C_omega.
4. Adversarial cases: giant gap containing I_p; cluster of tiny gaps; edge gaps; multiplicity m_p.
5. Refined bound: omega(p) <= 2*min(1,(g_edge/2y)^2-ish) + sum over interior; state in actual local gaps.
6. Corollary under a-priori max-gap bound: omega(p) <= C' * min(1, Gmax_local/y).
7. Numeric checks: synthetic configs + X-105061 zeros.json gap census.
8. Bookkeeping: W_k(T) <= C_omega * P_k(T+1/2) + edge terms; check T-window carefully.
9. Honest constants analysis: two-rung machine, A'C_omega < 1 question; record failure if vacuous.
10. Write L-105064-draft.md deposit-grade; final message: STATEMENTS PROVED first.

## D1. Setup and structure lemma
F = Xi_k. Real zeros = closed discrete set Z (unbounded both sides; all gap
components bounded, per L-105061 S1). Gaps = bounded connected components of
R\Z, pairwise disjoint open intervals. Pair p = (x,y), 0 < y <= 1/2 (strip),
distinct-pair multiplicity m_p. I_p := (x-y, x+y), |I_p| = 2y.
Overhang (deposited convention, L-105061 S1): p overhangs G=(a,b) iff
x-y < b and x+y > a  <=>  I_p and G intersect as OPEN intervals.
Per-pair total weight (multiplicity-free; W charges m_p * omega):
  omega(p) := Sum_{gaps G : G cap I_p != empty} min(1, |G|^2/(4y^2)).
NOTE min(1, u^2) = (min(1,u))^2 for u>=0; write q(G) := min(1, |G|/(2y)),
so each term = q(G)^2.

**Lemma W1 (run structure).** The gaps meeting I_p form a finite consecutive
run G_1 < ... < G_r (r >= 0). Classify: G is CONTAINED if G subset I_p,
PROTRUDING otherwise. Then (i) at most two overhung gaps are protruding;
(ii) the contained gaps are disjoint subintervals of I_p, so
Sum_{contained} |G_i| <= 2y.
Proof. Finiteness: all overhung gaps lie in the bounded interval
(x-y-sup g, x+y+sup g)? Cleaner: each overhung gap contains a point of I_p;
gaps are disjoint; each gap meeting I_p either contains one of the two points
x-y+j*delta... Standard: Z cap [x-3y, x+3y] is finite (discrete + compact),
and every overhung gap has closure meeting cl(I_p), with endpoints in
Z cup {}; the overhung gaps have pairwise disjoint nonempty intersections
with I_p; each such intersection is a maximal subinterval of I_p \ Z, and
I_p \ Z has finitely many components (Z cap cl(I_p) finite). So r is finite
and the overhung gaps are exactly the gaps containing the components of
I_p \ Z — consecutive. (i): G = (a,b) protruding means G not subset I_p and
G cap I_p != empty: then a < x-y or b > x+y; if a < x-y then, since b > x-y
(nonempty intersection), the point x-y lies in (a,b), i.e. G contains x-y;
similarly b > x+y forces x+y in G. Gaps are disjoint, so at most one gap
contains x-y and at most one contains x+y: at most two protruding (one gap
containing both endpoints — the giant-gap case G superset I_p — is a single
gap, r = 1). (ii): contained gaps are disjoint open subsets of I_p; total
length <= |I_p| = 2y. QED.

**Lemma W2 (pointwise weight compression).** Let
g_max(p) := max{|G| : G overhung by p} (0 if r = 0) and
mu_p := min(1, g_max(p)/(2y)). Then
  omega(p) <= mu_p + 2 mu_p^2 <= 3 mu_p <= 3.
Proof. Each protruding gap contributes q(G)^2 <= mu_p^2; at most two of them
(W1(i)): protruding total <= 2 mu_p^2. Contained gaps: q(G_i)^2 <=
(|G_i|/2y) * q(G_i) <= (|G_i|/2y) * mu_p, and summing with W1(ii):
contained total <= mu_p * (Sum |G_i|)/(2y) <= mu_p. Add. The chains
mu + 2mu^2 <= 3mu (mu <= 1) and 3mu <= 3 are trivial. QED.

**Remarks.** (a) Absolute constant C_omega = 3 — every pair carries total
weight < 3 across ALL gaps it overhangs, regardless of how many (a pair
overhanging six gaps, L-105061's adversarial config, is charged once per gap
yet totals < 3). (b) Adversarial checks: giant gap superset I_p: r = 1,
omega = q^2 <= 1 <= bound. Cluster of n tiny contained gaps of length g:
omega = n g^2/4y^2 <= (ng/2y)*(g/2y) <= g/2y = mu (since ng <= 2y). (c) The
constant 3 is SHARP as a supremum: G_1 = (x-y-L, x-y+eps),
G_2 = (x-y+eps, x+y-eps), G_3 = (x+y-eps, x+y+L), L >= 2y: omega =
1 + ((2y-2eps)/2y)^2 + 1 -> 3 as eps -> 0; and omega < 3 always (a contained
gap has length < 2y strictly when r >= 2, protruding q^2 = 1 needs the gap
to exist). (d) mu + 2mu^2 is sharp in BOTH regimes: mu = 1 family above
(value 3); small mu: n = 2y/g equal contained gaps of length g = g_max give
contained part -> mu, two protruding length-g gaps give 2mu^2. (e) Strict
subadditivity used nowhere; no averaging assumption; actual local gaps only.

## D2. Global compression: W_k dominated by the off-line count
Notation of L-105062/T-105060: N_k, N_k^r, N_k^c on (0,T] with mult;
gap list Gcal_k(T) = gaps meeting (0,T]; t_1 = t_1(k) = smallest positive
real zero of Xi_k; b_T = b_k(T) = smallest real zero > T (exists: real zeros
unbounded above). W_k(T) = Sum_{G in Gcal_k(T)} Sum_{p overhanging G} m_p q(G)^2.

**Lemma W3 (localization of charged pairs).** Every gap in Gcal_k(T) is
contained in (-t_1, b_T]. Hence any pair overhanging some G in Gcal_k(T) has
  x_p + y_p > -t_1  and  x_p - y_p < b_T,  i.e.  x_p in (-t_1 - 1/2, b_T + 1/2)
(using y_p <= 1/2, strip lemma).
Proof. G = (a,b) meets (0,T]: b > 0 and a <= T (if a > T then G cap (0,T]
empty). b > T would force, since (a,b) is zero-free and a <= T, that b is the
first zero above T: b = b_T. So b <= b_T always. If a < 0: 0 in cl(G); for k
even 0 is not a zero (or is it? if Xi_k(0)=0 the gaps abut 0) — in either
case a zero-free open interval containing negative points with b > 0 must
contain 0 or abut it, and its left endpoint is a zero or -infty; boundedness
gives a in Z, a >= -t_1 by symmetry of Z (parity (-1)^k: Z = -Z), since
(a, b) zero-free and -t_1 < 0 < t_1 are the innermost zeros: a >= -t_1.
So G subset (-t_1, b_T]. Overhang x-y < b <= b_T, x+y > a >= -t_1. QED.

**Theorem W4 (global compression).** For every k >= 0 and T > 0:
  W_k(T) <= Sum_{pairs p : x_p in (-t_1-1/2, b_T+1/2)} m_p (mu_p + 2 mu_p^2)
        <= 3 * #{those pairs, mult}
        <= (3/2) N_k^c(b_T + 1/2) + c_k^0,
  c_k^0 := (3/2) N_k^c(t_1 + 1/2) + 3 P_k^0  (finite, T-independent),
P_k^0 = number of purely imaginary pairs (mult). In particular W_k is
dominated by the OFF-LINE ZERO COUNT up to height b_k(T) + 1/2.
Proof. Interchange the (absolutely convergent, nonneg, finite) double sum:
W_k(T) = Sum_p m_p Sum_{G in Gcal_k(T) overhung by p} q(G)^2
      <= Sum_{p charged} m_p omega(p)   [inner sum over a SUBSET of all
overhung gaps of p — dropping gaps outside Gcal_k(T) only helps]
      <= Sum_{p charged} m_p (mu_p + 2mu_p^2)   [Lemma W2]
      <= 3 Sum_{p charged} m_p            [mu_p <= 1].
Charged pairs have x_p in (-t_1 - 1/2, b_T + 1/2) (W3). Count with mult:
x_p in (0, b_T + 1/2]: N_k^c(b_T+1/2)/2 pairs (each pair at x>0 = two
strip zeros of Re in (0,T']); x_p = 0: P_k^0; x_p in (-t_1-1/2, 0): mirrors
of x_p in (0, t_1+1/2) by parity: N_k^c(t_1+1/2)/2. Both correction terms
finite (zeros of an entire function in a compact set). QED.

**Trap honored (T-105060 S2):** no unconditional bound on b_T - T exists at
every rung — the T-overhanging gap may be long; W4 is stated at the honest
argument b_T + 1/2, NOT T + 1. The orchestrator sketch's "N_k^c(T+1)" is
UNSUPPORTED as stated; it holds iff b_T <= T + 1/2. Corrected below via a
density argument: b_T = O(T) given any positive liminf real-zero proportion.

**Lemma W5 (b_T = O(T) from a positive real-zero proportion).** Suppose
kappa_k := liminf_T N_k^r(T)/N_k(T) >= c > 0. Then
b_k(T) <= (1/c + o(1)) T as T -> infinity.
Proof. Fix eps in (0, c); S_0 with N_k^r(S) >= (c-eps) N_k(S) for S >= S_0.
For T >= S_0: no real zeros in (T, b_T), so for every S in [T, b_T):
N_k^r(S) = N_k^r(T) <= N_k(T). Apply at S up to b_T-:
(c-eps) N_k(b_T-) <= N_k(T). RvM on rung k (L-105062 Cor 2.1):
N_k(S) = (S/2pi)log(S/2pi) - S/2pi + O_k(log S). So
b_T log(b_T/2pi) <= (1/(c-eps))(1+o(1)) T log(T/2pi); since b_T > T,
log(b_T/2pi) >= log(T/2pi), whence b_T <= (1/(c-eps))(1+o(1)) T. QED.
Sources for c: k = 0: EXTERNAL-CLASSICAL Levinson 1974, c = 0.34 (any
classical value); every k >= 0: repo-internal L-105062 S6, c = 0.6725007...
MODULO the Z23-UPSTREAM import row's status; k large: Conrey 1983 (already
consumed by T-105060(d)) gives c -> 1.

## D3. What the compression buys (honest analysis)
**Corollary W6 (normalized).** Assume kappa_k >= c > 0 (sources in W5). Then
  w_k := limsup_T W_k(T)/N_0(T) <= (3/(2c)) * (1 - kappa_k).
Proof. Fix eps>0 small. W4: W_k(T) <= (3/2)N_k^c(S_T) + c_k^0, S_T := b_T+1/2.
S_T > T -> infinity. limsup defn: for large S, N_k^c(S) <= (1-kappa_k+eps)N_k(S)
[limsup N_k^c/N_k = 1 - liminf N_k^r/N_k = 1-kappa_k]. W5: S_T <= (1/c+eps)T
eventually, so log S_T <= (1+eps)log T and RvM on rungs k and 0:
N_k(S_T)/N_0(T) <= (1+eps)^3 (S_T log S_T)/(T log T) <= (1+eps)^5/c.
Multiply, let eps -> 0. QED.
NOTE: 1/c loss is REAL in this route — b_T can be ~T/c late in a long gap.
With c = 0.6725 (repo-internal, modulo Z23 import): w_k <= 2.2305(1-kappa_k).
With c -> 1 (Conrey, large k): w_k <= (3/2+o_k(1))(1-kappa_k).

**Check of orchestrator's fear (1) — direct feed into descent (b) is WRONG
DIRECTION.** (b): N_k^c <= N_{k+1}^c + A' W_k + A_k log T + B_k'. Feeding
W_k <= (3/2)N_k^c(S_T) + c^0 gives N_k^c(T) <= N_{k+1}^c(T) +
(3A'/2)N_k^c(S_T) + ..., and 3A'/2 >= 9 > 1 with S_T >= T: SELF-REFERENTIAL,
VACUOUS. Confirmed: the compression pays ONLY in the normalized master.

**Two-rung machine (Corollary W7).** T-105060(c) with K=0:
1-kappa_0 <= (1-kappa_1) + A' w_0 <= (1-kappa_1) + A'(3/(2c_0))(1-kappa_0).
IF theta := 3A'/(2 c_0) < 1:  kappa_0 >= 1 - (1-kappa_1)/(1-theta)
— a machine converting any rung-1 bound into a rung-0 bound, loss 1/(1-theta).
CONSTANTS LEDGER (honest): need A' < 2c_0/3.
  c_0 = 0.6725 (modulo import): need A' < 0.4483.
  c_0 = 0.4149 (Pratt-Robles-Zaharescu class., unverified): need A' < 0.2766.
Proved regime constant A' = 6: theta = 13.4 (c=0.6725) — FAILS by ~13.4x (the earlier "~30x" figure was the Levinson c = 0.34 value; hostile-review consistency fix).
Conjectured sharp A' = 2: theta = 4.46 — FAILS by ~4.5x (at c = 0.6725; hostile-review consistency fix).
Even a hypothetical A' = 1 with C_omega = 3 and NO 1/c loss (i.e. b_T ~ T):
theta = 3/2 — STILL FAILS. Conclusion: the ABSOLUTE compression constant 3
cannot close the two-rung loop for ANY plausible A'; C_omega = 3 is sharp
pointwise (D1 sup family), so improvement must come from the AVERAGE of
omega over pairs — i.e. from the refined bound mu_p + 2mu_p^2: the machine
closes iff hypothetical off-line zeros are predominantly HIGH (y >> local
gaps), since high pairs carry vanishing weight. That is a zero-distribution
statement, not combinatorics; recorded as the open successor target.

**All-K master feed (Corollary W8).** T-105060(d) + W6:
1-kappa_0 <= A' Sum_k w_k <= (3A'/2) Sum_k (1-kappa_k)/c_k. With c_k >=
c* = 0.6725 (modulo import) the series converges IFF Sum(1-kappa_k) < inf —
Conrey's QUANTITATIVE rate (reported 1 - kappa_k = O(1/k^2)-type;
literature-unverified in-container) would give convergence; but the k=0 term
alone is (3A'/2c*)(1-kappa_0) with coefficient >> 1: the inequality is
SELF-REFERENTIAL AND VACUOUS as a bound on 1-kappa_0. Verdict: W6+(d) turns
"Sum w_k < infinity" from OPEN into TRUE-modulo-(quantitative Conrey +
import row) — i.e. the master corollary's hypothesis is now plausibly
DISCHARGED — but the resulting numerical inequality has no content until
the product A' * C_avg < 1. The compression's real yield: (i) w_k < infinity
for every k (unconditional given any c_k > 0 — new: previously not even
finiteness was known, T-105060 S6.1); (ii) w_k -> 0 as k -> infinity
(via Conrey qualitative); (iii) the target functional is now a pure
off-line-zero statistic: W_k <= Sum_p m_p (mu_p + 2 mu_p^2).
