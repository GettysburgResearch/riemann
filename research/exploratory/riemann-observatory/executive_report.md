# The Riemann Observatory: executive report

```text
Status: SYNTHESIS (exploration layer). Executive summary of the archive as delivered on 2026-11-17. It is not
        a review approval, an integrated packet or a referee report. RH is open. Every 2026 claim named here is
        unrefereed, and every statement carries its status and an archive reference.
Scope: the whole Observatory archive: corpus, paper records, theorem database, frontier ledger, audits,
        campaigns C1-C5, connections, repository bridge, history and quality records.
Exact sources or dependencies:
        - quality/coverage_report.md, evidence_audit.md, limitations.md; logs/RUN_LOG.md;
        - audits/findings.jsonl, verified_findings.md, unresolved_findings.md, quasi_rh/DOSSIER.md,
          claims_2026/CRIT23/DOSSIER.md and SIEGEL/DOSSIER.md;
        - proposals/independent_campaigns/C1..C5/FINAL.md (authoritative over REPORT.md and
          SKEPTIC_REVIEW.md);
        - frontiers/records_ledger.md and ledger.jsonl (verifier-corrected values);
        - connections/connections_register.md, strongest_connections.md, repository_bridge.md;
        - frontiers/missing_lemmas.md, known_obstructions.md, unsolved_questions.md;
          proposals/ranked_research_directions.md.
What was actually run: reading of the files above, plus short python3 tabulations that re-counted the audit
        levels in corpus/bibliography.jsonl, the verifier verdicts in frontiers/ledger.jsonl, and the verdicts
        in connections/connections.jsonl and repository_bridge.jsonl. All agree with the quality files. No
        mathematics was redone and no computation was re-run for this report.
Smallest remaining gap: no human expert has reviewed any part of the archive, and no Lean development was
        built or replayed. The C2, C4 and C5 adjudications postdate several synthesis files; the superseded
        entries are listed in final_synthesis/open_problems_for_future_agents.md Sec. 0.3.
```

## 1. Bottom line

- **RH is open.** Nothing in this archive proves or disproves it, or adds evidence for or against it beyond the cited literature ([quality/limitations.md](quality/limitations.md)).
- **2026 moved the frontier near Re s = 1 and in density statements, not on the critical line.** Three unrefereed claims matter:
  - a zero-free half-plane Re s > 11/12 (and Re s > 7/8) for ζ and every Dirichlet L-function;
  - at least 2/3 of the zeros simple and on the line;
  - no Landau–Siegel zeros.

  Our AI-agent audits found no error invalidating the 11/12, 2/3 or Siegel-exclusion claims in the portions inspected; the 7/8 manuscript was not audited. One proof step in Alpöge–Furman needed, and received, a short repair (FND-0004).
- **Two campaign results change how computations should be read.**
  - No published large criterion computation (Li, Jensen, ψ/π, Robin, Mertens, Nyman–Beurling, de Bruijn–Newman) is informative beyond the verified height T₀ = 3,000,175,332,800 (C1 FINAL §4–§5).
  - The brief's "Nyquist locality" heuristic for Weil windows is refuted. Under a single-defect hypothesis, a window of half-width L ≈ (1/(2δ)) log log T already detects an off-line zero at height T. Blindness is proved only in an astronomically thin neighbourhood of the line (C4 FINAL §3.3).
- **Verification gates come first.** Lean replays, human review of the imported metaplectic inputs, and an audit of the 7/8 manuscript bound the status of everything built on the 2026 claims ([frontiers/unsolved_questions.md](frontiers/unsolved_questions.md) §A).

## 2. What was done

All counts are from [quality/coverage_report.md](quality/coverage_report.md) and [quality/evidence_audit.md](quality/evidence_audit.md).

| Stage | Count |
|---|---|
| zbMATH / arXiv records harvested | 24,876 (27 queries) / 5,737 (30 queries) |
| Deduplicated candidate pool | 20,166 |
| Expert seed works | 1,422 listed; 1,356 verified automatically at Level 0 |
| Candidates triaged, each with a recorded decision | 3,373 (include 1,453; borderline 696; reject 1,224) |
| Selected corpus | 1,000 works, PAPER-0001 … PAPER-1000 |
| Level-1 reading | 231 attempted; 108 full text, 46 partial; 77 without legitimate open full text |
| Index-content (L0+) / metadata-only (L0) records | 373 / 473 |
| Theorem database | 1,635 statements (732 lemmas) from the 154 works read; 265 intra-paper dependency edges |
| Frontier ledger | 232 records in 12 areas: 140 confirmed against full text, 36 from abstract or secondary sources, 52 corrected, 4 superseded, 0 rejected |
| Repository bridge | 215 items for 7 host programmes; of 166 prior-art and obstruction items, 79 confirmed, 74 confirmed with correction, 12 relation overstated, 1 ungraded |
| Cross-paper proposals | 39: 9 sound and useful, 10 sound but known, 19 needs correction, 1 vocabulary only, 0 false |
| Level-2 audits | targeted claims in 15 works as enumerated (8 flag targets; OpenAI 11/12; Alpöge–Furman; Lamzouri; the Landau–Siegel papers of OpenAI, Banks, Kerr, Guo); quality/evidence_audit.md §2 prints the count as 12 |
| Level-3 adjudications | 5 for the 2026 claims, 4 for the flag audits, 5 campaign adjudications |
| Findings register | FND-0001 … FND-0014: 12 classified, 2 unresolved |
| Rigorous zero data | 100,000 Arb-certified zeta zeros, maximum radius 1.7·10⁻²⁴ (EXP-0001) |

The corpus spans 1737–2026. Stratum S7 (2024–2026) has 101 works, 13 of them read at L1. The run used 19 workflows and jobs, with about 220 sub-agent invocations ([logs/RUN_LOG.md](logs/RUN_LOG.md)). Every producer and every verifier was an AI agent.

## 3. Most important findings

### 3.1 The 2026 claims after our audits

| Claim | Status | What the Observatory did | Reference |
|---|---|---|---|
| ζ and all Dirichlet L-functions (and finite-order Hecke L over ℚ(√−3)) have no zeros in Re s > 11/12 | unrefereed; AI-generated, human-edited | Level-2 audit of every line from l.206 to l.3988: 0 errors, 0 gaps, about 35 presentation items, about 100 identity checks in ℤ[ω]. The imported Patterson/Kubota inputs (as transcribed by Dunn–Radziwiłł) and Goldmakher–Louvel were checked against their statements, not re-proved | FND-0009; [audits/quasi_rh/DOSSIER.md](audits/quasi_rh/DOSSIER.md) §1.2 |
| The same with Re s > 7/8 | unrefereed; AI-generated, 199 pp. | read for structure only. The Lean challenge statements were read statically: faithful for ζ and Dirichlet; the custom L-function of the Hecke statement is unchecked. Nothing was built | DOSSIER §1.3; [audits/lean_replay/README.md](audits/lean_replay/README.md) |
| Refinements to about 0.8741 (best claimed B_tw = 0.8740585, Liu hexagon:2610.00655v3; also Xu–Sang, Chang–Wang, Newton) | unrefereed | statements and dependencies read: every one imports the 7/8 inputs | DOSSIER §1.5; LED-ZFR-3 |
| liminf N₀ˢ/N ≥ 2/3, and ≥ 0.6725007 with the Montgomery–Taylor window; distinct zeros ≥ 5/6 and ≥ 0.8362504 | unrefereed. Alpöge–Furman: argument discovered and written by Claude, verified by the authors. Lamzouri: independent human proof | the load-bearing steps were re-derived (except the BGSTB24 error terms). One local proof-step error in AF Prop. 4.2, with witnesses, was repaired; the theorems are unaffected | FND-0004; [CRIT23 DOSSIER](audits/claims_2026/CRIT23/DOSSIER.md); LED-CRIT-1, LED-CRIT-2 |
| Knausgård: 0.67353820 and 0.83900460 | unrefereed; Lean with three run-axioms | algebra reproduced; computer searches not replayed | LED-CRIT-3 |
| (1 − β) log q ≥ c for every real zero of every real primitive L(s, χ) | unrefereed (OpenAI; human re-proofs by Banks, Kerr, Guo) | nine load-bearing steps re-derived in each of four proofs: no error, no gap. Banks's all-q constant 3.0·10⁻³ rests on the refereed but unreplayed Lu–Zaman–Zhao computation | FND-0010; [SIEGEL DOSSIER](audits/claims_2026/SIEGEL/DOSSIER.md); LED-LFUN-6 |

**Method limits.** These are Observatory derivations, labelled [O] (sketch) in the dossiers.
- 11/12 is the floor of the paper's own architecture: β(n, h) = 1/2 + h(n − 1)/(2n) at n = 6, h = 1.
- The 7/8 comparison system has boundary B(ℓ) = 11/12 − ℓ/4, with a structural floor of 2/3.
- The critical-line method saturates near 0.682 with Fourier support [−1, 1] (author-stated) and is blind to o(N) off-line zeros, so even 100% would not be RH.
- The Siegel method caps c near 3 − 2√2 ≈ 0.17 in its present shape.

Sources: DOSSIER §4, CRIT23 §7, SIEGEL §7. None of the four results bears on Re s = 1/2.

### 3.2 Verified findings (scoped wording, as allowed by the register)

- **FND-0001** (Yakaboylu, J. Phys. A 2024). The Stage-II similarity-transformation claim fails: the weight defines an indefinite form, and the boundary condition admits spurious solutions (explicit witnesses). The paper does not claim RH.
- **FND-0002** (Farmer, Adv. Math. 2022). The Table 4.1 thresholds do not match the configuration described (j = 10: certified 120, printed 119; three Arb implementations). The conclusion is unaffected.
- **FND-0003** (Bellotti–Trudgian–Yang, 2026 preprint). One localized Table 1 entry is invalid for the stated polynomial; the corrected value preserves Theorem 1. The Observatory independently reproduced the constant 4.896.
- **FND-0004** (Alpöge–Furman). A proof-step error, repaired; the theorems are unaffected.
- **FND-0006, -0007, -0008**: correct but misinterpreted.
  - Connes 1999 Thm 5 is proved for positive characteristic only.
  - Andrade–Keating Thm 1 rests on their Conjecture 5.
  - Ng–Shen–Wong's apparent "k ≥ 12" was our own pdftotext artifact.
- **FND-0012**: Cheng–Graham Lemma 2, already corrected in print.
- **FND-0013**: the Conrey–Li necessary condition for de Branges' programme fails often, at 15,567 of the first 10⁵ zeros.
- **FND-0014**: the exact failing steps in already withdrawn or unaccepted RH proofs.
- **Unresolved, not characterized as errors**: FND-0005 and FND-0011 (public characterization not allowed).

C2 FINAL also adjudicates two refutations of external claims that are **not yet in the findings register**:
- the claim that every nontrivial Davenport–Heilbronn zero lies on the critical line (arXiv:2503.24275), which is contradicted by certified off-line zeros and by Davenport–Heilbronn 1936;
- Bétermin–Šamaj–Travěnec Conjecture 1.1, refuted by the theorem C2-ADJ-2.

C2 FINAL §7.8 asks for one more independent Level-2 check before either is cited outside the Observatory.

### 3.3 Campaigns (statuses as adjudicated in each FINAL.md)

**C1, detection horizons.**
- THEOREM C1-L2: if T ≥ 100 and RH(T) holds, then λ_n > 0 for 1 ≤ n ≤ T². The statement is Oesterlé's (2000, unpublished); the campaign's proof is complete and independent. So RH(T₀) gives n ≤ 9.0·10²⁴, and RH(317) already implies Johansson's rigorous λ₁, …, λ₁₀₀₀₀₀ > 0.
- THEOREM C1-N1: an off-line pair forces the Nyman–Beurling floor (4δ/T²)(1 + O(T⁻²)).
- IMPORTED horizons: Jensen hyperbolicity for d ≤ 9.0·10²⁴ (GORTTW); the Schoenfeld bounds for x ≤ 1.10·10²⁶ (Johnston); Λ ≤ 0.2 derived from RH up to 2.51·10¹² (Platt–Trudgian 2021, Cor. 2). The last refutes the investigator's sentence that de Bruijn–Newman has no finite implication.
- Single-defect detection scales are HEURISTIC.

**C2, countermodel zoo.**
- NUMERICAL-RIGOROUS: complete lists of off-line zeros for Davenport–Heilbronn (|t| ≤ 300: 5 zeros, the lowest at 85.70) and for the Epstein function of x² + 5y² (|t| ≤ 200: 35 zeros, the lowest at 15.67); a zero of ζ₁₉ with real part 1.0010955 near t = 600884.
- THEOREM C2-ADJ-1 (folklore status confirmed): F_c(s) = ζ(s)(1 + c·2⁻ˢ + 2·4⁻ˢ), c > 2√2, has an ordinary Dirichlet series, an Euler product and a self-dual degree-1 functional equation (conductor 4), and still has off-line zeros. The protocol's blind spot is therefore the full Selberg class, not "Euler product plus functional equation".
- THEOREM C2-14, given Csordas–Varga 1988 (read at L0+): all Turán inequalities hold for every H_t, t real, although H_t has non-real zeros for t < 0.

**C3, failure anatomy.**
- Eight complete proofs. Example: C3-ADJ-O2, Oliva's step (3) holds for every prime 5 ≤ p ≤ 1.39·10¹⁷ and fails for some prime below e^{727.95}.
- THEOREM C3-ADJ-S: the de Branges zero condition at the n-th zero is exactly S(γ_n) − δ_n ∉ (3/4, 7/4) mod 2.
- CONJECTURE C3-ADJ-RATE: the failure proportion tends to 1/2.
- A 20-item checklist for proposed proofs (HEURISTIC).

**C4, Weil-window locality.**
- REFUTED for every fixed δ: the heuristic that a window of half-width L can detect an off-line quadruple at height T only if T ≲ 2πe^{2L}.
- THEOREM C4-B, under the single-defect hypothesis H1: detection for L ≥ (1/(2δ))(log log T + log log log T + O_δ(1)). At T₀ this is below the Nyquist window L_N = (1/2) log(T/2π) for δ > δ* = 0.2354455 (Arb-certified at δ = 0.2355; the margin is negative at δ = 0.2354).
- THEOREM C4-ADJ-C: under H1, detection for all L ≥ L_N(T) + C(δ), with C(δ) ≈ (2.1–3.1)/δ.
- THEOREM C4-ADJ-BLIND: height-uniform blindness is proved only for very small δ (no lower bound on detection windows is proved beyond that radius). For example, in the additive model, δ ≤ 3.5·10⁻⁹ for windows L ≤ 0.8, using Zhu's unrefereed bound (described by Zhu as certified; not directed rounding per CON-0010).
- Profile values are Rayleigh–Ritz upper bounds, 0.3–6% above the infimum.

**C5, function-field transfer.**
- THEOREMS: RH for a curve is equivalent to positivity of one 2g × 2g Toeplitz form (C5-T3, no squarefree hypothesis). By C5-ADJ-W, positivity on one window of half-width greater than (g − 1/2) log q decides RH, sharply over the formal class.
- Census: 12,787 RH-false "fake" zeta functions among 16,354 admissible ones.
- C5-ADJ-LOG: "over ℚ no finite window suffices" is false as stated.
- C5-ADJ-MODEL: zero-side window positivity plus counting asymptotics cannot force RH, so an effective finite reduction must use the Euler product.

### 3.4 Connections and the bridge

- **CON-0032**, the strongest unconditional item: an Euler product plus integer regularity N(x) = ax + O(x^{β+ε}) cannot imply RH for any β > 2/5. It is Observatory-proposed and non-constructive, and rests on BDR Thm 1.3 (arXiv; journal status unverified). The region β < 1/2, Θ ≥ 2/3 has no known countermodel.
- **Bridge.** The host programmes' identity-level prior art and binding obstructions are in [connections/strongest_connections.md](connections/strongest_connections.md) §4. Every item is a proposal for the host's own review.

## 4. The frontier after 2026

Values are as corrected by the ledger verifiers.

| Quantity | Record (ledger status) | 2026 unrefereed claims | Reference |
|---|---|---|---|
| RH verification height | 3,000,175,332,800, i.e. 12,363,153,437,138 zeros (rigorous computation, 2021) | — | LED-VERIF-1 |
| Fixed zero-free half-plane, ζ and all Dirichlet L | none | 11/12 (audited); 7/8 (unaudited); about 0.8741, B_tw = 0.8740585 (imports 7/8) | LED-ZFR-1, -2, -3 |
| Classical zero-free constant R | 5.558691 | 4.896 (reproduced; FND-0003) | LED-ZFR-5, -4 |
| Zero density, sup A(σ) | 30/13 (Guth–Maynard, Annals 2026); DH for σ ≥ 25/32 | — | LED-ZDE-1, -6 |
| Simple zeros on the line, κ* | 0.407511457 (κ ≥ 0.417293962) | 2/3; 0.6725007; 0.67353820 | LED-CRIT-4, -1, -3 |
| Lindelöf exponent μ(1/2) | 13/84 | — | LED-GROWTH-1 |
| de Bruijn–Newman Λ | 0 ≤ Λ ≤ 0.2 | < 0.156821 and others (FND-0011) | LED-DBN-6, -10, -12 |
| Landau–Siegel | computational exclusion for q ≤ 10¹⁰ | c = 1/64 (Guo, App. A; verifier-corrected best all-q constant); 3.0·10⁻³ (Banks) | LED-VERIF-18; LED-LFUN-6 |
| Weil positivity window | Pos((log 2)/2) (Yoshida; Connes–Consani) | Pos(0.8), by computation (Zhu; not directed rounding, per CON-0010) | LED-POS-6, -7 |
| Robin's inequality | verified to 10^(10^13.11485); proved for all 21-free n | — | LED-ARITH-1, -2 |
| Mertens | \|M(x)\| < √x for x ≤ 10¹⁶; first failure below exp(1.96·10¹⁹) | — | LED-ARITH-7, -9 |
| Small gaps μ | < 0.515396 under RH | ≤ 1/2 unconditionally | LED-SPACING-7, -8 |

**What did not move:**
- RH itself, the density hypothesis below σ = 25/32, and μ(1/2);
- the verification height since 2021, and the Robin range since 2021;
- the absence of any unconditional self-adjoint realization of the zeros (LED-OPS-20).

## 5. Top recommendations

1. **Lean replays** (D-01), with explicit user permission and in an isolated environment.
   - Targets: OpenAI at 4eaee875 (QuasiRiemannHypothesis, DirichletSevenEighths, HeckeSevenEighths plus its fidelity proof, SiegelZeros), with comparator and an independent kernel; anthropics/zeta-23-lean v1.0; Kimura's development.
   - Record all hashes. A replay certifies statements, not the papers' arguments.
2. **Human review of the 11/12 imports**, in risk order. First, the Patterson/Kubota transcription against Patterson 1977. Then the Goldmakher–Louvel family, the multiplier cases at l.3175–3196, and Lemma B.2. Write the half-page human proof (D-02).
3. **Audit the 7/8 manuscript** section by section, and run the adversarial round on the quasi-RH dossier, which has never been done.
4. **Close the 2/3 residues** (D-09): a second review of the FND-0004 repair, an independent Arb replay of Knausgård's three inequalities, and the residue on the Lamzouri route.
5. **Review one Siegel core** (Guo Prop. 3.1 is the shortest) to version-of-record standard, and replay Lu–Zaman–Zhao (D-03).
6. **Replay Zhu's Pos(0.8)** with directed rounding. It is the only computational anchor of the window route (C5 FINAL §5, EFR (i)).
7. **Classify before computing, filter before reviewing.** Before running any criterion computation, place it in the C1 horizon table. Before reviewing any claimed proof, apply the C3 checklist and the C2 hitting-set test (D-08).
8. **Attempt the cheap weaker theorems:**
   - Li positivity beyond T², and an explicit Nicolas implication theorem (C1 FINAL §8);
   - infinitely many de Branges failures (C3 FINAL §9);
   - near-line detection with C(δ) = O(log 1/δ) (C4 FINAL §6);
   - the O(1)-error refinement of C5-ADJ-MODEL (C5 FINAL §3.5).
9. **Propagate the FINAL statuses.** Carry the C2/C4/C5 statuses into the proposals/ and frontiers/ files and, after replay, into the findings register. Sync the bibliography audit levels with the audits.
10. **Host repository work.** Treat every 2026 result as unrefereed. Bridge items are proposals for host review, never integrated results.

## 6. Limitations

- **Verification.** All verification was done by AI agents, with no human expert review, and correlated model errors are possible. "No error found" is not a referee verdict, and imported deep inputs were not re-proved.
- **Coverage.**
  - 846 of the 1,000 works are recorded at index level only.
  - Paywalled pre-1995 journals were not accessed.
  - OpenAlex and Semantic Scholar were not used.
  - Non-English literature and families G and H are thin.
- **Text and records.** pdftotext and OCR corrupt formulas (FND-0008 was such an artifact). 260 triage records rely on labelled model recollection.
- **Not replayed.** No Lean was built. The 7/8 manuscript was not audited. Knausgård's searches, Lu–Zaman–Zhao and the Planat–Raymond certificate were not replayed.
- **Finite computations and models.** Finite computations carry no global implication. Campaign model statements stay model statements. All five campaigns were reviewed in three stages by AI agents only.
- **Bookkeeping inconsistencies.**
  - Level-1 counts: 231 attempted and 77 without access in the coverage report, against 232 and 78 in the evidence audit and limitations files.
  - corpus/bibliography.jsonl records only the reading pipeline, so the 2026 works audited at Level 2 appear as L0/L0+.
  - [proposals/independent_campaigns/README.md](proposals/independent_campaigns/README.md) predates the C2/C4/C5 adjudications.
- **Recency.** The status of the 2026 claims may change quickly after the cutoff.

## 7. Where to go next

- [START_HERE.md](START_HERE.md): a one-day reading plan.
- [final_synthesis/open_problems_for_future_agents.md](final_synthesis/open_problems_for_future_agents.md): problems by tractability, pitfalls, protocols and a continuation plan.
- [audits/verified_findings.md](audits/verified_findings.md) and the five campaign FINAL.md files: the primary evidence.

