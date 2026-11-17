# Unsolved questions, prioritized

```text
Status: SYNTHESIS (exploration layer). This is a list of open questions, not of results. Each question gives
        its type, priority and source. Where a question rests on a 2026 claim, that claim is unrefereed (quasi-RH
        11/12 audited by the Observatory with no error found; 7/8 not audited, Lean claimed not replayed; 2/3
        audited with one repaired proof step). RH is open.
Scope: 96 questions in ten areas (A-J). They cover verification gates, the quasi-RH route, critical-line
        proportions, Weil positivity and operators, de Branges, Li/Jensen/heat flow, arithmetic criteria, zero
        density and L-function consequences, function-field transfer, and the host repository's open cuts.
Exact sources or dependencies: frontiers/ledger.jsonl (LED, corrected values); frontiers/research_programs.md
        ("<AREA> §n"); connections/connections.jsonl (CON; corrected forms); connections/repository_bridge.jsonl
        (BRG); audits/verified_findings.md and unresolved_findings.md (FND); audits/quasi_rh/DOSSIER.md;
        audits/claims_2026/CRIT23 and SIEGEL dossiers; campaigns C1-C5 (C3 FINAL; others REPORT + SKEPTIC);
        corpus/bibliography.jsonl (PAPER). Companion files: frontiers/missing_lemmas.md,
        frontiers/known_obstructions.md.
What was actually run: the sources were read. Questions were extracted and normalised to precise quantified
        form; duplicates were merged. No question has been attempted here.
Smallest remaining gap: priorities are the synthesizer's judgement. The Observatory-proposed formulations
        (marked) are unreviewed.
```

**Priority.** P1 marks a verification gate or a well-posed, high-leverage target that a single research effort could plausibly settle. P2 marks a substantive mathematical target. P3 marks computational, bibliographic or bookkeeping work.

**Type.**
- RH-eq: equivalent to RH.
- QRH-eq: equivalent to or as hard as a quasi-RH statement.
- Weaker: genuinely weaker than RH.
- Verif: verification of an existing claim.
- Comp: a finite computation.
- Obstr: settling an obstruction.

---

## A. Verification gates (all P1 unless marked)

1. **A1 (Verif).** Replay OpenAI's Lean development for `QuasiRiemannHypothesis` and `DirichletSevenEighths` at github.com/openai/math@4eaee875 (toolchain v4.34.1, Mathlib d13f23b7):
   - `lake build`;
   - Lean FRO `comparator` with `lean4export`;
   - an independent kernel (nanoda, disabled in the configs);
   - `#print axioms`.

   Does it certify ζ(s) ≠ 0 and L(s, χ) ≠ 0 for Re s > 7/8, and hence 11/12 a fortiori? Source: QRH dossier §1.3 and §5(2); unresolved_findings; audits/lean_replay/README.md.
2. **A2 (Verif).** In the HeckeSevenEighths challenge, does the custom `LFunction := π^sΓ(s)⁻¹Λ(s)/6`, built from shifted Hurwitz even kernels, equal Σ_{𝔞≠0} η(𝔞)N𝔞^{−s} on Re s > 1? Source: QRH dossier §1.3.
3. **A3 (Verif).** For paper2 (11/12), check the risk-ordered imports by human review (QRH dossier §5(3)):
   - (i) Dunn–Radziwiłł's transcription of Patterson's Thm 8.1 and of the Kubota multiplier (c/a)₃, against Patterson 1977 itself;
   - (ii) Goldmakher–Louvel Thm 1.1 for the family (x/k)₂κ_λ^{e_k};
   - (iii) the multiplier case analysis at l.3175–3196 and Lemma 6.3;
   - (iv) the Lemma B.2 constants.

   Are all correct?
4. **A4 (Verif).** Audit the 199-page 7/8 manuscript (PAPER-0528), section by section, at least to the depth of the 11/12 audit (FND-0009). Source: QRH dossier §1.1 and §5(1).
5. **A5 (Verif).** Does an independent second reviewer confirm the repair of AF Prop. 4.2 (P1-F1), i.e. tr G̃ = N(I) + O(X^{1/2}L) from (2.8) with one-sided sums? Source: CRIT23 §8(1); FND-0004.
6. **A6 (Verif).** Replay anthropics/zeta-23-lean v1.0 (Lean v4.33.0-rc2) with `#print axioms` on the main theorems and run comparator. How does it relate to anthropics/formal-math fbdc36b (finding F5)? Source: CRIT23 §8(2).
7. **A7 (Verif, Comp).** Replay Knausgård's three local inequalities (Props 3.3, 5.3, 6.3) by an independent branch-and-bound in directed-rounding Arb, written from the statements. This is the only gap between 0.6735382/0.8390046 and the audited 0.6725007/0.8362504. Source: CRIT23 §8(3); LED-CRIT-3.
8. **A8 (Verif; P2).** Close the residue on the LZ route: write out P2-N1 line by line, or re-derive BGSTB24 Lemma 4 and the Goldston–Montgomery R(x, T) evaluation on [0, 1 − 2ε₀]. Source: CRIT23 §8(4); LED-CRIT-2 and LED-CRIT-13 corrected.
9. **A9 (Verif).** Replay OAI `SiegelZeros` (comparator with nanoda) and Kimura's `B4.Chi8.zero_gap_all`. Audit the κ = 1/2 variants (Green, hexagon:2610.00311v2; van Dijk; Pescador; Barreto). Source: SIEGEL §8(2)–(3); FND-0010.
10. **A10 (Verif, Comp; P2).** Replay the Lu–Zaman–Zhao production run for 4·10⁵ < q ≤ 10¹⁰, on which Banks' all-q constant 3.0·10⁻³ depends. Source: SIEGEL §3; unresolved_findings.
11. **A11 (Verif, Comp).** Replay Zhu's certificate of Pos(0.8) independently, with directed rounding (ball arithmetic). Does λ*(0.8) ≥ 8.9·10⁻¹⁸ hold? Source: LED-POS-7; C5-ML-E1; CON-0010 correction (1).
12. **A12 (Verif; P2).** Replay the Planat–Raymond Λ < 0.156821 certificate, and any one of Gordon's < 0.158 or Raymond's < 0.149396. Source: FND-0011; LED-DBN-11, LED-DBN-12, LED-DBN-13; DBN §7(1).
13. **A13 (Verif, Comp; P2).** Complete the canopy verification for Polymath Table 1 row 2, which underlies the peer-reviewed Λ ≤ 0.2. Source: LED-DBN-9 corrected; DBN critique.
14. **A14 (Verif; P2).** For Cureton–Thorner (hexagon:2610.00200 v1 and v2): what are the exact formal statement and `#print axioms` of the AxiomProver development? Which consumers use 1 − 1/6000 and which use 31/32? Source: CON-0026 corrected.
15. **A15 (Verif; P2).** Audit Ji's 599/600 argument (PAPER-0155) and its unrefereed input, de Faveri's zero-density Cor. 1.5. Have an independent reader re-derive the six inequalities. Source: QRH dossier §1.5; CON-0038 next step (1).
16. **A16 (Verif; P3).** Is Li–Liu's claim correct that any Θ < 11/12 already gives the GRH power N^{1/2}? It is extraordinary and unaudited. Source: CON-0028 correction.
17. **A17 (Verif, Comp; P2).** Replicate RH(3·10¹²) independently, rigorously and with a different algorithm, then extend to H ≥ 10¹³ with archived code and hashes. The phase reduction at t ≈ 10¹³ must be exact or double-double. Source: VERIF §7 and its critique; LED-VERIF-1.
18. **A18 (Verif; P3).** Settle FND-0005: does Yang's written argument cover the v1 constant 21.432 over the full stated range? Source: unresolved_findings.
19. **A19 (Verif; P3).** Fix Farmer's convention for Table 4.1 (the j = 10 off-by-one; the zeros moved for j = 20) and re-certify j = 40 and j = 60 exactly. Source: FND-0002; C1-J4 and the C1 skeptic.
20. **A20 (Verif; P2).** Audit arXiv:0807.0090 v5–v10 (X.-J. Li, a live unrefereed claim) with C3 checklist items 3, 4 and 8. Separately, determine whether de Branges' post-2004 manuscripts rely on conditions of the (3.1)/(3.3) type. Source: C3 FINAL §9(5)–(6).

## B. Quasi-RH large-sieve route

21. **B1 (QRH-eq; P2).** Over K = ℚ(√−3), does Σ_{0<N(u)≤D^h} |Σ_{(𝔫,S)=1} μ(𝔫)ν(𝔫)(u/𝔫)₆W(N𝔫/D)|² ≪ D^{1+h+ε} hold for some fixed h < 1? This is conjecture (C1); it would give Re s > 1/2 + 5h/12. Source: QRH dossier §4.3.
22. **B2 (QRH-eq; P1).** Do the angular-weight-1 quartic Kubota coefficients over ℤ[i] satisfy a μ-removal identity analogous to eq:gj? Equivalently, are there explicit quartic metaplectic theta coefficients that would prove J4: Σ_{0<N(u)≤X^h} |A_u(X)|² ≪ X^{1+h+ε} for some 1 ≤ h ≤ 10/9, giving ζ ≠ 0 on Re s > 1/2 + 3h/8? Source: CON-0038 (sound_and_useful); QRH dossier §4.3 (C2) and §5(5c).
23. **B3 (QRH-eq; P2).** Over K, is there square-root cancellation for Möbius-weighted cubic Gauss sums with a suitable angular twist? This is a Patterson-type statement for μ·g̃, and would give 5/6 by the short route. Source: QRH dossier §4.3 (C2).
24. **B4 (QRH-eq; P2).** In the 7/8 comparison system, which of the following can be proved?
    - (a) a count for the critical simultaneous-large-value class (δ_c, x = 1/2) with exponent < 2/3;
    - (b) the plain fourth moment at κ < 13/18;
    - (c) a direct estimate breaking B(ℓ) = 11/12 − ℓ/4.

    Source: QRH dossier §4.3 (C3).
25. **B5 (Weaker; P2).** Can de Faveri's sharp sextic sieve, or the Dunn–Radziwiłł / dFDH structure, enter Part II of the 7/8 argument (row counts from witnesses), and not only Part I? Source: QRH dossier §4.2 and §5(5b).
26. **B6 (Weaker; P1).** State and prove, as a separate checkable theorem, the density-hypothesis consequence of paper2 Prop. 3.1 for the sextic family: #{u₀ ~ U : L(s, νχ_·(u₀)) has a detectable zero with β ≥ σ} ≲ U^{2−2σ+ε}. A numerical violation would falsify Prop. 3.1. Source: QRH dossier §2.5 and §5(5d).
27. **B7 (Verif; P1).** Write the human half-page proof of 11/12 that Radziwiłł reports, and identify its minimal imports. Source: QRH dossier §1.4 [S] and §5(5a).
28. **B8 (QRH-eq; P2).** Conjecture G (CON-0037 corrected; Observatory-proposed): is every unitary Hecke character ψ of ℚ(√−3), of any infinity type, zero-free on Re s > 11/12? That would be the first fixed zero-free half-plane for a holomorphic GL(2) newform of weight ≥ 2, e.g. L(E, s) for y² = x³ + D. The load-bearing step is Prop. 3.1 at angular frequency m = l − 1.
29. **B9 (Weaker; P3).** Make the 11/12 proof effective, with explicit derivative orders (≈4^{4/ϑ}) and constants. Does it yield any explicit zero-free region near Re s = 1 beyond the half-plane? Source: QRH dossier §2.6.
30. **B10 (Obstr; P2).** Is there a countermodel family showing that, in the extraction architecture, the trivialising-row density r ≤ 1/n is forced? That would turn CON-0031(B)(ii) into a genuine obstruction. Conversely, does any architecture reach a half-plane left of 3/4? Source: CON-0031 correction; QRH dossier §4.1.
31. **B11 (Obstr; P2).** Does a Beurling [α, β]-system exist with α ≥ 2/3 and β < 1/2? Determine A(β) := sup{α : an [α, β]-system exists} for β < 1/2. This is the open region of CON-0032 T4 that covers the claimed 7/8 and 11/12. Source: CON-0032 next step (2).
32. **B12 (Verif; P2).** Verify CON-0032 T2 line by line: does BDR §5 use RH only through zero-freeness with Lindelöf-type bounds on Re s > 1 − α/2? Source: CON-0032 and its correction.

## C. Critical-line proportions and zero statistics

33. **C1 (Weaker; P1).** Prove unconditionally that liminf N0^s(T)/N(T) > 0.6819. Any proof must bring an input beyond the bandwidth-one ceiling. Source: CRIT §7(2); LED-CRIT-10.
34. **C2 (Weaker; P1).** Obtain any unconditional **upper** information on the all-zeros form factor F(α) for some α > 1, even averaged over [1, 1+δ]. Source: CRIT23 §7.3 and §8(7a).
35. **C3 (Obstr; P2).** Can an inertia-compatible certificate use the unconditional sign F ≥ 0 off [−1, 1]? Non-square kernels lose the identity ΣK² = tr A². Source: CRIT23 §7.3 and §8(7b).
36. **C4 (Weaker; P2).** Is there unconditional triple-correlation (third-trace) information for complex zeros at X ≍ T, beyond the Rudnick–Sarnak range? Source: CRIT23 §8(7c).
37. **C5 (Weaker; P1).** ML-CGG (CON-0006 corrected; Observatory-proposed): does Σ_{T<γ≤2T, β≠1/2} |Bζ′(ρ) − Bζ′(1−ρ̄)|² = o(T(log T)³) hold for the BHB mollifier with θ → 1/2? It gives liminf N*/N ≥ 19/27 and is strictly weaker than RH.
38. **C6 (Weaker; P2).** What is the largest η for which |β − 1/2| ≤ η/(log T)^{3/2} on (T, 2T], combined with Conrey's 99.9%-within-8/L input, gives liminf N*/N > 0.6818 through CON-0006(*)? Source: CON-0006 next step (2) and correction (1).
39. **C7 (Weaker; P2).** Prove liminf N0^s/N ≥ 19/27 unconditionally, matching the best RH-conditional value. Source: CRIT §7(3).
40. **C8 (Weaker; P2).** Under RH, prove that more than 19/27 of the zeros are simple, e.g. by feeding Hejhal/Rudnick–Sarnak third-trace information into the rank–trace certificate. Source: CRIT §7(4); SPACING §7(ii).
41. **C9 (Weaker; P2).** For one fixed GL(2) newform, prove the all-zeros pair-sum asymptotic for Fourier support < 1/2. With the rank–trace inequality this gives liminf N_d/N ≥ 1/R*_{1/2} = 0.4617. Source: CON-0035 corrected.
42. **C10 (Weaker; P2).** Prove the explicit Petersson diagonal lemma Σ_f ω_f|Σ_{p≤X} a_pλ_f(p)|² = (1 + O((X/N)^{k−1}N^ε))Σ|a_p|² for X ≤ N^{1−ε}. Together with the Hua–Yang template it would give harmonic averages ≥ 0.6725 (simple critical) and ≥ 0.8363 (distinct) over H_k(N). Source: CON-0036 corrected.
43. **C11 (Obstr; P3).** Run the ceiling LP for ξ′ with the Farmer–Gonek form factor. Can any bandwidth-one certificate make "simple and on the line" for ξ′ exceed Wu's 0.86957? The window class saturates at 0.868642. Source: CON-0015.
44. **C12 (Weaker; P1).** Under RH alone, prove μ ≤ 1/2 − δ for an explicit δ > 0, refuting the strong Alternative Hypothesis without Siegel zeros. Source: SPACING §7.
45. **C13 (Obstr; P2).** Do the resonance-weighted methods (Bondarenko–Heap quotient resonance; Durkan–Pearce-Crump moments) saturate at μ = 1/2, or can they cross it unconditionally? Source: SPACING critique (1); LED-SPACING-8.
46. **C14 (Weaker; P3).** Is there an admissible mollifier length θ > 4/7 for Conrey- or Feng-type coefficients? It would break a barrier that has stood since 1989. Source: CRIT §7(5); LED-CRIT-7.
47. **C15 (Verif; P3).** Audit the Yang–Yang higher-moment report (0.7962 simple-on-line), which conflicts with AF §7.2(e). Source: CRIT23 finding D-2; LED-CRIT-20.
48. **C16 (Weaker; P3).** Make every o(N) in AF/LZ explicit and extract T₀ such that N0^s ≥ 0.6·N on (T, 2T] for T ≥ T₀. Source: CRIT23 §8(6).

## D. Weil positivity and operator routes

49. **D1 (Weaker; P1).** Prove, without computer certification of the continuum infimum, that Pos(L₁) holds for some L₁ > (log 2)/2, i.e. on a window whose autocorrelation contains the prime 2. Source: POS §7(1); OPS §7.
50. **D2 (Weaker; P1).** Prove Connes–Consani Conjecture 4.1 for q = 3, with h₁ supported in (3^{−1/2}, 3^{1/2}). This includes identifying ker u(F)₂₂ with the semilocal Sonin space. Source: C5-ML-C1 corrected.
51. **D3 (Weaker; P2).** Prove a two-sided Fuchs-ladder estimate c₁δ₄(λ)/λ^A ≤ ε_λ(1) ≤ Cδ₄(λ)(log λ)³ together with a gap ε_λ(2)/ε_λ(1) ≥ cλ⁴, on an unbounded λ-range that includes the prime terms. Source: OPS §7; LED-OPS-9.
52. **D4 (RH-eq component; P2).** Is the lowest eigenvalue of QW_λ simple, isolated and ι-even for all large λ? This is hypothesis (H1) of the Connes programme. Source: OPS §3; LED-OPS-7; CON-0010 correction (3).
53. **D5 (Obstr; P2).** Is there a non-detection (blindness) theorem for windows L < L_N − c at height T when δ log(T/2π) < κ_c = 2.1773? Or does the collision model, which shows detection up to 0.85 below L_N, extend to a proof that near-line defects are seen below L_N? Source: C4-R and C4-BL with the C4 skeptic.
54. **D6 (Weaker; P2).** Prove a rigorous detection theorem in the interpolation regime: δ small and L ≈ (1/2)log(T/2π) + O(1). Source: C4 smallest remaining gap (i).
55. **D7 (Weaker; P3).** Prove the local resolvent hypothesis R(T, L, η) for ζ at some explicit heights. Note that R restricted to span{e_z} is equivalent to the needed matrix inequality. Source: C4-BL with the skeptic.
56. **D8 (Obstr; P2).** Can non-envelope certificates, such as prolate conditioning (ACL Thm 8.14, Prop. 8.18), bypass Zhu's resolution barrier T₁ = 2πe^{A_L}? Source: BRG-OPERATORS_HEAT-O1 correction.
57. **D9 (Weaker; P2).** ML-W0 (Observatory-proposed, with the skeptic's correction): on the square of the scaling site, can a Riemann–Roch inequality Dim H⁰(D(f)) + Dim H⁰(−D(f)) ≥ s(f, f) re-derive the known Pos((log 2)/2)? Source: C5-ML-W0.
58. **D10 (Weaker; P3).** ML-F1: in some F₁-framework, can Δ·Ψ(λ) be defined intrinsically so that it equals the explicit-formula distribution of CCM 2009 Prop. 7.2? Source: C5-ML-F1.
59. **D11 (Weaker; P3).** ML-Den: for one H₈ quaternion field with W(π) = −1, construct a canonical 2-dimensional V_k(π) with a G-invariant alternating form that is a sum of local contributions, and an antilinear * with *² = −1 giving positivity. Source: C5-ML-Den; C5-OB4.
60. **D12 (Weaker; P3).** Is there an unconditional partial decay rate for the Lax–Phillips semigroup Z″(t) toward the RH-equivalent condition? Source: LED-OPS-16.

## E. de Branges spaces and canonical systems

61. **E1 (Obstr; P2).** Does the de Branges zero condition −Re{ξ′(ρ_n)ξ(1+ρ_n)} ≥ 0 fail for infinitely many n, or for a positive proportion? By C3-ADJ-S it suffices that S(γ_n) − δ(γ_n) ∈ (3/4, 7/4) mod 2 infinitely often, for example via large negative values of S in (−0.93, −0.57). Source: C3 FINAL §9(1); FND-0013.
62. **E2 (Obstr; P2).** Conjecture C3-ADJ-RATE: does #{n ≤ N : P_n < 0}/N → 1/2? This needs a joint CLT for (S(γ_n), arg ζ(3/2 + iγ_n)) over zeros, with equidistribution mod 2 at unit scale. A cheap test: blocks near n = 10¹¹ and 10¹² (predicted ≈0.23 and ≈0.24). Source: C3 §3.3 and §9(2).
63. **E3 (Weaker; P3).** Prove the analogue of Conrey–Li Theorem 2 in argument form: Re{ξ(1+it)/ξ(2+it)} < 0 ⇔ −π/4 + arg ζ(1+it) − arg ζ(2+it) + O(1/t) ∉ [−π/2, π/2] mod 2π. Source: C3 §9(3).
64. **E4 (QRH-eq; P2).** For some ω < 1/2, does Suzuki's canonical system for ξ extend to [0, ∞), i.e. Ψ_ω ≥ 0 for all t? By Suzuki Thm 11.1 this is equivalent to ξ ≠ 0 on Re s > 1/2 + ω. Source: LED-OPS-15; CON-0007.
65. **E5 (RH-eq; P2).** Is there a positivity condition on H(E_ξ), E_ξ = ξ + ξ′, that is RH-equivalent and not merely sufficient, and that survives the one-off-line-pair test? Source: BRG-OPERATORS_HEAT-O6; LED-OPS-14.

## F. Li, Jensen, Laguerre–Pólya and heat flow

66. **F1 (Weaker; P1).** Prove the converse semi-local Li theorem: λ₁, …, λ_N ≥ 0 ⇒ no zero with β ≠ 1/2 and |γ| ≤ c√N (up to logarithms). This would repair Brown's Theorem 2 and make Li positivity a two-way finite detector. Source: POS §7(2); PAPER-0600.
67. **F2 (Weaker; P3).** What is the optimal c such that RH(T) ⇒ λ_n ≥ 0 for n ≤ cT² log T? The sketch suggests c up to about 2. Source: C1-L4; C1 open questions.
68. **F3 (Weaker; P2).** Make the Jensen–heat bridge rigorous: is hyperbolicity of J^{d,0} near height T equivalent to real-rootedness of H_{T²/(2d)} near T, up to O(T³/d²)? Source: C1-J2 (HEURISTIC; skeptic upheld with corrections).
69. **F4 (Weaker; P2).** Converse semi-local Jensen: does hyperbolicity of J^{d,0} for all d ≤ D imply RH up to height f(D) for an explicit f(D) → ∞? Source: POS §7(3).
70. **F5 (Weaker; P2).** Is the global Laguerre inequality L₁[Ξ](x) ≥ 0 true for |x| ≥ X₀, or on any interval longer than the verified-zero interval, without new zero input? This is Csordas' Problem 2. Source: LED-POS-14.
71. **F6 (Weaker; P3).** Does D_{r,k} > 0 hold for k ≥ C·r^{1+δ} with δ < 2, without zero input? Source: POS §7(4); LED-POS-13.
72. **F7 (Obstr; P2).** CON-0033 conjecture: is (λ_n(t)) strictly infinitely log-concave for all t ∈ (−t₀, 0], for some t₀ > 0? A redo of Liu–Mao §3 with kernel e^{tu²}Φ would settle it. Source: CON-0033 corrected.
73. **F8 (Weaker; P1).** Persistence lemma: does ζ(1/2 + δ + iγ) = 0 imply Λ ≥ cδ²/(log γ)²? Is the sharp form Λ ≥ c·min(δ², δ/log γ) true? Source: CON-0008 (sound_and_useful).
74. **F9 (Weaker; P2).** Explicit Polymath scaling: if all zeros with 0 < γ ≤ T are on the line, is Λ ≤ A/log T for T ≥ T₀, with explicit A ≈ 5? Source: DBN §7(2); LED-DBN-9.
75. **F10 (Weaker; P3).** Is there a rigorous lower bound on the collapse time t_c(T, δ) of a given off-line quadruple under the backward heat flow? Source: C1 open questions; C1-E1.
76. **F11 (Weaker; P3).** Is Λ_χ ≤ c < 1/2 for all primitive Dirichlet characters, or all real ones, of every conductor? Source: DBN §7(3); LED-DBN-17.
77. **F12 (Comp; P3).** For Pólya's approximant ξ*, determine Λ(Φ*). The verifier suggests reducing it to a strip-width question for the heat-flowed K_{iz/4}(2π) kernel via de Bruijn's cosh shrink. Is Λ* ≤ −4, as the non-rigorous numerics suggest? Source: CON-0024 corrected.

## G. Nyman–Beurling and arithmetic criteria

78. **G1 (QRH-eq; P2).** Prove CON-0021: for α ∈ (Θ, 1), limsup_n log s_n(α)/log n = −2(α − Θ), with the corrections for α = 1. Hence RH ⇔ s_n(α) ≪ n^{1−2α+ε}. Source: CON-0021 (tested_supported).
79. **G2 (Comp; P3).** Run a synthetic Nyman–Beurling d_N computation, using Gram matrices of a modified zeta with injected zeros, to test D² ≈ β/log N + F at small T. Source: C1-N2 and the C1 open questions.
80. **G3 (Weaker; P3).** Is there an exact L^p-norm natural-integer Nyman–Beurling criterion with ρ_a(x) = {1/(ax)}, for 1 < p < 2? It should be stated against Dimitrov–Oliveira's graded criteria. Source: CON-0007 correction (2).
81. **G4 (Weaker; P1).** Prove Robin's inequality for every 22-free n > 5040. By the ARITH critique this needs a certified Mertens-product bound with relative error below ≈2.4·10⁻⁷ near x ≈ p_k0 = 29,996,208,012,611. Source: LED-ARITH-2; ARITH critique (1).
82. **G5 (Weaker; P2).** Prove a Büthe-type theorem: RH(T) ⇒ Nicolas' (resp. Robin's) criterion for x (resp. log n) ≤ X(T) ≈ T²/log² T, with all truncation and O(1/log x) terms explicit. Source: C1-D3 (sketch); C1 open questions; CON-0002 corrected.
83. **G6 (Comp; P2).** Give a certified proof that limsup M(x)/√x ≥ 2 and liminf ≤ −2. Give a rigorous proof that the first Mertens counterexample is below exp(10¹⁸). Source: ARITH §7(i)–(ii); LED-ARITH-8, LED-ARITH-9.
84. **G7 (Comp; P3).** Narrow the window (1.39·10¹⁷, e^{727.951332668}) for the first failure of Oliva's step (3). Any x with θ(x) − x > (0.53 + o(1))log x gives a failure at the largest prime ≤ x. Source: C3-ADJ-O2; C3 §9(4).
85. **G8 (Open; P3).** Is Stieltjes' M(x) = O(√x) false? It is believed false (Ingham under LI) and is not refuted. Source: C3-D6.

## H. Zero density, zero-free regions and L-function consequences

86. **H1 (Weaker; P1).** For 1-bounded Dirichlet polynomials, is |W| ≤ N^{9/10−δ} at σ = 7/10, T = N^{13/10}, i.e. LV(σ, τ) < τ + 1 − 2σ near (7/10, 13/10)? This would give sup A < 30/13 and PNT in intervals x^{17/30−δ″}. Source: ZDE §7(a) and its critique; LED-ZDE-1.
87. **H2 (Weaker; P2).** Does the density hypothesis hold for σ ≥ 25/32 − δ? There has been no movement since 2000. Source: ZDE §7(b); LED-ZDE-6.
88. **H3 (Weaker; P2).** Is there a zero-free region of shape σ ≥ 1 − c/(log t)^θ with θ < 2/3, or the Vinogradov–Korobov shape without the (log log t)^{1/3} factor? Source: ZFR §7(i).
89. **H4 (Weaker; P2).** Is μ(1/2) ≤ 13/84 − δ for an explicit δ > 0? For δ ≤ 6.4·10⁻⁴ it suffices to bound Σ_{m~M} m^{−it} ≪ M^{1/2}T^{13/84−δ+ε} for T^{0.4054−3.3δ} ≤ M ≤ T^{1/2}. Source: GROWTH §7(A).
90. **H5 (Weaker, conditional; P2).** Write a full proof that QRH(θ) for all Dirichlet L-functions gives P(a, q) ≪ q^{12/5+ε} effectively from refereed density inputs, or q^{7/3+ε} with CGL. This corrects the QRH dossier's 8/3 + ε. Source: CON-0001 and CON-0016 (sound_but_known; Thorner–Zaman Thm 2.3; CGL Cor. 1.4).
91. **H6 (Weaker, conditional; P3).** Under a half-plane hypothesis, write the QRH version of Montgomery–Vaughan Lemma 2 with error x·y^{θ−1}(log kx)²/(1 − θ)². Does M(χ) ≪ (1 − θ)⁻¹√q log log q follow? Source: CON-0017 corrected.
92. **H7 (Weaker; P2).** Can the interpolation-determinant method uniformly exclude exceptional zeros for GL(2) or Rankin–Selberg families, or for quadratic Hecke characters over K ≠ ℚ? Source: LFUN §7(iv); SIEGEL §8(5).
93. **H8 (Obstr; P2).** Can any comparison of Guo-Lemma-5.1 type certify c ≥ 1/5 for (1 − β)log q? Or is 3 − 2√2 = 0.1716 the ceiling of the present shape? Source: SIEGEL §7.2 and §8(4).
94. **H9 (Weaker; P3).** Artin's primitive-root conjecture under quasi-GRH(7/8): is there a non-abelian large sieve over q ∈ [x^{1/8}, x^{1/2}] that goes beyond the Nongkynrih level? Source: CON-0020 corrected.

## I. Function-field transfer

95. **I1 (Weaker; P2).** Pritsker's problem: is there a sequence of weights w_n of type (1.12) with B(w_n) → 1, i.e. an elementary PNT via Gelfond–Schnirelman? By the C5 skeptic §3.4, a one-sided lower bound on ψ would suffice over ℚ. Source: C5-ML-S(ii); C5-OB6 corrected.
96. **I2 (Obstr; P2).** For abstract zero multisets with the zeta functional equation and density, does a sufficiently small off-line displacement survive Weil positivity on every fixed window [−L, L]? This model-theoretic form of "no finite window suffices over ℚ" is plausible and unproved. Source: C5 skeptic §3.3.

## J. Host-repository open cuts (P2 unless marked; BRG statuses apply)

- **J1 (§1, QRH-eq).** For each detector in the host class whose converse is not yet checked, prove the converse (partial summation from M(x) = O(x^{Θ+ε})), so that "negative mass Y^{θ+ε} ⇔ zero-free Re s > 1/2 + θ" holds detector by detector. Source: BRG-MELLIN_WAVELET-O3 corrected; CON-0007 next step (2).
- **J2 (§1, Obstr).** Write Ingham's Fejér-kernel argument line by line for H^[1], with trivial zeros, convergence and multiplicity handled. Is eventual nonnegativity of H^[1] equivalent to RH plus linear dependence of the ordinates? Source: BRG-MELLIN_WAVELET-O1; BRG-SHARP_NATIVE-O1.
- **J3 (§2).** Give an explicit lemma for the margin factor ∏_{i≤m}(1 − p_i^{−b_i−1})·∏_{p>p_m}(1 − p^{−A−1}) of an exact-prefix canonical subtree, uniform in a declared range of A. Source: BRG-ROBIN-O3 corrected.
- **J4 (§3, P1).** Does the safe-axis Kwong hierarchy disperse zero information like Jensen polynomials (order ≈T²) or concentrate it like PF_k (Sra Thm C.11)? Source: BRG-XI_PICK-O2, BRG-XI_PICK-O7.
- **J5 (§3).** Produce one error-enclosed lower certificate for the source-defined effective matrix on one window. What is the minimal K under the sharper Ω(0) > −11/2 bound? Source: BRG-OPERATORS_HEAT-O1 and its correction.
- **J6 (§3).** Do the zeros of H_t for t < 0 satisfy the horizontal-strip bound and the subquadratic counting needed to apply ZH.17? Source: BRG-OPERATORS_HEAT-O4 correction (2).
- **J7 (§4).** Find an adjacent-order descent inequality with quantified loss that fails, as it must, for Farmer's X₁₀ and for H_t with t < 0, yet holds for ξ. Source: BRG-XI_PICK-O2, O3, O4; C3 checklist items 3 and 18.
- **J8 (§5).** Give an explicit relative error bound for principal-member extraction in the required depth regime, or one checked source adapter. Source: host OPEN_CUTS §5; BRG-FAMILIES-O3, O7.
- **J9 (§6).** Write the one-page hybrid Euler–Hadamard lemma in host notation, with the two-sided equivalence to zero-free half-planes. Give an Ω-type argument for the pointwise non-locality claim, which is conjectural. Source: CON-0013 and its correction; BRG-CAUSAL_EULER-O1.
- **J10 (§6, P3).** Do Vinogradov–Korobov inputs in host DC3/DC4 improve the line-one rate from exp(−c√(log X)) to exp(−c(log X)^{3/5}(log log X)^{−1/5})? This is an unchecked suggestion. Source: CON-0013(iv).

---

## Priority digest

P1 items:
- A1–A7, A9, A11, A17;
- B2, B6, B7;
- C1, C2, C5, C12;
- D1, D2;
- F1, F8;
- G4;
- H1;
- J4.

The verification gates (A) bound the status of everything else. Until A1–A7 and A9 are passed, no Observatory document should treat 11/12, 7/8, 2/3 or Siegel exclusion as a theorem.

