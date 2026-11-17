# Independent campaigns C1-C5: index and adjudicated outcomes

```text
Status: EXPLORATORY index (Riemann Observatory). No campaign claims anything about RH or its negation; RH is
        open. C1 and C3 completed three stages (investigator, skeptic, adjudicator), and their FINAL.md is
        authoritative. C2, C4 and C5 completed two stages (investigator, independent skeptic) and have no
        adjudication: their outcome below is the investigator report as corrected by the skeptic, with every
        downgraded claim reported at its downgraded status, and with the skeptic's own new statements labelled
        as skeptic results (not adjudicated). All three stages were AI agents.
Scope: the five campaigns under proposals/independent_campaigns/: C1 detection horizons, C2 countermodel zoo,
        C3 failure anatomy, C4 Weil-window locality, C5 function-field transfer.
Exact sources or dependencies: C1-detection-horizons/{FINAL,REPORT,SKEPTIC_REVIEW}.md;
        C2-countermodel-zoo/{REPORT,SKEPTIC_REVIEW}.md; C3-failure-anatomy/{FINAL,REPORT,SKEPTIC_REVIEW}.md;
        C4-weil-window-locality/{REPORT,SKEPTIC_REVIEW}.md; C5-function-field-transfer/{REPORT,SKEPTIC_REVIEW}.md;
        code in ../../experiments/code/<campaign>/ and outputs in ../../experiments/results/<campaign>/.
What was actually run: reading of the files listed; no campaign computation was re-run for this index; the two
        cross-campaign numbers in Section 3 (T^2/(4 delta^2) predictions) were recomputed with mpmath
        (scratchpad synth/checks.py).
Smallest remaining gap: C2, C4 and C5 lack an adjudication round; the items an adjudicator should settle are
        listed in Section 5. The REPORT.md files of C2, C4 and C5 were materialized from structured returns
        (tools/materialize_results.py), as their headers state.
```

## 1. Index

| Campaign | Question | Stages | Files | Code and results | Outcome in one line |
|---|---|---|---|---|---|
| C1 | What can a finite criterion computation imply, and when would a hypothetical off-line zero become visible? | investigator, skeptic, adjudicator | [FINAL](C1-detection-horizons/FINAL.md), [REPORT](C1-detection-horizons/REPORT.md), [SKEPTIC](C1-detection-horizons/SKEPTIC_REVIEW.md) | [code](../../experiments/code/C1-detection-horizons/), [results](../../experiments/results/C1-detection-horizons/) | Implication horizons are about T² for Li, Jensen and ψ/π; no published large criterion computation is informative beyond T₀ |
| C2 | Which structural properties of ζ fail to imply RH, as shown by certified RH-false relatives? | investigator, skeptic | [REPORT](C2-countermodel-zoo/REPORT.md), [SKEPTIC](C2-countermodel-zoo/SKEPTIC_REVIEW.md) | [code](../../experiments/code/C2-countermodel-zoo/), [results](../../experiments/results/C2-countermodel-zoo/) | Certified off-line zeros for Davenport-Heilbronn, Epstein and ζ₁₉; the stated blind spot is refuted by F_c, and two structural claims are downgraded to CONDITIONAL |
| C3 | How exactly did refuted conjectures and failed proofs fail? | investigator, skeptic, adjudicator | [FINAL](C3-failure-anatomy/FINAL.md), [REPORT](C3-failure-anatomy/REPORT.md), [SKEPTIC](C3-failure-anatomy/SKEPTIC_REVIEW.md) | [code](../../experiments/code/C3-failure-anatomy/), [results](../../experiments/results/C3-failure-anatomy/) | 8 complete proofs, 1 conjecture; the de Branges zero condition is a condition on S(γ_n) mod 2 |
| C4 | Which Weil windows can see an off-line zero at height T? | investigator, skeptic | [REPORT](C4-weil-window-locality/REPORT.md), [SKEPTIC](C4-weil-window-locality/SKEPTIC_REVIEW.md) | [code](../../experiments/code/C4-weil-window-locality/), [results](../../experiments/results/C4-weil-window-locality/) | The brief's Nyquist-locality heuristic is refuted for fixed δ; the replacement "locality" claims are downgraded |
| C5 | Which ingredients of the function-field proofs have number-field analogues? | investigator, skeptic | [REPORT](C5-function-field-transfer/REPORT.md), [SKEPTIC](C5-function-field-transfer/SKEPTIC_REVIEW.md) | [code](../../experiments/code/C5-function-field-transfer/), [results](../../experiments/results/C5-function-field-transfer/) | Over F_q one 2g x 2g Toeplitz form decides RH; formal axioms admit thousands of certified fakes; "no finite window over Q" is not a theorem |

## 2. Outcomes

### C1 - Detection horizons (adjudicated; FINAL.md authoritative)

**Theorems.**

- C1-L1, the Li quadruple identity.
- C1-L2: if T ≥ 100 and RH(T) holds, then λ_n > 0 for 1 ≤ n ≤ T². RH(T₀) gives n ≤ 9.00105·10²⁴, and RH(317) gives n ≤ 100489, so Johansson's rigorous λ₁, …, λ₁₀₀₀₀₀ carry no information beyond height 317. The statement is due to Oesterlé (2000, unpublished, via Voros); the campaign's proof is complete and independent, with the Rosser tails written out by the adjudicator.
- C1-N1, a Nyman-Beurling floor F = (4δ/T²)(1 + O(1/T²)) for an off-line pair, and Corollary N2.
- C1-ADJ-MONO: real-rootedness of Jensen polynomials is monotone in the degree.

**Rigorous numerics.** Farmer's X₁₀ is real-rooted for d ≤ 119 and has non-real zeros for d ≥ 120, certified by three independent Arb implementations. This corrects Farmer's printed table; the Observatory classifies it as FND-0002, verified_error (minor; the conclusion is unaffected).

**Imported horizons** (relative to T₀ = 3,000,175,332,800):

- Jensen hyperbolicity for d ≤ 9.0·10²⁴ (GORTTW).
- The Schoenfeld ψ/π bounds for x ≤ 1.10·10²⁶ (Johnston; this supersedes the investigator's 2.17·10²⁵).
- Λ ≤ 0.2 (PT21 Cor. 2). It is derived from RH up to 2.51·10¹², which refutes the investigator's sentence "de Bruijn-Newman has no finite RH-implication".

**Heuristic and sketch statements.**

- Every single-defect detection scale, at δ_max(T₀) = 0.49374: Li 1.19·10²⁷, Jensen 4.44·10²⁵, ψ/π 10^29.2, Nicolas/Robin 10^50.5, Nyman-Beurling log N 2.1·10²³.
- The Jensen-heat bridge d* ≈ T²/(2t_c).
- The de Bruijn-Newman collapse model.
- The T² log T barrier for Li, and the Nicolas implication horizon (both PROPOSITION-PROOF-SKETCH).

**Withdrawn or corrected wording.** "Possibly new" for C1-L2; "< 0.3% agreement" for the bridge (the correct figure is ≤ 1.03% over 20 comparable rows); the 4·10²³ Nyman-Beurling headline; the source of the zero-free-region constant (it is Mossinghoff-Trudgian-Yang 2022).

**Bottom line.** No published large criterion computation is informative beyond T₀, except trivially, in the formal sense, for isolated π(x) above 1.1·10²⁶.

### C2 - Countermodel zoo (skeptic-reviewed, not adjudicated)

**Certified zeros and counts.**

- Davenport-Heilbronn: 5 off-line zeros with t ≤ 300. The skeptic's rigorous count, 214 = 204 + 2·5, makes the list complete, and 85.70 is rigorously the lowest height.
- Epstein x² + 5y²: 35 off-line zeros with t ≤ 200, complete by the count 253 = 183 + 2·35, the lowest at height 15.67. It also has certified zeros with Re s > 1, already at t ≈ 1193.9 (skeptic F4, correcting the investigator's "first near 3.6·10⁶").
- ζ₁₉ has a certified zero with Re s = 1.0010955… at t ≈ 600884.2.
- Elementary right edges: DH has no zeros for Re s ≥ 1.13514; the Epstein function has none for Re s ≥ 1.17816.

**A refutation.** The claim of Liu and Wu (arXiv:2503.24275) that all Davenport-Heilbronn zeros lie on the line is refuted. Their step divides 0 by 0 at common zeros. The skeptic supplied an independent winding-number witness, so the methodology's requirement for public wording is met.

**Accepted as stated.**

- The meta-lemma C2-24 (THEOREM, elementary).
- The continuous Beurling toy C2-21 (THEOREM).
- The synthetic ξ̃ construction C2-15 (THEOREM).

**Downgraded or corrected by the skeptic.**

- C2-17 and C2-28: the "uniform in d" Jensen statement for ξ̃ is CONDITIONAL on RH (F2). It can be rebased on H_{0.2}.
- C2-31: the hitting-set corollary becomes a protocol heuristic. The stated blind spot, "no known RH-false function has a Dirichlet series over N, an Euler product and a self-dual functional equation", is refuted by F_c(s) = ζ(s)(1 + c·2^{−s} + 2·4^{−s}), which only the Selberg-class local condition excludes (F1).
- C2-16: the Li table is numerically wrong (F3). The first failing indices are 20855, 7477, 112538 and 40908, not 20857, 7395, 112929 and 41098.
- C2-14: its premise is the Csordas-Varga theorem (F5), so Turán inequalities for every H_t become a THEOREM, modulo the moment lemma at p = −1/2.
- Side finding (F7): Betermin-Samaj-Travenec's Conjecture 1.1 is false by a relative 4.2·10⁻²⁰.

### C3 - Failure anatomy (adjudicated; FINAL.md authoritative)

**Theorems with complete proofs** (eight in all):

- C3-A1: Atiyah's identity forces the Todd-type function to be constant.
- C3-Q1: Queme's boundary termwise limit is illegitimate.
- C3-M1: an explicit counterexample to Micheas' Theorem 1.
- C3-O1 and C3-ADJ-O2: Oliva's step (3) holds for every prime 5 ≤ p ≤ 1.39·10¹⁷, fails for some prime p < e^{727.951332668}, and fails infinitely often.
- C3-CG1: a computer-assisted counterexample to Cheng-Graham's Lemma 2, already corrected in print.
- C3-ADJ-S: the de Branges zero condition at the n-th zero is exactly S(γ_n) − δ(γ_n) ∉ (3/4, 7/4) mod 2.
- The identity in the C3-D1 scan.

**Rigorous numerics.** 15,567 failures of the de Branges condition among the first 10⁵ zeros, counted by three implementations where they overlap; M(7766842813) = 50286.

**One conjecture.** C3-ADJ-RATE: the failure proportion tends to 1/2. It is supported by Arb-certified 1000-zero blocks up to n₀ = 10¹⁰, with rates rising from 0.08 to 0.22.

**What changed in adjudication.** No investigator claim is refuted. One mechanism sentence ("phase-locking with no arithmetic reason") is withdrawn, and one bibliographic note is corrected: Atiyah's companion was published as Atiyah-Kouneiher 2019.

**Heuristic outputs.** The failure taxonomy F1-F15 and the 20-item checklist (item 13 rewritten) are HEURISTIC. They are reproduced, with lessons, in ../../history/abandoned_approaches.md §20.

**Gaps left.** arXiv:0807.0090 v5-v10 and de Branges' post-2004 manuscripts are unaudited.

### C4 - Weil-window locality (skeptic-reviewed, not adjudicated)

**Upheld proofs** (re-derived by the skeptic).

- C4-C: the exact detection criterion, a standard Schur-Sylvester argument and the zeros-side counterpart of the host's S_L.
- C4-LAT: an exact two-regime law in the lattice model. The aside on the mirror pair is wrong, but it lies outside the theorem and is easily repaired.
- C4-B: under the single-defect hypothesis H1, a window of length L_B = (1/(2δ))(log log T + log log log T + O_δ(1)) detects the defect. Two corrections: the asymptotic coefficient is 0.704L, not 1.407L, and at T = 3·10¹² the rigorous window beats Nyquist only for δ ≥ 0.2354.
- C4-BL: conditional blindness under hypothesis R. Correct, but close to tautological.

**REFUTED.** The brief's heuristic that a window is blind for T ≫ 2πe^{2L}, up to O(log 1/δ), fails for every fixed δ.

**Downgraded.**

- The investigator's corrected form of that heuristic (Nyquist locality for κ < 2.18) is not established, and the collision model contradicts it: near-line defects are detected 0.42-0.85 below L_N at T ≈ 10⁴.
- C4-H, the two-regime law with its conjecture, is downgraded.
- C4-REL, which claimed that host window families must reach L ≈ L_N, is downgraded to a question.

**Corrected numerics.** The window-profile values (C4-P) are Rayleigh-Ritz upper bounds 0.3-6% above the infimum; they replicate Zhu's Table 1, so at most 2-3 digits are meaningful. All detection thresholds are upper bounds on L*.

**Missed prior art.** Danesh (arXiv:2611.10726), which uses the same e^{δx} mechanism.

### C5 - Function-field transfer (skeptic-reviewed, not adjudicated)

**Upheld theorems** (no claim refuted).

- C5-L0 (the parametrisation of curve-type polynomials); C5-L1; C5-L2 (a mod-2 / big-Witt criterion).
- C5-T1: both of Weil's proofs feed one Gram matrix.
- C5-T2: RH(C) ⇔ T_N ⪰ 0 for all N ⇔ the Hasse-Weil bound for all k.
- C5-T3: an inertia theorem, so RH(C) ⇔ T_{2g} ⪰ 0. The skeptic proved a confluent version, so squarefreeness is unnecessary.
- C5-S1 (half of Stepanov would suffice over Q) and C5-D1 (the tensor-power trick in number-field form is RH-equivalent).

**Rigorous numerics.**

- The census of fake curve zeta functions: rational, satisfying the functional equation, with a nonnegative integral Euler product, and RH-false. It counts 16,354 admissible and 12,787 fakes over 24 pairs (q,g); if the degenerate Z ≡ 1 is counted, 16,368 and 12,801.
- Realisations of fakes as quadratic-type Euler products over P¹.
- Exact inertia checks on 3,300 cases.

**Corrections by the skeptic.**

- "Over Q no finite window suffices", stated in four places, is not a theorem: it is a logical error.
- OB-9 inverts Zhu's RH-conditional upper bound. The actual decay is exp(−c e^{2L}).
- OB-6 overstates Pritsker: fixed weights are excluded, weight sequences are open.
- The 41 "undecided" census cases are non-admissible.
- The phenomenon has prior art in arithmetical semigroups and Ihara zeta functions.

**New skeptic theorems.** The confluent inertia theorem, and the asymmetry of one-sided Hasse-Weil bounds. The window criterion without RH is a PROPOSITION-PROOF-SKETCH.

**Open targets** (CONJECTURE labels, mostly RH-equivalent or model cases). ML-W0 (Riemann-Roch on the square of the scaling site, re-deriving Yoshida positivity), ML-C1 (semilocal positivity at λ² = 3, whose content is the mechanism), ML-E1, ML-Den, ML-TP, ML-F1 and ML-S.

## 3. Cross-campaign observations (Observatory-proposed)

- **Jensen-heat bridge versus the zoo (C1 and C2).**
  - C1's isolated-pair prediction d* ≈ T²/(4δ²) gives 39.06 for the injected quadruple at 0.9 + 5i.
  - C2 found the first non-hyperbolic J^{d,0}(ξ̃) at exactly d = 40 (C2-17 and the skeptic's replay; NUMERICAL-NONRIGOROUS).
  - The predictions for the three undetected quadruples, 625, 400 and 306, all exceed C2's scan limit of 240.
  - This is a consistency check of a HEURISTIC, not a validation. A certified test is AC-15 in [actionable_conjectures](../actionable_conjectures.md).
- **Two kinds of horizon (C1 and C4).**
  - Index criteria disperse information: Li needs n of order T²/δ, and Jensen needs d of order T²/(2t_c).
  - A Weil window sees large-δ defects at L ≈ (1/(2δ)) log log T (C4-B, under H1) but near-line defects only near L_N = (1/2) log(T/2π) (numerical upper bounds; blindness unproved).
  - Both are single-defect model statements.
- **Finite windows (C4 and C5).** Over F_q one window of half-width just above (g − 1/2) log q decides RH (C5 skeptic §3.2, sketch). Over Q, λ_min(L) decays doubly exponentially, and no finite-rank mechanism is known. That is the quantitative trace of "infinite genus" (C5-OB2, OB-9 as corrected).
- **Countermodel tests (C2 and C3).** C3's checklist items 2-3 (run each step on Davenport-Heilbronn, ζ₁₉ and Epstein; mark where Re ρ ≠ 1/2 is used) are executable with C2's certified zeros. Direction D-08 proposes mechanising them.

## 4. Where the campaigns feed

| Campaign | Ranked directions ([file](../ranked_research_directions.md)) | Actionable statements ([file](../actionable_conjectures.md)) |
|---|---|---|
| C1 | D-15, D-17, D-25, D-29, D-34 | AC-14, AC-15, AC-16, AC-17 |
| C2 | D-08, D-26 | AC-15, AC-27, AC-28 |
| C3 | D-08, D-32 | AC-18 |
| C4 | D-16, D-33 | AC-19, AC-20 |
| C5 | D-16, D-23, D-28, D-35 | AC-21, AC-22, AC-23 |

## 5. Open process items

**C2 adjudication.** Settle:

- F1: add member M10 and rewrite C2-00(i) and C2-31.
- F2: relabel C2-17 and C2-28 as CONDITIONAL, or rebase them on H_{0.2}.
- F3: replace the C2-16 table.
- F4: update SP-8 and matrix row M2.
- F5: confirm that the moment lemma covers p = −1/2.
- F6: upgrade C2-04 and C2-09 to rigorous completeness.
- F7: decide whether to record the BST finding publicly.

**C4 adjudication.** Settle:

- the final status of C4-H and C4-REL;
- the corrected asymptotic coefficient in C4-B;
- the restriction of the C4-R "corrected statement";
- citations of Zhu's Table 1 and of Danesh.

**C5 adjudication.** Settle:

- the logical correction "no finite window over Q" (C5-T3, OB-2c, ML-E1, C5-A);
- the decay law in OB-9;
- the census conventions (the degenerate Z ≡ 1);
- prior-art citations for E1 and OB-5;
- the confluent form of C5-T3.

**C1 and C3 next steps** are listed in their FINAL.md §8 and §9. In particular: the Nicolas implication theorem, the Jensen-heat comparison lemma, the de Branges positive-proportion theorem, and an audit of arXiv:0807.0090 v5-v10.

