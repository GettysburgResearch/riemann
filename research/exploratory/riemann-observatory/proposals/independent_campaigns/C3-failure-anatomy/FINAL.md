# C3-failure-anatomy: FINAL (adjudicated)

This is the adjudicator's report. `REPORT.md` (investigator) and `SKEPTIC_REVIEW.md` (skeptic) are kept unchanged as the record. Where this file and those two disagree, this file states the final status and the reason.

```text
Status:
  ADJUDICATED EXPLORATORY DOSSIER. No claim about RH or its negation is made anywhere.
  It contains:
  - 8 statements with complete proofs, labelled THEOREM: C3-A1, C3-Q1, C3-M1, C3-O1, C3-ADJ-S, C3-ADJ-O2,
    C3-CG1 (computer-assisted), and the identity in C3-D1-scan;
  - IMPORTED literature statements, each with its source and the evidence level actually reached (L0/L0+/L1);
  - NUMERICAL-RIGOROUS replays (Arb balls or exact integers). Every investigator replay was reproduced by an
    independent skeptic implementation. The adjudicator's extensions (n > 20000; the 10^6..10^10 blocks) are
    single-implementation, cross-checked against a second formula for n <= 20000;
  - 1 CONJECTURE (C3-ADJ-RATE) with heuristic support;
  - a failure-mode taxonomy and a one-page checklist, both HEURISTIC (methodological, not theorems).
  Evidence level of this adjudication: L2 for the items re-derived here (Conrey-Li Thm 1 consequence and Sec. 3,
  Oliva v1 Sec. 2, Bellissard's comment, the Hurst table, Platt-Trudgian 2016 Thms 1-2). L1 or L0+ elsewhere,
  as stated per claim.

Scope:
  14 dossiers:
  - de Branges positivity and Conrey-Li 2000;
  - X.-J. Li 2008;
  - Atiyah 2018;
  - Bender-Brody-Mueller 2017 and Bellissard;
  - Turan's partial-sum hypothesis (Montgomery 1983);
  - Mertens and Stieltjes (Odlyzko-te Riele 1985);
  - Polya and Turan's T(x) (Haselgrove 1958);
  - Cramer's model and Maier 1985;
  - mollifier and proportion ceilings (Hardy-Littlewood, Selberg, Levinson-Conrey);
  - three 2018-2026 arXiv claims (Oliva 1807.06447, Queme 2004.00460, Micheas 2607.04338);
  - corrected published explicit constants (Turing->Lehman, Cheng-Graham->Hiary-Patel-Yang, Ford 2002,
    Feng 2012->PRZZ/Pratt-Robles, Pearce-Crump 2026);
  - the Davenport-Heilbronn countermodel.
  Also: a taxonomy, a checklist, and four adjudicator additions (C3-ADJ-S, C3-ADJ-RATE, C3-ADJ-O2, C3-ADJ-M).

Exact sources or dependencies:
  Per claim, in the table in Section 2.
  Load-bearing primary texts read by the adjudicator:
  - Conrey-Li, arXiv:math/9812166 (pdf sha256 bdb68ede...4568), Thms 1-2, Sec. 3, Remark;
  - Oliva, arXiv:1807.06447v1 (16ee55e7...), Sec. 1-2;
  - Bellissard, arXiv:1704.02644 (36244a8e...), pp. 2-3;
  - Hurst, arXiv:1610.08551 (18bdf91d...), Sec. 6.1 table;
  - Platt-Trudgian, "On the first sign change of theta(x)-x", Math. Comp. 85 (2016) 1539-1547,
    doi:10.1090/mcom/3021, arXiv:1407.1914 (cb4ee24a...), Thm 1, Thm 2, Sec. 3.1.5, Cor. 2;
  - Tao blog comment page 1 (b566f1f6...).
  Metadata fetched on 2026-11-17:
  - arXiv API for 0807.0090, 1807.06447, 2004.00460, 2607.04338, 2608.13637, 2609.02882, 2609.15329,
    2609.24167, 2610.08965;
  - zbMATH 1425.32011;
  - Crossref 10.1142/S0219887819500919.
  Certified zeros: zeros_1_50000.tsv (sha256 6a7eb7ab...cc88) and zeros_50001_100000.tsv (494b5c10...5e5a),
  plus flint.acb.zeta_zeros(n0, 1000) for n0 = 10^6 ... 10^10.

What was actually run:
  - Investigator: 3 scripts (sieve to 1e9; Arb Conrey-Li scan to K=20000; 8 witness sections).
  - Skeptic: 6 re-implementations with different algorithms and libraries.
  - Adjudicator: 4 new scripts under experiments/code/C3-failure-anatomy/adjudicator/:
    (i)   adj_debranges_S.py: exact S(t)-reformulation of the de Branges zero condition, Arb, first 100000
          zeros, plus a direct xi(3/2+i gamma) cross-check for n <= 20000; 261 s.
    (ii)  adj_debranges_highblocks.py: 1000-zero blocks at n0 = 1, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 1e10;
          Arb verdicts plus a Gaussian comparison; 372 s.
    (iii) adj_mertens_point.py: exact M(x) at isolated x by the M(v) recursion; 3 s.
    (iv)  adj_misc_checks.py: sympy algebra of Oliva's (3); Arb bounds for C3-ADJ-O2; longdouble Cheng-Graham sum;
          mpmath Davenport-Heilbronn and zeta_19 residuals; Micheas gap; 1 s.
  All investigator and skeptic output hashes were re-verified and match their manifests.

Smallest remaining gap:
  (a) arXiv:0807.0090 v5-v10 (2024-2025, a new unrefereed claimed proof under the 2008 identifier): not audited
      by anyone in this campaign. No published critique was located.
  (b) de Branges' post-2004 manuscripts: not audited against Conrey-Li.
  (c) Primary texts still at L0/L0+: Turan 1948, Montgomery 1983, Maier 1985, Odlyzko-te Riele 1985,
      Haselgrove 1958, Turing 1953, Lehman 1970, Cheng-Graham 2004, Stieltjes 1885. Their statements rest on
      zbMATH reviews and on L1 secondary sources.
  (d) For the de Branges zero condition: it is NOT proved that it fails infinitely often, let alone for a
      positive proportion of zeros. Conrey-Li give one failure; we give 15567 among the first 10^5 zeros and
      a conjectured limiting rate of 1/2 (C3-ADJ-RATE).
```

---

## 1. How the disagreements were resolved

| # | Point of disagreement | Resolution | Basis |
|---|---|---|---|
| 1 | C3-D1. The de Branges condition was called "strictly stronger than RH". | **Skeptic upheld.** "Strictly stronger" has content only if RH is true. Correct wording: a sufficient condition for RH that is unconditionally false. | Logic. |
| 2 | C3-D1-scan. Investigator: the sign condition is a "phase-locking [with] no arithmetic reason". Skeptic: it is a Gram-type phase condition. | **Skeptic upheld, and sharpened into a theorem.** The condition at the n-th zero is exactly a condition on S(gamma_n) mod 2 (C3-ADJ-S, proof in Sec. 3.2). The investigator's sentence is withdrawn. | Proof in Sec. 3.2. A third independent count over 10^5 zeros, at 0 undetermined, matches the other two exactly where they overlap. |
| 3 | C3-D2. The time of Tao's first comment. | **Skeptic upheld:** "2 July, 2008 at 6:28 pm". The quoted text, about (6.9) and the dilation symmetry, is in that comment. | Cached page, line 763. |
| 4 | C3-D3. "The companion paper was not found in zbMATH or Crossref." | **Corrected by the adjudicator.** The Todd-function construction was published posthumously as M. Atiyah and J. Kouneiher, "Todd function as weak analytic function", Int. J. Geom. Methods Mod. Phys. 16 (2019), no. 6, 1950091, doi:10.1142/S0219887819500919, Zbl 1425.32011. Its abstract does not mention RH, and its content was not read (L0). No publication titled "The fine structure constant" was found. | zbMATH API; Crossref API. |
| 5 | C3-D4. Bellissard's weighted-space shift; "no Hilbert space has been exhibited". | **Skeptic upheld.** Bellissard's generator is A_alpha = i x d/dx + i(alpha+1)/2, so the real-eigenvalue line for x^{-z} is Re z = (alpha+1)/2. Normalizability of psi_z at Re z = 1/2 in L^2(x^alpha dx) needs alpha < -2, which puts that line at Re z < -1/2. "No Hilbert space has been exhibited" is qualified to "to our knowledge (searched: arXiv API, the BBM reply, Liu 2026, Mueller 2017)". | Bellissard pp. 2-3, re-read. Elementary computation. |
| 6 | C3-D9. The "ceilings" list. | **Skeptic upheld.** Item 1 ("kappa < 1 for every proven theta") is a record, not a theorem, and is withdrawn as a "ceiling". Item 3: Hardy-Littlewood and Selberg count sign changes of Z(t); Levinson-Conrey count zeros via Littlewood's lemma. Neither excludes any off-line zero. Knausgard arXiv:2610.08965 (Oct 2026, unrefereed, L0+: 0.67353 simple and critical) is added. | arXiv metadata. |
| 7 | C3-TAX, F15. Two arXiv items were cited only for their version counts. | **Skeptic upheld.** A version count is not a mathematical failure mode, and no error in either item was identified by us or located in the literature. Both are removed from the taxonomy. F15 now cites only D10, where the author's own withdrawal states that both versions have critical errors. | Methodology Sec. 6(iv). |
| 8 | C3-CHECKLIST item 13. "Mertens (\|M\|/sqrt x < 0.571 up to 1e16)". | **Skeptic upheld, and checked independently.** It fails for small x (\|M(5)\|/sqrt 5 = 0.894). Hurst's 0.571 is the rounded value at x = 7766842813. The adjudicator's exact recursion gives M(7766842813) = 50286, so q = 0.5705909. Item 13 is rewritten (Sec. 6). | adj_mertens_point.json. |
| 9 | C3-O1. Oliva's step (3) is "numerically true and false infinitely often". | **Sharpened by the adjudicator** (C3-ADJ-O2). Step (3) holds for every prime 5 <= p <= 1.39e17 and fails for some prime p < exp(727.951332668), and infinitely often. So the first failure lies in an explicit window. This answers the investigator's open question. | Proof in Sec. 3.4. Imports Platt-Trudgian Thms 1-2 and Cor. 2. |

No investigator claim is REFUTED in its mathematical content. One interpretive sentence (item 2) is withdrawn, and one bibliographic sentence (item 4) is corrected.

---

## 2. Adjudicated claims table

Evidence levels follow methodology Sec. 5: L0 = index only; L0+ = abstract or review only; L1 = full text read.

**Summary table** (details and corrections follow in 2a and 2b).

| ID | Short statement | Investigator label | Skeptic verdict | FINAL status |
|---|---|---|---|---|
| C3-D1 | Conrey-Li: de Branges conditions (3.1), (3.3), (3.7), (3.8) false; implications correct | IMPORTED + NUM-RIG | upheld, minor wording | IMPORTED + NUMERICAL-RIGOROUS (wording corrected) |
| C3-D1-scan | 195/2000 and 2724/20000 zero-condition failures | NUM-RIG + sketch | counts upheld; mechanism corrected | NUMERICAL-RIGOROUS (counts, 3 implementations; 15567/10⁵ added); identity THEOREM; mechanism sentence WITHDRAWN |
| C3-D2 | Li 2008 v1-v3: failing steps per Tao and Connes; v4 withdrawn | IMPORTED | upheld, timestamp fix | IMPORTED (v5-v10 unaudited) |
| C3-D3 | Atiyah 2018: 2.6 forces T constant; proves too much | IMPORTED + THEOREM | upheld | IMPORTED + THEOREM (publication note corrected) |
| C3-A1 | h(u+v+uv) = h(u+v) implies h constant | THEOREM | upheld | THEOREM |
| C3-D4 | BBM conditional programme; no self-adjoint realization exhibited | IMPORTED + NUM-RIG | upheld, wording fixes | IMPORTED (+ imported non-L² fact; numerics illustrative) |
| C3-D5 | Turan partial sums refuted (Spira, Montgomery, Platt-Trudgian) | IMPORTED + NUM-RIG | upheld | IMPORTED + NUMERICAL-RIGOROUS |
| C3-D6 | Mertens refuted; Stieltjes open | IMPORTED + NUM-RIG | upheld | IMPORTED + NUMERICAL-RIGOROUS |
| C3-D7 | Polya and Turan T refuted (Haselgrove) | IMPORTED + NUM-RIG | upheld | IMPORTED + NUMERICAL-RIGOROUS |
| C3-D8 | Cramer model vs Maier | IMPORTED + sketch | upheld | IMPORTED + PROPOSITION-PROOF-SKETCH |
| C3-D9 | Mollifier and proportion ceilings | IMPORTED | upheld with corrections | IMPORTED (ceiling item 1 withdrawn, item 3 refined) |
| C3-D10 | Oliva 2018: step (3) fails | IMPORTED + sketch | upheld | IMPORTED + THEOREM |
| C3-O1 | Direction error; (3) fails infinitely often; equivalent to RH given Nicolas | PROPOSITION-PROOF-SKETCH | upheld | THEOREM (modulo imported Littlewood; float part superseded) |
| C3-D11 | Queme 2020: illegitimate boundary termwise limit | IMPORTED + THEOREM | upheld | IMPORTED + THEOREM |
| C3-Q1 | Taylor series diverges at a boundary pole | THEOREM | upheld | THEOREM |
| C3-D12 | Micheas 2026: Theorem 1 false | IMPORTED + THEOREM | upheld | IMPORTED + THEOREM |
| C3-M1 | Explicit counterexample to Micheas Thm 1 | THEOREM | upheld | THEOREM |
| C3-D13 | Published constants corrected in print | IMPORTED | upheld | IMPORTED |
| C3-CG1 | Explicit counterexample to Cheng-Graham Lemma 2 | THEOREM | upheld | THEOREM (computer-assisted) |
| C3-D14 | Davenport-Heilbronn off-line zero | NUM-RIG + IMPORTED | upheld | NUMERICAL-RIGOROUS + IMPORTED |
| C3-TAX | Taxonomy F1-F15 | HEURISTIC | upheld with corrections | HEURISTIC (tags; F15 restricted) |
| C3-CHECKLIST | 20-item checklist | HEURISTIC | item 13 corrected | HEURISTIC (item 13 rewritten) |
| C3-ADJ-S | de Branges zero condition ⇔ S(γ_n) − δ_n mod 2 outside (3/4, 7/4) | (new) | (new) | THEOREM + NUMERICAL-RIGOROUS |
| C3-ADJ-RATE | Failure proportion → 1/2 | (new) | (new) | CONJECTURE |
| C3-ADJ-O2 | Oliva (3): true for p ≤ 1.39e17, false below e^{727.95}, false infinitely often | (new) | (new) | THEOREM (modulo IMPORTED) |
| C3-ADJ-M | M(7766842813) = 50286, M(10¹⁰) = −33722 | (new) | (new) | NUMERICAL-RIGOROUS |

No claim receives REFUTED. The only WITHDRAWN item is the D1-scan mechanism sentence.

### 2a. Dossiers

**C3-D1. De Branges positivity and Conrey-Li Thm 1 / Thm 2.**
- Statement: the implications are correct, but the hypotheses fail for E(z) = xi(1-iz) and W = 1/xi(1-iz) and for chi_4. Conditions (3.1), (3.3), (3.7) and (3.8) are false.
- FINAL status: **IMPORTED** (Conrey-Li, IMRN 2000 no. 18, 929-940; read at L1 by all three agents) **+ NUMERICAL-RIGOROUS** (four witnesses replayed: Arb 192-bit by the investigator; mpmath, 20 digits, by the skeptic).
- Adjudication note: wording corrected (item 1). Sarnak's numerics-free proof covers only the F(W) conditions (3.3) and (3.8), for all Dirichlet characters.

**C3-D1-scan (counts).** The zero condition -Re{xi'(rho_n)xi(1+rho_n)} >= 0 fails at 195 of the first 2000 zeros and 2724 of the first 20000.
- FINAL status: **NUMERICAL-RIGOROUS**, by three independent implementations: investigator (Arb power-series xi'); skeptic (Arb closed form, TSV zeros, with an mpmath sample); adjudicator (S-reformulation, never evaluating xi').
- Extended by the adjudicator: **15567 of the first 100000** (15.567%), with 0 undetermined. The first 60 failing indices are identical across implementations.
- Dependency now stated explicitly: zeros simple, on the line, and correctly indexed up to gamma_K. This is certified by acb.zeta_zeros (Turing-method indexing).

**C3-D1-scan (identity).** -Re{xi'(rho)xi(1+rho)} = -Xi'(gamma) Im xi(3/2+i gamma) for rho = 1/2+i gamma.
- FINAL status: **THEOREM** (elementary). Re-verified, with residual 0 for n <= 200 (skeptic).

**C3-D1-scan (mechanism sentence).** "phase-locking has no arithmetic reason to hold".
- FINAL status: **WITHDRAWN**. It is superseded by C3-ADJ-S (item 2).

**C3-D1-scan (Thm 2 grid).** Re{xi(1+it)/xi(2+it)} < 0 on the grid t in [1,1000], step 1/4, exactly at {282, 527.25, 527.5, 527.75, 836.5, 898.75, 899}.
- FINAL status: **NUMERICAL-RIGOROUS** (Arb, at grid points only), reproduced in mpmath by the skeptic.
- Adjudication note: grid information only. It says nothing between grid points.

**C3-D2. X.-J. Li, arXiv:0807.0090, the 2008 text (v1-v3).**
- Failing steps per public expert comments: (6.9) on p. 20 (Tao, fixed in v2/v3); Thm 7.3 on p. 29, extending from ideles to adeles by 0, where ideles have measure 0 (Connes; Tao "after (7.13)"); an invertibility assumption on p. 18 that fails if there is an off-line zero (Tao, 7 July). v4 was withdrawn by the author "due to mistake on page 29".
- FINAL status: **IMPORTED** (blog texts L1; arXiv metadata L0, re-fetched 2026-11-17: v10 dated 2025-10-12, comment "Improved presentation. No results changed").
- Adjudication note: timestamp corrected (item 3). "Withdrawn" applies only to the 2008 text. **v5-v10 were not audited, and nothing is claimed about them.**

**C3-D3. Atiyah 2018 preprint, Sec. 2-3.**
- Failing steps: (i) property 2.6 forces T to be constant (C3-A1), so "T invertible => zeta == 0" fails; (ii) under the "linear approximation" reading, 3.3 does not follow; (iii) the argument proves too much, because it never uses Re b != 1/2.
- FINAL status: **IMPORTED** (preprint L1; Lipton-Regan L1) **+ THEOREM** (via C3-A1).
- Adjudication note: publication status corrected (item 4). Atiyah died in January 2019.

**C3-A1.** If h(u+v+uv) = h(u+v) in C[[s]] for all u, v in sC[[s]], then h is constant.
- FINAL status: **THEOREM**. The proof was re-derived by all three agents. Exact checks: sympy to degree 13 (investigator); integer Bareiss to degree 59 (skeptic).
- Adjudication note: this applies to Atiyah's T only under the formal-power-series reading of 2.6. The text does not define T well enough to fix one reading, and that is itself failure mode F9.

**C3-D4. Bender-Brody-Mueller 2017.**
- This is a CONDITIONAL programme ("if ... can be made rigorous"), not a claimed proof.
- Bellissard: p on L^2(0,inf) with the Dirichlet condition has deficiency indices (1,0), and psi_z is not in L^2 at Re z = 1/2.
- FINAL status: **IMPORTED** (Bellissard and the BBM reply L1; Liu 2607.19067 and Mueller 1704.04705 L0+).
- psi_z(x) = -zeta(z,x+1) is not in L^2(0,inf) for Re z <= 3/2. This follows from zeta(z,x+1) ~ (x+1)^{1-z}/(z-1) (DLMF 25.11.43), which is an IMPORTED theorem. The numbers 1.00332 ... 1.000000000025 are a NUMERICAL-RIGOROUS illustration (Arb; reproduced by the skeptic in mpmath plus Euler-Maclaurin).
- Adjudication note: wording corrected (item 5).

**C3-D5. Turan's partial-sum hypothesis.**
- Refuted for N = 19, 22-27, 29-50 by Spira 1968, and for all large N by Montgomery 1983. Platt-Trudgian 2016: zeta_N has no zeros in sigma > 1 iff N <= 18 or N = 20, 21, 28.
- FINAL status: **IMPORTED** (Platt-Trudgian L1; Montgomery and Turan L0) **+ NUMERICAL-RIGOROUS** (the zeta_19 zero at Re = 1.0010955..., certified by Krawczyk and, independently, by Rouche).
- Adjudication note: the adjudicator's mpmath residual \|zeta_19\| = 3.4e-23 at the ball centre is consistent.

**C3-D6. Mertens and Stieltjes.**
- Mertens' \|M(x)\| < sqrt x is REFUTED (Odlyzko-te Riele 1985: limsup > 1.06, liminf < -1.009). The best bounds are Hurst 2018: limsup > 1.826054, liminf < -1.837625.
- Stieltjes' M(x) = O(sqrt x) is **OPEN** (believed false; Ingham 1942).
- FINAL status: **IMPORTED** (zbMATH reviews L0+; Hurst and Kim-Nguyen L1) **+ NUMERICAL-RIGOROUS** (two independent exact sieves to 1e9, plus the adjudicator's exact point values).
- Adjudication note: the task premise "Stieltjes refuted" stays corrected.

**C3-D7. Polya's L(x) <= 0 and Turan's T(x) >= 0 for large x.**
- Both refuted by Haselgrove 1958. Smallest counterexamples: L at 906150257 (Tanaka 1980); T at 72,185,376,951,205 (Borwein-Ferguson-Mossinghoff 2008).
- FINAL status: **IMPORTED** (zbMATH L0+; BFM review) **+ NUMERICAL-RIGOROUS** (two exact sieves agree on every figure; T(x) > 1.42e-6 > 0 for x <= 1e9 by an exact fixed-point certificate).

**C3-D8. Cramer's model and Maier 1985.**
- Model prediction for lambda > 2: PROPOSITION-PROOF-SKETCH. Maier 1985: Omega_± for every lambda > 1. Banks-Ford-Tao 2023: the model ignores mod-p bias.
- FINAL status: **IMPORTED** (Maier zbMATH L0+; BFT L1) **+ PROPOSITION-PROOF-SKETCH** (Chernoff + Borel-Cantelli, lambda > 2 sharp for that argument, re-derived by the skeptic).

**C3-D9. Mollifier and proportion methods.**
- A proportion, even 1-o(1), never excludes an individual off-line zero. Sign-change methods (Hardy-Littlewood, Selberg) and Levinson-Conrey (Littlewood's lemma) both give lower bounds for zeros on the line only.
- Records: PRZZ more than 5/12. In 2026, by a different mechanism (unrefereed): Alpoge-Furman >= 2/3, Lamzouri 67.25%, Knausgard 67.353%. Selberg's method alone: more than 6.78% (Pearce-Crump v2).
- FINAL status: **IMPORTED** (PRZZ L1 Sec. 1; Conrey 1989 and Farmer 1993 zbMATH L0+; the 2026 items L0+).
- Adjudication note: ceiling item 1 withdrawn and item 3 refined (item 6).

**C3-D10. Oliva, arXiv:1807.06447.**
- v1 claimed a proof, v2 a disproof, v3 is "Withdrawn for expected critical errors in both versions" (re-fetched 2026-11-17).
- FINAL status: **IMPORTED** (status, and v1 text at L1) **+ THEOREM** (C3-O1, C3-ADJ-O2).

**C3-O1.** On Oliva's step (3):
- (a) direction error: (3) implies (4), not the converse;
- (b) (3) fails infinitely often;
- (c) the lemma is "numerically true" to 2e7;
- (d) given Nicolas' dichotomy, the propagation lemma is equivalent to RH.
- FINAL status: **THEOREM**, upgraded from PROPOSITION-PROOF-SKETCH. (a) and (d) are elementary; (b) has a complete proof in Sec. 3.4, given IMPORTED Littlewood. The float64 part of (c) was **NUMERICAL-NONRIGOROUS** and is now superseded by C3-ADJ-O2(a), which covers p <= 1.39e17.
- Adjudication note: the algebraic equivalence of (3) was re-checked symbolically (adj_misc_checks.json, oliva_algebra).

**C3-D11. Queme, arXiv:2004.00460.**
- v2 comment: "irrecoverable error paragraph 6 page 4". The failing step is a termwise limit eps -> 0 taken at the boundary of the disc of convergence. The argument also proves too much.
- FINAL status: **IMPORTED** (status; v1 L1) **+ THEOREM** (C3-Q1).

**C3-Q1.** If f is meromorphic, analytic on D(rho+v, v), and has a pole at rho, then sum_k (-v)^k f^(k)(rho+v)/k! diverges.
- FINAL status: **THEOREM** (Cauchy-Hadamard plus Abel's theorem; re-derived).

**C3-D12. Micheas, arXiv:2607.04338.**
- v2: "Mistakes in main approach. Withdrawn". Theorem 1 of v1 is false.
- FINAL status: **IMPORTED** (status; v1 L1) **+ THEOREM** (C3-M1).

**C3-M1.** Micheas' Theorem 1 (v1) is false independently of RH. Witness: tau_n = t_n - 1/(2n), b_n = 1/n.
- FINAL status: **THEOREM**.
- Adjudication note: the Arb check t_2 - 1/4 - t_1 = 6.6373 > 0 was redone (adj_misc_checks.json). The skeptic's shorter argument (tau_n = t_n versus tau_n = t_n - 1/(2n) give different zero sets) is also valid, given t_1 < t_2 < ....

**C3-D13. Corrected published explicit constants.**
- Turing's errors were corrected by Lehman.
- Cheng-Graham's Lemma 2 constant 1/pi should be 2/pi (Hiary-Patel-Yang 2022: "has impacted all published explicit subconvex bounds").
- Ford 2002, Thm 4: 8.463 becomes 8.464 (author's v2-v5).
- Feng 2012: a gap, repaired by Pratt-Robles' theta_F = 6/11 (PRZZ).
- Pearce-Crump: 7% becomes 6.78%.
- FINAL status: **IMPORTED** (Trudgian 2011, HPY, Ford v1/v5, PRZZ at L1; Pearce-Crump L0+). Every quotation was located by the skeptic.
- Adjudication note: these are corrections by the authors or by third parties in print. Per methodology Sec. 6(iii) they are reported as such, not as Observatory findings.

**C3-CG1.** Cheng-Graham Lemma 2 as stated (\|sum e(f(n))\| <= 1/(pi theta) + 1) is false. Witness: theta = 0.02, a sigmoid f', n in [975,1025]. \|S\| = 31.598085273673954... > 16.9155, and below Landau's cot(pi theta/2) = 31.8205.
- FINAL status: **THEOREM** (computer-assisted: Arb ball of radius 3e-34; reproduced in mpmath by the skeptic and in numpy longdouble by the adjudicator, 31.598085273673956).
- Adjudication note: this adds only an explicit smooth instance to Landau's 1928 extremal examples. The error was established by HPY and Ford.

**C3-D14. Davenport-Heilbronn.**
- The period-5 Dirichlet series satisfies a Riemann-type functional equation and has a zero at 0.808517182456637385553... + 85.699348485377592171929...i.
- FINAL status: **NUMERICAL-RIGOROUS** (Krawczyk by the investigator; Rouche on 400 arcs by the skeptic) **+ IMPORTED** (the functional equation, Titchmarsh Sec. 10.25).
- Adjudication note: the adjudicator's mpmath check, rebuilt from scratch, gives kappa = 0.28407904384041229603, functional-equation residuals of 1e-38 to 1e-41, \|f\| = 5e-28 at the zero, and \|f'\| = 1.256, so the zero is simple.

**C3-TAX. Failure-mode taxonomy F1-F15.**
- FINAL status: **HEURISTIC** (classification). Corrected: the codes are tags, not a partition, and F15 is restricted (item 7). See Sec. 5.

**C3-CHECKLIST. 20-item checklist.**
- FINAL status: **HEURISTIC**. Item 13 corrected (item 8). See Sec. 6.

### 2b. Adjudicator additions

**C3-ADJ-S. Exact reformulation of the de Branges zero condition through S(t).**
- FINAL status: **THEOREM** (proof in Sec. 3.2) **+ NUMERICAL-RIGOROUS** (data to n = 10^5; blocks to n ~ 10^10).
- This is new as stated, as far as a search of the arXiv API, the AIM de Branges page and the Gram's-law literature (Trudgian, Acta Arith. 148 (2011); Kalpokas-Korolev-Steuding 2012) found. It is elementary.

**C3-ADJ-RATE. The proportion of n <= N at which the zero condition fails tends to 1/2.**
- FINAL status: **CONJECTURE**, with heuristic support from a Gaussian model of S(gamma_n) - delta_n, which matches all 8 blocks (Sec. 3.3).
- Not proved; even "infinitely many failures" is open here.

**C3-ADJ-O2.** Oliva's (3) holds for all primes 5 <= p <= 1.39e17, fails for some prime p < e^{727.951332668}, and fails for infinitely many p.
- FINAL status: **THEOREM** (proof in Sec. 3.4), modulo **IMPORTED** results: Platt-Trudgian, Math. Comp. 85 (2016), Thm 1, Thm 2 with its quantitative form (Sec. 3.1.5) and Cor. 2; and Littlewood 1914 (psi(x) - x = Omega_+(x^{1/2} logloglog x)).
- Arb check of the failure bound in adj_misc_checks.json.

**C3-ADJ-M.** Exact values M(10^9) = -222, M(7766842813) = 50286 (q = 0.5705909), M(10^10) = -33722.
- FINAL status: **NUMERICAL-RIGOROUS** (exact integer recursion, independent of both sieves).
- Confirms Hurst's table entry and corrects checklist item 13.

---

## 3. The most useful precise statements

### 3.1 Conrey-Li, exactly (IMPORTED, L1; arXiv:math/9812166, IMRN 2000)

**Theorem 1 ("essentially due to de Branges").** Let E be entire with:
- no real zeros;
- \|E(z̄)\| < \|E(z)\| for Im z > 0;
- Ē(z̄) = εE(z−i) with \|ε\| = 1;
- \|E(x+iy)\| strictly increasing in y > 0 for each real x.

If Re⟨F(z), F(z+i)⟩_{H(E)} ≥ 0 for every F ∈ H(E) with F(z+i) ∈ H(E), then the zeros of E lie on Im z = −1/2, and Re{Ē′(w)E(w+i)/2πi} ≥ 0 at every zero w of E.

**Theorem 2.** Let W be analytic and zero-free in Im z > 0. Let T be a linear map of F(W) into itself with T K(w,·) = K(w+i,·) for Im w > 0. If Re⟨F, TF⟩_{F(W)} ≥ 0 for all F, then W extends analytically to Im z > −1/2, and Re{W(z)/W(z+i)} ≥ 0 there.

**Application.** Take ξ(s) = s(s−1)π^{−s/2}Γ(s/2)ζ(s) (no factor 1/2) and E(z) = ξ(1−iz).
- The hypotheses of Theorem 1 hold unconditionally, by 0 < Re ρ < 1 and the paired product.
- Condition (3.1) would imply RH, and condition (3.3), on W = 1/ξ(1−iz), would imply zero-freeness for Re s > 1/2.
- Both are **false**: −Re{ξ′(ρ₃₄)ξ(1+ρ₃₄)} = −5.3891005071829451814...×10⁻⁶⁹ and Re{ξ(1+282i)/ξ(2+282i)} = −0.000131957293372083...
- The same holds for χ₄, giving conditions (3.7) and (3.8), with values −2.3103490049934834562×10⁻⁴⁵ and −0.00042234060658023277.

**What this kills.** The positivity conditions themselves. The Hermite-Biehler / de Branges-space framework is untouched.

### 3.2 C3-ADJ-S: the de Branges zero condition is a condition on S(γ_n) mod 2 (THEOREM)

**Notation.**
- θ(t) is the Riemann-Siegel theta function: θ(t) = Im log Γ(1/4+it/2) − (t/2)log π, with θ(0) = 0.
- S(t) = π⁻¹ arg ζ(1/2+it) by the usual continuous variation. At an ordinate, take S(γ) := ½(S(γ⁺) + S(γ⁻)).
- For t > 0 put:
  - a(t) := arg ζ(3/2+it), the principal value. It is continuous, and \|a(t)\| ≤ log ζ(3/2) < 0.961.
  - c(t) := [Im log Γ(3/4+it/2) − Im log Γ(1/4+it/2) − π/4] + [arg(3/2+it) + arg(1/2+it) − π]. Here c(t) = O(1/t), and \|c(γ_n)\| ≤ 0.0402 for 10 ≤ n ≤ 10⁵ (computed; the maximum is at the small end).
  - δ(t) := (a(t) + c(t))/π.

**Theorem.** Let n ≥ 1. Suppose the zeros of ζ with 0 < Im ρ ≤ γ_n are exactly 1/2+iγ_1, ..., 1/2+iγ_n, with γ_1 < ... < γ_n, and all are simple. Put P_n := −Re{ξ′(ρ_n)ξ(1+ρ_n)}, which is the quantity Theorem 1 requires to be ≥ 0. Then

  sign P_n = sign sin(π S(γ_n) + π/4 − a(γ_n) − c(γ_n)).

Equivalently, P_n < 0 if and only if S(γ_n) − δ(γ_n) ∈ (3/4, 7/4) (mod 2).

**Proof.**
1. Write Ξ(t) = ξ(1/2+it), which is real for real t. Then ξ′(ρ_n) = −iΞ′(γ_n), so P_n = −Ξ′(γ_n) Im ξ(3/2+iγ_n).
2. From π^{−s/2}Γ(s/2) = π^{−1/4}\|Γ(1/4+it/2)\|e^{iθ(t)} on s = 1/2+it, and s(s−1) = −(1/4+t²), we get Ξ(t) = −(1/4+t²)π^{−1/4}\|Γ(1/4+it/2)\| Z(t), where Z(t) = e^{iθ(t)}ζ(1/2+it). Hence −Ξ′(γ_n) is a positive multiple of Z′(γ_n).
3. By hypothesis Z has exactly the simple zeros γ_1, ..., γ_{n−1} in (0, γ_n), and Z(0) = ζ(1/2) < 0. Hence sign Z′(γ_n) = (−1)^{n+1}.
4. ξ(3/2+it) ≠ 0. Taking arguments factor by factor, the π^{−s/2} phases cancel against θ, and arg ξ(3/2+it) ≡ θ(t) + 5π/4 + a(t) + c(t) (mod 2π).
5. The hypothesis gives N(γ_n) = n − 1/2 with the averaged convention. Then N(T) = θ(T)/π + 1 + S(T) (Titchmarsh 9.3) gives θ(γ_n) = π(n − 3/2 − S(γ_n)).
6. Combining steps 3-5:
   sign P_n = (−1)^{n+1} sign sin(π(n − 3/2 − S) + 5π/4 + a + c) = sign sin(πS + π/4 − a − c).
   This is negative exactly when πS + π/4 − a − c ∈ (π, 2π) mod 2π, which is the stated window. ∎

**Consequences.**
- Since \|δ(γ_n)\| ≤ (0.961 + 0.0402)/π < 0.319 for 10 ≤ n ≤ 10⁵, and for all large n because c(t) = O(1/t), the condition **fails** at every such n with S(γ_n) ∈ [−0.93, −0.57].
- In the skeptic's Gram-offset language, u_n = θ(γ_n)/π − n = −3/2 − S(γ_n). The failures are zeros lying late in, or beyond, their Gram interval. This is exactly the skeptic's table: 0/995 failures for u_n < −1.5, and 63/63 for u_n ≥ −1.
- The condition is therefore governed by the same object as Gram's law, namely S at special points. It is a statement about S(t), not about anything new.

**Numerical confirmation (NUMERICAL-RIGOROUS).** adj_debranges_S.py evaluates sin(πX_n), with X_n = S(γ_n) − δ(γ_n) − 3/4, in 128-bit Arb on the certified ordinate balls. It never evaluates ξ′.
- Result: 15567 failures among n ≤ 100000, with 0 undetermined.
- This agrees with the investigator and the skeptic on n ≤ 20000: 195 failures for n ≤ 2000, 2724 for n ≤ 20000, and identical first indices 34, 71, 106, 127, ...
- A direct Arb evaluation of sign((−1)^{n+1} Im ξ(3/2+iγ_n)) with Γ, not log Γ, agrees at all n ≤ 20000.

### 3.3 C3-ADJ-RATE (CONJECTURE) and the data behind it

Each block below is 1000 consecutive zeros. Per-zero verdicts are rigorous (Arb), and there were 0 undetermined verdicts in any block. The model columns are HEURISTIC.

| n0 | T range | failures/1000 | Var S(γ_n) | Var(S−δ) | corr(S,δ) | Gaussian model on S−δ | model with S independent of δ |
|---|---|---|---|---|---|---|---|
| 1 | 14–1419 | 80 | 0.067 | 0.032 | 0.89 | 0.079 | 0.186 |
| 10001 | 9.9e3–1.07e4 | 131 | 0.091 | 0.053 | 0.81 | 0.138 | 0.224 |
| 99001 | 7.4e4–7.5e4 | 167 | 0.101 | 0.063 | 0.78 | 0.160 | 0.238 |
| 1e6 | 6.0e5 | 193 | 0.112 | 0.073 | 0.74 | 0.181 | 0.252 |
| 1e7 | 5.0e6 | 194 | 0.120 | 0.081 | 0.72 | 0.194 | 0.261 |
| 1e8 | 4.3e7 | 209 | 0.128 | 0.089 | 0.70 | 0.207 | 0.271 |
| 1e9 | 3.7e8 | 227 | 0.135 | 0.095 | 0.69 | 0.215 | 0.278 |
| 1e10 | 3.3e9 | 224 | 0.139 | 0.101 | 0.67 | 0.224 | 0.283 |

The binomial standard error per block is about 0.013.

**Reading.**
- The failure rate is P(Y mod 2 ∈ (3/4, 7/4)) for Y = S(γ_n) − δ_n. A wrapped Gaussian with the empirical variance of Y reproduces every block to within about one standard error.
- Ignoring the strong positive correlation (0.67 to 0.89) between S(γ_n) and arg ζ(3/2+iγ_n) overestimates the rate by 5 to 11 points.
- Var(S − δ) grows at about 0.055 per unit of log log T from n0 = 10⁶ to 10¹⁰. This is close to Selberg's 1/(2π²) = 0.0507.

**Conjecture C3-ADJ-RATE.** #{n ≤ N : P_n < 0}/N → 1/2 as N → ∞.

**Heuristic basis.**
- A Selberg-type central limit theorem for S(γ_n) over zeros has variance (1/(2π²)) log log T → ∞.
- δ_n is bounded and depends mainly on small primes.
- So (S − δ) mod 2 should equidistribute, and the window has length 1 out of 2.

**Extrapolation (HEURISTIC).** Using Var(S − δ) ≈ 0.0507 log log T − 0.056 (Selberg's slope, anchored at the n0 = 10⁹ and 10¹⁰ blocks), the rate would reach 25% near T ≈ 10^14, 30% near T ≈ 10^34, and 40% near T ≈ 10^543.

**Proof status.** Not proved. Proving even infinitely many failures needs control of S at zeros, in the style of Trudgian's "Gram's law fails a positive proportion of the time" (Acta Arith. 148 (2011)). That is the natural next step (Sec. 9).

### 3.4 C3-ADJ-O2: where exactly Oliva's step (3) breaks (THEOREM, modulo IMPORTED Platt-Trudgian and Littlewood)

**Setup.**
- For a prime p ≥ 5, let N(p) = ∏_{q≤p} q, so that log N(p) = θ(p), and let p⁻ be the preceding prime.
- Oliva v1, eq. (3), with p_{n+1} = p, is (1 − e^{−γ}/LL₁ − 1/p)(1 − e^{−γ}/LL₀)^{−1} ≥ 1 − 1/p, where LL₁ = log log N(p) and LL₀ = log log N(p⁻).
- **(i) Algebra.** (3) is equivalent to (1 − 1/p) log log N(p) ≥ log log N(p⁻). The constant e^{−γ} and the counterexample hypothesis on A_n drop out. This was checked symbolically (sympy) and agrees with the skeptic.
- The equivalence needs 1 − e^{−γ}/LL₀ > 0, which holds for p ≥ 5 since N(p⁻) ≥ 6.
- Put H(L) := (1 − 1/p) log L − log(L − log p). Then (3) at p is H(θ(p)) ≥ 0.

**Lemma.**
- (a) H is strictly decreasing on (log p, ∞). Indeed H′(L) = −[L/p + (1 − 1/p) log p]/[L(L − log p)] < 0. This is also why substituting Dusart's lower bound for θ(p) makes (3) easier, so (3) implies (4) and Oliva's "(3) is weaker than (4)" reverses the direction.
- (b) H(p) > y²/2 > 0, where y = (log p)/p. This holds because −log(1−y) > y + y²/2.
- (c) For L ≥ p, H(L) ≤ y²/(2(1−y)) − (L − p)(1 + (1 − 1/p) log p)/L². This uses −log(1−y) ≤ y + y²/(2(1−y)) and the bound on H′.

**Theorem.**
- (A) If θ(p) ≤ p, then (3) holds at p. Hence (3) holds for every prime 5 ≤ p ≤ 1.39·10¹⁷, by Platt-Trudgian Thm 1: θ(x) < x for 0 < x ≤ 1.39·10¹⁷.
- (B) If p ≥ 100 and log p ≤ θ(p) − p, then (3) fails at p. Proof: Cor. 2 of Platt-Trudgian gives E := θ(p) − p < 7.5·10⁻⁷ p. Then (c) shows H(θ(p)) < 0 as soon as E > (log p)²(1 + 7.5·10⁻⁷)²/[2(1−y)(1 + (1 − 1/p) log p)], and the right-hand side is < 0.53 log p for p ≥ 100.
- (C) (3) fails at some prime p < exp(727.951332668). Proof:
  1. Platt-Trudgian Sec. 3.1.5 gives some u ∈ (727.951332642, 727.951332668) with θ(e^u) − e^u > 2.75·10⁻⁶ e^{u/2} > 10¹⁵².
  2. Let p be the largest prime ≤ x = e^u. Then θ(p) = θ(x) and p ≤ x, so θ(p) − p ≥ θ(x) − x > 10¹⁵² > log p.
  3. Apply (B).
  An Arb evaluation of the bound in (c) over the whole range log p ∈ [727.25, 727.951332668] gives p²·(upper bound for H) ∈ [−7.29·10¹⁵⁴ ± 7.5·10¹⁵¹].
- (D) (3) fails for infinitely many primes p. Proof: Littlewood's 1914 theorem, ψ(x) − x = Ω₊(x^{1/2} log log log x), together with θ(x) = ψ(x) − x^{1/2}(1 + o(1)), gives θ(x) − x > √x for arbitrarily large x. Oliva quotes this form himself (v1, p. 2, citing Ingham's book). Let p be the largest prime ≤ x, as in (C); then θ(p) − p > √x ≥ √p > log p, and apply (B).

**Consequence.** The least prime at which Oliva's induction step fails lies in (1.39·10¹⁷, e^{727.951332668}). The lemma is true for every prime up to 1.39·10¹⁷, and false. This is failure mode F5 in its purest form: a finite-to-infinite extrapolation, here hidden inside an "eventually" (F6).

### 3.5 Other complete statements (proofs in REPORT.md, re-derived by the skeptic and the adjudicator)

- **C3-A1.** Atiyah's 2.6, read as an identity of formal power series, forces h(w) = T(1+w) to be constant.
  - Proof: compare the coefficient of s^m in h(2s+s²) − h(2s); its top term is (m−1)2^{m−2}c_{m−1}. Induct on m.
- **C3-Q1.** Let f be analytic on D(ρ+v, v) with a pole at ρ. Then the Taylor series at ρ+v diverges at ρ. Hence Queme's termwise limit ε → 0 is illegitimate.
  - Model: for 1/(z−ρ), every term equals 1/v, while the value at ρ+ε is 1/ε.
- **C3-M1.** Hypotheses (C1)-(C5) of Micheas' Theorem 1 admit τ_n = t_n − 1/(2n). For that choice the product is nonzero at 1/2 + it_1, so it is not ξ.
  - Arb partial product at N = 10⁵: −0.0014185196...
- **C3-CG1.** The explicit counterexample to "1/(πθ) + 1" given in Sec. 2.
- **Davenport-Heilbronn.** Coefficients a(n) of period 5, (1, κ, −κ, −1, 0), with κ = (√(10−2√5) − 2)/(√5 − 1).
  - Functional equation: Λ(s) = (5/π)^{s/2}Γ((s+1)/2)f(s) = Λ(1−s).
  - Certified simple zero at Re s = 0.80851718245663738555..., Im s = 85.69934848537759217193...

---

## 4. Per-case dossiers (final form)

Each dossier gives the claim, the exact failing step or counterexample, the failure category (tags from Sec. 5), and whether anything is salvageable.

**D1. de Branges positivity (1986-1994), with Conrey-Li 2000.**
- Claim: (3.1) on H(E), E = ξ(1−iz), or (3.3) on F(1/ξ(1−iz)), implies RH via Thm 1 or Thm 2.
- Failing step: the hypotheses themselves are false. Witnesses: ρ₃₄; t = 282; χ₄. By C3-ADJ-S the zero condition fails exactly when S(γ_n) − δ_n ∈ (3/4, 7/4) mod 2: 15.6% of the first 10⁵ zeros.
- Tags: F4.
- Salvageable: the de Branges-space framework (Lagarias 2005). Not these conditions.

**D2. X.-J. Li 2008, arXiv:0807.0090 v1-v3.**
- Claim: RH, then Bombieri's refinement of Weil positivity.
- Failing steps: (6.9) on p. 20 (fixed in v2/v3); Thm 7.3 on p. 29, extending from ideles to adeles by 0, a measure-zero support (Connes, Tao); an invertibility on p. 18 that fails if there is an off-line zero (Tao). v4 withdrawn.
- Tags: F8, F3, F7.
- Salvageable: Li's criterion and the Weil/Connes target. The v5-v10 text was **not audited**.

**D3. Atiyah 2018.**
- Claim: T{(1+f)(1+g)} = T{1+f+g} and F = T{1+ζ(s+b)} − 1 give F = 2F, so ζ ≡ 0.
- Failing step: 2.6 forces T constant (C3-A1); "T invertible" fails; the argument never uses Re b ≠ 1/2.
- Tags: F9, F2, F1.
- Salvageable: none.

**D4. Bender-Brody-Mueller 2017.**
- Claim (conditional): H = (1−e^{−ip})^{−1}(xp+px)(1−e^{−ip}); ψ_z = −ζ(z, x+1); ψ(0) = 0 iff ζ(z) = 0.
- Failing step: the missing Hilbert space. p has no self-adjoint extension (indices (1,0)); ψ_z ∉ L² for Re z ≤ 3/2; weights move the real-eigenvalue line. The formal eigen-equation holds for every z.
- Tags: F7.
- Salvageable: heuristic only (Berry-Keating, PT symmetry).

**D5. Turan's partial-sum hypothesis.**
- Claim: ζ_N(s) ≠ 0 in σ > 1 for all large N would give RH.
- Failing step: the hypothesis is false. Spira 1968 (N = 19, ...); Montgomery 1983 (all large N); Platt-Trudgian (the exact exceptional set).
- Tags: F4.
- Salvageable: none as a route. Zeros of ζ_N remain an object of study.

**D6. Mertens 1897 (Stieltjes 1885).**
- Claim: \|M(x)\| < √x, which would give RH.
- Failing step: Odlyzko-te Riele 1985, non-constructive; the first counterexample is below exp(1.96·10¹⁹) (Kim-Nguyen 2025). Stieltjes' O(√x) is **open**.
- Tags: F5, F4.
- Salvageable: M(x) = O(x^{1/2+ε}) (equivalent to RH); lattice-reduction methods.

**D7. Polya 1919 and Turan's T(x).**
- Claim: L(x) ≤ 0 for x ≥ 2, or T(x) ≥ 0 for large x, would give RH.
- Failing step: Haselgrove 1958. Explicit counterexamples: 906150257, and 72,185,376,951,205.
- Tags: F5, F4.
- Salvageable: the Ingham-Haselgrove oscillation method.

**D8. Cramer's model.**
- Claim (heuristic): primes behave like independent events of probability 1/log n.
- Failing step: Maier 1985, Ω± in intervals of length (log x)^λ for every λ > 1. Banks-Ford-Tao: mod-p bias.
- Tags: F12.
- Salvageable: Granville's model and the Banks-Ford-Tao models.

**D9. Mollifier and proportion methods.**
- Claim (as sometimes misread): a large proportion means progress to RH.
- Failing step: proportion ≠ all. Even 100% allows o(N(T)) off-line zeros. The methods give lower bounds on the line and never exclude an off-line zero.
- Tags: F13.
- Salvageable: valid theory. The 2026 records come from a different mechanism.

**D10. Oliva 2018.**
- Claim: a counterexample to Nicolas' inequality at n propagates to n+1, which with Nicolas' dichotomy gives RH.
- Failing step: eq. (3). The direction is reversed ((3) ⇒ (4)); (3) holds for p ≤ 1.39·10¹⁷, fails below e^{727.95}, and fails infinitely often (C3-ADJ-O2). Given Nicolas' dichotomy, the propagation lemma is equivalent to RH. Author-withdrawn.
- Tags: F10, F6, F5, F3, F15.
- Salvageable: none for the route.

**D11. Queme 2020.**
- Claim: at a zero of maximal real part, ζ′/ζ(ρ+ε) ~ 1/ε contradicts a finite termwise limit.
- Failing step: item 6 on p. 4, a termwise limit at the boundary of the disc of convergence (C3-Q1). It proves too much, since it excludes ρ₁. Author-flagged.
- Tags: F6, F2.
- Salvageable: none. The v1 footnote inviting readers to find the error is exemplary practice.

**D12. Micheas 2026.**
- Claim: any τ_n within b_n → 0 of the ordinates gives a product equal to ξ, hence RH.
- Failing step: Theorem 1 is false (C3-M1). Product formulas take the zeros as input. Author-withdrawn.
- Tags: F11, F2.
- Salvageable: none.

**D13. Published explicit constants.**
- Claim: various explicit bounds.
- Failing step: corrections in print (Lehman; HPY; Ford v2-v5; PRZZ / Pratt-Robles; Pearce-Crump v2). C3-CG1 is an explicit witness for the Cheng-Graham lemma.
- Tags: F14.
- Salvageable: all were repaired. The constants changed little, except for the Cheng-Graham-dependent subconvex constants (0.63 → 0.77).

**D14. Davenport-Heilbronn.**
- Role: a countermodel, not a claim.
- Point: it has a functional equation of Riemann type, and a certified zero at Re = 0.8085.
- Tags: F1 (its test).
- Salvageable: it is the standard falsification test.

---

## 5. Failure-mode taxonomy (HEURISTIC; tags, not a partition; adjudicated)

| Code | Mechanism | Instances (verified) | Quick test |
|---|---|---|---|
| F1 | Uses only the functional equation, the Gamma factor, analytic continuation, or other properties shared with a countermodel | D3, D14 | Run the argument on Davenport-Heilbronn (zero 0.80852+85.69935i), on Epstein zeta, or on ζ_19 (zero with Re 1.00110) |
| F2 | The hypothesis "Re ρ ≠ 1/2" is never used, so the argument proves too much | D3, D11, D12 | Re-run at ρ₁ = 1/2+14.1347i, on 1/(z−ρ), and on a perturbed zero set |
| F3 | Circularity: a hidden RH-equivalent invertibility, positivity or propagation step | D2(c), D10 | Does each lemma survive one off-line pair? Is it equivalent to RH given known dichotomies (Nicolas, Robin)? |
| F4 | A sufficient condition that is (unconditionally) false | D1, D5, D6, D7 | Compare with Ingham-type and Conrey-Li-type obstructions. Find the S(t)- or arg ζ-phase form of the condition (C3-ADJ-S). |
| F5 | Finite-to-infinite extrapolation | D6, D7, D10 | Estimate the Skewes-type scale of the first failure. Example: Oliva's (3) is true up to 1.39·10¹⁷ and false below e^{728}. |
| F6 | A non-uniform limit: a limit/sum interchange at the boundary of convergence, or "eventually" applied in a moving parameter | D10(a), D11 | Name the theorem behind each interchange. Track every parameter in an "eventually". |
| F7 | A domain, self-adjointness or normalizability gap | D2(c), D4 | Name the Hilbert space, domain, closure and deficiency indices. Check the eigenvectors lie in the space. |
| F8 | Support of measure zero | D2(b) | Check the support of each extension by zero |
| F9 | An undefined or inconsistent new object | D3 | Exhibit a model of the stated axioms (C3-A1) |
| F10 | An inequality direction or sign error in a criterion | D10(a) | Compute the monotonicity of the target in each substituted bound |
| F11 | Factorization-only arguments (Hadamard/Weierstrass) | D12 | Perturb the zero set |
| F12 | A heuristic model treated as a law | D8 | Check against Ω-theorems (Maier) |
| F13 | A density or proportion read as "all zeros" | D9 | Proportion 1 − o(1) ≠ RH |
| F14 | Bookkeeping errors in explicit constants | D13 | Re-derive imported lemmas; test them on extremal examples (Kusmin-Landau cot(πθ/2)) |
| F15 | The same method yields opposite conclusions in successive versions | D10 only | If a revision reverses the conclusion, the method does not discriminate. **A version count alone is not a failure mode.** |

---

## 6. One-page checklist for a proposed RH proof (human or AI) (HEURISTIC; adjudicated)

1. **State the target exactly.** Is it RH, a cited equivalent (with its normalization), or a sufficient condition? If it is a sufficient condition, is it known to be false (F4; Conrey-Li, Haselgrove, Odlyzko-te Riele, Montgomery)?
2. **Countermodel test (F1).** Does every step also hold for Davenport-Heilbronn (zero 0.80851718+85.69934848i), for Epstein zeta, or for ζ_19 (zero with Re = 1.0010955)? If so, the argument is invalid.
3. **Locate where Re ρ ≠ 1/2 is used (F2).** Re-run the argument at ρ₁ = 1/2+14.1347i and on 1/(z−ρ).
4. **Test every invertibility, positivity, density or propagation lemma against one off-line pair (F3).** Is the lemma equivalent to RH via a known dichotomy (e.g. Nicolas)?
5. **Write all quantifiers (F6).** "Fixed b, eventually in x" is not "b ~ x".
6. **Name the theorem behind every limit/sum/integral interchange (F6).** Never evaluate a series at the boundary of its disc of convergence.
7. **Compute the monotonicity of the target in every substituted bound (F10).**
8. **Name the Hilbert space, measure, domain, closure and deficiency indices (F7, F8).** Check that eigenvectors and test functions lie in it, and that supports have positive measure.
9. **Exhibit a model of every new object's axioms (F9).**
10. **If only the Hadamard product and the functional equation are used, the zeros are free parameters (F11).**
11. **Point to the exact step that uses the Euler product in a way Davenport-Heilbronn fails.**
12. **A proportion, even 1 − o(1), is not RH (F13).**
13. **No finite computation proves an infinite statement (F5).** Estimate the scale of a possible first failure. Precedents:
    - Mertens: Hurst 2018 reports \|M(x)\|/√x ≤ 0.571 for x ≤ 10¹⁶ away from small x. The extreme is M(7766842813) = 50286, q = 0.5706. The maximum over 200 ≤ x ≤ 10⁹ is 0.5657. Yet limsup > 1.826.
    - Polya: true up to 906150256.
    - Turan's T: true up to 7.2·10¹³.
    - Oliva's (3): true for all p ≤ 1.39·10¹⁷.
14. **Re-derive imported explicit lemmas with sharp constants (F14)**, and test them on extremal examples (Kusmin-Landau: cot(πθ/2), not 1/(πθ) + 1).
15. **Label every number** as a certified ball, an exact integer, or floating point. High precision is not certification.
16. **Random-model and RMT predictions are not evidence about individual zeros (F12).** Check them against Ω-theorems (Maier).
17. **If a revision reverses the conclusion, the method does not discriminate (F15).**
18. **Does the argument apply to a family that contains a member with known off-line zeros?**
19. **Search arXiv and zbMATH for published obstructions:** Conrey-Li, Montgomery, Odlyzko-te Riele, Haselgrove, Maier, Farmer arXiv:2008.07206.
20. **Pre-register the smallest statement whose failure kills the argument** (cf. Queme's v1 footnote).

---

## 7. Negative results and withdrawn statements

- **Withdrawn (investigator, C3-D1-scan):** "phase-locking has no arithmetic reason to hold". The condition is exactly a condition on S(γ_n) mod 2 (C3-ADJ-S).
- **Refuted premises of the campaign brief, which stay corrected:**
  - Stieltjes' M(x) = O(√x) is not refuted; it is open.
  - BBM is a conditional programme, not a proof claim.
  - arXiv:0807.0090 is "withdrawn" only for its 2008 text; v5-v10 (2024-2025) are a separate, unaudited claim.
  - Turan's hypothesis was contradicted numerically by Spira (1968) before Montgomery (1983).
- **Corrected sentences:**
  - "strictly stronger than RH" (D1);
  - Tao's timestamp (D2);
  - "companion paper not found" (D3): Atiyah-Kouneiher 2019 exists, content unaudited;
  - Bellissard's shift wording (D4);
  - ceiling items 1 and 3 (D9);
  - F15 examples (TAX);
  - checklist item 13.
- **Model failure (adjudicator).** A Gaussian model for S(γ_n) that treats it as independent of arg ζ(3/2+iγ_n) overestimates the de Branges failure rate by 5 to 11 points in every block. The correlation, 0.67 to 0.89, must be kept.
- **Not proved (open):**
  - infinitely many failures of the de Branges zero condition;
  - an effective first failure of Mertens (only an upper bound, exp(1.96·10¹⁹));
  - any statement about Li's v5-v10;
  - any statement about de Branges' post-2004 manuscripts.
- **Process artefacts recorded by the earlier agents (kept as negative knowledge):**
  - The float64 bound for T(x) was inadequate and was replaced by an exact certificate.
  - A float64 finite difference in Oliva's Lemma 2.2 was replaced by 60-digit mpmath and an analytic f′.
  - The skeptic's own "mechanism_identity_failures: 2000" was a tolerance artefact.
  - The skeptic's mpmath Hurwitz evaluation ran out of memory at a = 10¹⁰.
  - A first adjudicator run printed an Arb ball "[± 3.15e−477]" for the unscaled Oliva bound. It was rescaled by p² to [−7.29e154 ± 7.5e151] before being used.

---

## 8. Reproducibility

Versions: Python 3.13.18, python-flint 0.9.0, mpmath 1.3.0, numpy 2.5.3, sympy 1.14.0. Each run used at most 2 cores, with `nice -n 10`.

Run from `research/exploratory/riemann-observatory/experiments`, with `D=<scratchpad>/data` holding the certified zero TSVs.

```bash
# investigator (see results/C3-failure-anatomy/manifest_C3.json for hashes)
python3 code/C3-failure-anatomy/liouville_mertens_sieve.py 1000000000 22 results/C3-failure-anatomy/liouville_mertens_1e9.json   # 153 s
python3 code/C3-failure-anatomy/conrey_li_debranges.py 2000 results/C3-failure-anatomy/conrey_li_debranges.json                  # 16 s
python3 code/C3-failure-anatomy/witnesses.py $D/zeros_1_50000.tsv,$D/zeros_50001_100000.tsv results/C3-failure-anatomy/witnesses.json  # 193 s
# skeptic: see SKEPTIC_REVIEW.md Sec. 1 (scripts in code/C3-failure-anatomy/skeptic/)
# adjudicator
python3 code/C3-failure-anatomy/adjudicator/adj_debranges_S.py 100000 20000 $D/zeros_1_50000.tsv,$D/zeros_50001_100000.tsv \
        results/C3-failure-anatomy/adjudicator/adj_debranges_S_K100000.json                                    # 261 s
python3 code/C3-failure-anatomy/adjudicator/adj_debranges_highblocks.py 1000 \
        1,10001,99001,1000000,10000000,100000000,1000000000,10000000000 $D/zeros_1_50000.tsv,$D/zeros_50001_100000.tsv \
        results/C3-failure-anatomy/adjudicator/adj_debranges_highblocks.json                                    # 372 s (1e10 block: 197 s)
python3 code/C3-failure-anatomy/adjudicator/adj_mertens_point.py 2e7 1000000000,7766842813,10000000000 \
        results/C3-failure-anatomy/adjudicator/adj_mertens_point.json                                           # 3 s
python3 code/C3-failure-anatomy/adjudicator/adj_misc_checks.py $D/zeros_1_50000.tsv \
        results/C3-failure-anatomy/adjudicator/adj_misc_checks.json                                             # 1 s
```

SHA-256 of the adjudicator code and outputs is in `results/C3-failure-anatomy/adjudicator/manifest_adjudicator.json`.
- The sha256 of the comma-joined list of the 15567 failing indices (n ≤ 10⁵) is `d8dfc93cbb3c2bbaa063ad57d960e778cdbb414dee1b6776738c840ec77ef65c`.
- Recomputing it is the cheapest end-to-end check of C3-ADJ-S.

---

## 9. Next precise steps for a researcher

1. **Infinitely many / positive proportion of de Branges zero-condition failures.** By C3-ADJ-S, it suffices to show that S(γ_n) − δ_n ∈ (3/4, 7/4) mod 2 for infinitely many n, or for a positive proportion of n.
   - A positive-proportion route: adapt Trudgian's proof that Gram's law fails a positive proportion of the time (Acta Arith. 148 (2011)) from Gram points to zeros. Use Selberg's moments of S(t) and its shifted differences, plus the boundedness of δ.
   - Unconditionally, it may be easier to show the window (−0.93, −0.57) is hit infinitely often, using large negative values of S.
2. **Prove or refute C3-ADJ-RATE.** This needs a joint CLT for (S(γ_n), arg ζ(3/2+iγ_n)) over zeros, together with equidistribution of S(γ_n) − δ_n mod 2 at unit scale, not only at scale √(log log T).
   - A cheaper test: blocks near n = 10¹¹ and 10¹² with acb.zeta_zeros. These are about 50 s per 100 zeros at 10¹¹. The prediction is ≈ 0.23 and ≈ 0.24.
3. **Theorem 2 analogue.** Show, in the same way, that Re{ξ(1+it)/ξ(2+it)} < 0 if and only if −π/4 + arg ζ(1+it) − arg ζ(2+it) + O(1/t) lies outside [−π/2, π/2] mod 2π.
   - This puts Sarnak's density argument and the grid set {282, 527.25, ...} in one explicit criterion.
   - Not done here.
4. **Oliva (3).** Narrow the window (1.39·10¹⁷, e^{727.95}) for the first failure. Any x with θ(x) − x > (0.53 + o(1)) log x gives a failure at the largest prime ≤ x.
   - The first sign change of θ(x) − x is expected well below e^{728}. Büthe-type analytic methods could lower the upper end.
5. **Audit arXiv:0807.0090 v5-v10.** It is a live unrefereed claim. Apply checklist items 3, 4 and 8: off-line-pair test, positivity circularity, and trace-class domain.
6. **Audit de Branges' post-2004 manuscripts.** Determine whether they rely on conditions of the (3.1)/(3.3) type.
7. **Upgrade the L0/L0+ primary texts listed in the header to L1**, especially Montgomery 1983 and Odlyzko-te Riele 1985.
8. **Mechanize tests F1, F2 and F11.** Run a candidate argument symbolically on a parameterized family that contains Davenport-Heilbronn-type members, or on perturbed zero sets, as a pre-review filter for proof attempts.
