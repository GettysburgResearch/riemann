# Strongest connections: ranked, verified, corrected

```text
Status: SYNTHESIS (exploration layer, Riemann Observatory). A ranked digest of the connection proposals that
        survived independent verification, each stated in its corrected form. It is not a review approval and
        not an integrated packet. RH is open, and no item below proves or disproves it.
Scope: the 39 proposals CON-0001..CON-0039 (verdicts: 9 sound_and_useful, 10 sound_but_known,
       19 needs_correction, 1 vocabulary_only, 0 incompatible_hypotheses, 0 false); the strongest confirmed
       mappings of the repository bridge (215 BRG items: 79 confirmed, 74 confirmed_with_correction,
       12 relation_overstated, 50 not individually graded); negative knowledge.
Exact sources or dependencies: connections/connections.jsonl and connections_register.md (proposal fields,
       verifier reasoning, corrections, prior art); connections/repository_bridge.jsonl and .md;
       audits/verified_findings.md and unresolved_findings.md (FND ids); audits/quasi_rh/DOSSIER.md (incl. Sec. 4);
       audits/claims_2026/CRIT23/DOSSIER.md and SIEGEL/DOSSIER.md; frontiers/ledger.jsonl and records_ledger.md
       (LED ids); frontiers/research_programs.md; proposals/independent_campaigns/C1..C5 (REPORT.md with
       SKEPTIC_REVIEW.md; C3 FINAL.md); history/recent_developments_2024_2026.md and abandoned_approaches.md;
       corpus/bibliography.jsonl (PAPER ids).
What was actually run: I read the files above, and ran short Python scripts to tabulate verdicts and relations
       and to look up PAPER ids in the jsonl files. I did no new mathematics and recomputed nothing. Every number
       is quoted from a proposer record as confirmed or corrected by its verifier or skeptic.
Smallest remaining gap: no item has had human expert review. The top-ranked unconditional item (CON-0032, T1)
       rests on an arXiv construction (Broucke-Debruyne-Revesz Thm 1.3) whose journal status was not verified.
       Every QRH-dependent item inherits the unrefereed status of the 2026 half-plane claims.
```

## 0. Reading rules

**Status labels.** Every mathematical statement carries one of these labels:
- [theorem]: published or classical;
- [theorem, unrefereed]: a preprint;
- [AI-generated, unrefereed];
- [Observatory-proposed]: first written in this archive by a proposer agent; the verifier's re-derivation is noted;
- [conditional on X];
- [heuristic];
- [conjecture];
- [numerical, non-rigorous];
- [computed, exact]: integer or rational arithmetic.

**2026 inputs.** These names are used throughout.
- **QRH-11/12.** Claim: ζ and all Dirichlet L-functions have no zeros in Re s > 11/12 (OpenAI paper2, PAPER-0161; LED-ZFR-2). Status: AI-generated, unrefereed. The Observatory's Level-2 section audit found no error in the inspected portions (FND-0009). The imported metaplectic and large-sieve inputs were not re-proved.
- **QRH-7/8.** Claim: the same with Re s > 7/8 (PAPER-0528; LED-ZFR-1). Status: AI-generated, unrefereed, 199 pp.; **not audited by us**. A Lean formalization is claimed but was **not replayed** (unresolved_findings).
- **Sub-7/8 refinements.** Liu PAPER-0156/0157, Xu–Sang PAPER-0158, Chang–Wang, Newton (LED-ZFR-3). Unrefereed; they import the 7/8 inputs.
- **CRIT-2/3.** Claim: liminf N₀ˢ/N ≥ 2/3, and ≥ C_MT = 0.6725007 with the Montgomery–Taylor window. Proofs: Alpöge–Furman PAPER-0486 (argument discovered and written by Claude, verified by the human authors) and Lamzouri PAPER-0533 (independent human proof). Unrefereed. The CRIT23 audit found no error affecting any stated result, and one local proof-step error, which was repaired (FND-0004). Lean was not replayed (LED-CRIT-1, -2).
  - Knausgård's refinements (PAPER-0166: 0.67353820; distinct 0.83900460; simple-anywhere 0.67800919) are unrefereed and depend on unreplayed computer searches (LED-CRIT-3).
- **SIEGEL.** Claim: (1−β) log q ≥ c for every real zero. Sources: OpenAI PAPER-0529 (AI-generated); Banks PAPER-0160, Kerr PAPER-0164, Guo PAPER-0165 and Kimura arXiv:2610.21511 (human-signed, AI-assisted). Unrefereed. FND-0010 found no issue in the inspected portions; LED-LFUN-6.

**Ranking rule.** Section 2 ranks the 28 new items: the sound_and_useful items plus the needs_correction items **after** their corrections. The ranking criteria are, in order:
1. Strength of what is actually established, in decreasing order: an unconditional proof; a proof conditional on refereed inputs; a proof conditional on unrefereed 2026 claims; an exact computation; numerics; a conjecture.
2. Leverage on an RH-relevant obstacle.
3. The proposer's significance score, as moderated by the verifier.

Section 3 ranks the 10 confirmed prior-art (sound_but_known) items separately. Significance and difficulty are the proposer's scores (scale up to 7), unchanged unless stated.

## 1. Ranked summary

| Rank | ID | Verdict | Corrected claim (short) | Strongest established content | Needs unrefereed 2026 input? |
|---|---|---|---|---|---|
| 1 | CON-0032 | sound_and_useful | Euler product plus integer regularity N = ax + O(x^{β+ε}) cannot imply RH for any β > 2/5; the region β < 1/2, Θ ≥ 2/3 has no known countermodel | unconditional, non-constructive theorem, given BDR Thm 1.3 (arXiv) | no (QRH only in the frontier map) |
| 2 | CON-0021 | sound_and_useful | Nyman–Beurling/Hardy-space error decays exactly like n^{−2(α−Θ)} | Observatory-proposed proposition; verifier re-derived both directions | no (the 7/8 corollary only) |
| 3 | CON-0006 | needs_correction | unconditional inequality N* ≥ S₁²/(S₂ + D/2); a near-line hypothesis gives 19/27 | inequality and conditional theorem re-derived | no |
| 4 | CON-0025 | sound_and_useful | exponent-2 class groups are exactly the 65 known fields; idoneal list complete without QRH | exact scan replayed independently | SIEGEL (Kimura constant), not QRH |
| 5 | CON-0038 | sound_and_useful | Ji's Q(i) route has a floor ≥ 0.9898 for every density input; an independent 11/12 needs a quartic row mean square | computed floor of a transcribed inequality system, analytically re-derived | no (a statement about Ji's system) |
| 6 | CON-0030 | needs_correction | density-type zero inputs are blind to o(T) off-line zeros | elementary lemma (formalised folklore) | no |
| 7 | CON-0035, CON-0011 | needs_correction | individual GL(2): no simple zeros from bandwidth-1/2 windows (λ* = 0.5502); distinct-zero target 0.4617 | (A) elementary; (B) conditional on an unported GL(2) pair-sum asymptotic | CRIT-2/3 machinery (to be ported) |
| 8 | CON-0036, CON-0012 | needs_correction | GL(2) harmonic family averages ≥ 0.6725 simple-critical, ≥ 0.8363 distinct (plan); Weil-only fallback 0.4191 / 0.7095 | plan plus a standard off-diagonal bound | Hua–Yang template (unrefereed) |
| 9 | CON-0008 | sound_and_useful | an off-line zero at 1/2 + δ + iγ forces Λ ≥ cδ²/log²γ | proof sketch with two gaps | no |
| 10 | CON-0017 | needs_correction | QRH(θ) for small twists gives Pólya–Vinogradov at Montgomery–Vaughan strength, for every θ < 1 | outline (MV route) | QRH |
| 11 | CON-0018 | sound_and_useful | QRH(θ) gives α_k ≤ θ − C(θ)/k; at 7/8 this beats the records for k = 14..21 | conditional implication re-derived | QRH-7/8 |
| 12 | CON-0019 | sound_and_useful | QRH-7/8 lowers the Gafni–Tao μ(θ) only on (0.2445, 5/12) | conditional computation reproduced | QRH-7/8 |
| 13 | CON-0015 | sound_and_useful | the ξ′ window class tops out at 0.868642, below Wu's 0.86957 | floating-point global optimum | AF Rem. 7.1 (AI-generated) |
| 14 | CON-0024 | sound_and_useful | Λ for Pólya's ξ* as an arithmetic-free control; empirically Λ* ≤ −4 | empirical | no |
| 15 | CON-0007 | needs_correction | graded criteria (Suzuki, Beurling, Dimitrov–Oliveira) at ω = 3/8 under 7/8 | immediate corollaries | QRH-7/8 |
| 16 | CON-0020 | needs_correction | Artin from quasi-GRH: thresholds 0.656 (elementary), 0.796 (Nongkynrih, a = 2); 7/8 is insufficient | corrected elementary bound | — |
| 17 | CON-0033 | needs_correction | infinite log-concavity of λ_n (only) cannot imply RH if a heat-flow conjecture holds | (a) classical lemma; (c) conjecture | no |
| 18 | CON-0031 | needs_correction | extraction bookkeeping; proven mollified moments give no half-plane | known corollary plus heuristic | no |
| 19 | CON-0014 | needs_correction | order-r extraction ceiling 1 − 1/(2r); the order-2 mean square is strictly stronger than its conclusion | elementary plus corrected equivalence | QRH architecture |
| 20 | CON-0037 | needs_correction | Conjecture G: quasi-RH for infinite-order Hecke characters of Q(√−3) | conjecture; algebra checked | paper2 machinery |
| 21 | CON-0003 | needs_correction | Robin range estimate: log n up to about 4–5·10^22 unconditionally; about 1.5·10^30 under QRH-7/8 | pre-proof estimate | partly |
| 22 | CON-0002 | needs_correction | explicit ranges for the Nicolas and Johnston criteria from partial RH | pre-proof estimates | partly |
| 23 | CON-0004 | needs_correction | non-Robin counting under H_Θ; φ-relaxation floor exp((log x)^{3/4}) | sketch plus corrected floor | partly |
| 24 | CON-0005 | needs_correction | Gorodetsky substitution: Ψ ~ xρK for y ≥ (log x)^{8+ε} under 7/8 | substitution into a refereed parametric theorem | QRH-7/8 |
| 25 | CON-0010 | needs_correction | route-by-route missing-lemma ledger (corrected labels) | organisational | — |
| 26 | CON-0026 | needs_correction | Cureton–Thorner v1/v2 provenance and consumer scope | provenance | — |

Confirmed prior art (Section 3), in order: CON-0039, CON-0016 with CON-0001, CON-0034, CON-0027, CON-0013, CON-0023, CON-0028, CON-0009, CON-0029.

## 2. New connections: full entries (ranked)

Each entry gives, in order:
- the sources;
- the link between them;
- the compatibility checks the verifier made;
- the claim in corrected form;
- what is proved and what is conjectural;
- the next step, counterexamples and tests;
- significance and difficulty.

### Rank 1: CON-0032 (sound_and_useful; M7; sig 6, diff 3)
**Beurling frontier.** Euler product plus integer regularity cannot give RH for β > 2/5, unconditionally. The region β < 1/2, Θ ≥ 2/3, which contains 7/8 and 11/12, has no known countermodel.
- **Sources.**
  - Broucke–Debruyne–Révész (BDR), arXiv:2309.01567v2 [theorem, unrefereed arXiv; journal status not verified]:
    - Thm 1.1: for every α ∈ [0,1) and β ∈ [1/2,1) an [α,β]-system exists;
    - Thm 1.3: assuming RH, systems exist for 1/2 < α < 2/3 and 2α/(α+2) ≤ β < 1/2;
    - Sec. 5 construction: P ∪ P^{1/β} minus P_S, with ζ_{α,β} = ζ(s)ζ(s/β)/ζ_S(s).
  - Hilberdink 2005 [theorem]: max{α,β} ≥ 1/2.
  - Broucke arXiv:2507.13780, Thm 1.6 [unrefereed].
  - Diamond–Montgomery–Vorhauer, PAPER-0581 [theorem].
  - Campaign claim C2-26 (upheld with corrections).
- **Link.** The rational system has N(x) = ⌊x⌋ = x + O(1), so it satisfies every regularity hypothesis P_β. Hence 'Beurling + P_β implies X' is refuted either by not-X for ζ or by a construction. A construction that is conditional on X for ζ becomes an unconditional refutation by a case split.
- **Verified compatibility.** The verifier read BDR Sec. 5 in full.
  - RH enters only through π(x) = Li(x) + O(x^{1/2+ε}), which is used for exactness of α, and through ζ^{±1} ≪ |t|^ε on Re(s+1−α) ≥ 1 − α/2 + ε > 2/3.
  - Lemma 5.1, the random-prime Thm 1.2 and the PNT are unconditional.
  - ζ_S has a simple pole at α, so ζ_{α,β} has a real zero at α > 1/2.
  - The constraints α > 1/2 and α ≤ 2β/(2−β) are compatible iff β > 2/5.
- **Claim (corrected).**
  - **T1** [Observatory-proposed theorem, non-constructive; verifier re-derived; given BDR Thm 1.3]. For every β > 2/5 there is a discrete Beurling system with N_P(x) = ax + O_ε(x^{β+ε}) for which ψ_P(x) = x + O(x^{1/2+ε}) fails.
  - **T2** [Observatory-proposed; the verifier confirmed the audit of where RH is used]. For Θ ∈ [1/2, 2/3) and β > 2Θ/(Θ+2), the implication 'Beurling + P_β implies QRH(Θ)' is false unconditionally. The hypothesis actually used is zero-freeness of ζ with Lindelöf-type bounds on Re s > 1 − α/2. Example: Θ = 0.6 needs β > 6/13.
  - **T3** [theorem, from BDR Thm 1.1]. For every Θ < 1 and β ≥ 1/2 the QRH(Θ) implication is false.
  - **T4** [open frontier]. No countermodel is known for β < 1/2 and Θ ≥ 2/3.
- **Proved.** T1 and T3; T2 at the level of the Sec. 5 audit.
- **Conjectural.**
  - The Hilberdink–BDR existence conjecture: all [α,β] with max{α,β} ≥ 1/2 occur.
  - Whether β < 1/2 forces any zero-free region beyond de la Vallée Poussin.
  - The 'QRH hitting set' restates known obstructions (verifier). It says that a proof of QRH(Θ) needs an input beyond each of: FE plus Dirichlet-series shape; sieve axioms; Euler product plus integer regularity; generic large-sieve coefficients. The 2026 inputs (the Gauss-sum identity and the metaplectic theta function) lie outside all four, consistent with quasi-RH DOSSIER Sec. 2.1–2.3.
- **Next step.**
  1. Write T2 as a lemma under QRH(Θ).
  2. Extend the perturbation to α ≥ 2/3 with β < 1/2 (BDR Remark 5.3(2)).
  3. Record A(β) := sup{α : an [α,β]-system exists} as an obstruction-frontier row in the ledger.
- **Counterexamples.**
  - T1 fails if BDR Thm 1.3 is wrong.
  - A Beurling theorem of the form 'β < β₀ gives a region beyond de la Vallée Poussin' would refute the Hilberdink–BDR conjecture. It would also be a Beurling route to QRH-type statements for ζ.
- **Tests.** Planned, not run:
  - a system at (α,β) = (0.6, 0.47) with primes up to 10^8, checking N − (ζ(1/β)/ζ_S(1))x ≍ x^{0.47};
  - the sign change of ζ_{α,β}(σ) at σ = 0.6.
- **Significance.** For θ > 2/5 this answers, non-constructively, the question the C2 report left open: is there an unconditional RH-false Beurling system with N(x) = Ax + O(x^θ), θ < 1/2? It also maps exactly where integer regularity could still matter for the 2026 exponents.
- **Difficulty.** 3.

### Rank 2: CON-0021 (sound_and_useful; M5; sig 3, diff 2)
**Littlewood 1912 / Beurling 1955 in Hardy-space form.** The Möbius Nyman–Beurling error decays exactly like n^{−2(α−Θ)}, where Θ = sup Re ρ.
- **Sources.**
  - Manzur–Quintero arXiv:2611.03924v1 [unrefereed]: Prop. 4.1, Thms 3.2 and 3.5, Cor. 3.6, eq. (4.2), Table 1.
  - Littlewood 1912 (PAPER-0287) and Beurling 1955 (PAPER-0475).
  - Balazard–Saias 1998, Lemme 2 (the rate n^{−δ/3}).
  - Titchmarsh Sec. 14.2 and Thm 14.25(A) (PAPER-0168).
  - Dimitrov–Oliveira arXiv:1608.07887, Thm 4: L^{±1} ≪ |t|^ε in a zero-free half-plane.
- **Link.**
  - Start from the identity E − S_n = (1 − ζ(s)[M_n(s) − M_1(n)])/s.
  - Apply truncated Perron to M_n with T = n², shifted to Re = Θ + ε.
  - Bound M_1(n) by partial summation.
  - The lower bound comes from the analytic continuation of 1/ζ(1+s).
- **Verified compatibility.**
  - 1/ζ ≪ |t|^ε on σ ≥ Θ + ε, given the half-plane.
  - The mean square of ζ on Re s = α > 1/2 is ≍ T, so ∫|ζ|²(1+|t|)^{2ε−2} converges.
  - The truncation error does not depend on t.
- **Claim** [Observatory-proposed proposition; the verifier re-derived both bounds, with minor corrections]. For α ∈ (Θ,1):
  - s_n(α) ≪ n^{2(Θ−α)+ε} for all n;
  - s_n(α) ≥ n^{2(Θ−α)−ε} infinitely often;
  - so limsup log s_n(α)/log n = −2(α−Θ), and for α ≥ 1 the value is −2(1−Θ).
- **Corollaries.**
  - RH holds iff s_n(α) ≪ n^{1−2α+ε} for one (equivalently every) α ∈ (1/2,1).
  - Power decay at a single α forces Θ ≤ α − δ/2.
  - The Manzur–Quintero threshold satisfies α_c = Θ unconditionally (verifier's addition).
  - [Conditional on QRH-7/8] their Thm 3.2 extends from α > 1 to α > 7/8.
- **Proved.** Both directions, at proof-sketch level. Two minor repairs:
  - at α = 1, bound (M_n(s) − M_n(1))ζ(s) directly, because of the pole;
  - writing (|t| + n²)^ε = n^{2ε}(1+|t|)^ε disposes of the large-|t| issue.
- **Conjectural.**
  - Only the unrefereed status of the proposition itself, and of QRH-7/8 in the corollary.
  - The lower bound holds only along a subsequence.
  - The constants blow up as α decreases to Θ.
- **Next step.**
  1. Write the 3–4 page proof.
  2. Check Balazard–Saias, Notes 4 (2004), for an existing weighted rate.
  3. File it as a separately labelled object.
- **Counterexamples.** None known. The statement is vacuous for α ≤ 1/2.
- **Tests.**
  - Identity checks at n = 10 and 30 (s_10(0.8) = 0.0313396 reproduced).
  - An n = 10^7 envelope fit is proposed. It is a consistency check only and cannot decide Θ.
- **Significance.** This is an exact unconditional dictionary between NB approximation rates and the abscissa Θ. It removes the Balazard–Saias n^{−δ/3} loss and gives a rate-to-half-plane converter for graded criteria (see CON-0007 and BRG-MELLIN_WAVELET-O3).
- **Difficulty.** 2.

### Rank 3: CON-0006 (needs_correction, corrected; M2; sig 4, diff 3)
**Off-line pair defect.** This locates exactly where RH enters the 19/27 simple-zero machinery, and gives an RH-free conditional theorem.
- **Sources.**
  - Bui–Heath-Brown arXiv:1302.5018 (PAPER-0070): pp. 3–4 say RH is used only for S₂ ('the only place we need RH'); Lemmas 1–2; eq. (10).
  - Conrey–Ghosh–Gonek, PAPER-0049.
  - Balasubramanian–Conrey–Heath-Brown, PAPER-0453 (mollified mean values, θ < 1/2).
  - BGST v3, Thms 1–2 (LED-CRIT-13).
  - Knausgård PAPER-0166: simple-anywhere 0.67800919 [unrefereed, computer-assisted].
- **Link.** Put a(ρ) = BZ′(ρ) and ρ* = 1 − ρ̄. Then S₂ = Σ_{on-line} |a|² + Σ_{pairs} 2 Re(u v̄) holds exactly without RH. Apply Cauchy–Schwarz with weight-2 coordinates (u+v)/2.
- **Verified compatibility.** B has real coefficients. A pair of zeros shares its ordinate and multiplicity. A multiple zero gives a = 0.
- **Claim (corrected)** [Observatory-proposed; the verifier re-derived both parts].
  - (a) **[Unconditional inequality.]** N*(T) ≥ |S₁|²/(S₂ + D/2), where D is the off-line pair defect.
    - N* counts simple zeros anywhere. The right comparators are therefore 0.67800919 and the window cap 0.6818287, not 0.6725.
  - (b) **[Conditional theorem.]** Suppose every zero with T < γ ≤ 2T satisfies |β − 1/2| ≤ η(T)/(log T)^{3/2} with η → 0. Then liminf N*/N ≥ 19/27.
    - In the quantitative form D ≤ ηTL³, one needs η < 0.01315, 0.01074 or 0.0091 to beat 0.6725007, 0.67800919 or 0.6818287 respectively.
    - The hypothesis is weaker than RH. The pair-correlation route needs only a fixed thin box (b = 0.3185 gives 2/3), so the gap between (b) and that route is wider than 'b → 0'.
- **Proved.** (a) and (b). The proof of (b) uses:
  - subharmonicity of |a′|² on discs of radius 1/L;
  - the local zero count O(L);
  - ∫|(BZ′)′|² ≪ TL⁴ near the line.
- **Conjectural.**
  - ML-CGG [conjecture]: Σ_{β≠1/2} |BZ′(ρ) − BZ′(1−ρ̄)|² = o(T log³ T).
  - 'D is of order S₂ for Davenport–Heilbronn' [heuristic only].
  - A fourth moment near the line: BBLR gives one only for mollifier length θ < 1/8.
- **Next step.**
  1. A referee-ready note for (a) and (b).
  2. Find the largest explicit η admissible from Conrey's '99.9% within 8/L' plus a mean value over the remaining near-line zeros.
- **Counterexamples.** None for (a) or (b). A configuration with D comparable to S₂ would defeat the route.
- **Tests.** 20,000 random configurations with 0 violations. The equality case u = 1, v = t gives 2.
- **Significance.** The first exact accounting of the RH input in the CGG/BHB discrete moments (bottleneck (c) of CRIT in research_programs.md), with an RH-free target and explicit thresholds.
- **Difficulty.** 3.

### Rank 4: CON-0025 (sound_and_useful; M6; sig 4, diff 2)
**Exponent-2 class groups and Euler's idoneal numbers.** The Siegel-exclusion constant suffices, and QRH is not needed.
- **Sources.**
  - Kimura arXiv:2610.21511 [unrefereed; the author reports Lean checks; not replayed]:
    - Thm 1: (1−β) log q ≥ 5.811·10⁻⁴ for all q, and ≥ 1193/200000 for log q ≥ 35.0131;
    - Prop. 9.
  - Elsenhans–Klüners–Nicolae (EKN), Acta Arith. 193 (2020) [theorem; refereed computation]:
    - Thm 1: an unconditional count for |D| ≤ 3.1·10^20;
    - Thm 2: its hypothesis is the zero gap [1 − 1/(4 log|D|), 1);
    - Lemma 1: the Weinberger lemma.
  - Grube's reduction, via Kani 2011 Thm 6.
  - PAPER-0161, Sec. 1: the route QRH ⇒ EKN Thm 2.
  - SIEGEL DOSSIER Sec. 5, item 6.
- **Link.** Genus theory gives h = 2^{ω−1}. The split-prime criterion applies. A Siegel constant bounds |D| through Prop. 9, and an exhaustive scan covers the rest.
- **Verified compatibility.**
  - All 2026 constants are ≤ 1/64, below EKN's 1/4, so EKN Thm 2 is unavailable.
  - Route A uses EKN Thm 1.
  - Route B uses Kimura's list of fields with h ≤ 2000 (d ≤ 1.06·10^9).
- **Claim (corrected)** [conditional on Kimura Thm 1 + Prop. 9, and on EKN Thm 1 (Route A) or on Kimura Thm 2 plus the scan (Route B)].
  - The imaginary quadratic fields with class group of exponent ≤ 2 are exactly the 65 known ones; the largest |D| is 5460.
  - Euler's 65 idoneal numbers are complete.
  - Verifier's strengthening: Kimura's all-q constant alone excludes exponent ≤ 2 for |D| ≥ 6.60·10^19 < 3.1·10^20, so the constant that depends on log q is not load-bearing.
  - Corrected thresholds: Guo's 1/100 gives 2.14·10^15; Guo's 1/64 gives 8.5·10^14; Banks's 3·10⁻³ gives 1.15·10^17.
- **Proved** [computed, exact].
  - Scan of every fundamental discriminant d ≤ 3.2981·10^16 with ω ≥ 12.
    - Counts: 2,217,855 of the form d = n, 49,375,797 of the form 4n and 32,728,456 of the form 8n, with 0 survivors.
    - Program exp2scan.c, sha256 2022745…; an independent verifier implementation reproduced the counts exactly.
  - Route B: every fundamental d ≤ 1.1·10^9 leaves exactly 65 survivors.
- **Imported, not re-derived.**
  - The correspondence between Kimura's text and his Lean files.
  - The Grube/Kani reduction at the level of orders.
  - EKN's computation.
  - EKN's exponent-4 and exponent-8 lists are not recovered.
- **Next step.**
  1. A third replay (PARI qfbclassno on samples).
  2. Check Kimura's Lean statement of Prop. 9.
  3. Write the order-level step for non-fundamental −4n.
  4. Add a ledger note: idoneal completeness follows from Siegel exclusion, not from QRH.
- **Counterexamples.** An error in Kimura's constants, or an enumeration bug.
- **Tests.** Done: two independent scans, the 65 known discriminants, and 26 non-examples.
- **Significance.** It decouples a headline QRH consequence (paper2 l.116–125) from QRH and ties it to the SIEGEL cluster (FND-0010). It is not an RH statement.
- **Difficulty.** 2.

### Rank 5: CON-0038 (sound_and_useful; M8; sig 5, diff 7)
**Ji's independent Q(i) route cannot reach 11/12 from zero-density inputs.** An OpenAI-independent 11/12 needs a quartic row mean square.
- **Sources.**
  - Ji arXiv:2611.16665v2 (PAPER-0155) [unrefereed; claims 599/600]:
    - (9): H = X^{65/144}, Y = X^{1/288};
    - Prop. 2.1 (bound X²Y⁵H⁻²) and Prop. 2.3;
    - Lemma 4.1: bound (24) holds only for θ = Re w ≥ 1/2;
    - Lemma 4.2: s₀ ≥ 5/8;
    - (27)–(29).
  - de Faveri arXiv:2610.04045 [unrefereed]: quartic density estimate and sieve Θ₄.
  - quasi-RH DOSSIER Sec. 4.1 (C2): β(n,h) = 1/2 + h(n−1)/(2n).
- **Link.** Transcribe Ji's constraints C1–C6 and optimise over all parameters, for an arbitrary density input E(σ).
- **Verified compatibility.**
  - Ji's own parameters are feasible at 599/600 and infeasible at 0.9983.
  - Λ(σ,θ) = max(0, 1 − 3σ/2, 1 − σ − θ/3).
  - The w-contour constraint a ≥ 1/2 (Lemma 4.1) is separate from s₀ ≥ 5/8 (Lemma 4.2).
- **Claim (corrected).**
  - (A) [computed floor of the transcribed inequality system; verifier re-derived analytically]
    - With de Faveri's E: inf Θ = 0.998327.
    - For every density input, including DH and GRH for the quartic family: inf Θ ≥ 0.996732 (this uses a ≥ 1/2).
    - With s₀ → 1/2: 89/90.
    - Deleting the local-factor loss: 23/24 > 11/12.
    - Without the w-contour constraint: ≥ 0.98980 unconditionally and ≥ 25/26 under GRH.
    - So no zero-density improvement brings this architecture to 11/12.
  - (B) [conjecture J4; this is DOSSIER (C2) with n = 4, made explicit]
    - Hypothesis: Σ_{0<N(u)≤X^h} |A_u(X)|² ≪ X^{1+h+ε} for some 1 ≤ h ≤ 10/9, where A_u(X) = Σ_{(n,1+i)=1} μ_K(n)(u/n)₄W(Nn/X).
    - Conclusion: ζ_{Q(i)}, and hence ζ, has no zeros in Re s > 1/2 + 3h/8.
    - More generally, any bound X^aH^b with a + (b − 1/4)h ≤ 11/6 and h ≥ 1/3 gives 11/12.
- **Proved.** (A), as a statement about Ji's system, not about ζ. The extraction step in (B) is elementary.
- **Conjectural.** J4 itself. It needs a quartic duality partner:
  - a quartic Kubota series of angular weight 1;
  - a μ-removal identity analogous to (eq:convert2).
  Explicit coefficients of n-fold metaplectic theta functions are known only for n = 2, 3 (DOSSIER Sec. 4.3).
- **Next step.**
  1. Independent re-derivation of C6 and of the H^Λ factor.
  2. Restructure Ji's Prop. 2.2 as a mean square over u, using de Faveri's sieve.
  3. Test a μ-removal identity for quartic Kubota coefficients of angular weight 1.
- **Counterexamples.**
  - A degree of freedom missed in the transcription.
  - Gauss-sum bias for n = 4 without an angular twist (Dunn–Radziwiłł PAPER-0960; de Faveri–Dunn–Hoffstein).
- **Tests.** The floor table is done. Proposed: a sensitivity test, and small numerics at X ≈ 2000, H ≈ X^{1.05} over Z[i].
- **Significance.** The only OpenAI-independent route known to the Observatory is blocked at about 0.99 for all density inputs. The single missing input is named.
- **Difficulty.** 7.

### Rank 6: CON-0030 (needs_correction, corrected; M7; sig 5, diff 2)
**Density-currency ceiling.** Density-type zero inputs cannot exclude any set of o(T) off-line zeros.
- **Sources.**
  - Goldston–Lee–Schettler–Suriajaya (PAPER-0537): Thm 1; Sec. 4, the pair correlation conjecture (PCC) with o(TL) error; Sec. 7.
  - Bettin–Gonek PAPER-0064.
  - Lagarias–Rodgers PAPER-0103, Thm 3.1.
  - The AF ceiling 0.6818287 (LED-CRIT-10).
  - Littlewood's lemma; Balazard–Saias–Yor 1999.
- **Link.** The following inputs all stay stable when E(T) = o(T) zeros are moved:
  - (i) Riemann–von Mangoldt with S(t) = O(log T);
  - (ii) pair or n-level correlations with o(TL) error;
  - (iii) Fujii–Tsang moments of Δ_U S(t), which depend only on ordinates;
  - (iv) the Littlewood-plus-Jensen output inequality of Levinson–Conrey;
  - (v) bandwidth-limited trace moments (the AF certificates).
- **Claim (corrected)** [Observatory-proposed formalisation of folklore; verifier re-derived].
  - (a) |N_Z(λ) − N_Z′(λ)| ≤ 4E(T)(λ + C log T).
  - (b) |D_Z − D_Z′| ≤ E(T)/2.
  - (c) An n-level sum with a Schwartz-decay test function changes by at most 2n‖η‖_∞E(T)(C log T)^{n−1}.
    - This is o(TL) if E(T) = o(T/(log T)^{n−2}).
    - It is o(TL) for any E(T) = o(T) if the moved zeros, at both old and new positions, sit where the window count is O(λ+1).
    - The moved zeros must be well separated.
  - Consequence [theorem-level for this input class]: no argument whose only zero inputs are (i)–(v) can prove RH, exclude one off-line quadruple, or exclude any o(T) off-line set. Its best conclusion is '100% critical and simple', and that is attained.
- **Proved.** (a), (b), and (c) as corrected.
- **Conjectural.**
  - Which functional each 2026 proportion paper actually uses (to be tagged).
  - BGST's F(α), as a mixed-currency functional.
- **Next step.**
  1. An explicit C from Trudgian's bound on S(t).
  2. A 'currency' tag on each CRIT ledger row.
- **Counterexamples.** Clustering inside windows for n ≥ 3, handled by the correction.
- **Tests.** Derivation only.
- **Significance.** It formalises CRIT23 DOSSIER Sec. 7.5 ('even 100% would not be RH') as a reusable lemma. It is folklore in substance (verifier).
- **Difficulty.** 2.

### Rank 7: CON-0035 (sig 7, diff 5) and CON-0011 (sig 4, diff 3) (needs_correction, corrected; M8 / M3)
**The rank–trace certificate transplanted to an individual GL(2) L-function.** Bandwidth 1/2 gives no simple zeros, but there is a distinct-zero target 1/R*(1/2) = 0.4617.
- **Sources.**
  - AF PAPER-0486 [AI-generated, unrefereed]: Thm A; chain (1.2); Lemma 3.2; Rem. 3.3 (rank ≥ tr²/‖·‖²_HS); Rem. 6.1 (R_λ(ψ₀) = 1/λ + λ/3); Sec. 7.2(e).
  - Lamzouri PAPER-0533, Prop. 2.1 [unrefereed].
  - Hua–Yang arXiv:2609.27808 [unrefereed]: the closed form c*_λ = 1/R*(λ).
  - Murty–Perelli, IMRN 1999 [theorem, conditional on GRH + Hypothesis MP]: pair correlation for |α| < 1/d.
  - Das–Ismoilov–Ramos arXiv:2502.05106, Cor. 8 [unrefereed]: the window-optimal constant R*(1/m) in degree m.
  - Bernard arXiv:1404.6432: 2.97% of GL(2) zeros on the line, and no simple zeros.
  - LED-CRIT-19: 6.96% critical zeros for each GL(2) cusp form.
- **Link.**
  - Use the per-form explicit formula with Gabor compression at density (1/2π) log(NT²).
  - For a single GL(2) form the diagonal bandwidth is 1/2 in GUE units.
- **Verified compatibility.**
  - Bandwidth 1/2 agrees with the Murty–Perelli range at d = 2.
  - Recomputed to 30 digits: R*(1) = 1.3274993 = 1/C_MT; R*(1/2) = 2.165963850; λ* = 0.5501939647; R*(1/3) = 3.1109043.
- **Claim (corrected).**
  - (A) [theorem, elementary, within the window class; known in substance as Das–Ismoilov–Ramos Cor. 8]
    - For every ψ ≥ 0 on [−1/2, 1/2] and every λ ≤ 1/2, 2 − R_λ(ψ) < 0.
    - The simple-on-line certificate is positive iff λ > λ* = 0.5501939647 (for the flat window, 3 − √6).
    - So bandwidth-1/m window certificates give no simple or critical zeros in degree m ≥ 2.
    - But the distinct-zero bound 1/R*(1/m) is positive for every m (m = 3: 0.3214).
  - (B) [conditional on the GL(2) all-zeros pair-sum asymptotic at support < 1/2, i.e. on porting AF/LZ to L(s,f)]
    - Statement: for every fixed primitive holomorphic or Maass newform f, liminf N_d(f;T,2T)/N(f;T,2T) ≥ 1/R*(1/2) = 0.4616882225. No self-duality restriction is needed.
    - Under RH the two-moment integer bound would be (5 − R*)/6 = 0.472339; reaching it unconditionally is open.
    - Superseded: the targets (3 − R)/2 = 0.4170180748 and 'degree 3 gives nothing'.
- **Proved.** (A). The rank bound tr²/‖·‖²_HS holds for every Hermitian matrix.
- **Conjectural.** The GL(2) port:
  - the Rankin–Selberg diagonal must reproduce |α|;
  - the archimedean–prime cross terms must be o(N);
  - the C² taper tail must be redone with degree-2 Gamma factors.
  λ* is a barrier for window certificates only.
- **Next step.**
  1. Write the GL(2) prime-side second-moment lemma (Λ_f, the λ_f(p²) − 1 terms, Maass prime powers).
  2. Rerun chain (1.2) with the window cos(x/√2).
- **Counterexamples.** None known. Any unconditional GL(2) second-moment bound at bandwidth 1/2 + η with η > 0.0502 would give simple critical zeros.
- **Tests.** A quadratic programme with n = 400 discretisation points reproduces the constants.
- **Significance.** (B) would be the first unconditional positive proportion of distinct zeros for an individual GL(2) L-function. (A) is the exact barrier for simple zeros within the window class.
- **Difficulty.** 5 and 3.

### Rank 8: CON-0036 (sig 6, diff 5) and CON-0012 (sig 3, diff 2) (needs_correction, corrected; M8 / M3)
**Petersson orthogonality instead of character orthogonality.** This gives proportions of simple and distinct GL(2) zeros on a harmonic family average.
- **Sources.**
  - Hua–Yang arXiv:2608.16034 [unrefereed]: prime-modulus Dirichlet family, family-total proportions 0.6725007 and 0.8362504; Sec. 3 (Selberg family argument estimate; Hiary–Zhao deletion of exceptional characters); Sec. 9 (Gevrey tail); Secs 10–11.
  - AF Rem. 7.2: Dirichlet average 0.811/0.905; details omitted; not in Lean.
  - ILS PAPER-0019, Sec. 2.
  - Kowalski–Michel math/9707238, Thm 1.1.
  - Iwaniec–Kowalski PAPER-0457, Prop. 14.5.
  - LZ Prop. 2.1: linear in (tr A, tr A²), so nonnegative weights are admissible.
- **Link.** Combine the per-form inertia certificate with the Petersson formula. At polylogarithmic T, log(NT²) ~ log N, so the bandwidth λ tends to 1.
- **Verified compatibility (after correction).** Three inputs are needed.
  - An explicit diagonal lemma: for fixed k ≥ 2, N prime and X ≤ N^{1−ε}, Σ_f ω_f |Σ_{p≤X} a_p λ_f(p)|² = (1 + O((X/N)^{k−1}N^ε)) Σ|a_p|². It is proved by opening the Kloosterman sums and applying the additive large sieve; Bessel decay alone reaches only X ≤ N^{1−1/(2k)−ε}.
  - A GL(2) analogue of Hua–Yang Sec. 3: zero-density deletion and an averaged count uniform at fixed T.
  - A GL(2) analogue of Sec. 9: the Gevrey tail.
- **Claim (corrected)** [conjecture / expected theorem GL2-F; proof plan].
  - Setting: k ≥ 2 fixed, N prime → ∞, (log N)^{1+η} ≤ T ≤ (log N)^A.
  - Conclusion: the harmonic-weight family ratio is ≥ 0.6725007 for simple zeros on the line and ≥ 0.8362504 for distinct zeros.
  - Fallback using the Weil bound only: bandwidth 1 − 1/(2k).
    - At k = 2 this gives ≥ 0.4191 and ≥ 0.7095.
    - 2 − R*(1 − 1/(2k)) = 0.419075, 0.569339, 0.642191, 0.669052 for k = 2, 4, 12, 100.
  - Corrected test prediction: R*(0.9) = 1.406898.
  - Removing the harmonic weights needs the ILS device with L(1, sym² f).
  - This is a family statement only. By CON-0011(A), no conclusion for individual forms follows.
- **Proved.** Only the standard off-diagonal Petersson bound.
- **Conjectural.** The whole theorem.
- **Next step.**
  1. Rewrite the trace sections of Hua–Yang using Petersson.
  2. Prove the diagonal lemma.
  3. Add the zero-density deletion.
- **Counterexamples.** Without analogues of Hua–Yang Secs 3 and 9 the fixed-T tail is uncontrolled.
- **Tests.** Corrected target for the Kloosterman tail: (X/N)^{k−1}.
- **Significance.** No unconditional proportion of simple or distinct GL(2) zeros on average is known.
- **Difficulty.** 5 and 2.

### Rank 9: CON-0008 (sound_and_useful; M2; sig 2, diff 3)
**A persistence lemma for the de Bruijn–Newman converse.**
- **Sources.**
  - Polymath15 (Res. Math. Sci. 6 (2019); LED-DBN-8):
    - Prop. 3.1: the zero ODE dz_j/dt = 2Σ′ 1/(z_j − z_k);
    - Thm 1.5(iv): local count O(log(2+X)) for 0 < t ≤ 1/2;
    - Thm 3.2.
  - Rodgers–Tao PAPER-0036: Λ ≥ 0 (LED-DBN-6).
  - Platt–Trudgian PAPER-0001: Λ ≤ 0.2 (LED-DBN-10).
  - C1-E1 [heuristic, numerical].
- **Link.** Take the windowed energy E(t) = Σ φ_j y_j² of the complex zeros of H_t.
  - It satisfies |dE/dt| ≤ C log² x₀.
  - E(0) ≥ 4δ².
  - E(t) > 0 forces t < Λ.
- **Verified compatibility.** The verifier re-derived each pair contribution. Collisions are harmless (the He_m roots sum to zero). One input is still missing: an O(log x) bound for H_t′/H_t at distance about 1 from the zeros, uniform in t.
- **Claim** [Observatory-proposed; proof sketch].
  - If ζ(1/2 + δ + iγ) = 0 with 0 < δ < 1/2 and γ ≥ γ₀, then Λ ≥ cδ²/(log γ)².
  - Sharp form [conjecture]: Λ ≥ c·min(δ², δ/log γ).
- **Proved.** A sketch, with two gaps: the far-field velocity bound, and the a.e.-ODE / absolute-continuity step.
- **Conjectural.** The sharp form and an explicit c. With Λ ≤ 0.2 the lemma constrains only γ ≲ 10^4, which is already verified.
- **Next step.** A rigorous energy proof; the sharp form via a near/far splitting.
- **Counterexamples.** Clusters of nearly coincident complex zeros; this is why the energy is windowed.
- **Tests.** Farmer-type toy models with Arb root tracking.
- **Significance.** This is the correct δ-dependent form of the open converse (research_programs.md, DBN l.102). A δ-free form cannot follow from the dynamics, since a pair with δ → 0 collapses in time about 2δ².
- **Difficulty.** 3.

### Rank 10: CON-0017 (needs_correction, corrected; M4; sig 3, diff 2)
**Pólya–Vinogradov at Montgomery–Vaughan strength under any fixed half-plane.**
- **Sources.**
  - Granville–Soundararajan math/0503113, Thm 2.1 [theorem].
  - Montgomery–Vaughan 1977 (PAPER-0082), Secs 8–9 [theorem, conditional on GRH]: GRH enters only through Lemma 2 on the major arcs.
- **Link.** QRH(θ) for the twists replaces GRH in MV Lemma 2, with error x·y^{θ−1}(log kx)²/(1−θ)².
- **Claim (corrected)** [conditional on L(s,χψ) ≠ 0 for Re s > θ for every ψ of modulus ≤ (log q)^C; outline verified].
  - M(χ) ≪ (1−θ)^{−1}√q log log q for every primitive χ mod q, and for every fixed θ < 1.
  - Superseded: the claim that θ < 2/3 is needed and that the claimed 7/8 does not reach Montgomery–Vaughan. The 2/3 is an artifact of the Granville–Soundararajan Prop. 2.3 route.
  - Part (a), the bound √q(log q)^{6/7}, is correct but superseded.
- **Proved.** An outline.
- **Conjectural.** QRH itself.
- **Next step.** Write the QRH version of MV Lemma 2 and the bookkeeping of MV Sec. 9.
- **Counterexamples.** None. The bound √q log log q is attained up to constants.
- **Tests.** None.
- **Significance.** It would put the GRH-sharp character-sum bound on a QRH footing.
- **Difficulty.** 2.

### Rank 11: CON-0018 (sound_and_useful; M4; sig 2, diff 1)
**Piltz divisor exponents from ζ ≠ 0 on Re s > 7/8.**
- **Sources.**
  - ANTEDB Lemma 16.9 (Ivić Sec. 13.3).
  - ANTEDB Lemma 9.9 (Ivić Thm 8.4: A = 10/(5 − 6σ) on (5/8, 35/54], with anchors).
  - Li Thm 16.20: α₁₄ ≤ 0.731898, α₂₀ ≤ 0.791374.
  - Trudgian–Yang Thm 16.19: α₂₁ ≤ 0.79951.
- **Link.** A zero-free half-plane gives μ(σ) = 0 for σ > θ, hence M(θ + ε, B) = 1 for every B. Log-convexity (Gabriel; Hardy–Ingham–Pólya) then interpolates.
- **Claim** [conditional on QRH(θ); the qualitative bound α_k ≤ θ is classical].
  - α_k ≤ θ − C(θ)/k, with C(7/8) = 49/24 (k ≥ 9) and C(11/12) = 17/7 (k ≥ 12).
  - Under QRH-7/8 this beats the tabulated records for k = 14 to 21 (k = 14: 0.72917 against 0.73190; k = 20: 0.77292 against 0.79137).
  - There is no gain at k = 13.
- **Proved.** The implication; the script piltz.py was reproduced.
- **Conjectural.** QRH-7/8.
- **Next step.** Check the hypotheses of Ivić Lemma 8.3; rerun with the anchors of Li and of Trudgian–Yang.
- **Counterexamples.** None.
- **Tests.** The case θ = 1/2 gives α_k ≤ 1/2, a Lindelöf check.
- **Significance.** Modest.
- **Difficulty.** 1.

### Rank 12: CON-0019 (sound_and_useful; M4; sig 2, diff 1)
**Exceptional sets for the PNT in short intervals, under ζ ≠ 0 on Re s > 7/8.**
- **Sources.** Gafni–Tao arXiv:2505.24017: Thm 1.2; Thm 1.3; the convention A(σ) = −∞ when no zeros exist; Tables 1–2.
- **Link.** Under QRH-7/8, A(σ) = −∞ for σ > 7/8, while A(7/8) = 12/7 and A*(7/8) = 24/5.
- **Claim (corrected)** [conditional on QRH-7/8; a bound produced by the Gafni–Tao method].
  - μ(θ) ≤ max(U_{<7/8}(θ), min((3/14)(1−θ) + 3/4, (3/5)(1−θ) + 1/2)).
  - This is a strict improvement exactly for θ ∈ (0.2445, 5/12), with maximal gain about 0.0108 at θ ≈ 0.2725.
  - The 17/30 and 2/15 thresholds are unchanged.
  - Corrected: the gain under QRH-11/12 is at most about 0.0026.
- **Proved.** The conditional computation.
- **Next step.** Feed the QRH-improved μ(σ) on [3/4, 7/8] into the ANTEDB routines.
- **Counterexamples.** None.
- **Tests.** Exact rational arithmetic at the breakpoints.
- **Significance.** Modest.
- **Difficulty.** 1.

### Rank 13: CON-0015 (sound_and_useful; M3; sig 2, diff 2)
**Zeros of ξ′: the bandwidth-one window class is exhausted at 0.868642.**
- **Sources.**
  - AF Rem. 7.1 [AI-generated, unrefereed]: flat window 0.85838/0.92919; quartic window 0.86864/0.93432.
  - The Farmer–Gonek form factor.
  - Knausgård PAPER-0166, Thm 5.1 [unrefereed].
  - Wu arXiv:1206.3737: 0.86957 on the line.
  - Chirre–Gonçalves–de Laat PAPER-0073.
- **Claim** [numerical, non-rigorous; recomputed by the verifier].
  - The optimal window has R* = 1.13135850. Simple-on-line: 0.86864150; distinct: 0.93432075.
  - The quadratic form is positive definite on even windows, so this is the global optimum, signed windows included.
  - AF's quartic window is within 10⁻⁶ of it.
  - So no window can make 'simple and on the line' exceed Wu's 'on the line'.
- **Proved.** Nothing rigorous.
- **Conjectural.** That the ξ′ ceiling exceeds 0.86957.
- **Next step.** An ξ′ ceiling LP; abandon the direction if the ceiling is below 0.86957 + 10⁻⁴.
- **Counterexamples.** A ceiling below Wu's value would close the direction, which is useful negative knowledge.
- **Tests.** An interval evaluation at n = 1600.
- **Significance.** Small. The test is meaningful because Knausgård's gain for ζ (about 0.001) is the size of the gap.
- **Difficulty.** 2.

### Rank 14: CON-0024 (sound_and_useful; M5; sig 2, diff 3)
**Pólya's approximant ξ* under the de Bruijn–Newman flow, as an arithmetic-free control.**
- **Sources.**
  - Pólya 1926, PAPER-0438.
  - Pólya 1927, PAPER-0424.
  - Newman–Wu arXiv:1901.06596 (PAPER-0657), Thms 2, 7–10.
  - de Bruijn 1950, Thm 8.
  - Hejhal 1990, PAPER-0864.
- **Claim (corrected).**
  - [theorem] −∞ < Λ* ≤ 0.
  - [numerical, non-rigorous] No Fourier critical points of H*_λ were found for λ between −0.05 and −2048, and the argument-principle counts agree in two boxes.
  - [conjecture] Λ* ≤ −4.
  - Corrected λ = 0 zeros: 17.9856, 38.1308, 48.9495, 57.9499.
  - Nothing proves Λ* < 0.
  - Verifier's structural route [heuristic]: write Φ* = 4π² cosh(9u)·exp(−2π cosh 4u). Then de Bruijn's cosh shrink would bound Λ* by the strip width of the heat-flowed kernel of K_{iz/4}(2π). But de Bruijn's strip theorem covers only forward flow.
- **Next step.** A rigorous strip-width or Hermite–Biehler lemma; use ξ* as a positive control for de Bruijn–Newman certification codes.
- **Counterexamples.** Nonreal zeros outside the scanned windows.
- **Tests.** The scripts polya_dbn*.py, plus the verifier's scripts polya0.py and polya4.py.
- **Significance.** It separates gamma-factor effects from arithmetic effects in heat-flow certificates.
- **Difficulty.** 3.

### Rank 15: CON-0007 (needs_correction, corrected; M2; sig 3, diff 2)
**Graded criteria whose missing lemma at level ω is exactly a zero-free half-plane.**
- **Sources.**
  - Suzuki arXiv:2206.03682 (PAPER-0101), Thm 11.1 [theorem].
  - Beurling 1955 (PAPER-0475), with the restriction Σ b_k/θ_k = 0.
  - Dimitrov–Oliveira arXiv:1608.07887, Thms 1–2: graded natural-integer criteria for Re s > 1/p.
  - Báez-Duarte PAPER-0004.
- **Claim (corrected)** [immediate corollaries; conditional on QRH-7/8].
  - Ψ_{3/8}(t) ≥ 0 for all t.
  - Beurling density holds in L^{8/7}(0,1).
  - d_n(ζ, 8/7) → 0.
  - The host's MELLIN graded premise holds at θ = 3/8 + ε.
  - Superseded: the 'new natural-integer L^p lemma'. Dimitrov–Oliveira already cover every 1/p ∈ (1/2, 1).
  - Cureton–Thorner's 31/32 [unrefereed] would be an independent input at ω = 15/32.
- **Next step.** The Titchmarsh 14.2 step for the host's rows.
- **Significance.** Bookkeeping.
- **Difficulty.** 2.

### Rank 16: CON-0020 (needs_correction, corrected; M4; sig 3, diff 2)
**Artin's conjecture from quasi-GRH.**
- **Sources.**
  - Hooley 1967, PAPER-0035.
  - Nongkynrih 2001 (Zbl 1011.11005) [theorem].
  - Murty–Murty, Bombieri–Vinogradov variant.
  - Moree, survey math/0412262.
- **Claim (corrected)** [conditional on zero-freeness of the Kummer-field zeta functions in Re s > θ].
  - Elementary, using Bombieri–Vinogradov: liminf N_a(x)/π(x) ≥ A(a) − log(1/(2(1−θ))), which is positive for θ < 0.656.
  - Nongkynrih: a positive proportion for a = 2 when θ < 0.796.
  - Hooley: infinitude for a = 2 when θ < 0.816.
  - Superseded: the threshold 0.5466.
  - Kept: 7/8 and 1 − 10⁻⁶ lie outside every known threshold.
- **Significance.** A precise boundary for what QRH-type claims give Artin.
- **Difficulty.** 2.

### Rank 17: CON-0033 (needs_correction, corrected; M7; sig 4, diff 4)
**Infinite log-concavity of the Taylor coefficients of ξ cannot imply RH, conditional on a heat-flow conjecture.**
- **Sources.**
  - Liu–Mao 2026, Thm 1.1 [unrefereed].
  - McNamara–Sagan 2010, Lemma 2.1 [theorem].
  - Rodgers–Tao PAPER-0036.
  - Csordas–Norfolk–Varga PAPER-0622.
  - Farmer PAPER-0686.
  - C2-29.
- **Claim (corrected).**
  - (a) [theorem, elementary] (1, b, c) is infinitely log-concave iff b²/c ≥ φ² = (3 + √5)/2, while real-rootedness needs b²/c ≥ 4.
  - (b) [numerical, in the low-index Gaussian regime] Uninformative.
  - (c) [conjecture] There is t₀ > 0 such that (λ_n(t)) is strictly infinitely log-concave for t ∈ (−t₀, 0]. If so, then by Rodgers–Tao, infinite log-concavity of λ_n and its truncations cannot imply RH.
  - Corrected scope: the Turán, higher-Turán and Jensen-hyperbolicity inequalities (for γ_n = n!λ_n) are stronger, not weaker. All-degree Jensen hyperbolicity is equivalent to RH.
- **Next step.** Redo Liu–Mao Sec. 3 with the kernel e^{tu²}Φ at t = −t₀, in interval arithmetic.
- **Significance.** If (c) is proved, a coefficient-inequality route is closed.
- **Difficulty.** 4.

### Rank 18: CON-0031 (needs_correction, corrected; M7; sig 6 proposer, diff 4)
**Extraction bookkeeping.**
- **Sources.**
  - Bettin–Gonek PAPER-0064, Thms 1–2.
  - DWZ arXiv:2605.24363, Thms 1.1, 1.3, 1.8 and Remarks 1.6–1.7 [unrefereed].
  - quasi-RH DOSSIER Sec. 4.1.
  - LED-CRIT-7: mollifier length 4/7.
- **Claim (corrected).**
  - (A) [heuristic, not a law] β ≤ 1/2 + (h/2)(1 − r + a).
  - (B)(i) [known corollary] Proven mollified moments give only vacuous half-planes. Reaching 7/8 would need mollifier length θ = 4/3.
  - (B)(ii) [architecture-specific; already in the DOSSIER] The paper2 lemma with trivial rows cannot beat 1 − 1/(2n) ≥ 3/4.
- **Next step.** An abstract extraction lemma.
- **Difficulty.** 4.

### Rank 19: CON-0014 (needs_correction, corrected; M3; sig 3, diff 3)
**Order-r residue families in the row extraction.**
- **Sources.**
  - quasi-RH ARCHITECTURE item 1.
  - Heath-Brown, Acta Arith. 72 (1995), Thm 1 [theorem].
- **Claim (corrected).**
  - (a) [elementary; credit: ARCHITECTURE item 1] The ceiling is 1 − 1/(2r) at θ = 0.
  - (b) [corrected] The order-2 full mean square is strictly stronger than its conclusion. Modulo Heath-Brown it is equivalent to the conclusion plus dyadic averages |A^{(u1)}| ≪ D^{1/2}(H/U)^{1/4} for 1 < U < D^{1−θ}. The Poisson-dual route is circular. 'Exactly circular' is withdrawn.
  - (c) [heuristic design rule] Row extraction transfers control to the principal member only with a power density of trivialising rows, and only with a duality whose dual principal rows do not contain the principal source.
- **Next step.** Test r = 3 over Z[ω] with zomega.py.
- **Difficulty.** 3.

### Rank 20: CON-0037 (needs_correction, corrected; M8; sig 7, diff 7)
**Conjecture G: quasi-RH for Hecke Grössencharacters of infinite order over Q(√−3).**
- **Sources.**
  - paper2 PAPER-0161: Thm 1.1; l.808–812; (eq:gj) and (eq:convert2); App. A.2.
  - Dunn–Radziwiłł PAPER-0960.
  - Ji PAPER-0155.
- **Claim (corrected)** [conjecture].
  - For every unitary Hecke character ψ of Q(√−3), of any infinity type l, L(s,ψ) ≠ 0 for Re s > 11/12.
  - If true:
    - L(E,s) ≠ 0 for Re s > 17/12, for every E/Q with j(E) = 0;
    - this would be the first fixed zero-free half-plane for a holomorphic GL(2) newform of weight ≥ 2. Superseded: 'the first for any GL(2)', since weight-one dihedral forms are already covered by paper2 and by Liu;
    - Hecke angular equidistribution with error x^{11/12+ε}.
  - Load-bearing unverified step: paper2 Prop. 3.1 at angular frequency m = l − 1.
- **Verified.** The algebraic identity; the normalisation L(E,s) = L(s − 1/2, ψ_E); small numerics.
- **Next step.** List every use of radial weights in paper2; derive J_m for m = −2.
- **Counterexamples.** A Patterson-type main term at m = 0.
- **Significance.** High if true, but entirely conditional on unrefereed 2026 machinery.
- **Difficulty.** 7.

### Rank 21: CON-0003 (needs_correction, corrected; M1; sig 3, diff 3)
**Robin's inequality: extending the range analytically with a signed zero-sum tail.**
- **Sources.**
  - Morrill–Platt PAPER-0590: Thm 13 (LED-ARITH-1); Lemmas 5, 6, 8.
  - Platt–Trudgian PAPER-0001.
  - Robin PAPER-0206.
  - Nicolas PAPER-0008.
  - Ramanujan PAPER-0079.
- **Claim (corrected)** [pre-proof estimates, ±30%].
  - Unconditionally: log n up to about 4–5·10^22, pending an explicit remainder bound.
  - Under H_Θ: about 1.5·10^30 for Θ = 7/8 and about 1.5·10^27 for Θ = 11/12.
  - Superseded: the cap at 2.169·10^25.
  - Morrill–Platt's range is a computation, not an analytic barrier.
- **Next step.** A directed-arithmetic inequality for colossally abundant (CA) numbers.
- **Host link.** BRG-ROBIN-T1.
- **Significance.** A finite range only, never global evidence.
- **Difficulty.** 3.

### Rank 22: CON-0002 (needs_correction, corrected; M1; sig 2, diff 2)
**Explicit ranges for the Nicolas and Johnston criteria.**
- **Sources.**
  - Nicolas PAPER-0008.
  - Johnston PAPER-0100.
  - Platt–Trudgian PAPER-0001.
- **Claim (corrected)** [pre-proof estimates].
  - Nicolas's criterion for p_k up to about 4·10^23, and Johnston's for x up to about 3.7·10^22. This requires an unconditional tail bound for ψ − θ to be added.
  - Under Θ = 7/8: about 3·10^31 and 1·10^30.
  - The band claim in (C) holds only while S_H p_k^{Θ−1/2} < εe^{−γ}, i.e. up to about 2.5·10^27 for ε = 0.1.
- **Difficulty.** 2.

### Rank 23: CON-0004 (needs_correction, corrected; M1; sig 2, diff 2)
**Counting non-Robin numbers, and the true floor of the φ-relaxation.**
- **Sources.**
  - Luca–Solé PAPER-0094, Thm 3.
  - Nicolas PAPER-0008, eq. (1.7).
- **Claim (corrected).**
  - [sketch] Under H_Θ, #NR(x) ≤ exp((log x)^{(1+Θ)/2+o(1)}).
  - [corrected] Under RH, log #Φ(x) = (log x)^{3/4+o(1)}.
  - Any improvement must use Robin's extra factor.
  - Finding: step (5) of Luca–Solé is wrong as printed. Their Thm 3 is still true, but it needs a swap comparison.
- **Difficulty.** 2.

### Rank 24: CON-0005 (needs_correction, corrected; M1; sig 2, diff 1)
**Gorodetsky's ϑ-form theorem at 7/8.**
- **Sources.** Gorodetsky, J. Anal. Math. 151 (2023) [theorem]: Thm 1.1; Remark 4; Thm 1.2.
- **Claim (corrected)** [substitution; conditional on QRH-7/8].
  - Ψ(x,y) ~ xρ(u)K and Ψ ≥ xρ(u) for y ≥ (log x)^{8+ε}.
  - Ψ ≍ xρ(u) fails for every c < 2, regardless of RH.
  - The window c ∈ [2, 8] stays undetermined.
  - There is no consequence for signed sums.
- **Host link.** BRG-SHARP_NATIVE-O4.
- **Difficulty.** 1.

### Rank 25: CON-0010 (needs_correction, corrected; M2; sig 3, diff 1)
**Ledger of missing lemmas, by route.**
- **Content (corrected).** The routes are sorted into three classes:
  - closing lemmas that are equivalent to RH;
  - weaker statements with only a finite horizon;
  - weaker infinite targets.
- **Corrections applied.**
  - Zhu arXiv:2608.24827 is an unrefereed high-precision computation with an error budget, not a directed-rounding certificate.
  - The statement 'RH(T) ⇒ λ_n > 0 for n ≤ T²' is due to Oesterlé.
  - Dimitrov–Oliveira closes the 'L^p NB' gap.
- **Difficulty.** 1.

### Rank 26: CON-0026 (needs_correction, corrected; M6; sig 3, diff 2)
**Cureton–Thorner provenance.**
- **Claim (corrected)** [provenance].
  - Version v1 claims Re s > 1 − 1/6000.
  - Version v2 claims Re s > 31/32 for every number field, with an AxiomProver Lean certificate [unrefereed, not replayed].
  - Frei–Sofos–Widmer cite v1; the other consumers cite v2.
  - The descent to general fields has a single load-bearing step: Kazhdan–Patterson over a field containing μ₁₂.
  - Only history/recent_developments Sec. 5 is stale.
- **Difficulty.** 2.

## 3. Confirmed prior art (sound_but_known), ranked

### P1: CON-0039 (M8; sig 6, diff 2)
- **Sources.**
  - Weinberger 1973 (Zbl 0217.04202) [theorem].
  - Frei–Sofos–Widmer, Cor. 1.2 [unrefereed].
  - EKN Lemmas 1 and 3.
  - Heath-Brown, Forum Math. 20 (2008), Thm 2 [theorem].
- **Confirmed claim** [conditional on QRH(δ)].
  - E(D) ≥ (δ − o(1)) log|D|/log log|D|, effectively. This is Weinberger's theorem with QRH in place of GRH.
  - Corrected: EKN's list for E | 8 needs zero-freeness on [1 − 1/(4 log|D|), 1). The 2026 Siegel constants do not give this; QRH does.
- **Next step.** Make c(δ) explicit.
- **Significance.** QRH would settle effective growth of the exponent E(D).

### P2: CON-0016 and CON-0001 (M4 / M1; sig 4, diff 2)
- **Sources.**
  - Thorner–Zaman PAPER-0962, Thm 2.3 and Rem. 2.4 [theorem].
  - Chen–Gupta–Li (CGL) PAPER-0745, Cor. 1.4 [unrefereed].
  - Huxley 1975.
  - Bruna arXiv:2603.25612.
  - Xylouris (LED-LFUN-10).
- **Confirmed claim** [conditional on H_Θ].
  - P(a,q) ≪ q^{12/5+ε}, effectively.
  - P(a,q) ≪ q^{7/3+ε} using CGL.
  - The PNT in progressions holds for φ(q) ≤ x^{5/12−ε}.
  - The quasi-RH DOSSIER Sec. 3 rows can be strengthened accordingly.
- **Significance.** Replaces the direct exponents 8 and 12 by 12/5.

### P3: CON-0034 (M7; sig 4, diff 2)
- **Sources.**
  - Conrey–Iwaniec PAPER-0102.
  - Heath-Brown PAPER-0685.
  - Lagarias–Rodgers PAPER-0103.
- **Confirmed claim** [logic, conditional on any uniform Siegel exclusion].
  - Theorems that assume exceptional sequences become vacuous.
  - Corrected: no unconditional small-gap result below 1/2 the mean spacing exists.

### P4: CON-0027 (M6; sig 3, diff 1)
- **Sources.**
  - McCurley 1984.
  - Lu–Zaman–Zhao PAPER-0855 [theorem, refereed computation].
  - Guo PAPER-0165.
  - Heath-Brown PAPER-0048.
  - Xylouris.
- **Confirmed claim.**
  - An exception-free explicit zero-free region with R* = 9.6459 for q ≤ 10^10 and R* = 64 for larger q (Guo, Rem. 1.2). Only the R* = 64 form is new.
  - Corrected reason why Linnik's L = 5 is unchanged: the binding cases have no exceptional zero.

### P5: CON-0013 (M3; sig 2, diff 2)
- **Sources.**
  - Gonek–Hughes–Keating PAPER-0027.
  - Gonek 2012, PAPER-0006.
  - Conrad 2005.
  - The host's pass7 PROOF.md Sec. 8.
- **Confirmed claim** [classical].
  - C_X = exp(−E₁((s−1)L)).
  - OPEN_CUTS Sec. 6 at σ₀ = 1/2 is equivalent to RH, which the host proof already states. The graded version is equivalent to QRH(σ₀).
  - Conjectural: pointwise non-locality.

### P6: CON-0023 (M5; sig 2, diff 1)
- **Sources.**
  - Speiser PAPER-0107.
  - Levinson–Montgomery PAPER-0360, Thm 1.
- **Confirmed claim** [direct substitution; conditional on CRIT-2/3].
  - N₁⁻(T) ≤ (0.163750 + o(1))N(T); with Knausgård's value, 0.163231.
  - So at least 83.6% of the zeros of ζ′ lie in σ ≥ 1/2.

### P7: CON-0028 (M6; sig 2, diff 1)
- **Sources.**
  - Gafni–Tao.
  - Guth–Maynard PAPER-0054.
  - Li–Liu.
  - Visser.
- **Confirmed claim** [corollary].
  - Any zero-free half-plane with θ₀ ≥ 7/10 leaves the 17/30 and 2/15 thresholds unchanged.
  - Li–Liu's claim is flagged for audit.

### P8: CON-0009 (M2; sig 2, diff 2)
- **Sources.**
  - quasi-RH ARCHITECTURE item 1(3).
  - audit_S3 Sec. 4.
  - Liu Thm 10.8.
- **Confirmed claim** [restatement].
  - β(θ,ν) = 1/2 + (1+θ)(1−ν)/2.
  - The route-closing lemma is GRH for L_K^S(s,ν).
  - 'Structurally unable' holds only within this design.

### P9: CON-0029 (M6; sig 2, diff 3)
- **Sources.**
  - Littlewood PAPER-0404.
  - Lamzouri–Li–Soundararajan.
  - Granville–Soundararajan.
  - Rodosskii / Montgomery–Vaughan Thm 13.12.
  - Pathak.
  - Kimura, Remark 11.
- **Confirmed claim** [routine adaptation].
  - L(1,χ) lies between ((1−θ)π²/(6e^γ))/log log q and (e^γ/(1−θ)) log log q, up to ε.
  - h(−d) ≥ (π/(48e^γ))√d/log log d under 7/8.
  - Open: the explicit q₀ is not supplied.

## 4. Connections to the host repository

Per AGENTS.md, everything here is a **proposal for the host repository's own review**. It does not change any integrated status, and acceptance by the host does not imply novelty against the literature.

The selection below takes:
- confirmed items, or items confirmed with correction;
- relation identical, equivalent reformulation, special case, or weaker;
- plus obstructions that bind a host open cut.

### 4.1 Prior art at identity level

| BRG id | Host object | Literature (status) | Relation, verdict | Consequence (proposal) |
|---|---|---|---|---|
| BRG-CAUSAL_EULER-P1 | C_X(s) and the corrected product, CURRENT_RESULTS Sec. 9 | Gorodetsky arXiv:2212.01949, eq. (1.5) [theorem] | identical, confirmed | cite the smooth-number lineage; novelty lies only in the L² packaging and the DC3/DC4 constants |
| BRG-CAUSAL_EULER-P2 | proof eq. (13), the Dickman Laplace transform | Hildebrand–Tenenbaum, JTNB 5 (1993), Lemma 2.6 [theorem] | identical, confirmed | cite it |
| BRG-CAUSAL_EULER-P3 | DC5, cancellation on the line Re s = 1 | Saias's lemma as Hildebrand–Tenenbaum Lemma 3.4 [theorem] | host statement weaker, confirmed | host has de la Vallée Poussin strength |
| BRG-CAUSAL_EULER-P4 | DC6 criterion | Akatsuka 2017 (PAPER-0227), Thms 2–3 [theorem] | closely analogous, confirmed | one nonzero pointwise limit suffices |
| BRG-FAMILIES-P3 | L-106213.2 coefficient majorant | Afshar–Porritt, Acta Arith. 187 (2019) [theorem] | host is special case, confirmed | the conductor-uniform shell is prior art |
| BRG-FAMILIES-P5 | L-106000.8/.10, Euler restoration | Davenport; Montgomery–Vaughan [theorem] | identical, confirmed | textbook identity |
| BRG-MELLIN_WAVELET-P1 | M3 consumer | Landau 1905; MV Lemma 15.1 [theorem] | identical, confirmed | cite it |
| BRG-MELLIN_WAVELET-P5 | R17 negative-mass converse | Littlewood 1912 [theorem] | host is special case, confirmed with correction | nodes are RH-equivalent |
| BRG-OPERATORS_HEAT-P10 | L-91035 isometry | Suzuki PAPER-0812 [theorem] | identical, confirmed | pin the source |
| BRG-OPERATORS_HEAT-P11 | T-91008 equivalence | Suzuki PAPER-0101, Thm 1.2 [theorem] | identical, confirmed | pin the source |
| BRG-OPERATORS_HEAT-P15, P16 | Sec. 10 scalar R ≈ 0.6730085; H₀ | Knausgård Thm 5.1 [unrefereed]; AF/LZ | identical, confirmed | the host scalar is not a record |
| BRG-ROBIN-P1, P2 | canonical transform and complete reduction | CLMS 2007 (PAPER-0563); Vojak 2020 [theorem] | identical, confirmed | cite them |
| BRG-ROBIN-P3 | existence of a canonical violator | Akbary–Friggstad 2009 [theorem] | host statement weaker, confirmed | stronger reductions exist |
| BRG-ROBIN-P9 | OPEN_CUTS Sec. 2 | Robin 1984 (PAPER-0206), Thm 1 [theorem] | equivalent reformulation, confirmed | Sec. 2 is equivalent to RH |
| BRG-SHARP_NATIVE-P8 | L-101220 Dickman semigroup | Tao 2010 [theorem] | equivalent reformulation, confirmed | cite it |
| BRG-SHARP_NATIVE-P10 | least-prime recursion | Buchstab 1937 [theorem] | equivalent reformulation, confirmed with correction | cite it |
| BRG-XI_PICK-P1 | RH-necessity interface | Lagarias 1999 (PAPER-0661) [theorem] | identical, confirmed with correction | scalar interface only |
| BRG-XI_PICK-P4, P7 | safe-axis matrix and the all-order criterion | Audenaert 2011 [theorem]; Sra arXiv:2611.02944 [unrefereed] | special case / equivalent reformulation, confirmed with correction | the order-3 factorisation is not in Audenaert |

### 4.2 Obstructions that bind host open cuts

- **BRG-FAMILIES-O1, O2, O3.**
  - A functional equation without an Euler product does not force RH (LED-LFUN-14).
  - Family conclusions do not certify an individual member.
  - Extracting the principal member is RH-strength, because that member is ζ(s)(1 − 67^{−s}).
- **BRG-MELLIN_WAVELET-O1 and O3.**
  - Ingham's theorem obstructs eventual one-signedness of Pólya-class detectors.
  - Graded negative mass is equivalent to quasi-RH, for the detectors that have been checked.
- **BRG-OPERATORS_HEAT-O1 and O4.**
  - The barrier of Zhu's Thm 1.4: the coercive codimension K grows doubly exponentially in L.
  - The Rodgers–Tao barrier (a heuristic).
- **BRG-SHARP_NATIVE-O4 and O6.**
  - The Hildebrand threshold (a heuristic).
  - The subunit-mass limit m* ≈ 1.80207.
- **BRG-XI_PICK-O1 and O7.**
  - Strict gaps between classes of matrix-monotone functions (Hansen–Ji–Tomiyama).
  - Sra's pole obstruction.
- **BRG-ROBIN-O4.** The t-free method stalls at t = 21.

### 4.3 Connection proposals with a host consequence

- **CON-0013** (CAUSAL_EULER). Sec. 6 is equivalent to RH.
- **CON-0005** (SHARP_NATIVE O4). Counts only.
- **CON-0007** (MELLIN). θ = 3/8 + ε under 7/8.
- **CON-0003, CON-0002, CON-0004** (ROBIN). Finite ranges only.
- **CON-0024** (OPERATORS_HEAT). ξ* as a positive control.
- **CON-0030.** The host's Sec. 10 deduction is density currency.
- **C4-C** (campaign claim). The same completing-the-square lemma as the host's S_L. This is a structural analogy, not a result.

### 4.4 What the bridge does not license

- Galerkin upper sections are not lower certificates. The C4-P values sit 0.3–6% above the infimum.
- A family identity is not extraction of the principal member.
- Fixed-P61 control is not growing-prime control.
- No finite certificate is global evidence.

## 5. Negative knowledge

### 5.1 Proposals with a vocabulary_only verdict

- **CON-0022** [vocabulary_only].
  - Its parts (i)–(iii) are an equivalent reformulation of the N₀ counts in the phase variables of Siegel and Arias de Reyna.
  - Part (ii) is equivalent to the 2026 bound.
  - No constraint on R(s) follows without the open attribution lemma (iv).
  - The tests are vacuous below γ ≈ 1.6·10^5.

### 5.2 Refuted sub-claims inside corrected proposals

These sub-claims were refuted, and the corrected entries above do not contain them:
- CON-0017(c);
- CON-0020, the threshold 0.5466;
- CON-0005, the claim that failure needs c ∈ [2, 8];
- CON-0003, the cap at 2.169·10^25;
- CON-0004, the floor exp(c(log x)^{1/2});
- CON-0007(c), the novelty claim;
- CON-0011 and CON-0035, the target 0.4170 and 'degree 3 gives nothing';
- CON-0014, 'exactly circular';
- CON-0031, the 'law';
- CON-0033, the list of 'weaker' inequalities;
- CON-0036, the Bessel-decay diagonal;
- CON-0037, 'first for any GL(2)';
- CON-0010, Zhu 'certified';
- CON-0006, the comparator;
- CON-0019, the figure 0.008;
- CON-0009(c);
- CON-0016, the novelty claim;
- CON-0039, the hedged claim about EKN;
- CON-0027, the reason given for Linnik's constant;
- CON-0034, 0.7892;
- CON-0029, the 'new law';
- CON-0030(c), for n ≥ 3;
- CON-0026, a single version of Cureton–Thorner;
- CON-0002(C);
- CON-0024, the list of zeros.

### 5.3 Bridge items with relation_overstated (12)

- CAUSAL_EULER-P5 and -P11.
- FAMILIES-P6 and -P21.
- MELLIN_WAVELET-P2, -O4 and -O5.
- OPERATORS_HEAT-P8 and -O5. The premise of O5 is out of date: OpenAI claims quasi-RH.
- ROBIN-O3.
- SHARP_NATIVE-P1 and -P14.

One further warning from the CAUSAL_EULER verifier: recommended action 4 would cause a false strengthening.

### 5.4 Campaign downgrades

- **C4-H** downgraded.
- **C4-REL(2)** downgraded.
- **C4-R:** its 'corrected statement' is unestablished.
- **C5:** 'over Q no finite window suffices' is not a theorem. This affects C5-T3, OB-2c, ML-E1 and C5-A.
- **C5-OB9:** the decay law is a misquote of an upper bound; the actual decay is about exp(−c e^{2L}).
- **C2-31:** a non sequitur.
- **C2-17, C2-28:** downgraded.

### 5.5 Recurrent obstructions (abandoned_approaches Sec. 2)

- The Davenport–Heilbronn countermodel.
- Ingham 1942.
- A spectral realization alone carries no content; positivity is the content.
- Finite and density statements are not RH.

## 6. Assessment

- **Where the strong items cluster.**
  - Obstruction maps: CON-0032, CON-0030, CON-0038, CON-0014.
  - Exact exponent dictionaries: CON-0021, CON-0018, CON-0019, CON-0017.
  - The GL(2) transfer of the 2026 rank–trace device: CON-0035/0011, CON-0036/0012.
  - Exact accounting of RH inputs: CON-0006.
- **What none of them does.** No item gives any zero-free region for ζ beyond the unrefereed 2026 claims. No item advances RH.
- **Highest-value next actions.**
  1. Write T2 of CON-0032 and attempt α ≥ 2/3.
  2. Write the proofs for CON-0021 and CON-0006.
  3. Prove the GL(2) second-moment lemma for CON-0035.
  4. Re-derive the Ji transcription for CON-0038.
  5. Do a third replay for CON-0025.

