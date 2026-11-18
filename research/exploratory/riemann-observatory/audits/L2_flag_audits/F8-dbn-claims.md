# Level-2 audit F8-dbn-claims

```text
Status: AUDIT (Level 2; adjudicated where flagged)
Scope: the specific issue named below, not the whole paper
Exact sources or dependencies: see 'Sources checked'
What was actually run: independent reading and recomputation by an auditor agent; independent two-sided adjudication where the auditor flagged an issue
Smallest remaining gap: see adjudication
```

**Target.** F8-dbn-claims: 2024-2026 upper-bound claims for the de Bruijn-Newman constant below Platt-Trudgian's 0.2. Principal object: Planat-Raymond, arXiv:2611.06245v1 (4 Nov 2026), claim Λ < 0.156821. The other 2026 reports are classified by status.

**Auditor classification.** `no_issue_found_in_inspected_portion`

**Final classification.** `no_issue_found_in_inspected_portion`

**Summary.** Planat-Raymond (arXiv:2611.06245v1) claims Λ < 156821/10^6 in the Polymath normalisation. They prove it by excluding real double zeros of H_t for every real x and every t in [0.156821, 1/5]. This replaces Polymath's complex canopy and its y0²/2 penalty. The proof uses the same RH height as Platt-Trudgian (T_PT = 3,000,175,332,800), a new stationary separator at X = 6,000,000,185,827, five 4-prime Gram/stability certificates on [X, W = 7.24e13], and an Euler-product differential barrier for x ≥ W. The external inputs are Polymath Thm 1.3, Thm 3.2 and Thm 1.5(i), and Platt-Trudgian Thm 1 and Cor. 2 (Λ ≤ 1/5).

The L2 audit checked the logical assembly, which is sound. It also re-derived the transfer of Polymath eqs. (20)-(24). I recomputed every quantity I could test independently: the exact rational gates, P11 and S1, the Cauchy-Schwarz feasibility crossing, the five Gram polynomials on the 4-torus, the five weakest-leaf recovery margins, the inverse defects, the centred moment M32, the complete Euler-tail arithmetic, and the separator on a (t,y) grid, cross-checked against mpmath zeta. All agree with the paper and none falls below a claimed floor. The separator has a large margin (grid min |f| ≈ 1.44 vs certified floor 0.01). The Gram margins sit 20 to 4000 times above their floors. The method is, however, knife-edge in t: the four-prime family fails just below t ≈ 0.1568206.

The full certificate (44,182 C++ torus boxes and 17,385 Arb rectangles) was not replayed, and the GitHub release was not retrievable here. The construction is consistent with the Polymath15 framework. It uses the same RH-height input and improves only the constant in the O(1/log T) heuristic (t·log X = 4.61 vs 5.06-5.95 for Polymath Table 1), which Polymath explicitly allows.

One inherited caveat: the upper anchor Λ ≤ 1/5 (Platt-Trudgian Cor. 2) rests entirely on Polymath Table 1 row 2. Polymath §10 describes the canopy step for that row as something one should 'expect to be able to verify', and computes the barrier mesh 'at 20 digits'. That is a documentation-level ambiguity in a refereed input, not a defect of Planat-Raymond.

None of the other 2026 claims is refereed or independently replayed. That covers Raymond 0.149396 (v1.1 erratum), Gordon 0.158, Mosaic 0.1875/0.16/0.1595, Kornaus 0.172422 (v1.1 correction), Gomila 0.1787854, Planat 0.1732 and 0.17795 (audit-relative), Planat's CA bound 0.148612 (conditional on (A1)-(A3)), Hakimoglu-Brown 0.13963 (conditional on H7/8) and Raymond 0.107965 (conditional on H7/8, though self-described as unconditional). An arXiv API query on 17 Nov 2026 found no further dBN-bound preprints after 2611.06245.

**Witness / evidence.** I recomputed these independently in Python (numpy/mpmath/python-flint). Scripts are in /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/scripts/.

1. **Exact rational gates.** All match exactly (Fractions):
   - Q(1/790) = 107199260708819659/312050000000000000000000 > 3/10^7.
   - Q'(1/790) = 649470206171/19750000000000.
   - D2 = 234549697/116640000000000000000 < (1/500000 - ι)^2.
   - (ET21) = 59035878729/183840625000000 > 3/10000.
   - The N-gate margins are 427919.33 and 954057.66.
   - T_PT - X/2 = 350479773/2.
2. **Coefficient sums at (a, X), n ≤ 690988.**
   - S1 = 4.64917303132614 (claimed 4.649173031326).
   - P11 = 2.32523927475099 (claimed 2.325239274751).
   - 2P - S = 0.00130551817585 (claimed 0.001305518176).
   - Rough labels: 157939, as claimed.
   - The Cauchy-Schwarz feasibility crossing sits at t ≈ 0.1568205-0.1568206 (claimed ≈ 0.15682042). 2P - S is negative at t = 0.1568.
3. **Gram polynomial T_j on the 4-torus, sources 1-5.** These are sampled minima (random points plus Nelder-Mead), not certified:
   - Source 1: global min 2.1966e-5 at the origin, positive-definite Hessian (certified floor 1e-6).
   - Sources 2-5: minima 6.5e-4, 2.3e-3, 2.6e-2 and 1.3e-2 (floors 2.5e-6, 6.2e-6, 7e-6, 1.6e-6).
   - The prediction at the origin, (2P - S - δ)(δ + S) ≈ 1.188e-4, matches the computed bracket 1.185e-4.
4. **Weakest-leaf recovery margins**, using exact unbinned R(s) ≥ binned R̂:
   - Source 1: 0.0012729678122737 (floor 0.001272967812272).
   - Source 2: 0.002111607662 (floor 0.002111607661648).
   - Source 3: 0.0016369 (floor 0.0015974).
   - Source 4: 0.0014376 (floor 0.0013688).
   - Source 5: 0.0030168 (floor 0.0028931).
   - The (MA11) sign gates hold for all five.
5. **Inverse defects.** ||E F1 - 1||_1 ranges over 0.002356-0.002768 (< 3/1000). The support counts 53, 1160 and 3323 match.
6. **Centred moment M32.** Maximum over the sampled domain is 20.14374 at (98/625, X), below the certified leaf bound 20.21386 and below 81/4.
7. **Euler tail.**
   - Z(U0) = 0.98103177518922 (claimed < 0.981031775189216).
   - (B + C0)/κ = 0.75252559 (< 0.752526).
   - ρ bounds: 0.4720618472989 and 1.82363945.
   - L1 = 0.89671620664513; |E_x| = 0.57934212655049; ℓ0 = 27.5885261773423.
   - β_m ≥ 0 for every m ≤ K, and all ET5/ET6 gates hold.
8. **Separator.**
   - I first validated my implementation of Polymath's f_t against the true H_t/B_t at x = 2e4 and 5e4 (true H_t via the Gaussian average of ξ/8). The error is always below the e_C,0 scale.
   - At X = 6000000185827 with N = 690988, min |f_t(X+iy)| on a 41×21 grid over [0, 1/5]×[0, 1] is 1.4396, at t = 0.2, y = 1 (certified floor 0.0100458).
   - Cross-check: |f_0(X)| = 80.98814 vs mpmath |ζ(1/2 + iX/2)| = 80.98761. The difference of 5.4e-4 is below e_C,0 ≈ 1.203e-3.
   - The hand-recomputed error budgets EAB ≈ 1.3624e-9 and EC ≈ 1.20300e-3 match the paper.
9. **Inherited anchor (documentary evidence).**
   - Platt-Trudgian arXiv 2004.09765 p.5: Cor. 2 (Λ ≤ 0.2) cites only row 2 of Polymath Table 1.
   - Polymath debruijn.tex §10 says it "expect[s] to be able to verify" the large-x zero-free hypothesis, with Thm 1.2 labels (ii)/(iii) swapped in that paragraph. Barrier mesh points were computed "at 20 digits accuracy".
10. **Fractions of other claims.**
    - Raymond 2026b: 427693072077942473661578098491/3961408125713216879677197516800 = 0.10796491007877.
    - Gordon: 3885632262767861213460393068710302759/24646172707879668706230182733520000000 = 0.15765661909549.
    - Raymond 2026a: 18674384228461/125000000000000 = 0.149395073827688.

**Sources checked.**
- arXiv:2611.06245v1 PDF (sha256 5465b84a0bfbdb17e825c64a79a9cd518d3b0c47dd0fa84114cfcd261435abf9), full text read
- arXiv:2611.06245 e-print source: ms.tex, math/*.tex (balanced_gauge, multi_anchor_transport, finite_arithmetic, PHYSICAL_SEPARATOR_TRANSFER, INTERIOR_THEOREM, infinite_tail, global_descent), anc/README_REPRODUCIBILITY.txt, anc/PROOF_INPUT_BINDINGS.json, anc/SOURCE_INPUT_HASHES.json, anc/TESTED_ENVIRONMENT.json (inspected, nothing executed)
- Polymath arXiv:1904.12438v2 LaTeX source (debruijn.tex): Thm 1.2, Thm 1.3 eqs (6)-(24), Thm 1.5, Thm 3.2, Section 10 and Table 1
- Platt-Trudgian arXiv:2004.09765 (Cor. 2 text, p.5)
- arXiv API queries (17 Nov 2026) for 'de Bruijn Newman' / abs:Newman AND abs:Bruijn
- Zenodo API records 23781981 (Raymond 0.149396 v1.1 erratum), 23752103 (Raymond 0.107965), 22658444 (Kornaus v1.1), 21175533 (Mosaic 0.1875)
- Crossref record 10.2139/ssrn.7608638 (Gordon abstract)
- MathWorld de Bruijn-Newman Constant page (last updated 16 Nov 2026)
- mpmath zeta(1/2 + i*3000000092913.5) cross-check
- Observatory ledger frontiers/ledger.jsonl LED-DBN-8..17 and history/recent_developments_2024_2026.md
- NOT accessed: GitHub release Dale-Dug/planat-raymond-collision-exclusion-0156821 (session GitHub access denied); Gomila, Gordon, Mosaic GitHub repos; SSRN full text; Zenodo PDFs of Raymond/Kornaus/Mosaic (metadata only)

## Auditor report

# L2 audit F8-dbn-claims: 2026 de Bruijn–Newman upper-bound claims

**Auditor level reached:**
- **Planat–Raymond (arXiv:2611.06245v1):** L2. I re-derived the logical assembly and the transfer of Polymath's published error terms, and independently recomputed a broad set of certificate quantities. The full interval certificate was **not** replayed.
- **All other claims:** L0+ or secondary, from metadata, abstracts and citations only.

**Primary outcome:** `no_issue_found_in_inspected_portion` for Planat–Raymond. All other claims are `announced_unrefereed`, and none is verified by the Observatory.

**Secondary item:** an inherited, documentation-level ambiguity in the published anchor Λ ≤ 1/5 (see §5). It is not a finding against Planat–Raymond.

---

## 1. What Planat–Raymond claim

### 1.1 The theorem
- **Claim (Thm 9.4, eq. (3)):** Λ < 156821/10⁶ = 0.156821, with H_0(z) = ξ((1+iz)/2)/8 and ∂_t H = −∂_z² H.
- **Status in the paper:** "proposed version 0.3". The paper says it "does not represent completed peer review". Its Table 1 labels it "U, draft".
- **Fixed parameters:**
  - a = 156821/10⁶, b = 1/5.
  - X = 6 000 000 185 827.
  - W = 72 382 294 738 709 = ⌈4π·2 400 000²⌉.

### 1.2 Architecture (Thm 9.3, regional assembly)
1. **Stationary separator:** H_t(X+iy) ≠ 0 for (t, y) ∈ [0, 1/5] × [0, 1]. Certified as |H_t/B_t| > 7/800.
2. **Finite exterior:** (H_t(x), ∂_x H_t(x)) ≠ (0, 0) for X ≤ x ≤ W and t ∈ [a, b].
   - It uses five 4-prime ({2,3,5,7}) Gram/stability certificates and a weighted Cauchy–Schwarz "recovery" over rough primes.
   - It adds a forward-heat minimum-modulus lemma (Lemma 4.4) and a balanced real-gauge transfer (Thm 3.1, Cor. 3.2).
3. **Infinite exterior:** the same exclusion for x ≥ W. It uses an Euler factor over the primes ≤ 13, Poisson-covering positivity of the mollified coefficients, and a differential inequality in U = log N.
4. **Interior:** the separator, RH from Platt–Trudgian up to T_PT, and a local Hermite splitting lemma together make all zeros with |Re z| ≤ X real and simple for 0 < t ≤ 1/5.
5. **Assembly:** Λ ≤ 1/5 (Platt–Trudgian Cor. 2), combined with Lemma 9.2, gives the bound. Lemma 9.2 says that if 0 < Λ ≤ 1/2 then H_Λ has a finite multiple real zero; its proof uses Polymath Thm 1.5(i) remote reality. The exclusion covers the closed band, so Λ < a strictly.

### 1.3 Certificate (as described)
- 664 505 structural Fourier coefficients, i.e. 5 × 132 901.
- 44 182 closed torus boxes, with C++ exact-integer jets after 2⁻⁴⁴ quantisation and a Taylor bound (FB1).
- 184 Acb separator moments and 17 385 separator rectangles.
- 56 recovery leaves, 151 centred-moment leaves, and Euler-tail Arb sums over 2 391 233 terms.
- **Release:** GitHub `Dale-Dug/planat-raymond-collision-exclusion-0156821`, tag certificates-0156821-v1, commit 18dbc01ea36b…
  - ZIP SHA-256: 08bf5123ac79a438b626275eb8174df6d8cdfd069e7c7a0a70c1c4807b1ebde7.
  - Tested stack: CPython 3.12.14, python-flint 0.9.0, FLINT 3.6.0, NumPy 2.3.5.
  - The arXiv ancillary directory contains only two abbreviated checkers plus hash bindings. The authors state that these are "NOT a substitute" for the full replay.
- **Authors' own caveats:** the diagnostics share Arb/FLINT, so the authors do not call them an independent end-to-end interval proof. AI assistance is declared (ChatGPT 6.1, with an adversarial audit by Claude Opus 5.5).

### 1.4 Inputs
- **RH height (Platt–Trudgian Thm 1):** T_PT = 3 000 175 332 800.
  - Required: T_PT ≥ X/2 = 3 000 000 092 913.5.
  - Margin: 175 239 886.5 (I verified this exactly).
- **Λ ≤ 1/5 (Platt–Trudgian Cor. 2):** the upper end b of the band.
- **Polymath inputs:** Thm 1.3 with eqs. (20)–(24), Thm 3.2 (strip contraction), and Thm 1.5(i). Thm 1.5(i) has an ineffective constant, which is fine because it is used only qualitatively.
- **No larger RH height is needed.** No new barrier is needed beyond the authors' own separator at X.

## 2. Logic and analytic transfer (re-derived)

### 2.1 The global logic
- **Theorem 7.2 / Lemma 7.1.** Forward heat with ∂_t H = −∂_z² H splits an m-fold real zero into m simple real zeros: the local model is the Hermite-type P_m with real roots. Backward heat produces non-real zeros.
  - With a zero-free boundary on Ω = {|Re z| < X, |Im z| < 2}, the supremum argument is correct.
  - The boundary is zero-free because the separator covers |y| ≤ 1 at x = ±X and the strip bound covers 1 < |y| ≤ 2.
- **Lemma 9.2** is correct. It needs only that all zeros of H_Λ are real, together with Rouché, the strip bound, and remote reality on [Λ/2, Λ].
- **Theorem 9.3** is correct.

### 2.2 Transcription of Polymath Thm 1.3
I compared the paper against the Polymath LaTeX source:
- M_0, α, M_t and B_t = M_t(s₋) match.
- s* and κ match, including the identity w₋ + κ − y = w₊.
- The bound |γ| ≤ e^{0.02y}(x/4π)^{−y/2} is retained. This is the factor Kornaus's v1.1 had to restore.
- The (·)₊ term of (21) is bounded by 1 + 8/x² on y ∈ [0, 1].
- In (23), 0.626 = 313/500 and 6.66 = 333/50.
- In (24), 1.24 = 31/25 and 10.44 = 261/25.

Separator error budget, recomputed by hand:
- EAB ≈ 1.3624e-9.
- EC ≈ 1.20300e-3.
- Total budget ≈ 1.2030073e-3.
- Certified floor minus budget: 0.0100458444 − 0.0012030073 = 0.0088428371 > 7/800.

Extending to t = 0 by continuity is valid because the bound is uniform in t.

### 2.3 Key lemmas re-derived
- **Lemma 3.4.** Root-location argument: if |ρ| > 1 then Re 1/(1−ρ) < 1/2.
  - The TeX states Re(Ā_χ L_χ) ≤ ½ log N |A_χ|²; the PDF extraction drops the bar and the ½.
  - Combined with ℓ − log N > 13, it gives Re(Ā S) > 13 r₀². Q(r₀) follows.
  - The identity u′ = −½ Im(P·B_true) checks out.
- **Lemma 4.3 (recovery).** Vector maximum modulus plus Cauchy–Schwarz. Correct.
- **Lemma 4.4.** The root ODE gives d log|r_i|/dh = c − ¼ − ½ Σ Re r_i/(r_i − r_j) ≥ c − n/4. Correct.
- **§8 tail.**
  - The Poisson covering identity β_m = b_m C_m ≥ 0 checks out; the edge rates sum correctly.
  - The heat-time monotonicity gates (ET5) and (ET6) hold.
  - The differential inequality Z′ ≤ −κZ + B(U₀) + C₀ is correct. It uses d⌊K/d⌋ > K − D, and B is decreasing because −aU₀/2 + ½ + aε₀ = −0.652 < 0.
  - The operator-norm step in (ET17) and (ET18) is correct.

## 3. Independent numerical recomputation

All of these were computed by my own code, not the authors'. None of the values I recomputed falls below a claimed bound or floor.

| Quantity | Paper | Independent value |
|---|---|---|
| Q(1/790), Q′(1/790), D2, (ET21), ι gate | exact rationals | identical (Fractions) |
| S₁, P₁,₁ at (a, X), n ≤ 690988 | 4.649173031326, 2.325239274751 | 4.64917303132614, 2.32523927475099 |
| 2P−S | 0.001305518176 | 0.00130551817585 |
| Four-prime feasibility crossing | ≈0.15682042 | 0.1568205–0.1568206 (2P−S < 0 at t = 0.1568) |
| Gram T₁ min on torus (floor 1e-6) | certified > 1e-6 | 2.1966e-5 at origin; Hessian positive definite (sampled, not certified) |
| Gram T₂…T₅ minima (floors 2.5e-6, 6.2e-6, 7e-6, 1.6e-6) | certified | 6.5e-4, 2.3e-3, 2.6e-2, 1.3e-2 (sampled) |
| Weakest-leaf margins, sources 1–5 | 0.001272967812272, 0.002111607661648, 0.001597440849477, 0.001368843821548, 0.002893065121426 | 0.0012729678122737, 0.002111607662, 0.0016369, 0.0014376, 0.0030168 (exact R ≥ binned R̂) |
| Inverse defect ‖EF₁−1‖₁ | < 3/1000 | 0.002356 – 0.002768 |
| Support counts 53 / 1160 / 3323 / 157939 | as stated | identical |
| M₃₂ maximum | < 81/4 (leaf bound 20.21386) | 20.14374 at (98/625, X) |
| Z(U₀), (B+C₀)/κ | < 0.981031775189216, < 0.752526 | 0.98103177518922, 0.75252559 |
| ρ bounds, L₁, \|E_x\|, ℓ₀ | 0.472061847298902, 1.82364, 0.896716206645132, 0.579342126550494, 27.5885 | 0.4720618472989, 1.8236395, 0.8967162066451, 0.5793421265505, 27.58852617734 |
| Separator min \|f̃\| over [0, 1/5]×[0, 1] | certified floor 0.0100458 | grid (41×21) min 1.4396 at t = 0.2, y = 1 |
| \|f₀(X)\| vs \|ζ(1/2 + iX/2)\| | – | 80.98814 vs 80.98761 (difference 5.4e-4 < e_C,0) |

**Validation of my model code.** At x = 2e4 and 5e4, my f_t differs from the true H_t/B_t by less than the e_C,0 scale. The true value was computed by quadrature of the Gaussian average H_t(z) = E[H₀(z − i√(2t)G)].

**What these numbers say.**
- The separator is very robust: X sits at a large peak of |ζ|.
- The finite-exterior Gram certificates hold with large factors at t = a.
- The method itself is knife-edge in t. The four-prime family stops working just below 0.1568206, as the authors' Prop. 4.1 and Remark 4.2 state.

**Not done.**
- Replay of the 44 182 C++ boxes, the 17 385 Arb rectangles and the 151/56 leaf enclosures.
- Hash check of the release ZIP: GitHub access was denied in this session.
- Formal certification of the torus minima. Mine come from sampling plus local optimisation.

## 4. Consistency with the Polymath15 framework

### 4.1 Same RH-height input
- Polymath Thm 1.2 needs (i) RH to X/2, (ii) a complex canopy at t₀, and (iii) a barrier, and gives Λ ≤ t₀ + y₀²/2.
- Planat–Raymond keep (i) unchanged, at the same Platt–Trudgian height.
- They replace (ii), (iii) and de Bruijn's y₀²/2 contraction with three things:
  - a full-height stationary separator;
  - real-double-zero exclusion on the band [a, 1/5];
  - Λ ≤ 1/5 and remote reality to close the argument.
- No hidden larger RH height is needed.

### 4.2 Scaling
- Polymath's heuristic is Λ ≲ C/log T. It explicitly allows "improving the implied constant".
- Polymath Table 1 rows give t·log X between 5.06 and 5.95.
- Planat–Raymond give t·log X = 4.614, equivalently t·log(X/4π) = 4.217.
- The Polymath method itself would need X ≈ 2×10¹⁵ for Λ ≤ 0.16.
- The gain is plausible for two reasons. First, the y₀²/2 penalty is removed. Second, a real-axis jet criterion is weaker than complex zero-freeness near the axis.
- An isolated hypothetical off-line zero with y = 1 at this height lands at t ≈ 0.060 (from dy/dt ≈ −1/y − L/2). That is well below 0.1568, so there is no tension.

### 4.3 A natural scale (context only, not a finding)
- At t = 4/log(X/4π) = 0.148744, the highest-index coefficients of the Riemann–Siegel model reach effective exponent 1.
- Planat–Raymond's analytic module needs p(v) > 1, i.e. t > 4/(L − 2h₀) ≈ 0.14875.
- Every claim of unconditional form lies above this scale. Raymond 0.149396 sits only 0.44% above it (t·L = 4.0175).
- Only Planat's conditional 0.148612 lies below it (t·L = 3.9964).
- This is a heuristic marker for these techniques. It is not a lower bound on Λ.

## 5. Inherited caveat on the anchor Λ ≤ 1/5 (classified `unresolved_ambiguity`, documentation level)

**The dependency chain.**
- Planat–Raymond's band end b = 1/5 is Platt–Trudgian Cor. 2.
- Platt–Trudgian (arXiv 2004.09765 p.5) obtain Cor. 2 solely from row 2 of Polymath Table 1: X = 5×10¹²+194858, t₀ = 0.186, y₀ = 0.16733.

**What Polymath §10 says about that row.**
- It opens with "results verifying the second two hypotheses".
- It then describes the large-x zero-free (canopy) step as something one should "expect to be able to verify". That paragraph also swaps the (ii)/(iii) labels relative to Thm 1.2.
- It states that barrier mesh points were computed "at 20 digits accuracy". It does not explicitly claim outward-rounded enclosures.

**How to read it.**
- Λ ≤ 0.2 is refereed (BLMS 2021) and universally cited, so treating it as published input is standard.
- Still, for an evidence-graded archive, Planat–Raymond's "unconditional" label inherits this certification level.
- Every 2026 claim anchored at the Platt–Trudgian site inherits it in the same way.
- No witness of failure exists.
- **Suggested follow-up target:** "certification level of Polymath Table 1 row 2 / Platt–Trudgian Cor. 2". Polymath's code lives in the `dbn_upper_bound/arb` repository.

## 6. Status of each 2026 claim (ζ case unless noted)

**Unconditional in form, unrefereed:**

| Claim | Source | Observatory status |
|---|---|---|
| Λ < 0.156821 | Planat–Raymond, arXiv 2611.06245v1 (4 Nov 2026) | announced_unrefereed. **L2: no issue found in the inspected portion.** Full replay not done; release not retrieved. |
| Λ < 0.149396 (= 18674384228461/1.25e14) | Raymond 2026a, Zenodo 22867547 → v1.1 23781981 (30 Oct 2026). The erratum changes 5/6→11/12 and the wall bound to 697/900; the author says the bound is unchanged. | announced_unrefereed. Not audited (metadata only). Planat–Raymond decline to rely on it. |
| Λ < 0.158 (0.1576566190954906…) | Gordon, SSRN 7608638 / GitHub v1.0.0 (12 Sep 2026). Piecewise-affine barrier with 12 666 rows; partial Lean, conditional on analytic inputs. | announced_unrefereed. Not audited. |
| Λ ≤ 0.1875; < 0.16; < 0.1595 | Mosaic Intelligence: Zenodo 21175533 (3 Jul 2026, AI-generated) plus GitHub certificates | announced_unrefereed. Not audited. |
| Λ < 0.172422 | Kornaus, Zenodo 22658444 v1.1. Collision exclusion; v1.1 restored the omitted e^{0.02y} factor in the separator error. | announced_unrefereed, with an author correction. Not audited. |
| Λ ≤ 0.1787854 | Gomila, GitHub (20 Aug 2026) | announced_unrefereed. Not audited. |
| Λ ≤ 0.1732 | Planat, arXiv 2610.32694v1 | announced_unrefereed. Not audited here. |
| Λ ≤ 0.17795… | Planat, arXiv 2609.37164v2 | audit-relative: it assumes Gomila's package. |

**Conditional:**

| Claim | Source | Observatory status |
|---|---|---|
| Λ ≤ 0.148611789321711 | Planat, arXiv 2610.18214v1 | conditional on premises (A1)–(A3), which are not established. Not a record. |
| Λ ≤ 0.13963 | Hakimoglu-Brown, arXiv 2610.12803 | conditional on H7/8. |
| Λ ≤ 0.10796491007877 (exact fraction verified) | Raymond 2026b, Zenodo 23752103 | conditional on H7/8. The deposit calls it "unconditional" via OpenAI's unrefereed 7/8 theorem, which claims a Lean formalization; the Observatory has not replayed that formalization. This is a status-label dispute, not a mathematical error. |

**Not about ζ:**
- Λ_L ≤ 0.2978125 for real primitive characters with conductor ≤ 400. Source: Freire et al., arXiv 2610.27343. Status: announced_unrefereed.

**Search for further claims:**
- An arXiv API query on 17 Nov 2026 found no dBN-bound preprints after 2611.06245, which is still at v1.
- MathWorld (updated 16 Nov 2026) lists Mosaic, Gomila, Gordon, Raymond 2026a and 2026b as "unreviewed". It does not yet list Planat–Raymond, Kornaus or Planat 0.1732.

## 7. Notes for the ledger (suggestions only; no files edited)
- **LED-DBN-12:** the content is accurate. It could record "L2 partial, no issue found: independent recomputation of gates, sums, Gram minima, leaf margins, tail and separator; full certificate not replayed". It should also note the inherited Λ ≤ 1/5 dependency described in §5.
- **LED-DBN-9 / LED-DBN-10:** add the §10 wording issue ("expect to be able to verify"; (ii)/(iii) labels swapped). Note that Λ ≤ 0.2 rests on row 2 only.
- **LED-DBN-11:** the original deposit DOI is 10.5281/zenodo.22867547 (v1.0); v1.1 = 23781981.
- **Cosmetic only:** the paper states the lower bound ℓ₀ > 27.588526177342325 to 15 decimals. A float64 recomputation gives 27.588526177342324, so float64 can neither confirm nor refute the last digit. The gates that actually need ℓ₀ are ℓ₀ > 27 and ℓ₀ > U₀ + log D ≈ 25.0, both of which hold by a wide margin.

## 8. Smallest statements whose failure would invalidate Planat–Raymond
1. **Source-1 Gram positivity (G)** at (a, X, C, δ₁ = 4/3125, ϑ₁ = 0.9999). The independent minimum is 2.2e-5, versus the certified floor 1e-6.
2. **Correctness of the 44 182-box enclosure pipeline.** Not replayed.
3. **Λ ≤ 1/5**, a published input (see §5).
4. **Polymath Thm 1.3, eqs. (20)–(24)**, a published input; its transcription was checked.

The separator and the Euler tail have comfortable margins in my recomputation.

Scripts: /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/scripts/ (rationals.py, coeffs.py, cs_cross.py, tail.py, m32.py, ftmodel.py, separator.py, gram.py, gram_min.py, sources.py).



