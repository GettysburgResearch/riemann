# Level-2 audit F5-connes-thm5

```text
Status: AUDIT (Level 2; adjudicated where flagged)
Scope: the specific issue named below, not the whole paper
Exact sources or dependencies: see 'Sources checked'
What was actually run: independent reading and recomputation by an auditor agent; independent two-sided adjudication where the auditor flagged an issue
Smallest remaining gap: see adjudication
```

**Target.** F5-connes-thm5: A. Connes, "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function", Selecta Math. (N.S.) 5 (1999) 29-106; arXiv:math/9811068v1 (only arXiv version), Theorem 5 (Sec. VIII) versus the abstract/introduction claim and the number-field paragraph of Sec. VIII

**Auditor classification.** `correct_but_misinterpreted`

**Final classification.** `correct_but_misinterpreted`

**Summary.** I found no issue in Theorem 5 as stated. It is restricted to global fields of positive characteristic, and there it is also unconditional, because RH there is Weil's theorem. For number fields the paper proves four things: the δ-Sobolev spectral realization of the critical zeros only (Thm 1, Cor 2), the local trace formula (Thm 3), the S-local trace formula (Thm 4) and the explicit-formula check (Thm 6). The global "trace formula ⇔ RH" for k = Q is only sketched, in one paragraph built on prolate functions ("This gives the analogue of Lemma 1, Theorem 5, and Lemma 3", p. 47), with no statement and no proof. Theorem 5's literal formulation does not carry over: for any number field its subspace B_Λ is {0}, so condition (a) fails whatever the truth of RH. The paper's abstract and introduction state the equivalence without the positive-characteristic qualifier. Later citations split three ways: careful (Bombieri, Deitmar, Meyer, Watkins, Connes 2000/2015/2019/2021); author self-summaries that drop the scope (Connes–Marcolli 2006, Connes–Consani–Marcolli 2007, Connes 2026); and third-party statements that turn it into a proved equivalence for classical RH (Wikipedia's Hilbert–Pólya page, Khalkhali). One citation is plainly wrong: Tamburini 2025 says "Connes' trace formula therefore applies and forces every ... zero ... to lie on the critical line", and nothing of the kind is in Connes 1999.

**Witness / evidence.** (W1, the literal Theorem 5 does not carry over to number fields; derived independently here.) Take k = Q and f in S(A_Q). Write f = Σ_j g_j ⊗ 1_{U_j} with U_j disjoint compact-open subsets of A_f and g_j in S(R). Each U_j contains finite ideles x_f. The condition f(x) = 0 whenever |x| > Λ, applied at x = (x_∞, x_f), makes every g_j compactly supported. The same argument applied to f-hat gives compactly supported functions h_k, and each ĝ_j is a linear combination of them (the Fourier transforms of the indicators 1_{U_j} are linearly independent), so each ĝ_j is compactly supported. By Paley–Wiener, g_j = 0. So the subspace B_Λ in Theorem 5 is {0} for k = Q, and the same holds for any field with an archimedean place. Then Trace(Q_Λ U(h)) = 0, while the right-hand side of (a) contains 2h(1)·log'Λ, which tends to infinity when h(1) ≠ 0. Condition (a) therefore fails regardless of RH. Corroboration: Connes himself writes (p. 46) "when v is an Archimedean place there exists no non-zero function on k_v which vanishes as well as its Fourier transform for |x| > Λ". Watkins, "Notes on Connes and RH" (2007), p. 13, writes: "Indeed, B Λ ≡ 0, and the trace formula is false in the form given above ... Although Connes does not list the details". Theorem 5 opens with "Let k be a global field of positive characteritic" (p. 42, in arXiv v1 and in the version on Connes's website). The number-field passage, for k = Q only and restricted to even functions, ends with "This gives the analogue of Lemma 1, Theorem 5, and Lemma 3" (p. 47) and contains no proof. Connes 2000 (math/0011193, p. 56) restricts the corresponding Theorem 11 to function fields "to simplify ... This allows for a straightforward definition of the cutoff operators Q_Λ". (Misinterpretation instance.) Tamburini, arXiv:2503.09644v3 (2025-07-22), p. 41: "Because these conditions hold, (A, H, D) is a bona-fide spectral triple; Connes' trace formula therefore applies and forces every spectral line of D–hence every non-trivial zero of the Riemann zeta function–to lie on the critical line and to be simple", citing [55] = Connes 1999. Connes 1999 has no theorem of this kind. For number fields the global formula is unproved, and Connes 2026 (arXiv:2602.04022, p. 18) calls it "a conjecture". Further instances, with quotes, are in the report. (Numerical checks.) The limit in eq. (29) of the Lemma 3 proof (Poisson kernel / harmonic measure) agreed to 6 digits for single and multiple off-circle points. The Landau–Pollak–Slepian description on p. 46–47 was confirmed: #eigenvalues > 1/2 equals 4Λ² for Λ = 2, 3, 4, 6, 8, and the transition region grows slowly. The dimension count in Lemma 1 / eq. (12) was checked by hand.

**Sources checked.**
- arXiv:math/9811068v1 full text (Connes 1999) — abstract p.1, intro p.3, Thm 1 p.13, Thm 4 p.31, Sec. VIII pp.37-50, Thm 5 p.42, Lemma 3 p.44, number-field paragraph pp.45-47
- alainconnes.org/wp-content/uploads/selecta.ps-2.pdf (Connes website version; same Thm 5 hypothesis and intro wording)
- arXiv API metadata for math/9811068 (single version v1, 1998-11-10)
- arXiv:math/0011193 Connes, Noncommutative Geometry Year 2000, p.56-57 (Thm 11 restricted to function fields)
- arXiv:1509.05576 Connes, An essay on the Riemann Hypothesis (2015), pp.12-15
- arXiv:1910.14368 Connes-Consani, The Scaling Hamiltonian (2019), intro
- arXiv:2006.13771 Connes-Consani, Weil positivity and trace formula, the archimedean place (2020), intro
- arXiv:2106.01715 Connes-Consani, Spectral triples and zeta-cycles (2021), p.4
- arXiv:2310.18423 Connes-Consani-Moscovici, Zeta zeros and prolate wave operators, intro
- arXiv:2602.04022 Connes, The Riemann Hypothesis: Past, Present and a Letter Through Time (2026), sec. 3.5.1 p.18
- arXiv:2611.13129 Andrews-Connes-La Gatta (2026) references
- arXiv:math/0512138v2 Connes-Consani-Marcolli, NCG and motives: thermodynamics of endomotives, sec. 5.2 p.40
- arXiv:math/0703392 Connes-Consani-Marcolli, The Weil proof and the geometry of the adeles class space, p.2-4, Prop 7.2
- arXiv:math/0601054 Connes-Marcolli, A walk in the noncommutative garden, p.89
- arXiv:math/0311468v3 R. Meyer (Duke 2005), p.2
- arXiv:math/0111108v2 A. Deitmar, A semi-local trace identity and RH for function fields, pp.2,9,16
- Mark Watkins, Notes on Connes and RH (magma.maths.usyd.edu.au/~watkins/papers/connes.pdf, 2007), pp.1,12-13
- E. Bombieri, Clay official problem description (claymath.org riemann.pdf), p.10
- M. Khalkhali, What is new with Connes' approach to the Riemann hypothesis? (math.uwo.ca TehProg.pdf), p.3
- Wikipedia: Hilbert-Polya conjecture, section Later developments (retrieved 2026-11-17)
- Wikipedia: Riemann hypothesis, section Noncommutative geometry (retrieved 2026-11-17)
- arXiv:2503.09644v3 F. Tamburini (2025), pp.41-42, ref [55]
- arXiv:1410.1214 M. Wolf, Will a physicist prove the Riemann Hypothesis?, p.19
- arXiv:1707.01770v2 R. Perez-Marco, Notes on the Riemann Hypothesis, p.22
- arXiv:1101.3116 Schumayer-Hutchinson, Physics of the Riemann Hypothesis (RMP 2011)
- arXiv:1601.01797 G. Sierra (2016/2019)
- arXiv:0805.4079 Sierra-Townsend, Landau levels and Riemann zeros
- arXiv:quant-ph/0407167 Ahmed-Jain (2004)
- arXiv:math/0409520 Marcolli lectures
- arXiv:1608.03679 Bender-Brody-Mueller
- arXiv:math/0112254 Burnol; arXiv:1012.4665 Planat-Sole-Omar; arXiv:1006.4810 Connes-Consani; arXiv:math/0510572 Sierra; arXiv:1710.01558; arXiv:math/0001013 Burnol (no relevant attribution found)
- Not accessible: Conrey Notices AMS 2003 (HTTP 403), Connes-Marcolli AMS book (not fetched, copyright), Lapidus 2008 book
- Scratch scripts: /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/f5scripts/lemma3_check.py and /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/f5scripts/prolate_check.py

## Auditor report

# L2 audit F5: Connes (1999), Theorem 5 versus the number-field reading

**Target.** A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. (N.S.) 5 (1999) 29–106. arXiv:math/9811068 has only v1 (1998-11-10). The version on Connes's own website (selecta.ps-2.pdf) has the same Theorem 5 hypothesis and the same introduction wording. Page numbers below are from arXiv v1.

**Classification.** `correct_but_misinterpreted`. I found no issue in Theorem 5 as stated. The abstract and introduction state the result without its scope, and several later citations, including some by the author, read it as a proved equivalence for number fields or for classical RH.

---

## 1. What the paper proves, by field type

| Object | Location | Field type | Status in the paper |
|---|---|---|---|
| Thm 1: spectral realization on the cokernel H of E: L²_δ(X)_0 → L²_δ(C_k), δ > 1 | III, p.13; proof in App. I ("We only treat the case of number fields") | **number fields** (p.14: "similar formulation" in char > 0) | Proved. Only **critical** zeros appear, and their multiplicity is capped at the largest n < (1+δ)/2. Non-critical zeros are invisible. |
| Cor 2 (III): trace of W(h) on H | p.14 | any characteristic | Proved, with the δ-capped multiplicity. |
| Sec. VI: character of U on L²(X) | pp.~25–28 | general | **Formal** computation only (p.2: "formal computation"). |
| Thm 3: local trace formula, K* on L²(K) | V | any local field, including ℝ and ℂ | Proved. |
| Thm 4: S-local trace formula with cutoff R_Λ = P̂_Λ P_Λ | VII, p.31 | **any global field**, S finite, containing the infinite places | Proved. |
| Thm 6: Weil explicit formula rewriting | App. II | general | Proved (a check). |
| Lemma 1, Cor 2 (VIII), **Thm 5**, Lemma 3 | VIII, pp.39–44 | **positive characteristic only** ("We shall first concentrate on the case of positive characteristic", p.38; Thm 5: "Let k be a global field of positive characteritic", p.42) | Proved, with two "requires more care" steps elided (χ = 1 in Lemma 1; multiple points of F in Lemma 3). Since (b) is Weil's theorem, Theorem 5 also gives the global trace formula (a) **unconditionally** in positive characteristic. Connes notes this (p.42). |
| Number-field analogue | VIII, pp.45–47 | **k = ℚ only**, χ = 1, even functions | **Sketch.** B_Λ is replaced by the span of prolate functions ψ_n, n ≤ 4Λ², tensored with 1_R. The paragraph ends: "This gives the analogue of Lemma 1, Theorem 5, and Lemma 3." There is no statement of the analogue and no proof. |

Even in positive characteristic, a direct proof of (16) is not given: "We can prove directly that (16) holds when h is supported by C_{k,1} but are not able to prove (16) directly for arbitrary h" (p.42).

**Source-level presentation.**
- Abstract (p.1): "This reduces the Riemann hypothesis to the validity of the trace formula."
- Introduction (p.3): "in the global case is left open and shown (Theorem 5 of section VIII) to be equivalent to the validity of the Riemann Hypothesis for all L functions with Grössencharakter."

Neither sentence carries the positive-characteristic hypothesis of Theorem 5. Minor typo: "characteritic" in the statement of Theorem 5 (present in both versions).

## 2. Witness W1: Theorem 5's formulation does not transport to number fields

**Claim.** For k = ℚ, and for any number field, the subspace B_Λ used in Theorem 5 is {0}. Here B_Λ is the span of f ∈ S(A) with f(x) = f̂(x) = 0 for |x| > Λ.

**Proof** (re-derived independently here).
1. Write f = Σ_j g_j ⊗ 1_{U_j}, with U_j disjoint compact-open subsets of A_f and g_j ∈ S(ℝ).
2. Each U_j contains finite ideles x_f. At points (x_∞, x_f) with x_f in U_j, the vanishing condition gives g_j(x_∞) = 0 once |x_∞| > Λ/|x_f|. So every g_j has compact support.
3. f̂ = Σ_j ĝ_j ⊗ 1̂_{U_j}, and the functions 1̂_{U_j} are linearly independent. Re-expanding f̂ over a disjoint compact-open partition and applying step 2 shows that each ĝ_j is a linear combination of compactly supported functions. So each ĝ_j has compact support.
4. By Paley–Wiener, g_j = 0.

**Consequence.** Trace(Q_Λ U(h)) = 0. The right-hand side of (a) contains 2h(1)·log′Λ, which tends to infinity when h(1) ≠ 0. So (a) fails for every number field, whatever the truth of RH. Read literally for number fields, Theorem 5 would therefore "imply" that GRH is false, which is absurd. So the theorem cannot be read as a number-field statement. The number-field version needs a different, approximate B_Λ (the prolate span), and the paper gives that only as a sketch.

**Corroboration.**
- Connes, p.46: "when v is an Archimedean place there exists no non-zero function on k_v which vanishes as well as its Fourier transform for |x| > Λ."
- M. Watkins, *Notes on Connes and RH* (2007), p.13: "In the number field case ... Indeed, B Λ ≡ 0, and the trace formula is false in the form given above ... Although Connes does not list the details, for the (real) infinite places we should be able to take ... the span of the eigenfunctions ψn for n ≤ 4Λ² and make it work." His p.1: "In the number field case, there are more difficulties, but the equivalence ... can likely be established."
- Connes 2000 (arXiv:math/0011193, p.56): "we shall replace the number field k by a function field of positive characteristic. This allows for a straightforward definition of the cutoff operators QΛ". The equivalence there (Thm 11) is stated for function fields only.

This is **not** an error in Connes: he scopes Theorem 5 correctly and flags the archimedean obstruction. It shows that the scope-free sentences in the abstract and introduction, and in later citations, outrun what is proved.

## 3. Independent checks

- **Lemma 3, eq. (29).** I checked numerically that Trace((S_N − E_N)V(f)) tends to Σ_z ∫ P_z f̂, the Poisson-kernel (harmonic-measure) limit. Cases: one point off the circle, |z| = 1.3 and |z| = 0.8, agree to 6 digits at N = 20. Three distinct points agree to 6 digits at N = 60. One point on the circle converges as O(1/N) to the Dirac mass (1.8203, 1.8304, 1.8341 → 1.8356). This confirms that off-line zeros enter only through harmonic measure ("resonances"). Script: `/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/f5scripts/lemma3_check.py`.
- **Lemma 1 counting.** #{m : −N − (2 − 2g − f) ≤ m ≤ N} · l = (2N+1)l − fl + (2−2g)l, which matches eq. (12).
- **Prolate description, pp.46–47.** Nyström eigenvalues of P_Λ P̂_Λ P_Λ: #eigenvalues > 1/2 equals 4Λ² exactly for Λ = 2, 3, 4, 6, 8; the trace equals 4Λ²; the number of eigenvalues in (0.01, 0.99) is 6, 6, 6, 8, 8, a slow (consistent with logarithmic) growth. So Connes's description is accurate. Script: `/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/f5scripts/prolate_check.py`.
- **A doubt I raised and withdrew.** I first suspected that the O(log Λ) ambiguity in the prolate cutoff index makes the number-field formula ill-defined at o(1) precision. A semiclassical estimate suggests that transition-region states contribute only O(Λ⁻²) each for fixed smooth h, so this is **not** asserted as a defect.

## 4. Citation survey: correct versus incorrect attributions

### A. Accurate or carefully scoped
1. **Bombieri, Clay official problem description, p.10:** "the papers [Conn], [Den], [Hara] offer glimpses of a possible setup for these basic problems." No overclaim.
2. **Deitmar, arXiv:math/0111108v2 (2002), pp.2, 9.** The paper works explicitly in positive characteristic ("Let k be a global field of positive characteristic ... recall Connes' result"). It states that the global formula "can as yet only be proved as a consequence of the Riemann hypothesis".
3. **R. Meyer, Duke 127 (2005), arXiv:math/0311468v3, p.2:** "a geometric computation of the character in Connes' situation is therefore equivalent to the Generalized Riemann Hypothesis. Since I have not been able to do this computation, I have developed an alternative spectral interpretation". This correctly treats the equivalence as coming via Weil's explicit formula, not as a result Connes proved.
4. **Watkins (2007).** Scoped exactly; see §2.
5. **Connes–Consani–Marcolli, arXiv:math/0703392, p.2:** "In [10] the analytic setting is that of Hilbert spaces ... but the spectral realization only involves the critical zeros." Accurate.
6. **Author statements that are precise:**
   - Connes 2000 (function-field Thm 11).
   - Connes, *Essay* (arXiv:1509.05576), pp.12–13: "only sees the zeros which are on the critical line and where the value of δ artificially cuts the multiplicities".
   - Connes–Consani, *The Scaling Hamiltonian* (arXiv:1910.14368): "the construction of a global Hilbert space spectral realization remained artificial by the use of Sobolev spaces"; "the semi-local trace formula proved in [10]".
   - Connes–Consani, arXiv:2106.01715, p.4: "ad-hoc Sobolev spaces used in [3] to provide the spectral realization".
7. **M. Wolf, arXiv:1410.1214, p.19:** "Connes constructed a quantum system that has energy levels corresponding to all the Riemann zeros that lie on the critical line." Accurate for Thm 1, though it omits the δ multiplicity cap. Schumayer–Hutchinson (RMP 2011) and Sierra–Townsend describe the absorption picture neutrally.

### B. Author self-summaries that drop the scope
These are not third-party misreadings. They repeat the introduction's wording without its scope.

8. **Connes–Marcolli, *A walk in the noncommutative garden*, arXiv:math/0601054, p.89:** "Finally it was shown in [64] that the generalized Riemann hypothesis is equivalent to the validity of a global trace formula".
9. **Connes–Consani–Marcolli, arXiv:math/0512138v2 (Adv. Math. 2007), §5.2, p.40:** "It is then shown in [14] that, in the Hilbert space context, the global trace formula is in fact equivalent to the Riemann hypothesis for all L-functions with Grössencharakter." The surrounding section treats a general global field K.
10. **Connes 2026, arXiv:2602.04022, §3.5.1, p.18:** "In the beginning the trace formula was stated for general global fields as a conjecture equivalent to the validity of the analogue of RH for all L-functions with Grössencharakter". This correctly calls the global formula a *conjecture*, but keeps the "general global fields" equivalence framing.

### C. Third-party statements that overstate the proved scope
11. **Wikipedia, *Hilbert–Pólya conjecture*, section "Later developments" (retrieved 2026-11-17):** "In 1998, Alain Connes formulated a trace formula that is actually equivalent to the Riemann hypothesis." This presents as established an equivalence with classical RH. The proved equivalence (Thm 5) is for function fields only.
12. **M. Khalkhali, *What is new with Connes' approach to the Riemann hypothesis?* (c. 2006, math.uwo.ca), p.3:** "Connes' trace formula was shown to be equivalent to the Riemann hypothesis and its generalizations by Connes". Unscoped, in a passage about the characteristic-zero program.
13. **Milder, following the abstract's wording:**
   - Wikipedia, *Riemann hypothesis*, section "Noncommutative geometry" (retrieved 2026-11-17): Connes "showed that a suitable analog of the Selberg trace formula ... would imply the Riemann hypothesis". For number fields this "showed" rests on the p.47 sketch.
   - Pérez-Marco, arXiv:1707.01770v2, p.22: "Connes reduced the Riemann Hypothesis to the proof of a trace formula."
   - Wolf, arXiv:1410.1214, p.19: "he has shifted the problem of proving the RH to equally difficult problem of the validity of a certain trace formula" (reported as "common opinion").

### D. Incorrect citations
14. **F. Tamburini, arXiv:2503.09644v3 (math.GM, 2025-07-22), p.41**, citing [55] = Connes 1999: "Because these conditions hold, (A, H, D) is a bona-fide spectral triple; Connes' trace formula therefore applies and forces every spectral line of D–hence every non-trivial zero of the Riemann zeta function–to lie on the critical line and to be simple." Connes 1999 contains no theorem that a spectral triple satisfying the axioms has a trace formula forcing zeros onto the critical line, nor anything about simplicity of zeros. For ℚ the global trace formula is unproved: p.47 is a sketch, and Connes 2026 calls it "a conjecture". The attribution is unsupported by the cited source. This finding concerns the attribution only; the rest of that paper was not audited.
15. **Ahmed–Jain, arXiv:quant-ph/0407167, p.1 (minor, tangential):** "Connes [2] who constructed a classical eigenvalue problem with a Perron-Frobenius operator". There is no Perron–Frobenius operator in Connes 1999. The phrase "presented a spectral interpretation of Riemann zeros" in the same sentence is accurate.

**I found no instance attributing to Connes a proved *spectral realization of all zeros* for number fields.** Citations of the spectral realization are generally accurate. The all-zeros realization is correctly credited to Meyer (2005) and to Connes–Consani–Marcolli.

## 5. Classification rationale and boundaries

- **Theorem 5 is correct as stated**, with two elided "more care" steps that I did not reconstruct.
- **The abstract and introduction omit its positive-characteristic scope.** This is a presentation issue in the source.
- **The number-field analogue is only sketched**, and the theorem's literal form fails there (W1). The author acknowledges this obstruction on p.46.
- **Misinterpretation instances are concrete**: items 11, 12 and 14. Items 8–10 are unscoped self-summaries by the author.
- **Not classified `verified_error`.** No author error was found, and nothing here should be read as calling Connes's work erroneous.
- **Not classified `suspected_gap`.** The number-field claim is openly a sketch ("analogue"), not a purported proof. If the Observatory wants to record "the abstract/intro reduction of classical RH is not proved in the paper" as a separate item, the right classification for that sub-item is `typo_or_presentation` or `unresolved_ambiguity` for the number-field formulation, and it would need adjudication.

**Not inspected or not replayed:**
- Conrey, Notices AMS 2003 (HTTP 403).
- The Connes–Marcolli AMS book, chapter 2 (not fetched).
- Lapidus (2008).
- The full proofs of Thm 1 (Appendix I) and Thm 4 (Sec. VII), which I did not re-derive.
- The elided χ = 1 case of Lemma 1.

**Smallest statement whose failure would overturn this classification:** "Connes 1999 contains no proved statement of the global trace formula ⇔ GRH equivalence for any number field." It would be overturned if a precise number-field version with proof were located in the published Selecta text (I checked the website version) or in an erratum. No erratum was found.


