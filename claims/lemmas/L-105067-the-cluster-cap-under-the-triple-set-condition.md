# L-105067 — Count cap on clusters with empty triple set; the exact frontier of the 0-2-4 method

Status: Theorem T-1 and Propositions T-2, T-3(a) PROVED (modulo upstream L-105061/62,
LEMMA A/B, C-2 Step 2 budget lemmas, all cited precisely). T-3(b) is a certified
family of counterexamples to the METHOD (not to the cap). RH is not addressed.
Shrinks residual R-C1 of X-105063/FINAL_LEMMA.md §6; does not close it.
Numerics: t1_triple.py, t2_capscan_bracket.py (the CANONICAL cap scan — implements the bracket-overlap attribution the text describes; the original t2_capscan.py used point attribution and emits 385 spurious confinement flags, retained only as the recorded incident per replay discipline) + inline scans (this directory), logs in NOTES.md. The adversarial g=128 grazing families are inline-only (recorded limitation).

## 0. Setting (verbatim from FINAL_LEMMA.md §0)

F real entire, order <= 1, Hadamard genus 0 in t^2 (L-105062 §1). Gap G = (a,b),
g = b - a; h = F'/F; extra(G) = Z_mult(h, G) - 1. By [I-PF] on G:
h' = -B + Sum_j m_j phi'_j, B = m0/t^2 + Sum m_n (t-t_n)^{-2},
phi'_j(t) = f(t - x_j; y_j), f(s; y) = 2(y^2 - s^2)/(s^2 + y^2)^2,
all series absolutely locally uniformly convergent on G (termwise differentiable;
h' real-analytic on G). Deep / shallow overhang, weights W, W_sh, V_1, V_2, band
loads M^(4), M^(6), budgets (L2), (L4), (L6), R4 = 2 + sqrt3, Itilde_j: as in
FINAL_LEMMA.md §0-1. Deep overhanging pairs of G are finitely many (zeros of F in a
bounded set). (Sep) is NOT assumed anywhere in this note.

**Clusters.** Let U~ := Union of Itilde_j over deep overhanging pairs j. Its connected
components are intervals; the (maximal) clusters K_1, ..., K_r are the sets of deep
overhanging pairs whose Itilde_j lie in a common component. K_span := the component
(= Union_{j in K} Itilde_j). For distinct clusters K, K': Itilde_i ∩ K_span = ∅ for
every i in K', hence |t - x_i| >= R4 y_i for all t in K_span.       (0.1)

**Cluster profile and triple set.** For a cluster K with pairs (x_j, y_j, m_j), j = 1..m_K
(distinct z_j; multiplicity M_K := Sum m_j):
  Phi_K := Sum_{j in K} m_j phi'_j   (rational function),
  T_K := {t in R : Phi_K(t) > 0} ∩ {Phi_K''(t) > 0} ∩ {Phi_K''''(t) > 0}.
T_K depends only on the finite data of K (positions, scales, multiplicities) — it is
machine-checkable per cluster and independent of the gap and of all other pairs.

## 1. Theorem T-1 (count cap under empty triple sets)

Assume (L2), (L4), (L6) — and NOT (Sep). Assume
  (T-EMPTY)   T_K = ∅ for every maximal cluster K of G.
Then every zero of h' in G lies in Union_j I_j (deep pairs), the count splits over
clusters, and for each cluster K:
  Z_mult(h', K_span ∩ G) <= 16 m_K - 10.
Hence extra(G) <= Z_mult(h', G) <= Sum_K (16 m_K - 10) <= 16 W(G), and if there are
no deep overhanging pairs, extra(G) = 0 (under (L2) alone).

Remarks. (i) m_K = 1 gives the bound 6 — LEMMA A's constant — and T_K = ∅ is
automatic for singletons (Prop. T-2), so T-1 contains C-2: under (Sep) all clusters
are singletons. (ii) The hypothesis is per-cluster and local; no deep-deep
separation of any kind is assumed. (iii) Empirical sharp value remains 2 per pair.

### 1.1 The comparison function

Fix a cluster K. On K_span ∩ G define
  Q_K := B - Sum_{shallow ov} m_i phi'_i - Sum_{non-ov} m_i phi'_i
           - Sum_{other clusters' deep ov} m_i phi'_i,
so that h' = Phi_K - Q_K there.

**Lemma 1.1.** On K_span ∩ G: Q_K > 0 under (L2); Q_K'' > 0 under (L4);
Q_K'''' > 0 under (L6).

Proof. Termwise (Weierstrass). Level 0: B >= 8/g^2 (endpoint floor); non-ov pairs
have phi'_i <= 0 on G (support of the positive part of f is int I_i, disjoint from
G); shallow pairs have (phi'_i)_+ <= 2/y_i^2 = (8/g^2) w_i, total <= (8/g^2) W_sh
(FINAL_LEMMA §3 Step 1 — pointwise, (Sep)-free); other clusters' deep pairs have
|t - x_i| >= R4 y_i by (0.1), hence phi'_i <= 0 (LEMMA A §2 sign table). So
Q_K >= (8/g^2)(1 - W_sh) > 0.
Levels 2 and 4: identical assembly to FINAL_LEMMA §3 Step 2, clauses (i), (iii),
(iv) — all pointwise on G and (Sep)-free (B.3 holds at every t in G; B.4 holds for
every t in G) — plus, for other clusters' deep pairs, (0.1) and the sign table
(-phi'_i)'' >= 0, (-phi'_i)'''' >= 0 beyond R4 y_i: these terms only help. There is
no deep-deep clause left: every deep pair of K is in Phi_K, every other deep
overhanging pair is R4-far from K_span. Hence
  Q_K'' >= (6/d_a^4 + 6/d_b^4)[1 - kappa V_1 - G_4 max(M_L,M_R)] > 0 under (L4),
  Q_K'''' >= (120/d_a^6 + 120/d_b^6)[1 - V_2 - G_6 max(M_L,M_R)] > 0 under (L6). QED

### 1.2 Confinement and splitting

**Lemma 1.2.** Under (L2), every zero of h' in G lies in Omega_K := {Phi_K > 0} ∩ G
for some cluster K, and Omega_K ⊆ Union_{j in K} I_j. Distinct clusters' Omega's are
disjoint.

Proof. At a zero t of h': Sum_{all deep} m_j phi'_j(t) = B - (shallow) - (non-ov)
terms >= (8/g^2)(1 - W_sh) > 0 (as in Lemma 1.1, level 0), so some deep pair has
f_j(t) > 0, i.e. t in int I_j; j belongs to a cluster K, and on K_span the other
clusters' deep terms are <= 0 (0.1), so Phi_K(t) >= Sum_{all deep} m_j phi'_j(t) > 0.
{Phi_K > 0} ⊆ Union_{j in K} I_j because outside that union every f_j <= 0. The
I-unions of distinct clusters are disjoint (overlapping I's would merge the fattened
components). QED

### 1.3 Degree and component counts

Phi_K = N0 / Prod_{j in K} q_j^2, q_j = (t-x_j)^2 + y_j^2 > 0. As t -> ±inf,
Phi_K ~ -2 M_K / t^2 < 0, so deg N0 = 4 m_K - 2 exactly, with negative leading
coefficient. Phi_K'' = N2 / Prod q_j^4 with Phi_K'' ~ -12 M_K / t^4, so
deg N2 = 8 m_K - 4, negative leading coefficient. A rational function with positive
denominator, whose numerator has degree d and which is negative near ±inf, has at
most d/2 positivity components (each component consumes two sign changes of the
numerator). Hence
  #comp {Phi_K > 0} <= 2 m_K - 1,   #comp {Phi_K'' > 0} <= 4 m_K - 2.
Intersecting families of disjoint open intervals (merge bound):
  #comp (Omega_K ∩ {Phi_K'' > 0}) <= (2 m_K - 1) + (4 m_K - 2) - 1 = 6 m_K - 4.
(Intersecting with the interval G does not increase counts.)

### 1.4 The 0-2-4 chain

Fix a component omega of Omega_K, and let V_1, ..., V_p (p <= 6 m_K - 4 in total
over all omega) be the components of Omega_K ∩ {Phi_K'' > 0}.

(a) Zeros of (h')'' in omega lie in the V's: at such a zero, Phi_K'' = Q_K'' > 0.
Elsewhere in omega, (h')'' = Phi_K'' - Q_K'' < 0.

(b) On each V: T_K = ∅ forces Phi_K'''' <= 0 on V (V ⊆ {Phi_K>0} ∩ {Phi_K''>0}),
so (h')'''' = Phi_K'''' - Q_K'''' < 0: (h')'' is strictly concave on V, hence
Z_mult((h')'', V) <= 2 (three distinct zeros are impossible; a multiple zero is
unique of multiplicity exactly 2 — LEMMA A Step 3 argument verbatim).

(c) Finiteness: Z_mult((h')'', omega) <= 2p < inf is sign-based and unconditional
given (a), (b); infinitely many zeros of (h')' in omega would give (Rolle)
infinitely many zeros of (h')''; same for h' via (h')'. So Rolle-with-multiplicity
(LEMMA A Step 2) applies twice on omega:
  Z_mult(h', omega) <= Z_mult((h')'', omega) + 2 <= 2 #{V in omega} + 2.

Summing over the components omega of Omega_K (at most 2 m_K - 1 of them) and using
Lemma 1.2 (zeros of h' in K_span ∩ G all lie in Omega_K):
  Z_mult(h', K_span ∩ G) <= 2 (6 m_K - 4) + 2 (2 m_K - 1) = 16 m_K - 10.

### 1.5 Assembly

Summing over clusters (Lemma 1.2 splits the count) and using finiteness of zeros of
h on G with the endpoint blow-up (FINAL_LEMMA §3 Step 5 verbatim):
extra(G) <= Z_mult(h', G) = Sum_K Z_mult(h', K_span ∩ G) <= Sum_K (16 m_K - 10).
Each deep pair contributes m_j >= 1 to W(G), so Sum_K m_K <= W(G) and
extra(G) <= 16 W(G). If there is no deep overhanging pair, h' <= -(8/g^2)(1-W_sh)<0
on G and extra(G) = 0. QED (T-1)

## 2. Proposition T-2 ((Sep) ⇒ (T-EMPTY); singletons)

If m_K = 1, T_K = ∅: with a single profile, Phi_K > 0 forces |s| < y, Phi_K'' > 0
forces |s| > (sqrt2 - 1) y, Phi_K'''' > 0 then forces |s| < (2 - sqrt3) y — empty
since 2 - sqrt3 < sqrt2 - 1 (LEMMA A §2 tables). Under (Sep) every cluster is a
singleton (two pairs in one cluster would chain overlapping fattened intervals,
contradicting pairwise disjointness), so (T-EMPTY) holds and T-1 applies. Hence
T-1's regime strictly contains C-2's. (C-2's constant 6 per pair remains sharper
there; T-1 with m_K = 1 also gives 6.)

## 3. Proposition T-3 (the frontier: T-EMPTY is exactly what the 0-2-4 method can reach)

(a) METHOD-NECESSITY. Let Phi be any C^4 function on an interval and [c,d] a
subinterval on which Phi > m_0 > 0, Phi'' > m_2 > 0, Phi'''' > m_4 > 0. For any
omega > 0 put eps := (1/2) min(m_0, m_2/omega^2, m_4/omega^4) and
Q := Phi - eps sin(omega t). Then Q > 0, Q'' > 0, Q'''' > 0 on [c,d], while
Phi - Q = eps sin(omega t) has >= floor(omega (d-c)/pi) zeros there. Consequently NO
bound on Z(Phi - Q) can follow from the data "(Q, Q'', Q'''') > 0 pointwise" alone
when the triple set has nonempty interior: any proof of a per-cluster cap beyond
(T-EMPTY) must use more about Q than Lemma 1.1 provides (its realizability as
B - Phi'_far for an actual zero configuration — e.g. Q'' convexity is already used;
level-6 budgets (L8-type) or arithmetic input would be needed).

(b) NONEMPTY TRIPLE SETS EXIST — even at unit multiplicities (certified numerically,
40-dps replay of the margins; grid + local refinement):
  - Equal scales y_1 = y_2 = 1, m_1 = 1: T ≠ ∅ iff mult ratio mu is outside roughly
    (0.6, 1.75) for some offset c. E.g. mu = 3.4, c = 0.7, t = -0.2241:
    (L0, L2, L4) = (+2.011, +4.806, +20.86), 40-dps replay.
  - Unit multiplicities, unequal scales: pairs (0, 0.8, 1), (0.05, 1, 1):
    t* = -0.849 gives (L0, L2, L4) = (+0.0301, +10.02, +4.162), 40-dps replay.
    Mechanism ("edge injector"): at |s| = y the profile has f = 0, f'''' = 0,
    f'' = +3/y^4; the outer band |s|/y in (1, sqrt2+1) has signature
    (f, f'', f'''') = (-, +, +) with |f| small, and combined with a larger pair's
    inner band (+, +, -) all three levels go positive. Robust: at m_1 = m_2 = 1,
    T ≠ ∅ occurs for all scale ratios y_1/y_2 <= 0.98 at some offset; 13 unit
    pairs at near-common scale (one at y = 1/1.3, twelve at y = 1, offsets
    ±1.05..±1.2) give T = ±(0.1046, 0.2035) (two islands; at t = -0.1540:
    (+2.191, +6.459, +410.5), 40-dps replay; hostile-review note: this example's offsets are under-specified in the run log — the reviewer's reconstruction certifies a triple point with values (+2.12, +5.95, +415.7); the two 2-pair examples replay EXACTLY at 40 dps).
  - Worst-case-over-offsets map (m = 2): T-EMPTY for all offsets only in the sliver
    scale ratio >= 0.99 and mult ratio in ~[0.7, 1.6]. For FIXED configurations
    T-EMPTY is much more common: random genuine R4-clusters are T-empty in
    ~99% (k=2, near-equal scales, unit mults) down to ~25-60% (k=5, spread scales).

## 4. Numerical verification of T-1 (t2_capscan_bracket.py; bracket-overlap attribution — hostile-review patch: the shipped t2_capscan.py did NOT implement the described attribution)

600 finite rational configs (g in {1,4,16}; 1-5 deep pairs, y down to 1e-4 g, mults
to 4, endpoint-hugging; shallow + band-adjacent non-ov within (L2)(L4)(L6); extra
real zeros): 518 T-empty / 82 not. Violations of the cap 16 m - 10, of confinement
to Union I_j (bracket-overlap attribution; midpoint attribution false-flags roots
lying ~1e-3 y inside the I_j edge, reproducing the capC incident), or of the
empirical 2 M bound: NONE, in either regime. Max observed Z(h') = 10 at m = 5,
M = 15 (T-empty), 8 at m = 5, M = 10 (T nonempty). Adversarial nonempty-T families
(edge-injector 2-cluster, mu = 4 equal-scale, 13-unit-pair cluster; gaps to
g = 128 so that B ~ Phi at the triple point; added band non-ov mass): Z(h') = 2
always — the cap is comfortably TRUE where the method cannot prove it.

## 5. Honest residual (R-C1 after this note)

R-C1 shrinks to:
(R-C1') clusters K with T_K ≠ ∅ (given (L2)(L4)(L6); otherwise also R-C2).
UPDATE 2026-08-23 (`L-105076`): the "genuinely different input" arrived — the
Jensen window cap (complex-center cone lemma at height 8L) bounds T-nonempty
clusters at `5.813` per distinct pair with NO triple-set condition, eliminating
the log(g/y_min) obstruction; R-C1' shrinks to R-J (stopping-recursion
failures, empty on all 104 adversarial T-nonempty clusters tested, including
this note's §3b certified families — 13/13).
This is now an explicit, decidable, per-cluster geometric condition, with certified
minimal examples (§3b) and a proved method-obstruction (§3a): no pointwise-sign
argument at levels 0/2/4 can remove it. Escalating to levels 6+ requires new
budgets ((L8): shallow V_3 <= W_sh is free, but non-ov band loads M^(8) with band
cot(pi/16) ≈ 5.03 are a NEW hypothesis) and faces the L-105061 §5(ii) regress —
the sign pattern of Re(t-z)^{-n} recurs with period ~pi/arg, so new injector
combinations reappear at every finite level. A genuinely different input (the
realizable structure of Q — e.g. Markov/Stieltjes total positivity of the real-zero
field B, or the argument-principle/winding route on a rectangle around K_span with
the deep poles divided out) appears to be required for unbounded clusters.
Falsifiers: a T-empty config violating 16 m_K - 10 (would refute T-1 or upstream);
any config with Z(h', K_span ∩ G) > 2 M_K (would refute the conjectured sharp
constant 2 and locate genuine cluster cooperation).

-- Lane T, 2026-08-23. Files: NOTES.md (plan + derivation log), t1_triple.py
(triple-set explorer), t2_capscan.py (cap scan), t3_debug.py (attribution debug),
this draft.
