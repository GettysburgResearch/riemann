# Ranked research directions (Riemann Observatory)

```text
Status: EXPLORATORY / OBSERVATORY-PROPOSED agenda. This is a ranked list of research directions, not a
        result, not a review approval and not an integrated packet. RH is open. Every mathematical statement
        below carries its status label. The quasi-Riemann hypothesis (OpenAI, 2026: half-planes Re s > 7/8
        and Re s > 11/12) and the "two thirds of the zeros are simple and on the critical line" theorem
        (Alpoge-Furman, AI-discovered and human-verified; Lamzouri, human) are UNREFEREED 2026 claims. The
        11/12 paper was Level-2 audited by the Observatory (AI agents) with no error found; its imported
        metaplectic and large-sieve inputs were not re-proved. The 7/8 paper was not audited; its Lean
        formalization is claimed and was not replayed. The Landau-Siegel exclusion (OpenAI; Banks, Kerr,
        Guo) is unrefereed; the Observatory audit found no error and replayed no Lean. Scores and ranks are
        the synthesizer's judgment (HEURISTIC), not calibrated against outcomes.
Scope: 36 directions ranked by expected value EV = significance x tractability. Coverage: verification and
        method limits of the 2026 claims; extensions of the 2/3 (rank-trace) method; consequences and
        limits of Siegel-zero exclusion; directions arising from campaigns C1-C5; directions useful to the
        host repository's programmes (OPEN_CUTS.md). Classical zeta unless a direction says otherwise.
Exact sources or dependencies: frontiers/records_ledger.md and frontiers/ledger.jsonl (LED ids; verifier-
        corrected values used); frontiers/research_programs.md (items 7-8 and critiques per area);
        connections/connections_register.md and connections.jsonl (CON ids; needs_correction proposals are
        used only in their corrected form); connections/repository_bridge.md and .jsonl (BRG ids);
        audits/verified_findings.md and audits/unresolved_findings.md (FND ids); audits/quasi_rh/DOSSIER.md
        (incl. Sec. 4, method limit); audits/claims_2026/CRIT23/DOSSIER.md; audits/claims_2026/SIEGEL/
        DOSSIER.md; proposals/independent_campaigns/C1..C5 (FINAL.md for C1 and C3; REPORT.md read together
        with SKEPTIC_REVIEW.md for C2, C4, C5, with downgraded statuses reported as downgraded);
        history/*.md; corpus/bibliography.jsonl (PAPER ids). Works absent from the corpus are cited by
        arXiv id and marked "not in corpus".
What was actually run: selective reading of the files above, with short python3 -I extractions of JSONL
        fields; one arithmetic cross-check script (scratchpad synth/checks.py, mpmath at 30 digits) that
        recomputed the constants quoted here: c*_lambda, lambda* = 0.5501939647, C_MT = 0.6725007037, the
        extraction table beta(n,1), the isolated-pair Jensen-heat predictions T^2/(4 delta^2), and the
        elementary bound of D-23 / AC-22. No proof was re-checked for this file, no certified computation
        was run, no Lean was built, and no source outside the archive was opened.
Smallest remaining gap: the three highest-ranked directions (D-01 kernel replay, D-02 human verification of
        Proposition 3.1 of the 11/12 paper, D-03 a version-of-record review of one Siegel-exclusion core)
        gate most QRH- and Siegel-conditional directions below. No direction in this file moves RH itself;
        the ones that come closest (D-07, D-14, D-16) are bounded by proved ceilings or by RH-equivalence.
```

## 0. Conventions

**Status labels** (archive methodology):

- THEOREM: refereed, classical, or a complete proof inside an Observatory campaign that its adjudicator or skeptic re-derived (the label then says which).
- CONDITIONAL: on the named hypothesis.
- UNREFEREED: human preprint without a version of record.
- AI-GENERATED UNREFEREED: the OpenAI manuscripts ("raw research data" per the release README).
- AI-DISCOVERED, HUMAN-VERIFIED, UNREFEREED: Alpoge-Furman.
- HEURISTIC, CONJECTURE, PROPOSITION-PROOF-SKETCH (PPS).
- OBSERVATORY-PROPOSED: first stated in an Observatory campaign, connection or this file; not reviewed outside the Observatory.
- NUMERICAL-RIGOROUS (Arb balls or exact integers) versus NUMERICAL-NONRIGOROUS (floating point, mpmath, rounded polynomials).

**Auditor disclosure.** The Observatory audits were produced by AI agents (Claude). The Alpoge-Furman proof was discovered by Claude, so the CRIT23 audit is not institutionally independent of it. Weight every "no error found" by its explicit witnesses and re-derivations, not by its authorship.

**Scores.**

- S (significance, 1-5): 5 changes the status of a 2026 headline claim or gives a first-of-its-kind theorem; 4 is a new theorem at an active frontier; 3 is a sharp lemma, a decisive negative result, or infrastructure; 2 is bookkeeping, a conditional consequence, or host hygiene; 1 is minor.
- T (tractability, 1-5): 5 means the procedure is fixed (weeks); 4 a clear plan (months); 3 one identified hard lemma; 2 a new idea needed at a known place; 1 a conceptual breakthrough needed.
- EV = S x T. Ties are broken by S.

**Route tags.** VERIFY, QRH-LIMIT, QRH-EXT, QRH-CONSEQ, SIEGEL, CRIT (critical-line proportions), GL2, POS (Weil, Li, Jensen positivity), DBN (de Bruijn-Newman), ARITH, FF (function fields), OPS (operators), OBSTR (countermodels and obstructions), ZDE, HOST. Origin tags: 2026, C1-C5, M1-M8 (discovery mechanisms).

## 1. Ranking at a glance

| Rank | ID | Direction | Route / origin | S | T | EV | Weakest load-bearing input |
|---|---|---|---|---|---|---|---|
| 1 | D-01 | Kernel replay of the formal 2026 statements | VERIFY / 2026 | 5 | 5 | 25 | building third-party Lean needs separate authorisation |
| 2 | D-02 | Human-checkable proof of the 11/12 half-plane | VERIFY / QRH | 5 | 4 | 20 | Patterson-Kubota transcription (via Dunn-Radziwill) not re-proved |
| 3 | D-03 | One Siegel-exclusion core to version-of-record standard | VERIFY / SIEGEL | 4 | 5 | 20 | no human referee yet |
| 4 | D-04 | A falsification handle for Proposition 3.1 | QRH-LIMIT / 2026 | 4 | 4 | 16 | detector step is heuristic [O] |
| 5 | D-05 | Cureton-Thorner and all-field QRH: provenance and replay | VERIFY / QRH-EXT | 4 | 4 | 16 | source not read by the Observatory |
| 6 | D-06 | Effective consequences of Siegel-zero exclusion | SIEGEL / 2026 | 4 | 4 | 16 | Kimura constant (Lean-claimed, unrefereed) |
| 7 | D-07 | Beyond the bandwidth-one ceiling for simple critical zeros | CRIT / 2026 | 4 | 4 | 16 | 0.6818 ceiling author-stated, not audited |
| 8 | D-08 | Mechanized countermodel pre-review filter | OBSTR / C2, C3 / HOST | 3 | 5 | 15 | hitting-set reading is a protocol heuristic |
| 9 | D-09 | Close the residual gaps of the 2/3 audit | VERIFY / CRIT | 3 | 5 | 15 | Knausgard branch-and-bound unreplayed |
| 10 | D-10 | Architecture floors of the quasi-RH method as theorems | QRH-LIMIT / M7 | 4 | 3 | 12 | floors are Observatory sketches [O] |
| 11 | D-11 | GL(2) distinct zeros through the rank-trace certificate | GL2 / M8 | 4 | 3 | 12 | GL(2) all-zeros pair-sum lemma unwritten |
| 12 | D-12 | GL(2) family averages through Petersson | GL2 / M8 | 4 | 3 | 12 | Kloosterman diagonal lemma unwritten |
| 13 | D-13 | The order-3 route | QRH-EXT / 2026 | 4 | 3 | 12 | no mu-removal identity for n = 3 |
| 14 | D-14 | RH-free 19/27 through the off-line pair defect | CRIT / M2 | 3 | 4 | 12 | proof sketch |
| 15 | D-15 | Partial-RH horizons for arithmetic criteria | ARITH / C1 / HOST | 3 | 4 | 12 | explicit error terms unwritten |
| 16 | D-16 | Certified Weil positivity on windows containing primes | POS / C4, C5 / HOST | 3 | 4 | 12 | Zhu Pos(0.8) unreplayed |
| 17 | D-17 | de Bruijn-Newman: explicit asymptotic theorem and checker | DBN / C1 | 3 | 4 | 12 | constants of Polymath Thm 1.5(i) |
| 18 | D-18 | Montgomery-Vaughan character sums under a half-plane | QRH-CONSEQ / M4 | 3 | 4 | 12 | verifier's sketch |
| 19 | D-19 | Quartic row mean square (J4): an OpenAI-independent 7/8 | QRH-EXT / M8 | 5 | 2 | 10 | no quartic duality partner known |
| 20 | D-20 | Conjecture G: CM elliptic curves with j = 0 | QRH-EXT / M8 | 5 | 2 | 10 | angular version of Prop 3.1 unverified |
| 21 | D-21 | Conditional consequences of a half-plane, as lemmas | QRH-CONSEQ / M4 | 2 | 5 | 10 | unrefereed half-plane |
| 22 | D-22 | Host: corrected Euler products and smooth numbers | HOST / M1, M3 | 2 | 5 | 10 | unrefereed half-plane for part (b) |
| 23 | D-23 | Function fields: finite-window theorem without RH | FF / C5 | 2 | 5 | 10 | window corollary is a PPS |
| 24 | D-24 | Extending and limiting the Siegel-exclusion method | SIEGEL | 3 | 3 | 9 | larger-kernel zero estimate unchecked |
| 25 | D-25 | Persistence lemma for the de Bruijn-Newman converse | DBN / C1 / M2 | 3 | 3 | 9 | far-field estimate |
| 26 | D-26 | The Beurling frontier for RH and quasi-RH | OBSTR / M7 / C2 | 3 | 3 | 9 | constructions stop at alpha < 2/3 |
| 27 | D-27 | Host: principal-member transfer through trivializing rows | HOST / QRH | 3 | 3 | 9 | design rule is heuristic |
| 28 | D-28 | Semilocal positivity at lambda^2 = 3 as a mechanism | OPS / C5 | 4 | 2 | 8 | identification of ker u(F)_22 |
| 29 | D-29 | Jensen-heat bridge with error control | POS / C1, C2 | 2 | 4 | 8 | C1-J2 is heuristic |
| 30 | D-30 | Host: Ingham-kernel lattice searches and firewalls | HOST / ARITH | 2 | 4 | 8 | firewall value only |
| 31 | D-31 | Host: fixed-order xi-Pick positivity | HOST | 2 | 4 | 8 | Sra 2026 unrefereed |
| 32 | D-32 | de Branges zero condition: failures and rate | C3 | 2 | 3 | 6 | control of S(t) at zeros |
| 33 | D-33 | Weil-window detection theorems | C4 / POS | 2 | 3 | 6 | full-saturation construction |
| 34 | D-34 | Li coefficients beyond T^2 | C1 / POS | 2 | 3 | 6 | adversarial phases |
| 35 | D-35 | Riemann-Roch on the square of the scaling site | FF / OPS / C5 | 5 | 1 | 5 | no definition of H^0 exists |
| 36 | D-36 | Zero density at the Guth-Maynard bottleneck | ZDE | 5 | 1 | 5 | needs a new large-values idea |

## 2. The directions

### Tier A (EV at least 15)

#### D-01 - Kernel replay of the formal 2026 statements
*VERIFY / 2026 (QRH, Siegel, CRIT). S 5, T 5, EV 25.*

**Statement to decide.** Does the Lean 4 kernel (toolchain v4.34.1, Mathlib d13f23b7; permitted axioms propext, Quot.sound, Classical.choice) accept OpenAI's comparator challenges?

- QuasiRiemannHypothesis: `riemannZeta s ≠ 0` for 7/8 < Re s.
- DirichletSevenEighths: for every q, every χ : DirichletCharacter ℂ q, 7/8 < Re s and ¬(χ = 1 ∧ s = 1) imply `LFunction χ s ≠ 0`.
- HeckeSevenEighths, together with a fidelity lemma that nobody has proved yet (DOSSIER §1.3): for Re s > 1, the challenge's custom `LFunction` equals (1/6) Σ_{z ∈ O∖0} χ(z) N(z)^{-s}, with O = Z[ω].
- SiegelZeros: there is c > 0 such that for all q ≥ 3, all primitive real nonprincipal χ and all β ∈ (0,1), L(β,χ) = 0 implies c ≤ (1 − β) log q.

The same procedure applies to the two-thirds formalizations:

- Alpoge-Furman: anthropics/zeta-23-lean v1.0, reported hypothesis-free.
- Lamzouri: AxiomProver; assumes BGSTB24 Lemma 5 and Riemann-von Mangoldt as hypotheses.
- Knausgard: three extra axioms recording search-program outputs.
- Kimura: `B4.Chi8.zero_gap_all`, c = 5.811·10⁻⁴.

**Inputs.**

- OpenAI 7/8 (PAPER-0528): AI-generated, unrefereed, not audited; Lean claimed.
- OpenAI Siegel (PAPER-0529): AI-generated, unrefereed; audited with no error found (FND-0010); static scan of the Lean files 31/31.
- Alpoge-Furman (PAPER-0486): AI-discovered, human-verified, unrefereed.
- Knausgard (PAPER-0166): AI-assisted, unrefereed.

**Archive support.**

- quasi_rh DOSSIER §1.3 and §5.2; audits/lean_replay/README.md; audits/unresolved_findings.md.
- SIEGEL DOSSIER §8.2 (item U4); CRIT23 DOSSIER §1, §8.2 (item F5).
- LED-ZFR-1, LED-LFUN-3, LED-LFUN-6, LED-CRIT-1, LED-CRIT-3.
- research_programs ZFR §8(1), LFUN §8 step 1, DBN §8.

**What success would and would not establish.**

- Passing the first two challenges establishes the zeta and Dirichlet 7/8 statements (hence 11/12) relative to the Lean kernel and Mathlib's definitions, independently of how readable either paper is.
- It would not certify paper2's argument (D-02), and it does not touch Re s = 1/2.
- A secondary source reports a caution that some OpenAI Lean statements prove weaker results than the papers claim (DOSSIER §1.4, [S]). The fidelity review is therefore part of the task.
- A failed build is a fact about the build, not a refutation.

**Next steps.**

1. Obtain explicit authorisation and an isolated environment. The build runs third-party code, which this session's policy blocked.
2. Pin the toolchain and manifest, and verify the patches the lakefile applies from lean/patches/.
3. Run `lake build`, then comparator with lean4export, plus an independent kernel (nanoda, which the configs disable).
4. Run `#print axioms` on every challenge theorem and hash every artifact.
5. Check statement fidelity by human review, including the Hecke fidelity lemma.
6. For Siegel, also read the 642 lines of the chain-A assembly that no reported external build covers.
7. Settle CRIT23 item F5 (zeta-23-lean v1.0 versus formal-math fbdc36b).

**Unlocks.** D-18, D-21 and D-22(b), the conditional bound Λ ≤ 0.13963 (LED-DBN-15), and CON-0018/0019. All of these would move from "conditional on an unverified manuscript" to "conditional on a kernel-checked statement".

#### D-02 - Human-checkable proof of the 11/12 half-plane
*VERIFY / QRH. S 5, T 4, EV 20.*

**Statement.** This is Proposition 3.1 of paper2 (PAPER-0161; AI-generated, human-edited, unrefereed). Let K = Q(√−3), ν a finite-order Hecke character, W smooth with compact support, ε > 0 and 0 < ϑ ≤ 1/10 (the restriction ϑ ≤ 1/10 is never used). Then

Σ_{0<N(u)≤D^{1+ϑ}} |Σ_{(𝔫,S)=1} μ(𝔫)ν(𝔫)(u/𝔫)_6 W(N𝔫/D)|² ≪ D^{2+ϑ+ε}.

The deduction to Theorem 1.1 has three ingredients:

- the one-page extraction (l.694-724), averaging over rows u = p⁶, where χ_𝔫(p⁶) = 1_{𝔭∤𝔫};
- base change, L_K(s, χ∘N) = L(s,χ)L(s,χχ₋₃);
- the resulting conclusion: no finite-order Hecke L over K, hence no Dirichlet L including ζ, has a zero in Re s > 11/12.

**Inputs.**

- Observatory Level-2 audit of every line from l.206 to l.3988: 0 verified errors, 0 suspected gaps, about 35 presentation items (FND-0009; an AI-agent audit).
- Imported and not re-proved: Patterson's coefficient formula, the cusp table and the automorphy of the cubic theta function on Γ₂ with multiplier (c/a)₃, all as transcribed in Dunn-Radziwill (PAPER-0960) §5.1 and App. A. These were corroborated numerically only.
- Also imported and not re-proved: Goldmakher-Louvel Thm 1.1, and the constants of Lemma B.2.
- Load-bearing points:
  - Prop. 6.2 plus Lemma 6.3 in the form used by Lemma 6.6: the k₀-dependence must be exactly χ_{k₀}³, with weight N(k₀)² and a unimodular scalar.
  - The sign of the Kubota multiplier. It was checked to 2·10⁻¹³; the conjugate multiplier is off by |1 − ω|.

**Archive support.** DOSSIER §1.2, §5.1, §5.3; FND-0009; LED-ZFR-2; research_programs ZFR §7-8 and LFUN §7(i).

**Next steps,** in the order of risk given in DOSSIER §5.3:

1. Check Dunn-Radziwill's transcription against Patterson (1977) itself.
2. Check the Goldmakher-Louvel Def. 1 hypotheses for x ↦ (x/k)₂κ_λ(x)^{e_k}.
3. Check the multiplier case analysis (l.3175-3196) and Lemma 6.3.
4. Check Lemma B.2.
5. Write and pin a short human proof with minimal imports. The press reports 7-13 page private write-ups and a half-page sketch [S].
6. Run the adversarial round the dossier lists as missing; no adversarial/ folder exists.

The gating resource is human expert time.

**Stop rule.** A located gap in steps 1-3 is reported with an explicit witness (methodology §6). The deduction from Prop. 3.1 to Thm 1.1 is elementary and was audited (audit_S3).

#### D-03 - One Siegel-exclusion core to version-of-record standard
*VERIFY / SIEGEL / 2026. S 4, T 5, EV 20.*

**Statement.** There is an absolute c > 0 such that every real zero β ∈ (0,1) of every primitive real nonprincipal L(s,χ) of conductor q ≥ 3 satisfies (1 − β) log q ≥ c.

- Guo (PAPER-0165) gives c = 1/100 for all q ≥ 3 (1/64 in App. A), with no computation.
- Banks (PAPER-0160) gives 3.0·10⁻³ for q ≥ 10¹⁰. His all-q constant uses Lu-Zaman-Zhao (PAPER-0855), a refereed computation (Math. Comp.).
- The shortest core is Guo's Prop. 3.1, which is unconditional: S₋(x,χ) = Σ_{p≤x, χ(p)=−1} log p/p ≤ (11/20) log x + (29/60) log q + 6 for x ≥ 2.

**Inputs.**

- Four structurally different unrefereed proofs: OpenAI's is AI-generated; Banks, Kerr (PAPER-0164) and Guo are human-signed, AI-assisted, and were written after reading OpenAI's.
- The Observatory found no verified error and no suspected gap in any of them (FND-0010). Kerr has two harmless missing hypotheses: q = 8 is excluded, and Masser's basis condition is satisfied but unstated.
- The statement is also a one-line corollary of the claimed half-planes: β ≤ 7/8 gives (1 − β) log q ≥ (log 3)/8 = 0.1373 [O]. None of the four proofs uses QRH.

**Archive support.** SIEGEL DOSSIER §0-§4 and §8.1-8.3; FND-0010; LED-LFUN-6, LED-LFUN-8, LED-VERIF-18.

**Next steps.**

1. Get an independent human review of one core (Guo Prop. 3.1 with Lemmas 3.2-3.3, or OpenAI Lemma 3 plus Lemma 7) against a SHA-pinned source.
2. Audit the κ → 1/2 variants (Green, PAPER-0547 / hexagon:2610.00311v2; van Dijk; Pescador; Barreto) before relying on the floor κ = 1/2 attained (§7.1).
3. Track the communal write-up Green announced.

The Kimura and OpenAI Lean replays belong to D-01.

#### D-04 - A falsification handle for Proposition 3.1
*QRH-LIMIT / 2026. S 4, T 4, EV 16.*

**Statement** (HEURISTIC [O], DOSSIER §2.5; to be turned into a theorem, see AC-01).

- Proposition 3.1 is "GRH on average" for the sextic twist family at rows at or just above the diagonal.
- Heuristically it has density-hypothesis strength. Suppose L(s, νχ_·(u₀)) has a zero with β ≥ σ that a fixed detector sees at length D ≍ N(u₀). Then the roughly (H/N(u₀))^{1/6} rows u₀a⁶ all carry sums of size D^σ, so #{u₀ ~ U : such a zero} ≲ U^{2−2σ+ε}.
- This exceeds generic large-sieve zero density. de Faveri (arXiv:2610.04045, not in corpus) has Cor. 1.5 exponent ≈ 0.73 at σ = 3/4, against 0.5.
- That is not a contradiction, since the coefficients are special. But it shows that all the risk sits in Prop. 3.1.

**Next steps.**

1. Write the detector step and state "Prop. 3.1 ⇒ (count)" as a theorem.
2. Compute Σ_{N(u)≤H} |A_u(D)|² in exact Z[ω] arithmetic for D ≤ 4000 and H = D^{1.1}, with the archive harness (audits/quasi_rh/architecture_checks, zomega utilities).
   - Systematic power growth beyond D^{2+ϑ} would flag Prop. 3.1 for expert review.
   - Consistency at these sizes carries no evidential weight.

**Archive support.** DOSSIER §2.5 and §5.5(d); audit_S3 §4, §7.

#### D-05 - Cureton-Thorner and all-field QRH: provenance and replay
*VERIFY / QRH-EXT. S 4, T 4, EV 16.*

**Statement to establish.** What exactly does Cureton-Thorner prove? The paper is hexagon:2610.00200; it is not in the corpus and the Observatory has not read it.

- Version 1 claims a zero-free region Re s > 1 − 1/6000.
- Version 2 (14 Oct 2026) claims that ζ_K and every finite-order Hecke L over every number field K have no zeros in Re s > 31/32, via K(ζ₁₂) and abelian descent. A Lean formalization via AxiomProver is claimed (CON-0026, corrected).
- For comparison, Liu (PAPER-0157, unrefereed) claims B♭ = 0.874886647… for every number field. That claim is conditional on the 7/8 inputs and on another unreviewed OpenAI preprint.

**Why it matters.** A kernel-checked Dedekind QRH that is independent of the OpenAI manuscripts would give power-saving Chebotarev for every Galois extension L/Q. The Q(√−3) claims cover only those L with LK/K abelian (DOSSIER §3, last row).

**Next steps.**

1. Download the PDF and the Lean development; record the formal statement and the `#print axioms` output.
2. Decide whether Cureton-Thorner depends on the OpenAI inputs. CON-0007's correction treats it as an independent input, which is unverified.
3. Tag each consumer by version: FSW (arXiv:2610.18491) cites v1; BV (2611.09031), Cao et al., Shunia, Kimura and Liu cite v2.
4. Update history Sec. 5. Its "unlocated dependency" is stale, since the DOSSIER already locates the paper.

**Archive support.** CON-0026, CON-0007; DOSSIER §1.5 and §3; LED-ZFR-3.

#### D-06 - Effective consequences of Siegel-zero exclusion
*SIEGEL / 2026. S 4, T 4, EV 16.*

**(a) Exponent-2 class groups** (CON-0025, sound_and_useful, corrected form; CONDITIONAL).

- Hypotheses: Kimura's Thm 1 constant 5.811·10⁻⁴ and his Prop. 9 (arXiv:2610.21511, not in corpus; unrefereed; Lean-claimed, not replayed), and EKN Thm 1 (a refereed computation).
- Conclusion: the imaginary quadratic fields whose class group has exponent at most 2 are exactly the 65 known ones, the largest being |D| = 5460. With Grube's reduction (Kani 2011, Thm 6), Euler's 65 idoneal numbers are complete.
- Neither QRH nor EKN's c = 1/4 hypothesis is needed.
- Thresholds: Kimura's constant alone excludes exponent ≤ 2 for |D| ≥ 6.60·10¹⁹, below EKN's 3.1·10²⁰. Guo's 1/100 gives 2.14·10¹⁵ and Banks's 3·10⁻³ gives 1.15·10¹⁷.

**(b) Effective class numbers** (auditor's derivation, SIEGEL §5.3; CONDITIONAL on Guo). L(1,χ) log q ≥ 0.0076709 for q ≥ 10, hence h(D) ≥ 0.00244 √|D|/log|D| for D < −4. This is effective, against Goldfeld-Gross-Zagier's ≫ log|D|.

**(c) Not implied** (negative knowledge).

- EKN's E | 8 list: it needs zero-freeness on [1 − 1/(4 log|D|), 1), and the 2026 constants (all at most 1/100) do not give that (CON-0039 correction).
- Any improvement of Linnik's L = 5: the binding cases have no exceptional zero (CON-0027).
- GRH-strength L(1,χ) ≫ 1/log log q: that needs a half-plane.

**(d) Vacuity bookkeeping** (CON-0034, sound_but_known). Theorems that assume exceptional zeros become vacuous, not false:

- Heath-Brown on twin primes (PAPER-0685);
- the Conrey-Iwaniec corollaries (PAPER-0573);
- Chowla under a Siegel zero (PAPER-0854);
- Bondarenko-Heap, but only if their E₀ exceeds 1/c (CON-0027).

**(e) Brauer-Siegel.** Effective Brauer-Siegel for normal towers via Stark (recalled, not re-derived; SIEGEL §5.7).

**Next steps.**

1. Replay the exponent-2 scan independently (PARI qfbclassno plus a second enumeration).
2. Check the Lean statement of Kimura's Prop. 9.
3. Write the order-level (−4n) step from Kani §2.3.
4. Grep theorems.jsonl `conditional_on` for "Siegel" and "exceptional" and tag the hits.
5. Make the constant in Conrey-Iwaniec Thm 2.1 explicit (CON-0034).

#### D-07 - Beyond the bandwidth-one ceiling for simple critical zeros
*CRIT / 2026 / M3, M7. S 4, T 4, EV 16.*

**Statements.**

- **The 2026 bounds.** AI-discovered, human-verified, unrefereed; the CRIT23 audit found no error affecting a stated result, and one proof step (FND-0004) was repaired.
  - liminf N₀ˢ(T)/N(T) ≥ 2/3 with the flat window, and ≥ C_MT = 3/2 − cot(1/√2)/√2 = 0.6725007…; distinct zeros ≥ 5/6 and ≥ 0.8362504… (Alpoge-Furman, PAPER-0486; Lamzouri, PAPER-0533).
  - Lamzouri's analytic input is BGSTB24 Lemma 5 (PAPER-0053, refereed). The proof of BGST Thm 1 needed a correction (arXiv:2501.14545v3 §3); Lemma 5 is stated to survive (ledger CRIT verifier critique).
  - Knausgard's 0.6735382 and 0.8390046 (PAPER-0166) additionally rest on three unreplayed searches.
- **Ceilings** (author-stated, not audited). Every bandwidth-one two-moment certificate gives at most 0.6818287 (AF §7.2). Knausgard's frames reach at most 0.67357 (LED-CRIT-10).
- **CONDITIONAL** (CRIT23 §7.3, check (D)). If the all-zeros form factor equalled min(|α|,1) on [−Δ,Δ], the flat-window certificate would give N₀ˢ/N ≥ 1 − 1/(3Δ²) for Δ ≥ 1, e.g. 0.852 at Δ = 3/2. Under HL*(4), the Chebyshev-Markov-Stieltjes bound gives 13/18 (CRIT23 §7.4).
- **Decision question** (research_programs CRIT §8). Does a certificate that also uses a third trace moment at reduced bandwidth X = T^{2/3−ε} (the Rudnick-Sarnak range) have a certified ceiling above 0.6818 + 10⁻³?
  - AF §7.2(e) say informally that higher moments add nothing at X ≍ T.
  - AF Rem. 6.1 shows that reducing the bandwidth lowers the second-moment constant.
  - The ledger verifier expects no gain. Hence the pessimistic conjecture AC-12.
- **ξ′ sub-question** (CON-0015, sound_and_useful; NUMERICAL-NONRIGOROUS). For zeros of ξ′ the window class is exhausted at 0.868641 ± 2·10⁻⁶, below Wu's 0.86957 (on the line, simplicity not asserted). Run the ξ′ ceiling LP (AC-13).
- **Structural limit** (CON-0030, corrected; a formalisation of folklore). Density-currency methods saturate at "100% critical and simple" and cannot exclude any o(T) set of off-line zeros. Even 100% would not be RH (CRIT23 §7.5).

**Next steps.**

1. Solve an interval-enclosed LP/SDP over periodic configurations with the on/off-line partition plus a third moment at bandwidth 2/3. Stop if the gain is below 10⁻³.
2. If not stopped, attempt an RH-free triple sum over complex zeros with restricted support, in BGST style.
3. Seek unconditional upper information on F(α) averaged over [1, 1 + δ] (CRIT23 §8.7(a)).
4. Decide whether an inertia-compatible certificate can use F ≥ 0 off [−1,1] (CRIT23 §8.7(b)).

**Archive support.** CRIT23 DOSSIER §5-§8; LED-CRIT-1/2/3/10/14; LED-SPACING-18; CON-0015, CON-0030.

#### D-08 - Mechanized countermodel pre-review filter
*OBSTR / C2, C3 / HOST. S 3, T 5, EV 15.*

**Statement.** Meta-lemma C2-24 (THEOREM, elementary): suppose W satisfies predicates P₁, …, P_k with the same normalisation and quantifiers as for ζ, and W has a zero off its symmetry line. Then "P₁ ∧ … ∧ P_k ⇒ RH_W" is false, and any proof whose RH-deciding step uses only P₁, …, P_k is invalid.

Certified witnesses in the archive:

- **Davenport-Heilbronn** (PAPER-0417). Five off-line zeros with t ≤ 300. The list is complete by a rigorous argument-principle count, 214 = 204 + 2·5 (C2-03, C2 skeptic F6). The lowest is 0.80851718… + 85.69934848…i (LED-LFUN-15).
- **The Epstein zeta function of x² + 5y².**
  - It has 35 off-line zeros with t ≤ 200, complete by the count 253 = 183 + 2·35; the lowest is at height 15.668.
  - It has zeros with Re s > 1 already near t ≈ 1193.946 (C2 skeptic F4), as well as near 3.6·10⁶.
- **ζ₁₉**, with a zero of real part 1.0010955… at t ≈ 600884.2.
- **Synthetic and heat-flow models**: the synthetic ξ̃ with an injected quadruple; H_t for t < 0 (Rodgers-Tao, PAPER-0036); the continuous Beurling toy C2-21.
- **The skeptic's F_c(s) = ζ(s)(1 + c·2^{-s} + 2·4^{-s})** (C2 skeptic F1; folklore for the extended Selberg class).
  - It is a Dirichlet series over N with an Euler product over the rational primes and a self-dual functional equation of conductor 4.
  - It is RH-false, with zeros on Re s = log₂ a and Re s = 1 − log₂ a.
  - Only the Selberg-class local condition (θ < 1/2; here equivalently Λ_F ≥ 0) excludes it.

**Corrected protocol status.** The hitting-set corollary C2-31 is downgraded to a protocol heuristic. The claim "a valid proof must use the Euler product" is overstated; the blind spot is the full Selberg class.

**Deliverable.**

- A harness that runs each step of a candidate argument, human or AI, on parameterised families containing these members (C3 §9.8; abandoned_approaches §20, items 1-5 and 9).
- Theorem-backed benchmarks for host counterfeit rejection (BRG-FAMILIES-T8, -O8, -O2):
  - Saias-Weingartner;
  - Kaczorowski-Perelli (the S₁ classification; S♯_d is empty for 1 < d < 2);
  - Bombieri-Hejhal (PAPER-0271: 100% of zeros on the line is compatible with off-line zeros).

**Next steps.**

1. Add member M10 (F_c) to experiments/results/C2-countermodel-zoo/property_matrix.csv.
2. Relabel C2-17 and C2-28 as CONDITIONAL (skeptic F2).
3. Replace the C2-16 table with the skeptic's recomputation (F3).
4. Apply the harness to arXiv:0807.0090 v5-v10, a live unrefereed claim (C3 gap (a)).

**Archive support.** C2 REPORT and SKEPTIC_REVIEW; C3 FINAL §5-§6; FND-0014; the C2-07 refutation of Liu-Wu (arXiv:2503.24275), which has an independent winding-number witness.

#### D-09 - Close the residual gaps of the two-thirds audit
*VERIFY / CRIT. S 3, T 5, EV 15.*

**Items.**

1. Re-derive the P1-F1 repair independently: tr G̃ = N(I) + O(X^{1/2}L) = N(I′) + O(√T log T). Then send AF a consolidated erratum covering P1-F1, P1-F2, P2-F1, P2-F2, P2-F3, F1, F3 and F7 (FND-0004).
2. Replay Knausgard's Props 3.3, 5.3 and 6.3 by an Arb branch-and-bound written from the statements. This is the single gap between the audited 0.6725007/0.8362504 and Knausgard's 0.6735382/0.8390046.
3. Write out P2-N1 line by line: the restricted support supp Q ⊂ [−1 + 2ε₀, 1 − 2ε₀] avoids the Korobov-Vinogradov/[GM87] endpoint. Alternatively, re-derive BGSTB24 Lemma 4 and take the correction in arXiv:2501.14545v3 §3 into account.
4. Settle F2: the pre-2026 distinct-zero baseline (Ki-Lee 2012, Thm 5).
5. Effective version: an explicit T₀ with N₀ˢ ≥ 0.6N on (T, 2T]. Item P2-N2 suggests T₀ is very large.
6. Inspect the unverified Yang-Yang report (0.7962 and 0.8981 from higher moments; item D-2), which is in tension with AF §7.2(e).

**Archive support.** CRIT23 DOSSIER §3-§4 and §8; FND-0004; LED-CRIT-3, LED-CRIT-20. An independent human second review is the point of this direction (see the auditor disclosure in §0).

### Tier B (EV from 10 to 14)

#### D-10 - Architecture floors of the quasi-RH method as theorems
*QRH-LIMIT / 2026 / M7. S 4, T 3, EV 12.*

**(a) Extraction lemma** (paper2 l.694-724, [P] for n = 6; [O] in general; checked symbolically in DOSSIER §4.1).

- Statement: if the full-row mean square Σ_{0<N(u)≤D^h} |A_u(D)|² ≪ D^{1+h+ε} holds for an order-n residue-symbol family, then β ≤ β(n,h) = 1/2 + h(n − 1)/(2n).
- At h = 1 this gives 3/4, 5/6, 7/8 and 11/12 for n = 2, 3, 4 and 6.
- For h < 1 the duality returns Σ|A_u|² ≍ DH + D², which is the large-sieve barrier. In this architecture h ≥ 1 is forced [O].

**(b) Abstract form** (CON-0031 corrected to a heuristic; CON-0009 restated).

- Setting: a family of H completely multiplicative twists with H^r trivial members. The expected conclusion is β ≤ 1/2 + (h/2)(1 − r).
- Target: prove this as a lemma, with Bettin-Gonek (r = 0) and paper2 (r = 1/n) as instances.
- To become an obstruction, it needs either a countermodel family or a proof that r ≤ 1/n is forced.

**(c) The 7/8 comparison system** [O].

- B(ℓ) = 11/12 − ℓ/4 with ℓ < 1 − |b|, so B > 2/3 whatever the nonprincipal estimates are.
- Liu's "optimality" theorems (B_new = 0.874957…, Thm 34.4; B♭ = 0.874886647…, Thm 14.13) give the optimum of a fixed semi-algebraic system. They are not upper bounds on what the ideas can give.
- Going below about 0.8745 needs one of three inputs:
  - (C3a) a counting estimate for the critical class (δ_c, x = 1/2) with exponent below 2/3;
  - (C3b) the plain fourth moment at κ < 13/18;
  - (C3c) a new direct estimate.

**(d) Sharper sieves** (DOSSIER §5.5(b)). de Faveri's sharp sextic sieve widens only the margins of Part I of the 7/8 paper: the r = 1 branch becomes max(1 − δ/2, 7/6 − δ). Decide whether it, or the Dunn-Radziwill / de Faveri-Dunn-Hoffstein structure, enters Part II.

**(e) Generic coefficients cannot work** (DOSSIER §4.3, item C4). With Θ₆(A,B) ≍ A + B + A^{5/6}B^{1/3} + A^{1/3}B^{5/6}, the extraction gives only the trivial bound.

**Status.** These are statements about architectures, not about ζ. All QRH inputs are unrefereed. DOSSIER §4.3 (C5) records that every input reaching 1/2 is of GRH strength for a family.

**Archive support.** DOSSIER §4; CON-0009, CON-0014, CON-0031; LED-ZFR-3.

#### D-11 - GL(2) distinct zeros through the rank-trace certificate at bandwidth 1/2
*GL2 / M8 / extension of the 2/3 method. S 4, T 3, EV 12.*

**Statement** (CON-0035 and CON-0011, corrected; CONDITIONAL).

- Setting: f a primitive holomorphic or Maass newform. Self-duality is not needed, since ρ ↔ 1 − ρ̄ holds for every primitive L(s,f).
- Assume **Lemma GL2-PC**: for r real, even and supported in [−1/2 + ε, 1/2 − ε] in GUE units, the pair sum over all zeros of L(s,f) in (T, 2T] equals N(f;T,2T)(r(0) + 2∫₀^{1/2} α r(α) dα + o(1)), unconditionally.
- Conclusion: liminf N_d(f;T,2T)/N(f;T,2T) ≥ 1/R*_{1/2} = c*_{1/2} = 0.461688….
  - Here c*_λ = √2 tan(λ/√2)/(1 + (λ/√2) tan(λ/√2)), a closed form due to Hua-Yang (arXiv:2609.27808, not in corpus), valid for λ ≤ 1.
  - The proof route is rank(G̃) ≥ (tr G̃)²/‖G̃‖²_HS (AF Rem. 3.3), which beats (3 − R)/2 = 0.417018 at λ = 1/2.

**Barrier** (THEOREM for the window class; elementary).

- The simple-on-line certificate 2 − R*_λ is positive iff λ > λ* = 0.5501939647 (the flat window needs 3 − √6). Bandwidth-1/2 data alone therefore yield no simple critical zeros.
- A doubled-lattice configuration with 0% simple zeros is consistent with bandwidth-1/2 data.
- For degree d the distinct bound 1/R*_{1/d} is positive for every d (0.3214 for d = 3).

**Status and prior art.**

- Lemma GL2-PC is plausible (Montgomery-Vaughan plus the Rankin-Selberg prime number theorem) but unwritten.
- No positive proportion of simple zeros is known for an individual GL(2) L-function. Bernard proves 2.97% on the line; LED-CRIT-19 records ≥ 6.96% critical for each GL(2) cusp form.

**Next steps.**

1. Port AF §§2-5 and BGSTB24 Lemma 5 to L(s,f): gamma factor Γ_ℂ(s + (k−1)/2), Gabor compression at density (1/2π) log(NT²), Λ_f, and the λ_f(p²) − 1 terms.
2. Check whether Murty-Perelli's GRH pair correlation already gives the conditional version.
3. Test the normalisation on LMFDB zeros of Δ or of 11a (AC-09).

#### D-12 - GL(2) family averages through Petersson orthogonality
*GL2 / M8. S 4, T 3, EV 12.*

**Statement** (CON-0036 and CON-0012, corrected; an expected theorem whose proof is unwritten).

- Setting: fix k ≥ 2; N prime → ∞; T polylogarithmic in N; harmonic weights ω_f on H_k*(N).
- **Diagonal Lemma**: for X ≤ N^{1−ε}, Σ_f ω_f |Σ_{p≤X} a_p λ_f(p)|² = (1 + O((X/N)^{k−1}N^ε)) Σ|a_p|². The proof route is to open the Kloosterman sums and apply the additive large sieve; Bessel decay alone does not suffice.
- Further inputs: a family zero-density estimate (Kowalski-Michel), an averaged counting estimate, and an exterior-tail bound.
- Conclusion: the per-form inertia certificate is linear in tr A and tr A², so it averages, giving Σω_f N₀ˢ(f)/Σω_f N(f) ≥ 0.6725 − o(1) and the distinct-zero analogue ≥ 0.8363 − o(1).
- Fallback with the Weil bound only (bandwidth 1 − 1/(2k)): for k = 2 this gives 0.4191 and 0.7095. Recomputed here: 2 − R*_{3/4} = 0.41908 and (3 − R*_{3/4})/2 = 0.70954.

**Scope and prior art.**

- These are family averages; by D-11's barrier, no statement about simple zeros of an individual member follows.
- Comparable family results: Hua-Yang for the Dirichlet family (arXiv:2608.16034, not in corpus), and Conrey-Iwaniec-Soundararajan (Crelle 681, Thm 3), which gives ≥ 7/20 simple on-line zeros on average for a different family, GL(2) twists by Dirichlet characters (ledger CRIT verifier note).

#### D-13 - The order-3 route
*QRH-EXT / 2026. S 4, T 3, EV 12.*

**Statement** (DOSSIER §4.3, item C2 with n = 3; a CONDITIONAL implication [O]). Over K, the bound Σ_{0<N(u)≤D^{1+ϑ}} |Σ μ(𝔫)ν(𝔫)(u/𝔫)₃ W(N𝔫/D)|² ≪ D^{2+ϑ+ε} would give zero-freeness in Re s > 5/6.

**Obstruction.**

- The Poisson dual coefficient is μ times a cubic Gauss sum, so it keeps μ.
- The Dunn-Radziwill bias (PAPER-0960) shows that untwisted Gauss-sum averages need not cancel.
- What is needed is square-root cancellation for μ-weighted cubic Gauss sums with an angular twist: a Patterson-type statement for μ·g̃.

**Cheap test** (CON-0014, next step).

- Compute the Poisson-in-u dual coefficients of the cubic family.
- Test whether μ(𝔫)g̃(𝔫) is, or correlates with, a Patterson theta coefficient over primary 𝔫 with N(𝔫) ≤ 10⁶, using the zomega utilities.
- If no theta structure appears, r = 6 is the smallest admissible order and 11/12 is the template's ceiling (design rule, D-27).

#### D-14 - RH-free 19/27 through the off-line pair defect
*CRIT / M2. S 3, T 4, EV 12.*

**Statement** (CON-0006, corrected).

- **(a) Unconditional inequality**: N*(T) ≥ |S₁|²/(S₂ + D/2). Here S₁ and S₂ are the Conrey-Ghosh-Gonek / Bui-Heath-Brown discrete moments and D is the off-line pair defect.
- **(c) CONDITIONAL theorem** (proof sketch; "provable now"). Suppose that for all large T every zero with T < γ ≤ 2T satisfies |β − 1/2| ≤ η(T)/(log T)^{3/2}, with η(T) → 0. Then liminf N*(T)/N(T) ≥ 19/27, counting simple zeros anywhere.
- **Thresholds**: writing D ≤ ηTL³, the values η < 0.01315, η < 0.01074 and η < 0.0091 beat 0.6725, 0.67800919 and 0.6818 respectively.
- **Comparator**: the right one is Knausgard's simple-anywhere value 0.67800919 (unrefereed, computer-assisted), not AF's simple-and-on-the-line value.

**Inputs.** BHB (PAPER-0070), BCHB (PAPER-0453) and CGG (PAPER-0049) are refereed. The gap to BGST's fixed thin box (b = 0.3185 for 2/3) is wider than "b → 0".

**Next steps.**

1. Write a referee-ready note.
2. Check that BHB's error terms O(TL^{2+ε}) do not interact with the defect.
3. Compute the CGG constant at mollifier length θ < 1/8, where the twisted fourth moment is available.

#### D-15 - Partial-RH implication horizons for arithmetic criteria
*ARITH / C1 / M1 / HOST (Robin). S 3, T 4, EV 12.*

**(a) Nicolas implication theorem** (PROPOSITION-PROOF-SKETCH, C1-D3).

- Target statement: RH(T) implies Nicolas' inequality N_k/φ(N_k) > e^γ log log N_k for all p_k ≤ X(T).
- Leading order: X(T) ≈ ((2 − β)πT/(log(T/2π) + 1))², about 4.36·10²³ at T₀, with β = 2 + γ − log 4π.
- Any rigorous X(T₀) ≥ 3.0·10¹³ would make Morrill-Platt Thm 13 (Robin's inequality up to 10^(10^13.11485); LED-ARITH-1, PAPER-0590) a corollary of RH(T₀) (PAPER-0001).
- No such explicit theorem exists yet (C1 FINAL, smallest gap (b)).

**(b) Robin's range** (CON-0003, corrected; pre-proof estimates, ±30%). With the Platt-Trudgian zero-sum tail and Dusart's |θ − x| ≤ 1.405·10⁻¹⁰x:

- unconditionally, Robin's inequality should hold up to x ~ 4-5·10²², i.e. n ≤ 10^(10^22.3);
- under H_θ, up to x ≤ (0.62/S_H)^{1/(θ − 1/2)}: about 1.5·10³⁰ for 7/8 and 1.5·10²⁷ for 11/12.

**(c) Nicolas primorials** (CON-0002, corrected): unconditionally for p_k ≲ 3·10²³; c(N_k) > 0 up to about 3·10³¹ under H_{7/8}.

**(d) Prime-counting horizon** (IMPORTED, Johnston, PAPER-0917). RH(T₀) implies the four Schoenfeld bounds for x ≤ 1.10·10²⁶ (C1-D1, LED-ARITH-17).

**(e) t-free Robin** (LED-ARITH-2, verifier critique).

- 22-free looks within reach using Büthe's 2018 computed bounds, 0.05√x < x − θ(x) ≤ 1.95√x on [1423, 10¹⁹].
- The perfect-information ceiling is t ≈ 25-26.
- In the same pass, repair the Dusart 2018 dependency chain (LED-ARITH-19).

**Host relevance.** OPEN_CUTS §2; BRG-ROBIN-T1, -T3, -O4. The bridge's recommended action is CA enumeration plus Robin's interpolation lemma, with the repository's directed enclosures.

**Next steps.** Write an explicit bound for the remainder R(x) in the colossally abundant inequality from x₀ = 3·10¹³, in directed interval arithmetic, together with the unconditional tail of ψ − θ for t > B².

#### D-16 - Certified Weil positivity on windows containing primes
*POS / C4, C5 / HOST (operators). S 3, T 4, EV 12.*

**Statement.** Pos(L) means W(g ∗ g̃) ≥ 0 for all g ∈ C_c^∞(−L, L), on the log scale.

- THEOREM: Pos((log 2)/2) (Yoshida; Connes-Consani, PAPER-0099; LED-POS-6).
- UNREFEREED: Zhu (arXiv:2608.24827, not in corpus) claims a certified 8.9·10⁻¹⁸ ≤ λ*(0.8) ≤ 2.27·10⁻¹⁷ (LED-POS-7). CON-0010's correction labels this "high-precision computation with an error budget, not directed rounding".
- RH implies Pos(L) for every L (Zhu Prop. 2.3).
- λ_min(L) decays like exp(−c e^{2L}). This is the C5 skeptic's correction of OB-9; Zhu's empirical law is −ln λ* ≈ 2π² N(T*)/ln N(T*) with T* = 2πe^{2L}.
- The C4-P Galerkin values are Rayleigh-Ritz upper bounds, 0.3-6% above the infimum, and replicate Zhu's Table 1 (C4 skeptic).
- Over F_q a finite window decides RH (C5-T3, D-23). Over Q, "no finite window suffices" is not a theorem (C5 skeptic §3.3).

**Targets.**

1. An independent Arb replay of Pos(0.8), so that two checkers authenticate it.
2. Pos(1.19): replace the pointwise prime-comb envelope A_L = Σ_{n≤e^{2L}} Λ(n)n^{−1/2} by a certified bound on the actual trigonometric sum over the primes 2, 3, 5 and 7, using linear forms in logarithms to exclude near-alignment (POS §8).
3. Host: a certified lower enclosure λ_min(S₁) > 0 for the repository's Lorentz-weighted energy-Schur kernel, or a precise obstruction. The tool is Zhu's one-stroke reduction (verified Cholesky, Bernstein-ellipse quadrature, tail coupling) (BRG-OPERATORS_HEAT-T1; OPEN_CUTS bounded contribution "whole-window sign certificate").
4. Host: restate the all-L gate in the slack form of Andrews-Connes-La Gatta, min(0, λ_min(S_L)) → 0 (BRG-OPERATORS_HEAT-T2).

**Ceiling.**

- Each Pos(L) is a consequence of RH.
- Pointwise-envelope certificates need doubly exponential resolution (BRG-OPERATORS_HEAT-O1).
- The host's "unbounded family of full windows" needs signed prime-comb cancellation.

#### D-17 - de Bruijn-Newman: explicit asymptotic theorem and an independent checker
*DBN / C1. S 3, T 4, EV 12.*

**Statement** (research_programs DBN §7(2), §8).

- Make Polymath Thm 1.5(i) (PAPER-0083) explicit: find a numerical C such that for 0 < t ≤ 0.2 and x ≥ exp(C/t), H_t(x + iy) ≠ 0 for y ≥ y₀(t,x) = O(1/√log x).
- Then "RH up to T implies Λ ≤ A/log T for T ≥ T₀, with explicit A ≈ 5" becomes a theorem that needs no canopy computation.

**Facts.**

- Λ ≥ 0 (PAPER-0036).
- Λ ≤ 0.2 (PT21 Cor. 2, LED-DBN-10) is derived from RH up to 2.51·10¹². So it adds no constraint on zeros beyond RH(T₀) plus unconditional theory (C1 FINAL, item 8). This refutes the investigator's sentence "dBN has no finite RH-implication".
- The 2026 claims are unrefereed: Planat-Raymond 0.156821 (FND-0011) and others (LED-DBN-11 to -13).
- The bounds conditional on 7/8 (LED-DBN-15) are gated by D-01.
- Heuristic model: no proved or claimed bound ≥ 0.1013 can exclude a single quadruple above T₀ (C1-ADJ-DBN).

**Next steps.**

1. Replay from scratch, in Arb, one Polymath criterion instance at X ≤ 2 × 3,000,175,332,800 (e.g. X = 6000000185827).
2. Optimise (t₀, y₀) to certify a baseline below 0.2.
3. Use the code as an independent checker for one 2026 certificate.
4. Record which inputs were reproduced from primitive sources.

This is certification infrastructure, not RH progress (see D-25 for how it could become informative).

#### D-18 - Montgomery-Vaughan character-sum bound under a half-plane
*QRH-CONSEQ / M4. S 3, T 4, EV 12.*

**Statement** (CON-0017, corrected; CONDITIONAL; the verifier's sketch, with MV §§8-9 not re-read).

- Hypothesis: L(s, χψ) ≠ 0 for Re s > θ for every ψ of modulus ≤ (log q)^C, for some fixed θ < 1.
- Conclusion: max_x |Σ_{n≤x} χ(n)| ≪ (1 − θ)^{−1} √q log log q for every primitive χ mod q. That is the Montgomery-Vaughan GRH bound under any fixed half-plane.
- Route: the unconditional MV Corollary 1 on minor arcs, plus a QRH version of MV Lemma 2 with error x·y^{θ−1}(log kx)²/(1 − θ)² on major arcs r ≤ (log u)^{O(1)}.
- The threshold θ < 2/3 of the Granville-Soundararajan route is specific to that route; it is not a limit of QRH.
- A weaker statement was checked: √q (log q)^{6/7} under QRH for twists of conductor ≤ (log q)^{1/3} (GS Thm 2.1).

**Next steps.**

1. Write the QRH version of Lemma 2 and the MV §9 bookkeeping in full.
2. Check that θ = 1/2 recovers MV.
3. Reconcile with CON-0029, whose character-sum claim is unverified.

#### D-19 - An OpenAI-independent 7/8 by the short route: the quartic row mean square
*QRH-EXT / M8 / 2026. S 5, T 2, EV 10.*

**Statement J4** (CON-0038, sound_and_useful; a CONDITIONAL implication [O], DOSSIER item C2 with n = 4).

- Setting: K = Q(i) and A_u(X) = Σ_{(𝔫,1+i)=1} μ_K(𝔫)(u/𝔫)₄ W(N𝔫/X).
- Implication: if Σ_{0<N(u)≤X^h} |A_u(X)|² ≪ X^{1+h+ε} for some fixed h with 1 ≤ h ≤ 10/9, then ζ_{Q(i)}(s), and hence ζ(s), has no zeros with Re s > 1/2 + 3h/8. That is at most 11/12, and tends to 7/8 as h → 1⁺.
- More generally, a bound X^a H^b with a + (b − 1/4)h ≤ 11/6 and h ≥ 1/3 gives 11/12.

**Floor result** (sound_and_useful; computed within the Observatory's transcription of Ji's inequalities).

- Ji's architecture (PAPER-0155; unrefereed; reaches 599/600; uses de Faveri's unrefereed density estimate, not OpenAI's results) cannot reach 11/12 with any zero-density input.
- The floor is ≥ 0.9898 unconditionally and ≥ 25/26 under GRH for the quartic family. With Ji's w-contour constraint it is ≥ 0.996732.

**New input needed.**

- A quartic duality partner: μ-removal for the angular-weight-1 quartic Kubota coefficients (David-Dunn-Hamieh-Lin, arXiv:2306.11875, Prop. 4.3), analogous to paper2's eq:convert2.
- A quadratic or optimal reflected large sieve.
- Explicit Fourier coefficients of n-fold metaplectic theta functions are known only for n = 2 and 3 [standard, not re-verified]. That is the concrete obstruction.

**Next steps.**

1. Re-derive Ji's six inequalities independently, especially C6 and the H^Λ factor.
2. Test a μ-removal identity numerically.
3. Compute Σ|A_u(X)|² at small scale (X ≈ 2000, H ≈ X^{1.05}).
4. Compute what de Faveri's optimal quartic sieve Θ₄ gives for a row mean square. The generic sieve alone gives nothing (DOSSIER item C4).

#### D-20 - Conjecture G: half-planes for infinite-order Hecke characters of Q(√−3) and CM elliptic curves
*QRH-EXT / M8 / 2026. S 5, T 2, EV 10.*

**Statement** (CON-0037, corrected; CONJECTURE). For every unitary Hecke character ψ of K = Q(√−3), of any infinity type l, L(s,ψ) ≠ 0 for Re s > 11/12. The bound would be 7/8 if the 7/8 architecture's angular bookkeeping goes through.

**Corollaries if true.**

- Every E/Q with j(E) = 0 (for example y² = x³ + D) has L(E,s) ≠ 0 for Re s > 17/12 (or 11/8). This would be the first fixed zero-free half-plane for a holomorphic newform of weight ≥ 2. Weight-one dihedral forms are already covered, conditionally, by paper2 Thm 1.1 and by Liu.
- Angular equidistribution of primes in Z[ω] with power saving, error O(x^{11/12+ε}) uniformly in arcs.
- Lindelöf to the right of Re s = 17/12.

**Mechanism** (sub-claim).

- From eq:convert2: μψγ₋₁ = χ_𝔫(−1)G^{−1}ν₀α^{l−1}γ₂.
- Only the frequency m = l − 1 = 0 carries a Patterson main term ≈ cX^{5/6}. Numerics up to N(𝔫) ≤ 3200 show this and were reproduced by the verifier; they are finite.
- For the frequency-0 case, pass to the conjugate character ψ̄.

**Load-bearing and unverified.**

- paper2 Prop. 3.1 with angular-frequency coefficients;
- an entire J_m(s) for |m| ≥ 2, including the cusp-cocycle terms generated by a second derivative;
- two-variable Mellin separation (Lemma B.3).

Keep the radial nonnegative weights and move α^l into the coefficients.

**Next steps.**

1. List every use of radiality in paper2 Secs. 4-7 and App. A-B.
2. Derive J_m(s) for m = −2.
3. Rerun the archive's check_paired and check_local identities with angular coefficients.

#### D-21 - Conditional consequences of a uniform half-plane, written as lemmas
*QRH-CONSEQ / M4 / M1 / M6. S 2, T 5, EV 10.*

Everything here is CONDITIONAL on the unrefereed half-plane claims and is gated by D-01 and D-02.

**(a) Linnik and progressions** (CON-0016, CON-0001; sound_but_known).

- H_θ implies P(a,q) ≪ q^{12/5+ε} effectively, with refereed density inputs (Montgomery and Huxley).
- With Chen-Gupta-Li (PAPER-0745, unrefereed) the exponent is 7/3 + ε. Their Cor. 1.4 already states this under any zero-free region of width η with η log x → ∞.
- ψ(x;q,a) = (x/φ(q))(1 + O(x^{−δ})) for φ(q) ≤ x^{5/12−ε} (x^{3/7−ε} with CGL).
- These correct DOSSIER §3, which gave Linnik exponent 8/3 and range x^{1−Θ}. Unconditionally L = 5 (LED-LFUN-10).

**(b) Piltz divisor problem** (CON-0018, sound_and_useful).

- ζ ≠ 0 on Re s > 7/8 implies α_k ≤ 7/8 − 49/(24k) for k ≥ 9.
- This improves the tabulated records for k = 14, …, 21: 0.72917 against 0.73190 at k = 14, and 0.77292 against 0.79137 at k = 20.
- Under 11/12: α_k ≤ 11/12 − 17/(7k) for k ≥ 12.
- Only the zeta statement is used, which is the Lean-claimed one.

**(c) Short-interval exceptional sets** (CON-0019, sound_and_useful; with CON-0028).

- Under 7/8, the Gafni-Tao Thm 1.2 bound for μ(θ) improves exactly on θ ∈ (≈0.2445, 5/12), with maximal gain ≈ 0.0108 at θ ≈ 0.2725 (for example μ(0.30) drops from 0.910 to 0.900). Under 11/12 the gain is at most ≈ 0.0026.
- It is a record only if it survives GT Thm 1.3 with A*, which has not been recomputed.
- The thresholds 17/30 (all intervals) and 2/15 (almost all) are unchanged for every half-plane θ₀ ≥ 7/10, because the binding point is σ = 7/10.

**(d) Artin's conjecture** (CON-0020, corrected). Hooley-type routes need θ below one of three thresholds:

- 0.656 (elementary Bombieri-Vinogradov);
- 0.796 (Nongkynrih; positive proportion, a = 2);
- 0.816 (Hooley's infinitude remark).

Both 7/8 and 1 − 10⁻⁶ lie outside all three.

**(e) Classical adaptations** (CON-0029, routine):

- Lindelöf to the right of θ;
- n(p) ≪ (log p)^{1/(1−θ)+ε};
- ((1 − θ)π²/(6e^γ) − ε)/log log q ≤ L(1,χ) ≤ (e^γ/(1 − θ) + ε) log log q.

The explicit q₀(θ,ε) remains open.

**Next steps.**

1. Write one-page lemmas that record every effectivity dependence on θ.
2. Recompute (c) with A*.
3. Check the endpoint of Ivić Lemma 8.3 for (b).

#### D-22 - Host: corrected Euler products and smooth numbers under graded hypotheses
*HOST (causal Euler, SHARP) / M1 / M3. S 2, T 5, EV 10.*

**(a) Corrected Euler products** (CON-0013, sound_but_known; BRG-CAUSAL_EULER-O1, -T2, -T4).

- OPEN_CUTS §6 at σ₀ = 1/2 is RH-equivalent; the host's pass7 PROOF.md §8 already states this.
- The σ₀-version is equivalent to ζ ≠ 0 on Re s > σ₀ (Akatsuka 2017, Thm 2). A single nonzero pointwise limit on Re s = σ₀ already forces it.
- Bounded deliverable: the conditional explicit-dependence theorem under H_Θ, with Ω± sharpness (Gorodetsky, arXiv:2211.08973: Cor. 5.4, eq. (2.15), Prop. 2.12, Lemma 2.8, Cor. 2.10). Label it non-RH-progress.
- Under QRH(11/12), the §6 target holds on Re s > 11/12 with discrepancy X^{11/12−σ+ε}.
- Cite the sharp tail X^{1/2−σ}/((σ − 1/2) log X) and the √2 factor on σ = 1/2 (Conrad 2005; Akatsuka Thm 1).

**(b) Smooth numbers** (CON-0005, corrected; a substitution theorem, CONDITIONAL on QRH(7/8)).

- Ψ(x,y) ~ xρ(u)K(−log log x/log y) and Ψ(x,y) ≥ xρ(u) for all y ≥ (log x)^{8+ε}, and also for 2 log x ≤ y ≤ (log x)^{8/7−ε}.
- Ψ ≍ xρ(u) fails for every c < 2 regardless.
- Effect on the host: the SHARP_NATIVE obstruction O4 moves from "growing-P control beyond (log X)² is RH-equivalent" to "available under QRH at (log X)^{8+ε}, with the window c ∈ [2, 8] open". There is no consequence for signed sums.

**Next steps.**

1. Add one line justifying the complex-s discrepancy identity; the bridge records this as a question for the authors.
2. File both items as separately labelled proposed objects for host review (AGENTS.md).

#### D-23 - Function-field transfer: a finite-window theorem without RH, and a fake-zeta test bed
*FF / C5. S 2, T 5, EV 10.*

**(a) Confluent inertia** (THEOREM; C5 skeptic §3.1; exact integer checks on 9,900 + 249 + 93 cases).

- Setting: P satisfies the curve functional equation, has distinct normalised reciprocal roots γ₁, …, γ_r, and m = #{j : |γ_j| > 1}.
- Then inertia(T_N) = (r − m, m, N − r) for every N ≥ r.
- Hence RH(C) ⇔ T_{2g} ⪰ 0, with no squarefree hypothesis. This corrects the hypothesis of C5-T3.

**(b) Window corollary without RH** (PROPOSITION-PROOF-SKETCH; C5 skeptic §3.2).

- Via Suzuki's fibre decomposition (arXiv:2610.41115, Prop. 4.3, not in corpus), with off-circle ζ_j allowed: RH(C) ⇔ W ≥ 0 on C_c^∞(−a, a) for any single a > (g − 1/2) log q.
- This is sharp for the formal class: for q = 3, g = 3, h = x³ − 10x − 7, T₅ ≻ 0 while T₆ is indefinite.

**(c) Census** (NUMERICAL-RIGOROUS; C5-E1, reproduced by the skeptic).

- Over 24 pairs (q,g): 16,354 admissible fake-or-genuine curve zeta functions, of which 12,787 are RH-false.
- If the degenerate Z ≡ 1 is counted, the totals are 16,368 and 12,801. The 41 cases the investigator left "undecided" are non-admissible.
- Prior art for the phenomenon: additive arithmetical semigroups (Knopfmacher; W.-B. Zhang 1990) and Ihara zeta functions of non-Ramanujan graphs.

**(d) One-sided bounds** (THEOREM; skeptic §3.4; elementary). Over F_q the lower bound N_r ≥ q^r + 1 − Cq^{r/2} for all r implies RH. The upper bound does not (g = 1 fakes).

**Use.**

- (b) is the precise function-field statement behind "a finite window decides RH over F_q".
- (c) is a test bed for any argument claiming "formal axioms imply RH".
- Over Q, no finite-rank mechanism is known, and no theorem says that none exists.

**Next steps.**

1. Write (b) line by line.
2. Add the semigroup and Ihara prior art to C5-E1 and OB-5.
3. See AC-22 for the function-field detection horizon.

### Tier C (EV at most 9)

#### D-24 - Extending and limiting the Siegel-exclusion method
*SIEGEL. S 3, T 3, EV 9.*

**(a) The κ floor** (SIEGEL §7.1).

- Every valid bound of the shape S₋(X) ≤ κ log X + e log q + O(1) has κ ≥ 1/2, by the prime ideal theorem.
- The published values all comply: OpenAI/Banks 13/16 → 3/4; Kerr 39/40 → 3/4; Guo 11/20 → 1/2.
- HEURISTIC count for larger kernels: κ(m) = (1 + m)/(2m). The zero estimate it needs has not been checked (§8.5(c)).

**(b) The ceiling on c** (auditor's computation).

- δ* = (1 − κ)²/(4bK).
- Guo's comparison with ideal arithmetic and a hypothetical y → q gives 3 − 2√2 = 0.171573…, below 1/5, the constant Lu-Zaman-Zhao computed for q ≤ 10¹⁰.
- Negative target: prove that no comparison of Guo Lemma 5.1 type reaches 1/5, or find the structural change that avoids the εκ loss.

**(c) Improving Guo's remainder.** Replace the trivial |Σχ| ≤ q/2 by an explicit Pólya-Vinogradov bound, to move y from q^{2+} toward q^{1+} (§8.4).

**(d) Extensions** (open).

- Quadratic Hecke characters over a number field K: relative Frobenius conjugation, heights ≍ |d_L|^{1/2}, and a Masser-type zero estimate for rank-[L:Q] lattices.
- Stark's residual cases.
- Exceptional zeros for GL(2) and Rankin-Selberg families by interpolation determinants (LFUN §7(iv)).

**Limit** (§7.5). The method cannot give (1 − β) log q → ∞, a fixed zero-free interval, Chowla-type positivity on (1/2, 1), or anything about complex zeros.

#### D-25 - Persistence lemma for the de Bruijn-Newman converse
*DBN / C1 / M2. S 3, T 3, EV 9.*

**Statement** (CON-0008, sound_and_useful; a target lemma with a proof outline).

- There are absolute constants c, γ₀ > 0 such that ζ(1/2 + δ + iγ) = 0 with 0 < δ < 1/2 and γ ≥ γ₀ implies Λ ≥ cδ²/(log γ)².
- Equivalently, Λ ≤ ε implies |β − 1/2| ≤ C√ε log|γ|.
- Sharp form (HEURISTIC, C1-E1): Λ ≥ c·min(δ², δ/log γ).

**Why it matters.** A bound on Λ currently carries no information on zeros beyond RH(T₀) (D-17). Persistence would turn such bounds into partial RH statements. The δ-free converse stated in research_programs cannot be obtained this way.

**Next steps.**

1. Write the energy proof rigorously: an almost-everywhere ODE between collision times, with continuity at collisions from Polymath Prop. 3.1(ii).
2. Prove a far-field estimate for H_t′/H_t at distance about 1 from the zeros for 0 < t ≤ 1/2, beyond Polymath Thm 1.5(iv).
3. Cross-check against C1's gap-lattice ODE model (exp_dbn_jensen.py) (AC-17).

#### D-26 - The Beurling frontier for RH and quasi-RH
*OBSTR / M7 / C2. S 3, T 3, EV 9.*

**Statement** (CON-0032, sound_and_useful).

- **T1** (THEOREM given BDR 1.3; a non-constructive case split). For every β > 2/5, the implication "a Beurling system with N_P(x) = ax + O_ε(x^{β+ε}) has ψ_P(x) = x + O(x^{1/2+ε})" is false. If RH fails, the rational system is a witness. If RH holds, BDR 1.3 gives a system with a real zero at some α ∈ (1/2, 2/3).
- **T2** (to be verified line by line). For Θ ∈ [1/2, 2/3) and β > 2Θ/(Θ + 2), the implication "Beurling with N_P = ax + O(x^{β+ε}) implies QRH(Θ)" is false.
- **T3** (BDR 1.1; Broucke 1.6). The same implication is false for every Θ < 1 when β ≥ 1/2.
- **T4.** For β < 1/2 and Θ ≥ 2/3, which covers 7/8 and 11/12, no countermodel is known.

**Target.**

- Construct an [α,β]-system with α ≥ 2/3 and β < 1/2 (BDR Remark 5.3(2) says improvements may be possible).
- Record A(β) := sup{α : an [α,β]-system exists} as a frontier quantity.
- Hilberdink: max(α, β) ≥ 1/2 for every system.

**Consequence.** This decides whether integer regularity can enter any QRH proof (the QRH hitting set of CON-0032).

#### D-27 - Host: principal-member transfer through trivializing rows
*HOST (families) / QRH mechanism / M3. S 3, T 3, EV 9.*

**Statement.** paper2's extraction is a concrete transfer from a family to its principal member, with two features:

- the rows u = p⁶ trivialise the sextic symbol (χ_𝔫(p⁶) = 1_{𝔭∤𝔫}) and have density ≍ H^{1/6}/log H;
- the full-row mean square is proved by a duality whose dual principal rows do not contain the principal source: μ times a sextic Gauss sum becomes a cubic Gauss sum, i.e. a Patterson coefficient.

**Design rule** (CON-0014, corrected; HEURISTIC). Extraction transfers family control to the principal member only if (i) the trivialising-row density is a power of H, and (ii) such a duality exists.

- For n = 2 the Poisson-dual principal rows return Σμ(n)n^{−1/2}{1, χ₋₄(n)}, so the duality is circular.
- The order-2 full mean square is equivalent, modulo Heath-Brown's large sieve, to its conclusion plus the dyadic bounds |A^{(u₁)}| ≪ D^{1/2}(H/U)^{1/4} for 1 < U < D^{1−θ}.

**Host relevance.** OPEN_CUTS §5 and the BRG-FAMILIES recommended actions.

- For the Dirichlet family mod ℓ, subpower principal-member extraction is RH-strength, because the principal member is ζ(s)(1 − 67^{−s}).
- There are three known family-to-member templates, each with its extra hypothesis: ILS Cor. 10.4, Iwaniec-Sarnak, and Deligne Weil I §3 (BRG-FAMILIES-O4, -O5, -O9, -T2, -T3).

**Next step.** Test (i) and (ii) for each host family and record a precise obstruction where they fail.

#### D-28 - Semilocal positivity at λ² = 3 as a mechanism
*OPS / C5. S 4, T 2, EV 8.*

**Statement** (C5-ML-C1 as corrected by the C5 skeptic; OPS §7-8; Connes-Consani Conj. 4.1, PAPER-0126). For S = {∞, 2, 3}:

1. Prove QW_λ ≥ μ > 0 on the complement of the span of the E-images of the even zero-integral prolate vectors and the two pole directions. This means verifying hypothesis (H2′) of Andrews-Connes-La Gatta Thm 8.14 (PAPER-0544, unrefereed).
2. Enclose the Schur complement on the ≈ 2λ² near-radical modes in ball arithmetic, controlling the Galerkin tail by the Sonin-space lower bound.
3. A required sub-step: identify ker u(F)₂₂ with the geometric semilocal Sonin space (PAPER-0125).

**Window reading.**

- h₁ is supported in (3^{−1/2}, 3^{1/2}), i.e. the statement is Pos((log 3)/2) = Pos(0.549).
- Zhu's unrefereed Pos(0.8) already covers this window numerically, so the content is the mechanism.
- Via Connes-van Suijlekom, it would make reality of the ground-state Mellin zeros a theorem.

**Status.** Open. Each fixed-window positivity is a consequence of RH. The step missing for RH is a uniform-in-window mechanism (C5-A).

#### D-29 - Jensen-heat bridge with error control, and a certified test on injected zeros
*POS / C1, C2. S 2, T 4, EV 8.*

**Statement.**

- HEURISTIC (C1-J2): for even Jensen polynomials of Ξ near height T, the first non-hyperbolic degree is d*(T,δ) ≈ T²/(2t_c(T,δ)), where t_c is the de Bruijn-Newman collapse time. For an isolated pair, d* ≈ T²/(4δ²).
- Target theorem (C1 §8.2): J^{d,0}_ev is hyperbolic near X = T² iff H_t is real-rooted near 2T at t = T²/(2d), up to O(T³/d²).

**Cross-campaign consistency** (OBSERVATORY-PROPOSED in this file; arithmetic only).

- For ξ̃ with an injected quadruple at 0.9 + 5i (δ = 0.4, T = 5), the isolated-pair prediction is 39.06.
- C2-17 found the first non-hyperbolic degree at d = 40, and the C2 skeptic confirmed exactly 40. Both are NUMERICAL-NONRIGOROUS (rounded coefficients, Sturm counts).
- The predictions for the undetected cases are 625 (0.6 + 5i), 400 (0.75 + 10i) and 306 (0.9 + 14i). All exceed the scan limit d = 240, consistent with C2's "hyperbolic up to 240".
- On Farmer's toy functions X_j the bridge is within 2.6% of the certified thresholds (C1-J3; for X₁₀, 119.63 against the certified 120).

**Next steps.**

1. Certify thresholds for J^{d,0}(ξ̃) in Arb at several (δ,T) in the isolated regime. By C1-ADJ-MONO, one certified pair (real-rooted at D, non-real at D + 1) fixes the threshold for all d (AC-15).
2. Then attempt the comparison lemma on Farmer's X_j.

#### D-30 - Host: Ingham-kernel lattice searches and fixed-detector firewalls
*HOST (SHARP, Mellin) / ARITH. S 2, T 4, EV 8.*

**(a) Mertens oscillations.**

- Hurst (PAPER-0585) gives limsup M(x)/√x > 1.826054 and liminf < −1.837625 (NUMERICAL-NONRIGOROUS, LED-ARITH-8).
- First re-evaluate h(y±, 14400) in Arb with zeros to at least 5200 digits.
- Then port the Kim-Nguyen BKZ and pruned-enumeration pipeline (PAPER-0786; LED-ARITH-9) to Ingham's kernel f(t) = (1 − t)cos πt + sin(πt)/π, with N ≈ 1000-1200 and target |h(y,N)| ≥ 2 (ARITH §7(i), §8).

**(b) The host's H₁ detector.**

- Under RH, H₁ = b_H + Σ_ρ c_ρ x^{iγ} + o(1), with apparent bias b_H ≈ 1.8033.
- By Ingham 1942 (PAPER-0071), eventual nonnegativity would force Q-linear relations among the ordinates (BRG-SHARP_NATIVE-O1; BRG-MELLIN_WAVELET-O1).
- A lattice search on c_ρ = (1 − 67^{−ρ})(ρ + 1)/(ζ′(ρ)(ρ − 1)(ρ − 1/2)) could refute "H₁ eventually ≥ 0" unconditionally (BRG-SHARP_NATIVE-T4). That would be a firewall, never progress on the negative-mass target.

**(c) A graded node** (MELLIN recommended action; CON-0007, corrected).

- θ-negative-mass for the 1/s²-smoothed rows is equivalent to ζ ≠ 0 on Re s > 1/2 + θ: Landau gives the forward direction and Titchmarsh 14.2 the converse.
- Any unconditional θ < 1/2 would be a zero-free strip.
- After host review, relabel the negative-mass branches as OPEN_RH_EQUIVALENT.

#### D-31 - Host: fixed-order xi-Pick positivity from verified zeros
*HOST (xi). S 2, T 4, EV 8.*

**Statement** (BRG-XI_PICK recommended action; tool T1).

- Safe-axis Kwong positivity of order N = 4 (then 5, …) for the actual ξ should follow from RH(T₀) via Sra's moving-frame perturbation (arXiv:2611.02944, Lemma C.4 and Thm C.9; unrefereed, not in corpus).
- This is bounded, probably provable, and not RH-equivalent.
- The all-order statement is RH-equivalent and is known in equivalent forms (Sra Prop. A.1; Polson Thm 26; Audenaert together with Lagarias/Hinkkanen).

**Pre-step (TT4).** On an X₉-type model, find the minimal Kwong packet size N(b) that detects an off-line quartet at height b, and compare it with Chasse's T² dispersal and Sra's PF concentration (BRG-XI_PICK-O7, -T4).

Sra's PF_k and Laguerre horizons are linear in the height (C1-ADJ-LOCAL), the opposite extreme from the T² horizons of Li and Jensen. Classify them in C1's implication/detection framework (C1 §8.7).

#### D-32 - de Branges zero condition: infinitely many failures and the rate 1/2
*C3. S 2, T 3, EV 6.*

**Statement.**

- THEOREM (C3-ADJ-S, adjudicated). Suppose the zeros with 0 < Im ρ ≤ γ_n are exactly 1/2 + iγ₁, …, 1/2 + iγ_n, all simple. Then P_n := −Re{ξ′(ρ_n)ξ(1 + ρ_n)} < 0 iff S(γ_n) − δ(γ_n) ∈ (3/4, 7/4) mod 2.
  - Here |δ(γ_n)| < 0.319 for 10 ≤ n ≤ 10⁵ and for all large n.
  - So the condition fails whenever S(γ_n) ∈ [−0.93, −0.57].
- NUMERICAL-RIGOROUS: 15,567 failures among n ≤ 10⁵.

**Targets.**

- Infinitely many failures, via large negative values of S at zeros.
- A positive proportion of failures, by adapting Trudgian's Gram-law theorem (LED-VERIF-13).
- CONJECTURE C3-ADJ-RATE (AC-18).

**Value.** It turns Conrey-Li's single counterexample (PAPER-0779) into a quantitative statement. The route is already refuted, hence S = 2.

#### D-33 - Weil-window detection: interpolation-regime theorem and sharpening of C4-B
*C4 / POS. S 2, T 3, EV 6.*

**Statements.**

- **THEOREM under H1** (C4-B; upheld by the skeptic with corrections).
  - Hypothesis H1: ρ₀ = 1/2 + δ + iT is a zero, and every other nontrivial zero outside its quadruple is on the line.
  - Conclusion: λ_min(L) < 0 for some L ≤ L_B(T,δ) = (1/(2δ))(log log T + log log log T + O_δ(1)).
  - Asymptotically, e^{2δL}/(4δ) ≈ (0.5 + 0.704L) log T. The investigator's 1.407L was a factor-2 slip.
  - At T = 3·10¹², the rigorous window is below the Nyquist window L_N = (1/2) log(T/2π) only for δ ≥ 0.2354.
- **REFUTED** (C4-R): the brief's heuristic that a window is blind for T ≫ 2πe^{2L}, up to O(log 1/δ), fails for every fixed δ.
- **Not established** (skeptic): "Nyquist locality" for κ = δ log(T/2π) < κ_c = 2.1773. The collision model contradicts it, with detection 0.42-0.85 below L_N at T₀ ≈ 10⁴.

**Open.**

1. Interpolation-regime detection L* ≤ L_N + C for every δ (AC-19).
2. Remove the (1 + 1.41L) loss using S₁(t) bounds.
3. Remove H1: a localised version assuming no other off-line zeros within (log T)^{C/δ}.
4. Relate detection to Andrews-Connes-La Gatta's reconstruction of zeros up to ≈ 2T*: does a window reconstruct heights at which it cannot detect off-line defects?

Missed prior art to cite: Danesh (arXiv:2611.10726), a two-interval criterion with the same e^{δx} mechanism and no window law.

**Host.** C4-REL is downgraded. The claim "no height-locality shortcut" rests on an unproved blindness statement; treat it as an open question for the energy-Schur route (OPEN_CUTS §3).

#### D-34 - Li coefficients beyond T²
*C1 / POS. S 2, T 3, EV 6.*

**Statement.**

- THEOREM (C1-L2). The statement is due to Oesterlé (2000, unpublished), as reported by Voros (arXiv:1703.02844); C1 FINAL §3.1 gives a complete independent proof.
  - T ≥ 100 and RH(T) imply λ_n > 0 for 1 ≤ n ≤ T².
  - RH(T₀) gives n ≤ 9.00105·10²⁴; RH(317) gives n ≤ 100489.
  - So Johansson's rigorous λ₁, …, λ₁₀₀₀₀₀ (LED-POS-1) carry no information beyond height 317.
- Target: RH(T) implies λ_n > 0 for n ≤ cT² log T, with an explicit c > 0.
  - The heuristic ceiling against adversarial phases is c = 2.
  - The single-defect barrier is c(T) → 4, with c(T₀) = 4.53.
  - At T₀, c = 1 would reach about 2.6·10²⁶.
- Converse target (POS §7(2)): repair Brown 2005, Thm 2 (PAPER-0600), i.e. λ₁, …, λ_N ≥ 0 implies no off-line zeros with |γ| ≤ c√N.

#### D-35 - Riemann-Roch on the square of the scaling site: a model case
*FF / OPS / C5. S 5, T 1, EV 5.*

**Statement** (C5-ML-W0 with the skeptic's addition; an open target with no RH claim). Define H⁰(D) and Dim H⁰(D) for D(f) = ∫ f(λ)Ψ(λ) d*λ on the square of the scaling site so that:

- (a) Dim H⁰(D) > 0 implies D is linearly equivalent to an effective divisor;
- (b) an effective nonzero divisor has positive degree against Ψ(1) + Ψ(1)^t; the degree is invariant under linear equivalence and equals ∫f d*u + ∫f du on D(f);
- (c) for real f ∈ C_c^∞([2^{−1/2}, 2^{1/2}]) with ∫f d*u = ∫f du = 0: Dim H⁰(D(f)) + Dim H⁰(−D(f)) ≥ s(f,f).

Then s(f,f) ≤ 0 on that support. This would re-derive the Yoshida / Connes-Consani positivity by the function-field mechanism W3 (Riemann-Roch gives effectivity, which gives the sign).

C5-ML-W (Connes' Lemma 2.1; PAPER-0007) shows that the general version is RH-equivalent, so all the content is in proving effectivity.

**Status.** No definition satisfying (a)-(b) is known; PAPER-0116 records that H¹ on the square is undefined.

#### D-36 - Zero density at the Guth-Maynard bottleneck
*ZDE (classical track). S 5, T 1, EV 5.*

**Statement** (ZDE §7(a)).

- Target: for (σ,τ) near (7/10, 13/10) and |b_n| ≤ 1, prove LV(σ,τ) < τ + 1 − 2σ. For example, |W| ≤ N^{9/10−δ} at σ = 7/10, T = N^{13/10}.
- Together with an improvement just left of 7/10, this gives sup A ≤ 30/13 − δ′ (LED-ZDE-1; Guth-Maynard, PAPER-0054, refereed) and the prime number theorem in all intervals of length x^{17/30−δ″} (LED-ZDE-8).
- No 2026 half-plane can move these exponents (CON-0028: the binding point σ = 7/10 lies below 7/8).

**First step.** Encode Guth-Maynard's master inequality (12.1) term by term in the ANTEDB framework, with free exponents (δ₁, δ₂) for the low-energy and energy terms, and compute which pairs push A(7/10) below 30/13.

## 3. Directions examined and not recommended (negative knowledge)

| Direction | Why not | Source |
|---|---|---|
| Lower Linnik's L = 5 using Siegel exclusion | the binding cases of Heath-Brown/Xylouris have no exceptional zero; when one exists, Deuring-Heilbronn helps | CON-0027 |
| Order-2 (quadratic) row extraction for a half-plane left of 11/12 | the Poisson-dual principal rows return the principal Möbius sums of ζ and L(s,χ₋₄); circular modulo Heath-Brown's large sieve | CON-0014 (corrected); DOSSIER §4.1 |
| QRH from proven mollified second moments (Bettin-Gonek or DWZ extraction) | any half-plane needs mollifier length above 1 (7/8 needs 4/3); proven lengths are 4/7 and 17/33 | CON-0031 (B)(i); LED-CRIT-7 |
| A generic sextic large sieve in place of the theta coefficients | the extraction then gives only the trivial bound | DOSSIER §2.3 and §4.3 (C4) |
| Siegel-type method toward zero-free strips, Chowla positivity or complex zeros | κ ≥ 1/2 and the δ(log X)² coupling cap c near 0.17 at best | SIEGEL §7 |
| Artin's conjecture by Hooley's route from 7/8 or from the 1 − 10⁻⁶ strip | known thresholds are 0.656, 0.796 and 0.816 | CON-0020 (corrected) |
| Short-interval PNT exponents from any half-plane θ₀ ≥ 7/10 | the binding point is σ = 7/10 | CON-0028; CON-0019 |
| Simple critical zeros for an individual GL(2) L-function from bandwidth-1/2 data | the certificate is negative for λ ≤ 0.5502; a doubled lattice is consistent | CON-0011; CON-0035 |
| Large criterion computations (Li, Jensen, ψ/π, Robin, Mertens, Nyman-Beurling, Λ) as tests of RH beyond T₀ | they lie inside an implication horizon of RH(T₀) or below every single-defect scale | C1 FINAL §4-§5 |
| "Nyquist locality" as guidance for host window families | blindness is unproved and the collision model contradicts it | C4 skeptic (C4-R, C4-REL) |
| Constraining Siegel's 1932 R(s) through the 2026 theorem | vocabulary only without an open attribution lemma | CON-0022 (vocabulary_only) |
| Turán's partial-sum route; Pólya's and Turán's T(x) conjectures; Mertens | refuted | C2 SP-7; C3 D5-D7; LED-ARITH-7, -9 |
| Turán, fixed-degree Jensen or infinite log-concavity of Taylor coefficients as a proof of RH | Turán holds for every H_t (THEOREM given Csordas-Varga); infinite log-concavity is expected to hold for small t < 0 (AC-24) | C2-29 (skeptic F5); CON-0033 (corrected) |
| Heat-flow arguments "with room to spare" | Rodgers-Tao: any valid argument must fail for every t < 0 | C2-29; BRG-OPERATORS_HEAT-O4 |
| Formal transfer of a function-field proof | fakes satisfy rationality, the functional equation and an Euler product; Deligne's tensor-power trick in number-field form is equivalent to RH | C5-E1; C5-D1; C5-OB5 |

## 4. Gating between directions

- **D-01 (kernel replay).** If the 7/8 challenges pass, D-18, D-21, D-22(b), LED-DBN-15, CON-0018 and CON-0019 become conditional on a kernel-checked statement. D-01 does not affect D-02 or D-10, which concern arguments and architectures.
- **D-02 (human proof of Prop. 3.1).** D-04, D-13, D-19, D-20 and D-27 all study or reuse the Prop. 3.1 mechanism. A gap found in D-02 would void D-20 and reshape D-13, D-19 and D-27.
- **D-03 (Siegel core).** Gates D-06 and D-24.
- **D-09 (two-thirds residue).** D-07, D-11, D-12 and D-14 reuse the AF/LZ certificate algebra and the BGSTB24 input.
- **D-08 (countermodel filter).** A prerequisite for reviewing any claimed proof, human or AI, including host submissions.
- **D-16, D-28 and D-33** share the Weil-form machinery. D-23 is the function-field model in which the finite-window question has a theorem.
- **D-29** uses C1-ADJ-MONO. **D-25** is what would make D-17's bounds informative.

## 5. Misreadings to avoid

- **QRH.** A half-plane Re s > Θ with Θ < 1 says nothing about Re s = 1/2. RH and GRH are open. QRH does not imply the density hypothesis for σ ≤ Θ, Lindelöf on the line, Bombieri-Vinogradov beyond level 1/2, or better short-interval exponents (DOSSIER §3).
- **Liu's "optimality".** It is the optimum of a fixed inequality system (DOSSIER §4.2), not a bound on the method.
- **Two thirds.** 2/3, and even 100%, is a lim inf density statement. It is insensitive to o(N) off-line zeros, gives nothing at any finite height, and is not RH (CRIT23 §6, §7.5).
- **Siegel exclusion.** It gives a gap c/log q at s = 1 only. It is not Chowla's conjecture, says nothing about complex zeros, and leaves Linnik's constant unchanged (SIEGEL §6).
- **Lean.** "Lean claimed" does not mean "replayed". Knausgard's Lean has three run-axioms. Lamzouri's Lean assumes BGSTB24 Lemma 5 and Riemann-von Mangoldt. The Observatory compiled nothing.
- **Zhu's Pos(0.8).** It is unrefereed, and the archive's connection verifier labels it high-precision computation with an error budget, not directed rounding (CON-0010).
- **Finite windows.** "Over Q no finite Weil window suffices" is not a theorem (C5 skeptic §3.3).
- **Λ.** A proved Λ ≤ 0.2 adds nothing beyond RH(T₀) plus unconditional theory (C1 FINAL, item 8).
- **Finite criterion computations.** Below T₀-derived horizons they are logical consequences of RH(T₀) (C1 FINAL §4).

