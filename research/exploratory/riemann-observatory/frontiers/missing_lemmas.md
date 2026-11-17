# Missing lemmas, route by route

```text
Status: SYNTHESIS (exploration layer). This file claims no new theorem. Every mathematical statement carries
        a status label (see the legend). Targets marked Observatory-proposed have not been reviewed outside the
        Observatory. RH is open. Quasi-RH (11/12, 7/8) and the 2/3 critical-line result are unrefereed 2026
        claims. The 11/12 paper was audited by the Observatory with no error found; the 7/8 paper was not
        audited, and its Lean formalization is claimed but has not been replayed.
Scope: thirteen routes (R1-R13) plus the six open cuts of the host repository (H1-H6). For each route the file
        gives the closing statement with quantifiers, whether it is RH-equivalent or genuinely weaker, the
        restricted versions already proved (with sources), and the smallest next lemma.
Exact sources or dependencies: frontiers/ledger.jsonl (LED ids; where a verifier corrected an entry, the
        corrected value is used); frontiers/research_programs.md (cited as "<AREA> frontier §n");
        connections/connections.jsonl (CON ids; the corrected form is used for every needs_correction item);
        connections/repository_bridge.jsonl (BRG ids); audits/verified_findings.md and
        audits/unresolved_findings.md (FND ids); audits/quasi_rh/DOSSIER.md ("QRH dossier");
        audits/claims_2026/CRIT23/DOSSIER.md and SIEGEL/DOSSIER.md; campaigns C1, C2, C4 and C5
        (REPORT.md together with SKEPTIC_REVIEW.md) and C3 (FINAL.md); history/abandoned_approaches.md;
        corpus/bibliography.jsonl (PAPER ids). Host OPEN_CUTS.md was read for the cut names only.
What was actually run: the files above were read. One mpmath script (scratchpad, python3 -I) re-evaluated
        these quoted closed forms: beta(n,h); B(l) = 11/12 - l/4; C_MT = 0.6725007037; lambda* = 0.5501939647;
        kappa_c = 2.1773190; 3 - 2*sqrt2 = 0.1715729; C(Delta); T0^2 = 9.0011e24; and the coincidence window
        0.4053787. Every value agreed with its source. Nothing new was proved, and no third-party code was run.
Smallest remaining gap: every "smallest next lemma" below is an open target, and none has been reviewed.
        Statements imported from unrefereed 2026 preprints keep their unrefereed status.
```

## Status legend

| Label | Meaning |
|---|---|
| THEOREM (refereed) | Published and refereed; the source is given |
| THEOREM (unrefereed) | A complete proof in a preprint that has not been refereed |
| AI-generated unrefereed | Manuscript produced by an AI model (OpenAI 2026 family 003). The AF paper is labelled AI-discovered, human-verified, unrefereed |
| CONDITIONAL | Proved assuming a named hypothesis |
| Observatory-proposed | Statement first written in this archive. It is unreviewed unless a skeptic or adjudicator verdict is quoted with it |
| [O] | An Observatory derivation inside a dossier: a sketch, not reviewed |
| HEURISTIC / CONJECTURE | As named |
| NUM-RIG / NUM-NONRIG | Ball or exact arithmetic / floating point or model computation |
| RH-equiv | The statement is equivalent to RH, in the stated normalisation |

Conventions used throughout:
- T0 = 3,000,175,332,800 is the rigorous verification height (LED-VERIF-1, PAPER-0001).
- Θ := sup Re ρ over the nontrivial zeros.
- QRH(θ) means no zero in Re s > θ for the stated family.
- Pos(L) means that W(g∗g̃) ≥ 0 for every g ∈ C_c^∞(−L, L), in the log variable, with W the Weil functional.

## Status of the 2026 inputs used below

| Claim | Source | Status |
|---|---|---|
| ζ and all Dirichlet L-functions (and finite-order Hecke L over Q(√−3)) are zero-free on Re s > 11/12 | OpenAI "paper2", PAPER-0161; LED-ZFR-2 | AI-generated unrefereed. Level-2 audited by the Observatory: no error found in the inspected portion (FND-0009). The imported metaplectic and large-sieve inputs were not re-proved |
| The same with 7/8 | PAPER-0528; LED-ZFR-1 | AI-generated unrefereed. **Not audited.** Lean claimed, not replayed |
| Refinements down to ≈0.8741 | Liu PAPER-0156 and PAPER-0157; Xu–Sang PAPER-0158; Chang–Wang; Liu hexagon B_tw = 0.8740585038 (ZFR frontier critique) | Unrefereed. All are conditional on the 7/8 inputs (LED-ZFR-3) |
| ζ_K ≠ 0 on Re s > 31/32 for every number field K | Cureton–Thorner (hexagon v2; v1 claimed 1 − 1/6000), per CON-0026 corrected | Unrefereed. Lean via AxiomProver claimed, not checked |
| ζ_{Q(i)} ≠ 0 on Re s > 599/600 | Ji, PAPER-0155 | Unrefereed. An independent route, resting on de Faveri's unrefereed density estimate |
| liminf N0^s/N ≥ 2/3 (flat window) and ≥ C_MT = 0.6725007; N_d/N ≥ 5/6 and 0.83625 | AF PAPER-0486 (AI-discovered, human-verified); LZ PAPER-0533 (human); LED-CRIT-1/2 | Unrefereed. The CRIT23 audit found no error affecting a stated result; one proof step was repaired (FND-0004) |
| 0.67353820 and 0.83900460 | Knausgård PAPER-0166; LED-CRIT-3 | Unrefereed, computer-assisted. Three searches were not replayed |
| (1−β) log q ≥ c for real zeros of real χ | OpenAI PAPER-0529; Banks PAPER-0160; Kerr PAPER-0164; Guo PAPER-0165; LED-LFUN-6 corrected | Unrefereed; AI-generated or AI-assisted. Audited with no error found (FND-0010). Constants: Guo 1/100 (1/64 in App. A); Banks 3.0·10⁻³ for q ≥ 10¹⁰, extended to all q via LZZ PAPER-0855 (refereed computation) |

## Summary table

| Route | Closing statement | RH-equivalent? | Best restricted result (status) | Smallest next lemma (status) |
|---|---|---|---|---|
| R1 Weil windows | Pos(L) for every L | RH-equiv | Pos((log 2)/2), THEOREM refereed (Yoshida; PAPER-0099). Pos(0.8), unrefereed computation (LED-POS-7) | A computer-free proof of Pos(L) for some window containing a prime; directed-rounding replay of Pos(0.8) (open) |
| R2 Operators | Positivity/unitarity of a spectral realization | RH-equiv in every form surveyed | S-local trace formula, THEOREM (LED-OPS-2) | A lower certificate for QW_λ at one λ² > 2 (open) |
| R3 de Branges | E_ξ Hermite–Biehler / Suzuki system extends to [0,∞) | RH-equiv; the de Branges sufficient conditions are false | Hamiltonian explicit for ω > 1 (LED-OPS-15) | An RH-equivalent, not merely sufficient, positivity on H(E_ξ) (open) |
| R4 Li/Keiper | λ_n ≥ 0 for every n | RH-equiv | RH(T) ⇒ λ_n > 0 for n ≤ T² (Oesterlé; C1-L2) | The converse semi-local Li theorem (open) |
| R5 Nyman–Beurling | d_N → 0 | RH-equiv | Burnol lower bound; C1-N1 floor | Full proof of the CON-0021 rate law (Observatory-proposed) |
| R6 Robin/Lagarias/Nicolas | σ(n) < e^γ n log log n for all n > 5040 | RH-equiv | Range 10^(10^13.11485); 21-free n | t = 22 via a certified Mertens-product bound at x ≈ p_k0 (open) |
| R7 de Bruijn–Newman | Λ ≤ 0 | RH-equiv (Λ ≥ 0 is known) | 0 ≤ Λ ≤ 0.2 | Persistence lemma CON-0008 (Observatory-proposed) |
| R8 Jensen/LP | J^{d,0} hyperbolic for every d | RH-equiv | d ≤ 9·10²⁴ for all shifts | A rigorous Jensen–heat bridge (C1-J2, heuristic now) |
| R9 Levinson + 2026 pair correlation | κ = 1 is not RH; θ = ∞ mean square ⇒ RH | Proportion route: weaker and never RH. θ = ∞: RH-strength | 0.6725 (unrefereed); 0.4173 refereed | ML-CGG / thin-box theorem (CON-0006, Observatory-proposed) |
| R10 Quasi-RH large sieve | Pointwise A_1(D) ≪ D^{1/2+ε} | GRH for the family member | 11/12 (audited, unrefereed); 7/8 (unaudited) | Quartic μ-removal identity / J4 (CON-0038) |
| R11 Zero density | DH: A(σ) ≤ 2 | Genuinely weaker | sup A ≤ 30/13; DH for σ ≥ 25/32 | Beat the mean-value theorem at σ = 7/10 (open) |
| R12 Function-field transfer | Effectivity/Hodge index on a surface over F_1 (ML-W) | RH-equiv (ML-W) | RH(C) ⇔ T_{2g} ⪰ 0 over F_q (C5) | ML-W0 model case (Observatory-proposed) |
| R13 Exceptional zeros (adjacent) | (1−β) log q → ∞; zero-free strip | Weaker than GRH | c = 1/64 (unrefereed) | A comparison chain reaching 1/5, or a proof that none can (open) |

---

## R1. Weil / explicit-formula positivity and finite windows

**Closing statement (RH-equiv; THEOREM refereed, Weil 1952 as reproved in Bombieri 2000, PAPER-0090 Thm 2).** For every L > 0, Pos(L). Equivalently RH ⇔ ∀L Pos(L).

**Restricted versions proved.**
- **Pos((log 2)/2).** The autocorrelation window (1/2, 2) contains no prime power.
  - THEOREM (refereed): Yoshida 1992 (PAPER-0667), with a finite calculation; Connes–Consani 2021 (PAPER-0099).
  - LED-POS-6; LED-OPS-5, corrected: Theorem 6.11 gives Sonin constant c = 4γ/log 2 ≈ 16.99 with an operator constant γ ≈ 2.94355, and the optimal constant lies in (13, 17).
- **Small support.** THEOREM (refereed; Bombieri 2000 Thm 12): if supp g ⊂ I with |I| < log 2, then W ≥ (log(1/|I|) − log log(1/|I|) − O(1))‖g‖². The O(1) is unspecified, so this alone does not certify the whole log 2 window (C4 skeptic).
- **Pos(0.8).** Unrefereed (Zhu 2026, LED-POS-7). The paper reports 8.9·10⁻¹⁸‖f‖² ≤ λ*(0.8) ≤ 2.27·10⁻¹⁷. The CON-0010 verifier classifies it as high precision with an error budget, not directed-rounding certification. Not replayed here.
- **Inertia for finite multisets.** THEOREM (refereed; Bombieri 2000 Thm 8): the number of negative eigenvalues of a finite truncation equals the number of distinct off-line conjugate pairs.
- **Exact detection criterion C4-C.** Observatory-proposed THEOREM; standard Schur/Sylvester argument; skeptic: upheld. Assume the real-zero form P is coercive on the window. Then the negative index of W on window L equals the number of negative eigenvalues of G⁻¹ + M, where G is the P-Gram matrix of the evaluation functionals at the non-real ordinates.
- **Growth detection C4-B.** Observatory-proposed THEOREM, conditional on the single-defect hypothesis H1 (one quadruple off the line, every other zero on it); skeptic: upheld with corrections.
  - Conclusion: λ_min(L) < 0 once L ≥ L_B(T, δ) = (1/(2δ))[log log T + log log log T + O_δ(1)].
  - At T = 3·10¹², L_B < L_N = (1/2) log(T/2π) for δ ≥ 0.2354 (skeptic correction).
- **Function-field analogue.** C5-T3 inertia (THEOREM) plus the skeptic's confluent version (THEOREM): RH(C) ⇔ T_{2g} ⪰ 0, with no squarefree hypothesis. Window theorem C5-ADJ-W (THEOREM, adjudicated; no RH, no Euler product, no squarefreeness): W ≥ 0 on C_c^∞(−a, a) ⇔ T_{⌈2a/log q⌉} ⪰ 0, so RH(C) ⇔ W ≥ 0 for one (every) a > (d − 1)(log q)/2, in particular a > (g − 1/2) log q; sharp over the formal class (C5-ADJ-SHARP; C5 FINAL §3.3–§3.4).
- **Reality theorem.** THEOREM per LED-OPS-7 (Connes–van Suijlekom, arXiv:2511.23257): a simple, isolated, even ground state of a window form forces all zeros of ξ̂ to be real, for every finite-prime window.

**Missing statements that are genuinely weaker but infinite.**
- (W-a) Pos(L) for all L ≤ L1, for some fixed L1 > (log 2)/2. This follows from RH. The sentence "no finite window implies RH over Q" is **false as stated** (C5-ADJ-LOG: an L0 with Pos(L) ⇒ RH for all L ≥ L0 exists, non-constructively). Its true content is that no explicit L0 is known, plus C5-ADJ-MODEL (THEOREM): zero-side window positivity with zeta-like counting (error O(T)) cannot force RH (C5 FINAL §3.5).
- (W-b) The three gaps of the Connes semilocal programme (OPS frontier §3), with (H1) + (H2) ⇒ RH (CON-0010 correction: Thm 6.1 plus Hurwitz):
  - (H1) simple, isolated, ι-even lowest eigenvalue of QW_λ for all large λ;
  - (H2) convergence of the normalized ground states in weighted L¹;
  - the lower-bound direction of the Fuchs ladder, uniformly in λ, prime terms included. The existing estimates assume QW_λ ≥ 0, which is circular (LED-OPS-9).
- (W-c) Connes–Consani Conjecture 4.1 for each q (C5-ML-C1, corrected reading): the factor h₁ is supported in (q^{−1/2}, q^{1/2}). For q = 3 the window is Pos((log 3)/2) = Pos(0.549). Zhu's unrefereed Pos(0.8) covers it numerically, so the content of the conjecture is the mechanism.

**Smallest next lemma.**
- **ML-R1a (open; OPS frontier §7, POS frontier §7(1)).** An unconditional proof, without computer certification of the continuum infimum, that Pos(L1) holds for some L1 > (log 2)/2. Equivalently, positivity of QW_λ for some λ² > 2, with a simple, isolated, ι-even ground state. CC Conj. 4.1 at q = 3 is the natural instance.
- **ML-R1b (open, computational; C5-ML-E1).** An independent directed-rounding Arb replay of Pos(0.8).
- **Proof of concept (Observatory-proposed; C5-ML-W0 with the skeptic's correction).** On the square of the scaling site, define Dim H⁰(D). Write the degree invariance under linear equivalence into (a)–(b). Show Dim H⁰(D(f)) + Dim H⁰(−D(f)) ≥ s(f, f) for f supported in [2^{−1/2}, 2^{1/2}] with ∫f d*u = ∫f du = 0. This would re-derive the known Pos((log 2)/2) by a Riemann–Roch mechanism. It makes no RH claim.

## R2. Hilbert–Pólya and operators

**Closing statement (RH-equiv).** There should be a Hilbert space and a self-adjoint operator whose spectrum is exactly the multiset {γ : ζ(1/2 + iγ) = 0}, or equivalently a *unitary* spectral realization. The content is positivity, because realizations without positivity exist unconditionally:
- THEOREM (refereed), Connes 1999 (PAPER-0026): critical zeros on a Sobolev-type space.
- THEOREM (refereed), Meyer 2005 (PAPER-0074): all zeros, on a non-unitary representation. LED-OPS-3 corrected: the obstruction is unitarity, not the impossibility of a Hilbert space.

The OPS frontier §3 finds five forms of the same RH-equivalent positivity:
- Weil positivity;
- Hermite–Biehler membership of ξ + ξ′;
- the canonical-system boundary at ∞;
- Lax–Phillips decay;
- W > 0 in intertwiner schemes.

**Restricted versions proved.**
- S-local trace formula for every finite S. THEOREM (refereed; LED-OPS-2). The global formula ⇔ RH is proved only in positive characteristic (Connes Thm 5). FND-0006: citations that attribute a number-field result misread the paper.
- Zeta-cycles. THEOREM per LED-OPS-4.
- Localized operators (Suzuki 2026, unrefereed). LED-OPS-11: real simple spectrum for every window. LED-OPS-12: CONDITIONAL on RH, t_{a,n} ↓ γ_n.
- Upper bound ε_λ ≤ Cδ₄(λ)(log λ)³ with δ₄(λ) ~ c₄λ⁹e^{−4πλ²}. Unrefereed theorem of Connes–Kastoris as stated in Andrews–Connes–La Gatta, PAPER-0544 (LED-OPS-9).

**Missing.** All five forms are RH-equivalent. The weaker infinite targets are those of R1 (W-b).

**Smallest next lemma (open; OPS frontier §7).** Either of:
- A rigorous **lower** certificate: QW_λ > 0 on L²([1/λ, λ], d*u), with a simple, isolated, ι-even ground state, for one λ with λ² > 2 (for example λ² = 3, S = {∞, 2, 3}).
- A two-sided Fuchs-ladder estimate c₁δ₄(λ)/λ^A ≤ ε_λ(1) ≤ Cδ₄(λ)(log λ)³ together with a gap ε_λ(2)/ε_λ(1) ≥ cλ⁴, on an unbounded λ-range that includes the prime terms.

At any fixed λ neither is RH-equivalent. Galerkin truncations cannot supply either (BRG-OPERATORS_HEAT-O3).

## R3. de Branges spaces and canonical systems

**The original sufficient conditions are false.** THEOREM (refereed; Conrey–Li 2000, PAPER-0779; C3 §3.1). For E(z) = ξ(1 − iz), with ξ normalised as s(s−1)π^{−s/2}Γ(s/2)ζ(s), the hypotheses of de Branges' Theorem 1 hold. But his conditions (3.1) and (3.3) are false:
- −Re{ξ′(ρ₃₄)ξ(1 + ρ₃₄)} = −5.389…·10⁻⁶⁹;
- Re{ξ(1 + 282i)/ξ(2 + 282i)} = −0.000131957….

The same holds for χ₋₄. FND-0013 (valid_with_stronger_consequences) records failure at 195 of 2000, 2724 of 20000 and 15567 of 100000 zeros. C3-ADJ-S (THEOREM, Observatory, adjudicated) gives the exact rule: P_n < 0 ⇔ S(γ_n) − δ(γ_n) ∈ (3/4, 7/4) mod 2.

**Remaining closing statements (RH-equiv).**
- (i) Hermite–Biehler membership of E_ξ = ξ + ξ′. LED-OPS-14, corrected: E_h(s) = ξ(h + s) is a structure function unconditionally for h ≥ 1/2, and under RH for h > 0.
- (ii) Suzuki's canonical system (LED-OPS-15; PAPER-0812). The Hamiltonian is explicit for ω > 1, and RH ⇔ the solution extends to [0, ∞).
- (iii) Graded form. THEOREM (refereed; Suzuki, PAPER-0101, Thm 11.1, confirmed by the CON-0007 verifier): ξ ≠ 0 on Re s > 1/2 + ω ⇔ Ψ_ω ≥ 0 for t ≥ t₀. Ψ_ω ≥ 0 holds unconditionally for ω ≥ 1/2.
- CONDITIONAL on unrefereed QRH(7/8): Ψ_{3/8} ≥ 0. CON-0007 corrected calls this an immediate corollary, not a new result.

**Genuinely weaker statements.** Statements strictly weaker than (iii) at a fixed ω < 1/2 are not known; at level ω the route needs QRH(1/2 + ω) (CON-0007(a)).

**Smallest next lemma (open).** Identify a positivity condition on H(E_ξ) that is RH-equivalent, not merely sufficient, and check it against one off-line pair (BRG-OPERATORS_HEAT-O6). Smaller targets concern the obstruction itself:
- C3 §9(3): the analogue of Conrey–Li Theorem 2 in argument form, i.e. Re{ξ(1+it)/ξ(2+it)} < 0 ⇔ −π/4 + arg ζ(1+it) − arg ζ(2+it) + O(1/t) ∉ [−π/2, π/2] mod 2π. Observatory-proposed, not done.
- Infinitely many failures of the zero condition (see the questions file).

## R4. Li / Keiper

**Closing statement (RH-equiv).**
- THEOREM (refereed; Li 1997, PAPER-0193): λ_n ≥ 0 for every n ≥ 1.
- Sharp form, THEOREM (refereed; Arias de Reyna, LED-POS-4): RH ⇔ Σ y_n² < ∞.

**Restricted versions proved.**
- **Implication horizon.** Oesterlé 2000 (unpublished, quoted by Voros PAPER-0005 and later): RH(T) ⇒ λ_n ≥ 0 for n ≤ T².
- **Independent explicit proof, C1-L2.** Observatory THEOREM; skeptic verdict "prior_art_found (mathematically upheld)". For T ≥ 100, RH(T) ⇒ λ_n > 0 for 1 ≤ n ≤ T². At T0 this covers n ≤ 9.0011·10²⁴ (LED-POS-2).
- **Computation.** λ_n > 0 for n ≤ 10⁵ (Johansson; LED-POS-1). This is already implied by RH below height 317 (C1-L2(ii)).
- **Uncertainty scale.** Voros: λ_n detects 1/2 + t + iT only for n ≳ T²/|t| (POS frontier §5(5)).
- **Single-defect model.** C1-L3, HEURISTIC + NUM-NONRIG: n* = X[log X + 2 log log X − log 4 + o(1)] with X ≍ T²/δ. At T0 with δ_max = 0.49374, n* ≈ 1.19·10²⁷. The leading formula runs 11–12% low at T0 (skeptic).

**Missing statements that are genuinely weaker.**
- (Li-a) The converse semi-local theorem: λ₁, …, λ_N ≥ 0 ⇒ no zero with β ≠ 1/2 and |γ| ≤ c√N up to logarithms. Brown 2005 (PAPER-0600, Thm 2) needs repair (POS frontier §7(2)).
- (Li-b) Extend Theorem L1 to n ≤ cT² log T. C1-L4 (PROPOSITION-PROOF-SKETCH; skeptic stress test: failure at 4.7–5.2·T² log T) indicates that no argument using only RH(T) plus zero counting gets past order T² log T.

**Smallest next lemma (Observatory-proposed, open).** A complete two-way finite statement: [RH(T) ⇒ λ_n ≥ 0 for n ≤ T²] together with [λ_n ≥ 0 for all n ≤ N ⇒ β = 1/2 for every zero with |γ| ≤ c N^{1/2}(log N)^{−A}], with explicit c and A.

## R5. Nyman–Beurling / Báez-Duarte

**Closing statement (RH-equiv; THEOREM refereed, Báez-Duarte 2003, PAPER-0004).** χ_(0,1] lies in the L²(0,∞)-closure of span{ρ_a(x) = {1/(ax)} : a ∈ ℕ}, equivalently d_N → 0.

**Restricted versions proved.**
- Burnol (PAPER-0606), THEOREM (refereed): liminf_N d_N² log N ≥ Σ_ρ m_ρ²/|ρ|².
- CONDITIONAL asymptotic: d_N² ~ (2 + γ − log 4π)/log N (LED-POS-16).
- C1-N1, Observatory THEOREM (classical method; skeptic upheld, error term O(1/T²)): an off-line pair with Re ρ₀ = 1/2 + δ forces ‖χ − f‖² ≥ F = (4δ/T²)(1 + O(1/T²)) for every f in B_λ.
- Graded L^p version (Beurling 1955): density in L^p ⇔ ζ ≠ 0 on Re s > 1/p, with the restriction Σ b_k/θ_k = 0 (CON-0007 correction (3)). Graded natural-integer criteria for every 1/p ∈ (1/2, 1) already exist (Dimitrov–Oliveira, arXiv:1608.07887; CON-0007 and CON-0010 corrections).
- CONDITIONAL on unrefereed QRH(7/8): d_n(ζ, 8/7) → 0.

**Missing statements that are genuinely weaker.** Rate statements. CON-0021 (tested_supported; the proposition itself is not reviewed): for α ∈ (Θ, 1), limsup_n log s_n(α)/log n = −2(α − Θ), hence RH ⇔ s_n(α) ≪ n^{1−2α+ε}. The qualitative part already follows from Balazard–Saias 1998; only the exponent is new.

**Smallest next lemma.** Write CON-0021(a)–(b) as a 3–4 page proof (Observatory-proposed; verifier: sound_and_useful), including:
- the explicit Perron remainder;
- uniformity in α;
- at α = 1, bounding (M_n(s) − M_n(1))ζ(s) on |t| ≤ 1, as the verifier's correction (1) requires.

## R6. Robin / Lagarias / Nicolas

**Closing statements (RH-equiv).**
- σ(n) < e^γ n log log n for all n > 5040. THEOREM (refereed; Robin 1984, PAPER-0206).
- Lagarias' inequality. PAPER-0490.
- N_k/φ(N_k) > e^γ log log N_k for every primorial N_k. THEOREM (refereed; Nicolas 1983, PAPER-0232; LED-ARITH-6).

**Restricted versions proved.**
- Robin for 5040 < n ≤ 10^(10^13.11485). Rigorous computation (Morrill–Platt, PAPER-0590; LED-ARITH-1 corrected: the gain over Briggs is ×1303 in log₁₀ N). It is a finite computation and carries no global information.
- Robin for every 21-free n ≥ 5041. THEOREM (Axler 2023, LED-ARITH-2), re-proved by Assani–Chester–Paschal 2026.
- σ(n)/n < (1 + 3.15367·10⁻⁷)e^γ log log n outside an explicit finite set. THEOREM (LED-ARITH-4; the description of the exceptional set is corrected there).

**Missing statements that are genuinely weaker and infinite.**
- (Rob-a) Robin for every t-free n, for t = 22, 23, …. Each is weaker than RH (CON-0010).
  - ARITH frontier critique: the binding region is x ≈ p_k0 = 29,996,208,012,611. There, Axler's uniform Mertens-product bound has relative error ≈ 3.05·10⁻⁷, against the needed ≈ 2^{−22} ≈ 2.4·10⁻⁷.
  - The heuristic perfect-information ceiling of the t-free method is t ≈ 26 at the current range.
- (Rob-b) An explicit implication horizon: RH(T) ⇒ the criterion for x (Nicolas) or log n (Robin) ≤ X(T) ~ T²/log² T. C1-D3 (sketch): about 4.4·10²³ at T0.
- CON-0002 and CON-0003 in corrected form: thresholds from partial RH plus a zero-free half-plane are pre-proof estimates (±30%), pending an explicit R(x) bound from x₀ = 3·10¹³.

**Smallest next lemma (open).** A certified unconditional bound for e^{−γ}∏_{p≤x} p/(p−1)/log θ(x) − 1 with relative error below ≈2.4·10⁻⁷, uniformly for x ≥ p_k0. Beyond x ≈ 10²⁶, existing ε-bounds of order ≲10⁻¹² suffice (ARITH critique (1b)). This would give t = 22.

## R7. de Bruijn–Newman

**Closing statement (RH-equiv).** Λ ≤ 0. Together with Λ ≥ 0 (THEOREM refereed; Rodgers–Tao, PAPER-0036; LED-DBN-6), RH ⇔ Λ = 0.

**Restricted versions proved.**
- Λ ≤ 0.2. THEOREM (refereed; Platt–Trudgian, PAPER-0001; LED-DBN-10).
  - Caveat (DBN frontier critique; LED-DBN-9 corrected): this rests on Polymath Table 1 row 2. There the canopy is documented only by a lower bound at N = N₀ and the authors' statement that they expect to be able to verify it.
- Λ ≤ 0.22. THEOREM (refereed; Polymath, PAPER-0083).
- Λ < 0.156821. Unrefereed (Planat–Raymond; LED-DBN-12). FND-0011: not verified; the certificate was not replayed.
- Further unrefereed claims: 0.149396 and others (LED-DBN-11, LED-DBN-13).
- Λ ≤ 0.108–0.14 under H7/8. Unrefereed and CONDITIONAL on the unrefereed half-plane (LED-DBN-15).

**Missing statements that are genuinely weaker.**
- (dBN-a) **Persistence lemma** (CON-0008: tested_supported, verifier sound_and_useful; outline only). There are absolute c, γ₀ > 0 such that ζ(1/2 + δ + iγ) = 0 with γ ≥ γ₀ implies Λ ≥ cδ²/(log γ)². CONJECTURE: the sharp form is Λ ≥ c·min(δ², δ/log γ).
- (dBN-b) An explicit Polymath scaling: if every zero with 0 < γ ≤ T is on the line, then Λ ≤ A/log T for T ≥ T₀, with A ≈ 5 explicit. Open; Polymath §10 gives it only as a heuristic.
- (dBN-c) Λ_χ ≤ c < 1/2 uniformly in the conductor. Open (DBN frontier §7(3)).

**Smallest next lemma.** Make the CON-0008 window-energy argument rigorous:
- an a.e. ODE for E(t) between collision times;
- continuity at collisions via Polymath Prop. 3.1(ii);
- a far-field H_t′/H_t bound at distance ≍ 1 for 0 < t ≤ 1/2, which goes beyond Polymath Thm 1.5(iv) (verifier note);
- an explicit constant.

Model-world calibration (C1-E1, HEURISTIC, skeptic upheld with corrections): a quadruple at T0 collapses by t_c ≤ 0.10130. So Λ ≤ 0.2 excludes nothing above T0, and Λ ≤ 0.2 is in any case derived from RH(2.51·10¹²).

## R8. Jensen / Laguerre–Pólya

**Closing statements (RH-equiv).**
- J^{d,0}(ξ) is hyperbolic for every d. THEOREM: Pólya; GORZ, PAPER-0024.
- Equivalently Ξ ∈ LP.
- Equivalently L_n[Ξ](x) ≥ 0 for all n and all real x (Csordas–Varga, PAPER-0614).

**Restricted versions proved.**
- J^{d,n} hyperbolic for all n ≥ 0 when d ≤ 9·10²⁴. THEOREM (refereed; GORTTW 2022, PAPER-0087, via Chasse PAPER-0871 and Platt–Trudgian). LED-POS-9 corrected: the record belongs to GORTTW 2022, not Ono 2026.
- Shift threshold N(d) = O_ε(d^{1/2+ε}). THEOREM (Kim–Lee; ineffective; LED-POS-10 corrected: published GORTTW gives c·e^d, arXiv v3 gives c·e^{d/2}).
- Turán and higher Turán inequalities for d = 2, 3 at all indices. LED-POS-12; PAPER-0583, PAPER-0681.
- The unshifted J_d has at least d − C√(d log d) real zeros. Unrefereed (LED-POS-11 corrected).
- L_n[Ξ](x) ≥ 0 for |x| ≤ T0 − 1/2. Unrefereed (Sra; LED-POS-14). The global L₁ ≥ 0 is open.
- D_{r,k} > 0 for k ≥ 10¹⁸r³, and infinite log-concavity of λ_n. Unrefereed (LED-POS-13).

**Missing statements that are genuinely weaker.**
- (J-a) A converse semi-local Jensen theorem: hyperbolicity of J^{d,0} for all d ≤ D ⇒ RH up to height f(D) → ∞. Farmer suggests f(D) ≈ c√D at best (POS frontier §7(3)).
- (J-b) Global L₁[Ξ](x) ≥ 0 for |x| ≥ X₀ without new zero input (POS frontier §7(5)).
- (J-c) D_{r,k} > 0 for k ≥ C r^{1+δ} with δ < 2 (POS frontier §7(4)).

**Smallest next lemma (Observatory-proposed; currently HEURISTIC).** Make the C1-J2 Jensen–heat bridge rigorous: hyperbolicity of J^{d,0} near height T is equivalent to real-rootedness of H_{T²/(2d)} near T, up to O(T³/d²).
- Validation so far: exact thresholds for Farmer's toys X_j (j = 10: 120; j = 20: 750 or 478 depending on configuration) are Arb-certified by two independent algorithms (C1-J3).
- Predictions agree within 2.6%.
- The skeptic corrects the claimed agreement "<0.3% in 24 cases" to "≤1.03% in 20 comparable cases".

## R9. Levinson / mollifier and the 2026 pair-correlation critical-line route

**What would close what.**
- A proportion κ = 1 is **not** RH. Density currency: even 1 − o(1) allows o(N(T)) off-line zeros (CON-0030 corrected: a formalisation of folklore; C3-D9).
- The RH-strength input. THEOREM (refereed; Bettin–Gonek 2017, PAPER-0064): if ∫₀^T |M_Nζ(1/2+it)|² dt ≪ T^{1+ε} uniformly for N ≤ T^θ, then ζ ≠ 0 on Re s > 1/2 + 1/(2θ). For arbitrarily large θ this is RH. So the θ = ∞ conjecture (Farmer) is at least as hard as RH.

**Restricted versions proved.**
- Mollifier lengths: θ < 4/7 for structured coefficients (Conrey 1989, PAPER-0191); θ < 17/33 for generic coefficients (Bettin–Chandee–Radziwiłł, PAPER-0244). LED-CRIT-7 corrected: 48/95 is unpublished.
- κ ≥ 0.417293962 and κ* ≥ 0.407511457 (PRZZ, PAPER-0045), refereed, jointly with Wu (PAPER-0988: κ > .4172, κ* > .4074) (LED-CRIT-4 corrected).
- θ = 1 gives κ ≥ 0.6107. CONDITIONAL (Feng, PAPER-0046; LED-CRIT-8).
- 2026 route: κ* ≥ 2/3 (flat window) and ≥ C_MT = 3/2 − cot(1/√2)/√2 = 0.6725007, with N_d/N ≥ 5/6 and 0.83625. Unrefereed (AF PAPER-0486; LZ PAPER-0533; CRIT23 dossier).
  - Mechanism: Montgomery's second moment over all zeros, plus an inertia / rank–trace inequality.
  - Analytic input: the BGSTB24 lemma (PAPER-0053). The proof of BGSTB24 Thm 1 was corrected in v3, and Lemma 5 survives (LED-CRIT-2, LED-CRIT-13).
- CONDITIONAL thin-box results: 2/3 for b = 0.3185; 100% under the pair correlation conjecture without RH (LED-CRIT-13).

**Missing statements for going beyond 0.6818.** These are genuinely weaker than RH; any one would suffice (CRIT frontier §7(2); CRIT23 §8(7)).
- (L-a) Unconditional **upper** information on the all-zeros form factor F(α) for some α > 1, even averaged over [1, 1+δ]. The CRIT23 check (D) shows what support Δ would give, under the hypothetical form factor min(|α|, 1): C(Δ) = 1 + 1/(3Δ²), giving 0.852 at Δ = 3/2 and 0.917 at Δ = 2.
- (L-b) An RH-free third trace at X ≍ T. Prime-side evaluation of tr G̃^k is available unconditionally only in the range X^k ≤ T^{2−ε} (AF §7.2(e), author-stated).
- (L-c) **ML-CGG** (CON-0006 corrected; Observatory-proposed): Σ_{T<γ≤2T, β≠1/2} |Bζ′(ρ) − Bζ′(1−ρ̄)|² = o(T(log T)³) for the Bui–Heath-Brown mollifier with θ → 1/2. With BHB Lemmas 1–2 it gives liminf N*/N ≥ 19/27. It is strictly weaker than RH.

**Conditional theorem available now** (CON-0006(c), Observatory-proposed; the verifier says it stands).
- Hypothesis: every zero with T < γ ≤ 2T satisfies |β − 1/2| ≤ η(T)/(log T)^{3/2}, with η → 0.
- Conclusion: liminf N*(T)/N(T) ≥ 19/27.
- Thresholds in absolute form, D ≤ ηTL³: η < 0.01315 beats 0.6725; η < 0.01074 beats Knausgård's simple-anywhere 0.67800919; η < 0.0091 beats 0.6818.

**Smallest next lemmas.**
- (i) Write inequality (*) and theorem (c) of CON-0006 as a referee-ready note. Fix the local-count convention.
- (ii) Run the periodic-configuration ceiling LP for ξ′ (CON-0015, sound_and_useful). It decides whether any bandwidth-one certificate can make "simple and on the line" for ξ′ exceed Wu's 0.86957; the window class saturates at 0.868642.
- (iii) GL(2). Assume the all-zeros pair-sum asymptotic for one newform with Fourier support < 1/2. Then liminf N_d/N ≥ 1/R*_{1/2} = 0.461688 (CON-0035 corrected; Observatory-proposed). Simple critical zeros need bandwidth > λ* = 0.5501939647 for this window certificate (CON-0011 corrected).
- (iv) Family average (CON-0036 corrected). The needed lemma is an explicit Petersson diagonal statement: Σ_f ω_f|Σ_{p≤X} a_p λ_f(p)|² = (1 + O((X/N)^{k−1}N^ε))Σ|a_p|² for X ≤ N^{1−ε}.

## R10. The quasi-RH large-sieve route

**Closing statement for the critical line (GRH for the family member).** For the sextic architecture this is the pointwise bound A_1(D) = Σ μ(𝔫)ν(𝔫)W(N𝔫/D) ≪ D^{1/2+ε} for every smooth W. CON-0009 (sound_but_known; downgraded by the verifier to "within uniform-trivialising-row mean-square extractions") records this. The route is therefore not structurally able to reach 1/2 inside that class.

**Exponent bookkeeping.**
- Extraction lemma (paper2 l.694–724; QRH dossier §4.1; algebra checked symbolically):
  - β(n, h) = 1/2 + h(n−1)/(2n);
  - β(6,1) = 11/12, β(4,1) = 7/8, β(3,1) = 5/6, β(2,1) = 3/4.
- [O] h ≥ 1 is forced in the paper2 architecture.
- [O] In the 7/8 system, B(ℓ) = 11/12 − ℓ/4 with ℓ < 1 − |b|, so B > 2/3.

**Missing statements that lower the exponent.** All CONJECTURE; the implications are [O] (QRH dossier §4.3).
- **(C1) Sub-diagonal sextic Möbius mean square, 0 < h < 1.** Over K = Q(√−3), Σ_{0<N(u)≤D^h} |Σ_{(𝔫,S)=1} μ(𝔫)ν(𝔫)(u/𝔫)₆W(N𝔫/D)|² ≪ D^{1+h+ε}.
  - It implies zero-freeness on Re s > 1/2 + 5h/12: h = 9/10 gives 7/8, h = 3/5 gives 3/4.
  - It is implied by GRH for the twists.
  - It lies beyond the large-sieve barrier and needs cancellation between the dual diagonal and the off-diagonal.
- **(C2) Full-row mean squares of order n < 6.** n = 4 over Q(i) gives 7/8; n = 3 over K gives 5/6; n = 2 gives 3/4. Each needs a duality partner that removes μ. Explicit n-fold metaplectic theta coefficients are known only for n = 2, 3 (standard; not re-verified).
- **J4 (CON-0038, sound_and_useful; credited to QRH dossier §4.1 (C2)).** Over K = Q(i), suppose Σ_{0<N(u)≤X^h} |A_u(X)|² ≪ X^{1+h+ε} for some 1 ≤ h ≤ 10/9, with A_u(X) = Σ_{(𝔫,1+i)=1} μ_K(𝔫)(u/𝔫)₄W(N𝔫/X). Then ζ_{Q(i)}, and hence ζ, has no zeros on Re s > 1/2 + 3h/8 (≤ 11/12).
- **(C3) Inputs for the 7/8 system.** Any of:
  - (a) a count for the critical class (δ_c, x = 1/2) with exponent < 2/3;
  - (b) the plain fourth moment at κ < 13/18;
  - (c) a direct estimate that breaks B(ℓ) = 11/12 − ℓ/4.

**Restricted versions.** These are the claims in the 2026 table above. Liu's "optimality" (PAPER-0156 Thm 34.4; PAPER-0157 Thm 14.13) is optimality of a fixed inequality system. It has been bypassed several times (ZFR frontier critique), so it is not a barrier.

**Smallest next lemmas (open; QRH dossier §5).**
- (i) State as a separate checkable theorem the density-hypothesis consequence of Prop. 3.1 for the sextic family: #{u₀ ~ U : the twist has a detectable zero with β ≥ σ} ≲ U^{2−2σ+ε} (HEURISTIC now).
- (ii) A quartic μ-removal identity for angular-weight-1 quartic Kubota coefficients, analogous to eq:gj (CON-0038, next step (3)).
- (iii) Prove that the custom `LFunction` in the HeckeSevenEighths challenge equals the Dirichlet series on Re s > 1 (dossier §1.3).

## R11. Zero density

**Closing statement (genuinely weaker than RH).** The density hypothesis A(σ) ≤ 2 for all σ ∈ [1/2, 1). It is implied by Lindelöf (LED-ZDE-14). RH gives N(σ, T) = 0 for σ > 1/2.

**Restricted versions proved.**
- sup A ≤ 30/13, attained at σ = 7/10. THEOREM (refereed; Guth–Maynard, PAPER-0054; LED-ZDE-1, whose history is corrected).
- A(3/4) ≤ 20/9 (LED-ZDE-3).
- DH on {1/2} ∪ [25/32, 1) (LED-ZDE-4 corrected; Bourgain, PAPER-0312).
- Family exponent A = 7/3. Unrefereed (CGL, PAPER-0745; LED-ZDE-11).
- CONDITIONAL on QRH(θ), N(σ, T) = 0 for σ > θ. This does not touch sup A at 7/10 (CON-0028, sound_but_known).

**Missing statement and smallest next lemma (open; ZDE frontier §7(a) and its critique).** For 1-bounded coefficients near (σ, τ) = (7/10, 13/10), prove LV(σ, τ) < τ + 1 − 2σ, i.e. |W| ≤ N^{9/10−δ} at σ = 7/10, T = N^{13/10}. Three Guth–Maynard terms are tangent to the mean-value bound at T = N^{6/5}. This would also be the first improvement on Ingham anywhere in σ < 7/10.

## R12. Function-field transfer

**Closing statement over Q (RH-equiv; C5-ML-W, a faithful restatement of Connes 2016).** Find a real space E with a symmetric form, isotropic ξ₀ and ξ₁ with ⟨ξ₀, ξ₁⟩ = 1, and a map D with ⟨Df, Dg⟩ = 2s(f, g), satisfying the **effectivity axiom**: every x with ⟨x, x⟩ > 0 has ⟨x, ξ₀ + ξ₁⟩ ≠ 0. Connes' lemma then gives RH. All the content is in proving effectivity.

**Function-field facts.** THEOREM (C5-T1, T2 and T3; skeptic upheld):
- Weil's two proofs feed one Gram matrix G = (q^{min(m,n)}s_{|m−n|}).
- RH(C) ⇔ T_N ⪰ 0 for all N ⇔ |N_k − q^k − 1| ≤ 2g q^{k/2} for all k.
- RH(C) ⇔ T_{2g} ⪰ 0, a single finite check (confluent version, skeptic §3.1).

**Missing statements that are genuinely weaker** (C5 open targets; each CONJECTURE / open):
- ML-W0, the model case (see R1).
- ML-C1, semilocal Weil positivity at q = 3.
- ML-F1: an intrinsic definition of Δ·Ψ(λ) in some F₁-framework that equals the explicit-formula distribution of CCM 2009 Prop. 7.2.
- ML-TP: one cohomology on Spec ℤ̄ with the full Euler product as a ratio of regularised determinants.
- ML-Den: a quaternionic (category K_R) structure for one H₈ field with W(π) = −1. By OB-4 no real structure exists.
- ML-S(ii): Pritsker's problem, weights w_n with B(w_n) → 1, i.e. an elementary PNT via Gelfond–Schnirelman. C5 skeptic: "cannot even give the PNT" holds only for fixed weights.

**Smallest next lemma.** ML-W0 (Observatory-proposed): reproduce a known positivity by a Riemann–Roch mechanism before attempting any new one.

## R13. Exceptional zeros (adjacent route; SIEGEL dossier)

**The claim.** Unrefereed; see the 2026 table: there is an absolute c > 0 with (1 − β) log q ≥ c for every real zero β of every primitive real L(s, χ), q ≥ 3. It is a trivial corollary of QRH(7/8), with c = (log 3)/8 = 0.1373 [O], but the four audited proofs do not use QRH.

**Missing stronger statements (not reachable by the method; SIEGEL §7.5).**
- (1 − β) log q → ∞;
- a fixed zero-free interval [1 − η, 1);
- Chowla positivity on (1/2, 1).

**Smallest next lemma (open; SIEGEL §8(4)).**
- Replace Guo's trivial character-sum remainder by an explicit Pólya–Vinogradov bound, so that y moves from q^{2+} toward q^{1+}.
- Or prove that no comparison of Lemma 5.1 type reaches 1/5. The auditor's ceiling with ideal arithmetic and hypothetical y → q is 3 − 2√2 = 0.1716.

---

## H. Host-repository programmes (OPEN_CUTS §1–§6)

The statuses below are those of the BRG verifications. None of them is a reviewed host result.

| Cut | Missing statement (quantified) | RH-equivalent? | Restricted / conditional facts | Smallest next lemma |
|---|---|---|---|---|
| H1 Fixed-detector negative mass | ∫₁^Y F₋(x) dx/x = O_ε(Y^ε) for every ε > 0, for one fixed zero-safe detector F | RH-equiv for each detector whose converse has been checked: rows 2/3, W_X, C_m, H^[1], MWOC (BRG-MELLIN_WAVELET-O3 corrected). Graded: Y^{θ+ε} ⇔ zero-free Re s > 1/2 + θ for those detectors, so at least as hard as QRH(1/2 + θ) | CONDITIONAL on unrefereed QRH(7/8): the graded premise holds at θ = 3/8 + ε (CON-0007(b), corrected). Ingham obstruction to pointwise eventual sign (BRG-MELLIN_WAVELET-O1, BRG-SHARP_NATIVE-O1) | For each remaining detector in the class, write the converse (partial summation from M(x) = O(x^{Θ+ε}), simpler than Titchmarsh §14.2) so that the per-detector equivalence is explicit. Or produce a counterexample to a proposed intermediate bound |
| H2 Unbounded arithmetic tails | A Robin tail theorem for the canonical class with unbounded support and exponents; growing-prime uniformity beyond fixed P₆₁ | Full form RH-equiv (Robin; BRG-ROBIN-O1 corrected: the extra Ω statement is the "Robin ⇒ RH" ingredient) | Every exact-prefix subtree has an unconditional margin factor < 1, but it is non-uniform in the cap A (BRG-ROBIN-O3 corrected). The t-free method stalls at t = 21 (O4). Smooth numbers: under unrefereed QRH(7/8), Ψ(x,y) ~ xρ(u)K(·) and Ψ ≥ xρ(u) for y ≥ (log x)^{8+ε}; c ∈ [2, 8] stays open (CON-0005 corrected) | A lemma with explicit dependence on (prefix, cap A), e.g. t = 22 via R6's Mertens-product bound. Or an exact finite certificate on a declared range |
| H3 All-order / full-domain positivity | (a) Pick: low order to the full hierarchy. (b) Energy-Schur: a continuum lower certificate, then an unbounded prescribed family of full windows. (c) First-Hermite: the whole complement of the proved region | All-order versions RH-equiv | Zhu's barrier for pointwise-envelope certificates (BRG-OPERATORS_HEAT-O1; it does not cover non-envelope routes). Margin collapse (O2). Galerkin gives upper sections only (O3). Λ ≥ 0, so heat positivity must use an input that backward deformation destroys (O4, assuming a strip bound and subquadratic counting for H_t, t < 0) | One error-enclosed lower certificate for one window containing a prime (R1/R2). Determine whether the safe-axis Kwong hierarchy disperses information like Jensen (order ~T²) or concentrates it like PF_k (BRG-XI_PICK-O2, O7) |
| H4 Xi derivative descent | Uniform signed transport between adjacent derivative orders, with the complete source and endpoint/winding terms | Not determined. A raw-innerness premise may already imply RH (host statement) | The high-derivative regime is RH-blind (BRG-XI_PICK-O3: Kim 1996, Gunns–Hughes). The de Bruijn–Newman constants are monotone along derivatives (O4; the fixed-margin ban is a heuristic reading). Farmer's X₁₀ defeats naive descent (O2) | One adjacent-order inequality with quantified loss that provably fails for X₁₀ and for H_t with t < 0 (it must, or it proves too much; C3 checklist items 3, 18) |
| H5 Principal-member transfer | A family, function-field or generalized-object estimate converted into an estimate for the principal arithmetic source | A subpower principal extraction is RH-strength (BRG-FAMILIES-O3, a heuristic per its correction) | Orthogonality controls only what is put in (O3, O7 corrected). Family nonvanishing sits at 1/2 − ε while 1/2 + ε is needed (O4). ILS positivity needs GRH (O5). Deuring–Heilbronn propagation is repulsive (O6). Over F_q the mechanism is cohomological and gives Ramanujan-type control over Q (O9; C5-OB7). Family averages can be unconditional while the member stays hard (BRG-MELLIN_WAVELET-O7 corrected) | One checked source adapter, or an explicit relative error bound in the required depth regime (host wording) |
| H6 Corrected Euler products below Re s = 1 | Local boundedness of the corrected products, together, on compacta of Re s > 1/2 | Boundedness on compacta of Re s > σ₀ ⇔ ζ ≠ 0 there (BRG-CAUSAL_EULER-O1 corrected; Akatsuka PAPER-0227 needs convergence to a nonzero limit). Already stated in host pass7 PROOF.md §8 (CON-0013) | CONDITIONAL on unrefereed 11/12: holds on Re s > 11/12 with discrepancy X^{11/12−σ+ε} (CON-0013(iii)). On the line, convergence is DRH-strength (O6). Ω-bounds cap any rate (O2). There is a zero-counting obstruction to uniform approximation (O4) | A one-page lemma in host notation: corrected product = ζ^{±1}·exp(±Z_X)·E_X with Gonek smoothing, plus the two-sided equivalence, filed as a separately labelled proposed object (CON-0013 next step). The pointwise non-locality claim stays conjectural until an Ω-type argument is written |

## Cross-route remarks

1. **Every closing statement above is RH-equivalent except two kinds:** zero density (R11), and the density-currency targets (R9), which can never give RH. The useful work is therefore on the genuinely weaker infinite statements:
   - W-a/W-b/W-c, Li-a, Rob-a, dBN-a/b/c, J-a/b/c, L-a/b/c;
   - C1–C3 and J4;
   - ML-W0 and ML-C1.
2. **Graded statements coincide with quasi-RH.** Suzuki's Ψ_ω, Beurling L^p density, the host H1 graded premise and the host H6 graded boundedness are all equivalent to, or implied by, QRH(1/2 + ω) (CON-0007 corrected). None has a route-internal missing lemma weaker than quasi-RH at that level.
3. **The verification gates come first.** No route should cite 11/12, 7/8, 2/3 or Siegel exclusion as a theorem until the gates in `frontiers/unsolved_questions.md` §A are passed.

