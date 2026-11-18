# C4-weil-window-locality: FINAL (adjudicated)

This is the adjudicator's report. `REPORT.md` (investigator) and `SKEPTIC_REVIEW.md` (skeptic) are kept unchanged as the record. Where this file disagrees with either of them, this file gives the final status and the reason. RH is open. Nothing here claims to prove or disprove it. Every "detection" or "blindness" statement below is either (i) an implication about a HYPOTHETICAL off-line zero (vacuous if RH holds) or (ii) a statement about an explicitly defined synthetic model. Model statements stay model statements.

```text
Status:
  ADJUDICATED EXPLORATORY DOSSIER. No claim about RH or its negation.
  - THEOREM (complete proof in REPORT.md or here):
      C4-C   exact detection criterion (standard Schur/Sylvester lemma; not new);
      C4-LAT lattice/flat two-regime law (model); its mirror-pair aside is REFUTED and repaired here;
      C4-B   growth detection under the single-defect hypothesis H1 (asymptotic display corrected: 0.704 L, not 1.407 L);
      C4-ADJ-PAIR  exact pair identity W = P + 2m|<g,u>|^2 - 2m delta^2 |<g,w>|^2 and single-pair criterion;
      C4-ADJ-BLIND height-uniform small-delta blindness from coercivity of the real-zero form;
      C4-ADJ-C     the brief's task 2(a) holds under H1 with an explicit C(delta) (Arb-certified on finite T-ranges,
                   tail T > 10^tmax by a sketched asymptotic argument);
      C4-ADJ-INV   window positivity => exclusion region for single defects under H1 (contrapositive of C4-B).
  - CONDITIONAL: C4-BL (blindness under hypothesis R and (S)); R restricted to V is equivalent to G <= (1+eta) G_flat,
    so all content is in R.
  - NUMERICAL-RIGOROUS (python-flint/Arb, modulo FLINT correctness):
      C4-B2 table points and the delta* correction (adj_thmB_arb.py);
      C(delta) upper bounds (adj_Cdelta.py);
      8 explicit test functions on which the injection-model form is certified negative (C4-ADJ-WIT), including
      near-line defects (kappa < kappa_c) detected BELOW the Nyquist window in BOTH injection models.
  - NUMERICAL-NONRIGOROUS: C4-P window profile (Rayleigh-Ritz upper bounds, 0.3-6% above the infimum);
    C4-D1..D4 threshold scans (upper bounds on model thresholds).
  - IMPORTED: C4-0 (a)-(c); C4-1 (with corrections); Zhu Table 1; Danesh 2026; Connes-Consani 2021 prolate count.
  - HEURISTIC: C4-H two-regime description (additive model only); C4-REL (rewritten).
  - CONJECTURE: a narrowed form of the C4-H conjecture (Sec. 2a).
  - REFUTED: the brief's Nyquist heuristic, for every fixed delta > 0 (C4-R main part); C4-R's "corrected statement"
    as a universal near-line locality law; the C4-LAT mirror-pair aside.
  - WITHDRAWN: the C4-H "normalised" conjecture (it is a corollary of C4-B); "0 <= c(T)"; "supported by C4-D4";
    C4-REL point (2) as guidance; six-digit precision of C4-P.
  Evidence level of this adjudication:
  - L2 for C4-C, C4-B (proof chain re-derived; constants re-implemented), C4-LAT, C4-BL, C4-B2;
  - L1 for primary texts re-read here: Connes-Consani arXiv:2006.13771 (intro, Thm 1, Cor 2); Zhu arXiv:2608.24827v2
    (eq. (1), Prop. 2.3, Table 1, Cor. 6.3 statement); Danesh arXiv:2611.10726 (abstract, final remarks);
    Connes-Consani arXiv:2106.01715 (Sec. 1 prolate count, Sec. 2.5) and Connes-Consani-Moscovici arXiv:2310.18423
    (abstract, eq. (2)), both partial;
  - L0+ (abstract only): Burnol math/0203120, math/0208121; Trudgian 2014 S(t) bound (zbMATH 1284.11119 review).

Scope:
  zeta only. Brief's normalisation: g in C_c^inf(-L,L) (log variable), h_g(z) = int g(x) e^{izx} dx,
  W(g) := W(g*g~) = sum_rho h_g(gamma) conj h_g(conj gamma), rho = 1/2 + i gamma (with multiplicity), which equals
  the arithmetic side A(g) (prime powers n < e^{2L}, archimedean and pole terms) unconditionally.
  lambda_min(L) = inf W(g)/||g||^2. L_N(T) = (1/2) log(T/2pi) ("Nyquist window"), T*(L) = 2 pi e^{2L}.
  Hypothetical defect: one quadruple {1/2 +- delta +- iT}, i.e. ordinates {+-T +- i delta}, 0 < delta < 1/2.
  sigma^2(delta,L) = int_{-L}^{L} sinh^2(delta x) dx = sinh(2 delta L)/(2 delta) - L;  kappa = delta log(T/2pi);
  kappa_c = 2.1773189849653 (root of sinh k = 2k).
  Injection models (synthetic): ADDITIVE = A(g) + quadruple terms; COLLISION = additive minus the two Arb-certified
  neighbouring ordinates (both signs).

Exact sources or dependencies:
  Per claim, in Section 2. Primary texts re-read by the adjudicator (pdf sha256, first 8 hex digits):
  - Connes-Consani, arXiv:2006.13771 (b8e0b54a): displays (3)-(5), Thm 1, Cor 2;
  - Zhu, arXiv:2608.24827v2 (70332e42; unrefereed): eq. (1) (lambda* over real even f), Prop. 2.3, Table 1, Cor. 6.3;
  - Danesh, arXiv:2611.10726v1 (f0e7d3ea; unrefereed): abstract; "first violating separation ... undetermined";
  - Connes-Consani, arXiv:2106.01715 (784000e3): Sec. 1 (1 + nu(lambda^2) ~ 2 lambda^2 near-radical prolate vectors), Sec. 2.5;
  - Connes-Consani-Moscovici, arXiv:2310.18423v2 (8bc19764): abstract, eq. (2) W_lambda = -S^2 + 2 pi lambda^2 (4N+1) - ...
  Zeros: EXP-0001 (first 100000 Arb-certified ordinates; durable copy experiments/results/zeros/zeta_zeros_1_100000_arb.tsv.gz).
  Load-bearing imported inputs: Trudgian 2014 |S(t)| <= 0.112 log t + 0.278 log log t + 2.510 (t >= e) [L0+];
  Stirling remainder for theta' (DLMF 5.11); Platt-Trudgian 2021 RH height 3.0001753328e12 [via C1 FINAL, L1].

What was actually run:
  - Investigator: 13 scripts; skeptic: 8 scripts (see their files). All 16 investigator output hashes listed in
    REPORT.md (identical in manifest_C4.json) and all 17 skeptic output hashes (SKEPTIC_REVIEW.md manifest) were
    re-verified by the adjudicator on 2026-11-17: all match.
  - Adjudicator, 4 new scripts in experiments/code/C4-weil-window-locality/adjudicator/:
    (i)   adj_numbers.py (mpmath 50 digits; Arb for kappa_c; 5.6 s): coincidence window; kappa_c; C4-B inequality
          re-implemented (L_B table, delta* at T_PT, asymptotic coefficient, inverse map); lattice mirror-pair check.
    (ii)  adj_thmB_arb.py (Arb 256 bits; 0.9 s): ball certificates of the C4-B inequality at the C4-B2 points, the
          delta* signs, and the inverse-map ranges (adaptive interval cover in log T).
    (iii) adj_Cdelta.py (mpmath search + Arb interval cover; 119 s): C(delta) for T >= 100 and for T >= T_PT.
    (iv)  adj_witness.py (Arb 256-3000 bits, acb.integral; 8 cases, 0.7-36 s each): exact-rational test functions,
          injection-model form evaluated from the definition (pole term in closed form, exact prime-power sum,
          rigorous archimedean integral, exact h_g); compared with the investigator's float64 eigenvalues.
  - Literature re-checks listed under "Evidence level" above; one arXiv API query (au:Burnol AND Sonine).

Smallest remaining gap:
  (a) BLINDNESS: apart from the lattice model and the astronomically small height-uniform radius of C4-ADJ-BLIND,
      no lower bound on the detection window L*(T,delta) is proved, even in the injection models. The exact
      quantity to control is the local resolvent D(T,delta,L) = lambda_max(E_w^* (P + 2m E_u E_u^*)^{-1} E_w)
      (C4-ADJ-PAIR); hypothesis R of C4-BL is one sufficient bound for it. Counter-witnesses (C4-ADJ-WIT) show that
      no height-only law of the form "L* >= L_N(T) - c" holds across injection models.
  (b) DETECTION: under H1 the window L_N(T) + C(delta) suffices with C(delta) ~ (2.1 to 3.1)/delta (C4-ADJ-C);
      the injection numerics suggest L* - L_N <= 0.63 at T <= 7e4 (upper bounds). An O(1) or O(log(1/delta))
      theorem is open, and H1 (a single defect) has not been removed.
  (c) The statement whose failure would invalidate C4-B, and with it C4-B2, C4-ADJ-C, C4-ADJ-INV and the rigorous
      (conditional) refutation of the brief's heuristic, is Trudgian's S(t) bound (IMPORTED, read at L0+ only),
      together with the theta' Stirling bound used in step 4 of the C4-B proof.
```

---

## 1. How the disagreements were resolved

| # | Point | Resolution | Basis |
|---|---|---|---|
| 1 | C4-0(d): value of the coincidence window | **Skeptic upheld.** L_c = (1/2) log(gamma_1/2pi) = 0.405378739661, not 0.405408 (where 2 pi e^{2L} = 14.13555). Immaterial for the conclusion "no feature at L_c". | adj_numbers (a). |
| 2 | C4-1: Zhu's lambda* and missed overlap | **Skeptic upheld.** Zhu eq. (1) defines lambda*(L) as an infimum over real even f; the brief's lambda_min is over all g (equal at L = 0.8 by Zhu Thm 6.2 / Cor 6.3). Zhu Table 1 (converged Legendre sector floors, both parities, L = 0.5..1.2) directly overlaps C4-P. Danesh arXiv:2611.10726 (7 Nov 2026) is contemporaneous related work (two narrow, separated supports; e^{(delta-eps) x} growth of a cross term; it states that the first violating separation is left undetermined, so it gives no (T, delta) window law). | Zhu text lines 86-87, 878-918; Danesh abstract and lines 427-428. |
| 3 | C4-P: precision of the profile | **Skeptic upheld.** Zhu Table 1 reference values lie below every investigator value with L >= 0.5: 9.34e-7 vs 9.37661e-7 (L=0.5), 1.61e-9 vs 1.62065e-9, 4.18e-13 vs 4.23548e-13, 1.65e-17 vs 1.70156e-17, 4.14e-23 vs 4.29796e-23, 5.88e-30 vs 6.25697e-30, 2.04e-38 vs 2.05682e-38. The skeptic's larger bases reproduce the Zhu values. The investigator's numbers are Rayleigh-Ritz upper bounds 0.3-6% above the infimum; quote at most 2 significant digits. | Zhu Table 1 (L1); sk_profile_conv.jsonl. |
| 4 | C4-LAT: "if the mirror pair is present, take a higher sinc power" | **Skeptic upheld; aside REFUTED.** With p sinc factors the mirror term behaves like T0^2 (p/(2(L - pi/s) T0))^{2p}. Lattice s=1, delta=0.3: at L - pi = 0.05, T0 = 10.5 the (positive) mirror term is 1757, 1840, 1883, 1904 for p = 4, 8, 16, 32 against a main term -0.393; at T0 = 100.5 it is 1.6, 2051, 2.1e4, 6.1e4. The repair h -> ((r+T0)^2 + delta^2) h (sinc^6) kills the mirror term exactly and keeps the main term negative: the factor contributes q(T0 - i delta)^2 = 16 T0^2 (T0 - i delta)^2, whose real part is positive for T0 > delta. The theorem as stated (one pair) is unaffected. | adj_numbers (d); algebra here. |
| 5 | C4-B: asymptotic display | **Skeptic upheld.** e^{2 delta L}/(4 delta) ~ (0.5 + 0.704 L) log T, since 2 pi x 0.112 = 0.7037. The ratio of e^{2 delta L_B}/(4 delta) to (0.5 + 0.7037 L_B) log T is 1.151, 1.018, 1.002, 1.0002 at log10 T = 1e2, 1e3, 1e4, 1e5 (delta = 0.49). With 1.407 the ratio tends to 0.5. | adj_numbers (c3). |
| 6 | C4-B2: "delta >~ 0.22" at T_PT | **Skeptic upheld.** delta* = 0.2354455 (mpmath). Arb: margin(L_N(T_PT) - 1e-6, T_PT, delta) > 0 for delta = 0.2355, 0.24, 0.3, 0.4, 0.49, and margin(L_N(T_PT), T_PT, delta) < 0 for delta = 0.2354 and 0.22. | adj_numbers (c2); adj_thmB_arb. |
| 7 | C4-R: the "corrected statement" (Nyquist locality for kappa < kappa_c) | **Skeptic upheld and strengthened.** The refutation of the brief's heuristic stands (C4-B under H1; C4-LAT exactly; injection numerics). The "corrected statement" fails as a universal law: Arb-certified negative values of the model form at L < L_N with kappa < kappa_c exist in the collision model (kappa = 0.22 at L_N - 0.016; kappa = 0.74 at L_N - 0.386; kappa = 1.47 at L_N - 0.486) and in the additive model (kappa = 1.86 at L_N - 0.159). See C4-ADJ-WIT. It survives only as a HEURISTIC description of additive-model upper bounds. | adj_witness (8 cases). |
| 8 | C4-BL: content of hypothesis R | **Skeptic upheld.** R(T,L,eta) on V = span{e_z} is literally G <= (1+eta) G_flat, so the theorem is a reformulation; (S) must be listed. The adjudicator adds what blindness CAN be proved without R: the exact single-pair criterion and a height-uniform small-delta blindness (C4-ADJ-PAIR, C4-ADJ-BLIND). | Proofs in Sec. 3.2-3.3. |
| 9 | C4-D3: "sinh test function nearly optimal (gap 0.001-0.06)" | **Skeptic upheld.** True only for delta >= 0.3 at T >= 1e12. At delta = 0.2 and T = 1e6, 1e8, 1e10 the gap L_sinh - L* is 0.14, 0.42, 0.11. | sk_sinh_highT.json. |
| 10 | C4-H: conjecture and "supported by C4-D4" | **Skeptic upheld.** (i) Collision data contradict "supported by C4-D4". (ii) The normalised conjecture abs(L* - min(L_N, L_flat))/L_N -> 0 is a corollary of C4-B: in the additive model (and under H1) L* <= L_B = O_delta(log log T) and L_flat = O_delta(log log T), so abs(L* - L_flat) = o(L_N). (C4-B's proof uses only P <= int F dN over true zeros, so it applies verbatim to the additive model, conditional on RH for the true zeros, which is the model's premise.) (iii) "0 <= c(T)" is a blindness claim that Rayleigh-Ritz numerics cannot support, and the additive exception at kappa = 1.86 is Arb-certified. | Logic; adj_witness. |
| 11 | C4-REL point (2): "only windows L >~ L_N + O(0.2) see near-line defects" | **Skeptic upheld.** Rests on unproven blindness and is contradicted by certified collision-model witnesses. Rewritten in Sec. 3.6. | Sec. 3.6. |
| 12 | Reliability of float64 thresholds (not disputed; checked) | **Confirmed.** In 8 cases the Arb value of the model form at the investigator's float64 ground state agrees with the investigator's float64 eigenvalue to <= 3.4e-10 absolute, including lambda = -1.3067e-6 (T0 = 1000.57, delta = 0.01, L = 3). This is an independent validation of the investigator's arithmetic-side assembly (archimedean moments, prime moments, pole and quadruple terms) at the eigenvector level. Thresholds remain upper bounds. | adj_witness. |

No investigator theorem is refuted. The REFUTED items are the brief's heuristic, the "corrected" universal near-line locality law in C4-R, and the C4-LAT aside on the mirror pair.

---

## 2. Adjudicated claims table

| ID | Short statement | Investigator label | Skeptic verdict | FINAL status |
|---|---|---|---|---|
| C4-0 | CC window [2^{-1/2}, 2^{1/2}] is for g: L = (log 2)/2 = 0.346574, f = g*g~ on abs(y) <= log 2; Yoshida same window; Bombieri Thm 12; Zhu L = 0.8; coincidence 2 pi e^{2L} = gamma_1 at L_c is not a threshold | IMPORTED + NUM | upheld w/ corr. | **IMPORTED** (a)-(c) (CC at L1, re-read here; Bombieri L1 via investigator/skeptic; Yoshida L0+; Zhu unrefereed); (d) **L_c = 0.4053787397** (corrected), "no feature" **NUMERICAL-NONRIGOROUS** |
| C4-1 | Prior art on profile, resolution height, eigenvalue counts; no (T, delta) window law found | IMPORTED | upheld w/ corr. | **IMPORTED** (Zhu lambda* is over real even f; Zhu Table 1 overlaps C4-P; Danesh 2026 added; no window law found by any of the three agents) |
| C4-P | lambda_min(L) profile L = 0.1..1.2 (e.g. 1.7e-17 at 0.8, 8e-49 at 1.2) | NUM-NONRIG | upheld w/ corr. | **NUMERICAL-NONRIGOROUS**: Rayleigh-Ritz upper bounds, 0.3-6% above the infimum for L >= 0.5; 2 significant digits; reference values: Zhu Table 1 (**IMPORTED**, not certificates) |
| C4-C | Negative index of W on window L = negative index of G^{-1} + M; <= number of conjugate pairs; monotone; complex inf = real inf | THEOREM | upheld | **THEOREM** (standard; not new). (iv) holds without (S) |
| C4-LAT | Lattice/flat: inf W_lat < 0 iff L > pi/s or sinh(2 delta L)/(2 delta) - L > Psi0/2; kappa_c = 2.17732 | THEOREM | upheld w/ corr. | **THEOREM** (model). Mirror-pair aside **REFUTED**; repaired construction is a THEOREM (Sec. 1 row 4) |
| C4-B | Under H1: 2 sigma^4 > sigma^2[log(T/2pi) + 4 pi L S*(2T)] + eps => lambda_min(L) < 0; L_B = (1/(2 delta))[log log T + log log log T + O_delta(1)] | THEOREM | upheld w/ corr. | **THEOREM** (implication under H1; vacuous if RH holds). Asymptotic display corrected to (0.5 + 0.704 L) log T. "Possibly new" (search-limited; Danesh 2026 uses the same e^{delta x} mechanism without a window law) |
| C4-B2 | L_B table and crossovers; at T_PT, L_B < L_N for delta >~ 0.22 | THEOREM | upheld w/ corr. | **NUMERICAL-RIGOROUS** (Arb certificates at the table points; the investigator's 50-digit mpmath evaluation is non-rigorous). **delta* = 0.2354** at T_PT, not 0.22 |
| C4-R | Brief's heuristic false for every fixed delta; "corrected statement": Nyquist locality for kappa <~ kappa_c | REFUTED (+ corrected statement) | upheld w/ corr. | Brief's heuristic **REFUTED** (rigorously under H1 via C4-B / C4-ADJ-C; exactly in the lattice model; NUMERICAL-RIGOROUS and NUMERICAL-NONRIGOROUS in the injection models). "Corrected statement" **REFUTED as a universal law** (C4-ADJ-WIT); survives as **HEURISTIC** for additive-model upper bounds |
| C4-BL | Blind if (1+eta)^{-1} G_flat^{-1} + M >= 0, under R(T,L,eta) | THEOREM + HEURISTIC | upheld w/ corr. | **CONDITIONAL** (on R and (S); proof complete; R on V is equivalent to G <= (1+eta) G_flat). Heuristic part (eta ~ 0.1-0.7 at 1e6-1e10; eta -> 0) **HEURISTIC**, unverified; "eta -> 0" can hold only for typical T |
| C4-D1 | Additive-model thresholds T0 = 27.7..7e4, 8 deltas | NUM-NONRIG | upheld | **NUMERICAL-NONRIGOROUS** (upper bounds; 7 reproduced by the skeptic on the zeros side; sampled detections Arb-certified in C4-ADJ-WIT) |
| C4-D2 | N-refinement lowers Nyquist-regime thresholds; offset <= 0.18 (T0 = 100), <= 0.16 (1000), still decreasing; weak log(1/delta) slope | NUM-NONRIG | upheld | **NUMERICAL-NONRIGOROUS** |
| C4-D3 | Large heights 1e6..1e50: L* near L_flat while L_N grows | NUM-NONRIG | upheld w/ corr. | **NUMERICAL-NONRIGOROUS** (sinh near-optimality only for delta >= 0.3, T >= 1e12) |
| C4-D4 | Collision model lowers thresholds; locality must involve the local configuration | NUM-NONRIG | upheld | **NUMERICAL-NONRIGOROUS**, key below-Nyquist detections **NUMERICAL-RIGOROUS** (C4-ADJ-WIT) |
| C4-H | L* ~ min{L_N + c + b ln(1/delta), L_loc}; conjecture 0 <= c <= 0.1, normalised limit | HEURISTIC + CONJ | downgraded | **HEURISTIC** (additive model only). Conjecture **narrowed** (Sec. 2a). Normalised form **WITHDRAWN** (corollary of C4-B); "0 <= c(T)" and "supported by C4-D4" **WITHDRAWN** |
| C4-REL | Relevance to the host's operator route | HEURISTIC | downgraded | **HEURISTIC**, rewritten (Sec. 3.6). Point (1) and (3) stand; point (2) **WITHDRAWN** as guidance |
| C4-ADJ-PAIR | Pair identity; exact single-pair and quadruple criteria | (new) | (new) | **THEOREM** (elementary; equivalent to C4-C for these configurations) |
| C4-ADJ-BLIND | If P >= a norm(g)^2 on window L, then W >= (a - 2m[sigma^2 + 2 sinh^2(delta L)/T]) norm(g)^2 | (new) | (new) | **THEOREM** |
| C4-ADJ-C | Under H1: lambda_min(L) < 0 for all L >= L_N(T) + C(delta); C(delta) <= 4.40 (0.49) ... 313.17 (0.01); for T >= T_PT: -6.94 ... 313.17 | (new) | (new) | **THEOREM** (finiteness; certified constants on T in [Tmin, 10^tmax]) + **PROPOSITION-PROOF-SKETCH** (explicit tail T > 10^tmax) |
| C4-ADJ-INV | W >= 0 on window L => (under H1) no defect with margin(L,T,delta) > 0; first informative window beyond T_PT at delta = 0.49 is L = 6.49 | (new) | (new) | **THEOREM** (contrapositive) + **NUMERICAL-RIGOROUS** ranges |
| C4-ADJ-WIT | 8 explicit g with Arb-certified W_mod(g) < 0 (additive and collision models) | (new) | (new) | **NUMERICAL-RIGOROUS** (model statements) |
| C4-ADJ-LIT | CC 2021 prolate count ~ 2 lambda^2; CCM eq. (2); Burnol Sonine spaces | (new) | (new) | **IMPORTED** (L1 partial / L0+); no window-height law found |

### 2a. Notes on individual claims (only where the final wording differs from REPORT.md)

- **C4-0.** Final wording of (a): "Connes-Consani (arXiv:2006.13771, display (3) and Thm 1) consider g in C_c^inf(R*_+) supported in [2^{-1/2}, 2^{1/2}], with ghat(i/2) = 0 (and ghat(0) = 0 in Thm 1). Then f = g*g^* is supported in (1/2, 2). In the brief's log variable this is L = (1/2) log 2 = 0.3465736 for g and |y| <= log 2 for f, the largest window whose f sees no prime power. It is the window of Yoshida 1992 (t = (log 2)/2, as stated by Bombieri 2000, Sec. 1). There 2 pi e^{2L} = 4 pi = 12.566 < gamma_1." (b) Bombieri Thm 12 has an unspecified O(1), so it does not by itself certify the whole log 2 window. (c) Zhu Cor. 6.3 (unrefereed): W >= 8.9e-18 ||g||^2 on L = 0.8, all g, certified on the geometric side (no zero data).
- **C4-P.** Values to keep (upper bounds): 0.457 (L=0.1), 0.095 (0.2), 7.6e-3 (0.3), 1.3e-3 ((log 2)/2), 1.8e-4 (0.4), 1.4e-4 (L_c), 9.4e-7 (0.5), 1.6e-9 (0.6), 4.2e-13 (0.7), 1.7e-17 (0.8), 4.3e-23 (0.9), 6.3e-30 (1.0), 2.1e-38 (1.1), 8e-49 (1.2). For L >= 0.5 use Zhu Table 1 (9.34e-7, 1.61e-9, 4.18e-13, 1.65e-17, 4.14e-23, 5.88e-30, 2.04e-38, 7.94e-49; last row converged only to a factor ~2 per Zhu) as reference values, not certificates.
- **C4-B.** Proof chain re-derived by the adjudicator at the level of: quadruple term -2m sigma^4 (what(-i delta) = sigma^2, what(i delta) = -sigma^2); P <= int F dN (off-line ordinates add 2m F(T) >= 0); Backlund integration by parts; int |F'| <= 2 ||what|| ||what'|| <= 4 pi L sigma^2; mirror pair <= Ac^2/(2T^2). The skeptic checked every numerical ingredient (36 true-zero tests). Final asymptotic: L_B(T,delta) = (1/(2 delta)) [log log T + log log log T + O_delta(1)], from e^{2 delta L}/(4 delta) ~ (0.5 + 0.704 L) log T.
- **C4-B2.** Arb-certified (margin > 0 at the L shown, so L*(T,delta) <= L under H1): T_PT = 3000175332800: L = 6.490 (delta=0.49), 7.938 (0.4), 10.565 (0.3), 15.819 (0.2), 31.581 (0.1); T = 1e100: 8.262, 10.102, 13.443, 20.123, 40.162, 80.239 (0.05); T = 1e1000: 10.734 (0.49), 52.318 (0.1). L_N(T_PT) = 13.4459073904. The crossovers log10 T = 6.09 (0.49) ... 413 (0.01) were reproduced by three implementations (mpmath only).
- **C4-R.** Final wording: "For every fixed delta in (0, 1/2), the heuristic 'a window L detects an off-line quadruple at height T only if T <~ 2 pi e^{2L} (up to O(log 1/delta) in L)' is false for single quadruples: under H1, detection holds for all L >= L_B(T,delta) = O_delta(log log T) = o(L_N(T)) (C4-B), so L_B(T,delta) - L_N(T) -> -inf, and uniformly for all L >= L_N(T) + C(delta) with an explicit finite C(delta) (C4-ADJ-C). In the lattice model the exact law is L* = min(L_N^+, L_flat). Near the line, neither a lower nor an O(1) upper detection law is proved; both injection models place the finite-basis thresholds for kappa <= 0.25 within [-0.04, +0.63] of L_N at T0 <= 7e4, and the collision model moves them below L_N by up to 0.85 for kappa in [0.5, 1.5]."
- **C4-BL.** Add (S) to the hypotheses. Note that <P^{-1}v, v> <= ||v||^2/a always, so R is informative only when (1+eta)/Psi0 < 1/a(L), i.e. always in practice.
- **C4-H, narrowed CONJECTURE (adjudicator's wording).** In the additive model with the true zeros, for fixed delta in (0, 1/2): (i) L*(T,delta) - L_flat(T,delta) = O_delta(1) as T -> inf outside a set of heights of logarithmic density zero; uniformity in T is expected to FAIL at heights where the prime phases T log p align (local symbol far below log(T/2pi)); (ii) for kappa <= 0.25 the N -> inf offset L* - L_N lies in [0, 0.2] at T0 <= 7e4. Evidence: C4-D2, C4-D3 (5 heights up to 1e50, |L* - L_flat| <= 0.3), all non-rigorous upper bounds. The rigorous upper side is L* - L_flat <= (1/(2 delta)) log log log T + O_delta(1) (C4-B); the lower side needs a bound on D(T,delta,L) (Sec. 3.2).

### 2b. Adjudicator additions

- **C4-ADJ-PAIR (THEOREM).** Sec. 3.2.
- **C4-ADJ-BLIND (THEOREM).** Sec. 3.3.
- **C4-ADJ-C (THEOREM + PPS tail).** Sec. 3.3.
- **C4-ADJ-INV (THEOREM + NUMERICAL-RIGOROUS).** Sec. 3.3.
- **C4-ADJ-WIT (NUMERICAL-RIGOROUS).** Sec. 3.5.
- **C4-ADJ-LIT (IMPORTED).**
  - Connes-Consani arXiv:2106.01715, Sec. 1: for the multiplicative window [lambda^{-1}, lambda] (brief's L = log lambda), the near-radical of the Weil form is spanned by "prolate vectors" built from the 1 + nu(lambda^2) ~ 2 lambda^2 prolate spheroidal functions PS_{2m,0}(2 pi lambda^2, .); Sec. 2.5 reports (numerically) that log s(L) of the smallest even eigenvalue is roughly linear in mu = exp(circle length) = lambda^2 = e^{2L}. This is the same Slepian/Nyquist count that underlies Zhu's resolution height and ACL Sec. 8.7; it concerns the near-null space, not which off-line zeros a window detects.
  - Connes-Consani-Moscovici arXiv:2310.18423, eq. (2): W_lambda = -S^2 + 2 pi lambda^2 (4N + 1) - ..., the prolate operator whose positive spectrum relates to low-lying zeros and whose negative spectrum is the Sonin space (ultraviolet). The scale 2 pi lambda^2 is the same time-frequency scale. No window-height detection statement.
  - Burnol math/0203120 (abstract, L0+): determines in which extended Sonine spaces the zeros form complete or minimal systems. Global (completeness) statements, not height-local; no detection window.
  - Net: no statement mapping a window L to the (T, delta) it detects was found by any of the three agents in 2026-11 searches; C4-B, C4-ADJ-C and C4-ADJ-BLIND are "possibly new" only in this search-limited sense.

---

## 3. The most useful precise statements

Notation as in the header. For z in C let e_z(x) = e^{-i conj(z) x} 1_{[-L,L]}(x), so h_g(z) = <g, e_z> (L^2 inner product, linear in g). Let Gamma_R be the real ordinates (with multiplicities m_gamma) and P(g) = sum_{gamma in Gamma_R} m_gamma |h_g(gamma)|^2. (S) means P(g) >= a ||g||^2 on C_c^inf(-L,L) for some a > 0.

### 3.1 Windows of known positivity and the coincidence (IMPORTED; answers the brief's Connes-Consani question)

| Window (brief's L, support of g) | Support of g*g~ | Statement | Source |
|---|---|---|---|
| L = (1/2) log 2 = 0.34657 | [-log 2, log 2] | W >= 0 under ghat(i/2) = 0 (CC Thm 1 also ghat(0) = 0); no prime power enters | Yoshida 1992 (via Bombieri Sec. 1; zbMATH 0817.11041, L0+); Connes-Consani 2006.13771 Thm 1 (L1) |
| \|I\| < log 2 | | W >= (log(1/\|I\|) - log log(1/\|I\|) - O(1)) \|\|g\|\|^2 | Bombieri 2000, Thm 12 (unspecified O(1)) |
| L = 0.8 | [-1.6, 1.6] | W >= 8.9e-18 \|\|g\|\|^2, all g, geometric side only | Zhu 2608.24827 Cor. 6.3 (unrefereed) |

The coincidence 2 pi e^{2L} = gamma_1 holds at L_c = 0.4053787397, strictly inside the certified range and above the CC/Yoshida window; ACL 2611.13129 Sec. 8.7 already records it ("no undersampling" regime). The profile shows no feature there (C4-P; skeptic at fixed N).

### 3.2 Exact criteria (THEOREMS)

**C4-C (standard).** If the non-real ordinates form a finite set Q (closed under conjugation and negation, multiplicities m_z) and (S) holds, then the negative index of W on window L equals the number of negative eigenvalues of G^{-1} + M, where G = (<P^{-1} e_w, e_z>) and M_{zw} = m_z [w = conj z]. It is at most the number of conjugate pairs, monotone in P and in L, and the infimum over complex g equals the infimum over real g.

**C4-ADJ-PAIR (pair identity).** For a conjugate pair {T' - i delta, T' + i delta} of multiplicity m, put
u_{T'}(x) = e^{-iT'x} cosh(delta x) 1_{[-L,L]} and w_{T'}(x) = e^{-iT'x} delta^{-1} sinh(delta x) 1_{[-L,L]}. Then, for every g,

  h_g(T'-i delta) conj h_g(T'+i delta) + h_g(T'+i delta) conj h_g(T'-i delta) = 2 |<g,u_{T'}>|^2 - 2 delta^2 |<g,w_{T'}>|^2.

*Proof.* e_{T'-i delta} = e^{-iT'x} e^{delta x} = u + delta w and e_{T'+i delta} = u - delta w. With a = <g,u>, b = <g,w>, the left side is 2 Re[(a + delta b) conj(a - delta b)] = 2|a|^2 - 2 delta^2 |b|^2 + 2 delta Re(b conj a - a conj b), and the last term vanishes because b conj a - a conj b is purely imaginary. QED.

*Consequences.* For one quadruple {+-T +- i delta} of multiplicity m, with (S): W = Q - 2m delta^2 (|<.,w_T>|^2 + |<.,w_{-T}>|^2), where Q = P + 2m(|<.,u_T>|^2 + |<.,u_{-T}>|^2) is coercive. Hence

  lambda_min(L) < 0  iff  2 m delta^2 lambda_max(E_w^* Q^{-1} E_w) > 1,  E_w = [w_T, w_{-T}],

and for a single pair (the one-sided complex model of C4-LAT) iff 2 m delta^2 <Q^{-1} w, w> > 1. This is the exact form of the C4-H mechanism "2 delta^2 D(T) > 1": D(T,delta,L) := lambda_max(E_w^* Q^{-1} E_w) is a local resolvent quantity, and C4-H's D(T) is its delta -> 0 limit (w_T -> x e^{-iTx}). Check: for the flat form P = Psi0 I, <u,w> = 0 and ||w||^2 = sigma^2/delta^2, so the criterion reads sigma^2 > Psi0/2, which is C4-LAT (b). C4-B's test function e^{-iTx} sinh(delta x) is w_T up to the factor delta.

### 3.3 Two-sided rigorous bounds for a single defect

**C4-ADJ-BLIND (THEOREM; height-uniform small-delta blindness).** Suppose the only non-real ordinates are one quadruple {+-T +- i delta} of multiplicity m (T > 0, delta > 0) and P(g) >= a ||g||^2 on C_c^inf(-L,L). Then for every g in C_c^inf(-L,L)

  W(g) >= ( a - 2m [ sigma^2(delta,L) + 2 sinh^2(delta L)/T ] ) ||g||^2.

In particular the window L is blind to the defect (W >= 0) whenever 2m[sigma^2(delta,L) + 2 sinh^2(delta L)/T] <= a, at every height T.

*Proof.* By C4-ADJ-PAIR, W(g) >= P(g) - 2m delta^2 (|<g,w_T>|^2 + |<g,w_{-T}>|^2) (drop the u-terms). The bracket is at most lambda_max(Gram) ||g||^2, where the Gram matrix of {w_T, w_{-T}} has diagonal sigma^2/delta^2 and off-diagonal entry c = int_{-L}^{L} delta^{-2} sinh^2(delta x) e^{-2iTx} dx. Since s(x) = delta^{-2} sinh^2(delta x) is even and increasing in |x|, one integration by parts gives |c| <= (2 s(L) + int |s'|)/(2T) = 2 s(L)/T. So 2m delta^2 lambda_max <= 2m (sigma^2 + 2 sinh^2(delta L)/T). QED.

For small delta L, 2 sigma^2 ~ (4/3) delta^2 L^3, so the blind radius is delta_0(L) ~ sqrt(3a/(4L^3)) (m = 1, T large).
- In the ADDITIVE model, P is the true Weil form. Zhu's certified (unrefereed, unconditional, geometric-side) bound a = 8.9e-18 at L = 0.8 gives blindness at every window L <= 0.8 for every injected quadruple with delta <= 3.5e-9 and T >= 100.
- With Zhu's Table 1 reference values (not certificates) as a: delta_0 ~ 2.4e-3 (L = 0.5), 4.9e-9 (0.8), 2.1e-15 (1.0), 5.9e-25 (1.2) (NUMERICAL-NONRIGOROUS illustration).
- Consequence: any BOUNDED family of windows is blind, uniformly in height, to an explicit neighbourhood of the line (in the additive model, and under (S) in general), so controlling all off-line zeros needs an unbounded family. The radius is astronomically small because a(L) collapses doubly exponentially.

**C4-B (THEOREM under H1).** H1: rho0 = 1/2 + delta + iT is a zero (multiplicity m >= 1), 0 < delta < 1/2, T >= 100, and every other nontrivial zero outside the quadruple of rho0 has real part 1/2. If 2 sigma^4 > sigma^2 [log(T/2pi) + 4 pi L S*(2T)] + eps(L,T,delta) (S* and eps as in REPORT.md), then lambda_min(L) < 0.

**C4-ADJ-C (the brief's task 2(a) under H1).** For each delta in (0, 1/2) let L_B(T,delta) := inf{L : margin(L,T,delta) > 0} (C4-B margin) and C(delta) := sup_{T >= 100} [L_B(T,delta) - L_N(T)]. Then:

  under H1, lambda_min(L) < 0 for every L > (1/2) log(T/2pi) + C(delta),

and, with the certified constants C_cert of the table below (for which margin(L0,T,delta) > 0 was certified at some L0 <= L_N(T) + C_cert), for every L >= (1/2) log(T/2pi) + C_cert.

*Proof.* C(delta) is finite: margin(L,T,delta) -> +inf as L -> inf uniformly for T in compacts (2 sigma^4 ~ e^{4 delta L}/(8 delta^2) dominates the other terms, which are O(L e^{2 delta L})), and, for any fixed real C, margin(L_N(T) + C, T, delta) > 0 for all large T (at L = L_N + C, sigma^2 >= c_{delta,C} T^delta, the bracket is O(log^2 T) and every eps-term is O(sigma^2 T^{-1/2} log^2 T)). By definition of the infimum there are L arbitrarily close above L_B(T,delta) <= L_N(T) + C(delta) with margin > 0, hence with lambda_min(L) < 0 (C4-B), and detection propagates to all larger L because windows are nested (C4-C(iii)). QED (the explicit large-T threshold in the second step is written out only as this sketch; see below).

Values C_cert (Arb-certified upper bounds; rigorous on T in [Tmin, 10^tmax] by an interval cover in log T; in addition margin(L_N(T),T,delta) > 0 was certified on [10^{tmax/2}, 10^{tmax}]; beyond 10^tmax only the sketch above, which applies at L = L_N(T) + C_cert also when C_cert < 0). The located numerical suprema (mpmath grid plus refinement, a lower estimate of the sup) are 4.382, 5.660, 7.978, 12.614, 26.521, 54.334, 313.158 (Tmin = 100) and -6.956, -5.508, -2.881, 2.373, 18.135, 49.657, 313.158 (Tmin = T_PT):

| delta | 0.49 | 0.4 | 0.3 | 0.2 | 0.1 | 0.05 | 0.01 |
|---|---|---|---|---|---|---|---|
| C_cert(delta), Tmin = 100 | 4.40 | 5.68 | 7.99 | 12.63 | 26.54 | 54.35 | 313.17 |
| C_cert,PT(delta), Tmin = T_PT = 3.0001753328e12 | -6.94 | -5.49 | -2.87 | 2.39 | 18.15 | 49.67 | 313.17 |
| tmax (log10) | 40 | 40 | 60 | 80 | 160 | 300 | 1200 |

The maximiser is T = Tmin except for delta = 0.01 (log10 T* = 36.6). delta x C(delta) rises from 2.15 (0.49) to 3.13 (0.01). So C4-B gives the brief's "L_N + C(delta)" form, but with C(delta) of order 1/delta. The brief's hoped-for "C absolute or O(log 1/delta)" remains open. The sinh test function is useless for delta L << 1; an interpolation-type (Landau-Widom) construction is needed there.

**C4-ADJ-INV (THEOREM, contrapositive of C4-B; ranges NUMERICAL-RIGOROUS).** If W >= 0 on window L, then H1 fails at every (T, delta) with margin(L, T, delta) > 0. Arb-certified ranges, with margin > 0 on the whole interval T in [100, Tmax]:

| L | delta = 0.49 | 0.4 | 0.3 | 0.2 |
|---|---|---|---|---|
| 0.8, 1.2, 2, 2.5, 3, 4, 5 | none | none | none | none |
| 6 | Tmax = 10^4.94 | none | none | none |
| 8 | 10^76.97 | 10^13.50 | none | none |
| 10 | 10^513.1 | 10^92.06 | 10^6.68 | none |
| 12 | 10^3152 | 10^431.0 | 10^39.58 | none |

"none" means margin <= 0 already at T = 100 (mpmath grid, non-rigorous). Since RH is verified to T_PT, positivity on a window gives new single-defect information only for L > L_B(T_PT, delta): 6.49 (delta = 0.49), 7.94 (0.4), 10.56 (0.3) (L_B is increasing in T on the computed grid; mpmath). The currently certified window is 0.8 (Zhu, unrefereed). The non-rigorous injection numerics would put the needed window near 3.6 at T ~ 1e12 for delta = 0.49.

### 3.4 Lattice and flat models (THEOREM, C4-LAT)

Gamma_R = lambda0 + sZ, Psi0 = 2pi/s, one pair {T0 +- i delta} at a lattice midpoint, one-sided complex form. Then inf W_lat < 0 iff L > pi/s or sigma^2(delta,L) > Psi0/2. With kappa = delta Psi0, the growth condition beats the Nyquist window iff kappa > kappa_c = 2.1773189849653 (Arb-enclosed). The flat model P = Psi0 I has the same growth criterion. Mirror pair: use the repaired function ((r+T0)^2 + delta^2)(r - T0) sin(pi(r - lambda0)/s) sinc^6(eps(r - T0)), eps = (L - pi/s)/6.

### 3.5 Injection models: certified witnesses (C4-ADJ-WIT, NUMERICAL-RIGOROUS) and what the scans say

Each row gives an explicit g = e^{-iT0x} p(x) on [-L, L], with p an exact-rational polynomial (degree N-1). Its Rayleigh quotient W_mod(g)/||g||^2 is enclosed in Arb, with W_mod as defined in the header. T0 is the midpoint of the two Arb-certified neighbouring ordinates. A negative ball proves that the model form is negative on window L.

| case | model | T0 | delta | kappa | L | L - L_N | float64 eigenvalue (investigator matrix) | Arb W_mod(g)/\|\|g\|\|^2 |
|---|---|---|---|---|---|---|---|---|
| coll_T1e4_d0.03_L3.67 | collision | 9999.4579 | 0.03 | 0.221 | 3.67 | -0.016 | -8.47351025e-3 | -8.4735105653e-3 (+-3e-19) |
| coll_T1e4_d0.1_L3.3 | collision | 9999.4579 | 0.1 | 0.737 | 3.3 | -0.386 | -4.34494270305e-2 | -4.34494270562e-2 (+-4e-19) |
| coll_T1e4_d0.1 | collision | 9999.4579 | 0.1 | 0.737 | 3.5 | -0.186 | -0.181129617208 | -0.181129617236 (+-8e-19) |
| coll_T1e4_d0.2 | collision | 9999.4579 | 0.2 | 1.474 | 3.2 | -0.486 | -1.08582044381 | -1.08582044383 (+-4e-19) |
| add_T7e4_d0.2_L4.5 | additive | 69999.8362 | 0.2 | 1.864 | 4.5 | -0.159 | -2.80299369386e-2 | -2.80299372762e-2 (+-2e-22) |
| add_T7e4_d0.2 | additive | 69999.8362 | 0.2 | 1.864 | 4.6 | -0.059 | -0.171975022894 | -0.171975023240 (+-2e-21) |
| add_T1e4_d0.49 | additive | 9999.4579 | 0.49 | 3.612 | 2.6 | -1.086 | -0.731067389736 | -0.731067389760 (+-1e-21) |
| add_T1e3_d0.01 | additive | 1000.5705 | 0.01 | 0.051 | 3.0 | +0.465 | -1.30665277e-6 | -1.30667260e-6 (+-6e-26) |

L_N = 3.6862 (T0 = 9999.46), 4.6592 (69999.84), 2.5352 (1000.57). What these certify (model statements): near-line defects (kappa < kappa_c) ARE detected below the Nyquist window in the collision model (kappa = 0.22, 0.74, 1.47) and in the additive model (kappa = 1.86); a growth-regime defect is detected 1.09 below L_N at T0 = 1e4; and a Nyquist-regime float detection with |lambda| ~ 1e-6 is genuine. What they assume: the explicit-formula normalisation (validated against 100000 zeros by investigator and skeptic to ~1e-8) and FLINT/Arb correctness. The removed ordinates use the certified EXP-0001 enclosure [mid - rad - 5e-21, mid + rad + 5e-21] (25-digit printing of the midpoints). Not replayed: no lower bound (non-detection) is certified anywhere.

Summary of the non-rigorous scans (C4-D1..D4), all finite-basis UPPER bounds on the model threshold L*:
- Additive model, kappa < kappa_c, T0 = 27.7..7e4: L* - L_N in [+0.02, +0.63], one exception (-0.175 at kappa = 1.86). These offsets shrink under basis refinement (T0 = 100: 0.327 -> 0.170 at N = 192); the N -> inf limit is undetermined.
- Additive model, kappa > kappa_c: L* - L_flat in [-0.28, +0.11] (T0 <= 7e4); |L* - L_flat| <= 0.30 at 1e12..1e50 while L_N reaches 56.6.
- Collision model: lower than additive by 0.24-1.12 at the same (T0, delta) (the investigator's "up to 0.8" is understated; maximum 1.12 at T0 = 9999.46, delta = 0.3); for kappa <= 0.25, L* - L_N in [-0.03, +0.07]; for kappa in [0.5, 1.5], L* below L_N by 0.07-0.85.

### 3.6 "Which windows control which heights" (HEURISTIC bridge; replaces C4-REL)

For one hypothetical quadruple (T, delta) and window L (brief's normalisation; translating to the host's L requires checking the host's source definitions, which was not done):
1. Exact: visible iff 2 m delta^2 D(T,delta,L) > 1 (C4-ADJ-PAIR). Everything else is a bound on D.
2. Always invisible if 2m[sigma^2(delta,L) + 2 sinh^2(delta L)/T] <= a(L) (C4-ADJ-BLIND), at all heights. a(L) collapses doubly exponentially, so this covers only an astronomically thin neighbourhood of the line.
3. Visible under H1 if the C4-B margin is positive at L, in particular if L >= L_N(T) + C_cert(delta) (C4-B, C4-ADJ-C). For fixed L the C4-B condition holds up to log T ~ e^{2 delta L}/(4 delta (0.5 + 0.704 L)), i.e. up to doubly exponential heights: no window is height-local for large-delta defects.
4. Between 2 and 3 there is no theorem. The model numerics show that the Nyquist window L_N(T) is the right scale only for very-near-line defects (kappa <~ 0.25), within O(0.6), and that the local real-zero configuration shifts L* by O(1) (C4-ADJ-WIT).
5. For the energy-Schur route (CURRENT_RESULTS Sec. 7; OPEN_CUTS Sec. 3): (i) positive Galerkin effective matrices approach from above and certify nothing; the margin to be certified is lambda_min(L) ~ 1.7e-17 at L = 0.8, 6e-30 at 1.0 and 8e-49 at 1.2 (upper bounds). (ii) Under H1, positivity at window L excludes single defects only in the C4-ADJ-INV region, which adds nothing beyond T_PT until L > 6.49 (delta = 0.49). (iii) No sparser-than-L_N family of windows is known to control near-line defects, and no proof that L_N-scale windows are necessary exists either. (iv) C4-C and the host's S_L are the same completing-the-square lemma on the zero and arithmetic sides: a structural analogy, not a result.

---

## 4. Negative results, withdrawn and rescoped statements

- **REFUTED: the brief's Nyquist heuristic** (window L blind to off-line zeros at T >> 2 pi e^{2L}, up to O(log 1/delta)) for every fixed delta > 0. The rigorous version is conditional on H1 (C4-B, C4-ADJ-C).
- **REFUTED: C4-R "corrected statement"** as a universal near-line locality law. Certified counter-witnesses are in Sec. 3.5. Model dependence (additive vs collision) is O(1) in L.
- **REFUTED: the C4-LAT mirror-pair aside** ("take a higher sinc power"). The mirror term grows with p near the Nyquist edge (Sec. 1 row 4). Repaired.
- **WITHDRAWN: C4-H normalised conjecture** (a corollary of C4-B), "0 <= c(T)" (unsupportable by Rayleigh-Ritz; additive exception certified), and "supported by C4-D4".
- **WITHDRAWN: C4-REL (2)** as guidance ("only windows L >~ L_N + O(0.2) see near-line defects").
- **Rescoped:** C4-P to 2 significant digits as upper bounds; "additive and collision models differ by up to 0.8" (REPORT failed attempts) to 0.24-1.12; C4-D3 sinh near-optimality to delta >= 0.3, T >= 1e12; C4-B2 delta* = 0.2354 (not 0.22); C4-0 L_c = 0.4053787 (not 0.405408); C4-B asymptotic coefficient 0.704 L (not 1.407 L).
- **Infeasible as planned (investigator):** lambda_min(L) for L up to 3. Double precision fails beyond L ~ 0.6, and L = 3 needs dimension ~5e3 at ~1e3 digits. Zhu Table 3 gives certified upper bounds to L = 2.
- **Adjudicator negative records:**
  - First Arb run: the removed-zero terms came out as [+- 2e123]. The 2e-25 radius of the zero ordinate was amplified by the cancellation in the integration-by-parts sum. Fixed by evaluating at the midpoint and adding |h'| <= L sqrt(2L) ||p|| times the radius.
  - Arb's exp() of a wide ball (width ~0.6 in log10 T) is a midpoint-radius enclosure containing 0, which made a tail check fail (never a false positive). Fixed with log10-T steps of 0.05.
  - python-flint's acb uses .conjugate(), not .conj().
  - The first collision runs used only the Arb radius column of EXP-0001; the 5e-21 printing error of the midpoints (reproducibility.md) was then added. Collision-witness radii grew from ~1e-22 to ~5e-19; all signs unchanged.
- **Not done:** no zeros-side Arb evaluation of the witnesses (the arithmetic side is exact; agreement with the investigator's float64 matrices to <= 3.4e-10 is the cross-check). No certified lower bound on any threshold. Yoshida 1992 and Bombieri 2003 not read in full. Trudgian 2014 read only via its zbMATH review.

---

## 5. Reproducibility

Environment: Linux x86-64, Python 3.13.18, python-flint 0.9.0 (Arb), mpmath 1.3.0, numpy 2.5.3, scipy 1.18.1. One BLAS thread; at most 2 cores. Zero data: `experiments/results/zeros/zeta_zeros_1_100000_arb.tsv.gz` (EXP-0001). Scripts read the scratchpad copies `.../scratchpad/data/zeros_{1_50000,50001_100000}.tsv` (paths set in `C1-detection-horizons/common.py` and `adjudicator/adj_witness.py`).

```bash
cd /home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C4-weil-window-locality
export OPENBLAS_NUM_THREADS=1
# investigator (outputs in ../../results/C4-weil-window-locality/, hashes in manifest_C4.json and REPORT.md; all re-verified)
python3 exp_lambda_profile.py main                 # lambda_profile_main.json  1dcdd50d...9b79  ~627 s (Arb)
python3 hp_spectral_check.py                       # hp_spectral_check.json    1a99c939...b5b
python3 exp_detect.py lowT 30,50,100,200,500,1000,2000 add 1.0          # detect_lowT.json   0768eb39...b0e  ~70 s
python3 exp_detect.py midT 5000,10000,20000,50000,70000 add 1.0         # detect_midT.json   3a334204...4519 ~698 s
C4_DELTAS=0.2,0.3,0.4,0.45,0.49 python3 exp_detect.py highT 1e6,1e8,1e10 add 1.0   # detect_highT.json 04d7ae79...e806
python3 exp_detect.py collision 100,1000,10000 collision 1.0             # detect_collision.json bb0a0e60...7383
python3 exp_detect.py convN15 100,1000,10000 add 1.5                     # detect_convN15.json  a16707e9...7388
C4_DELTAS=0.01,0.1,0.3,0.49 python3 exp_detect.py convN_T100 100 add 2.0        # detect_convN_T100.json (also _s3 with 3.0)
C4_DELTAS=0.01,0.1,0.3,0.49 python3 exp_detect.py convN_T1000_s2 1000 add 2.0   # detect_convN_T1000_s2.json
C4_DELTAS=0.01,0.1,0.3 python3 exp_detect.py convN_T1000_s3 1000 add 3.0        # detect_convN_T1000_s3.json
python3 exp_detect_ultra.py                        # detect_ultra.json  6a15e0db...08af  ~140 s
python3 check_flat_lattice.py; python3 thmB_bound.py; python3 psi_eff_diag.py; python3 make_tables.py
# skeptic: scripts in skeptic/ (run_detect_A.sh, run_detect_B.sh, run_profile_conv.sh, sk_*.py); hashes in SKEPTIC_REVIEW.md
# adjudicator (outputs in ../../results/C4-weil-window-locality/adjudicator/)
python3 adjudicator/adj_numbers.py                 # adj_numbers.json   1afc4c8d...b328   5.6 s
python3 adjudicator/adj_thmB_arb.py                # adj_thmB_arb.json  d5315119...ae9d   0.9 s
python3 adjudicator/adj_Cdelta.py                  # adj_Cdelta.json    7e56566e...a683   119 s
for c in coll_T1e4_d0.1 coll_T1e4_d0.2 coll_T1e4_d0.1_L3.3 coll_T1e4_d0.03_L3.67 \
         add_T1e4_d0.49 add_T1e3_d0.01 add_T7e4_d0.2 add_T7e4_d0.2_L4.5; do
  python3 adjudicator/adj_witness.py $c            # adj_witness_<case>.json, 0.7-36 s each
done
# manifest: results/C4-weil-window-locality/adjudicator/manifest_adjudicator.json (code and output sha256, runtimes)
```

The exact T lists for the investigator's `exp_detect.py` runs were read from `results[].T_target` in each output JSON; the command lines themselves were not recorded by the investigator. Adjudicator output JSONs contain runtime fields, so byte hashes change on rerun; the reproducible content is the balls and values. Code hashes (sha256, first 8 hex): adj_numbers.py 2beaa350, adj_thmB_arb.py 784248bb, adj_Cdelta.py b541d4b9, adj_witness.py 24850785. Total results directory: 384 KB. Arb certificates are conditional on the correctness of FLINT/Arb. Everything mpmath or float64 produces is non-rigorous.

---

## 6. Next precise steps for a researcher

1. **Local resolvent bound (the blindness half).** For zeta, bound D(T,delta,L) = lambda_max(E_w^*(P + 2E_uE_u^*)^{-1}E_w) from above for T >= (1+c) 2 pi e^{2L}. Natural route: the identity P(g) = (1/2pi) int |h_g(r)|^2 Psi_L(r) dr + pole terms, with Psi_L(r) = Re psi(1/4 + ir/2) - log pi - sum_{n<e^{2L}} 2 Lambda(n) n^{-1/2} cos(r log n) (exact, because f vanishes for |y| >= 2L). Prove hypothesis R with explicit eta when Psi_L stays >= Psi0/(1+eta) on |r - T| <~ few/L. Also exhibit heights where R fails, via prime-phase alignment (Zhu Lemma 3.2, A_L ~ 4e^L).
2. **Detection near the line.** Replace C(delta) ~ 2.5/delta (C4-ADJ-C) by O(log(1/delta)) or O(1), under H1. The sinh function cannot do this. Try an interpolating PW_L function vanishing at the real zeros near T (Landau-Widom/prolate construction at full saturation, beyond Zhu's half-saturation canonical product). Cheaper first step: replace Trudgian's S(t) term by an S_1(t) bound with a smoother window to remove the (1 + 1.41L) loss.
3. **Remove H1 locally.** Prove C4-B when the other off-line zeros (if any) lie at distance >= (log T)^{C/delta} from T. The cross terms of a far pair at T' are bounded by A^2/|T - T'|^2 for the sinh test function.
4. **Certified lower bounds on model thresholds.** Certify a positive lower bound for the injection-model form at one (T0, delta, L) with L just below the float threshold, e.g. collision, T0 = 9999.46, delta = 0.1, L = 3.2. It would need a certified lower bound on P in the modulated frame, of the same type as Zhu's geometric-side certificates. This is the only way to turn "L* ~ L_N" into anything two-sided.
5. **N -> inf offsets.** Recompute c(T) and b(T) with endpoint-adapted bases (prolate functions or explicit endpoint singular terms; ACL Sec. 8.7 notes jumps at the ends of the form domain). Report T0 = 100, 1000, 1e4 at delta = 0.01, 0.1. Current upper bounds: 0.170 (T0 = 100, N = 192) and 0.158 (T0 = 1000, N x3).
6. **Host translation.** Before any number here is used in the energy-Schur route, map the brief's L to the host's window parameters (OPERATOR_AUDIT.md: the L = 1, X = 3, K = 101 subspace) and check which normalisation of the Fourier transform and support the host uses.
7. **Primary sources.** Read in full: Yoshida 1992 (Hermitian forms attached to zeta functions); Bombieri 2003; Trudgian 2014 (to lift the S(t) input from L0+ to L1); Burnol math/0203120 (completeness thresholds of zero systems in Sonine spaces versus window size); Suzuki arXiv:2610.32704 (t_{a,n} >= gamma_n, decreasing to gamma_n), to compare "reconstruction" heights (ACL: about 2T*) with detection heights.
