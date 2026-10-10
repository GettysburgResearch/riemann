# Lane B3 — Descent assembly + master corollary
Status: derivations independent; orchestrator note re-derived, NOT trusted (errors found, see §7).
Interfaces: B1 = laneB1/NOTES.md (Thm 1 strip, Thm 2 conservation, Thm 3 Rolle floor, Thm 4 monotone ladder) — read and cross-checked.
B2 (dipole) delivered NOTHING at assembly time — the dipole interface is pinned HERE as an exact statement slot (L-105061), with the parts of it I could prove myself (support/threshold structure) proved below in §3.

## §1 (a) EXACT DEFINITIONS — final deposit form

Setting: Xi(t) = xi(1/2+it), real entire, even, order 1; Xi_k := (d/dt)^k Xi = i^k xi^{(k)}(1/2+it); Xi_k real entire of parity (-1)^k; all zeros of Xi_k in the closed strip |Im t| <= 1/2 (B1 Thm 1 / L-105062).

All counts on the half-window 0 < Re t <= T, WITH multiplicity, and zeros with Re t = 0 are excluded from every count (matching B1's rectangle convention; the finitely many possible axis zeros are absorbed into additive constants there).

- N_k(T) := #{ zeros t of Xi_k : 0 < Re t <= T } (multiplicity).
- N_k^r(T) := #{ real zeros t of Xi_k : 0 < t <= T } (multiplicity).
- N_k^c(T) := N_k(T) - N_k^r(T).
- Pairs: the non-real zeros of Xi_k come in conjugate pairs x_j +- i y_j, 0 < y_j <= 1/2 (reality + strip). A pair is indexed once per conjugate pair, with multiplicity (an m-fold non-real zero gives the pair multiplicity m). Parity maps the pair (x_j, y_j) to (-x_j, y_j); no quotient by parity is taken — pairs at x and -x are distinct pairs (unless x = 0).
- P_k(T) := #{ pairs (x_j, y_j) of Xi_k : 0 < x_j <= T } (with multiplicity). Then N_k^c(T) = 2 P_k(T). (Pairs with x_j = 0 — purely imaginary zeros — are excluded, consistently with the Re t = 0 exclusion.)
- Z_k^r := the set of ALL real zeros of Xi_k (whole line). Z_k^r is unbounded above (Hardy's theorem: N_0^r(T) -> infinity, plus B1 Thm 3 iterated: N_k^r(T) >= N_0^r(T) - k) and unbounded below (parity). Hence every connected component of R \ Z_k^r except the two infinite tails... — correction: since Z_k^r is unbounded in BOTH directions, EVERY component of R \ Z_k^r is a bounded open interval (a "gap"). For a gap G = (a, b), |G| := b - a; a, b are consecutive distinct real zeros of Xi_k.
- Gap list for the window: 𝒢_k(T) := { G component of R \ Z_k^r : G ∩ (0, T] ≠ ∅ }. Finite: if t_1 < ... < t_M are the distinct real zeros of Xi_k in (0, T], then #𝒢_k(T) <= M + 1 (consecutive members of 𝒢_k(T) are separated by at least one t_i). Note the leftmost member ("origin gap") extends below 0: for k even it is symmetric (-t_1, t_1) if Xi_k(0) != 0; for k odd, Xi_k(0) = 0 (odd function) and the origin gap is (0, t_1). The rightmost member overhangs T: G_last = (t_M, t_{M+1}) with t_{M+1} > T the next real zero above T. Both are legal bounded gaps; no special-casing is needed and none is done.
- Overhang interval of a pair: I_j := [x_j - y_j, x_j + y_j] (closed). A pair OVERHANGS the gap G = (a,b) iff int I_j ∩ G ≠ ∅, i.e. x_j - y_j < b and x_j + y_j > a. (Open condition: touching only at an endpoint does not count; the excitation mechanism in §3 needs an interior point.)
- Per-pair-per-gap weight: omega(j, G) := min( 1, |G|^2 / (4 y_j^2) ).

**FINAL DEFINITION (weighted close-pair functional):**
  W_k(T) := Sum_{G in 𝒢_k(T)} Sum_{pairs j of Xi_k, with multiplicity, overhanging G} min(1, |G|^2/(4 y_j^2)).
The inner sum runs over ALL pairs of Xi_k (any sign of x_j, including x_j = 0 and x_j > T); the overhang condition is the only localization. A pair overhanging several gaps contributes one term PER GAP it overhangs — the overhang multiplicity is baked into the double sum, so no separate "overhang factor" is ever needed downstream; this is the bookkeeping choice that makes the per-gap dipole bound sum with NO loss (see §4, one line). W_k(T) is nondecreasing in T.

Normalized quantities:
  kappa_k(T) := N_k^r(T)/N_k(T); kappa_k := liminf_{T->inf} kappa_k(T) in [0,1];
  w_k := limsup_{T->inf} W_k(T)/N_0(T) in [0, +infinity].
(w_k is normalized by N_0, the rung-0 total count = classical N(T); by B1 Cor 2.1 any fixed rung's N_k could be used equivalently, but N_0 is the deposit convention.)

Remark (why the y-normalization 4y^2): with this normalization the threshold lemma of §3 is exactly "total gap weight >= 1 whenever the gap is excited", i.e. the weight measures "fraction of the excitation threshold 8/g^2 that the pair can supply", since max phi_j' = 2/y_j^2 and (2/y_j^2)/(8/g^2) = g^2/(4y_j^2).

## §2 INTERFACES (exact statements consumed)

**[I-CONS] Conservation (B1 Thm 2, L-105062):** for every k there are explicit A_k, B_k, T_k (admissible A_k = 70 + 6k) with |N_{k+1}(T) - N_k(T)| <= A_k log T + B_k for T >= T_k. Also B1 Cor 2.1: N_k(T) = (T/2pi) log(T/2pi) - T/2pi + O_k(log T), hence N_k(T) >= (T/7) log T for T >= explicit T_k', and N_{k+1}(T)/N_0(T) -> 1.

**[I-ROLLE] Rolle floor (B1 Thm 3):** N_{k+1}^r(T) >= N_k^r(T) - 1. (Not consumed by the descent inequality itself, but by the monotone-ladder side; recorded for completeness.)

**[I-DIPOLE] Dipole interface (L-105061 — B2's deliverable; UNPROVED at assembly time; pinned form):**
There is an absolute constant A' >= 1 such that for every k >= 0 and every gap G of Xi_k (bounded component of R \ Z_k^r):
  n_k'(G) := #{ real zeros of Xi_{k+1} in G, with multiplicity } <= 1 + A' * Sum_{pairs j of Xi_k overhanging G} min(1, |G|^2/(4 y_j^2)).
Equivalently extra(G) := max(n_k'(G) - 1, 0) <= A' * (gap weight). Target A' = 4 per orchestrator; ANY absolute A' is accepted by the assembly and is carried symbolically. The statement must hold for every gap, including the origin gap and gaps overhanging T. NOTE for B2: the support structure (only overhanging pairs matter) and the excitation threshold are PROVED in §3 below modulo the convergence layer [I-PF]; what remains for B2 is ONLY the per-gap COUNT cap (§3 Rem 3).

**[I-PF] Partial-fraction layer (sub-interface of L-105061, B2):** for F = Xi_k, on any gap G,
  (F'/F)'(t) = - Sum_{t_n in Z_k^r} m_n/(t - t_n)^2 + Sum_{pairs j, mult} phi_j'(t),  phi_j'(t) = 2(y_j^2 - (t-x_j)^2)/(((t-x_j)^2 + y_j^2))^2,
absolutely and locally uniformly convergent on R \ Z_k^r. (Route: B1 §1's genus-0 square-variable Hadamard product Xi_k(t) = c t^m prod (1 - t^2/tau_n^2) gives F'/F(t) = m/t + Sum_n [1/(t-tau_n) + 1/(t+tau_n)] with symmetric grouping; differentiating termwise — justified by local uniform convergence — and regrouping each tau_n with its conjugate yields exactly the displayed formula, constants dead. Convergence: Sum |tau_n|^{-2} < infinity from order < 1 of the square-variable function. This is essentially proved by B1's §1 machinery; B2/B1 to co-sign. I verify it numerically for polynomials — where it is an identity — in §5.)

**[I-EXT] External classical input (label EXTERNAL-CLASSICAL, do NOT re-prove):** kappa_k -> 1 as k -> infinity. Source: J. B. Conrey, "Zeros of derivatives of Riemann's xi-function on the critical line", J. Number Theory 16 (1983), 49–74 (proportion of zeros of xi^{(m)} on the critical line tends to 1 as m -> infinity; his count is zeros with 0 < Im s <= T of xi^{(m)}, with multiplicity, which under s = 1/2 + it is exactly our N_m / N_m^r convention — Re t = Im s ... precisely: a zero s = beta + i gamma of xi^{(m)} corresponds to t = gamma + i(1/2 - beta), so 0 < gamma <= T is 0 < Re t <= T; on-line beta = 1/2 is t real). Deposit slot: exact quantitative form to be transcribed from the paper at deposit time; only kappa_m -> 1 is consumed.

**[I-BASE] Imported baseline (Zeta23):** liminf_T (on-line proportion at rung 0) >= 0.67250 (distinct/simple version), i.e. kappa~_0 >= 0.67250 in B1's distinct-count notation. Repo coordinates: to be attached by orchestrator per Packet 10 (canonical extraction plan) — external Zeta23 provenance; I did not locate a claim file carrying the constant 0.67250 in the repo tree (searched); the deposit must attach the four coordinates or downgrade the baseline mention to a placeholder. Used ONLY in the honest-scope discussion, not in any proof here.

## §3 What I PROVE toward the dipole layer (support + threshold), modulo [I-PF]

Fix k, F := Xi_k, and a gap G = (a,b), g := b - a. All statements assume [I-PF].

**Lemma 3.1 (background repulsion).** For t in G: Sum_n m_n/(t-t_n)^2 >= 1/(t-a)^2 + 1/(b-t)^2 >= 8/g^2.
Proof: keep only the endpoint terms (a, b in Z_k^r, m >= 1); u := t-a in (0,g): 1/u^2 + 1/(g-u)^2 is minimized at u = g/2 with value 8/g^2. QED.

**Lemma 3.2 (support).** phi_j'(t) > 0 iff |t - x_j| < y_j, i.e. iff t in int I_j; max phi_j' = phi_j'(x_j) = 2/y_j^2; min phi_j' = phi_j'(x_j +- sqrt(3) y_j) = -1/(8 y_j^2) * ... exact: phi_j'(x_j + u) = 2(y^2-u^2)/(u^2+y^2)^2, at u^2 = 3y^2 gives 2(-2y^2)/(16 y^4) = -1/(4y^2). (Orchestrator's -1/(4y^2) at line 104 re-derived: CORRECT; their line-103 fragment "-2/(8y^2)" was garbage, final value right.)
Proof: elementary calculus on the displayed formula. QED.

**Lemma 3.3 (threshold).** If (F'/F)' has a zero at t* in G, then Sum_{j overhanging G} min(1, g^2/(4 y_j^2)) >= 1.
Proof: at t*, Sum_j phi_j'(t*) = Sum_n m_n/(t*-t_n)^2 >= 8/g^2 (Lemma 3.1). Only j with t* in int I_j contribute positively (Lemma 3.2), and each contributes at most 2/y_j^2; discarding negative contributions, Sum_{j: t* in int I_j} 2/y_j^2 >= 8/g^2, i.e. Sum_{those j} g^2/(4 y_j^2) >= 1. Those j overhang G (t* in int I_j ∩ G). Finally Sum min(1, c_j) >= min(1, Sum c_j) >= 1 (if every c_j < 1 the min is the identity; otherwise some term already equals 1). QED.

**Corollary 3.4 (qualitative dipole).** If extra(G) >= 1 then the gap weight Sum_{j overhang G} min(1, g^2/(4y_j^2)) >= 1.
Proof: F != 0 on G, so real zeros of F' in G = zeros of F'/F in G (same multiplicities). If F'/F has z zeros in G with multiplicity, at p distinct points with mults mu_i, then (F'/F)' has >= Sum(mu_i - 1) + (p - 1) = z - 1 zeros in G (mult drop + Rolle between consecutive distinct zeros). So z >= 2 forces a zero of (F'/F)' in G; apply Lemma 3.3. QED.

**Remark 3.5 (what remains for B2 = the count cap).** Corollary 3.4 gives extra(G) >= 1 => weight >= 1, which is [I-DIPOLE] restricted to "detecting one extra zero". The full [I-DIPOLE] needs: extra(G) <= A' * weight also when extra(G) is LARGE — i.e. a cap on #zeros of (F'/F)' in G by A' * (number/weight of overhanging pairs). Every zero of (F'/F)' lies in the "excited set" E_G := {t in G : Sum phi_j'(t) >= 8/g^2} ⊆ union of int I_j — but one I_j can a priori contain several zeros of (F'/F)'; bounding that count (by winding, variation, or measure of E_G + a derivative bound) is exactly B2's open burden. The assembly below consumes only the pinned [I-DIPOLE]; if B2 lands a different weight shape (e.g. an extra absolute constant, or I_j fattened to [x_j - cy_j, x_j + cy_j]), the assembly goes through verbatim with W_k redefined with that weight — the summation layer (§4) is shape-agnostic as long as the weight is per-(pair,gap).

**Rolle lower bound per gap (unconditional):** n_k'(G) >= 1 for every gap (Rolle on [a,b]). So extra(G) = n_k'(G) - 1 >= 0 always; max(.,0) in the definition is belt-and-braces.

## §4 (b) THE DESCENT INEQUALITY

**Proposition 4.1 (converse Rolle with priced defect).** Assume [I-DIPOLE] with constant A'. Then for every k >= 0 and every T > 0:
  N_{k+1}^r(T) <= N_k^r(T) + 1 + A' * W_k(T).

Proof. Let t_1 < ... < t_M be the distinct real zeros of Xi_k in (0,T], multiplicities m_1..m_M (if M = 0 the argument below still runs with the empty first bucket). Partition the real zeros of Xi_{k+1} in (0, T] into two buckets:
(1) At points of Z_k^r ∩ (0,T] = {t_i}: Xi_{k+1} = Xi_k' vanishes at t_i iff m_i >= 2, and then with multiplicity exactly m_i - 1 (real-analytic mult drop). Bucket total = Sum_i (m_i - 1) = N_k^r(T) - M.
(2) At points of (0,T] \ Z_k^r: each such zero lies in a unique component of R \ Z_k^r meeting (0,T], i.e. in a unique G in 𝒢_k(T); it is counted (with multiplicity) inside n_k'(G). Bucket total <= Sum_{G in 𝒢_k(T)} n_k'(G). (Inequality, not equality: a gap in 𝒢_k(T) may stick out of (0,T] and n_k'(G) counts its whole interior — slack only helps.)
By [I-DIPOLE], Sum_G n_k'(G) <= #𝒢_k(T) + A' Sum_{G in 𝒢_k(T)} (gap weight) = #𝒢_k(T) + A' W_k(T) — this single line is where the W_k definition pays: the double-sum definition makes the per-gap bounds ADD WITH NO OVERHANG LOSS. With #𝒢_k(T) <= M + 1:
  N_{k+1}^r(T) <= (N_k^r(T) - M) + (M + 1) + A' W_k(T) = N_k^r(T) + 1 + A' W_k(T). QED.

(Boundary audit: the origin gap and the T-overhanging gap are ordinary members of 𝒢_k(T); the count #𝒢 <= M+1 covers them; W_k includes their weights — its pair sum reaches pairs with x_j slightly beyond T (at most x_j < t_{M+1} + 1/2) and slightly below 0; no term is dropped and none double-counted. For k even the origin gap is (-t_1, t_1): zeros of the ODD function Xi_{k+1} in it come in +-pairs plus 0 itself, but 0 and negative ones are outside (0,T], so bucket (2) counts at most n'(G_0) of them — slack again.)

**Theorem 4.2 (DESCENT INEQUALITY, deposit form).** Assume [I-DIPOLE] (constant A') and [I-CONS] (constants A_k, B_k, T_k). Then for every k >= 0 and all T >= T_k:
  N_k^c(T) <= N_{k+1}^c(T) + A' * W_k(T) + A_k log T + (B_k + 1).
Admissible A_k = 70 + 6k (B1); A' target 4.

Proof. N_k^c - N_{k+1}^c = (N_k - N_{k+1}) + (N_{k+1}^r - N_k^r) <= (A_k log T + B_k) + (1 + A' W_k(T)) by [I-CONS] and Prop 4.1. QED.

**Corollary 4.3 (iterated).** For every K >= 0 and T >= T_K^* := max_{k <= K} T_k:
  N_0^c(T) <= N_{K+1}^c(T) + A' Sum_{k=0}^K W_k(T) + S_K log T + S_K',
  with S_K := Sum_{k<=K} A_k = 70(K+1) + 3K(K+1) (admissible), S_K' := Sum_{k<=K} (B_k + 1).
(Fixed K: both S_K, S_K' are T-independent constants.)

## §5 (c) MASTER COROLLARY

**Theorem 5.1 (finite-K master, no external input).** Assume [I-DIPOLE] + [I-CONS]. For every fixed K >= 0:
  1 - kappa_0 <= (1 - kappa_{K+1}) + A' Sum_{k=0}^{K} w_k.
(If some w_k = +infinity the right side is +infinity and the statement is vacuously true.)

Proof. Divide Cor 4.3 by N_0(T) > 0 (T large) and take limsup_{T->infinity}. Left side: N_0^c/N_0 = 1 - kappa_0(T), and limsup(1 - kappa_0(T)) = 1 - liminf kappa_0(T) = 1 - kappa_0 (exact identity). Right side, superadditivity of limsup over a FINITE sum of nonnegative terms: limsup Sum <= Sum limsup. Term by term:
- N_{K+1}^c(T)/N_0(T) = (1 - kappa_{K+1}(T)) * (N_{K+1}(T)/N_0(T)); by [I-CONS] N_{K+1}/N_0 = 1 + O_K(log T / N_0(T)) -> 1 (B1 Cor 2.1: N_0(T) >> T log T); limsup of the product = limsup(1 - kappa_{K+1}(T)) * 1 = 1 - kappa_{K+1} (product rule for limsup with one factor convergent to 1 and both nonnegative).
- A' W_k(T)/N_0(T): limsup = A' w_k by definition (finite sum of K+1 terms).
- (S_K log T + S_K')/N_0(T) -> 0.
Assemble. QED.

**Theorem 5.2 (MASTER COROLLARY, with external input).** Assume [I-DIPOLE], [I-CONS], and [I-EXT] (kappa_k -> 1, EXTERNAL-CLASSICAL, Conrey 1983). Then
  1 - kappa_0 <= A' * Sum_{k=0}^{infinity} w_k,
with the convention: if Sum w_k = +infinity the inequality is TRIVIALLY TRUE and the theorem asserts nothing (stated plainly; the entire content lives in the case Sum w_k < infinity, which is NOT proved here and is the open successor problem).

Proof (double limit handled rigorously). Theorem 5.1 holds for EVERY fixed K — each instance is already a statement about extended-real NUMBERS, the T-limit having been taken inside. Let S := Sum_{k>=0} w_k in [0, +infinity] (monotone limit of the partial sums S_K^w := Sum_{k<=K} w_k, each term nonnegative). For every K: 1 - kappa_0 <= (1 - kappa_{K+1}) + A' S_K^w <= (1 - kappa_{K+1}) + A' S. Let K -> infinity: by [I-EXT], 1 - kappa_{K+1} -> 0, so 1 - kappa_0 <= inf_K [(1 - kappa_{K+1}) + A' S] = A' S. No interchange of the T- and K-limits ever occurs: the order is T first (inside Thm 5.1), then K, and the K-limit is applied to a family of true numerical inequalities. QED.

**Proposition 5.3 (RH-side sanity check).** If RH holds, then for every k all zeros of Xi_k are real; hence Xi_k has no pairs, W_k(T) = 0 for all T, w_k = 0 for all k, and both sides of Theorem 5.2 are 0 (RH => kappa_0 = 1 trivially). Consistency, not new information.
Proof. RH => all zeros of Xi real => Xi is in the Laguerre–Pólya class LP: indeed Xi is real entire, even, order 1, so by Hadamard (genus <= 1, and by evenness + B1 §1's square-variable argument genus 0 in t^2) Xi(t) = Xi(0) prod_n (1 - t^2/t_n^2) with all t_n real, absolutely convergent — this is an LP form (Levin, Distribution of Zeros of Entire Functions, Ch. VIII).
LP closure under differentiation — **Laguerre's theorem** (Laguerre; Pólya–Schur, J. reine angew. Math. 144 (1914); Levin Ch. VIII): if f in LP then f' in LP; in particular f' has only real zeros. Proof of the step as used: by the Laguerre–Pólya approximation theorem (Levin Ch. VIII Thm 1), f = lim p_n locally uniformly with p_n real polynomials having only real zeros. Then p_n' -> f' locally uniformly (Cauchy integral formula on compacts). Each p_n' has only real zeros (Rolle + multiplicity drop for real polynomials — or Gauss–Lucas: zeros of p_n' in the convex hull of the real zero set, hence real). Suppose f'(z_0) = 0 with Im z_0 != 0; f' not identically 0 (f nonconstant: Xi has zeros and is even entire of order 1). Hurwitz on the disk D(z_0, |Im z_0|/2) (f' not identically zero, p_n' -> f' loc. unif.) gives zeros of p_n' in that disk for large n — but that disk misses R. Contradiction; so f' has only real zeros, and (being a loc.-unif. limit of real polynomials with only real zeros) f' in LP, closing the induction Xi_k in LP for all k. QED.

## §6 (d) HONEST SCOPE (deposit section draft)

1. RH is NOT addressed. Nothing here bounds any w_k; a priori w_k may be +infinity (trivial estimates give only W_k(T) = O(N_k^c(T) log T) = O(T log^2 T), which does not even make W_k(T)/N_0(T) bounded). If Sum w_k = +infinity, Theorem 5.2 is vacuous. Bounding even a single w_k unconditionally is the open successor problem; the theorem's entire value is the exact isolation and pricing of the defect in Levinson's converse-Rolle heuristic.
2. Not a new proportion for zeta: the descent inequality CONSUMES lower bounds on kappa_{K+1} (Conrey) and would PRODUCE a lower bound on kappa_0 only if Sum w_k were bounded — which is not proved. The imported Zeta23 baseline kappa~_0 >= 0.67250 flows the OTHER way: B1's monotone ladder (Thm 4) pushes it UP the ladder (kappa~_k >= 0.67250 for every k, unconditionally); the descent inequality prices the return trip down. The two directions are complementary and neither is circular: ladder up = unconditional, descent down = priced by W.
3. Conditionality ledger: Theorem 4.2 / 5.1 / 5.2 are CONDITIONAL on [I-DIPOLE] (B2, unproved at assembly; support + threshold structure proved here in §3 modulo [I-PF]) and consume B1's proved [I-CONS]. [I-EXT] is external-classical (Conrey 1983). Unconditional-as-deposited content of this lane: §3 Lemmas 3.1–3.4 (modulo [I-PF]), Prop 4.1's bookkeeping (given [I-DIPOLE]), Prop 5.3, and the stress-tested summation layer.
4. Speiser / Levinson–Montgomery context: Speiser (1934): RH iff zeta' has no zeros in 0 < Re s < 1/2. Levinson–Montgomery (1974): zeta and zeta' have the same number of zeros in 0 < Re s < 1/2 up to O(log T) — the ancestor of [I-CONS]; their qualitative converse-Rolle counting is here made quantitative on the xi-ladder in the t-variable with the defect isolated as W_k. Conrey (1983) showed the high rungs are asymptotically fully real; Theorem 5.2 says exactly what stands between Conrey's kappa_infinity = 1 and the desired kappa_0 = 1: the summed close-pair weight along the ladder.
5. The strip constraint y_j <= 1/2 means every pair's overhang interval has length <= 1; at height x the mean real gap is ~ 2pi/log x, so a single pair can overhang up to ~ (log x)/pi + 2 gaps, each with weight <= 1: W_k is NOT trivially comparable to P_k; the definition deliberately charges per (pair, gap) incidence because that is what the per-gap dipole bound sums to. Any future improvement of [I-DIPOLE]'s weight shape transfers verbatim (§3 Rem 3.5).
6. Multiplicity: all counts with multiplicity; B1 also proved the distinct-zeros ladder (their Thm 3'), and the baseline import is a distinct/simple count — definition matching for the baseline is B1 §4 Remark + orchestrator's Packet-10 coordinates duty. The descent inequality itself is a multiplicity statement.

## §7 Orchestrator-note discrepancies found (B3 pass)

(i) Note line ~104: "phi' min = -2/(8y^2)?" — re-derived: min phi_j' = -1/(4 y_j^2) at |t-x_j| = sqrt(3) y_j (their final value was right, the intermediate wrong).
(ii) Note §6 line ~146: "g_j := length of the gap(s) that I_j meets ... define W with local mean gap??" — REJECTED: defining W per pair with a single g_j is ambiguous when a pair overhangs several gaps of different lengths; the per-(pair,gap) double sum (§1) is the form that telescopes with zero loss. This is the main convention-layer fix of this lane.
(iii) Note §6 line ~144: "N_{k+1}^r <= N_k^r + 1 + X_k" — correct as stated ONLY with the extended gap list including origin and T-overhang gaps (else the last gap's zeros are unaccounted and can exceed any O(log T) budget: unconditionally the last real-zero gap below T can be as long as ~ T^{1/4}, so its F'-zeros CANNOT be absorbed into C_k log T; they must be, and here are, priced inside W_k). This is a real trap the note did not flag.
(iv) The "+1" in Prop 4.1 (not present in some drafts of the note's §6) comes from #𝒢 <= M + 1; it is absorbed into B_k + 1 in Thm 4.2.
(v) B1's corrections to the note (their §6.5: false o(1) on the edge; orientation; failed positivity route) independently confirmed as issues by reading; not re-litigated here.

## §8 (e) STRESS TESTS OF THE BOOKKEEPING — results (code: stress_tests.py, exact_check.py, dissect.py; ledger: results.json)

Method: synthetic real polynomials F with KNOWN real zeros (with multiplicity) and known conjugate pairs; differentiate 1–2 times; roots of F', F'' by (i) numpy float64 and (ii) EXACT rational coefficients + mpmath polyroots at 60 dps; every quantity of §1/§4 computed on an explicit window; every inequality checked, plus two consistency invariants: per-gap parity (#zeros of F' in a gap is ODD, since F'/F runs +inf -> -inf) and the exact partial-fraction identity [I-PF] (identity for polynomials; verified to rel. err <= 4e-10 — validates the phi'_j formula and all sign conventions of §3).

Headline table (exact arithmetic; window counts N/N^r/N^c at rungs k and k+1; W, X = sum of extras; all of Rolle-per-gap, parity, threshold (Cor 3.4), dipole with A'=4, converse Rolle (Prop 4.1), descent (Thm 4.2 shape) checked):

| config | rung-k (N,N^r,N^c) | rung-k+1 | W_k | X_k | worst extra/weight | all checks |
|---|---|---|---|---|---|---|
| A all-real-simple (2 rungs) | (5,5,0) | (4,4,0) | 0 | 0 | – | OK |
| B pair annihilation | (4,2,2) | (3,3,0) | 1.0 | 2 | 2.0 | OK |
| C 1 pair overhanging 6 gaps | (7,5,2) | (6,4,2) | 2.198 | 0 | – | OK |
| D double real zero + pair | (5,3,2) | (4,4,0) | 1.0 | 2 | 2.0 | OK |
| E pair of multiplicity 2 | (6,2,4) | (5,3,2) | 2.0 | 2 | 1.0 | OK |
| F even parity, window (0,T] | (4,2,2) | (3,3,0) | 1.0 | 2 | 2.0 | OK |
| G deep pair y=g | (7,5,2) | (6,4,2) | 0.5 | 0 | – | OK |
| H tiny pair, gap 0.147 (2nd rung) | (4,2,2) | (4,4,0) | 1.0 | 2 | 2.0 | OK |
| MIXED double real + double pair | (11,5,6) | (10,6,4) | 3.0 | 2 | 1.0 | OK |
| TRIPLE real zero + pair | (8,6,2) | (7,7,0) | 1.0 | 2 | 2.0 | OK |

Mandatory configs from the tasking, each verified:
- **Pair overhanging 3+ gaps** (config C): one pair (x=1.4, y=0.45) overhangs SIX gaps; its per-(pair,gap) charges (1.0, .049, .049, .049, .049, 1.0) all enter W; per-gap dipole bound holds in each; the double-sum definition absorbs the overhang multiplicity with no extra factor. Second rung re-runs the whole machinery on F' with its own (moved) pair: OK.
- **Pair annihilation** (configs B, E, F, TRIPLE): F has pairs, F' has NONE (N^c drops 2 or 4 -> 0), while N^r JUMPS UP (e.g. 6 -> 7). The descent direction survives exactly because the jump in N^r is priced by A'W: e.g. B: N_{k+1}^r = 3 <= N_k^r + 1 + 4W = 2+1+4 ✓, and the per-gap ledger localizes it (gap (4,6): n'=3, extra=2 <= 4·weight=4).
- **Multiple real zeros** (D, MIXED, TRIPLE): multiplicity-drop bookkeeping (m -> m-1 AT the point, gap structure from DISTINCT zeros) exact; TRIPLE needed exact deflation of the double root of F' — polyroots cannot converge on multiple roots, recorded as a tooling note.

Random searches: (i) float64, 400 trials: 6 flagged "violations" — ALL exposed as float64 root-finder artifacts (one flagged gap had an EVEN number of F'-zeros, parity-impossible; degree-18 coefficient rounding moves clustered roots and flips real/complex classification). Re-audit of all flagged trials with exact coefficients: every inequality holds. (ii) EXACT arithmetic, 250 fresh trials (6–10 real zeros, 1–3 pairs, y in [.05,.5]): 0 violations of any of {Rolle>=1, parity, threshold, dipole A'=4, converse Rolle, descent}; classification margins clean. LESSON for the census lane: float64 root classification is NOT deposit-grade; exact/high-precision arithmetic is mandatory (mirrors the note's §7 budgeted-arithmetic discipline).

Adversarial battery targeting the orchestrator's "cooperation" fear (§8(ii) of the note): m = 3..10 pairs at the strip cap y = 1/2 over a gap g = 0.6 (per-pair weight 0.36 < 1): the extras SATURATE at 2 however many pairs cooperate (merged excitation makes one dip, not many); ratio extra/weight peaks at 1.85 (m=3) and DECREASES in m. Stacked near-real pairs realize the extremal ratio: extra = 2m, weight = m, ratio exactly 2. **Empirical maximum of extra(G)/weight(G) over every test ever run: 2.0.** Working conjecture for B2: the sharp constant is A' = 2 (i.e. extra(G) <= 2·#overhanging-pairs-weighted); the pinned A' = 4 held with a factor-2 margin in every experiment. Threshold lemma (Cor 3.4) never violated: no gap with extra >= 1 ever had weight < 1; single sub-threshold pairs (weight < 1 alone) never produced any extra zero.

Cross-check on the actual Xi ladder: B1's census (laneB1/results.json, 40 dps): all zeros of Xi_0..Xi_3 in [2,100]x[-1,1] are REAL (winding = sign-change count), so W_k = 0 on that range and the descent inequality is trivially consistent there (conservation breathing |N_{k+1}-N_k| <= 1 observed).

## §9 (f) DRAFT CLAIM FILE TEXT (deposit; DO NOT write into repo from this lane)

---DRAFT BEGINS---

# T-105060 — The Levinson descent ladder: off-line mass at rung 0 is priced by summed close-pair weight, modulo the dipole interface

Claim ID: `T-105060`
Status: **CONDITIONAL THEOREM (assembly complete and stress-tested; consumes L-105062 [proved, lane B1], L-105061 [dipole interface — OPEN, lane B2], and one EXTERNAL-CLASSICAL input]; RH NOT ADDRESSED**
Depends on: `L-105062` (strip + conservation + Rolle floor + monotone ladder), `L-105061` (dipole lemma, open interface), EXTERNAL-CLASSICAL: Conrey 1983 (kappa_k -> 1), [optional context] imported Zeta23 baseline per Packet-10 coordinates.
RH status: unproved, not addressed.

## Statement

Setting: Xi_k(t) := (d/dt)^k xi(1/2+it) · i^{-k}... (convention: Xi_k := (d/dt)^k Xi, Xi(t) = xi(1/2+it)); counts N_k, N_k^r, N_k^c on 0 < Re t <= T with multiplicity, Re t = 0 excluded; gaps = bounded components of R minus the real zero set of Xi_k; pair (x_j, y_j) overhangs gap G=(a,b) iff x_j - y_j < b and x_j + y_j > a;

  W_k(T) := Sum_{gaps G meeting (0,T]} Sum_{pairs j of Xi_k overhanging G, mult} min(1, |G|^2/(4 y_j^2)),
  kappa_k := liminf_{T} N_k^r(T)/N_k(T),   w_k := limsup_T W_k(T)/N_0(T).

(a) [DESCENT] Assume L-105061 with constant A'. Then for every k and T >= T_k (T_k, A_k, B_k from L-105062; A_k = 70+6k admissible):
  N_k^c(T) <= N_{k+1}^c(T) + A'·W_k(T) + A_k log T + (B_k + 1).
(b) [FINITE-K MASTER] For every fixed K: 1 - kappa_0 <= (1 - kappa_{K+1}) + A'·Sum_{k<=K} w_k.
(c) [MASTER COROLLARY] Admitting additionally the EXTERNAL-CLASSICAL input kappa_k -> 1 (Conrey, J. Number Theory 16 (1983) 49–74):
  1 - kappa_0 <= A' · Sum_{k>=0} w_k,
  VACUOUS when the right side diverges — the content is confined to the (unproved) case Sum w_k < infinity.
(d) [RH-SIDE CONSISTENCY] If RH holds, every Xi_k is Laguerre–Pólya (Laguerre's theorem: LP closed under differentiation), all W_k = 0, w_k = 0, and both sides of (c) vanish.

## Proof skeleton (interface slots marked ▸)

1. ▸[L-105062 §1] all zeros of Xi_k in |Im t| <= 1/2; real zeros unbounded both ways (Hardy + Rolle floor + parity) => every gap bounded, gap list of (0,T] finite (<= M+1 members incl. origin gap and T-overhanging gap).
2. Partition real zeros of Xi_{k+1} in (0,T]: at real zeros of Xi_k (multiplicity drop, exactly Sum(m_i - 1)) + inside gaps meeting (0,T]. ▸[L-105061] per gap: n'(G) <= 1 + A'·(gap weight). Summing — the per-(pair,gap) double-sum definition of W_k makes this LOSSLESS — gives the priced converse Rolle: N_{k+1}^r(T) <= N_k^r(T) + 1 + A'·W_k(T). [T-105060 Prop 4.1; boundary audit in lane notes §4.]
3. ▸[L-105062 §2] |N_{k+1} - N_k| <= A_k log T + B_k. Subtract: (a).
4. Iterate k = 0..K; divide by N_0(T); limsup with N_{K+1}/N_0 -> 1 [L-105062 Cor 2.1]: (b). Double limit T-then-K with ▸[EXTERNAL: Conrey]: (c). No limit interchange occurs (each finite-K statement is a numerical inequality before K -> infinity is taken).
5. (d): RH => Xi in LP (Hadamard, even, order 1); Laguerre's theorem (Pólya–Schur 1914; Levin, Distribution of Zeros, Ch. VIII): LP closed under d/dt via polynomial approximation + Hurwitz; no pairs at any rung.

Supporting lemmas proved in-lane (modulo the convergence layer [I-PF] assigned to L-105061): background repulsion Sum m/(t-t_n)^2 >= 8/g^2 in a gap; support of phi'_j = int I_j with max 2/y_j^2, min -1/(4y_j^2); THRESHOLD: any gap with an extra zero of Xi_{k+1} has total weight >= 1.

## Honest scope
[= lane notes §6, items 1–6 verbatim: no bound on any w_k (possibly infinite; theorem then vacuous); consumes — does not produce — proportions; Zeta23 baseline travels UP the ladder unconditionally via L-105062 Thm 4 and is logically independent of the descent; conditionality ledger; Speiser/Levinson–Montgomery/Conrey context.]

## Falsifiers
(F1) A gap of some Xi_k with an extra real zero of Xi_{k+1} but total overhanging weight < 1 would refute the threshold lemma (hence [I-PF] or the strip lemma). Numerically probed: 250 exact-arithmetic random ladders + 10 adversarial families, zero violations; extremal ratio extra/weight = 2.0 (stacked near-real pairs).
(F2) A per-gap ratio extra/weight > A' = 4 anywhere refutes the pinned L-105061 as stated (assembly then re-runs with any valid A').
(F3) A certified Xi-census gap on which counts violate (a) at computable height refutes the assembly given its interfaces.
(F4) kappa_0 = 1 (all-but-o(1) of zeta zeros on the line) makes (c) empty; the claim is about the LADDER's pricing structure, not about zeta proportions per se.

# L-105061 — Dipole lemma (interface, OPEN): per-gap extra critical points are capped by overhanging close-pair weight
Pinned statement: exists absolute A' (target 4) s.t. for every k and every gap G of Xi_k: #{real zeros of Xi_{k+1} in G, mult} <= 1 + A'·Sum_{pairs j overhanging G} min(1, |G|^2/(4 y_j^2)). Includes sub-interface [I-PF] (absolutely convergent pair-form partial fraction for (Xi_k'/Xi_k)'). Status: OPEN (lane B2 unstaffed at assembly); support+threshold structure PROVED in T-105060's lane notes §3; count cap open. Empirical sharp constant appears to be 2.

# L-105062 — Conservation / strip / Rolle / monotone ladder
= lane B1's Theorems 1–4 with their constants (A_k = 70+6k admissible; RvM on every rung; distinct-zeros variant). Status: PROVED (lane B1 notes; independent numerical falsification pass at T <= 100).

---DRAFT ENDS---

## §10 Failed / rejected approaches (recorded)

1. Defining W per pair with "the length of the gap(s) it meets" (orchestrator note §6): ambiguous for multi-gap overhang; rejected for the per-(pair,gap) double sum. This was the main historical-style convention trap; the fix is what makes step 2 of the skeleton lossless.
2. Bounding the T-overhang boundary gap by O(log T) instead of pricing it inside W_k: FAILS unconditionally — the last real-zero gap below T can have length ~ T^{1/4} (no better unconditional bound available), and its Xi_{k+1}-zeros are NOT O(log T)-many a priori. Pricing it inside W_k (gap list includes the overhanging gap) is necessary; noted as trap (iii) in §7.
3. Attempting an unconditional count cap n'(G) <= 1 + 2·#zeros of (Xi_k'/Xi_k)' in G followed by a second partial-fraction descent on (Xi_k'/Xi_k)': infinite regress (the second log-derivative has no clean pair structure); abandoned — this is exactly where B2 must inject new analysis (winding/variation/measure of the excited set).
4. float64 stress harness as evidence: rejected after discovering parity-impossible gap counts from coefficient rounding at degree 18; all conclusions re-derived in exact arithmetic.
