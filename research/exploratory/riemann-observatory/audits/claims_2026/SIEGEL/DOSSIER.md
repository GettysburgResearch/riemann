# SIEGEL dossier: "Landau–Siegel zeros do not exist: (1 − β) log q ≥ c for every real primitive χ" (2026)

```text
Status: EXPLORATORY AUDIT DOSSIER (exploration layer). This is not an integrated or reviewed packet and makes
        no new mathematical claim. Nothing here says RH is proved, disproved or closer to proved; the claim
        concerns real zeros of quadratic Dirichlet L-functions near s = 1 and is far weaker than GRH.
        Outcome as audited:
          - No verified error, no suspected gap, in any of the four proofs (OAI, Banks, Kerr, Guo).
          - Two harmless missing-hypothesis items in Kerr (q = 8 is outside the argument, with an explicit
            witness; Masser's "basis" hypothesis is unstated but satisfied).
          - Presentation-level items only otherwise.
        None of OAI, Banks, Kerr, Guo or Kimura is refereed: no journal reference or DOI on arXiv (API checked
        2026-11-17), and OAI calls its manuscripts "raw research data". The one refereed input is Lu-Zaman-Zhao
        (Math. Comp., DOI 10.1090/mcom/4268), used only for Banks's all-q constant.
        We did not build or replay any Lean development.
Scope: the statement "there is an absolute c > 0 such that every real zero beta in (0,1) of every primitive
        nonprincipal real Dirichlet L-function of conductor q >= 3 satisfies (1 - beta) log q >= c", as proved in
        OAI (c not explicit), Banks (c = 3.0e-3 for q >= 10^10; all q via LZZ), Kerr (c not explicit) and Guo
        (c = 1/100 for all q; 1/64 in App. A). Kimura's explicit constants (5.811e-4 for all q) are recorded as
        statements only. Out of scope: the OpenAI quasi-RH half-plane claims (audited separately in
        ../../quasi_rh/), Kimura's class-number computation, and the unread follow-ups (Green, van Dijk,
        Pescador, Barreto).
Exact sources or dependencies:
        OAI   = OpenAI, "Uniform exclusion of Landau-Siegel zeros", 1 Oct 2026, github.com/openai/math @
                4eaee87548250b2682affda7d05d947c05554bae, preprints/Uniform-exclusion-of-Landau-Siegel-zeros-
                October-1-2026/ (paper.pdf sha256 fab9f6e8...14ef; build/paper.tex sha256 b011ba9c...ded4, 773 lines;
                "l.N" below refers to paper.tex). Lean: lean/ComparatorChallenges/SiegelZeros.{lean,json}.
        Banks = W. D. Banks, arXiv:2610.15483v1 (11 Oct 2026; latest), PDF sha256 54891704...6d7f.
        Kerr  = B. Kerr, arXiv:2610.21099v1 (15 Oct 2026; latest), PDF sha256 30dc40c9...6116.
        Guo   = V. Z. Guo, arXiv:2610.30476v1 (21 Oct 2026; latest), PDF sha256 f3058ae2...e47a7e.
        Imported: LZZ = Lu-Zaman-Zhao, arXiv:2602.03626v2 = Math. Comp. (online 2026-10-16), Thm 1.1;
                  Masser, Invent. Math. 63 (1981), Thm 1; Rosser-Schoenfeld 1962, Thm 6 (via secondary sources).
        Context (statements only): Kimura arXiv:2610.21511v2 (sha256 5987fa4d...e733); T. Tao, blog post
                  "A sketch of the proof of non-existence of Siegel zeroes", 19 Oct 2026, and its comment thread
                  (snapshot 2026-11-17, sha256 0173ecd3...3979), read as data.
        Full hashes: Section 9. The audit records in this directory are ARCHITECTURE.md, audit_part1.md,
        audit_part2.md, adjudication_U2.md, adjudication_U3.md, adjudication_U4.md and architecture_checks/.
What was actually run:
        Earlier records (summarised, not redone here):
          - line-by-line reading of all four proofs; hand re-derivation of the nine load-bearing steps in each;
          - exact toy replays of OAI Lemma 7 inside Z[a,b] and of Guo Lemmas 3.2-3.3;
          - 4 architecture scripts, 8 part-1/part-2 scripts (130 PASS / 0 FAIL), and 11 adjudication scripts,
            one of them a library (U2: 13/0; U3: constants, two independent implementations of the LZZ test, a
            ball-arithmetic certificate for q <= 5000; U4: 31/0 static Lean checks).
        This dossier:
          - arXiv API metadata for 5 IDs and a Crossref lookup of the LZZ DOI (2026-11-17);
          - re-hashing of every audited file (all match the earlier records);
          - re-reading of OAI paper.tex in full, and of the provenance, scope and limit passages of Banks, Kerr,
            Guo, Kimura, the OAI README / history / lean/docs/003.md, and the Tao post and comments;
          - re-run of architecture_checks/check_constants.py (71 PASS / 0 FAIL);
          - one new script, siegel_dossier/dossier_checks.py (30 PASS / 0 FAIL): arb enclosures of the headline
            constants, the method-ceiling analysis of Section 7.2 (including the closed form 3 - 2 sqrt 2),
            the heuristic exponent count of Section 7.1, and the explicit consequences in Section 5.
        No author code, Lean code, or other repository content was run.
Smallest remaining gap:
        Independent expert review of one nonvanishing-plus-divisibility core, in a version of record. The
        smallest statements whose failure would invalidate the respective proof are:
          OAI/Banks: Lemma 3 (interpolation on a projected box) + Lemma 7 (Delta in p^{E_p} Z[a,b]);
          Kerr: Lemma 5 + Masser's Theorem 1 with mu >= 4/3 (Lemma 7);
          Guo: Proposition 3.1 (Lemmas 3.2-3.3).
        These three cores are structurally independent, so the claim does not rest on any single one. We
        re-derived each and found nothing wrong. Not replayed: the OAI Lean development (642 lines of its
        theorem-1 assembly appear in no reported external build) and Kimura's Lean checks.
```

## 0. Bottom line

* **The claim, precisely.** There is an absolute c > 0 such that L(β, χ) = 0 with β ∈ (0, 1) and χ a primitive real character of conductor q ≥ 3 implies (1 − β) log q ≥ c. This is exactly the statement "Landau–Siegel zeros do not exist" in its standard logarithmic form. It is a statement about real zeros within c/log q of s = 1 only.
* **Proofs.** Four written proofs are audited here. Further variants exist (Green, van Dijk, Pescador, Barreto) and were not read.
  * OAI: produced by an internal OpenAI model, nine pages, not refereed, constant not explicit.
  * Banks, Kerr and Guo: human-signed re-proofs written after reading OAI. Each discloses AI assistance (Claude; ChatGPT; ChatGPT).
  * Explicit constants: Guo c = 1/100 for all q ≥ 3 with no computation (1/64 in App. A); Banks 3.0·10⁻³ for q ≥ 10¹⁰.
* **Audit result.** All nine load-bearing steps were re-derived in each of the four proofs. Every stated constant and rational certificate was recomputed, and the headline constants are now enclosed in ball arithmetic. The finite algebra was replayed exactly at toy sizes, with explicit witnesses that the hypotheses p > H, Frob_p ∈ {σ, στ} and "kernel coordinates Q-independent" are each necessary. No verified error, no suspected gap.
* **What the mechanism is.** If χ(p) = −1, Frobenius at p acts on Z[√d] (or Z[√d, √2]) as conjugation. An auxiliary algebraic object built from small integers of the field (a determinant, a vanishing polynomial, or an injective evaluation map) is then divisible by far more inert primes than its Archimedean size allows, unless inert primes carry at most a fraction κ < 1 of the logarithmic prime mass. A real zero within δ/log q of 1 forces inert primes to carry almost all of it. The zero enters only through that classical first step.
* **Limits.** The arithmetic fraction obeys κ ≥ 1/2 (prime ideal theorem), and the zero couples to the primes with a loss of order δ(log X)². So the method yields a constant c of order 10⁻²; it cannot by itself reach zero-free strips, Chowla-type positivity on (0, 1), GRH-strength consequences, or anything about complex zeros (Section 7).

## 1. Exact claims and their status

| Source | Exact statement | Refereed? | Provenance (as stated by the source) | Lean claimed | Lean replayed by us |
|---|---|---|---|---|---|
| **OAI** (9 pp.) | **Thm 1** (l.66–73): absolute c > 0 with (1 − β) log q ≥ c for every real zero β ∈ (0, 1) of every primitive nonprincipal real L(s, χ), q ≥ 3. No value of c. Proof by contradiction along a sequence; bounded q by finiteness (l.665–676). | No. OAI README: manuscripts are "raw research data, rather than polished academic papers"; Kimura: "[SZ] has not been refereed". | "Produced by an unnamed internal OpenAI model" (README). Part of OAI family 003 together with the quasi-RH half-plane claims. | Yes: comparator challenge `SiegelZeros.json`, theorem `OAI.SiegelZeros.WeightedTorusJets.exists_absolute_real_zero_gap` (lean/docs/003.md). The formal statement matches Thm 1 (adjudication_U4 §2.1). | **No** |
| **Banks** v1 (19 pp.) | **Thm 1.1**: for q ≥ q0 = 10¹⁰, (1 − β) log q ≥ δ0 = 3.0·10⁻³ (exactly 81/(5888e^{3/2}) = 3.06956·10⁻³, Rem. 7.1). For all q ≥ 3: some c > 0 by finiteness, and c = 3.0·10⁻³ "by the computation of [LZZ]", which Banks says he did not verify. | No journal reference or DOI (arXiv API, 2026-11-17). | "The argument of the present paper is the argument of [OAI], and we claim no originality for its ideas." Claude produced "an initial report … and an expanded draft of the proof"; "every line of the paper has been verified by the author". | No | — |
| **Kerr** v1 (6 pp.) | **Thm 1**: absolute c > 0, (1 − β) log \|q\| ≥ c for χ = (q/·), q a fundamental discriminant. Not explicit. | No journal reference or DOI. | "Simplifies the recent OpenAI proof." "ChatGPT assisted with the mathematical development and preparation of this paper." Developed after Banks's draft. | No | — |
| **Guo** v1 (17 pp.) | **Thm 1.1**: (1 − β) log q > 1/100 for every primitive quadratic χ, q ≥ 3. **Rem. 1.2 / App. A**: 1/64. **Prop. 3.1** (unconditional): S₋(x, χ) ≤ (11/20) log x + (29/60) log q + 6 for x ≥ 2. | No journal reference or DOI. | "Follows the Frobenius method of [OAI] and its subsequent variants." "ChatGPT assisted with the development, organization, calculations, and drafting of this note." | No | — |
| Kimura v2 (context) | **Thm 1**: (1 − β) log q ≥ 5811·10⁻⁷ for all q ≥ 3, and ≥ 1193/200000 = 0.005965 for log q ≥ 35.0131; ≥ 0.01015 for log q ≥ 10⁴ (proof of Thm 1). | No journal reference or DOI. | Makes the OAI argument explicit; Claude Opus 5.5 used for the explicit argument, Lean files and text "under the author's direction" (§8). | Yes: reports Lean-kernel and nanoda checks of its own theorems, which import 254 of 306 OAI modules unmodified (adjudication_U4 §2.5). | **No** |
| LZZ (imported by Banks) | **Thm 1.1**: q ≤ 10¹⁰ ⇒ L(σ, χ) ≠ 0 for σ ≥ 1 − 1/(5 log q), every quadratic χ mod q. | **Yes**: Math. Comp., DOI 10.1090/mcom/4268 (Crossref: published online 2026-10-16). | Human; ball-arithmetic computation (~1.5·10⁵ core hours). | — | — (production run not replayed) |

**Expert reception (context, not refereeing).**
* Tao's 19 Oct 2026 post: "Recently, the Siegel zero problem has been solved in a number of ways." It sketches B. Green's formulation (hexagon:2610.00311v2, not read by us), with the unconditional bound S₋(x) ≤ ½ log x + O(log |D|) + O(log log x).
* Green, in the comments: "There will be a communal writeup with all of these ideas (intended to be published in something like the traditional way, as a version of record) in due course."
* As of 2026-11-17 we know of no version of record.

## 2. Provenance, independence and disclosure

* **No written proof is free of AI involvement.**
  * The OAI manuscript is model output.
  * Banks used Claude for the first draft and throughout, then verified every line himself.
  * Kerr and Guo used ChatGPT.
  * Kimura used Claude.
  * Guo's web source [9] (Pescador) is "produced using GPT-6 Pro (OpenAI) and Claude Opus 5.5 (Anthropic)".
  * The human checks on record are therefore the authors' own verification (explicit in Banks), Tao's and Green's expositions, and Kimura's reported kernel checks.
* **None of Banks, Kerr or Guo claims independent discovery.** All three were written after, and from, OAI.
* **The arithmetic cores are nevertheless structurally different** (ARCHITECTURE §3):
  * OAI/Banks: interpolation determinant in Z[√d, √2], weighted greedy rows, Hadamard.
  * Kerr: Siegel-lemma pigeonhole modulo ∏ p^{k_p}, with Masser's 1981 zero estimate (μ = 4/3).
  * Guo: integer coefficient counting plus Stepanov-type injectivity at an auxiliary inert prime, in Z[√d] alone.
* **The analytic inputs differ.**
  * OAI, Banks and Kerr use the Hadamard log-derivative inequality.
  * Guo uses no complex analysis: a paired-tail hyperbola estimate and positivity of 1 ∗ χ.
* **Relation to the quasi-RH claims.**
  * OAI family 003 also contains zero-free half-plane claims (Re s > 7/8, and Re s > 11/12 by a second proof) for all Dirichlet L-functions. If correct, these imply SIEGEL with 1 − β ≥ 1/8 (resp. 1/12).
  * The SIEGEL proofs do not use them. Guo §1.1 cites the 7/8 claim but states that it "is not an input" (T5).
  * The 11/12 paper is audited separately in `../../quasi_rh/DOSSIER.md`; the 7/8 paper is not audited.
* **Auditor disclosure.**
  * This dossier and the audits it summarises were produced by AI agents (Claude, Anthropic).
  * Claude also assisted Banks's and Kimura's papers. Our audit is therefore not independent of the model family that helped write two of the follow-ups.
  * It is independent of the OpenAI model that produced the claim.
  * Weight our "no error found" by the explicit re-derivations and witnesses it records, not by its authorship.

## 3. Audit coverage and outcomes

Step numbering is that of ARCHITECTURE.md §5. "OK" means no issue was found in the inspected portion.

| # | Load-bearing step | OAI (paper.tex) | Banks | Kerr | Guo | Our status (where) |
|---|---|---|---|---|---|---|
| 1 | Prime bias forced by the zero | Lem 2 | Lem 2.1 | Lem 1 | Prop 4.1, Lem 5.1 | OK. Re-derived. Zero-free −L′/L ≤ ½ log q − κ checked on 75 discriminants. Guo's paired-tail identity tested in unconditional form on 390 (χ, β, t) triples. The RS62 inequalities Banks uses were proved without RS62, given BKLNW Table 15 above 10⁷ (part 1 §1; adj. U2) |
| 2 | Frobenius = conjugation at inert p | (frobenius) | Lem 6.1 | (3)–(4) | (3.6), (3.9) | OK. About 55,000 exact congruence tests, all four Frobenius classes (part 1 §2) |
| 3 | Unitriangular weight-lowering basis change | Lem 7 | Lem 6.2, 4.1(a) | Lem 2 | (3.8) | OK. Exact transition matrices (part 1 §3) |
| 4 | p-adic extraction | Lem 7, (lower) | Cor 6.3 | Lem 4 | (3.10), Lem 3.2 | OK. Lemma 7 replayed **inside Z[a,b]**: 9 admissible tests, 6 with equality. Witnesses that p > H and Frob ∈ {σ, στ} are necessary (part 1 §4) |
| 5 | Nonvanishing at degree U ≍ N^{4/3} | Lem 3, Cor 4 | Prop 3.4, Cor 3.5 | Lem 6–7 (Masser) | Lem 3.3 | OK. Masser Thm 1 checked against the 1981 scan. Spanning threshold equals the dimension floor in 9 fields. Witness at d = 2: the conclusion of Lemma 3 fails at N = 53, and Kerr's μ drops to ≤ 1 (part 2 §1) |
| 6 | Degree concentration in the divisible coordinate | Lem 6 | Lem 4.2 | weight 8 | λ ≤ 1/30 | OK. Lossy constants (T6), correct (part 2 §2) |
| 7 | Archimedean size | (upper) | Lem 5.1 | Lem 3, 5 | Lem 3.2, (3.11) | OK. Exact N(Δ) sandwich in 8 toys (part 2 §3) |
| 8 | Exponent gap | (master): 1 ≤ 13/16 + 1/16 | (7.3) | 5/4 < 13/10 < 4/3 | (5.13)–(5.15) | OK. Order of parameter choices checked for circularity. Guo's chain has positive margin on 65 conductors from 3 to 10¹⁵, worst at q = 3 (exact-log margin 0.3256; rational 0.2579) (part 2 §4) |
| 9 | Parameters, small conductors | finiteness | q0 = 10¹⁰; LZZ | implicit (T1) | single choice for all q ≥ 3 | OK. LZZ dependence adjudicated (U3). Certified L(σ, χ_d) > 0 on [½, 1] for 3 ≤ \|d\| ≤ 3000 (part 2 §5; adj. U3 §4.3) |

**Not done.**
* No Lean build, kernel replay or comparator run, for either OAI or Kimura (policy: no execution of third-party build code).
* LZZ's production run for 4·10⁵ < q ≤ 10¹⁰ was not replayed. It was spot-checked: 312 discriminants, and an independent re-implementation on 20 of them.
* Page-level checks were not done for Davenport (Kerr's "[2, eq. (2), p. 89]"; U1), Apostol (U6) and RS62 p. 70 (U2 residual, bibliographic only).
* Not fetched: Green (hexagon:2610.00311v2), van Dijk (hexagon:2610.00409v2), Pescador's web note, and the Barreto and Pescador short proofs mentioned by Green. These are relevant to Section 7.1 (κ → ½) but not to the claim as audited.
* Kimura's explicit chain was read only for its statements, Remark 7, Lemma 8, Remark 11 and §8.

## 4. Adjudicated findings (consolidated)

The IDs are those of the underlying records. "Effect" means effect on a stated theorem.

| ID | Class | Location | Finding | Witness / evidence | Effect |
|---|---|---|---|---|---|
| — | **verified_error** | all four sources | **none** | — | — |
| — | **suspected_gap** | all four sources | **none** | — | — |
| M1 / P2-5 | missing_hypothesis (harmless) | Kerr, K = Q(√q, √2) "has degree four" | Fails for q = 8. Then Lemma 7's hypothesis fails and Kerr's argument does not apply. | γ1, γ4, γ2 − 2γ3 are Z-independent and lie in the plane x1 = x3, so μ ≤ 1. F = ∏_{s ≤ 3N−3}(x1 − x3 − 2√2 s), of degree 3N − 2, vanishes on all points (part 2 §1.3 (5b)). | None: one conductor, covered by the implicit finiteness step (T1). OAI and Banks exclude d = 2 explicitly. |
| M2 | missing_hypothesis (harmless) | Kerr Lem 6 | Masser's Thm 1 requires γ_j to be basis elements of Γ. Kerr does not state this. | Satisfied: π is injective on Z⁴ because ker π ∩ Q⁴ = 0. | None |
| P1-4 | no_issue (necessity witness) | OAI Lem 7 | Dropping p > H or Frob ∈ {σ, στ} breaks the divisibility. | d = 5, N = 2, H = 4, p = 3: v₃(Δ) = 5 < 9. Frobenius τ: d = −1, p = 5: v₅(Δ) = 0 < 1. | Hypotheses correctly stated |
| P2-6 | no_issue (necessity witness) | OAI Lem 3 / Banks Prop 3.4 | "Kernel coordinates Q-independent" is load-bearing. | d = 2: the budget holds at N = 53 (t = 1396), but spanning needs t ≥ 1430. | Correctly stated; d = 2 excluded |
| U2 | not_an_issue (adjudicated) | Banks (2.7) ← RS62 Thm 6 | Original not re-read. | The quoted inequalities were proved independently: arb ball arithmetic below 10⁷, BKLNW Table 15 above. Thresholds 319 and 32 reproduced as least integers. | None. Bibliographic residual only. |
| U3 | not_an_issue (adjudicated) | Banks all-q c = 3.0·10⁻³ | Declared external dependency on LZZ Thm 1.1, not replayed. | Imported statement matches its use. Two implementations of LZZ's test agree exactly on 20 discriminants. q ≤ 5000 certified directly. **New:** LZZ now has a Math. Comp. DOI. | None on Banks's q ≥ 10¹⁰ statement or on Guo's 1/100 |
| U4 | unresolved_ambiguity (narrowed; not load-bearing) | OAI Lean | Not replayed. Static scan of 318 files clean. Formal statement matches Thm 1. The formalization replaces Lemma 3 by a multiplicity estimate. Kimura's reported checks cover 254 of 306 modules but not OAI's final theorem. | — | Formal status only. No audit conclusion used Lean. |
| U1, U6 | unresolved_ambiguity (harmless) | Kerr Lem 1 citation; Guo's Apostol theorem numbers | Page and equation numbers not matched against the books. | Every use re-derived | None |
| U5 | unresolved_ambiguity (harmless) | Guo's hexagon and web sources | Not fetched. | Guo re-proves everything he uses | None |
| T1 | typo_or_presentation | Kerr | Small \|q\| and q = 8 are left implicit. | — | None |
| T2 | typo_or_presentation | OAI | c is not explicit (contradiction along a sequence). | Made explicit by Banks, Guo and Kimura | None |
| T3 | typo_or_presentation | Banks Lem 3.3 | "Proof. Exercise." | Standard induction | None |
| T4, T5 | typo_or_presentation | Guo §1.1 | The Kimura comparison uses 1/100 rather than Guo's own 1/64. Guo cites the unrefereed 7/8 claim, which is not used. | — | None |
| T6 / P2-9 | typo_or_presentation | OAI Lem 6, Banks Lem 4.2 | Very lossy constants (guaranteed S₂/S₁ ≤ 7.2·10⁶/H; toys below 1/3 already at H = 6–8). | — | None; only existence matters |
| T7 | typo_or_presentation | OAI (eq:mass) | p ∤ q is redundant given χ(p) = −1. | — | None |
| P2-7 | typo_or_presentation | Banks §7 | The (ω + 1) slack costs 4.4%: 3.209·10⁻³ would follow from the same chain. | exact arithmetic | None |
| D-1 | correction to our own records | ARCHITECTURE §1, part 1 U4 | "69,818 lines" undercounts the trusted Lean closure: 69,818 + 6,754 patched into PrimeNumberTheoremAnd = 76,572. Kimura's checks need the qualifier above. | adjudication_U4 §0 | Records only |

Known misreadings to avoid:
* "No Siegel zeros" here means a gap c/log q at s = 1. It does not exclude real zeros in (½, 1 − c/log q) (lean/docs/003.md says the same).
* The OAI construction as written has size slope log N = ¾ log U (l.131–132), so its arithmetic fraction tends to ¾ as H → ∞ (13/16 at the H used).
* Tao's blog comment (19 Oct, 11:49) speaks of "more like 2/3 log x" for biquadratic arguments without Green's multiplicity trick. We did not determine which variant is meant. Under the heuristic count of Section 7.1, 2/3 corresponds to three conjugate coordinates in a degree-8 field, not to the OAI layout. This is immaterial to correctness.
* The constants 1/100, 1/64, 3.0·10⁻³ and 5.811·10⁻⁴ are lower bounds for the same quantity inf (1 − β) log q. A smaller constant is a weaker theorem, not a disagreement.

## 5. Consequences if correct (precise)

Assume Guo's Theorem 1.1 (c = 1/100), or any of the other proofs with its constant. "Auditor's derivation" marks statements that are ours and not in the sources.

1. **Real-zero gap for every real character.** Let χ be a nonprincipal real character mod q, not necessarily primitive, induced by χ* of conductor q* ≥ 3. Every real zero β ∈ (0, 1) of L(s, χ) satisfies (1 − β) log q ≥ (1 − β) log q* ≥ c. The extra Euler factors vanish only on Re s = 0.
   * Constants: c = 1/100 for all q ≥ 3, or 1/64 (Guo); 3.0·10⁻³ for q ≥ 10¹⁰, and for all q given LZZ (Banks); Kimura's 5.811·10⁻⁴, 0.005965 and 0.01015 in their ranges (statements only).
2. **The classical zero-free region holds with no exceptional character.**
   * For every Dirichlet character χ mod q ≥ 3, L(σ + it, χ) ≠ 0 for σ ≥ 1 − c′/log(q(|t| + 2)), with c′ = min(c₁, c) effective. Here c₁ is the classical constant (Davenport Ch. 14), and the only possible exception there was a simple real zero of a real χ.
   * Page's theorem and the Deuring–Heilbronn dichotomy lose their exceptional branch.
3. **Effective Siegel: L(1, χ) ≫ 1/log q** (Hecke's implication; Kimura Lemma 8 and Prop. 9 make it explicit).
   * Auditor's derivation (audit_part1 §9; recomputed in arb here): L(1, χ) log q ≥ 0.0076709 for q ≥ 10, tending to c e^{−2c} ≈ 0.0098.
   * Hence h(D) ≥ 0.00244 √|D|/log |D| for D < −4, and h(D) log ε_D ≥ 0.0038 √D/log D for D > 0.
   * Previously the best effective lower bound was Goldfeld–Gross–Zagier's ≫ log |D|; Siegel's |D|^{1/2−ε} is ineffective.
   * Class-number tables cannot test this: the bound forces h > 1 only for |D| ≳ 3·10⁷ (audit_part2 §9).
4. **Effective prime number theorem in progressions.**
   * Siegel–Walfisz becomes effective, with error x·exp(−c″√log x) uniformly for q ≤ exp(c″√log x), with no exceptional term (classical consequence; Davenport Ch. 20, recalled).
   * Tao's post states the corresponding upgrade for Σ_{p ≤ x} (D/p) log p/p.
5. **Class-number tabulation** (Kimura's claims; not audited by us).
   * All imaginary quadratic fields with h ≤ 2000: 16,453,493 fields, largest |d_K| = 1,062,350,083.
   * The GRH-conditional lists of Cremona–Sutherland (orders, h ≤ 1000) and Holmin et al. (odd h ≤ 1999) become unconditional.
   * Kimura's route rests on its own Lean-reported constant, an unverified sieve program and the Mosunov–Jacobson tables.
6. **Class groups of exponent ≤ 2** (auditor's derivation; dossier_checks (C)).
   * Genus theory gives h = 2^{ω(D)−1} for such D. With h ≥ 0.00767 √|D|/(π log |D|), every imaginary quadratic field whose class group has exponent ≤ 2 has **|D| < X₀ = 1.5655·10¹⁶**.
   * Chowla's finiteness theorem (1934, recalled) was ineffective only because of a possible Siegel zero; the problem now reduces to a finite search.
   * Fields with h ≤ 1024 would appear in Kimura's h ≤ 2000 list. The remaining window is 1.48·10¹³ ≤ |D| < X₀ with ω(D) ∈ {12, 13, 14}. That search was not done.
7. **Effective Brauer–Siegel for fields with a normal tower over Q** (recalled, not re-derived). Stark (1974) showed that the only obstruction to effectivity there is an exceptional zero coming from a quadratic subfield. That obstruction is removed.
8. **Conditional "Siegel-world" theorems become vacuous, not false.** Examples: Heath-Brown on twin primes under infinitely many Siegel zeros; Friedlander–Iwaniec; Tao–Teräväinen (Hardy–Littlewood–Chowla in the presence of a Siegel zero).
9. **Relation to abc.** Kimura notes that Granville–Stark (2000) derived this bound for imaginary quadratic χ from a uniform abc conjecture for number fields. The theorem is consistent with that, and does not imply abc.

## 6. What is not implied

* **Not RH, not GRH, not a quasi-RH half-plane.**
  * Nothing is said about complex zeros. The classical region keeps its shape c′/log(q(|t| + 2)), and its constant c₁ is not improved.
  * The OAI half-plane claims would imply SIEGEL, not the other way round. They are separate, unrefereed, and only the 11/12 paper is audited (../../quasi_rh/).
* **Not Chowla's conjecture** (L(σ, χ) > 0 on (0, 1)). Real zeros in (½, 1 − c/log q) are not excluded. LZZ's computational 1/5 for q ≤ 10¹⁰ is not reached by any proof here (Section 7.2).
* **Not GRH-strength consequences.**
  * L(1, χ) ≫ 1/log q, not ≫ 1/log log q (Littlewood under GRH).
  * Kimura's Remark 11 notes that a zero-free half-plane, which also excludes complex zeros, would give h(−d) ≫ √d/log log d effectively (Littlewood's argument). SIEGEL alone gives √d/log d.
* **Not a better Linnik constant or least non-residue bound.**
  * Linnik's theorem was already effective.
  * The arithmetic layer has no small-prime strength in q: from Guo's (3.1), "all odd primes ≤ x inert" gives only log x ≤ (29/27) log q + 18.2, weaker than trivial (audit_part2 §10).
  * We have not checked whether c ≈ 10⁻² improves any explicit Linnik exponent. In Heath-Brown-type case analyses an exceptional zero is handled by Deuring–Heilbronn repulsion (recalled, not re-checked), so no improvement follows automatically.
* **Not level-of-distribution results.** Bombieri–Vinogradov, Elliott–Halberstam and zero-density estimates are unchanged.
* **Not other L-functions.**
  * The theorem is over Q, for quadratic Dirichlet characters.
  * Not claimed: quadratic Hecke characters of number fields K ≠ Q; exceptional zeros of Dedekind zeta functions outside Stark's normal-tower reduction; Artin or GL(n) L-functions.
* **Not "proved in Lean" by us.** The formal statements are the authors'. Neither OAI's nor Kimura's development was replayed. The OAI formalization does not formalize the paper's Lemma 3 as written.
* **Not refereed.** As of 2026-11-17 only the imported LZZ (Banks's all-q constant) has a version of record.

## 7. The method's limits (what prevents going further)

### 7.1 The arithmetic fraction κ has a hard floor at ½

Every proof establishes an unconditional bound S₋(X) ≤ κ log X + e log q + O(1) for X a power of q, with S₋(X) = Σ_{p ≤ X, χ(p) = −1} log p/p.
* For a fixed field, the prime ideal theorem gives S₋(x) = ½ log x + O_d(1). Hence **κ ≥ ½** for any valid bound of this shape.
* All versions comply:
  * OAI/Banks: 13/16, tending to ¾ as H → ∞;
  * Kerr: 39/40 as used, 15/16 intrinsic at weight 8, tending to ¾ as the weight grows;
  * Guo: 11/20, tending to ½;
  * Green, van Dijk, Barreto: ½ + o(1), reported, not read by us.
* None of them overshoots, which is a strong consistency check (audit_part2 §4.3).
* **Heuristic count (auditor's; dossier_checks (B)).** Adjoin r − 1 further square roots and use θ together with m conjugates whose Frobenius classes are inert in Q(√d). Then:
  * size slope log N/log U = (1 + m)/2^r;
  * usable inert fraction m/2^{r−1};
  * κ(m) = (1 + m)/(2m).
* So m = 2 gives OAI's ¾, m > 1 is needed for any gain, and κ → ½. This agrees with the observation Tao attributes to A. Pascadi ("arbitrarily close to ½ by adjoining enough new square roots"). It assumes a zero estimate with the generic exponent for larger kernels, which we have not checked.

### 7.2 The analytic coupling caps the constant

The zero enters only through step 1: the split-prime mass up to X = q^A is ≤ bδA² log q + O(log q). Combined with 7.1, this gives the generic inequality (1 − κ)A − K ≤ bδA², hence δ* = (1 − κ)²/(4bK).

The ceiling is a fixed number, and κ ≥ ½ keeps it from growing. Recomputed ceilings (dossier_checks (B); "y" is Guo's inner scale y = q^B):

| Chain and arithmetic input | Asymptotic ceiling on c (q → ∞) | Status |
|---|---|---|
| Banks's chain (κ = 13/16), continuous optimum | 3.244·10⁻³ | recomputed (arb); Banks states 3.07·10⁻³ |
| Kimura's OAI-type chain (Remark 7) | max η²e^{−η}/(16 + 8e^η) = 1.0196·10⁻² at η = 1.2268 | recomputed; Kimura: "≈ 1.02·10⁻²" |
| Guo's comparison, Prop. 3.1 as stated (11/20, 29/60), y ≥ q^{2+} | 0.06095 | recomputed; matches parts 1 and 2 |
| Guo's comparison, Barreto shape (½, ¼), y ≥ q^{2+} | 0.0788 | auditor's computation |
| Guo's comparison, ideal arithmetic (½, 0), y ≥ q^{2+} | 0.0858 | auditor's computation |
| Guo's comparison, ideal arithmetic, hypothetical y → q | **3 − 2√2 = 0.171573**, exact | closed form: optimum at A = 2 + 2√2, where the main constraint and Lemma 5.1's cap ε log(xy) ≤ 1 coincide (sympy) |

Reading of the table:
* Guo's y ≥ q^{2+} comes from the trivial bound |Σχ| ≤ q/2 in Prop. 4.1. Reaching y → q would need, for example, a Pólya–Vinogradov-strength remainder. That is a hypothetical improvement, not a claim.
* Even with ideal arithmetic and that improvement, Guo's comparison cannot certify c ≥ 0.1716 < 1/5. So **no chain of the present shape reaches LZZ's computed 1/5**, let alone (1 − β) log q → ∞.
* The binding constraint is analytic. A zero at distance δ/log q biases primes only up to about X = q^{O(1/δ)}. The arithmetic side needs X ≥ q^{A} with A ≳ 2K/(1 − κ) ≥ 4K, because the point heights √q contribute the term e log q.
* These ceilings bound chains, not zeros.

### 7.3 No small-prime or q-aspect strength

The arithmetic bound carries e log q because the evaluation points have height ≍ √q. Its entire strength is the x-slope κ < 1 at X = q^{large}, exactly where a Siegel zero would force inert dominance. It says nothing new about:
* the least split prime;
* the least quadratic non-residue;
* primes up to q^{O(1)}.

The data agree: across 115,502 fundamental discriminants with 10⁴ ≤ |D| ≤ 2·10⁵, the first non-inert prime is ≤ q^{0.362} (audit_part2 §10).

### 7.4 Only real zeros, only quadratic characters, only inert primes

* **The mechanism needs χ(p) = −1 dominance.** A complex zero ρ = β + iγ near 1 biases χ(p)p^{−iγ}, which has no Frobenius-conjugation meaning. Characters of order > 2 have no exceptional zeros to begin with.
* **Split primes contribute nothing.** In Guo's construction this is forced: ∂_z(z^p − z) ≡ −1 (ARCHITECTURE §3). Tao reports that a dual construction bounds the split-prime mass (going back to Selberg 1949, with an error O_D(1)). That bound is useless against zeros.
* **The method is not parity-limited.** Its parity-breaking input is integrality (the polynomial method), as Tao notes. But it sees only "Frobenius = conjugation" for quadratic extensions of Q.

### 7.5 The analogue of "toward 100%": from c > 0 to a zero-free strip

* The natural strengthenings are not reachable within the method:
  * (1 − β) log q → ∞;
  * a fixed zero-free interval [1 − η, 1);
  * positivity on (½, 1).
* Each would need either κ < ½, which contradicts the prime ideal theorem, or an analytic coupling without the δ(log X)² loss, which Section 7.2 shows is the binding constraint.
* Improvements of c inside the method are bounded by the ceilings above, of order 10⁻¹ at best. The quasi-RH route claims more by an entirely different, automorphic mechanism; Tao calls it "some (still poorly understood) automorphic miracle".

### 7.6 Note on the "2/3 toward 100% on the line" clause of the task template

That clause belongs to the separate claim audited in `../CRIT23/` (proportion of zeta zeros on the critical line). It has no counterpart here. SIEGEL concerns real zeros near s = 1, and nothing in CRIT23 bears on it; CRIT23 DOSSIER §7.6 records the converse. The SIEGEL analogue of that clause is Section 7.5.

## 8. Next precise research steps

1. **Version of record and expert review.**
   * Track the communal writeup announced by Green, and any journal submissions of Banks, Kerr or Guo.
   * Ask an independent reviewer to check one complete core with exact SHA-pinned sources. Guo Prop. 3.1 is the shortest; OAI Lemma 3 + Lemma 7 is the original.
2. **Lean replay in an isolated, separately authorised environment** (not done here, by policy).
   * Build `OAI.NumberTheory.SiegelZeros.Main` at 4eaee875 (Lean v4.34.1, Mathlib d13f23b) and run `comparator ComparatorChallenges/SiegelZeros.json` with nanoda enabled.
   * Replay Kimura's `B4.Chi8.zero_gap_all` (cln-imq-2k @ e66ab86). It implies the formal statement with c = 5.811·10⁻⁴ without OAI's final assembly.
   * Cheaper partial step: read the 642 lines of the chain-A assembly that no reported external build covers (adjudication_U4 §3).
3. **Audit the κ = ½ variants** before relying on Section 7.1's floor being attained: Green (hexagon:2610.00311v2), van Dijk (hexagon:2610.00409v2), Pescador's Stepanov-type note, and Barreto's 3-page proof. Pin versions and hashes.
4. **Improve the explicit constant inside its ceiling.**
   * Replace Guo's trivial character-sum remainder in Prop. 4.1 by an explicit Pólya–Vinogradov bound, so that y can move from q^{2+} toward q^{1+}.
   * Combine this with the sharpest audited arithmetic bound.
   * The auditor's ceilings (0.146 with the Barreto shape; 0.1716 with ideal arithmetic) indicate how far the present comparison can go.
   * A useful negative target: prove that no comparison of Lemma 5.1 type reaches 1/5, or find the structural change (avoiding the εκ loss) that would.
5. **Extensions (open problems, not claims).**
   * (a) Quadratic Hecke characters over a number field K: relative Frobenius conjugation in O_L for primes of K inert in L, points of height ≍ |d_L|^{1/2}, a Masser-type zero estimate for the rank-[L:Q] lattice.
   * (b) Stark's residual cases for Dedekind zeta functions of non-normal fields.
   * (c) Check the larger-kernel zero estimate behind the heuristic κ(m) = (1 + m)/(2m) of Section 7.1.
6. **Effective consequences to carry out.**
   * The finite search for exponent-2 class groups with 1.48·10¹³ ≤ |D| < 1.5655·10¹⁶ and ω(D) ∈ {12, 13, 14} (Section 5.6).
   * Tao's "tenth discriminant challenge", posted around 20 Oct 2026 and not read by us.
   * Explicit effective Brauer–Siegel constants via Stark's reduction.
7. **Bibliographic residues** (non-blocking): RS62 p. 70 (U2), Davenport p. 89 eq. (2) (U1), and Apostol theorem numbers (U6).
8. **Record maintenance.** Apply the reclassifications recommended by the adjudications: U2 and U3 become not_an_issue, and U4 is narrowed. Update the line counts in ARCHITECTURE.md §1 and audit_part1.md §11 (D-1). Cite LZZ as Math. Comp., DOI 10.1090/mcom/4268. These edits are not made here, so the reviewed records stay unchanged.

## 9. Reproduction and hashes

**Scripts.** All are under `research/exploratory/riemann-observatory/`. Run each with `python3 -I <script>` from its directory.

| Location | Scripts | Result | Recorded in |
|---|---|---|---|
| `audits/claims_2026/SIEGEL/architecture_checks/` | check_constants, check_divisibility_toy, check_guo_injectivity_toy, check_consequences | check_constants 71/0, re-run in this dossier (`siegel_dossier/architecture_check_constants_rerun.out`); others as recorded | ARCHITECTURE §14 |
| `experiments/code/claims_2026/siegel_l2_part1/` | s1_analytic_layer, s2_s4_frobenius_extraction, s3_constants_consistency, s4_consequences_barriers | 15 + 18 + 54 + 7 = 94 PASS / 0 FAIL (from the saved .out files) | audit_part1 §12 |
| `experiments/code/claims_2026/siegel_l2_part2/` | s5_nonvanishing, s6_s7_concentration_size, s8_s9_gap_parameters, s10_consequences | 14 + 6 + 11 + 5 = 36 PASS / 0 FAIL | audit_part2 §12 |
| `experiments/code/claims_2026/siegel_adjudication/` | adj_U2_*, adj_U3_* (pass 1 and pass 2), adj_U4_lean_static | U2 13/0; U3 see adjudication_U3 §4; U4 31/0 | adjudication_U2/U3/U4 |
| `experiments/code/claims_2026/siegel_dossier/` | dossier_checks.py | 30 PASS / 0 FAIL, 0.4 s | this file |

**Files of this dossier (sha256).**
```text
experiments/code/claims_2026/siegel_dossier/dossier_checks.py                        d9ee9d5e78db6c1a3bbeb34adb7be3df4c3f2c6106f2ffda9679649d8171aa6c
experiments/code/claims_2026/siegel_dossier/dossier_checks.out                       992e249b1159957fb05f397d67cd77a7ae47db869774a137d9fe0fe3a5777638
experiments/code/claims_2026/siegel_dossier/architecture_check_constants_rerun.out  13045a705707110278029006fbdfbb7ad87dca254c22192044f7880cb64ad958
experiments/code/claims_2026/siegel_dossier/arxiv_api_2026-11-17.xml                a591ad694815c03f75e19c45589285789fe64d63f52ba4cfdd26f452194121f3
audits/claims_2026/SIEGEL/architecture_checks/check_constants.py                     36b57a8350962340dd591123ad77c3be32fcb79c6ceaec9a3c8f29f7250e2f01
```

**Sources (sha256, re-verified by dossier_checks (H)).**
```text
OAI paper.pdf             fab9f6e84ece2a37d834b2c031d8eb14e81413d9f6270791e7b5468b295214ef
OAI build/paper.tex       b011ba9c1f55ee2164292492c55e0c6d75c458eb30d4808808f9953823b8ded4  (773 lines)
OAI SiegelZeros.lean      bedaac0248a641910f79a380d9702d82c6bfbbfd3760a69d27c72c5d8fb136ce
OAI SiegelZeros.json      620696740156c4503f27ac17760adf1b638f621ad81ab4cde7a0f8df32c4b643
Banks 2610.15483v1 PDF    54891704515ba9d58ae60ce4c16f4b368a377a9732ca98e26172209fa0647d6f
Kerr  2610.21099v1 PDF    30dc40c959735eaaddd3609919695f87258ec2807fb615a9a4386702f3536116
Guo   2610.30476v1 PDF    f3058ae2a77e5c8e277cf90ed0faf8f745b8b638442b3439dfbf230e93e47a7e
Kimura 2610.21511v2 PDF   5987fa4df134c5d94faf92a0278af96fcf18ac6adfb25adaddb7d6ff63e5e733
LZZ v1 / v2 PDF           77388d40...1a40 / 24b4f92e...42d8 (adjudication_U3 header)
Tao post snapshot (HTML)  0173ecd30eb86a3c3d799e0b74c878a93885a72f1a4dc1ae1340f72a353c3979 (2026-11-17; not stored)
```

**Status queries (2026-11-17).**
* arXiv API, id_list = 2610.15483, 2610.21099, 2610.30476, 2610.21511, 2602.03626: no journal_ref for any; DOI only for 2602.03626 (10.1090/mcom/4268). The response is stored as `arxiv_api_2026-11-17.xml`.
* Crossref, 10.1090/mcom/4268: journal-article, Mathematics of Computation, published online 2026-10-16.

Software: Python 3.13.18, python-flint 0.9.0, mpmath 1.3.0, sympy 1.14.0, numpy 2.5.3.
