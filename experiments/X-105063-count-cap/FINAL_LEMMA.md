# FINAL LEMMA (CAP-C assembly) — the count cap extra(G) <= A' W(G), A' = 6, on the assembled regimes

Status: PROVED (Theorems C-0, C-1, C-2, C-3 below; C-2 is new to this lane).
Residual stated precisely in Section 6. RH is not addressed.
Depends on: L-105061 [I-PF] + [THRESHOLD] (proved, repo working tree),
LEMMA_A.md (lane CAP-A, proved), LEMMA_B.md (lane CAP-B, proved).
Numerics: Section 5 (scanC.py, scanD.py, probe2.py, replay.py, constants2.py here).

## 0. Setting and notation

F real entire, order <= 1, genus 0 in t^2 (Hadamard product, L-105062 §1). Real zeros
{t_n} (mult m_n); non-real conjugate pairs z_j = x_j + i y_j, 0 < y_j <= 1/2 (mult m_j).
G = (a,b) a bounded gap between consecutive real zeros, g = b - a; h = F'/F on G;
extra(G) := Z_mult(h, G) - 1 = #{real zeros of F' in G, mult} - 1. By [I-PF]:
h' = -B + Phi', B = m0/t^2 + Sum m_n (t-t_n)^{-2} >= 1/d_a^2 + 1/d_b^2 >= 8/g^2
(d_a = t-a, d_b = b-t), Phi' = Sum m_j phi'_j, phi'_j(t) = -2 Re (t-z_j)^{-2}
= 2(y_j^2-(t-x_j)^2)/((t-x_j)^2+y_j^2)^2; all series absolutely locally uniformly
convergent on G, hence termwise differentiable to all orders (Weierstrass).

Pair j OVERHANGS G iff I_j ∩ G ≠ ∅, I_j := (x_j - y_j, x_j + y_j). Gap weight
W(G) := Sum_{overhanging} m_j min(1, g^2/(4 y_j^2)).
An overhanging pair is DEEP if y_j < g/2 (then its weight term is m_j * 1) and
SHALLOW if y_j >= g/2 (weight term m_j w_j, w_j := (g/(2y_j))^2 <= 1).
D_ov := number of DISTINCT deep overhanging pairs. Fattening radius R4 := 2 + sqrt3.
Fattened interval Itilde_j := (x_j - R4 y_j, x_j + R4 y_j).

Shallow weights: W_sh := Sum_{shallow ov} m_i w_i, V_1 := Sum m_i w_i^2,
V_2 := Sum m_i w_i^3 (so V_2 <= V_1 <= W_sh, and W = W_sh + Sum_{deep ov} m_j).
Band loads (non-overhanging pairs, any y; LEFT means x_i + y_i <= a, RIGHT mirror):
M_L^(n) := Sum { m_i : left non-ov, a - x_i < cot(pi/(2n)) y_i }, M_R^(n) mirror
(cot(pi/8) = 1+sqrt2 at n=4; cot(pi/12) = 2+sqrt3 at n=6).

Constants (Section 4): kappa = (11+5 sqrt5)/64 = 0.34656781 (exact);
kappa_6 = 1 (exact); G_4 = 0.02254249 (rigorous enclosure, lane B);
G_6 = 0.04631627 (numeric; rigorous cap G_6 <= 2 e^{-pi/2} = 0.41576 by B.5).

## 1. Theorem C (assembled count cap)

For every gap G, in each of the following regimes:

**C-0 (no overhang).** No pair overhangs G. Then h' < 0 on G and extra(G) = 0.

**C-1 (isolated site; = LEMMA A).** (H1): at most one pair has Itilde ∩ G ≠ ∅.
Then Z_mult(h', G) <= 6 and extra(G) <= 6; moreover extra(G) <= 6 W(G).

**C-2 (mixed deep + subcritical shallow; NEW).** Assume
  (Sep) the fattened intervals Itilde_j of the deep overhanging pairs are pairwise
        disjoint;
  (L2)  W_sh < 1;
  (L4)  kappa V_1 + G_4 (M_L^(4) + M_R^(4)) < 1;
  (L6)  V_2 + G_6 (M_L^(6) + M_R^(6)) < 1.
Then every zero of h' in G lies in some deep I_j, Z_mult(h', I_j ∩ G) <= 6 for each,
and
  extra(G) <= Z_mult(h', G) <= 6 D_ov <= 6 W(G).
If D_ov = 0 the conclusion is extra(G) = 0. Note: if M^(4) = M^(6) = 0 (no
band-adjacent non-overhanging mass), (L2) alone implies (L4) and (L6).
No deep-shallow or deep-non-ov separation is assumed — only deep-deep.

**C-3 (shallow ladder; = LEMMA B).** (SC): all overhanging pairs shallow. If
(B.7) V_k + G_n (M_L^(n)+M_R^(n)) < 1 for some k >= 1 (n = 2k+2), or the k=1
refinement (B.8) kappa V_1 + G_4 (M_L^(4)+M_R^(4)) < 1, then extra(G) <= 2k, and
extra(G) <= 2k W(G). (Also Cor. B-III(c): extra <= (4 + 2/log(1/w_max)) W under
its hypotheses.)

**Headline.** On the union of regimes C-0, C-1, C-2 the multiplicative cap holds
with the single absolute constant A' = 6:  extra(G) <= 6 W(G).

## 2. Proof of C-0, C-1, C-3 and the multiplicative upgrades

C-0: non-overhanging pairs have phi'_j <= 0 on G (support: phi'_j > 0 only on
int I_j), so h' <= -B < 0; h runs +infty -> -infty (simple poles at a, b), is
strictly decreasing, has one simple zero; extra = 0.

C-1 is LEMMA A verbatim (extra <= 6, all h'-zeros in I ∩ G). C-3 is LEMMA B
Theorem B-II / Corollary B-III verbatim.

Multiplicative upgrades ([THRESHOLD]): if extra(G) >= 1 then h has >= 2 zeros in G
(with multiplicity; a single multiple zero also forces h' = 0 there), so h' has a
zero in G by Rolle-with-multiplicity, and [THRESHOLD] gives W(G) >= 1. Hence any
additive bound extra <= c becomes extra <= c W(G), and extra <= A W + A'' becomes
extra <= (A + A'') W. Applied with c = 6 (C-1) and c = 2k (C-3). QED.

## 3. Proof of Theorem C-2

Throughout, "damage at level n" of a pair means the positive part of its
contribution to the relevant derivative of -Phi'; the derivative identities
(sympy-verified, constants.py; also LEMMA B (B.1))
  phi' = -2 Re (t-z)^{-2},  (phi')'' = -12 Re (t-z)^{-4},  (phi')'''' = -240 Re (t-z)^{-6}
per unit multiplicity, and the endpoint floors (only the two endpoint zeros kept)
  B >= 1/d_a^2 + 1/d_b^2 >= 8/g^2,
  B'' = 6 Sum m_n (t-t_n)^{-4} >= 6/d_a^4 + 6/d_b^4 >= 192/g^4,
  B'''' = 120 Sum m_n (t-t_n)^{-6} >= 120/d_a^6 + 120/d_b^6 >= 15360/g^6.

**Step 1 (level-2 confinement; uses (L2) only).** For t in G write
h'(t) = -B(t) + Sum_j m_j phi'_j(t). Non-overhanging pairs: phi'_j(t) <= 0
(support). Shallow overhanging pairs: (phi'_i)_+ <= 2/y_i^2 = (8/g^2) w_i, so
their total positive contribution is <= (8/g^2) W_sh. Deep overhanging pairs:
phi'_j(t) <= 0 unless t in int I_j. Hence for t in G \ U, U := union of deep I_j:
  h'(t) <= -(8/g^2)(1 - W_sh) < 0.
So all zeros of h' in G lie in U; by (Sep) the I_j are pairwise disjoint (they sit
inside the disjoint Itilde_j), so
  Z_mult(h', G) = Sum_{deep ov j} Z_mult(h', J_j),  J_j := I_j ∩ G.
If D_ov = 0: h' < 0 on all of G, h strictly decreasing, extra = 0.

**Step 2 (per-pair comparison function).** Fix a deep overhanging pair j; write
y = y_j, x = x_j, m = m_j, f(s) = 2(y^2-s^2)/(s^2+y^2)^2, s = t - x. On J_j,
  h' = m f(t-x) - Q,   Q := B - Sum_{i != j} m_i phi'_i.
Claim: Q'' > 0 and Q'''' > 0 on J_j. Termwise:
(i) Real zeros: contribute B'' , B'''' with the floors above.
(ii) Other DEEP OVERHANGING pairs i: for t in J_j ⊆ Itilde_j and Itilde_i ∩
Itilde_j = ∅ (Sep), |t - x_i| >= R4 y_i. By the LEMMA A §2 sign tables (re-verified
numerically at |s| = R4 y and beyond, constants2.py): f_i <= 0, f_i'' <= 0,
f_i'''' <= 0 there, i.e. -phi'_i, -(phi'_i)'', -(phi'_i)'''' >= 0: these terms only
help; drop them.
(iii) SHALLOW OVERHANGING pairs i (y_i >= g/2, so 1/y_i^2 = (4/g^2) w_i): at every
real t,
  level 4: ((phi'_i)'')_+ = 12 (-Re(t-z_i)^{-4})_+ <= 12 kappa / y_i^4
           = kappa w_i^2 * (192/g^4)                     [LEMMA B (B.3)],
  level 6: ((phi'_i)'''')_+ = 240 (-Re(t-z_i)^{-6})_+ <= 240 kappa_6 / y_i^6
           = kappa_6 w_i^3 * (15360/g^6),  kappa_6 = 1
           [|Re(t-z)^{-6}| <= r^{-6} <= y^{-6}; equality at t = x_i].
  Totals: <= kappa V_1 (192/g^4) and <= V_2 (15360/g^6).
(iv) NON-OVERHANGING pairs i (any y_i, left case; right mirror): LEMMA B Lemma B.4
with n = 4 and n = 6 gives (-2 Re(t-z_i)^{-n})_+ <= G_n / d_a^n per unit mult, zero
unless band-adjacent at level n. Hence
  level 4 damage <= 6 G_4 (M_L^(4)/d_a^4 + M_R^(4)/d_b^4),
  level 6 damage <= 120 G_6 (M_L^(6)/d_a^6 + M_R^(6)/d_b^6).
Assembling level 4 (level 6 identically, with 120/d^6-floors, kappa_6 V_2, G_6):
  Q'' >= 6/d_a^4 (1 - G_4 M_L^(4)) + 6/d_b^4 (1 - G_4 M_R^(4)) - kappa V_1 (192/g^4)
      >= (6/d_a^4 + 6/d_b^4) [ 1 - kappa V_1 - G_4 max(M_L^(4), M_R^(4)) ] > 0
under (L4), using 192/g^4 <= 6/d_a^4 + 6/d_b^4; similarly Q'''' > 0 under (L6).

**Step 3 (concavity split on J_j; LEMMA A Step 3 verbatim).** Cut J_j by the points
x ± (2 - sqrt3) y into at most three pieces.
Center (|s| < (2-sqrt3)y): since 2-sqrt3 < sqrt2-1, f'' < 0 there, so
(h')'' = m f'' - Q'' < 0: no zeros of (h')''; the cut points also have f'' < 0, so
no zeros sit at the cuts. Wings ((2-sqrt3)y < |s| < y): f'''' < 0 strictly, so
(h')'''' = m f'''' - Q'''' < 0: (h')'' is strictly concave, hence carries at most 2
zeros with multiplicity per wing (three distinct zeros are impossible; a double
zero is the unique zero, of multiplicity exactly 2). Total
  Z_mult((h')'', J_j) <= 4.

**Step 4 (Rolle with multiplicity).** h' is real-analytic on G with finitely many
zeros (h' -> -infty at both endpoints — double poles — so it is zero-free near
∂G; interior accumulation would force h' ≡ 0). The inequality
Z_mult(psi, J) <= Z_mult(psi', J) + 1 (LEMMA A Step 2) applied twice on J_j:
  Z_mult(h', J_j) <= Z_mult((h')'', J_j) + 2 <= 6.

**Step 5 (totals).** By Step 1, Z_mult(h', G) <= 6 D_ov. h is real-analytic on G
with finitely many zeros and h -> ±infty at the endpoints, so
Z_mult(h, G) <= 1 + Z_mult(h', G), i.e. extra(G) <= Z_mult(h', G) <= 6 D_ov.
Each deep overhanging pair contributes m_j min(1, g^2/(4y_j^2)) = m_j >= 1 to W(G),
so D_ov <= W(G) and extra(G) <= 6 W(G). QED (C-2).

Remarks. (i) Multiplicities enter only as positive factors; all sign arguments are
invariant. (ii) I_j straddling a gap endpoint is allowed: J_j = I_j ∩ G is still an
interval and Steps 2–4 never used the position of J_j inside I_j. (iii) Only
deep-deep separation is assumed: a deep pair sitting under a shallow pair's
interval, or near band-adjacent non-ov mass, is covered by (iii)/(iv) budgets.

## 4. Constants table

| constant | value | status |
|---|---|---|
| R4 | 2 + sqrt3 = 3.7320508 | exact (largest root of f, f'', f'''' sign pattern) |
| kappa (level 4 shallow) | (11+5 sqrt5)/64 = 0.34656781 | exact (lane B (B.3), re-verified) |
| kappa_6 (level 6 shallow) | 1 | exact (max at t = x_i; r >= y) |
| G_4 (level 4 non-ov) | 0.022542–0.022543 | rigorous enclosure (lane B) |
| G_6 (level 6 non-ov) | 0.04631627 | numeric (grid+critical pt, v* = 2.85784); rigorous cap 2 e^{-pi/2} = 0.41576 |
| per-deep-pair cap | 6 | proved (Steps 3–4) |
| A' (headline) | 6 | proved on C-0 ∪ C-1 ∪ C-2 (and 2k on C-3) |

For a fully closed-form variant of (L6) use V_2 + (2 e^{-pi/2}) (M_L^(6)+M_R^(6)) < 1.

## 5. Numerical confirmation (this directory)

Finite rational configurations (for which [I-PF] is exact algebra); zero counts by
sign changes on 400k-grids with cancellation filter |v| > 1e-11 Sum|terms|;
attribution of h'-zeros to intervals by sign-change bracket overlap (midpoint
attribution produced 66 spurious "outside" flags at y ~ 1e-3; mpmath 40-dps
bisection — probe2.py — showed the roots INSIDE I_j at distance ~1.4e-4 y from the
edges; classifier fixed; replay discipline per L-105061 §4).

| scan | configs | result |
|---|---|---|
| scanC.py mixed adversarial (g ∈ {0.5,1}; D_ov ∈ {1,2,3,5,8}, y to 1e-3, mults to 5, endpoint-hugging; shallow W_sh to 0.99; band-adjacent non-ov; extra real zeros) | 487 passing (Sep)+(L2)+(L4)+(L6) | 0 violations of extra <= 6 D_ov, of confinement to U, of per-interval cap 6. Max extra = 16 at D_ov = 8; max Z(h', I_j) = 2 |
| replay.py (mpmath 40 dps) | extremal config (8 deep pairs, mult sum 15) | 17 distinct zeros of h: extra = 16 exactly = 2 D_ov; extra/W = 16/15 > 1 |
| scanD.py residual (i): deep R4-clusters (Sep violated), k = 2..4 pairs crammed | 300 | max extra per clustered pair: 2.0 (no cooperative blow-up seen) |
| scanD.py residual (ii): supercritical shallow W_sh up to 3.02 + deep | 300 | max extra = 6 = 2 D_ov, all zeros in deep intervals; shallow surplus added nothing |

Observed sharp behavior: extra = 2 per deep site, i.e. empirically extra <= 2 W;
the proved constant 6 is never approached. The D_ov = 8 example shows extra(G)
grows genuinely linearly in W — a multiplicative cap is the correct shape, and
any valid A' must be >= 16/15; empirically A' = 2 is the conjectured sharp value.

## 6. Honest residual

The cap extra(G) <= A' W(G) for EVERY gap is not yet proved. The proved regimes
C-0 ∪ C-1 ∪ C-2 ∪ C-3 fail to cover exactly:

(R-C1) DEEP CLUSTERS: two or more deep overhanging pairs with intersecting
R4-fattened intervals (and not reducible to LEMMA A's (H1)). What is missing is a
per-cluster bound Z_mult(h', K) <= C * (mult of pairs in K): the cluster pairs'
profiles mutually destroy the fixed-sign f''/f'''' partition of Step 3, and the
Jensen/disk route stalls on the unabsorbed log(g/y_min) normalization term (the
per-pair weight is 1, but the log factor is unbounded). Numerically clusters show
extra = 2 per pair — no cooperation — so the obstruction looks technical.

(R-C2) SUPERCRITICAL SHALLOW MASS: W_sh >= 1 failing LEMMA B's ladder conditions —
precisely LEMMA B's remainders (R1) (near-critical concentration: >= 1/kappa of
quartic weight V_1 carried by pairs with w_j near 1) and (R2) (band-adjacent
non-ov mass beyond the G_n budgets) — now also in the presence of deep pairs.
Numerically the shallow surplus never added zeros beyond the deep sites' 2 each.

Any future additive bound extra <= A W + A'' on a residual regime upgrades to
extra <= (A + A'') W by [THRESHOLD] (Section 2). Falsifiers: a C-2 config with
extra > 6 D_ov (check confinement first, then per-interval counts, exact
arithmetic); a deep cluster with extra > 2 * (pair mult sum) would refute the
conjectured sharp constant and sharpen the residual's difficulty.

-- Lane CAP-C, 2026-08-22. Files: NOTES.md, constants.py, constants2.py, scanC.py,
scanD.py, probe.py, probe2.py, replay.py in this directory.
