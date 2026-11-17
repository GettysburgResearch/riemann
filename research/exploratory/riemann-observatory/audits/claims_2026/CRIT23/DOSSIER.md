# CRIT23 dossier: "at least 2/3 of the zeta zeros are simple and on the critical line" (2026)

```text
Status: EXPLORATORY AUDIT DOSSIER (exploration layer). This is not an integrated or reviewed packet and makes
        no new mathematical claim. Nothing here says RH is proved, disproved, or closer to proved.
        Outcome as audited:
          - No verified error affects any stated result.
          - There is one verified local error in a proof step (AF Prop 4.2). It was adjudicated and repaired,
            and the statement is unaffected.
          - There are several presentation-level slips.
        None of the three 2026 sources has a journal reference on arXiv (API checked 2026-11-17).
        We did not build or replay any Lean development.
Scope: the asymptotic lower bounds
          liminf N0s(T)/N(T) >= 2/3 (flat window) and >= C0 = 0.6725007036... (Montgomery-Taylor window);
          liminf Nd(T)/N(T)  >= 5/6 and >= C1 = 0.8362503518...,
        as proved in AF and LZ, together with LZ's two further bounds and the KN refinement layer
        (0.6735382..., 0.8390045...). The scope is zeta(s) only. Out of scope:
          - AF Theorem B (Dirichlet L) and AF Remarks 7.1-7.2 (xi', family averages);
          - the AF/KN "ceiling" computations, quoted here as author statements only;
          - every unrefereed follow-up report.
Exact sources or dependencies:
          AF      = Alpoge-Furman, arXiv:2608.13637v2 (2026-08-19; latest version)
          LZ      = Lamzouri, arXiv:2609.02882v2 (2026-09-08; latest version)
          KN      = Knausgard, arXiv:2610.08965v1 (2026-10-06; latest version)
          Imported: BGSTB24 = arXiv:2306.04799v1 = Acta Arith. 214 (2024) 357-376.
          Baselines: PRZZ20 = arXiv:1802.10521v3 = Res. Math. Sci. 7 (2020); Wu = arXiv:1206.3737v2.
        Full PDF hashes are in Section 9. The audit records in this directory are ARCHITECTURE.md,
        audit_part1.md, audit_part2.md and adjudication_P1-F1.md.
What was actually run:
        Earlier audits:
          - line-by-line reading of AF and LZ in full, KN (Sections 2, 3, 5, 6, App. A) and BGSTB24 (Sections 2-3);
          - hand re-derivation of every load-bearing step S1-S10, except the error terms of BGSTB24 Thm 1 / [GM87];
          - 11 part-1/part-2 audit scripts and 2 adjudication scripts (floating point, sympy exact, Lipschitz grids).
        This dossier:
          - arXiv API status check;
          - a reading of the published Lean statements for fidelity;
          - one new script, crit23_dossier/dossier_checks.py. It computes Arb ball enclosures of all AF/LZ
            constants and the exact KN rationals, builds an explicit sharpness configuration, gives a
            conditional support-Delta illustration, and re-checks the P1-F1 witnesses in ball arithmetic.
        No author code, Lean code, ancillary program or other repository content was run.
Smallest remaining gap:
        For 2/3, 0.6725, 5/6 and 0.83625 we found no gap that affects a stated result. Not replayed:
          (i)   the BGSTB24 Thm 1 / [GM87] error terms on the LZ route (refereed; P2-N1 argues they are not
                load-bearing at the endpoint, but this was not written out line by line);
          (ii)  every Lean build;
          (iii) an independent second review of the P1-F1 repair.
        The KN constants also rest on its three computer-assisted local inequalities (branch-and-bound;
        Lean `native_decide` axioms). We probed these only by sampling.
```

## 0. Bottom line

* **The claim, precisely.** It is an asymptotic lim inf statement, liminf_{T→∞} N₀ˢ(T)/N(T) ≥ 2/3, where N counts all nontrivial zeros with multiplicity. With the Montgomery–Taylor (MT) window the constant is ≥ C₀ = 3/2 − cot(1/√2)/√2 = 0.67250070367941…. The companion bound for distinct zeros is ≥ 5/6, and ≥ C₁ = (C₀ + 1)/2 = 0.83625035183970….
* **Proofs.** Two proofs exist and they share no unverified lemma.
  * AF: the argument was "discovered and written by Claude"; the human authors verified it.
  * LZ: an independent, human-written proof composed after reading AF.
* **Audit result.** All ten load-bearing steps were re-derived. The headline constants were recomputed, and now also enclosed in ball arithmetic. One local error in a proof step was found, with explicit witnesses (P1-F1, AF Prop 4.2), and repaired; the Proposition and every theorem are unaffected. Every other finding is presentation-level.
* **Refinements.** KN's improvements (0.6735382…, 0.8390045…) additionally depend on three unreplayed computer searches. All the algebra and data around those searches were reproduced.
* **What the mechanism is.** It is Montgomery's 1973 pair-correlation second-moment argument with RH replaced by an inertia / rank–trace (equivalently Bessel) inequality. The 2/3 is Montgomery's RH-conditional number; it is not an increment over the mollifier method.
* **Limits.** The method's ceiling with Fourier support [−1, 1] is about 0.682 for zeros on the line (author-stated, not audited). It is insensitive to o(N) off-line zeros, so even a 100% version would not imply RH.

## 1. Exact claims and their status

| Source | Exact statement (zeta only) | Refereed? | Provenance | Lean claimed | Lean replayed by us |
|---|---|---|---|---|---|
| **AF** arXiv:2608.13637v2, 21 pp. | **Thm A.** N₀ˢ(T,2T) ≥ (2/3 − o(1))N(T,2T) and N_d(T,2T) ≥ (5/6 − o(1))N(T,2T). With ψ_MT: 2 − c_MT⁻¹ = 0.67250… and (3 − c_MT⁻¹)/2 = 0.83625…, where c_MT⁻¹ = ½ + (1/√2)cot(1/√2). The same holds on (0, T] with rate O(log log T/log T) (Rem. 6.1). A fortiori the bounds hold for N₀*, N₀ and N_s. | No journal reference on arXiv (2026-11-17). | Title page: "discovered and written by Claude, an AI developed by Anthropic. The listed authors verified the proof and take responsibility for its content." | Yes: anthropics/zeta-23-lean tag v1.0, Lean v4.33.0-rc2, Mathlib 51e6992efd06. Main theorems "carry no hypotheses"; `#print axioms` reportedly gives only propext, Classical.choice and Quot.sound. | **No** |
| **LZ** arXiv:2609.02882v2, 17 pp. | **Thm 1.1** (on (0, T]). liminf N₀ˢ/N ≥ C₀ and liminf N_d/N ≥ C₁. Also liminf N_{s∪0}/N ≥ C₂ = (1 + 2√2 + 2C₀)/(3 + 2√2) = 0.88762… and liminf (N_s + N₀)/(2N) ≥ C₁. The flat-window 2/3 and 5/6 are not stated, but follow from the same proof with f = 1_{[−½,½]}. | No journal reference. LZ thanks six named analysts for reading a draft; this is not refereeing. | Human proof. "Conceptually simpler"; written after AF. | Yes, AxiomProver (github.com/AxiomMath/ZetaZerosV2). Prop 2.1 is unconditional. Thm 1.1 is certified **assuming** BGSTB24 Lemma 5 and N(T) ∼ (T/2π) log T as hypotheses (LZ App. A). | **No** |
| **KN** arXiv:2610.08965v1, 43 pp. | **Thm 1.1:** liminf N_d/N ≥ 1645064/1960733 = 0.83900459675…. **Cor 1.2:** liminf N_s/N ≥ 0.67800919…. **Thm 1.3:** liminf N₀ˢ/N ≥ 1669159/2478195 = 0.67353820…. **Thms 1.4–1.5:** 0.83676910… and 0.88931500…. | No journal reference. | "An experiment in AI-assisted mathematical research". Builds on the LZ operator, BGSTB24 Lemma 5 and the AF Lean library. | Yes (github.com/kristianmk/839 and arXiv ancillary files). It is hypothesis-free **plus three extra axioms**, each saying that one search program returned true; the kernel does not check those runs. The AF library is used with a 14-file patch. | **No** |
| BGSTB24 (imported by LZ, KN) | Lemma 5, the unconditional Montgomery pair sum over all zeros, for Fourier support [−1, 1]. Thm 1 also gives F(α) ≥ 0 for all α. | **Yes**, Acta Arith. 214 (2024). | Human. | — | — |

**Lean statement fidelity** (reading only; nothing was run).
* The AF statements (App. A) define:
  * `Ncount`, `Ndist`, `N0star` and `N0simple` from Mathlib's `riemannZeta`, with 0 < Re ρ < 1 and T₁ < Im ρ ≤ T₂;
  * multiplicity as `analyticOrderAt`;
  * the theorems in the form ∀ε > 0 ∃T₀ ∀T ≥ T₀, (2/3 − ε)·Ncount ≤ N0simple.
* This matches §1.1 and the lim inf claim.
* `finsum` and `ncard` return 0 on infinite sets. This does not make the statements vacuous, because the zero sets in a bounded box are finite and Ncount(T, 2T) → ∞ (Riemann–von Mangoldt).
* The KN statements use the same definitions (KN §8).
* Classification: no_issue_found_in_inspected_portion (statement level only).

## 2. Provenance, independence and disclosure

* **AF.** Per AF's title page, acknowledgments and Appendix B:
  * the argument was found by Claude over two interactive sessions and checked by adversarial review using further model instances;
  * Alpöge and Furman verified it and take responsibility for it;
  * the problem was posed by J. Sumner, and the Lean formalisation was orchestrated by E. Easley.
* **LZ.** An independent human proof of the same bounds. It is a separate *verification* of the AF mechanism, written after reading AF, not an independent discovery. It shares with AF only classical refereed inputs:
  * the explicit formula, Riemann–von Mangoldt, Stirling, Mertens;
  * Montgomery–Vaughan-type mean values;
  * the MT constant.

  The two proofs differ as follows:
  * **Algebraic core.** AF: von Neumann trace inequality plus Sylvester inertia. LZ: real flag U ⊂ V ⊂ W plus Bessel.
  * **Analytic core.** AF: its own §5, via the Weil formula, Montgomery–Vaughan and Mertens. LZ: BGSTB24 Lemma 5 plus LZ Lemma 3.2.
  * These were proved independently (ARCHITECTURE §6; audit_part2 §1.5).
* **KN.** Not independent of either proof. It imports BGSTB24 Lemma 5 and LZ's weight device, and its formalisation extends the AF Lean library.
* **Auditor disclosure.** This dossier and the audits it summarises were produced by AI agents (Claude, Anthropic), and AF's argument is reported to have been discovered by Claude. Our audit is therefore not institutionally independent of the discoverer. The independent human checks on record are LZ's proof and the refereed BGSTB24 input. That is a reason to weight the audit's "no error found" by its explicit witnesses and re-derivations, not by its authorship.

## 3. Audit coverage and outcomes

| # | Load-bearing step | AF | LZ | Our status (where) |
|---|---|---|---|---|
| S1 | Encoding; conjugation symmetry ρ ↔ 1 − ρ̄; real point ⇔ β = ½ | §2.2–2.3 | Thm 1.1 proof | verified (part 1 §2.1; numerics 1e−15) |
| S2 | Second moment as a nonnegative quadratic object over all zeros; AF Lemma 2.1 (Poisson–Gabor) at complex z | (2.2), (2.11), Lem 2.1 | (2.9), (2.12) | verified; explicit formula vs zeta zeros to 1e−13; Lemma 2.1 to 3e−14 (part 1 §2.2) |
| S3 | Inertia: on-line ⇒ PSD rank one; off-line pair ⇒ signature (1,1), trace 2m | Prop 4.1, Lem 3.1 | (2.11), (2.13) | verified on actual AF matrices (part 1 §2.3) |
| S4 | **Core inequality** (rank–trace / flag + Bessel) | Lem 3.2, §6 | Prop 2.1 | verified by hand; 20k random + 400 adversarial starts; equality cases exact (part 1 §2.4) |
| S5 | Trace = N; localisation; tail | Props 4.2–4.3, Cor 4.5 | trivial | statements verified; **P1-F1** proof-step error repaired (adjudication) |
| S6 | **Unconditional second moment**, support [−1, 1], over all zeros | §5 (own proof) | BGSTB24 Lem 5 | AF §5 re-derived (P2-F1, F2, F3 presentation-level); BGSTB24 statement verbatim; its Thm 1 error terms read, not re-derived |
| S7 | Removal of the weight w(ρ − ρ′) | — | Lem 3.2 | verified exactly (sympy; complex z) |
| S8 | Window constants C(f) | Lem 5.6 | Lem 3.2, Rem 3.4 | recomputed; Arb enclosures in this dossier |
| S9 | Counting bookkeeping; dyadic → cumulative | §6, Rem 6.1 | Thm 1.1 proof | verified (21 sympy identities; operator-level tests) |
| S10 | KN layer: threshold lemma, separated-set majorant, transfer, certificates, data | — | — | algebra verified; all data reproduced; **branch-and-bound not replayed** (sampling: min slack 1.3e−5, no violation) |

**Not done.**
* No Lean build or kernel check (AF, LZ/AxiomProver, KN). KN's `native_decide` searches (6.05·10⁷, 5.35·10⁸ and 5.73·10⁸ boxes) were not run.
* BGSTB24 Thm 1 / Lemma 4 error analysis and the [GM87] mean value were not re-derived; [GM87] was not inspected.
* Out of scope and not audited: AF Theorem B, Remarks 7.1–7.3 and the §7.2 ceiling computation, and KN §7.
* None of the unrefereed 2026 follow-ups listed in KN §1 were inspected: Wang, Chandru, D'Souza, Santibañez-Leal, Yang–Yang and others.
* Ki–Lee 2012 (Funct. Approx. 47, Thm 5) could not be obtained. It is not on arXiv, and the Project Euclid page did not serve the text.

## 4. Adjudicated findings (consolidated)

The finding IDs are those of the underlying records. "Effect" means effect on a stated theorem.

| ID | Class | Location | Finding (short) | Witness | Effect |
|---|---|---|---|---|---|
| **P1-F1** | **verified_error** (one proof step; severity minor; disposition repaired_minor) | AF Prop 4.2 proof (src l.327, PDF p.6) | (a) For zeros with Re γ_ρ ∈ I′∖I, the inequality \|Re γ_ρ − α_k\| ≥ D_ρ (k ∉ [0, d)) and the resulting tail bound are false, and so is the summed claim "≪ X^{1/2}". (b) α_d ∈ (2T − h, 2T) whenever LT/2π ∉ ℤ. | Zero #10085, γ = 9949.990912…, T = 10⁴: \|γ − α₋₅₉\| = 0.27369 < D_ρ = 50.00909. Re-checked here in ball arithmetic, check (E). AF's chain gives tail ≤ 0.0321 against an actual 45.59. α_d < 2T for T = 10³, 2·10³, 10⁴, 3·10⁴ (ball arithmetic, (E)). | **None.** Repair: tr G̃ = N(I) + O(X^{1/2}L) = N(I′) + O(√T log T), stronger than stated. Permitted public wording: "a local error in the proof of AF Prop 4.2, with a short repair; the Proposition and all results are unaffected." |
| P1-F2 | typo_or_presentation (witness) | AF §2.2 l.217, §7.2 l.589 | "d = N(T,2T) + O(L)" is false; d − N(T,2T) = −(2 log 2 − 1)T/2π + O(L). | T = 10⁴: d − N = −616 | None (only d ∼ N is used) |
| P1-F3 | typo_or_presentation | AF Lem 2.1 proof | Sign slips in the Poisson phase. | algebra; identity checked to 2.9e−14 | None |
| P1-F4 | typo_or_presentation | AF Prop 4.1 proof | The factor 2/(aL²) is dropped in the pull-back. | algebra | None |
| F3 | typo_or_presentation (witness) | AF (2.1) vs (2.2)/(2.11) | (2.1) is stated for even F and fails for non-even F. The form (2.2), which is the one used, is right. | zeta zeros at X = 50: the literal (2.1) is off by 1.4i–3.9i | None |
| F7 | typo_or_presentation | AF Prop 4.2 proof | The displayed bound gives √X L³ for the D_ρ < 1 zeros, not √X L². The true contribution is ≪ √X L. | numerics (part 1 (E)) | None |
| P2-F1 | typo_or_presentation (witness) | AF Prop 5.2, Thm 5.7 | The written proof gives the error O(N log L/L), not O(N log L/L²). | E₂-bound/(L⁴N) tracks log L/L | None (still o(N)) |
| P2-F2 | typo_or_presentation | AF Prop 5.5 | The bound for M[P_X, Π_X] does not follow from the sup bounds as claimed. A weaker O(LX) bound does follow and suffices. | s6_prime (e) | None |
| P2-F3 | typo_or_presentation | AF (5.2), Prop 5.4 | The lower bound 1_{[…]} ≤ φ² holds only for ψ₀; there is a leftover "second form"; ‖φ″‖₁ vs ‖(φ²)″‖₁. | algebra | None |
| F1 | typo_or_presentation (witness) | AF abstract, §1.1 | The previous record "5/12 for N₀ˢ/N" should be 0.407511. PRZZ20's 0.417293 (> 5/12) is for N₀. LZ and KN quote this correctly. | PRZZ20 §1; LZ p.2 | None (baseline only) |
| F2 | unresolved_ambiguity | previous distinct-zero record | AF cite 0.6603 (Wu, 66.036%); LZ and KN cite Ki–Lee 2012 Thm 5 (> 70%) and Farmer (63.9%). Ki–Lee was not inspected. Either way the new 0.836 exceeds both. | — | None |
| F4 / P2-N1 | no_issue_found (input-set note) | AF p.2; BGSTB24 Thm 1 | AF's route uses no zero-free region. BGSTB24 Thm 1 formally uses Korobov–Vinogradov, but only to reach α = 1. LZ/KN test functions have supp Q ⊂ [−1 + 2ε₀, 1 − 2ε₀], where the trivial bound suffices (our reading; not written out line by line). | s7 (e) | None |
| F5 | missing_hypothesis (formal scope) | Lean claims | LZ's Lean assumes BGSTB24 Lemma 5 and Riemann–von Mangoldt. KN adds three run-axioms. AF claim hypothesis-free (three standard axioms). AF cite anthropics/zeta-23-lean v1.0, while KN cites anthropics/formal-math commit fbdc36b; their relation was not checked. **None replayed.** | — | Formal status only |
| F6 | unresolved_ambiguity (out of scope) | AF Thm B, Rem 7.1–7.2 | Thm B is a one-paragraph sketch; Rem 7.2 "details omitted", not in Lean. | — | Not part of CRIT23 |
| P2-N2 | no_issue_found (finite-T calibration) | normalisations | On the first 10⁵ zeros, AF's zero side equals its prime side to 3e−5. LZ-normalised sums converge slowly from below: S/N = 1.185 vs C_δ = 1.366 at T = 7.5·10⁴. | s6_zero (A), (B) | Guards against any finite-height reading |
| P2-N3 | no_issue_found_in_inspected_portion | KN §3, §5, §6, App. A data | All budgets, x₁, x₂, Ω, β, Λ, f ≤ g, C(f) and the six rationals were reproduced. Local inequalities were sampled (2·10⁶ frames per window) with no violation. | s8–s10 | — |
| D-1 (new) | no_issue_found_in_inspected_portion | AF App. A, KN §8 | Lean statement fidelity (Section 1). | reading | — |
| D-2 (new) | unresolved_ambiguity (outside CRIT23) | KN §1, ref. [50] | KN reports an unverified Yang–Yang preprint claiming 0.7962 (simple, on line) and 0.8981 (distinct) from trace moments up to order six; its authors grade it a candidate. Exceeding the ≈ 0.682 two-moment ceiling would require higher moments to contribute unconditionally, which AF §7.2(e) state (informally) they do not. We did not inspect the report and draw no conclusion about it. | — | None on CRIT23 |

No finding is classified verified_error at the level of a statement, suspected_gap, or (for the mathematics) missing_hypothesis.

## 5. Consequences if correct (precise)

Assuming AF/LZ (and, where marked, KN) are correct:

1. **Simple zeros on the line.**
   * liminf_{T→∞} N₀ˢ(T)/N(T) ≥ C₀ ∈ [0.67250070367941164573 ± 3·10⁻³¹] (Arb, check (A)). Also ≥ 2/3 with the flat window.
   * AF give the same in every dyadic window (T, 2T].
   * KN would give ≥ 0.6735382001….
2. **Zeros on the line, and simple zeros.** Since N₀ˢ ≤ N₀* ≤ N₀ and N₀ˢ ≤ N_s, both liminf N₀/N and liminf N_s/N are ≥ C₀.
   * For N₀ the previous record was 0.417293 (PRZZ20). The increase (0.2552) is about three times the whole mollifier-era gain from Levinson's 1/3 (0.0840).
   * For N_s, KN Cor 1.2 would give 0.6780092.
3. **Distinct zeros.** liminf N_d/N ≥ C₁ = 0.83625035183970… (KN would give 0.8390045967…). The previous unconditional value was 0.6603 or > 70%, depending on the source (F2).
4. **LZ's rigidity bounds.**
   * liminf N_{s∪0}/N ≥ C₂ = 0.88762000817…. So the proportion of zeros that are both off the line and multiple is at most 1 − C₂ < 0.1124.
   * liminf (N_s + N₀)/(2N) ≥ C₁, hence max(N_s, N₀) ≥ (C₁ + o(1))N.
   * KN would give 0.8893150 and 0.8367691.
5. **Relation to conditional results.**
   * The unconditional bounds now equal the classical RH-conditional pair-correlation constants: Montgomery's 2/3, Montgomery–Taylor's 0.6725, and Conrey–Ghosh–Gonek's 5/6.
   * They remove the box hypotheses used before for 2/3 and 5/6: |β − ½| < b/(2 log T) (BGSTB25, b = 0.3185 for 2/3) and |β − ½| = o(1/log T) (Goldston–Suriajaya).
   * They remain **below** the best RH-conditional values: 19/27 = 0.7037 simple (Bui–Heath-Brown, RH); 0.6792 simple and 0.8477 distinct (Chirre–Gonçalves–de Laat, RH).
   * They do not reach the box-hypothesis value (2 + C₀)/3 = 0.8908 for "simple or on the line". LZ get 0.8876 and KN 0.8893.

## 6. What is not implied

* **Not RH, and no step toward it in any formal sense.**
  * The certificate is insensitive to o(N) off-line zeros, so infinitely many off-line zeros are compatible with every bound here.
  * AF §1.4 state that the inputs also hold for Davenport–Heilbronn and Epstein zeta functions, for which the analogue of RH is false. We did not check this.
* **Not a statement at any finite height.**
  * The theorems are lim inf bounds with inexplicit o(1) terms; AF's rate O(log log T/log T) has unspecified constants.
  * At T = 7.5·10⁴ the normalised second moment is still far below its limit (P2-N2). No "≥ 2/3 up to height T₀" statement follows.
  * The Lean theorems are ∃T₀ statements with no value of T₀ extracted.
* **Not "almost all"**, and not the simple-zero conjecture. Nothing is said about the remaining ≤ 1/3 (≤ 0.3275 with MT). Those zeros are *not shown to be off the line or multiple*; they are simply not reached by the certificate (AF §1.4).
* **Not a zero-density estimate or a zero-free region.** Classical density theorems (Bohr–Landau, Selberg) already give N(σ, T) = o(N(T)) for each fixed σ > ½. CRIT23 adds nothing to N(σ, T) for fixed σ > ½, nor to the location of the possible off-line zeros.
* **Nothing about individual zeros**, gaps, Lehmer pairs, or the vertical distribution beyond the second moment.
* **KN Cor 1.2 and LZ's N_{s∪0} bound say nothing about the critical line by themselves.** Off-line zeros can be simple. LZ's average bound does not say which of N_s and N₀ is larger.
* **Not a claim about other L-functions.** AF Thm B (fixed primitive χ) is a sketch, and the family averages (AF Rem 7.2) omit details. Neither was audited.
* **Not formally replayed by us.** The Lean claims are the authors' and were reported as such. LZ's formal certificate takes the analytic input as a hypothesis, and KN's adds three run-axioms.
* **Not refereed.** AF, LZ and KN carry no journal reference as of 2026-11-17. Only the imported BGSTB24 and the baselines are refereed.

## 7. The method's limits (what prevents going further)

### 7.1 The certificate is sharp for the information it uses (check (C))

The bound uses only three facts:
* tr A = N;
* tr A² = Σ K(z − s)² = (C(f) + o(1))N for one window f with f∗f supported in [−1, 1];
* the inertia structure.

These are consistent with configurations in which one third of the zeros are off the line. Check (C) builds one explicitly (flat window, K = sinc, rescaled points on ℤ). Each block of six integer sites holds four simple on-line points, one heavy site and one empty site. The heavy site is either an on-line double, or an off-line pair n ± iε, i.e. two simple zeros off the line.

| heavy site | N | true N₀ˢ | off-line share | ΣK²/N | certificate 2N − ΣK² |
|---|---|---|---|---|---|
| on-line double | 150 | 100 | 0 | 1.333333 (exactly 4/3) | 100.0000 (equality) |
| off-line pair, ε = 0.01 | 150 | 100 | **1/3** | 1.333625 | 99.9562 |
| off-line pair, ε = 0.001 | 150 | 100 | **1/3** | 1.333336 | 99.9996 |

* With only the flat-window trace and second moment, the bound 2/3 cannot be improved: "nothing in the method distinguishes 'two thirds' and 'all'" (AF §7.2(a), (b)).
* The distinct-zero certificate is not sharp on the pair configuration (124.998 vs N_d = 150), as AF §7.2(b) say.
* The same configuration has MT-window second moment 1.338504 > C_MT = 1.327499. It is therefore excluded by the MT information, and that is exactly why the MT window gives more than 2/3.

### 7.2 Windows and local refinements saturate near 0.682 (author-stated; not audited)

These are the authors' figures; we did not audit them.

| Certificate class | Ceiling for N₀ˢ/N | Ceiling for N_d/N | Source and status |
|---|---|---|---|
| All "bandwidth-one" certificates (first two trace moments for Fourier support [−1, 1], plus the on/off partition) | ≤ 0.6818287 | — | AF §7.2. Lean `Zeta23.PairCeiling.ceiling_law256`, given interval enclosures (EnclOK) that are **not kernel-checked**; one averaging step is outside Lean. |
| Windows with V(f) ≤ 10 B(f) | 0.68185 | 0.84093 | KN Cor 7.9 (ball arithmetic, outside Lean) |
| Any frame length (pair energy of simple points / first window) | 0.67383 | 0.83998 | KN Prop 7.3, §7 |
| Eight-point (N₀ˢ) and seven-point (N_d) frames | 0.67357 | 0.83916 | KN §7 |

KN's 0.673538 is 0.00003 below its eight-point ceiling and 0.0003 below its any-frame ceiling. Its 0.839005 is 0.0019 below the any-window ceiling 0.84093 (KN: "less than 0.002 is left"). Every two-moment refinement of this type stays below ≈ 0.682 (on the line) and ≈ 0.841 (distinct). These ceilings bound methods, not zeros.

### 7.3 The support barrier is the real obstruction to "2/3 → 100%" (check (D), conditional)

**Where the support comes from.** Support [−1, 1] is X ≤ T in the prime sum. For X ≫ T, the off-diagonal prime-pair terms are no longer dominated by the diagonal, and evaluating them needs Hardy–Littlewood-type prime-pair asymptotics; under RH that is equivalent to Montgomery's pair-correlation conjecture beyond α = 1 (AF §7.2(a); Goldston–Montgomery 1987).

**What larger support would give.** Check (D) computes the flat-window certificate under the **hypothetical** input that the all-zeros form factor equals min(|α|, 1) on [−Δ, Δ]:

| Δ | C(Δ) | 2 − C (simple, on line) | (3 − C)/2 (distinct) | Input status |
|---|---|---|---|---|
| 1/2 | 13/6 | −0.1667 | 0.4167 | unconditional (useless) |
| **1** | **4/3** | **0.6667** | **0.8333** | **unconditional (BGSTB24; AF §5)** |
| 3/2 | 31/27 | 0.8519 | 0.9259 | hypothetical |
| 2 | 13/12 | 0.9167 | 0.9583 | hypothetical |
| 10 | 301/300 | 0.9967 | 0.9983 | hypothetical |

In closed form:
* C(Δ) = 1/Δ + Δ/3 for Δ ≤ 1. This is AF Rem 6.1's H(λ) = 2 − 1/λ − λ/3.
* C(Δ) = 1 + 1/(3Δ²) for Δ ≥ 1.

**Consistency with the literature.** As Δ → ∞ the certificate tends to 100%. This agrees with:
* Goldston–Lee–Schettler–Suriajaya: the full pair-correlation conjecture, without RH, gives 100% simple and on the line;
* AF §7.3: "if Montgomery's form factor were known on support (−λ₀, λ₀) for all λ₀, the method would certify 100%".

**The positivity barrier (our reading).**
* BGSTB24 Thm 1 proves F(α) ≥ 0 for **all** α unconditionally.
* That sign goes the wrong way for these certificates. They need an *upper* bound on ΣK², and the relevant Fourier weight r = f∗f (up to LZ's lower-order Q″ term) is nonnegative because f = η² ≥ 0. Knowing F ≥ 0 off [−1, 1] therefore only bounds ΣK² from below.
* Chirre–Gonçalves–de Laat's RH-conditional gain to 0.6792 uses positivity inside a termwise SDP. AF state that it is "a regime the present method does not enter".
* Exploiting it unconditionally would need non-square kernels, and those lose the operator identity ΣK² = tr A² on which the inertia/Bessel step rests.

### 7.4 Higher moments

**Unconditional.** AF §7.2(e) state, informally, that the prime-side evaluation of tr G̃ᵏ is available only in the Rudnick–Sarnak range Xᵏ ≤ T^{2−ε}. At X ≍ T, higher moments therefore add nothing unconditionally.

**Conditional.** Under a hypothesis HL*(4) on the first four trace moments, the Chebyshev–Markov–Stieltjes bound gives 13/18 ≈ 0.7222: Λ₂(0) = 5/36 for the moments 1, 4/3, 2, 13/4, recomputed exactly in ARCHITECTURE §7. Under HL*(k₀) for all k₀ it gives 1.

The unverified report D-2 claims otherwise. We have not inspected it.

### 7.5 Even 100% would not be RH

* The extremal behaviour is insensitive to o(N) off-line zeros: rank P ≤ d = N(1 + o(1)) is the only ceiling.
* So even an unconditional "100%" from this mechanism would leave RH open. AF §7.2(f): "RH itself is out of reach of the mechanism."

### 7.6 Note on the "Siegel method" clause of the task template

That clause belongs to the separate claim audited in `../SIEGEL/`: exclusion of Landau–Siegel zeros, (1 − β) log q ≥ c. Siegel's theorem and Siegel zeros play no role in AF, LZ or KN; "Siegel" does not occur in any of the three texts. Nothing in CRIT23 bears on Siegel zeros, and nothing in the SIEGEL claim bears on CRIT23.

## 8. Next precise research steps

1. **Second review of the P1-F1 repair** (adjudication_P1-F1.md §5).
   * Have an independent reviewer re-derive tr G̃ = N(I) + O(X^{1/2}L) from (2.8) with the one-sided sums.
   * Then send AF a consolidated erratum: P1-F1, P1-F2, P2-F1, P2-F2, P2-F3, F1, F3, F7.
2. **Lean replay** in an isolated, separately authorised environment. Not done here, by policy.
   * Build anthropics/zeta-23-lean at tag v1.0 (Lean v4.33.0-rc2, Mathlib 51e6992efd06).
   * Run `#print axioms` on `Zeta23.thmB0_mult`, `thmC0_mult`, `two_thirds_on_critical_line` and the MT declarations.
   * Run `leanprover/comparator` against `comparator/Challenge/Multiplicity.lean`.
   * Settle F5: how zeta-23-lean v1.0 relates to anthropics/formal-math fbdc36b.
3. **Independent replay of KN's three local inequalities** (Props 3.3, 5.3, 6.3).
   * Use our own branch-and-bound in directed-rounding ball arithmetic (Arb), written from the statements, not from KN's code.
   * This is the single gap separating 0.6735382 / 0.8390046 from the audited 0.6725007 / 0.8362504.
4. **Close the LZ-route analytic residue.** Either write out P2-N1 line by line (restricted support avoids the KV / [GM87] endpoint), or re-derive BGSTB24 Lemma 4 and the [GM87] R(x, T) evaluation on [0, 1 − 2ε₀].
5. **Resolve F2.** Obtain Ki–Lee, Funct. Approx. 47 (2012) 79–87, Thm 5, and record the correct pre-2026 distinct-zero baseline.
6. **Effective version (open, exploratory).**
   * Make every o(N) explicit: Riemann–von Mangoldt with explicit constants, Montgomery–Vaughan, Mertens, and the AF taper terms.
   * Extract an explicit T₀ for, say, N₀ˢ ≥ 0.6 N on (T, 2T].
   * Only such a version could be compared with zero-verification data. The finite-T calibration (P2-N2) suggests T₀ will be very large.
7. **Mathematical directions suggested by the limits** (open problems, not claims).
   * (a) Any unconditional *upper* information on the all-zeros form factor F(α) for some α > 1, even on average over [1, 1 + δ], feeds directly into the certificate (7.3).
   * (b) Decide whether an inertia-compatible certificate can use the unconditional sign F ≥ 0 off [−1, 1] (7.3, last item).
   * (c) Look for unconditional third-moment (triple-correlation) information for complex zeros in a range usable at X ≍ T, against AF §7.2(e).
   * (d) Audit the unverified higher-moment report D-2, since it is in tension with AF §7.2(e).
8. **Out-of-scope audits, if wanted:** AF Thm B, Rem 7.1 (ξ′: 0.85838), Rem 7.2, the AF §7.2 ceiling (Lean + EnclOK), and KN §7.

## 9. Reproduction and hashes

**Scripts.** All are under `research/exploratory/riemann-observatory/experiments/code/claims_2026/`. Run each with `python3 -I <script>` from its directory.

| Directory | Scripts | Recorded in |
|---|---|---|
| `crit23_part1/` | af_testfn, constants_part1, s1_s4_blocks_linalg, s2_gabor_explicit_formula, s5_trace_tail | audit_part1.md §5 |
| `crit23_part2/` | s6_prime_side_af, s6_zero_side_data, s7_weight_removal, s8_window_constants, s9_counting, s10_kn_local | audit_part2.md §5 |
| `crit23_adjudication/` | adj_P1F1_trace, adj_P1F1_witness | adjudication_P1-F1.md §8 |
| `crit23_dossier/` | dossier_checks.py (this dossier; about 5 min on 4 vCPU) | below |

The SHA-256 hashes of all part-1, part-2 and adjudication scripts and outputs were recomputed on 2026-11-17 and match the values recorded in those files.

**Dossier script.** Environment: Python 3.13, python-flint 0.9.0 (Arb), mpmath 1.3.0, sympy 1.14.0.

```text
4b30c6f2d3b964703bb317ed2e7c594a4ae7ec81deb67debea73e33be5309620  crit23_dossier/dossier_checks.py
45c9e6cfb0eb918f79af2144eb2e0d785ae551e8f05737d04007817d91419640  crit23_dossier/dossier_checks.out
```

* (A), (B) and (E) are ball or exact-rational arithmetic.
* (C) and (D) use sympy exact algebra plus mpmath floating point at 40 digits. They illustrate the method's limits and prove nothing about zeta zeros. (D) is explicitly conditional for Δ > 1.
* Zero ordinates: `experiments/results/zeros/zeta_zeros_1_100000_arb.tsv.gz`, sha256 4d364a6ba8043e878409fe7d2ce89d2e9c6a29ba48dc1446b54c468579715603 (EXP-0001).

**Source PDFs** (SHA-256 of the copies read; not redistributed):

```text
6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444  AF  arXiv:2608.13637v2 (21 pp.)
305df7fcbbf96e61ccca2cbae13dcb2b7f9251b054d02dd0c78551982621046b  LZ  arXiv:2609.02882v2 (17 pp.)
aedf2891fbe0e55cde9ad85d4ecd8714a75dca1a258abd290d6b4aaf8a08200f  KN  arXiv:2610.08965v1 (43 pp.)
133071c4d85c875fe9b1a7d4001f22d7174270ab8f1fa8e6cee6178d20276ee9  BGSTB24 arXiv:2306.04799v1 (13 pp.)
147187ac00831b06e674a99705b0798181eb03024b1b09fc2b740610c80b90aa  PRZZ20 arXiv:1802.10521v3 (60 pp.)
d25092c0240fc8fb0dadd6952ae838c9051ef3d8703cec2b87b6f2a70047e6a5  Wu arXiv:1206.3737v2 (9 pp.)
```

The e-print tarball hashes are in audit_part2.md §5.

**arXiv status** (export.arxiv.org API, 2026-11-17):
* the latest versions are AF v2, LZ v2 and KN v1;
* AF, LZ and KN have no journal_ref or DOI;
* BGSTB24 is recorded as Acta Arith. 214 (2024) 357–376, doi:10.4064/aa230612-20-3.
