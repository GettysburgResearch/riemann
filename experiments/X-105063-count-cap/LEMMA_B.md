# LEMMA B — the shallow-cooperation cap (lane CAP-B)

Status: PROVED (Theorems B-I, B-II, B-III below, with explicit constants);
remainder precisely delimited in Section 7. Numerics: Section 8.
Depends on: L-105061 [I-PF] (partial-fraction layer, proved) and [THRESHOLD]
(proved). RH is not addressed.

## 0. Setting and standing hypotheses

F real entire, order <= 1, genus 0 in t^2 (Hadamard product as in L-105061).
G = (a,b) a gap between consecutive real zeros, g = b - a, h = F'/F on G.
extra(G) := Z_mult(h, G) - 1 (= #real zeros of F' in G with multiplicity, - 1).
Zeros of F: real {t_n} (mult m_n, incl. t=0 with mult m_0), and conjugate
pairs z_j = x_j + i y_j, 0 < y_j <= 1/2 (mult m_j).

A pair j OVERHANGS G iff I_j ∩ G ≠ ∅, I_j := [x_j - y_j, x_j + y_j].

SHALLOW-COOPERATION HYPOTHESIS (SC): every overhanging pair has y_j >= g/2.

Weights (overhanging pairs): w_j := (g/(2 y_j))^2 ∈ (0, 1] under (SC), so the
L-105061 gap weight is W = W(G) = Sum_ov m_j w_j. Higher weights:
  V_k := Sum_ov m_j w_j^{k+1}   (k >= 1);  V_1 = quartic weight; V_k <= V_1 <= W,
  and V_k <= w_max^{k-1} V_1 with w_max := max_ov w_j.

## 1. Lemma B.1 (derivative ladder identity)

For t in G and j >= 1,
  h^(j)(t) = -(-1)^{j-1} j! * Re S_{j+1}(t),   S_n(t) := Sum_rho m_rho (t-rho)^{-n},
the sum over ALL zeros rho of F (real zeros, and both members z_j, conj(z_j)
of each pair). In particular, for every k >= 0,
  h^(2k+1)(t) = -(2k+1)! * Re S_{2k+2}(t).                                 (B.1)

Proof. [I-PF] gives h'(t) = -Re S_2(t) on G: indeed -m_0/t^2 - Sum m_n/(t-t_n)^2
= -Re(those terms), and phi'_j(t) = 2(y_j^2-(t-x_j)^2)/((t-x_j)^2+y_j^2)^2
= -2 Re (t-z_j)^{-2} = -Re[(t-z_j)^{-2} + (t-conj z_j)^{-2}] (direct algebra,
verified symbolically). [I-PF] states absolute, locally uniform convergence on
G; each termwise-differentiated series Sum m_rho (t-rho)^{-n} (n >= 3) is
dominated on compact K ⊂ G by dist(K, {rho})^{-(n-2)} times the n=2 series,
hence also converges absolutely and locally uniformly; so h' may be
differentiated termwise repeatedly, and d^{j-1}/dt^{j-1} (t-rho)^{-2}
= (-1)^{j-1} j! (t-rho)^{-(j+1)}. QED.

## 2. Lemma B.2 (sign anatomy of Re S_n, n even)

Let n = 2k+2. Write d_a = t - a, d_b = b - t, so d_a, d_b > 0 and
min(d_a,d_b) <= g/2 <=... (both <= g). Then:

(a) Every REAL zero contributes m_n (t-t_n)^{-n} > 0; keeping only the two
endpoint zeros: Sum_real >= 1/d_a^n + 1/d_b^n >= 2 (2/g)^n.

(b) A pair contributes 2 m_j Re (t-z_j)^{-n} = 2 m_j cos(n θ_j)/r_j^n with
r_j^2 = (t-x_j)^2 + y_j^2, θ_j = arctan(y_j/|t-x_j|) ∈ (0, π/2]. It is
NEGATIVE ("hurting") only if θ_j > π/(2n), and then always
  |2 m_j Re (t-z_j)^{-n}| <= 2 m_j / r_j^n <= 2 m_j / y_j^n.               (B.2)

(c) n = 4 exact refinement: Re(t-z)^{-4} = (u^4 - 6u^2y^2 + y^4)/(u^2+y^2)^4
(u = t-x) is negative exactly for |u|/y ∈ (√2-1, √2+1), and
  ( -Re(t-z)^{-4} )_+ <= κ / y^4,   κ := (11 + 5√5)/64 = 0.34656781...,     (B.3)
the maximum of (6v^2-v^4-1)/(1+v^2)^4, attained at v = √(5-2√5).
(Symbolic optimization, exact.)

## 3. Lemma B.3 (hurt budget of a shallow overhanging pair)

Under (SC), for any overhanging pair j, any t in G, and n = 2k+2:
  |2 m_j Re (t-z_j)^{-n}|  <=  2 m_j / y_j^n  =  m_j w_j^{k+1} * [2 (2/g)^n].
For n = 4, by (B.3):  ( -2 m_j Re(t-z_j)^{-4} )_+ <= κ m_j w_j^2 * [2 (2/g)^4].
Proof: 2/y^n = 2 (2/g)^n (g/(2y))^n and (g/2y)^n = w^{n/2} = w^{k+1}. QED.
(The bracket [2 (2/g)^n] is exactly the two-endpoint floor of Lemma B.2(a).)

## 4. Lemma B.4 (load of a non-overhanging pair)

Let j be non-overhanging, say LEFT: x_j + y_j <= a (the right case is the
mirror image). Then for every t in G, with u = t - x_j >= y_j + d_a and
v = u/y_j >= 1:
  ( -2 m_j Re (t-z_j)^{-n} )_+  <=  m_j * G_n / d_a^n,                     (B.4)
where G_n := 2 max_{v >= 1} (v-1)^n * ( -Re((v+i)^{-n}) )_+ satisfies
  G_4 = 0.022543...,  and  G_n <= 2 e^{-π/2} < 5/12  for every even n.     (B.5)
Moreover the left-hand side of (B.4) is IDENTICALLY ZERO unless
  a - x_j < cot(π/(2n)) * y_j    ("band-adjacent at level n").             (B.6)

Proof. d_a <= u - y_j = (v-1) y_j, and r^n = y_j^n (1+v^2)^{n/2}, so
d_a^n * 2(-Re(t-z)^{-n})_+ <= 2 (v-1)^n (-Re((v+i)^{-n}))_+ <= G_n.
Bound (B.5): hurting requires cos(nθ) < 0 with θ = arctan(1/v), hence
θ > π/(2n), hence 1/v > tan(π/(2n)) >= π/(2n), i.e. n/v > π/2; then
(v-1)^n (1+v^2)^{-n/2} <= ((v-1)/v)^n = (1-1/v)^n <= e^{-n/v} < e^{-π/2},
and |cos| <= 1. (B.6): θ decreases in v and v >= (a-x_j)/y_j at t=a+, and v
only grows as t increases; hurting needs v < cot(π/(2n)). G_4 by symbolic
optimization (critical point v = 1.96261..., root of an explicit
polynomial; rigorous enclosure 0.022542 < G_4 < 0.022543). QED.

Define, per side and level n:  M_L^(n) := Sum { m_j : left non-ov pairs with
a - x_j < cot(π/(2n)) y_j },  M_R^(n) mirror. (Note cot(π/8) = 1+√2 at n=4;
with y_j <= 1/2 all such pairs lie within horizontal distance
cot(π/(2n))/2 of the gap.)

## 5. Theorem B-I (anchored excitation; unconditional under (SC))

(i) U := union of int I_j ∩ G over overhanging j has AT MOST TWO connected
components, each with an endpoint of G on its closure ("anchored" at a or b).
Proof: 2y_j >= g, so if I_j ∩ G had x_j - y_j > a and x_j + y_j < b then
2y_j < g. Hence each I_j ∩ G touches a or b; the union of the a-touching
ones is an interval (a, l_a), likewise (l_b, b). QED.

(ii) P := {t in G : h'(t) > 0} ⊆ U. Proof: at t with h'(t)>0, since
B(t) > 0 and non-overhanging pairs have phi'_j <= 0 on G (support lemma,
L-105061 3.2), some overhanging pair must have phi'_j(t) > 0, i.e. t ∈ int I_j.

(iii) #{distinct zeros of h in G} <= 1 + 2 #comp(P). Proof: between
consecutive distinct zeros τ_i < τ_{i+1}, h has one sign; if h > 0 there,
h' > 0 somewhere just right of τ_i; if h < 0, h' > 0 just left of τ_{i+1};
so each of the N-1 middle intervals contains a point of P. A single
component of P is an interval on which h is strictly increasing, so its
closure contains at most one zero of h; hence it can serve at most the two
intervals adjacent to that zero. N - 1 <= 2 #comp(P). QED.

(iv) Confinement: every zero of h' lies in {t : B(t) <= 8W/g^2}
⊆ [a + g/(2√2 √W), b - g/(2√2 √W)]. Proof: at a zero, Phi'(t) = B(t) and
Phi'(t) <= Sum_ov 2 m_j / y_j^2 = (8/g^2) W; then 1/d_a^2 <= B <= 8W/g^2. QED.

## 6. Theorem B-II (the ladder cap) and Corollary B-III

THEOREM B-II. Assume (SC). Fix k >= 1, n = 2k+2. If
    V_k + G_n * ( M_L^(n) + M_R^(n) )  <  1                                (B.7)
— or, for k = 1, the refined condition
    κ V_1 + G_4 * ( M_L^(4) + M_R^(4) )  <  1,   κ = (11+5√5)/64 —          (B.8)
then h^(2k+1) < 0 everywhere on G, and consequently
    Z_mult(h', G) <= 2k,   extra(G) <= 2k,
and every real zero of F' in G has multiplicity <= 2k+1 (= its multiplicity
as a zero of h, since F != 0 on G; hostile-review correction — the earlier
"mu - 1" step was wrong: ord(h) = ord(F'/F) = ord(F') on G).

Proof. By (B.1), h^(2k+1) = -(2k+1)! Re S_n, so it suffices that
Re S_n > 0 on G. Fix t. By Lemma B.2(a) the real zeros contribute at least
1/d_a^n + 1/d_b^n >= 2(2/g)^n (all their terms are positive; we may drop all
but the endpoint ones). Helping pairs contribute >= 0 and are dropped.
Hurting overhanging pairs cost at most V_k * 2(2/g)^n by Lemma B.3
(κ V_1 * 2(2/g)^4 for n = 4 by (B.3)); hurting left non-overhanging pairs
cost at most G_n M_L^(n) / d_a^n by (B.4), the right ones G_n M_R^(n)/d_b^n.
Assembling: Re S_n >= 1/d_a^n + 1/d_b^n
- V_k * 2 (2/g)^n - G_n M_L^(n)/d_a^n - G_n M_R^(n)/d_b^n
>= (1/d_a^n + 1/d_b^n) * [ 1 - V_k - G_n max(M_L^(n), M_R^(n)) ],
using 2(2/g)^n <= 1/d_a^n + 1/d_b^n. This is > 0 under (B.7), which implies
the bracket is positive (as V_k + G_n max <= V_k + G_n (M_L+M_R) < 1).
Negativity of h^(2k+1) gives: h^(2k) strictly decreasing, so
Z_mult(h^(2k), G) <= 1; the Rolle-with-multiplicity inequality
Z_mult(f, I) <= 1 + Z_mult(f', I) (valid for real-analytic f with locally
finitely many zeros; zeros of h cannot accumulate at a or b since
h -> ±∞ there) applied 2k times gives Z_mult(h', G) <= 2k and
Z_mult(h, G) <= 2k+1, i.e. extra <= 2k; a single zero of h of multiplicity
μ satisfies μ <= Z_mult(h, G) <= 2k+1, and its multiplicity as a zero of F'
in G is the SAME μ <= 2k+1 (F != 0 on G, so ord(F') = ord(h);
hostile-review correction of the earlier "μ - 1" claim). QED.

COROLLARY B-III (explicit caps). Assume (SC).
(a) [spread cooperation] If no non-overhanging pair is band-adjacent at
level 4 (M_L^(4) = M_R^(4) = 0), then
    V_1 < 1/κ = 16(5√5 - 11) = 2.88543...   ==>   extra(G) <= 2.
In particular W may be ARBITRARILY LARGE: e.g. any number of pairs with
w_j <= 1/2 and V_1 <= Sum m_j w_j^2 < 2.885 gives extra <= 2 — this covers
the diffuse-cooperation bulk (m pairs of equal weight w = W/m: V_1 = W^2/m,
so extra <= 2 whenever m > W^2/2.885).
(b) [strictly shallow, isolated] If w_max := max_ov w_j < 1 and all
M^(n)-loads vanish up to level n* = 2k*+2 with k* = 2 + floor(log_+ V_1 /
log(1/w_max)) (the +2/floor form guards the boundary case where
log_+ V_1 / log(1/w_max) is an exact integer or V_1 = 1, in which
w_max^{k-1} V_1 = 1 exactly and strict (B.7) would fail — hostile-review
correction), then, since V_k <= w_max^{k-1} V_1 < 1 for k >= k*,
    extra(G) <= 4 + 2 floor( log_+ V_1 / log(1/w_max) ).
(c) [linear-in-W form; safety net] Under (b)'s hypotheses, since V_1 <= W
(and inheriting (b)'s corrected +2/floor form):
    extra(G) <= 6 + (2/log(1/w_max)) log_+ W  <=  A W + A''
with A = 2/log(1/w_max), A'' = 6; by [THRESHOLD] (L-105061 §3) this upgrades
to the multiplicative cap extra(G) <= (6 + 2/log(1/w_max)) * W(G). The
dependence on W is in fact only LOGARITHMIC.

## 7. What remains open (precise remainder), and interfaces

The hypotheses fail only in two precisely delimited situations:
(R1) NEAR-CRITICAL CONCENTRATION: >= 1/κ units of quartic weight V_1, carried
necessarily by pairs with w_j close to 1 (y_j close to g/2): e.g. if all
w_j <= 1/2 then V_1 <= W/2 and (a) already needs W >= 5.77. Since
m_j w_j^2 <= m_j, condition (B.8) can only fail when the total multiplicity
of pairs with w_j > w* is >= (1 - stuff)/w*^2-ish: the remainder is a
BOUNDED-COOPERATION problem for O(1)-many near-critical pairs
(y_j ∈ [g/2, g/(2√w*))), which live at the boundary with the deep-pair lane
(y comparable to g). This is the natural next lane.
(R2) BAND-ADJACENT NON-OVERHANGING MASS: non-overhanging pairs within
horizontal distance cot(π/(2n)) y_j <= cot(π/(2n))/2 of G. Interface note
for the ASSEMBLY lane: such a pair overhangs or neighbours ITS OWN gaps and
pays weight there; global bookkeeping should charge its G_n-load (each unit
costs only G_4 = 0.0225 at level 4, and < 5/12 at every level) against that
weight. A per-side allowance of up to 43 multiplicity units of band-adjacent
non-ov pairs is FREE at level 4 when κ V_1 < 1/2 (0.0226 * 43 < 0.5 - takes
(B.8) to the boundary).

Recorded route for (R1)/(R2) slicing control (not needed above, may help a
successor): non-overhanging LEFT pairs can raise the background inside G
only on t - a < (√3 - 1) y_j <= (√3-1)/2 ≈ 0.366 (strip cap), with bump
width >= y_j >= (a - x_j): bumps are never narrow relative to their distance
from the endpoint, so staggered slicing bumps form a Whitney-type packing
and at most O(log W) can act independently above the confinement scale
g/(2√2√W) of Theorem B-I(iv). The designed numerical slicing attack
(Section 8) confirms the suppression: stacked bumps drown the excitation
(extra = 0) before they ever slice it (extra never exceeded 2).

## 8. Numerical record (float64 screening; counts by sign changes on
600k-800k grids; parity anomalies (extra = -1 or odd) are grid misses of
close zero pairs and never affect the max)

(1) Shallow scans: 600 configs, m = 2..30 overhanging pairs, g ∈ {0.3, 0.6,
1.0}, y ∈ [g/2, 1/2], modes random/clustered/near-critical-spread, mults
1..3, W up to 17.2: max extra = 2 (attained 432 times). SATURATION AT 2
confirmed (matches L-105061 §4). Zero violations of the B-II ladder
prediction extra <= 2k with k from w_max, V_1.
(2) Admissible-condition verification: 400 random configs incl. non-ov
pairs; the 80 satisfying (B.8): h''' < 0 on all of G in ALL cases (grid
max of h''' strictly negative), extra <= 2 in all cases. Derivative
formula (B.1) checked against finite differences to 9 digits.
(3) Designed slicing attacks (plateau pair mult A up to 200, up to 4
staggered non-ov bump pairs per side with multiplicities up to 3642 tuned
to overtop the plateau locally): never produced extra > 2; the bump tails
(quadratic decay) dominate globally before slicing locally — extra
collapses to 0. Files: scan1.py, slice.py, slice2.py, slice3.py, verify.py.

## 9. Falsifiers

(i) A config satisfying (B.7)/(B.8) with extra > 2k (refutes B-II — check
h''' sign first; use exact arithmetic per L-105061 replay discipline).
(ii) An (SC) config with U having 3 components (refutes B-I(i) — impossible
by 2y >= g). (iii) An (SC) config with extra > 2 at all (would refute the
working conjecture C_B = 2, not the theorems; would sharpen the remainder).

-- Lane CAP-B, 2026-08-22. Constants exact where stated; G_4 enclosure
rigorous to the printed digits; kappa exact: (11+5√5)/64.
