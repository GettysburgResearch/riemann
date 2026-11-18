# Verified findings

```text
Status: AUDIT FINDINGS (Level 2/3, adjudicated where flagged)
Scope: specific claims named per finding; not whole-paper verdicts
Exact sources or dependencies: per finding (evidence path)
What was actually run: independent auditor and adjudicator agents with recomputation (Arb/mpmath/exact arithmetic) where stated
Smallest remaining gap: human expert confirmation; Lean replays not performed
```

Rules applied (methodology §6): an error is reported only with an explicit, independently reproduced witness; published corrections by authors or third parties are reported as such; findings about AI-generated or unrefereed manuscripts are labelled. **No finding below affects a main theorem unless the text says so.** Each item links to its full audit record.

| ID | Subject | Classification | Main theorem affected? |
|---|---|---|---|
| FND-0001 | Yakaboylu, "Hamiltonian for the Hilbert-Pólya Conjecture", arXiv:2309.00405 (v6), J. Phys. A 57 (2024) 235204 | `verified_error` | The paper's Stage-II claim (it does not claim RH) |
| FND-0002 | Farmer, "Jensen polynomials are not a plausible route to proving the Riemann Hypothesis", Adv. Math. 411 (2022 | `verified_error` | No (qualitative conclusion unaffected) |
| FND-0003 | Bellotti-Trudgian-Yang, "Zero-free regions inspired by work of Heath-Brown", arXiv:2603.21490v1 (2026 preprint | `verified_error (localized, not load-bearing)` | No (4.896 reproduced) |
| FND-0004 | Alpöge-Furman, "More than two thirds of the zeta zeros are simple and on the critical line", arXiv:2608.13637v | `verified_error (proof step), repaired_minor` | No (repaired) |
| FND-0006 | Connes, "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function", Selecta Math. 5 | `correct_but_misinterpreted` | — |
| FND-0007 | Andrade-Keating, "Conjectures for the integral moments and ratios of L-functions over function fields", J. Num | `correct_but_misinterpreted` | — |
| FND-0008 | Ng-Shen-Wong, "The eighth moment of the Riemann zeta function", J. Eur. Math. Soc. 28 (2026); arXiv:2204.13891 | `correct_but_misinterpreted (by the Observatory reader); minor citation-range mismatch` | No |
| FND-0009 | OpenAI, "The Quasi-Riemann Hypothesis" (11/12 companion), 5 Oct 2026; github.com/openai/math@4eaee875, paper2. | `no_issue_found_in_inspected_portion` | No issue found |
| FND-0010 | Landau-Siegel exclusion: OpenAI (1 Oct 2026); Banks arXiv:2610.15483; Kerr arXiv:2610.21099; Guo arXiv:2610.30 | `no_issue_found_in_inspected_portion (with one unresolved formal-verification ambiguity)` | No issue found |
| FND-0012 | Cheng-Graham, explicit estimates (Lemma 2: |sum e(f(n))| <= 1/(pi theta) + 1) | `verified_error (already corrected in print)` | Already corrected in print |
| FND-0013 | Conrey-Li (IMRN 2000) de Branges necessary zero condition | `valid_with_stronger_consequences` | Strengthens a known negative result |
| FND-0014 | Withdrawn/claimed RH proofs: Atiyah 2018; Micheas arXiv:2607.04338 v1; Queme arXiv:2004.00460; Oliva arXiv:180 | `verified_error (in claims already withdrawn or not accepted)` | Claims already withdrawn/not accepted |

## FND-0001 — Yakaboylu, "Hamiltonian for the Hilbert-Pólya Conjecture", arXiv:2309.00405 (v6), J. Phys. A 57 (2024) 235204

*Location:* Sec. II, Eqs. (12)-(18) · *Classification:* `verified_error` · *Public characterization allowed:* True

The claimed existence of a similarity transformation making the Hamiltonian self-adjoint on a domain fixed by a zeta-zero boundary condition fails: the weight (18) defines an indefinite form (explicit vector with <U|U> = -0.0231), and the boundary condition (17) admits spurious solutions where zeta(s) != 0 (e.g. s = 1/2 + 3.70362i). The paper itself states its argument is formal and does not claim a proof of RH.

*Witness / evidence type:* Explicit numerical witnesses; independent two-sided adjudication

*Full record:* `audits/L2_flag_audits/F1-yakaboylu.md`


## FND-0002 — Farmer, "Jensen polynomials are not a plausible route to proving the Riemann Hypothesis", Adv. Math. 411 (2022) 108781; arXiv:2008.07206

*Location:* Sec. 4.2, Table 4.1 and the sentence on X_10 · *Classification:* `verified_error` · *Public characterization allowed:* True

Table 4.1 thresholds do not match the configuration described in the text (printed j=20 threshold corresponds to moving 9pi/2, 11pi/2, not the two zeros closest to 20, whose threshold is 478; j=10: certified 120 vs printed 119). The paper's qualitative conclusion is not affected.

*Witness / evidence type:* Arb-certified exact Jensen-polynomial root counts (campaign C1) independently recomputed by the L2 auditor and adjudicator

*Full record:* `audits/L2_flag_audits/F6-farmer-table.md; proposals/independent_campaigns/C1-detection-horizons/`


## FND-0003 — Bellotti-Trudgian-Yang, "Zero-free regions inspired by work of Heath-Brown", arXiv:2603.21490v1 (2026 preprint)

*Location:* Table 1, entry m_5 · *Classification:* `verified_error (localized, not load-bearing)` · *Public characterization allowed:* True

m_5 = 0.00735709 is not a lower bound for min_x G_5(1,x) with the paper's stated rational polynomial (certified minimum in (0.0073564918, 0.0073564919)); entries appear computed from Mossinghoff-Trudgian's floating-point F16. With the corrected entry sum (log p) m_p = 0.2354513 > 0.23545, so Theorem 1 and the constant 4.896 are unaffected. The Observatory independently reproduced the 4.896 chain (eta log t > 0.2042602). Separately, Lemma 4's constant c0 is mis-transcribed from Ford (typo; later numbers use the correct value).

*Witness / evidence type:* Arb ball evaluations, exact rational evaluation, root isolation; independent adjudication. Allowed public wording: a localized table entry invalid for the stated polynomial, with a corrected value preserving the theorem. Never an error in the 4.896 region.

*Full record:* `audits/L2_flag_audits/F7-bty-constant.md`


## FND-0004 — Alpöge-Furman, "More than two thirds of the zeta zeros are simple and on the critical line", arXiv:2608.13637v2 (2026 preprint)

*Location:* proof of Prop. 4.2 (LaTeX l.327, PDF p.6) · *Classification:* `verified_error (proof step), repaired_minor` · *Public characterization allowed:* True

The proof applies a distance bound |Re gamma_rho - alpha_k| >= D_rho to zeros with Re gamma_rho in I'\I, where it is false (explicit witnesses on actual zeta zeros). A short repair using one-sided decay (the estimate the authors use in Props 4.3 and 5.2) restores tr G = N(I') + O(sqrt T log T), within the stated error; Prop. 4.2, the Section 6 chain and Theorems A and B are unaffected.

*Witness / evidence type:* Numerical witnesses at T up to 3e4 with two cut-offs; independent adjudication

*Full record:* `audits/claims_2026/CRIT23/`


## FND-0006 — Connes, "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function", Selecta Math. 5 (1999); arXiv:math/9811068

*Location:* Theorem 5 vs abstract/introduction · *Classification:* `correct_but_misinterpreted` · *Public characterization allowed:* True

Theorem 5 (equivalence of the global trace formula with RH for Hecke L-functions) is proved for global fields of positive characteristic; for number fields the paper reduces RH to a trace-formula/positivity statement that is not proved. Citations attributing a proved number-field result misread the paper.

*Witness / evidence type:* Text of Sec. VIII; citation survey

*Full record:* `audits/L2_flag_audits/F5-connes-thm5.md`


## FND-0007 — Andrade-Keating, "Conjectures for the integral moments and ratios of L-functions over function fields", J. Number Theory 142 (2014); arXiv:1407.3099

*Location:* Theorem 1 (Sec. 5.4), Sec. 5.3 · *Classification:* `correct_but_misinterpreted` · *Public characterization allowed:* True

Theorem 1 and Sec. 5.3 rest on Conjecture 5; later citations should carry the conditionality.

*Witness / evidence type:* Text check; citation check

*Full record:* `audits/L2_flag_audits/F4-andrade-keating.md`


## FND-0008 — Ng-Shen-Wong, "The eighth moment of the Riemann zeta function", J. Eur. Math. Soc. 28 (2026); arXiv:2204.13891

*Location:* Prop. 3.1 / import of Thm 1.2 of "Shifted moments" · *Classification:* `correct_but_misinterpreted (by the Observatory reader); minor citation-range mismatch` · *Public characterization allowed:* True

All hypotheses of the imported theorem hold where used (k = 4). The Observatory Level-1 reader's "k >= 12" was a pdftotext artifact (\frac{1}{2} rendered as "12"). Minor: the paper quotes the imported range as k >= 1/2 whereas the companion proves k >= 1; immaterial at k = 4. Theorem 1.1 is conditional on RH and a quaternary additive divisor conjecture.

*Witness / evidence type:* LaTeX source check

*Full record:* `audits/L2_flag_audits/F2-ng-eighth.md`


## FND-0009 — OpenAI, "The Quasi-Riemann Hypothesis" (11/12 companion), 5 Oct 2026; github.com/openai/math@4eaee875, paper2.pdf sha256 f919b578...

*Location:* Sections 3-7, Appendices A-B, Outline · *Classification:* `no_issue_found_in_inspected_portion` · *Public characterization allowed:* True

Section-by-section Level-2 audit by seven auditor agents found no mathematical error; about one hundred numerical checks of the arithmetic identities (sextic/cubic residue symbols, Gauss sums, reciprocity, Gauss-Jacobi relations, cubic-theta transformation data) were confirmed in Z[omega]. Only presentational issues were found. Imported inputs (Patterson/Kubota cubic theta, Dunn-Radziwill cusp expansions, large-sieve inputs) were checked against their statements but not re-proved. This is not a refereeing verdict.

*Witness / evidence type:* Audit reports and numeric checks

*Full record:* `audits/quasi_rh/`


## FND-0010 — Landau-Siegel exclusion: OpenAI (1 Oct 2026); Banks arXiv:2610.15483; Kerr arXiv:2610.21099; Guo arXiv:2610.30476

*Location:* as in dossier · *Classification:* `no_issue_found_in_inspected_portion (with one unresolved formal-verification ambiguity)` · *Public characterization allowed:* True

Flagged items were adjudicated not_an_issue (Banks's quoted prime-sum inequalities re-proved independently with ball arithmetic; the all-q constant 3.0e-3 openly depends on the unreplayed Lu-Zaman-Zhao computation, as Banks discloses). The Lean formalization was not replayed (31/31 static checks passed; a third party reports a kernel replay with nanoda).

*Witness / evidence type:* Adjudications U2-U4

*Full record:* `audits/claims_2026/SIEGEL/`


## FND-0012 — Cheng-Graham, explicit estimates (Lemma 2: |sum e(f(n))| <= 1/(pi theta) + 1)

*Location:* Lemma 2 · *Classification:* `verified_error (already corrected in print)` · *Public characterization allowed:* True

Lemma 2 as stated is false; the correction (1/pi -> 2/pi) was already published by Hiary-Patel-Yang (2022) and noted by Ford. The Observatory adds an explicit smooth certified instance (theta = 0.02, |S| = 31.5980... > 16.9155).

*Witness / evidence type:* Arb certificate, reproduced in mpmath and long double

*Full record:* `proposals/independent_campaigns/C3-failure-anatomy/`


## FND-0013 — Conrey-Li (IMRN 2000) de Branges necessary zero condition

*Location:* Thm 1-2 consequences · *Classification:* `valid_with_stronger_consequences` · *Public characterization allowed:* True

The necessary condition -Re{xi'(rho_n) xi(1+rho_n)} >= 0 fails frequently, not only at Conrey-Li's witness: 195/2000, 2724/20000 and 15567/100000 zeros (three independent Arb implementations), with failure rates in 1000-zero blocks rising from 8% to 22.4% up to n = 1e10. New exact identity (campaign C3 adjudication): the condition at the n-th zero holds iff S(gamma_n) - delta_n lies outside (3/4, 7/4) mod 2, with delta_n a bounded phase term.

*Witness / evidence type:* Arb counts; identity proof in C3 FINAL

*Full record:* `proposals/independent_campaigns/C3-failure-anatomy/FINAL.md`


## FND-0014 — Withdrawn/claimed RH proofs: Atiyah 2018; Micheas arXiv:2607.04338 v1; Queme arXiv:2004.00460; Oliva arXiv:1807.06447

*Location:* as in dossiers · *Classification:* `verified_error (in claims already withdrawn or not accepted)` · *Public characterization allowed:* True

Exact failing steps reconstructed with short proofs or explicit counterexamples (e.g. Atiyah's property 2.6 forces T constant; Micheas' Theorem 1 is false independently of RH). All are already withdrawn, self-flagged, or publicly critiqued; the Observatory adds precise mechanisms for the failure-mode taxonomy.

*Witness / evidence type:* Theorems C3-A1, C3-M1, C3-Q1

*Full record:* `proposals/independent_campaigns/C3-failure-anatomy/`

