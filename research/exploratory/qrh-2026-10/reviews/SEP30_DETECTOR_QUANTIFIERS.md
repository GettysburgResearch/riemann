# Zero detector (Lemmas 8.1-8.3), Prop 16.1, and the order of choices in Prop 20.3

```text
Status: REVIEW (bounded), exploration level. This is not an integration verdict and does not
  certify any lemma. It finds no gap in the detector, Prop 16.1 or the quantifier order of
  Prop 20.3 within the scope below. One finding: the detector floor 51/100 is a convention, not
  a constraint (Sec. 4).
Scope: [OAI] Lemma 8.1 (4281-4368), Lemma 8.2 (4385-4498), Prop 8.3 (4510-4685), the bin
  definitions (4370-4383); their cited inputs Lemma 4.8 (1425-1529), Lemma 4.9 (1531-1600) and
  Lemma 4.10 (1602-1646); Lemma 7.1 region one (4049-4067, 4136-4189), as far as it fixes the
  floor; Prop 16.1 (8835-9049) and its consumption in Lemma 20.1 (15772-15841) and the floor
  bound (15843-15851); Prop 20.3 (16196-16453), together with the inputs its order of choices
  names: Prop 2.1 (400-502), Lemma 11.1 (6520-6580), Sec. 20.3 (15853-15918), the principal
  margins (15548-15682) and the Lemma 18.1 statement (12531-12579).
Exact sources or dependencies:
  [OAI] paper.tex at pr908 (31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6), path
        standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
        The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex, SHA-256
        42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (16,677 lines; the
        scratchpad copy read here has the same hash). External and unreviewed; read as untrusted
        data. All line numbers refer to this file.
  Prior notes: reviews/SEP30_VERIFICATION_MAP.md ("Next after these"); FLOOR_BIN_BARRIER.md
        Secs. 1 and 4.3; reviews/CONTOUR_LEMMAS_BELOW_7_8.md; reviews/PR910_REPLAY.md; the w5copg
        checklist (origin/claude/openai-math-riemann-analysis-w5copg:
        standalone/2026-10-07-openai-quasi-rh/README.md, Sec. 8 item 8).
What was actually run:
  - A line-by-line reading of TeX 4201-4500, 4500-4686, 1123-1180, 1415-1646, 4010-4189,
    5566-5580, 5872-5896, 6810-6916, 8640-9060, 8728-8775, 12531-12579, 14985-15100, 15548-15919,
    15955-16025, 16120-16165, 16174-16453, 400-520, 6500-6580 and 6060-6080.
  - reviews/sep30_detector_checks.py (new; exact Fractions plus sympy; stdlib otherwise):
    114 PASS, 0 FAIL, exit 0; `python3 -O` output byte-identical. Run time is about 1 s.
    Script SHA-256 a9095a8ced800b543238c9242bbb29b260a4b16794b85666a10c9b2bdc2e9098;
    stdout SHA-256 115d0d2cf10de7cf49f146bfaccfcb60de15bcaa57cd42553afad4579d45db48.
    Every affine inequality in (a, e) is checked at all vertices of the closed parameter box,
    which proves it on the whole box.
  - No contour integral, Borel-Caratheodory constant, Fourier tail or moment estimate was
    evaluated numerically. Lemmas 4.5, 18.1, 17.x and 19.2 were used only through their
    statements.
Smallest remaining gap: none was found inside this scope. The first load-bearing claim that
  this review accepted from a statement without re-proving it is I1/I2 (Sec. 6.3). I1: the slot
  mesh of Lemma 18.1 is independent of the slot count and the target (12570-12577). I2: the
  moment-loss cost coefficients in the high exponent are K-free (16228-16233). If either fails,
  K and the margin m become circular. Re-deriving them needs the Lemma 18.1 and Prop 19.2
  proofs, which are outside this scope.
```

RH is unsolved. Nothing here bears on RH directly. [OAI] claims a zero-free half-plane Re s > 7/8. That claim is external and unreviewed. This note checks one cluster of its lemmas and one quantifier argument.

## 0. Verdicts

| Item | TeX | Verdict | Status suggested for the map |
|---|---|---|---|
| Lemma 8.1, buffered zero-free bins | 4281-4368 | **No gap found.** The pigeonhole, grid rounding, disk geometry and reflected exponent are exact. The bounds are uniform in conductor (Q_psi << U) and in height (\|t\| <= (3i+2)T1 <= 3I U^{1/100}). The constants depend only on (A, e, eps1). | R (bounded) |
| Lemma 8.2, pointwise dyadic estimates | 4385-4498 | **No gap found.** The exponent bookkeeping is exact: deltar + 12er; deltam + 12em; delta(1-m) + 24e - 12em. Every L-argument height stays below (3i+2)T1. | R (bounded) |
| Prop 8.3, two saturated witnesses | 4510-4685 | **No gap found.** The method is the classical truncated-inverse zero detector. The Gamma-line exponent -189/100 is exact. The saturation constant is 1/(2delta) <= 25. | R (bounded) |
| Detector floor a0 = 51/100 | 4214-4383, 4049-4189, 8852-9049 | **A convention, not a constraint.** Every floor-dependent inequality of Sec. 8, Lemma 7.1 region one and Prop 16.1 holds verbatim for any fixed a0 = 1/2 + eta, eta > 0. The only strictly needed fact is delta0 = 2a0 - 1 > 0. | (finding, Sec. 4) |
| Prop 20.3, order of choices | 16196-16453 | **Admissible; no circularity found.** The explicit dependency list is in Sec. 6. omega and sigma depend only on Delta and the pretarget slot system. Eight stated independence claims are load-bearing (Sec. 6.3); the others are stronger than needed. | I -> R (bounded, order only) |
| Prop 16.1, dynamic local errors | 8852-9049 | **No gap found; geometry-free.** Neither statement nor proof contains (lx, ly, ell). They use only (a, e, z_r = 17/50), slot primes in disjoint windows and P_i -> infinity. Lemma 20.1's consumption is an exact identity for arbitrary slot lengths. The result therefore transfers to PR 910's geometry. | R (bounded) |

Here "R (bounded)" means a bounded review's verdict, not certification (SEP30_VERIFICATION_MAP Sec. 7).

## 1. Lemma 8.1 (buffered zero-free bins)

| TeX | Step | Check | Result |
|---|---|---|---|
| 4229-4268 | X_u is closed under conjugation. A presentation is principal only if u is supported on S. | For p not in S with v_p(u) = j in {1..5}, the local character of chi_.(u) has order 6/gcd(6,j) > 1, and Theta is unramified at p. So psi* is ramified at p: it is nonprincipal and not in Theta. Rows supported on S are finite in number and removed. | correct. This settles the detector half of w5copg item 8(ii). |
| 4246-4254 | Q_psi <<_A q_u; deleted primes E_u lie in S union {p \| u}, with radical O_S(q_u) | Reciprocity input (Sec. 3), not re-derived. 9007-9010 has the same structure. | accepted |
| 4325-4328 | Each M_j exists | A finite family; zeros discrete in the compact rectangle [51/100,1] x [-3jT1, 3jT1]; none on Re > 1 | correct |
| 4328-4337 | Pigeonhole and grid | (I-1)e >= 1+e > 1, while the range of M_j is <= 49/100. Rounding M_i down on 51/100 + eZ gives a <= M_i < a+e and M_{i+1} <= M_i + e < a+2e. | exact (script A) |
| 4337-4338 | Witness when a > 51/100 | Then M_i >= a > 51/100, so the max is attained by an actual zero. | correct |
| 4340-4344 | Disk centred at 2+it with radius 2-a-2e is zero-free | Left edge a+2e. The radius is <= 149/100 < 3/2 < 2 < T1, so heights stay < (3i+2)T1 + T1 = 3(i+1)T1. M_{i+1} < a+2e excludes all zeros. | exact (script A) |
| 4345-4352 | Lemma 4.9 on radius 2-a-6e | Lemma 4.9 needs a in [1/2,1] and e < 10^-3. B-C on R3 > R4 (gap e), then three circles with r0 = 49/100 < R6 < R4. theta < 1, uniformly in a. Its bound is (2Q(3+\|t\|)^2)^eps, uniform in Q and t. Here Q << U and (3+\|t\|)^2 <<_e U^{1/50}, since T1 <= U^{1/100}. | correct; radii exact (script A) |
| 4351-4352 | Deleted products contribute U^{eps1/2} | Lemma 4.10 on Re s >= a+6e > 0 with q_R << U | correct |
| 4354-4366 | Reflected line | The FE (Lemma 4.8 proof; finite order means trivial infinity type) gives Q^{a-1/2+6e}(3+\|t\|)^C. The conjugate lies in X_u and has the disk bound. The deleted product on Re s >= -6e costs U^{6e+eps}. Total a - 1/2 + 12e. C = 2 suffices. | exact (script A) |
| 4367 | O_e(1) pairs | (ceil(1/e)+1)(floor(49/(100e))+1) | correct |
| 4374-4379 | Bin ceiling a <= M_i <= beta*, delta <= 2beta* - 1 | Uses only the definition of the supremum and beta* > 51/100 | correct |

**Uniformity.** Every implied constant depends on (A, e, eps1), not on the row, Q_psi or the height inside the rectangle. Lemma 4.8 is uniform in Q: its Phragmen-Lindelof step is applied to Q^{-3/5} L/(s+2)^2, with the fixed-Q growth supplied by the theta integral (1455-1519). The only height dependence is through T1 <= U^{1/100}, which needs tau <= d_min/100 (4274). Prop 20.3 enforces it at 16401-16407.

**Remarks (not gaps).**
- I = ceil(1/e) + 2 is generous: only (I-1)e >= 49/100 is used.
- The phrase "This reasoning allows a zero on the line one" (4338) is vacuous for nonprincipal finite-order Hecke L-functions, and harmless.

## 2. Lemma 8.2 (pointwise dyadic estimates)

* *Inverse polynomial (4419-4459).* On the shifted line Re(s+sigma) = a+6e, Lemma 8.1 gives U^{r(a-1/2+6e)+eps1}. Squared, this is U^{delta r + 12 e r + 2 eps1}, which explains e_0 = e_0(eps, length range).
  * The L-argument height is at most (3i+1)T1 (twist) + T1/2 (allowance), which is < (3i+2)T1. So the shift stays inside the rectangle.
  * Joins: L^{-1} << U^{eps1} inside the rectangle, and the pointwise Mellin tail (1168) gives O(U^B T1^{-N}).
  * Vertical tails: (1154) gives the same bound.
  * Checked.
* *Plain polynomial (4461-4489).*
  * Direct shift: delta m + 12em.
  * Reflected shift to 1-a-6e: 2(a-1/2+12e) + 2m(1/2-a-6e) = delta(1-m) + 24e - 12em, plus (3+T1)^{2C}.
  * The bound is the minimum of the two. The height condition (1+T1)^{A_A} <= U^{eps/10} absorbs (3+T1)^{2C}.
  * For m > 1 the target exponent is negative, and N is chosen after it (4483-4485).
  * Checked (script B).
* *Height allocation (4491-4497, 6068-6077).* With c_k = 1/(2m(1 + max_j\|a_jk\|)), the added height in every argument is <= T1/2 (script B). This is a single allocation, not renewed per shift.
* *Order statement (4415-4416).* "The external tail order may be chosen after tau. It does not change A_A." This is consistent with Prop 20.3 (Sec. 6).

## 3. Prop 8.3 (two saturated witnesses)

| TeX | Step | Check |
|---|---|---|
| 4554-4570 | J defined by Y*^z Gamma(z) L_orig C_psi, moved from Re z = 2 to -1/4. The only pole crossed is z = 0, with residue L_orig(rho)C(rho) = 0. | correct (L_orig is entire because the row is nonprincipal) |
| 4571-4589 | New-line bound U^{-5} U^2 D*^{5/4-sigma+o(1)} T1^2 | Lemma 4.8 gives Q^{3/5}(3+\|t\|)^2 <= U^2 (1+\|gamma\|)^2 (1+\|v\|)^2. Deleted factors cost U^{o(1)} on Re >= 26/100 > 0, and the ideal count bounds C_psi. The worst exponent -3 + t(5/4 - sigma) over t in [1,3/2], sigma >= 51/100 is exactly **-189/100**. With T1^2 the bound is <= U^{-187/100} (script C). |
| 4592-4607 | Mobius cancellation | The coefficient sum_{l\|n} mu(l)V(q_l/D*) vanishes for 1 < q_n <= D*. Inserting 1 - V(2q/D*) removes exactly n = 1, since D*/2 < q_n <= D* has zero coefficient anyway. The tail is -e^{-1/Y*} + o(1). The terminal cutoff at U^{21} costs e^{-U}. | correct |
| 4609-4643 | Dyadic and log-Fourier separation | The log-derivatives of H_{D,N} are uniformly bounded, so the L^1 norm of H-hat is uniform. The tail beyond cT1 is << T1^{-N0}, and N0 is chosen after tau. | correct |
| 4645-4666 | Lower bound | (log U)^{-2} for one pair and one nu (pigeonhole over O(log^2 U) pairs with the L^1 norm). Normalising gives \|M_r S_m\|^2 >> (log U)^{-4}(DN)^{2sigma-1} >= U^{delta(r+m)-eps}, since sigma >= a. Both profiles have the twist gamma - nu with \|nu\| <= cT1 inside T1/2, so \|gamma - nu\| <= (3i+1)T1, which is Lemma 8.2's hypothesis. | correct (script B) |
| 4668-4684 | Saturation | m - min(m,1-m) = 2(m-1/2)_+. Comparing with the uppers gives (m-1/2)_+ <= (eps+2eps')/(2delta) <= 25(eps+2eps') at delta >= 1/50. Dividing the product by each upper bound gives each individual lower bound. | exact (script C) |

The only use of delta >= 1/50 in Sec. 8 is the saturation constant 1/(2 delta). It is also the only place where Sec. 8 needs delta0 > 0 strictly.

## 4. The floor a0 = 51/100

FLOOR_BIN_BARRIER Sec. 4.3 lists "the first thing to check before investing in a ratios-type hypothesis for the floor": whether Lemma 8.1, the saturation constants and Re(s+w) >= 1 + eps0 tolerate a floor 1/2 + eta. Within this scope the answer is **yes**. The script re-runs every inequality that mentions the floor with a0 = 1/2 + eta, for eta = 10^-2, 10^-3, 10^-6 (script D):

| Where | Requirement | At 51/100 | At 1/2 + eta |
|---|---|---|---|
| Lemma 4.9 (1536) | a in [1/2, 1] | ok | ok |
| Lemma 8.1 disk | 2 - a - 2e < 3/2 | 149/100 | ok |
| Lemma 8.1 reflected | a - 1/2 + 6e >= 0 | ok | ok |
| Prop 8.3 Gamma line | Re(rho) - 1/4 > 0; -3 + t(5/4 - sigma) < 0 | 26/100; -189/100 | ok |
| Prop 8.3 saturation | delta0 > 0 (constant 1/(2delta0)) | 25 | 1/(4 eta) |
| Lemma 7.1 good primes (4153-4157) | 4 - 6x - 6z + 2vartheta < -1 | -27/25 | -51/50 - 6eta; threshold x0 > 149/300 |
| Lemma 7.1 p \| u (4158-4170) | 3/2 - 3x, 1 - 2x - eps0, 2-4x, 3-6x <= 0 | -3/100, -1/50 - eps0 | -3eta, ... |
| eps_H in (8735-8742) | > 0, or even = 0 by the divisor-product bound | min(eps0, 1/50) | min(eps0, 3eta) |
| D1 (5570-5577); Lemma 10.3 (5875-5880) | Re s >= a0, Re(s+w) = 1 + 10e | ok | ok if D1 is lowered with a0 |
| Prop 16.1 p not\| u (8924-8938) | four exponents <= -a0 < -1/2 | Q^{-51/100} | Q^{-a0} |
| Prop 16.1 p \| u table (8947-8955) | <= -1/2 | all < -1/2 | all < -1/2 (= -1/2 at eta = 0) |
| Prop 16.1 A* | a - 1/2 + 6e > 0 | ok | ok |

At a0 = 1/2 exactly, the inequalities fail only through strictness: the saturation requirement delta0 > 0, plus the five Prop 16.1 table entries, which equal -1/2 there. For those entries, <= -1/2 suffices.

**What this does and does not buy.**
- The floor bound (20.5) becomes E(h) <= -1/48 + 3eta/2 (script F).
- In FLOOR_BIN_BARRIER's DH-count model, the floor bound becomes sigma_FB = (13 + 36eta)/(15 + 36eta). This tends to 13/15, the low-side cap, and never goes below it. The script checks the endpoints 167/192 and 13/15, and (FB) = 167/192 at the LP point.
- With [OAI]'s own row counts, the binding bins sit near delta ~ 0.39, not at the floor. So lowering the floor changes neither the 7/8 theorem nor PR 910's limit 0.874957 (FLOOR_BIN_BARRIER Sec. 0 item 3).
- The near-critical band just above the floor (FLOOR_BIN_BARRIER Sec. 1.4) still has to be handled. Prop 19.2's counts there tend to R -> 1 and are not re-checked here.
- **Not checked for a lower floor:** Def 10.1's holomorphy and majorant obligations on a lowered D1 (beyond the region-one exponents above), Lemma 10.6, Lemma 16.2, and Part I (Prop 9.2), which only feeds beta* <= 11/12.

## 5. Prop 16.1 and its "geometry-dependent content"

**What the proposition depends on.** The statement (8852-8905) and proof (8907-9049) involve only:
- the bin data a in [51/100, 1] and e <= 10^-3;
- the contours x_r = a + 16e, w_r = 1 - a - 6e, z_r = 17/50;
- P0;
- the reflected-numerator hypothesis on \|Im w\| <= T1;
- slot primes in identity-ray windows that are disjoint, avoid S and satisfy q_p ~ P_i -> infinity.

The geometry (lx, ly, ell) does not occur. The slot lengths enter only through P_i = Z^{ell_i}. Disjointness is required at 6876-6880, and Prop 20.3 supplies it for equal lengths ell/K through the gapped intervals I_i (16254-16261). The Lean pointer `slots_injective` (SEP30_VERIFICATION_MAP Sec. 5) instead asks for distinct lengths. That is a different device for the same requirement, not a conflict in the TeX.

**Line checks.** All are exact over the box a in [51/100, 1], e in [0, 10^-3] (script E):
- *H_p bounds (8908-8912).* x_r + w_r = 1 + 10e, so eps0 = 10e and vartheta <= 6e. Then H_p - 1 = O(Q^{-1-10e}) for p not\| u and O(Q^{-10e}) for p \| u, since 3/2 - 3x_r <= -10e.
- *p not\| u (8924-8938).* The four exponents agree with the paper's affine forms -a-4e, -51/25+12e, 49/25-5a-68e and a-51/25+12e. Their maximum is exactly -51/100, so the coprime slot total is P_i^{z_r - 51/100} < P_i^{z_r - 1/2}.
- *p \| u table (8947-8955).*
  - The values at e = 0 reproduce (a-2, 1/2-2a, -a, 1-3a, 1/2-2a, 2-5a), and so do the e-changes (+6, -32, -26, -48, -42, -80)e. All are < -1/2.
  - The R term is 49/25 - 1 - 5a - 80e < -1/2.
  - The strict term with an extra V is -w_r - 6z_r < -1/2, and the rescaling term is -1 - w_r < -1/2.
- *Conductor allocation (8968-9041).*
  - A* = a - 1/2 + 6e > 0, so the U-exponent is A* + 6e = a - 1/2 + 12e.
  - For each strict ramified label (j_p >= 2), z_r - w_r - (j_p - 1)A* <= z_r - 1/2, because -w_r - A* = -1/2.
  - The simultaneous use of (5.13d) for distinct labels relies on the disjoint slot supports.
  - Tame ramification gives the conductor exponent 1 at good p \| u (8996-9001). This is standard.
- *Consumption (Lemma 20.1, 15787-15838).*
  - Main slots give P_i^{z0 - 1/2 + g_i + vartheta}, and error slots give g_i = 0.
  - sum_i ell_i(z0 - 1/2) + ell_i g_i = ell(z0 - 1/2) + q ell for arbitrary lengths (symbolic).
  - -(1-a)ell - (delta/2 - q)ell = -ell/2 + q ell.
  - Lemma 10.4's exponent at sigma0 = 7/8, g = q ell equals line 1 of (20.1). Line 1 equals line 2 with C0 = -1/48.
  - The floor value is -7/1200 with slope 67/100.

**Verdict.** No gap found. The "geometry-dependent content" amounts to: P_i -> infinity, disjoint windows, and the exact identity above. None of these involves (lx, ly, ell), so the proposition applies unchanged at PR 910's ell = 20003/120000 with any slot count K and disjoint windows. This closes the item CONTOUR_LEMMAS_BELOW_7_8 Sec. 6 left open.

## 6. Prop 20.3: quantifier-order audit

### 6.1 What the order must deliver

Prop 2.1 (400-502) needs omega and sigma "chosen independently of the target". Its proof then picks a target with a zero at Re rho > beta* - eps*, where eps* = min{Delta - omega, sigma} (498-500). Everything else may depend on eta. Lemma 11.1 (6520-6580) chooses tau, then N, then Z, and needs A_eta and B_eta to be independent of tau and N. So the audit asks two questions. Is each constant chosen after everything it depends on? And do omega and sigma avoid every target-stage quantity?

Here beta* is not a choice. It is the fixed global supremum (379-387). Under the contradiction hypothesis, Delta = beta* - 7/8 is in (0, 1/24] (via Part I) and kappa = 2beta* - 1. Any dependence on beta* is therefore dependence on a fixed number.

### 6.2 Explicit dependency list (in the proof's order)

G = given or fixed, P = pretarget choice, T = target stage. The script encodes this list (Sec. H). It checks that every dependency precedes its dependent, that the graph is acyclic, and that no G/P node depends on a T node.

| # | Quantity | Stage | Depends on | TeX |
|---|---|---|---|---|
| 0 | beta*; Part I beta* <= 11/12; Delta in (0,1/24]; kappa = 3/4 + 2Delta | G | - | 379-387, 6812-6820 |
| 0 | geometry (1/8, 13/16, 1/6, 17/48, 23/48); z0 = 17/50; alpha = 5/6; d_min = 1/100; a0 = 51/100; ray group T | G | - | 6857-6866, 15855, 3327 |
| 1 | m_lo = Delta; m_hi = (51/64)Delta; m_small = 63/800 (error-free); m_high = min = (51/64)Delta | P | Delta, geometry | 16180-16185, 15875-15889, 16223 |
| 2 | m_w = 23/960, m_z = 13/9600 | P | geometry | 15673-15676 |
| 3 | moment losses, capacity decrement (cost < m_high/8) | P | m_high; coefficient bounds delta >= 1/50, D_x >= 37/18, J >= 35/54 | 16227-16236 |
| 4 | eta_mesh (Lemma 18.1 mesh) | P | moment losses, bounded ranges (not K, not the target: **I1, I12**) | 16238-16243; 12570-12572 |
| 5 | b_round (rounding cost < m_high/8) | P | m_high | 16243-16245 |
| 6 | K even, 2ell/K < min{eta_mesh, b_round, 1/185}; ell_i = ell/K; W_i on gapped I_i | P | eta_mesh, b_round, geometry | 16246-16261 |
| 7 | m_P = kappa_P = 7/(96K) | P | K | 16303-16307 |
| 8 | amplitude width vartheta; remaining powers eps (detector loss, eps1, eps_pr) | P | m_high, K (via the O(.) constant and min ell_i), m_w, m_z, m_P | 16312-16324 |
| 9 | e: total cost < m_high/8; (1+h)e + eps_pr < m_w/4; e + eps_pr < m_z/4, m_P/4; e < 10^-3; e < e_0(eps) (Lemma 8.2) | P | items 1-8 | 16312-16324; 4398-4404; 15064-15070 |
| 10 | zeta < min{1/48, m_high/16} | P | m_high | 16326-16331 |
| 11 | z_inf (large-row saving > m_high) | P | zeta, m_high | 16331-16335; 15905-15916 |
| 12 | P0 cutoff ((10.2); Prop 16.1 \|H_p - 1\| < 1/2) | P | e (Prop 16.1), region-two majorant | 16336-16341; 8858, 8911 |
| 13 | m = (1/4) min{m_high, m_w, m_z, m_P}; omega = Delta/2; sigma = m/2; eps_ht | P | items 1, 2, 7; Delta; eps | 16365-16372, 16451 |
| 14 | target eta (Prop 2.1) | T | omega, sigma (eps* = sigma = m/2) | 498-500 |
| 15 | arithmetic data, final S (including P0 and extra exclusions) | T | eta, P0, T | 16374-16377 |
| 16 | internal moment, seminorm and Sobolev orders; A_eta, B_eta, A_ht | T | data, K, eps | 16379-16394 |
| 17 | tau0 = d_min eps_ht / (20(1 + A_ht)); tau_eta <= min{d_min/100, tau0, m/(4(A_eta + 1))} | T | eps_ht, A, m | 16395-16407; 6561-6566 |
| 18 | auxiliary external orders (dyadic, witness, prime); N_eta with B_eta - N tau < C(beta*) - m/2 | T | tau_eta, B_eta | 16418-16431; 4415, 4642; 6571-6573 |
| 19 | Z_0(eta, tau, N) | T | all | 6575-6576; 16443 |

Per-row data that are not choices: the bin (i, a), the witness (rho, t, D, N, nu) and the amplitude vector g. They depend on e, T1 = Z^tau and Z. Their number is O_e(1), O(log^2 U) and ((delta/(2vartheta)) + 2)^K respectively, and none depends on tau except through (1+T1)^{fixed} factors.

**Result.** The order is admissible, and no constant is chosen after something that depends on it. omega = Delta/2 and sigma = m/2 depend only on Delta, the fixed geometry and K. K in turn depends on eta_mesh and b_round, which depend on m_high and Delta. The exact numerics the order relies on all re-run (script G):
- the supply margins 8/39 - 7/37 = 23/1443 and 1/5 - 7/37 = 2/185;
- h + zeta < 5 ell iff zeta < 1/48;
- K >= 62;
- kappa_P = 7/(96K) < 7/(48K);
- m_high = 51Delta/64 < 63/800 for Delta <= 1/24;
- the budget 5 x (1/8) leaving 3/8 > 1/4;
- tau0 giving tau A_ht <= d_min eps_ht/20;
- the crude detector error U^{-187/100};
- the coefficient bounds D_x >= 37/18, P_x >= 7/9, J >= 35/54, R_* + Delta/4 <= 139/96;
- the intermediate rows -529/2400 + 25delta/96 <= -49/14400.

### 6.3 Which stated independence claims are load-bearing

Each claim is an edge the paper asserts is absent. The script adds each edge in turn and classifies the result.

| Claim | Where stated | If false |
|---|---|---|
| I1 Lemma 18.1 mesh independent of the slot count | 12570-12572, 16241-16243 | **cycle** K -> eta_mesh -> K |
| I2 moment-loss cost coefficients in E independent of K | 16228-16233 | **cycle** |
| I3 A_eta independent of tau and N | 16384-16389, 16428-16431 | **cycle** tau -> A -> tau |
| I4 B_eta independent of N | 16385-16389; 6538 | **cycle** |
| I7 m_w, m_z independent of e | 15673-15676 (geometry only: verified) | cycle |
| I8 m_small independent of e | 15889 (error-free saving: verified) | cycle |
| I10 moment losses independent of the target | Lemma 18.1 uniformity over moving moduli (12574-12578) | **cycle through the target** (K -> m_P -> m -> sigma) |
| I12 Lemma 18.1 mesh independent of the arithmetic datum | 12570-12577 | **cycle through the target** |
| I5 P0 independent of the target | uniform majorant (CONTOUR review) | harmless: P0 may become target data |
| I6 K's capacity gap uniform in zeta < 1/48 | 16269-16275 (verified: gap >= 2/185) | harmless: choose zeta first |
| I9 eps_ht independent of the target | 16371 | harmless |
| I11 the O(e + vartheta + eps) constant of Lemma 20.1 independent of the target | 15751-15753 | harmless: only the margins must be pretarget, and e could be chosen per target |

I7 and I8 are verified here outright. I3 and I4 are verified at the level of Lemma 8.2's and Prop 8.3's own order statements (4415-4416, 4642-4643) and Lemma 11.1. I1, I2, I10 and I12 are taken from statements whose proofs are outside this scope. They are the smallest remaining gap for this item.

The paper is stronger than necessary in one respect. Lemma 11.1 assumes all real parameters are pretarget, but its proof uses only that m and omega are common. So e, the power losses, eps_ht and P0 could be per-target without harm (I5, I9, I11).

### 6.4 w5copg item 8

- (i) *Uniformity of margins "independent of the target".* This is confirmed at the level of the order (Secs. 6.2-6.3). The pretarget margins are Delta, m_high = 51Delta/64, m_w, m_z and m_P = 7/(96K). Their target-independence reduces to I1, I2, I10 and I12.
- (ii) *Rows whose inducing character lies in Theta.* Only the detector half was checked: 4259-4268 is correct (Sec. 1). The Sec. 18 treatment (14312-14779) is not reviewed here.
- (iii) *The boundary delta = 5/6.* The bin ceiling includes it (6824-6830), and the K constraint uses delta <= 5/6 < 1, endpoint included (16269). The no-slot endpoint estimate itself was not re-derived.

## 7. Minor and cosmetic findings

- **Notation collisions.**
  - tau is both the height exponent (4274) and a probe datum in "T, S, b*, xi, tau, Xi, W0, W1" (6847).
  - eta is the target, the Lemma 18.1 mesh (12547) and eta_mesh.
  - sigma is the high saving, Re rho, and sigma_width (16281).
  - q is the amplitude mean, distinct from the conductor exponent (the paper flags this at 15092).
- **Incomplete pretarget list.** The statement of Prop 20.3 does not name z_inf, P0, b_round or eta_mesh among its pretarget choices, although its proof fixes all of them pretarget.
- **Weaker displayed bound.** Prop 8.3 displays the crude U^2 where U^{3/5+eps} holds. The text says this is deliberate.

## 8. Not checked

- The proofs of Lemma 4.5 (smooth calculus) and of the reciprocity input Q_psi << q_u.
- Lemma 18.1, Lemmas 17.x and Prop 19.2: the mesh, the loss coefficients, the counts and the hypothesis matching.
- Lemma 10.6, Lemma 16.2, Def 10.1 on a lowered D1, and Part I.
- The endpoint certificate (Lemma 20.2; see PR910_REPLAY), and the low side.
- No Lean build.

## 9. Reproduction

```text
cd research/exploratory/qrh-2026-10/reviews
python3 -I sep30_detector_checks.py      # 114 PASS, 0 FAIL, exit 0, about 1 s
python3 -I -O sep30_detector_checks.py   # byte-identical output
```

The exit status equals the number of FAIL lines. Sec. H prints one INFO line per independence claim, giving its classification.
