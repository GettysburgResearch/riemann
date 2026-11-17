# Top 25 research opportunities

```text
Status: SYNTHESIS / OBSERVATORY-PROPOSED agenda (exploration layer). A ranked list of targets, not of results.
        RH is open. Every target keeps the status of its inputs: the 2026 half-planes, the 2/3 theorem and Siegel
        exclusion are unrefereed claims; targets marked Observatory-proposed have not been reviewed outside the
        archive. Ranks and difficulty estimates are the synthesizer's judgement (HEURISTIC).
Scope: 25 opportunities drawn from the campaigns' FINAL.md next steps, the audit dossiers' next steps, the
        verification gates (frontiers/unsolved_questions.md §A), the verified connections, missing lemmas,
        ranked directions D-01..D-36 and actionable conjectures AC-01..AC-28. They are re-ranked after the
        C2/C4/C5 adjudications, which postdate the ranked directions and actionable conjectures.
Exact sources or dependencies: proposals/independent_campaigns/C1..C5/FINAL.md (authoritative);
        audits/quasi_rh/DOSSIER.md; audits/claims_2026/CRIT23/DOSSIER.md and SIEGEL/DOSSIER.md;
        audits/findings.jsonl, verified_findings.md, unresolved_findings.md, audits/lean_replay/README.md;
        frontiers/ledger.jsonl and records_ledger.md (corrected values), research_programs.md, missing_lemmas.md,
        known_obstructions.md, unsolved_questions.md; connections/connections_register.md,
        strongest_connections.md, repository_bridge.md; proposals/ranked_research_directions.md,
        actionable_conjectures.md; history/*.md; quality/*.md; methodology.md.
What was actually run: reading of the files above, plus short python3 extractions of JSONL fields. Nothing was
        attempted, proved or computed for this list.
Smallest remaining gap: the ranking is unvalidated and has had no expert review. Several targets are stated in
        their Observatory-proposed form. Opportunities 1-5 bound the status of much of the rest, so the order
        should be revisited as soon as any of them is resolved.
```

## 0. How the list was built

**Ranking rule.**
1. **Verification gates first.** Until they are passed, no Observatory document should treat 11/12, 7/8, 2/3 or Siegel exclusion as a theorem (unsolved_questions §A, priority digest).
2. **Well-posed theorems next.** These have a concrete first step and leverage on an RH-relevant obstacle.
3. **Certified computations** with a clear acceptance rule.
4. **Conceptual targets** last.

Within each tier the order follows expected value (significance × tractability, by judgement).

**Difficulty scale.**
- *Low:* weeks; mostly engineering or write-up.
- *Medium:* months for a specialist.
- *High:* a major project; at least one component probably needs a new idea.
- *Very high:* success would be a major theorem.

**FINAL.md precedence.** ranked_research_directions.md and actionable_conjectures.md predate the C2/C4/C5 adjudications. Where they conflict, this list follows FINAL.md:
- ‘Nyquist locality’ is REFUTED as a universal law (C4), not merely unestablished.
- BST Conjecture 1.1 is false by THEOREM C2-ADJ-2.
- The moment lemma for C2-14 is proved (C2-ADJ-3).
- ‘Over Q no finite window suffices’ is false as stated (C5-ADJ-LOG).

**Changes relative to D-01..D-36.**
- Added as stand-alone items: the 7/8 audit (A4) and the replication of numerical RH (A17).
- Restated in their adjudicated form: the C4 targets (16, 17).
- Reformulated by the C2 adjudication: the C2 follow-up (22).
- Next in line, not included: D-13 (order 3), D-20 (Conjecture G), D-35 (Riemann–Roch on the square) and D-36 (zero density at the Guth–Maynard bottleneck). They have lower tractability, or are partly covered by items 14 and 24.

## 1. Ranking at a glance

| Rank | Opportunity | Kind | Difficulty | Main anchor |
|---|---|---|---|---|
| 1 | Kernel replay of the formal 2026 statements | verification (formal) | Low–Medium | quasi_rh DOSSIER §1.3; A1, A2, A6, A9 |
| 2 | Human verification of the imports of Prop. 3.1 (11/12) | verification (analytic) | Medium | quasi_rh DOSSIER §5(3); A3 |
| 3 | One Siegel-exclusion core to version-of-record standard | verification | Low–Medium | SIEGEL DOSSIER §8 |
| 4 | Close the residual gaps of the 2/3 audit | verification (computational) | Low–Medium | CRIT23 DOSSIER §8; A5–A8 |
| 5 | A Level-2 audit of the 7/8 argument | verification | High | quasi_rh DOSSIER §1.1; A4 |
| 6 | A falsification handle for Prop. 3.1 | theorem + computation | Medium | quasi_rh DOSSIER §2.5; AC-01 |
| 7 | Certified Weil positivity on a window containing primes | computation, then theorem | Medium / High / Very high | LED-POS-7; C5 EFR |
| 8 | An explicit Nicolas/Robin implication theorem | theorem | Medium | C1 FINAL §8.3 |
| 9 | An RH-free 19/27 through the off-line pair defect | theorem | Medium (High for ML-CGG) | CON-0006 |
| 10 | Distinct zeros of one GL(2) L-function via rank–trace | theorem | Medium–High | CON-0035 |
| 11 | GL(2) family averages via Petersson | theorem | Medium | CON-0036 |
| 12 | The bandwidth-one ceiling as a theorem | theorem + certified optimisation | Medium | CRIT23 §7; OB-16 |
| 13 | Quasi-RH architecture floors as theorems | obstruction theorem | Medium | quasi_rh DOSSIER §4 |
| 14 | A quartic row mean square (an independent 7/8) | theorem | Very high | quasi_rh DOSSIER §4.3; CON-0038 |
| 15 | Independent replication and extension of numerical RH | computation | High | LED-VERIF-1; A17 |
| 16 | Weil-window blindness via a local resolvent bound | theorem | High | C4 FINAL §6.1 |
| 17 | Near-line detection with an O(log 1/δ) window constant | theorem | Medium–High | C4 FINAL §6.2 |
| 18 | A persistence lemma for the de Bruijn–Newman converse | theorem | Medium–High | CON-0008 |
| 19 | A Jensen–heat bridge with error control | theorem + certified computation | Medium / High | C1 FINAL §8.2 |
| 20 | Li positivity beyond T² | theorem | Medium–High | C1 FINAL §8.1 |
| 21 | A mechanized countermodel pre-review filter | tool | Low–Medium | C2 FINAL §4; C3 FINAL §6 |
| 22 | Euler products with Λ_F ≥ 0 in S♯₁ (between M10 and S) | classification | Medium | C2 FINAL §7.5 |
| 23 | The Beurling frontier at α ≥ 2/3, β < 1/2 | construction | Medium–High | CON-0032 |
| 24 | Semilocal positivity as a mechanism (CC Conj. 4.1, q = 3) | theorem | High | C5 FINAL ML-C1 |
| 25 | Infinitely many failures of the de Branges zero condition | theorem | Medium | C3 FINAL §3.2–3.3 |

**Gating.**
- Item 1 gates every consumer of QRH (CON-0018, CON-0019, LED-DBN-15) by making it conditional on a kernel-checked statement. It does not affect items 2, 6, 13 or 14, which concern arguments, not statements.
- Item 2 gates items 6, 13 and 14 and D-20.
- Item 3 gates the effective Siegel consequences (CON-0025).
- Item 4 gates items 9–12.
- Item 15 underpins items 8, 19 and 20 and every horizon built on T₀.
- Items 16 and 17 share the C4 machinery.
- Items 7 and 24 share the Weil-form machinery.

---

## 2. The opportunities

### 1. Kernel replay of the formal 2026 statements

- **Target (exact statement).** Use github.com/openai/math at commit 4eaee87548250b2682affda7d05d947c05554bae, with Lean v4.34.1, Mathlib d13f23b7 and the lakefile patches from lean/patches verified. Build the solution modules of four comparator challenges:
  - QuasiRiemannHypothesis: for all s with 7/8 < s.re, riemannZeta s ≠ 0;
  - DirichletSevenEighths: for all q ≠ 0, χ : DirichletCharacter ℂ q and s with 7/8 < s.re and ¬(χ = 1 ∧ s = 1), LFunction χ s ≠ 0;
  - HeckeSevenEighths;
  - SiegelZeros: there is c > 0 such that every real zero β ∈ (0,1) of every primitive real nonprincipal L(s,χ) with q ≥ 3 satisfies c ≤ (1 − β) log q.

  Confirm with Lean FRO comparator (via lean4export) and an independent kernel (nanoda) that each challenge theorem holds with #print axioms ⊆ {propext, Quot.sound, Classical.choice}. *Fidelity sub-target:* prove in Lean that for Re s > 1 the challenge file's custom LFunction χ s equals (1/6) Σ_{z ∈ O∖{0}} χ(z) N(z)^{−s}, with O = Z[ω]. *Companion replays:* anthropics/zeta-23-lean v1.0 (AF Theorems A and B) and Kimura's B4.Chi8.zero_gap_all.
- **Why it matters.** This is the fastest route to certainty for the ζ and Dirichlet 7/8 statements, and hence for 11/12 a fortiori, independently of how readable either paper is. It would make every consumer of QRH conditional on a kernel-checked statement.
- **Already known.**
  - Static checks only: an import closure of 2,924 modules (≈486,000 lines) plus PrimeNumberTheoremAnd and RellichKondrachov.
  - A text scan found no sorry, axiom, native_decide or extern.
  - SiegelZeros passed 31/31 static checks, and a third party reports a nanoda kernel replay.
  - The formalization covers the 7/8 paper, not paper2.
  - Commelin cautions that some OpenAI Lean statements prove weaker results than the papers claim [S].

  Sources: quasi_rh DOSSIER §1.3; SIEGEL adjudication_U4; LED-LFUN-6.
- **First concrete step.** Obtain explicit authorization to build the third-party code. Then pin the toolchain, hash the manifest and patches, build only the three solution modules and SiegelZeros.Main, run comparator and #print axioms, and archive logs and hashes under audits/lean_replay/.
- **Expected difficulty.** Low mathematically and moderate in engineering (a large build). The Hecke fidelity proof is Medium.
- **Risks and known barriers.**
  - Building was blocked by the session's safety policy and needs separate authorization.
  - Statement fidelity remains a human-review question.
  - A pass certifies statements, not arguments: it neither checks paper2 or the mechanism of Prop. 3.1, nor touches items 2, 6, 13 or 14.
  - Knausgård's run-axioms show that Lean developments can carry unchecked computations.
- **Start from.** audits/lean_replay/README.md; audits/quasi_rh/DOSSIER.md §1.3, §5(2); audits/claims_2026/SIEGEL/adjudication_U4.md; audits/claims_2026/CRIT23/DOSSIER.md §1 and finding F5; frontiers/unsolved_questions.md A1, A2, A6, A9; proposals/ranked_research_directions.md D-01.

### 2. Human verification of the imports of Prop. 3.1 (the 11/12 proof)

- **Target (exact statement).** Prop. 3.1 of paper2 (l.679–689) states, for the sextic family over K = Q(√−3) and H = D^{1+ϑ}: Σ_{0<N(u)≤H} |A_u(D)|² ≪ D^{1+ε}H, where A_u(D) = Σ_{(n,S)=1} μ(n)ν(n)(u/n)₆ W(Nn/D). Verify every imported input against its primary source:
  - (i) Patterson's coefficient formula, cusp table and the automorphy of the cubic theta function on Γ₂ with multiplier (c/a)₃, as transcribed in Dunn–Radziwiłł §5.1 and App. A, against Patterson 1977, Thm 8.1;
  - (ii) the hypotheses of Goldmakher–Louvel Def. 1 / Thm 1.1 for the family x ↦ (x/k)₂ κ_λ(x)^{e_k};
  - (iii) the multiplier case analysis at l.3175–3196, and Lemma 6.3 in the form Lemma 6.6 uses: the k₀-dependence must be exactly χ_{k₀}³, with weight N(k₀)² and a unimodular scalar;
  - (iv) the constants of Lemma B.2.

  Then write a short human proof with minimal imports.
- **Why it matters.** 11/12 is the human-edited version and the one the Observatory audited, and experts focus on it. All of its risk sits in Prop. 3.1, which is of density-hypothesis strength for the family. A gap here would void D-20 and reshape items 6, 13 and 14.
- **Already known.**
  - FND-0009: no error in the inspected portions, and about 100 identities checked in Z[ω].
  - The sign of the Kubota multiplier is settled numerically: θ(γw) = (c/a)₃θ(w) to 2·10⁻¹³, while the conjugate is off by |1 − ω|.
  - 515,936 local-identity cases checked.
  - Radziwiłł reportedly sketches the argument in half a page, and private write-ups of 7–13 pages circulate [S].
- **First concrete step.** Obtain Patterson 1977 and compare DR (5.6)–(5.8) and App. A with Patterson's Thm 8.1 line by line, recording every change of normalisation. Check that only unconditional material is imported: DR's own bias theorem is GRH-conditional.
- **Expected difficulty.** Medium. It needs expertise in metaplectic forms, but its scope is finite.
- **Risks and known barriers.** Transcription errors in imported theory decades old are a classic failure point (C3 tag F14). The numerics cover (i) and (iii) only at small sizes, and a human proof may still lean on the same imports.
- **Start from.** audits/quasi_rh/DOSSIER.md §1.2, §2.2, §5(3); audits/quasi_rh/ARCHITECTURE.md item 18; audit_S6.md, audit_APPA.md, audit_APPB.md; experiments/code/quasi_rh/; PAPER-0960; unsolved A3; D-02.

### 3. One Siegel-exclusion core to version-of-record standard

- **Target (exact statement).** Give a complete, referee-ready proof, with every constant, of one arithmetic core. Guo's route: Prop. 3.1, S₋(x,χ) ≤ (11/20) log x + (29/60) log q + 6 for every primitive quadratic χ mod q and every x ≥ 2 (S₋ is the inert-prime logarithmic mass, in Guo's definition), via Lemmas 3.2–3.3; then the deduction (1 − β) log q > 1/100 (1/64 with App. A) for every real zero β of every primitive real L(s,χ), q ≥ 3. Alternatives:
  - OAI/Banks: Lemma 3 (interpolation on a projected box) + Lemma 7 (Δ ∈ p^{E_p} Z[a,b]);
  - Kerr: Lemma 5 + Masser's Thm 1 with μ ≥ 4/3.
- **Why it matters.** It removes the archive's reliance on AI audits for the most consequential 2026 claim that is not about half-planes. It also gates the effective consequences: exponent-2 class groups and idoneal numbers (CON-0025), effective Siegel–Walfisz, and h(D) ≥ 0.00244√|D|/log|D|.
- **Already known.**
  - FND-0010: four proofs with structurally independent cores, no error and no gap found.
  - The audit scripts gave 130 PASS / 0 FAIL.
  - Exact toy replays show that the hypotheses p > H, Frob_p ∈ {σ, στ} and Q-independence are each necessary.
  - The constants are enclosed in ball arithmetic.
  - A communal write-up has been announced (Green; Tao's blog), but no version of record exists.
- **First concrete step.** Write Guo's Lemmas 3.2–3.3 in fully expanded form with every inequality and constant, have an independent reader re-derive them, and re-run the constant checks in experiments/code/claims_2026/siegel_dossier/dossier_checks.py.
- **Expected difficulty.** Low–Medium.
- **Risks and known barriers.** No mathematical risk is known. The method's ceiling (κ ≥ 1/2, and c ≤ 3 − 2√2 even ideally; OB-20) means the result cannot be pushed to zero-free strips or to complex zeros. Banks's all-q constant depends on the unreplayed Lu–Zaman–Zhao production run.
- **Start from.** audits/claims_2026/SIEGEL/DOSSIER.md §3–§8; audit_part1.md, audit_part2.md; adjudication_U2.md, adjudication_U3.md, adjudication_U4.md; experiments/code/claims_2026/siegel_*; CON-0025; LED-LFUN-6; D-03, D-06.

### 4. Close the residual gaps of the 2/3 audit

- **Target (exact statement).**
  - (a) An independent, directed-rounding Arb branch-and-bound replay of Knausgård's three local inequalities (Props 3.3, 5.3, 6.3), written from their statements. Given the rest of the chain, it would certify liminf N₀ˢ/N ≥ 1669159/2478195 = 0.67353820 and liminf N_d/N ≥ 1645064/1960733 = 0.83900460.
  - (b) An independent second review of the repair of AF Prop. 4.2: tr G̃ = N(I) + O(X^{1/2}L), from (2.8) with one-sided sums.
  - (c) A line-by-line write-up of P2-N1: BGSTB24 Lemma 4 and the Goldston–Montgomery evaluation of R(x,T) on [0, 1 − 2ε₀]. It must account for BGST's correction of a lower-order term (arXiv:2501.14545v3).
- **Why it matters.** (a) is the only gap between 0.6735382/0.8390046 and the audited 0.6725007/0.8362504, and (b)–(c) close the audit's residue. Items 9–12 reuse this certificate algebra.
- **Already known.** The CRIT23 audit re-derived every load-bearing step except these. Sampling KN's boxes found a minimum slack of 1.3·10⁻⁵ and no violation, and the P1-F1 repair was adjudicated once.
- **First concrete step.** Implement the Prop. 3.3 search in python-flint with exact rational box endpoints and outward rounding. Reproduce KN's box count for that search (6.05·10⁷) before attempting the two larger ones (5.35·10⁸ and 5.73·10⁸).
- **Expected difficulty.** Low–Medium (computational, with substantial CPU time).
- **Risks and known barriers.** The compute cost is substantial. KN's searches enter the Lean development as axioms, so an independent replay is the only check. The ceiling of ≈0.6818 limits what further refinements can give.
- **Start from.** audits/claims_2026/CRIT23/DOSSIER.md §3, §4, §8; audit_part1.md, audit_part2.md, adjudication_P1-F1.md; experiments/code/claims_2026/crit23_*; LED-CRIT-2, LED-CRIT-3; unsolved A5–A8; D-09.

### 5. A Level-2 audit of the 7/8 argument

- **Target (exact statement).** A section-by-section Level-2 audit of the 199-page 7/8 manuscript (PAPER-0528), at least to the depth of the 11/12 audit. Part II comes first:
  - Prop. ‘continuation from a common signal’ (tex78 l.399–432);
  - Prop. ‘Row counts from the witnesses’ (l.15185);
  - the inverse and plain moment inductions, and prime compensation;
  - the critical simultaneous-large-value class (δ_c, x = 1/2), which limits every refinement.
- **Why it matters.** A Lean replay, if it succeeds, certifies the statement but not the argument. Every refinement below 7/8 (best claimed 0.8740585, LED-ZFR-3) imports this argument's analytic inputs, so those inputs need a readable, checked form. Experts reportedly set this paper aside [S].
- **Already known.**
  - The paper was read for structure only.
  - Its Part I gives a different 11/12 argument, with Mellin exponent C_I(s) = s − 2/3.
  - The BGL sextic large sieve is used only in Part I.
  - de Faveri's sharper sieve would widen Part I's margins but would not move 7/8 by direct substitution [O].
- **First concrete step.** An architecture map, like audits/quasi_rh/ARCHITECTURE.md for paper2. It should list the load-bearing steps, the imported inputs and the parameter system (ℓ, b, κ) behind B(ℓ) = 11/12 − ℓ/4.
- **Expected difficulty.** High, because of the length and the moment and detector technology.
- **Risks and known barriers.** Community rewriting (oai-math-revised) may duplicate the effort. If the Lean replay passes first, the audit's value lies in the refinement literature and in exposition.
- **Start from.** audits/quasi_rh/DOSSIER.md §1.1, §1.5, §4.2–4.3; LED-ZFR-1, LED-ZFR-3; unsolved A4; history/recent_developments_2024_2026.md §4.1.

### 6. A falsification handle for Proposition 3.1

- **Target (exact statement).** Prove the density shadow of Prop. 3.1 as a theorem with an explicit detector. If Prop. 3.1 holds, then for every σ > 1/2:

  #{u₀ sixth-power-free : N(u₀) ~ U, L(s, νχ_·(u₀)) has a zero with β ≥ σ detectable at length D ≍ N(u₀)} ≪ U^{2−2σ+ε}.

  Here ‘detectable’ must be made precise: such a zero forces |A_{u₀a⁶}(D)| ≫ D^{σ−ε} on ≍ (H/N(u₀))^{1/6} rows u₀a⁶. Then compare with numerically computed low-lying zeros of sextic twists of small conductor.
- **Why it matters.** It makes the riskiest statement in the 11/12 proof testable, and a violation found numerically would falsify Prop. 3.1. It also quantifies how far Prop. 3.1 exceeds generic large-sieve density: de Faveri's Cor. 1.5 has exponent 1 − δ₆(σ), e.g. ≈0.73 at σ = 3/4 against 0.5 here.
- **Already known.** A HEURISTIC sketch (quasi_rh DOSSIER §2.5 [O]; AC-01). Prop. 3.1 is consistent with GRH: it is ‘GRH on average’ at rows near the diagonal (audit_S3 §4).
- **First concrete step.** State and prove the detector lemma: a zero at β forces large smoothed Möbius sums on the rows u₀a⁶, with explicit dependence on W, ν and the height of the zero, via the explicit formula for 1/L.
- **Expected difficulty.** Medium.
- **Risks and known barriers.** The detector may lose powers that make the shadow vacuous. Numerics at accessible conductors say nothing asymptotic. The shadow can only falsify Prop. 3.1, never confirm it.
- **Start from.** audits/quasi_rh/DOSSIER.md §2.5, §4.1, §5(5)(d); audits/quasi_rh/audit_S3.md §4, §7; proposals/actionable_conjectures.md AC-01; D-04.

### 7. Certified Weil positivity on a window that contains primes

- **Target (exact statement).**
  - (a) Certify with directed rounding (ball arithmetic) that λ*(0.8) := inf{W(g * g̃)/‖g‖² : g real and even in C_c^∞(−0.8, 0.8)} ≥ 8.9·10⁻¹⁸. This is Zhu's Cor. 6.3, certified on the geometric side and unrefereed.
  - (b) Give a computer-free proof of Pos(L) for some L > (log 2)/2, i.e. for a window whose autocorrelation sees at least the prime 2.
  - (c) Long term (EFR): an explicit L₀ and a proof, not assuming RH, that Pos(L₀) ⇒ RH. Such a proof must use prime-side (Euler product) structure.
- **Why it matters.** This is the only lever on the Weil-positivity route that yields certified progress beyond Yoshida's prime-free window. By C4-ADJ-INV, window positivity becomes informative about single defects beyond T₀ only for L > 6.49, so the certification ladder matters. By C5-ADJ-MODEL, zero-side positivity plus counting can never give RH, which pins down what (c) must use.
- **Already known.**
  - Pos((log 2)/2) is proved (Yoshida; Connes–Consani 2021).
  - Zhu's Pos(0.8) uses 50-digit precision with an error budget and a verified Cholesky factorisation; the connection verifier labels it not directed rounding, and the author retracted an earlier claim at L = 1.19.
  - Margins decay like exp(−c·e^{2L}) with c ≈ 12, so certification costs ≈5.4·e^{2L} digits, and Zhu's barrier for pointwise-envelope certificates has A_L ∼ 4e^L.
  - Over F_q the analogue holds with L₀ = (g − 1/2) log q, sharp in the formal class (C5-ADJ-W, C5-ADJ-SHARP).
- **First concrete step.** Re-implement the Weil-form matrix on a polynomial basis in Arb: the prime-power sum exact, the archimedean integral rigorous and the pole term in closed form, following experiments/code/C4-weil-window-locality/adjudicator/adj_witness.py. Then run a verified LDLᵀ factorisation with interval pivots at L = 0.8, together with a rigorous bound for the basis-truncation error.
- **Expected difficulty.** (a) Medium (computational); (b) High; (c) Very high.
- **Risks and known barriers.** A positive finite matrix is an upper section, not a lower certificate, unless the truncation error is bounded rigorously from below, and that is the hard part. The cost grows doubly exponentially in L, and (b) may need the semilocal mechanism of item 24.
- **Start from.** LED-POS-6, LED-POS-7; C4 FINAL §3.1, §3.3 (C4-ADJ-INV), §3.6; C5 FINAL §3.3–3.5 and §5 (EFR); OB-18; CON-0010 (correction 1); unsolved A11; D-16.

### 8. An explicit Nicolas/Robin implication theorem from partial RH

- **Target (exact statement).** Find an explicit X(T) ≍ T²/log²T and a T₁ such that for every T ≥ T₁ the following holds. If all zeros with 0 < γ ≤ T lie on the line, then Nicolas' inequality c(x) := log Π_{p≤x}(1 − 1/p)^{−1} − γ − log log θ(x) > 0 holds for 2 ≤ x ≤ X(T), and hence so do Robin's and Lagarias' inequalities over the corresponding range of n. Any X(T₀) ≥ 3.0·10¹³, at T₀ = 3,000,175,332,800, would make the Morrill–Platt range (log n ≈ 3.0·10¹³) a corollary of Platt–Trudgian.
- **Why it matters.** It turns C1's ‘Robin computations are uninformative beyond T₀’ from a heuristic into a theorem, closing C1's gap (b). It also gives the arithmetic-criteria row of the implication table the same status as the Li, Jensen and ψ/π rows.
- **Already known.**
  - C1-D3 (PROPOSITION-PROOF-SKETCH) gives the leading-order horizon ((2 − β)πT/(log(T/2π) + 1))², i.e. 4.36·10²³ at T₀.
  - The leading explicit formula is √x log x · c(x) = 2 + Σ_ρ x^{ρ−1/2}/(ρ(1−ρ)) + o(1).
  - Johnston's Thm 3.2 is the template for ψ/π.
  - CON-0002 and CON-0003 give pre-proof estimates (needs_correction).
- **First concrete step.** Write the explicit truncated formula for √x log x · c(x) with every O(1/log x) term explicit, following Nicolas, arXiv:1202.0729, Lemmas 2.1–2.5. Bound the zeros above T with Rosser's N(T) bounds, exactly as in the tail step of C1-L2.
- **Expected difficulty.** Medium.
- **Risks and known barriers.** The secondary terms and the substitution of θ(x) for x at moderate x need care. The zeros above T need unconditional zero-density or zero-free input, and small ranges of x need direct computation.
- **Start from.** C1 FINAL §2 (C1-D2, C1-D3), §3.4, §8.3 and the tail technique of §3.1; CON-0002, CON-0003 (corrected forms) in connections/connections_register.md; LED-ARITH-1, LED-ARITH-6; AC-16; D-15.

### 9. An RH-free 19/27 through the off-line pair defect

- **Target (exact statement).**
  - (a) A referee-ready proof that unconditionally N*(T) ≥ |S₁|²/(S₂ + D/2). Here S₁ and S₂ are the discrete moments of Conrey–Ghosh–Gonek and Bui–Heath-Brown, and D is the off-line pair defect.
  - (b) The conditional theorem: if every zero with T < γ ≤ 2T satisfies |β − 1/2| ≤ η(T)/(log T)^{3/2} with η → 0, then liminf N*(T)/N(T) ≥ 19/27.
  - (c) The largest explicit η for which the quantitative form D ≤ ηTL³ beats 0.6725007, 0.67800919 and 0.6818287; the thresholds are η < 0.01315, 0.01074 and 0.0091.
  - (d) Long term, ML-CGG: Σ_{β≠1/2} |BZ′(ρ) − BZ′(1−ρ̄)|² = o(T log³T).
- **Why it matters.** It gives the first exact accounting of where RH enters the 19/27 simple-zero machinery, and an RH-free route to simple zeros beyond the bandwidth-one ceiling.
- **Already known.** CON-0006: both parts re-derived by the verifier, with 0 violations in 20,000 random configurations. BHB use RH only for S₂. The pair-correlation route needs only a fixed thin box (b = 0.3185 gives 2/3).
- **First concrete step.** Write (a) in full. Then bound D by combining Conrey's ‘99.9% of zeros within 8/L of the line’ with a mean-value estimate over the remaining near-line zeros.
- **Expected difficulty.** Medium for (a)–(c); High for (d).
- **Risks and known barriers.** A fourth moment near the line is known only for mollifier length θ < 1/8 (BBLR). A configuration with D comparable to S₂ defeats the route (heuristically, the Davenport–Heilbronn situation).
- **Start from.** CON-0006 in connections/connections_register.md and strongest_connections.md Rank 3; LED-CRIT-11, LED-CRIT-13; PAPER-0049, PAPER-0070; AC-11; D-14.

### 10. Distinct zeros of an individual GL(2) L-function via the rank–trace certificate

- **Target (exact statement).** For a fixed self-dual GL(2) L-function (e.g. of a level-1 holomorphic Hecke eigenform), prove liminf N_d(T)/N(T) ≥ 1/R*_{1/2} = 0.4617 in two steps:
  - (i) prove an unconditional pair-sum asymptotic over all zeros at diagonal bandwidth 1/2, the GL(2) analogue of BGSTB24 Lemma 5;
  - (ii) run the AF/LZ inertia certificate with that input.
- **Why it matters.** It would be the first positive proportion of distinct zeros for an individual degree-2 L-function from the 2026 machinery, and a test of whether that machinery's inputs port beyond ζ.
- **Already known.** CON-0035 and CON-0011 (corrected): at bandwidth 1/2 the window certificate for simple critical zeros is negative (λ* = 0.5501939647), while the distinct-zero bound is positive (0.4617 for d = 2; 0.3214 for d = 3). The earlier target 0.4170 was refuted inside the proposal. The critical-line proportion for an individual GL(2) form is ≥ 6.96% (LED-CRIT-19).
- **First concrete step.** Prove (i) for |α| ≤ 1/2 by Montgomery–Vaughan mean values and the Rankin–Selberg explicit formula, keeping all zeros (no GRH), following AF §5 or BGSTB24.
- **Expected difficulty.** Medium–High.
- **Risks and known barriers.** The GL(2) pair-sum lemma may need inputs (shifted convolution sums) whose error terms fail at the endpoint. Individual results cannot exceed the bandwidth-1/2 ceiling.
- **Start from.** strongest_connections.md Rank 7; OB-16(f); audits/claims_2026/CRIT23/DOSSIER.md §7; AC-09; D-11.

### 11. GL(2) family averages through Petersson

- **Target (exact statement).** For the harmonic family of weight-k Hecke eigenforms of level N, in the level aspect, prove that on average at least 0.6725 of the zeros are simple and critical and at least 0.8363 are distinct. The Petersson formula lifts the diagonal bandwidth from 1/2 to 1. With Weil-only input the fallback bounds are 0.4191 and 0.7095.
- **Why it matters.** It is the natural GL(2) analogue of the Dirichlet-family results of Hua–Yang and AF: a well-posed theorem with a standard off-diagonal analysis.
- **Already known.** CON-0036 and CON-0012 (corrected plans). AF Remark 7.2 gives Dirichlet family averages 0.811 and 0.905, with details omitted and no Lean. The Hua–Yang template is unrefereed.
- **First concrete step.** Prove the Kloosterman diagonal lemma: the Petersson off-diagonal contributes o(N) to the family pair sum for Fourier support up to 1.
- **Expected difficulty.** Medium.
- **Risks and known barriers.** Family conclusions do not individualize (BRG-FAMILIES-O2, O4). The Bessel-decay diagonal in the original proposal was refuted, so the off-diagonal must be treated in full.
- **Start from.** strongest_connections.md Rank 8; CON-0012, CON-0036; AC-10; D-12.

### 12. The bandwidth-one ceiling as a theorem, and what breaks it

- **Target (exact statement).** Consider certificates of AF/LZ type that use only tr A = N, tr A² = (C(f) + o(1))N for windows f with f * f supported in [−1, 1], and the on-line/off-line inertia structure. Prove that every such certificate gives liminf N₀ˢ/N ≤ 0.6818287 (and N_d/N ≤ 0.84093 for regular windows). Identify the weakest additional input that exceeds this, e.g. third moments in the Rudnick–Sarnak range, or pair correlation for |α| slightly above 1.
- **Why it matters.** It separates method limits from the truth and prevents wasted effort. The AF and KN ceilings are author-stated and unaudited, and the Observatory has proved only the 2/3 sharpness for the flat window.
- **Already known.**
  - OB-16: the sharpness configuration; ceilings 0.6818287 and 0.68185; 0.67383 for any frame; the support barrier 2 − C(Δ) with C(Δ) = 1/Δ + Δ/3 for Δ ≤ 1.
  - The EnclOK interval enclosures are not kernel-checked.
  - Under HL*(4), a Chebyshev–Markov–Stieltjes bound gives 13/18.
- **First concrete step.** Audit AF §7.2: recast the extremal problem as a semi-infinite linear programme over admissible zero configurations and certify its value with Arb.
- **Expected difficulty.** Medium.
- **Risks and known barriers.** The ceiling depends on the precise certificate class (frames versus windows). Exceeding it may need pair-correlation information equivalent to Hardy–Littlewood prime-pair input (Goldston–Montgomery).
- **Start from.** audits/claims_2026/CRIT23/DOSSIER.md §7; OB-16; LED-CRIT-10; AC-12; D-07.

### 13. Quasi-RH architecture floors as theorems

- **Target (exact statement).**
  - (i) Define the class of arguments built from exact identities, positivity enlargements, Cauchy–Schwarz and the GL quadratic large sieve acting on sextic Möbius rows. Prove that no argument in this class yields the full-row mean square for H = D^h with h < 1, so that 11/12 is the floor of paper2's architecture.
  - (ii) Prove that every 7/8-type comparison system whose direct estimate has the form |J_η(Z)| ≪ Z^{l_x/2+b/12+ε} has boundary B(ℓ) = 11/12 − ℓ/4 > 2/3.
- **Why it matters.** It turns the dossier's [O] sketches into obstruction theorems that say which input must change: a sub-diagonal mean square (C1), a duality partner of lower order (C2), or a better count for the critical class (C3). It also guards against misreading Liu-type ‘optimality’.
- **Already known.** paper2 states the 11/12 floor, and quasi_rh DOSSIER §4.1–4.3 sketches both floors. CON-0009 shows that trivialising-row extractions need GRH for the member; CON-0014 and CON-0031 give architecture-specific bookkeeping.
- **First concrete step.** Formalize ‘positivity plus duality returns DH + D²’ as a lower bound for the dual diagonal of the Prop. 4.5 duality, and test it on explicit coefficient families where the bound is attained.
- **Expected difficulty.** Medium; defining a class of methods rigorously is the subtle part.
- **Risks and known barriers.** Barrier theorems about loosely defined classes can be vacuous or easily evaded, and proofs may cover only idealised versions.
- **Start from.** audits/quasi_rh/DOSSIER.md §4; OB-19; CON-0009, CON-0014, CON-0031; D-10.

### 14. A quartic row mean square: a 7/8 independent of OpenAI

- **Target (exact statement).** Over K = Q(i), for every finite-order Hecke character ν and smooth W, prove

  Σ_{0<N(u)≤D^{1+ϑ}} |Σ_{(n,S)=1} μ(n)ν(n)(u/n)₄ W(Nn/D)|² ≪ D^{2+ϑ+ε}.

  By the paper2 extraction this makes ζ_{Q(i)}, hence ζ and L(s, χ₋₄), zero-free in Re s > 7/8, independently of OpenAI's 7/8 inputs.
- **Why it matters.** An independent 7/8 would be the strongest possible cross-check of the 2026 half-planes. CON-0038 shows that Ji's density route cannot reach even 11/12 (its floor is ≥ 0.996732 for every density input), so a row mean square is necessary.
- **Already known.** Ji's route through the quartic Kubota series gives 599/600 (PAPER-0155). Explicit Fourier coefficients of n-fold metaplectic theta functions are known only for n = 2, 3 (standard; not re-verified). For n = 6, Gauss–Jacobi converts μ times a sextic Gauss sum into a cubic Gauss sum.
- **First concrete step.** Search for a quartic analogue of (eq:gj)/(eq:convert2): an identity that eliminates μ from the Poisson dual of μ·(u/n)₄, in terms of coefficients of an automorphic form whose Fourier coefficients are explicitly known.
- **Expected difficulty.** Very high.
- **Risks and known barriers.** No duality partner is known, and Patterson-type biases block cancellation without an angular twist (compare n = 3). A negative answer would itself sharpen OB-19(c).
- **Start from.** audits/quasi_rh/DOSSIER.md §4.1, §4.3 (C2), §5(5)(c); CON-0038; OB-19(c), (g); AC-03; D-19.

### 15. Independent replication and extension of numerical RH

- **Target (exact statement).** Verify independently and rigorously that all zeros with 0 < γ ≤ 3,000,175,332,800 lie on the line, then extend to H ≥ 10¹³. Requirements: interval or ball arithmetic, an algorithm different from PT21's, archived code and hashes, and an exact or double-double phase reduction near t ≈ 10¹³.
- **Why it matters.** PT21 Thm 1 is the single statement whose failure would invalidate the T₀ table and every horizon built on T₀: Li up to 9.0·10²⁴, Jensen, ψ/π up to 1.10·10²⁶, Λ ≤ 0.2 via 2.51·10¹², and δ_max. It has never been replicated, and Gourdon's 10¹³ zeros are unrefereed and not in interval arithmetic.
- **Already known.** PT21 is refereed. Platt 2017 isolated the zeros up to 3.06·10¹⁰ to ±2⁻¹⁰². Turing-method constants exist (Trudgian 2011, 2016), and a Turing-bound issue has been noted for Booker-type computations (LED-VERIF-19).
- **First concrete step.** Reproduce rigorously one window near 10¹² (e.g. 10⁶ consecutive Gram intervals) with a ball-arithmetic Riemann–Siegel / Odlyzko–Schönhage implementation and Turing's method with Trudgian's constants, cross-checked against certificates in the style of EXP-0001.
- **Expected difficulty.** High (computational): many core-hours and engineering for certified FFT-based evaluation.
- **Risks and known barriers.** Cost; subtle rounding in the phase reduction; reliance on Turing-method constants that have had misprints.
- **Start from.** LED-VERIF-1, LED-VERIF-3, LED-VERIF-7, LED-VERIF-19; frontiers/research_programs.md (VERIF section and its critique); C1 FINAL Status gap (d); unsolved A17; experiments/code/zeros_arb.py.

### 16. Weil-window blindness via a local resolvent bound

- **Target (exact statement).** Let V = span{e_z} near height T, G = (⟨P⁻¹e_w, e_z⟩) and G_flat the flat-model Gram matrix. For ζ and a window L, prove hypothesis R(T,L,η) with an explicit η: G ⪯ (1+η)G_flat. It should hold for all T ≥ (1+c)·2πe^{2L} outside a set of heights of logarithmic density zero. By C4-BL the window is then blind to single defects whenever (1+η)⁻¹G_flat⁻¹ + M ⪰ 0; equivalently, the local resolvent D(T,δ,L) = λ_max(E_w*(P + 2E_uE_u*)⁻¹E_w) stays below 1/(2mδ²). The natural route: P(g) = (1/2π)∫|h_g(r)|²Ψ_L(r)dr + pole terms, with Ψ_L(r) = Re ψ(1/4 + ir/2) − log π − Σ_{n<e^{2L}} 2Λ(n)n^{−1/2} cos(r log n); show that Ψ_L ≥ Ψ₀/(1+η) on |r − T| ≲ few/L for most T.
- **Why it matters.** This is the missing half of the window-locality question. At present blindness is proved only in an astronomically thin neighbourhood of the line (C4-ADJ-BLIND), and the Nyquist heuristic is refuted for fixed δ. It is also what host window families would need before any guidance of the form ‘L ≈ L_N suffices’.
- **Already known.**
  - C4-BL is CONDITIONAL on R and nearly tautological.
  - C4-ADJ-PAIR gives the exact criterion 2mδ²D > 1.
  - Certified witnesses show that no height-only law L* ≥ L_N − c holds across models.
  - Alignment of prime phases can make R fail (Zhu Lemma 3.2, A_L ∼ 4e^L).
  - The narrowed C4-H conjecture: L* − L_flat = O_δ(1) outside a set of logarithmic density zero.
- **First concrete step.** Prove an L² bound, averaged over T ∈ [X, 2X], for Σ_{n<e^{2L}} Λ(n)n^{−1/2} cos(r log n), uniformly in |r − T| ≤ K/L, and deduce R on average. In parallel, map Ψ_L(r)/log(r/2π) numerically for L ≤ 3 to locate the aligned heights.
- **Expected difficulty.** High.
- **Risks and known barriers.** Ψ_L can be ≪ log T at aligned heights, so the statement must exclude a sparse set. The result covers only the single-defect hypothesis H1, and translating L to the host's window parameters needs a separate check.
- **Start from.** C4 FINAL §2a (narrowed conjecture), §3.2–3.3, §3.6, §6.1; AC-20; D-33; experiments/code/C4-weil-window-locality/.

### 17. Near-line detection with an O(log 1/δ) window constant

- **Target (exact statement).** Assume H1 at height T: one off-line quadruple at 1/2 ± δ ± iT, and all other zeros on the line. Prove λ_min(L) < 0 for every L ≥ (1/2) log(T/2π) + C′(δ) with C′(δ) = O(log(1/δ)), ideally absolute. This would improve the certified C(δ) ≈ (2.1–3.1)/δ of C4-ADJ-C.
- **Why it matters.** Together with item 16 it would give a two-sided ‘Nyquist scale’ law for near-line defects. It is the brief's task 2(a) in its hoped-for form.
- **Already known.** C4-B and C4-ADJ-C (THEOREM under H1), with certified constants from 4.40 at δ = 0.49 to 313.17 at δ = 0.01. The injection numerics suggest L* − L_N ≤ 0.63 for T ≤ 7·10⁴, as upper bounds. AC-19 conjectures an absolute constant.
- **First concrete step.** In the C4-B margin, replace Trudgian's S(t) term by an S₁(t) bound with a smoother window, removing the (1 + 1.41L) loss. Then try a prolate (Landau–Widom) interpolating Paley–Wiener function that vanishes at the real zeros near T; this is full saturation, beyond Zhu's half-saturation product.
- **Expected difficulty.** Medium–High.
- **Risks and known barriers.** The sinh test function is useless when δL ≪ 1. The result stays conditional on H1, and removing H1 needs control of other off-line zeros (C4 FINAL §6.3).
- **Start from.** C4 FINAL §3.3, §6.2–6.3; experiments/code/C4-weil-window-locality/adjudicator/adj_Cdelta.py, adj_thmB_arb.py; AC-19; D-33.

### 18. A persistence lemma for the de Bruijn–Newman converse

- **Target (exact statement).** Prove that if ζ has a zero at 1/2 + δ + iγ with δ > 0, then Λ ≥ c·δ²/log²γ for an absolute c > 0; conjecturally the bound is c·min(δ², δ/log γ).
- **Why it matters.** It converts the model statement ‘a quadruple implies Λ ≥ t_c’ into a theorem, so that upper bounds on Λ would carry information about zeros (C1 FINAL §8.5). At present a proved Λ ≤ 0.2 adds nothing beyond RH(T₀).
- **Already known.** CON-0008 is sound_and_useful, but its proof sketch has two gaps; the far-field estimate is the main one. Polymath supplies the ODE dz_j/dt = 2Σ′ 1/(z_j − z_k) and the counting statement Thm 1.5(iv). The model collision times are ≈2δ² for an isolated pair and ≈4δ/log(T/2π) in a dense configuration (C1-E1, HEURISTIC).
- **First concrete step.** Bound the far-field contribution to the velocity of the off-line pair under the backward heat flow, using Polymath's count N_t(X+1) − N_t(X), uniformly for t ∈ [0, cδ²/log²γ].
- **Expected difficulty.** Medium–High.
- **Risks and known barriers.** Other zeros near γ, possibly off the line themselves, may collide first. The constants may be too weak to be useful at T₀.
- **Start from.** strongest_connections.md Rank 9; CON-0008; C1 FINAL §2 (C1-E1), §3.5, §8.5; AC-17; D-25; PAPER-0083.

### 19. A Jensen–heat bridge with error control

- **Target (exact statement).** Prove that, for the even Jensen polynomials J^{d,0}_ev of Ξ, there is an explicit error term E(T,d) = O(T³/d²) such that J^{d,0}_ev is hyperbolic near X = T² if and only if H_t is real-rooted near 2T at t = T²/(2d), up to E. In the isolated-pair model this gives d* ≈ T²/(4δ²). *Companion computation:* certify, by Arb root isolation on exact ball coefficients, the first non-hyperbolic degree of J^{d,0}(ξ̃) for injected quadruples (the non-rigorous value is d = 40 for (0.9, 5)).
- **Why it matters.** It would be the only quantitative link between the Jensen degree and the de Bruijn–Newman time. It could turn the heuristic reproduction of the Chasse/GORTTW horizon d ≤ T² from de Bruijn's Λ ≤ 1/2 into a derivation (C1 FINAL §1 row 5 replaced 'follows from' by 'is heuristically reproduced by'), and turn the C1/C2 cross-check (prediction 39.06 against d = 40) into a test.
- **Already known.** C1-J2 (HEURISTIC) is within 2.6% on Farmer's X_j, with certified thresholds for j = 10, 20, 40, 60. C1-ADJ-MONO makes a certified adjacent pair decisive for all d. C2-17 provides non-rigorous scans; see also AC-15.
- **First concrete step.** Run the C1 adjudicator's certified Jensen pipeline (adj_farmer_x10.py) on ξ̃ for the four C2 configurations, and compare with the quadrature for t_c(T,δ) in C1-E1.
- **Expected difficulty.** Medium (computation); High (theorem).
- **Risks and known barriers.** The bridge may fail for dense zero configurations, and certified Jensen thresholds for Ξ-type functions at large T are expensive.
- **Start from.** C1 FINAL §2 (C1-J2, C1-J3, C1-E1), §3.3, §8.2; C2 FINAL C2-17, §7.1; experiments/code/C1-detection-horizons/adjudicator/adj_farmer_x10.py; AC-15; D-29.

### 20. Li positivity beyond T²

- **Target (exact statement).** Find explicit c > 0 and T₁ such that for every T ≥ T₁, RH(T) implies λ_n > 0 for all n ≤ cT² log T.
- **Why it matters.** It would improve the only rigorous finite-height Li theorem (Oesterlé's n ≤ T²). At T₀, even c = 1 would push the rigorous horizon from 9.0·10²⁴ to about 2.6·10²⁶. It would also test the barrier picture of C1-L4.
- **Already known.** C1-L2 is a THEOREM. C1-L4 (PROPOSITION-PROOF-SKETCH): exponent 2 is optimal for arguments using RH(T) plus counting; the single-defect barrier is c(T) → 4 (4.53 at T₀); adversarial phases cap the positive side near c = 2.
- **First concrete step.** Refine Regime I of the C1-L2 proof (zeros with T < γ < n). Replace the worst-case bound 1 − cosh x cos y ≥ −(cosh x − 1) by an averaged bound over dyadic windows of zeros, using N(t) and the distribution of n·φ_γ mod 2π.
- **Expected difficulty.** Medium–High.
- **Risks and known barriers.** Adversarial phase configurations consistent with RH(T) and the N(t) bounds may cap any such argument, and the gain is only a constant factor.
- **Start from.** C1 FINAL §3.1, §2 (C1-L3, C1-L4), §8.1; experiments/code/C1-detection-horizons/adjudicator/adj_numbers.py; AC-14; D-34.

### 21. A mechanized countermodel pre-review filter

- **Target (exact statement).** Build and validate a tool with this contract:
  - Input: a proposed proof decomposed into steps, each annotated with the properties of ζ it uses (the predicates P1–P11 of C2 FINAL §4, plus the type and conductor of the functional equation).
  - Output for each step: every zoo member that satisfies all of those properties, together with executable sanity checks at its certified off-line zeros.
  - The zoo: Davenport–Heilbronn, the Epstein function of x² + 5y², ζ₁₉, M10, ξ̃, H_t with t < 0, the continuous Beurling system and the function-field fakes.
- **Why it matters.** It is a prerequisite for reviewing any claimed proof, human or AI (C3 checklist items 2–3). The meta-lemma C2-24 is a theorem, so a step whose properties are all satisfied by an RH-false member cannot be the RH-deciding step.
- **Already known.** Certified zeros and completeness ranges (C2-04, C2-09); the adjudicated property matrix; M10 shows that ‘uses the Euler product’ is not sufficient. The failure dossiers (Atiyah, Queme, Micheas, Oliva, Yakaboylu) serve as test cases.
- **First concrete step.** Encode the adjudicated property matrix as a machine-readable predicate table. Run it on the C3 dossiers and on FND-0001, and check that each known failure is flagged at its failing step.
- **Expected difficulty.** Low–Medium.
- **Risks and known barriers.** Extracting the properties used by an informal argument is the hard, human part. There is a structural blind spot: no zoo member can test a step that uses the full Selberg-class axioms (θ < 1/2, Λ_F ≥ 0, Euler product and functional equation together).
- **Start from.** C2 FINAL §3.5, §4; C3 FINAL §5–6; experiments/results/C2-countermodel-zoo/adjudicator/property_matrix_adjudicated.csv; history/abandoned_approaches.md §20; D-08.

### 22. Between M10 and the Selberg class: Euler products with Λ_F ≥ 0

- **Target (exact statement).** Classify the elements F of the degree-1 extended Selberg class S♯₁ that have an Euler product over the rational primes and satisfy Λ_F(n) ≥ 0 for all n. Either show that every such F satisfies RH iff the corresponding Dirichlet L-function does, or exhibit an RH-false example.
- **Why it matters.** M10 (C2-ADJ-1) violates exactly P4 (the Selberg local condition), P5 (Λ_F ≥ 0) and P8 (conductor 1). Either answer sharpens SP-1c and the hitting-set picture, telling a proof which property must carry the weight.
- **Already known.** The Kaczorowski–Perelli structure theorem for S♯₁. Hamburger: degree 1 with conductor 1 forces F = cζ. Placing M10-type local factors in the denominator creates poles, not zeros (C2 FINAL §7.5).
- **First concrete step.** Use the structure theorem to write F as a Dirichlet-polynomial factor times L(s + iθ, χ*). Impose Λ_F ≥ 0 on the logarithmic coefficients of the polynomial factor, and determine which local factors (roots of 1 + a₁p^{−s} + …) survive.
- **Expected difficulty.** Medium.
- **Risks and known barriers.** The classification may turn out routine, with a negative answer (no new countermodel); that would still be informative.
- **Start from.** C2 FINAL §3.1, §3.5, §4, §7.5; OB-4; LED-LFUN-13; PAPER-0033.

### 23. The Beurling frontier at α ≥ 2/3, β < 1/2

- **Target (exact statement).** Construct, or rule out, a discrete Beurling system with N(x) = ax + O(x^{β+ε}) for some β < 1/2 whose zeta function has a zero with real part α ≥ 2/3. Equivalently: decide whether an Euler product plus integer regularity with β < 1/2 forces any zero-free region beyond the de la Vallée Poussin shape.
- **Why it matters.** CON-0032 shows, non-constructively and given BDR Thm 1.3, that an Euler product plus integer regularity cannot give RH for β > 2/5. It also maps the open region β < 1/2, Θ ≥ 2/3, which contains 7/8 and 11/12. Resolving this region says exactly where integer regularity could matter for quasi-RH-type statements.
- **Already known.** BDR Thm 1.1 (β ≥ 1/2, any α); BDR Thm 1.3 (assuming RH: 1/2 < α < 2/3 and 2α/(α+2) ≤ β < 1/2); Hilberdink: max{α, β} ≥ 1/2; Beurling optimality of the classical region (LED-ZFR-16).
- **First concrete step.** Extend BDR's Sec. 5 perturbation P ∪ P^{1/β} ∖ P_S to α ≥ 2/3 (BDR Remark 5.3(2)). Run the planned numerical system at (α, β) = (0.6, 0.47) with primes up to 10⁸, testing the error term and the sign change of ζ_{α,β}(σ) at σ = 0.6.
- **Expected difficulty.** Medium–High.
- **Risks and known barriers.** BDR's journal status was not verified, and the case-split theorem T1 fails if BDR Thm 1.3 is wrong. A construction at α ≥ 2/3 may need new ideas.
- **Start from.** strongest_connections.md Rank 1; CON-0032; OB-7; C2 FINAL C2-26, SP-2; AC-27; D-26; PAPER-0581, PAPER-0601.

### 24. Semilocal positivity as a mechanism (Connes–Consani Conjecture 4.1 at q = 3)

- **Target (exact statement).** Take S = {∞, 2}. Within the semilocal operator framework, prove Weil's inequality for h = h₁ * h₂, where h₂(x) = h₁(x^{−1}), h₁ is supported in (3^{−1/2}, 3^{1/2}) and ∫h₁ x^{±1/2} d*x = 0. The required sub-step is to identify ker u(F)₂₂ with the geometric semilocal Sonin space.
- **Why it matters.** The numerical inequality Pos(0.549) is already covered by Zhu's unrefereed Pos(0.8), so the content is a structural mechanism for positivity with finitely many places. It is the most technical but well-posed gap toward positivity from structure (C5 assessment).
- **Already known.** Connes–Consani 2021: archimedean positivity on supports in (1/2, 2), with Sonin constant c = 4γ/log 2 ≈ 16.99, where γ ≈ 2.94355 is an operator constant (LED-OPS-5, corrected). The quasi-inner local factors Π_v ρ_v (PAPER-0125 Thm 4.8). Connes' semilocal trace formula (Thm 4).
- **First concrete step.** Compute ker u(F)₂₂ numerically for S = {∞, 2} in a prolate basis at λ² = 3, and compare it with the semilocal Sonin space. If the two agree to high precision, attempt the identification proof.
- **Expected difficulty.** High.
- **Risks and known barriers.** The identification may fail, and even if proved it covers one small window. Certifying a window inequality and proving it from the framework are different tasks (C5 FINAL §1 row 9).
- **Start from.** C5 FINAL §1 rows 8–9, §4 (rows CT and E), §5 (ML-C1), §6; LED-OPS-5; PAPER-0099, PAPER-0125; D-28.

### 25. Infinitely many failures of the de Branges zero condition

- **Target (exact statement).** Prove, unconditionally or under RH, that #{n ≤ N : S(γ_n) − δ(γ_n) ∈ (3/4, 7/4) mod 2} → ∞ as N → ∞, and ideally that it is ≫ N (a positive proportion). Here δ(t) = (arg ζ(3/2 + it) + c(t))/π is the bounded phase of C3-ADJ-S, and the conjectured limiting proportion is 1/2 (C3-ADJ-RATE).
- **Why it matters.** It upgrades Conrey–Li's single witness to an infinite, quantified failure of a once-proposed route to RH. It is also a clean problem about S(t) at zeros, in the style of Gram's law.
- **Already known.** C3-ADJ-S is a THEOREM. There are 15,567 failures among the first 10⁵ zeros, and the block rates rise from 8% to about 22% up to n ≈ 10¹⁰. A wrapped-Gaussian model with Selberg-type variance growth matches every block. Trudgian (2011) proved that Gram's law fails a positive proportion of the time.
- **First concrete step.** Adapt Trudgian's positive-proportion argument for Gram failures to the shifted window (3/4, 7/4) − δ_n. Use the strong correlation between S(γ_n) and arg ζ(3/2 + iγ_n) (0.67–0.89 in the data), rather than treating the two as independent.
- **Expected difficulty.** Medium.
- **Risks and known barriers.** The identity assumes the zeros up to γ_n are simple and on the line, so an unconditional statement must handle exceptions. Controlling δ_n jointly with S at zeros may need a two-dimensional central limit theorem of Selberg type.
- **Start from.** C3 FINAL §3.2–3.3, §9; FND-0013; LED-OPS-13; AC-18; D-32; experiments/code/C3-failure-anatomy/adjudicator/adj_debranges_S.py, adj_debranges_highblocks.py.

---

## 3. Directions examined and not recommended

These entries update ranked_research_directions §3 with the adjudicated statuses.

| Direction | Why not | Source |
|---|---|---|
| ‘Nyquist locality’ as guidance for window families | REFUTED as a universal law. Certified witnesses detect near-line defects below L_N, and blindness is proved only in a thin neighbourhood of the line | C4 FINAL C4-R, C4-ADJ-WIT, C4-ADJ-BLIND |
| ‘Over Q no finite window suffices’ as an obstruction | False as stated. The real content is C5-ADJ-MODEL (zero-side positivity plus counting cannot force RH) | C5 FINAL §3.5 |
| Large criterion computations as tests of RH beyond T₀ | They lie inside an implication horizon of RH(T₀) or below every single-defect scale | C1 FINAL §4–5 |
| Turán, fixed-degree Jensen or large-shift Jensen hyperbolicity as a proof route | They hold for functions with off-line zeros (C2-14, C2-ADJ-6) | C2 FINAL §3.3–3.4 |
| Heat-flow arguments ‘with room to spare’ | Rodgers–Tao: any valid argument must fail for every t < 0 | OB-11; C2-29 |
| ‘The proof uses the Euler product’ as a certificate of plausibility | M10 has an Euler product and a self-dual functional equation and violates RH | C2-ADJ-1 |
| Quasi-RH from proven mollified moments; generic sextic sieves; order-2 extraction | No half-plane results (lengths 4/7 and 17/33; trivial bound; circular) | OB-14; OB-19(f); CON-0014, CON-0031 |
| Siegel-type methods toward strips, Chowla positivity or complex zeros | κ ≥ 1/2 and the δ(log X)² coupling cap c near 0.17 at best | SIEGEL DOSSIER §7; OB-20 |
| Short-interval exponents, Artin or Linnik's L = 5 from the 2026 inputs | The 7/10 pivot; Hooley thresholds 0.656 and 0.796; the binding cases of Linnik have no exceptional zero | CON-0028, CON-0020, CON-0027 |
| Simple critical zeros of an individual GL(2) L-function from bandwidth-1/2 data | The certificate is negative for λ ≤ 0.5502 | CON-0011, CON-0035 |

