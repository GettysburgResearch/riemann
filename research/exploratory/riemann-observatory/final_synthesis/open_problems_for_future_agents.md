# Open problems for future agents: a handover

```text
Status: HANDOVER (exploration layer). Open problems, protocols and a continuation plan for autonomous research
        agents. It claims no new theorem. Each problem gives its status and the archive file it comes from.
        RH is open. The 2026 claims are unrefereed:
          - quasi-RH 11/12: Level-2 audited by the Observatory, no error found in the inspected portions,
            imported inputs not re-proved;
          - quasi-RH 7/8: not audited by us; Lean claimed, not replayed;
          - >= 2/3 of zeros simple and on the line: one proof step repaired (FND-0004); independent proof by
            Lamzouri;
          - Landau-Siegel exclusion: FND-0010.
Scope: open problems grouped by tractability (finite verification tasks; well-posed theorems weaker than RH;
        hard targets needing a new idea; RH-equivalent and conceptual targets). Also: starting files and tools,
        known pitfalls, reusable verification protocols, and an executable continuation plan.
Exact sources or dependencies:
        - proposals/independent_campaigns/C1..C5/FINAL.md (authoritative over REPORT.md and SKEPTIC_REVIEW.md);
        - audits/findings.jsonl, verified_findings.md, unresolved_findings.md, quasi_rh/DOSSIER.md,
          claims_2026/{CRIT23,SIEGEL}/DOSSIER.md, L2_flag_audits/*.md, lean_replay/README.md;
        - frontiers/records_ledger.md and ledger.jsonl (verifier-corrected values), research_programs.md;
        - connections/connections_register.md, strongest_connections.md, repository_bridge.md;
        - frontiers/missing_lemmas.md, known_obstructions.md, unsolved_questions.md (cited "UQ <id>");
        - proposals/ranked_research_directions.md ("D-nn") and actionable_conjectures.md ("AC-nn");
        - history/abandoned_approaches.md; quality/*.md; experiments/reproducibility.md; methodology.md;
          corpus/bibliography.jsonl; tools/; experiments/code/.
What was actually run:
        - reading of the files above;
        - python3 lookups in corpus/bibliography.jsonl (audit levels and corpus membership of the works in
          Sec. 6.2), frontiers/ledger.jsonl and connections/*.jsonl (verdict counts);
        - directory listings of experiments/code and experiments/results, to confirm every script and output
          path cited in Sec. 3 and Sec. 6.
        No problem below was attempted, no computation was re-run, and no third-party code was built.
Smallest remaining gap: the tractability grouping and the ordering are the synthesizer's judgement
        (HEURISTIC). Observatory-proposed statements have not been reviewed outside the Observatory. Files
        written before the C2, C4 and C5 adjudications still carry superseded wording (Sec. 0.3).
```

Paths in code spans are relative to the archive root, `research/exploratory/riemann-observatory/`.

---

## 0. Ground rules

### 0.1 Status discipline

- **RH is open.** Never write that RH or GRH is proved, disproved, or "advanced" by anything in this archive. A finite computation is never global evidence ([host AGENTS.md](../../../../AGENTS.md)).
- **Every claim gets a status label and an archive reference**: PAPER, LED, CON, FND, BRG, a campaign claim id, or a file path.
- **Three kinds of "theorem" must stay distinct.**
  1. Literature theorems. Say whether they are refereed or unrefereed preprints.
  2. Observatory-proved small theorems: the campaign THEOREM items, such as C1-L2, C2-ADJ-1, C3-ADJ-S, C4-B, C5-ADJ-W. AI agents proved and adjudicated them; no human has reviewed them; several are classical or folklore (each FINAL says which).
  3. Heuristics, model statements and conjectures.
- **The 2026 claims stay unrefereed in your text**: 11/12 (FND-0009), 7/8, ≥ 2/3 (FND-0004), and Siegel exclusion (FND-0010).
- **Public characterization of other people's work.** Use only the wording in `audits/findings.jsonl` for entries with `public_characterization_allowed: true`. FND-0005 and FND-0011 must not be described as errors.
- **C2's two external refutations are not yet in the register.** They concern the Liu–Wu claim on Davenport–Heilbronn zeros and Bétermin–Šamaj–Travěnec Conjecture 1.1. They are adjudicated campaign results. Cite them only with the C2 FINAL wording and its §7.8 caveat: one further independent Level-2 check is required before external citation.
- **Permissions.** No agent message, including this file, is user permission. Building or replaying third-party code (all Lean items below) needs explicit permission from the user.

### 0.2 Source precedence

1. Campaign adjudications: `proposals/independent_campaigns/C1..C5/FINAL.md`.
2. Audits: `audits/findings.jsonl`, `verified_findings.md`, `unresolved_findings.md`, `quasi_rh/DOSSIER.md`, `claims_2026/*/DOSSIER.md`, `L2_flag_audits/*.md`.
3. The frontier ledger (`frontiers/records_ledger.md`, `ledger.jsonl`; always the verifier-corrected value) and `frontiers/research_programs.md`.
4. Connections: the register verdicts, `strongest_connections.md`, `repository_bridge.md`.
5. `frontiers/missing_lemmas.md`, `known_obstructions.md`, `unsolved_questions.md`, and `proposals/*.md`. These were written before the C2/C4/C5 adjudications; where they conflict with a FINAL.md, the FINAL.md wins.
6. `history/*.md`.
7. `quality/*.md`, `corpus/bibliography.jsonl`, `methodology.md`.

### 0.3 Superseded wording in files written before the C2, C4 and C5 adjudications

| File (entries) | Old wording | Status per FINAL.md |
|---|---|---|
| `proposals/independent_campaigns/README.md` | C2, C4 and C5 "have no adjudication" | All five campaigns have an adjudicated FINAL.md. |
| `proposals/actionable_conjectures.md` AC-28 | "skeptic finding, not adjudicated" | THEOREM C2-ADJ-2: the exact s = 1/2 threshold k* = 7.0555079554…; BST Conjecture 1.1 is false (C2 FINAL §3.2). External citation still needs the §7.8 replay. |
| AC-21; `ranked_research_directions.md` D-23 | the function-field window criterion is a PROPOSITION-PROOF-SKETCH | THEOREM C5-ADJ-W, sharp over the formal class (C5-ADJ-SHARP; C5 FINAL §3.3–§3.4). |
| `missing_lemmas.md` R1 (W-a); `known_obstructions.md` OB-24 OB2(c); D-23 text and §5 of the ranked directions; `strongest_connections.md` §5.4 | "over ℚ no finite window suffices" is "not a theorem" or a heuristic | The sentence is **false as stated** (C5-ADJ-LOG, trivial and non-constructive). Its precise replacements are C5-ADJ-MODEL (THEOREM) and the open target EFR (C5 FINAL §3.5, §5). |
| `unsolved_questions.md` I2 | open | Answered in model form by C5-ADJ-MODEL, with counting error O(T). The version with O(1) error (Gram points plus Beurling sampling) is a PROPOSITION-PROOF-SKETCH. |
| UQ D5; `known_obstructions.md` OB-18; ranked directions §3 ("Nyquist locality"); AC-19, AC-20 | blindness open; the "corrected statement" not established | The brief's Nyquist heuristic is REFUTED for every fixed δ. The "corrected statement" is REFUTED as a universal law (C4-ADJ-WIT, Arb-certified model witnesses). Blindness is a THEOREM only in an astronomically thin neighbourhood of the line (C4-ADJ-BLIND). The exact criterion is C4-ADJ-PAIR. Read AC-20 in the narrowed form of C4 FINAL §2a. |
| Anything quoting C2-14 "modulo the moment lemma" | CONDITIONAL | THEOREM, given IMPORTED Csordas–Varga 1988 (read at L0+); the moment lemma is proved (C2-ADJ-3). |
| Anything quoting C2-17 or C2-28 as a theorem | THEOREM | (a) is CONDITIONAL on ζ having finitely many off-line zeros. The unconditional analogue is THEOREM C2-ADJ-6. |
| Any C2 Li-threshold table | 20857, 7395, 112929, 41098 | 20855, 7477, 112538, 40908 (NUMERICAL-NONRIGOROUS, two codes; C2 FINAL F3). |
| Any Weil-window certification cost "L e^L digits" | exp(−L e^L) as a decay law | −ln λ_min ≈ c e^{2L} with c ≈ 12; certification needs about 5.4·e^{2L} digits (C5 FINAL §1 row 6). |

---

## 1. State of play in one table

| Object | Status after the Observatory | Reference |
|---|---|---|
| RH | open | — |
| RH(T₀), T₀ = 3,000,175,332,800 (12,363,153,437,138 zeros) | IMPORTED, rigorous computation | LED-VERIF-1 |
| Zero-free half-plane Re s > 11/12 for ζ and all Dirichlet L | unrefereed; L2 audit found no error; Patterson/Kubota and Goldmakher–Louvel imports not re-proved | FND-0009; DOSSIER §1.2 |
| Re s > 7/8 | unrefereed; not audited; Lean statements read statically, not built | DOSSIER §1.3; `audits/lean_replay/README.md` |
| Refinements to about 0.8741 (best claimed B_tw = 0.8740585…, Liu hexagon:2610.00655v3; verifier-corrected) | unrefereed; all import the 7/8 inputs | LED-ZFR-3; DOSSIER §1.5 |
| liminf N₀ˢ/N ≥ 2/3 (≥ 0.6725007); distinct ≥ 5/6 (≥ 0.8362504) | unrefereed; one proof step repaired; theorems unaffected | FND-0004; LED-CRIT-1, -2 |
| 0.67353820 / 0.83900460 (Knausgård) | unrefereed; three computer searches unreplayed | LED-CRIT-3 |
| (1 − β) log q ≥ c for real zeros | unrefereed; four proofs audited with no error and no gap | FND-0010; LED-LFUN-6 |
| de Bruijn–Newman Λ | 0 ≤ Λ ≤ 0.2 refereed. Λ ≤ 0.2 adds nothing beyond RH(T₀) plus unconditional theory | LED-DBN-6, -10; C1 FINAL §1 row 8 |
| Weil positivity | Pos((log 2)/2) refereed; Pos(0.8) an unrefereed computation | LED-POS-6, -7 |
| Large criterion computations | none informative beyond T₀; the Li, Jensen and ψ/π ranges are implied by RH(T₀) | C1 FINAL §4–§5 |
| Window locality | Nyquist heuristic REFUTED. Under H1, detection at L = O_δ(log log T); blindness proved only astronomically near the line | C4 FINAL §3.3, §3.6 |
| Function fields | RH(C) ⇔ T_{2g} ⪰ 0; one window of half-width > (g − 1/2) log q decides RH | C5 FINAL §3.2–§3.3 |
| Countermodel protocol | blind spot = the full Selberg class (M10 has an Euler product and a self-dual FE) | C2 FINAL §3.1, §3.5 |
| de Branges zero condition | ⇔ S(γ_n) − δ_n ∉ (3/4, 7/4) mod 2; 15,567 failures among the first 10⁵ zeros | C3-ADJ-S; FND-0013 |

---

## 2. Open problems by tractability

The four tiers:
- **Tier 1:** finite and decidable (a replay, an audit, a certified computation; days of work).
- **Tier 2:** well-posed theorems weaker than RH, where the archive identifies a route (weeks to months).
- **Tier 3:** targets that need a new idea (record-breaking, or quasi-RH strength).
- **Tier 4:** RH-equivalent or conceptual targets (work on model cases only).

Cross-references: UQ = `frontiers/unsolved_questions.md`, D = `proposals/ranked_research_directions.md`, AC = `proposals/actionable_conjectures.md`.

### Tier 1. Verification gates and finite, executable tasks

**V-1. Kernel replay of the 7/8 statements** (UQ A1; D-01; DOSSIER §1.3; `audits/lean_replay/README.md`). *Needs explicit user permission.*
- Setting: github.com/openai/math @ 4eaee87548250b2682affda7d05d947c05554bae, toolchain leanprover/lean4:v4.34.1, Mathlib d13f23b723b8a846827a245b89c10fc7d3f11612.
- Question: does `lake build OAI.NumberTheory.DirichletL.Nonvanishing` succeed, and do `riemannZeta_ne_zero_of_seven_eighths_lt_re` (ζ(s) ≠ 0 for 7/8 < Re s) and the DirichletSevenEighths challenge pass all of the following?
  - Lean FRO `comparator` with `lean4export`;
  - an independent kernel (nanoda, disabled in the configs);
  - `#print axioms`, showing only propext, Quot.sound and Classical.choice.
- Success certifies the ζ and Dirichlet 7/8 statements relative to the Lean kernel and Mathlib's definitions, and hence 11/12 a fortiori. It does not certify paper2's argument.

**V-2. Fidelity of the Hecke statement** (UQ A2; DOSSIER §1.3). The challenge defines its own `LFunction χ s := π^s Γ(s)⁻¹ Λ(s)/6` from shifted Hurwitz even kernels. Prove, by hand and then formally, that for Re s > 1 it equals Σ_{𝔞≠0} η(𝔞) N𝔞^{−s} = (1/6) Σ_{z∈O∖0} χ(z) N(z)^{−s}. The dossier calls this plausible but not done.

**V-3. Siegel-zero formal replays** (UQ A9; SIEGEL §8(2); FND-0010). *Needs permission.*
- Run `comparator ComparatorChallenges/SiegelZeros.json` with nanoda on `OAI.NumberTheory.SiegelZeros.Main` (same pin as V-1).
- Replay Kimura's `B4.Chi8.zero_gap_all` (cln-imq-2k @ e66ab86). It implies the formal statement with c = 5.811·10⁻⁴.
- Without permission: read the 642 lines of the chain-A assembly that no reported external build covers (`audits/claims_2026/SIEGEL/adjudication_U4.md` §3).

**V-4. Formal replay of the two-thirds theorem** (UQ A6; CRIT23 §8(2)). *Needs permission.*
- Setting: anthropics/zeta-23-lean, tag v1.0 (Lean v4.33.0-rc2, Mathlib 51e6992efd06).
- Run `#print axioms` on `Zeta23.thmB0_mult`, `thmC0_mult` and `two_thirds_on_critical_line`.
- Run comparator against `comparator/Challenge/Multiplicity.lean`.
- Settle finding F5: how this relates to anthropics/formal-math fbdc36b.

**V-5. Second review of the FND-0004 repair** (UQ A5; CRIT23 §8(1); `audits/claims_2026/CRIT23/adjudication_P1-F1.md` §5).
- Independently re-derive tr G̃ = N(I) + O(X^{1/2}L) from AF eq. (2.8), using one-sided sums (the decay estimate AF use in Props 4.3 and 5.2).
- Then the consolidated erratum list (P1-F1, P1-F2, P2-F1..F3, F1, F3, F7) can go to the authors.

**V-6. Knausgård's three local inequalities** (UQ A7; LED-CRIT-3; CRIT23 §8(3)).
- Re-certify Props 3.3, 5.3 and 6.3 of arXiv:2610.08965v1 with an independent branch-and-bound in directed-rounding Arb, written from the statements and not from the author's code.
- This is the only gap between 0.6735382 / 0.8390046 and the audited 0.6725007 / 0.8362504.

**V-7. Residue on the Lamzouri route** (UQ A8; CRIT23 §8(4)). Either write P2-N1 out line by line, or re-derive BGSTB24 Lemma 4 and the Goldston–Montgomery evaluation of R(x, T) on [0, 1 − 2ε₀].

**V-8. Directed-rounding replay of Pos(0.8)** (UQ A11; LED-POS-7; CON-0010; C5 FINAL §5, EFR (i)).
- Decide whether λ*(0.8) ≥ 8.9·10⁻¹⁸ holds in ball arithmetic.
- The claim is Zhu, arXiv:2608.24827v2, Cor. 6.3: unrefereed, and per the POS frontier critique, as cited by the CON-0010 verifier, the lower-bound assembly used non-interval 50-digit mpmath with an error budget.
- It is the only certified window containing primes, and it fixes the numerical radius in C4-ADJ-BLIND. The work is not in the corpus.

**V-9. The Planat–Raymond certificate and the Polymath canopy step** (UQ A12, A13; FND-0011 unresolved; LED-DBN-12).
- Replay Λ < 0.156821 (arXiv:2611.06245v1).
- Know before starting: even if correct, the bound adds nothing beyond RH(T₀) plus unconditional theory. It also lies above the single-defect model threshold 0.1013 (C1 FINAL §1 row 8, C1-ADJ-DBN). The value of the replay is record hygiene.
- Separately, verify the canopy step of Polymath15 Table 1 row 2, which underlies the refereed Λ ≤ 0.2 (C1 FINAL §2a, C1-E1).

**V-10. The Lu–Zaman–Zhao production run** (UQ A10; SIEGEL §3). Replay the run for 4·10⁵ < q ≤ 10¹⁰. Banks's all-q constant 3.0·10⁻³ depends on it.

**V-11. Rigorous Li thresholds for ξ̃** (C2 FINAL §7.3; C2-16).
- Goal: make "λ_n(ξ̃) > 0 for n ≤ 20854 and λ_20855(ξ̃) < 0" NUMERICAL-RIGOROUS, for the quadruple injected at (β, γ₀) = (0.6, 14). It is now NUMERICAL-NONRIGOROUS.
- Ingredients: Arb ordinates from EXP-0001; an Arb tail integral including the boundary term −g_n(T*)S(T*); an explicit bound on E_n via Trudgian's S₁ bound, conditional on RH(T₀).

**V-12. Rigorous Jensen threshold for ξ̃** (C2 FINAL §7.1; AC-15).
- Certify the least d for which J^{d,0}(ξ̃) is not hyperbolic, for the quadruple injected at 0.9 + 5i. The NUMERICAL-NONRIGOROUS value is d = 40; the HEURISTIC bridge C1-J2 predicts T²/(4δ²) = 39.06.
- Reuse C1's `adj_farmer_x10.py` pipeline. By C1-ADJ-MONO, one certified pair (real-rooted at D, a non-real zero at D + 1) fixes every d.
- Then test the predictions 625, 400 and 306 for the other injected quadruples.

**V-13. Lowest off-line zeros in the zoo** (C2 FINAL §7.2).
- Prove that Z_{x²+5y²} has no zero in [1, 1.17816] × [0, 1193.9) by an argument-principle count with exact corners (pitfall A1, §4.5).
- Do the same for ζ₁₉ below t = 6.0·10⁵.
- Both are currently screens only (NUMERICAL-NONRIGOROUS).

**V-14. de Branges rate blocks** (C3 FINAL §9.2; AC-18).
- Count failures of the zero condition in 1000-zero blocks near n = 10¹¹ and 10¹², using flint `acb.zeta_zeros` (about 50 s per 100 zeros at 10¹¹).
- C3-ADJ-RATE predicts proportions of about 0.23 and 0.24. This is a falsification test of a CONJECTURE, not a proof.

**V-15. A certified lower bound on one C4 model threshold** (C4 FINAL §6.4).
- Certify a positive lower bound for the collision-model form at T₀ = 9999.46, δ = 0.1, L = 3.2.
- This needs a certified lower bound on P in the modulated frame, of Zhu's geometric-side type. It is the only way to make "L* ≈ L_N" two-sided in any model.

**V-16. Replays before external citation** (C2 FINAL §7.4, §7.8).
- (a) A Level-2 check, by an agent independent of C2, of the Chowla–Selberg constant term Z_k(1/2) = 2γ + 2 log(k/(4π)) + 8 Σ d(N) K₀(2πNk), and of k* = 7.0555079554….
- (b) A Level-2 check of the failing step in Liu–Wu (a 0/0 at common zeros of f(s) and f(1 − s)) against the full text of arXiv:2503.24275.
- (c) Obtain Bateman–Grosswald 1964 (Acta Arith. 9, 365–373) to settle prior art.
- Only after these, propose findings-register entries.

**V-17. FND-0005** (UQ A18). Does Yang's written argument (arXiv:2301.03165 v1) cover the v1 constant 21.432 over the full stated range? Downstream constants are unaffected either way. No public characterization is allowed without an independently produced witness.

**V-18. The 7/8 manuscript and the first adversarial round** (UQ A4; DOSSIER §5(1), §5(7)).
- Audit the 199-page manuscript (PAPER-0528) section by section, at least to the depth of FND-0009.
- Then run the adversarial round on the quasi-RH dossier and audits, which has never been done: create an `adversarial/` folder with `*_adjudication.md` files.

**V-19. Live unrefereed proof claims** (UQ A20; C3 FINAL §9(5)–(6)).
- Audit arXiv:0807.0090 v5–v10 (PAPER-0885) with C3 checklist items 3, 4 and 8.
- Determine whether de Branges' post-2004 manuscripts rely on conditions of the Conrey–Li (3.1)/(3.3) type, which are false (C3-D1; FND-0013).

**V-20. Admissibility at genus 1** (C5 FINAL §3.6, §9.4(i)).
- Prove: for every prime power q, P(T) = 1 − aT + qT² has all place counts B_d ≥ 0 if and only if −q ≤ a ≤ q + 1.
- Necessity is a THEOREM: B₁ = q + 1 − a and B₂ = (q + a)(q + 1 − a)/2. Sufficiency is verified exactly for 14 values of q only.

**V-21. Shorter verification items:**
- Ji's 599/600 argument and its unrefereed input, de Faveri's Cor. 1.5 (UQ A15).
- Cureton–Thorner: provenance and formal statement (UQ A14; CON-0026).
- Li–Liu's claim that any Θ < 11/12 already gives the GRH power (UQ A16).
- The Yang–Yang 0.7962 report, which is in tension with AF §7.2(e) (UQ C15).
- The κ = 1/2 Siegel variants of Green, van Dijk, Pescador and Barreto (SIEGEL §8(3)).
- A third replay of the CON-0025 class-group scan, and Kimura's Lean statement of Prop. 9 (CON-0025, next steps 1–2).
- An independent replication of RH(3·10¹²), with archived code (UQ A17).

### Tier 2. Well-posed theorems weaker than RH, with an identified route

**T-1. Li positivity beyond T²** (C1 FINAL §8.1; C1-L4 PROPOSITION-PROOF-SKETCH; AC-14; UQ F2; D-34).
- *Statement.* There are explicit c > 0 and T₁ such that, for T ≥ T₁, RH(T) implies λ_n > 0 for all n ≤ cT² log T.
- *Known.* The version n ≤ T² is THEOREM C1-L2 (statement Oesterlé 2000; complete independent proof).
- *Heuristics.* Arguments using only RH(T) and N(t) bounds cannot exceed c = 2 (adversarial phases). The single-defect barrier is c(T) → 4, with c = 4.53 at T₀.
- At T₀, c = 1 would lift the horizon from 9.0·10²⁴ to about 2.6·10²⁶.
- *Start:* the proof in C1 FINAL §3.1 (Lemmas A and B, Rosser tails) and `adj_numbers.py` part (b).

**T-2. An explicit Nicolas/Robin implication theorem** (C1 FINAL §8.3; C1-D3 PROPOSITION-PROOF-SKETCH; AC-16; UQ G5; D-15).
- *Statement.* RH(T) implies Nicolas' inequality c(x) > 0 for all x ≤ X(T), with X(T) ≈ cT²/log²T and every truncation and O(1/log x) term explicit.
- The leading-order sketch gives 4.36·10²³ at T₀.
- Any X(T₀) ≥ 3.0·10¹³ would make the Morrill–Platt Robin range (LED-ARITH-1) a corollary of RH(T₀) (LED-VERIF-1).
- *Template:* Johnston, arXiv:2109.02249 Thm 3.2 (PAPER-0917).

**T-3. The Jensen–heat bridge with error control** (C1 FINAL §8.2; C1-J2 HEURISTIC; UQ F3; D-29).
- *Statement.* The even J^{d,0} of Ξ is hyperbolic near X = T² if and only if H_t is real-rooted near 2T at t = T²/(2d), up to O(T³/d²).
- *First test:* Farmer's X_j, with certified thresholds 120 (j = 10), 750 and 478 (j = 20, two configurations), 1898 (j = 40) and 4243 (j = 60). The bridge is within 2.6% of all of them (C1 FINAL §2a).

**T-4. Infinitely many de Branges failures** (C3 FINAL §9.1; UQ E1; FND-0013; D-32).
- *Statement.* Show that S(γ_n) − δ_n ∈ (3/4, 7/4) mod 2 for infinitely many n. By C3-ADJ-S this is exactly the failure of −Re{ξ′(ρ_n)ξ(1 + ρ_n)} ≥ 0. Stretch goal: a positive proportion of n.
- *Routes:*
  - adapt Trudgian's proof that Gram's law fails a positive proportion of the time (Acta Arith. 148, 2011) from Gram points to zeros, using Selberg's moments of S and the boundedness of δ;
  - or hit the window (−0.93, −0.57) through large negative values of S.
- *Companion:* UQ E3, the argument form of Conrey–Li Thm 2.

**T-5. Near-line detection under H1** (C4 FINAL §6.2; AC-19; UQ D6; D-33).
- *Statement.* Under H1 (one off-line quadruple, every other zero on the line), λ_min(L) < 0 for all L ≥ (1/2) log(T/2π) + C′(δ), with C′(δ) = O(log(1/δ)) or O(1).
- *Known:* THEOREM C4-ADJ-C gives C(δ) ≈ (2.1–3.1)/δ, with certified constants from 4.40 (δ = 0.49) to 313.17 (δ = 0.01).
- The sinh test function cannot do better. Try an interpolating Paley–Wiener function that vanishes at the real zeros near T (Landau–Widom/prolate at full saturation).
- *Cheaper first step:* replace the S(t) input by an S₁(t) bound, to remove the (1 + 1.41L) loss.

**T-6. Blindness through the local resolvent** (C4 FINAL §6.1; UQ D5, D7).
- *Statement.* Bound D(T, δ, L) = λ_max(E_w*(P + 2E_uE_u*)⁻¹E_w) from above for T ≥ (1 + c)·2πe^{2L}.
- *Tool:* P(g) = (1/2π)∫|h_g(r)|²Ψ_L(r) dr + pole terms, with Ψ_L(r) = Re ψ(1/4 + ir/2) − log π − Σ_{n<e^{2L}} 2Λ(n)n^{−1/2} cos(r log n).
- Prove hypothesis R with explicit η wherever Ψ_L ≥ Ψ₀/(1 + η) near T. Exhibit heights where R fails.
- *Constraint:* C4-ADJ-WIT shows that no height-only law "L* ≥ L_N(T) − c" holds across the injection models.

**T-7. Remove H1 locally** (C4 FINAL §6.3). Prove C4-B when every other off-line zero, if any, lies at distance at least (log T)^{C/δ} from T.

**T-8. Detection horizon for zeta-like zero multisets** (C5 FINAL §9.3, §3.5; connects to C1).
- *Setting:* the class Z_ζ of symmetric multisets with N(T) = θ(T)/π + O(log T).
- *Question:* determine L*(δ, T) := inf{L : every Z ∈ Z_ζ with an off-line point at (δ, T) has W_Z indefinite on window L}. Is L* = O(1/δ + log T)?
- *First step:* turn the Gram-point refinement of C5-ADJ-MODEL (PROPOSITION-PROOF-SKETCH) into a proof with an explicit δ₀(L).
- By C5-ADJ-MODEL this class gives only lower bounds; any effective finite reduction for ζ must use prime-side structure.

**T-9. Between M10 and the Selberg class** (C2 FINAL §7.5). Classify the elements of S^♯₁ that have an Euler product and Λ_F ≥ 0, using Kaczorowski–Perelli structure theory (PAPER-0192). Either exhibit an RH-false F with P1, P3, P5 and P7 that is not in S, or prove the class reduces to Dirichlet L-functions. Either answer sharpens SP-1c.

**T-10. The Beurling frontier** (CON-0032; UQ B11, B12; AC-27; D-26).
- First verify T2 line by line: does BDR §5 use RH only through zero-freeness with Lindelöf-type bounds on Re s > 1 − α/2?
- Then determine A(β) := sup{α : an [α, β]-system exists} for β < 1/2.
- In particular, decide whether α ≥ 2/3 with β < 1/2 occurs. This is the open region containing 7/8 and 11/12.

**T-11. The Möbius Nyman–Beurling rate law** (CON-0021; UQ G1; AC-26).
- *Statement.* For α ∈ (Θ, 1), with Θ = sup Re ρ, limsup_n log s_n(α)/log n = −2(α − Θ), with the stated corrections at α = 1. Hence RH ⇔ s_n(α) ≪ n^{1−2α+ε}.
- *Status:* Observatory-proposed; the verifier re-derived both directions. Write the full proof.

**T-12. 19/27 without RH** (CON-0006 corrected; UQ C5, C6; AC-11; D-14).
- *Statement (ML-CGG).* Σ_{T<γ≤2T, β≠1/2} |Bζ′(ρ) − Bζ′(1 − ρ̄)|² = o(T(log T)³) for the BHB mollifier with θ → 1/2.
- It gives liminf N*/N ≥ 19/27 unconditionally, and is strictly weaker than RH.
- The unconditional inequality N* ≥ S₁²/(S₂ + D/2) has been re-derived.

**T-13. The persistence lemma for de Bruijn–Newman** (CON-0008; UQ F8; AC-17; D-25; C1 FINAL §8.5).
- *Statement.* ζ(1/2 + δ + iγ) = 0 implies Λ ≥ cδ²/(log γ)². The sharp form c·min(δ², δ/log γ) is conjectured.
- *Status:* a proof sketch with two gaps. The hard part is controlling the other zeros.

**T-14. Robin's inequality for 22-free n** (UQ G4; LED-ARITH-2). This needs a certified Mertens-product bound with relative error below about 2.4·10⁻⁷ near x ≈ p_{k0} = 29,996,208,012,611 (ARITH critique).

**T-15. Transfer of the rank–trace device to GL(2)** (CON-0035, CON-0036; UQ C9, C10; AC-09, AC-10; D-11, D-12).
- (a) For one fixed GL(2) newform, prove the all-zeros pair-sum asymptotic for Fourier support below 1/2. With the rank–trace inequality this gives liminf N_d/N ≥ 0.4617.
- (b) Prove the explicit Petersson diagonal lemma. With the Hua–Yang template (unrefereed), harmonic family averages reach ≥ 0.6725 (simple and critical) and ≥ 0.8363 (distinct).

**T-16. A falsification handle for Prop. 3.1 of the 11/12 paper** (UQ B6; AC-01; D-04; DOSSIER §2.5, §5(5d)). Prove, as a separate theorem, #{u₀ ∼ U : L(s, νχ_·(u₀)) has a detectable zero with β ≥ σ} ≲ U^{2−2σ+ε}. A numerical violation would falsify Prop. 3.1.

**T-17. A human-readable proof of 11/12** (UQ B7; D-02; DOSSIER §5(5a)). Write the half-page proof that Radziwiłł reportedly has (secondary source) and list its minimal imports. This doubles as human verification.

**T-18. An effective two-thirds theorem** (UQ C16; CRIT23 §8(6)). Make every o(N) in AF and LZ explicit, and extract T₀′ such that N₀ˢ ≥ 0.6·N on (T, 2T] for all T ≥ T₀′. Only such a version can be compared with zero data.

**T-19. Where Oliva's step (3) first fails** (C3 FINAL §9.4; UQ G7). Narrow the window (1.39·10¹⁷, e^{727.951332668}). Any x with θ(x) − x > (0.53 + o(1)) log x gives a failure at the largest prime ≤ x.

**T-20. Quick function-field projects** (C5 FINAL §9.4(ii)–(iv)):
- the proportion of fakes that need the full window (N₁ = 2g);
- an extension of E4 to even q and to a_v of higher order;
- the "hidden fake" horizon k* against log max|β| (example: k* = 28 with max|β| = 1.041).

### Tier 3. Hard targets that need a new idea (weaker than RH)

**H-1. A quartic μ-removal identity, giving an OpenAI-independent 7/8** (UQ B2; CON-0038; AC-03; D-19; DOSSIER §4.3 (C2)).
- *Question.* Do the angular-weight-1 quartic Kubota coefficients over ℤ[i] satisfy a μ-removal identity analogous to paper2's Gauss–Jacobi step? That would give J4: Σ_{0<N(u)≤X^h} |A_u(X)|² ≪ X^{1+h+ε} for some 1 ≤ h ≤ 10/9, hence ζ ≠ 0 on Re s > 1/2 + 3h/8.
- Ji's route with density inputs floors at ≥ 0.9898 (CON-0038).
- The concrete obstruction: explicit Fourier coefficients of n-fold metaplectic theta functions are known only for n = 2 and 3.

**H-2. The order-3 route** (UQ B3; D-13). Square-root cancellation for Möbius-weighted cubic Gauss sums with a suitable angular twist over ℚ(√−3) would give 5/6 by the short route.

**H-3. Below the current ≈0.8741 (B_tw = 0.8740585, LED-ZFR-3 corrected) in the 7/8 system** (UQ B4; DOSSIER §4.2–§4.3 (C3)). Prove one of:
- (a) a count with exponent below 2/3 for the critical simultaneous-large-value class (δ_c, x = 1/2);
- (b) the plain fourth moment at κ < 13/18;
- (c) a direct estimate that breaks B(ℓ) = 11/12 − ℓ/4. Without (c), the system cannot go below 2/3 (Observatory sketch).

Liu's "optimality" is the optimum of a fixed inequality system, not a bound on the method.

**H-4. A sub-diagonal sextic Möbius mean square** (UQ B1; DOSSIER (C1)).
- *Statement.* For some fixed h < 1, Σ_{0<N(u)≤D^h} |Σ μ(𝔫)ν(𝔫)(u/𝔫)₆ W(N𝔫/D)|² ≪ D^{1+h+ε}. It gives Re s > 1/2 + 5h/12.
- It lies beyond the large-sieve barrier: any proof needs cancellation between the dual diagonal and the off-diagonal terms.

**H-5. Beyond the bandwidth-one ceiling** (UQ C1, C2, C3; LED-CRIT-10; D-07). Prove liminf N₀ˢ/N > 0.6819 unconditionally. Any proof needs input beyond Fourier support [−1, 1]: for example, any unconditional upper information on the all-zeros form factor F(α) for some α > 1, even averaged over [1, 1 + δ].

**H-6. Positivity on a window containing a prime, without computer certification of the continuum infimum** (UQ D1, D2; `missing_lemmas.md` ML-R1a; C5 ML-C1; D-28).
- *Statement.* Pos(L₁) holds for some L₁ > (log 2)/2.
- *Natural instance:* Connes–Consani Conjecture 4.1 at q = 3, i.e. the window Pos((log 3)/2) = Pos(0.549). It includes identifying ker u(F)₂₂ with the semilocal Sonin space for F = {∞, 2}.
- Zhu's unrefereed Pos(0.8) already covers this window numerically. The content of the problem is the mechanism.

**H-7. The Guth–Maynard bottleneck** (UQ H1; LED-ZDE-1; D-36). For 1-bounded Dirichlet polynomials, prove |W| ≤ N^{9/10−δ} at σ = 7/10, T = N^{13/10}. This gives sup A < 30/13 and primes in all intervals of length x^{17/30−δ″}.

**H-8. Small gaps under RH alone** (UQ C12). Prove μ ≤ 1/2 − δ for an explicit δ > 0, assuming only RH. This would refute the strong Alternative Hypothesis without assuming Siegel zeros.

**H-9. A converse semi-local Li theorem** (UQ F1; LED-POS-5; PAPER-0600).
- *Statement.* λ₁, …, λ_N ≥ 0 implies no zero with β ≠ 1/2 and |γ| ≤ c√N, up to logarithms.
- It would repair Brown's Theorem 2 and make Li positivity a two-way finite detector.

**H-10. Classical records** (UQ H2, H3, H4).
- DH for σ ≥ 25/32 − δ.
- A zero-free region beyond the Vinogradov–Korobov shape.
- μ(1/2) ≤ 13/84 − δ. For δ ≤ 6.4·10⁻⁴ it suffices to show Σ_{m∼M} m^{−it} ≪ M^{1/2}T^{13/84−δ+ε} for T^{0.4054−3.3δ} ≤ M ≤ T^{1/2}.

**H-11. Conjecture G** (UQ B8; CON-0037; AC-02; D-20).
- *Statement.* Every unitary Hecke character of ℚ(√−3), of any infinity type, has no zeros on Re s > 11/12.
- *Load-bearing step:* Prop. 3.1 at angular frequency m = l − 1. It is conditional on the unrefereed 11/12 mechanism.
- It would give the first fixed zero-free half-plane for a holomorphic GL(2) newform of weight ≥ 2, e.g. L(E, s) for y² = x³ + D.

**H-12. Limits of the Siegel method** (UQ H7, H8; SIEGEL §7–§8).
- Reach c ≥ 1/5 by a comparison of the type of Guo's Lemma 5.1, or prove that the present shape caps c at 3 − 2√2 ≈ 0.1716.
- Extend interpolation-determinant exclusion to GL(2), to Rankin–Selberg L-functions, or to quadratic Hecke characters over K ≠ ℚ.

### Tier 4. RH-equivalent or conceptual targets (model cases only)

- **R-1. ML-W** (C5 FINAL §5). A positivity space E with effectivity. It is equivalent to RH, and all the content is in effectivity.
- **R-2. ML-W0** (C5 FINAL §5; UQ D9; D-35). A Riemann–Roch inequality on the square of the scaling site that re-derives the known Pos((log 2)/2). No definition of H⁰ exists yet. It makes no RH claim, but would be the first positivity on Spec ℤ that comes from effectivity.
- **R-3. EFR** (C5 FINAL §5). An explicit L₀, and an RH-free proof that Pos(L₀) ⇒ RH.
  - Such an L₀ exists non-constructively (C5-ADJ-LOG).
  - The proof must use prime-side structure (C5-ADJ-MODEL).
  - Certifying Pos(L₀) costs about 5.4·e^{2L₀} digits.
- **R-4. Connes' semilocal hypotheses (H1) and (H2)** (UQ D3, D4; LED-OPS-9; `missing_lemmas.md` R1 W-b).
  - A simple, isolated, ι-even lowest eigenvalue of QW_λ for all large λ.
  - Convergence of the normalized ground states.
  - A lower Fuchs ladder, uniform in λ, with the prime terms included. The existing estimates assume QW_λ ≥ 0, which is circular.
- **R-5. ML-Den, ML-TP, ML-F1** (C5 FINAL §5; UQ D10, D11).
- **R-6. de Branges and Suzuki positivity.**
  - An RH-equivalent, not merely sufficient, positivity condition on H(E_ξ), E_ξ = ξ + ξ′, that survives the one-off-line-pair test (UQ E5).
  - Suzuki's canonical system extending to [0, ∞) for some ω < 1/2, which is QRH-equivalent (UQ E4).
- **R-7. The host open cuts H1–H6 in their full forms** (`frontiers/missing_lemmas.md` §H; BRG statuses). These are RH-equivalent. The useful sub-lemmas are UQ J1–J10.

---

## 3. Where to start: files and tools

| Task | Read first | Code to reuse | Data and outputs |
|---|---|---|---|
| Any zeta-zero computation | `experiments/reproducibility.md` (EXP-0001) | `experiments/code/zeros_arb.py` | `experiments/results/zeros/zeta_zeros_1_100000_arb.tsv.gz` and `SHA256SUMS` |
| Li coefficients (V-11, T-1) | C1 FINAL §3.1; C2 FINAL §3.7, §5 (pitfall A2) | `experiments/code/C2-countermodel-zoo/adjudicator/adj_li.py`; `.../C1-detection-horizons/adjudicator/adj_numbers.py` | `experiments/results/C2-countermodel-zoo/adjudicator/adj_li.json` |
| Certified Jensen thresholds (V-12, T-3) | C1 FINAL §2b, §3.3 | `.../C1-detection-horizons/adjudicator/adj_farmer_x10.py`; `jensen_root_certify.py` | `.../results/C1-detection-horizons/adjudicator/adj_farmer_x10.json` |
| Certified zeros and zero counts for countermodels (V-13) | C2 FINAL §1 (A1), §3.6 | `.../C2-countermodel-zoo/adjudicator/adj_dh_count.py` (exact corners), `adj_epstein_rouche.py`; `zoo_common.py` (Krawczyk) | `.../results/C2-countermodel-zoo/adjudicator/SHA256SUMS` |
| Countermodel screen for a proof step | C2 FINAL §4; C3 FINAL §6 | `property_matrix_adjudicated.csv` (C2 adjudicator results) | — |
| de Branges condition and S(t) at zeros (V-14, T-4) | C3 FINAL §3.2–§3.3 | `.../C3-failure-anatomy/adjudicator/adj_debranges_S.py`, `adj_debranges_highblocks.py` | `adj_debranges_S_K100000.json`; failing-index hash d8dfc93c… |
| Exact Mertens and Liouville values | C3 FINAL §8 | `adj_mertens_point.py`; `liouville_mertens_sieve.py` | — |
| Weil-window margins and witnesses (V-15, T-5 to T-7) | C4 FINAL §3.2–§3.5 | `.../C4-weil-window-locality/weil_core.py`, `detect_lib.py`, `thmB_bound.py`; adjudicator `adj_thmB_arb.py`, `adj_Cdelta.py`, `adj_witness.py` | `.../results/C4-weil-window-locality/adjudicator/*.json`, `manifest_adjudicator.json` |
| Function fields (V-20, T-20) | C5 FINAL §3.2–§3.6 | `ff_fake_census.py`, `ff_common.py` (code flaw, §4.5); adjudicator `adj_exact_checks.py`, `adj_window_fibre.py`, `adj_model_window.py` | `.../results/C5-function-field-transfer/adjudicator/SHA256SUMS` |
| Quasi-RH identity checks (T-16, T-17, V-18) | DOSSIER §1.2; `audits/quasi_rh/ARCHITECTURE.md`; `audit_S*.md`, `audit_APP*.md` | `experiments/code/quasi_rh/`; `audits/quasi_rh/architecture_checks/` | — |
| The 2026 claims (V-3 to V-7, V-10) | CRIT23 and SIEGEL dossiers; `adjudication_*.md` | `experiments/code/claims_2026/{crit23_*, siegel_*}`; `audits/claims_2026/CRIT23/checks/`; `audits/claims_2026/SIEGEL/architecture_checks/` | — |
| Lean (V-1 to V-4) | `audits/lean_replay/README.md`; DOSSIER §1.3 | none: permission needed | — |
| Literature updates | `methodology.md` §10; `quality/limitations.md`, "How to extend" | `tools/harvest_arxiv.py`, `harvest_zbmath.py`, `build_pool.py`, `build_candidates.py`, `verify_seeds.py`, `select_corpus.py`, `make_records.py`, `crossref_updates.py`, `build_graph.py`, `consolidate_ledger_bridge.py` | `corpus/*.csv`, `*.jsonl`; `graphs/` |
| Full text | §4.1 | `tools/fetch_arxiv_text.sh` (PDF + pdftotext); `tools/fetch_url_text.sh` | cache under the session scratchpad |
| Lookup | `theorems/notation_dictionary.md`; `graphs/graph_schema.md` | — | `theorems/theorems.jsonl`, `proof_dependencies.jsonl`; `graphs/knowledge_graph.jsonl` (12,589 lines); `frontiers/ledger.jsonl`; `connections/*.jsonl`; `audits/findings.jsonl` |

---

## 4. Known pitfalls

### 4.1 Text extraction and record errors

- **pdftotext corrupts formulas.** It renders \frac{1}{2} as "12" and drops overlines and conjugation bars. The Observatory's own Level-1 reader recorded Ng–Shen–Wong's hypothesis as "k ≥ 12" instead of k ≥ 1/2 (FND-0008).
  - `tools/fetch_arxiv_text.sh` uses `pdftotext -layout`.
  - For anything load-bearing, fetch the arXiv e-print (LaTeX) source and cite line numbers, as the audits do ("paper2.tex l.N").
- **OCR of historical scans garbles formulas** (GDZ, Numdam, Internet Archive). The displayed bounds of Bombieri's Séminaire Bourbaki 430 were lost (C5 FINAL §1 row 11). Pre-1950 Level-1 records are mostly partial (`quality/evidence_audit.md` §4).
- **Triage summaries can be wrong.**
  - Brent 1979 verifies 75,000,001 zeros, not 81,000,001.
  - Odlyzko 1987 works near height 2.7·10¹¹, not 10²⁰ (`quality/evidence_audit.md` §3).
  - 260 triage records carry `model_knowledge_unverified` content. Never cite them as readings.
- **Level-1 records are extraction-level evidence**, produced by a lighter model (`methodology.md` A.4). Re-check at Level 2 before relying on one.
- **Ledger values.** Use the verifier's correction: 52 of the 232 records were corrected. Example: the 1300-fold Robin improvement is in log N, not in log log N (LED-ARITH-1).
- **Citation drift.** Check what a cited paper actually proves. Connes 1999 Thm 5 holds in positive characteristic only (FND-0006).

### 4.2 Countermodel tests, mandatory before trusting any step

- **Run every step on the zoo** (C2 FINAL §3–§4; C3 FINAL §6, items 2, 3 and 18):
  - the Davenport–Heilbronn function, zero 0.80851718245663738555 + 85.69934848537759217193i;
  - the Epstein function of x² + 5y² (lowest off-line zero at height 15.6682495…; zeros with Re s > 1 at t ≈ 1193.946);
  - ζ₁₉ (Re ρ = 1.0010955… near t = 600884.2);
  - F_c = M10 (zeros on Re s = log₂ a; with c = 2^{3/4} + 2^{1/4}, the first is at 0.75 + 4.5324i);
  - ξ̃ with injected quadruples;
  - H_t for t < 0;
  - Farmer's X_j.
- **Write the step's inputs as the predicates P1–P11** (C2 FINAL §4).
  - If one zoo member satisfies all of them, the step cannot be the RH-deciding step (meta-lemma C2-24, THEOREM).
  - A valid proof must use some predicate in Missing(W) for every RH-false W. Since Missing(M10) = {P4, P5, P8}, "uses the Euler product" is not enough.
- **The structural blind spot.** A step that uses all the Selberg-class axioms cannot be tested by any zoo member, because an RH-false member would refute Selberg's GRH conjecture.
- **Hamburger caveat.** Degree 1, conductor 1 and the functional equation together force cζ. The meta-lemma therefore bites only on steps that do not use both.
- **Proves too much?** Re-run the argument at ρ₁ = 1/2 + 14.1347…i and on perturbed zero sets (C3 checklist item 3).
- **Some properties cannot force real zeros.**
  - Turán inequalities, log-concavity in √v and large-shift Jensen hyperbolicity cannot (C2-14, C2-ADJ-6, Rodgers–Tao).
  - Any heat-flow argument must fail for every t < 0.

### 4.3 Finite-horizon traps

- **Implication horizons** (C1 FINAL §4). RH(T₀) already implies:
  - λ_n > 0 for n ≤ 9.0·10²⁴;
  - Jensen hyperbolicity for d ≤ 9.0·10²⁴;
  - the Schoenfeld bounds for x ≤ 1.10·10²⁶;
  - Λ ≤ 0.2, together with unconditional theory.

  A computation inside these ranges is a logical consequence of RH(T₀). Robin, Nicolas, Mertens and Nyman–Beurling have no proved implication theorem; they are uninformative beyond T₀ only heuristically.
- **Single-defect scales are model statements** (HEURISTIC). A configuration of several defects with adversarial phases could fail earlier (C1-L4).
- **Sufficient or plausible conditions that are false:**
  - de Branges (3.1), (3.3), (3.7), (3.8) (Conrey–Li; FND-0013);
  - Mertens: |M(x)| < √x holds up to 10¹⁶, yet limsup M(x)/√x > 1.826;
  - Pólya holds below 906,150,257; Turán's T(x) holds to 7.2·10¹³;
  - Oliva's step (3) holds up to 1.39·10¹⁷ and fails infinitely often (C3-ADJ-O2).
- **Finite windows.**
  - "Over ℚ no finite window suffices" is false as stated (C5-ADJ-LOG). Its real content is that no explicit L₀ is known, plus C5-ADJ-MODEL.
  - Every bounded family of windows is blind to an explicit, astronomically thin neighbourhood of the line (C4-ADJ-BLIND). Controlling every off-line zero needs an unbounded family.
  - Under H1, window positivity adds single-defect information beyond T₀ only for L > 6.49 (δ = 0.49) (C4-ADJ-INV). The certified window is 0.8.
- **Galerkin and Rayleigh–Ritz values are upper bounds.** The C4-P values sit 0.3–6% above the infimum, and a positive Galerkin upper section is not a lower certificate (host AGENTS.md).
- **Density and proportion statements, even 100%, are blind to o(N) off-line zeros** (CRIT23 §7.5; CON-0030; OB-15).
- **Censuses.** No finite zero census can establish RH, though one can refute it (SP-8). The census of fakes over F_q (C5) is not evidence about ℚ.
- **Fitted trends.**
  - C1-L3 replaced λ_n by a trend surrogate in 60 of 63 cases (disclosed).
  - C3-ADJ-RATE is a conjecture extrapolated from blocks up to n = 10¹⁰.

### 4.4 Conditional citations: carry the condition

- **Literature results:**
  - Andrade–Keating Thm 1 and §5.3 rest on their Conjecture 5 (FND-0007).
  - Ng–Shen–Wong's eighth moment is conditional on RH and a quaternary additive divisor conjecture (FND-0008).
  - Bombieri 2000 Thm 12 has an unspecified O(1), so it does not by itself certify the whole log 2 window (C4 FINAL §2a).
- **The quasi-RH family:**
  - The refinements below 7/8 import the 7/8 analytic inputs. Liu's all-field result also imports another unreviewed OpenAI preprint (DOSSIER §1.5).
  - The consequences table in DOSSIER §3 is an Observatory sketch. Its Linnik exponent 8/3 + ε is corrected in UQ H5 (CON-0001, CON-0016): q^{12/5+ε} from refereed density inputs, or 7/3 + ε with CGL.
- **Formalizations and computations behind the 2026 claims:**
  - Lamzouri's Lean certifies Thm 1.1 assuming BGSTB24 Lemma 5 and N(T) ∼ (T/2π) log T as hypotheses. Knausgård's Lean adds three axioms asserting that search programs returned true (CRIT23 §1).
  - Banks's all-q constant depends on Lu–Zaman–Zhao (refereed, unreplayed; FND-0010).
  - Zhu's Pos(0.8) is unrefereed and was computed in non-interval mpmath with an error budget.
  - Λ ≤ 0.2 rests on Polymath15 Table 1 row 2, whose canopy step Polymath describes as one they "expect to be able to verify" (C1 FINAL §2a).
- **Campaign statements:**
  - C2-17(a) is CONDITIONAL on ζ having finitely many off-line zeros. C2-14 depends on Csordas–Varga 1988, read only at L0+.
  - C4-B, C4-ADJ-C and C4-ADJ-INV are conditional on H1 and on Trudgian's S(t) bound, read only at L0+.
  - C1-N2 rests on RH and the BDBLS asymptotic, and is non-effective.

### 4.5 Numerical pitfalls (each one occurred in this archive)

- **High precision is not certification.** Label every number as an Arb ball, an exact integer, or floating point (C3 checklist item 15).
- **Tail models.** Omitting the boundary term −g_n(T*)S(T*) caused an error of 0.91 in λ_100000 (C2 FINAL, A2).
- **Contour closure.** Floating-point boundary points a + (b − a)j/n failed to close a corner. A winding enclosure that excludes every integer is the warning sign (C2 FINAL, A1).
- **Library and precision traps** (C2 FINAL §5):
  - rounding Jensen polynomials to 60 digits fabricated non-real roots at d = 100;
  - `acb_series` truncates silently at its default length;
  - importing a module reset `flint.ctx.prec`;
  - complex128 evaluation of ζ₁₉ at t ≈ 6·10⁵ has a residual floor near 10⁻¹⁰.
- **Interpolation flipped a sign.** Linear interpolation of λ_n gave a negative value at n = 7395, where the true value is +1.87 (C2 FINAL §5).
- **C1 solver and precision traps** (C1 FINAL §6):
  - mpmath `polyroots` at 400 digits did not finish;
  - `findroot(..., solver='anderson')` failed on the Li amplitude crossing;
  - a = −log|1 − 1/ρ₀| underflows for T ≥ 10¹⁰⁰ (use log1p);
  - float64 artefacts appeared in Lemma A near γ ≈ 10⁷.
- **Arb cannot decide |α| = √q.** Classify through x = α + q/α instead (C5 FINAL §7).
- **Bases with too little resolution show nothing.** The B-spline row at T = 50, L = 2 illustrated nothing (C5 FINAL §7).
- **Printed zero midpoints.** EXP-0001 prints midpoints to 25 significant digits, so the certified enclosure is [mid − rad − 5·10⁻²¹, mid + rad + 5·10⁻²¹] (`experiments/reproducibility.md`).
- **A code flaw.** In `ff_common.py`, `positivity_all_degrees` gives up before the cheap exact screen for B_d (C5 FINAL §7).

### 4.6 Process and bookkeeping pitfalls

- **Stale index.** `proposals/independent_campaigns/README.md` predates the C2, C4 and C5 adjudications.
- **`audit_level` in `corpus/bibliography.jsonl` reflects only the Level-1 pipeline.**
  - Works audited at Level 2 show L0/L0+: Alpöge–Furman PAPER-0486 (L0+), OpenAI 11/12 PAPER-0161 (L0), Lamzouri PAPER-0533 (L0).
  - Works read by campaign adjudicators also show L0/L0+: Platt–Trudgian 2016 PAPER-0571 (L0), Johnston PAPER-0917 (L0+).
  - Several 2026 records lack an arXiv id (PAPER-0164, -0165, -0166, -0533), so lookups by arXiv id miss them.
  - Some works read by campaigns are not in the corpus at all: Zhu arXiv:2608.24827, Sra arXiv:2611.02944, Danesh arXiv:2611.10726, Suzuki arXiv:2610.41115.
  - Check `audits/` and the campaign headers before treating a work as unread.
- **Count discrepancies.** Level-1 attempts are 231 and no-access cases 77 in `quality/coverage_report.md`, against 232 and 78 in `quality/evidence_audit.md` and `limitations.md`.
- **Materialized reports.** The C2, C4 and C5 REPORT.md files were rendered from structured returns (`methodology.md` A.5): the content is the agents', the formatting is scripted.
- **Hardcoded scratchpad paths.** C1's `common.py` sets `SCR` to a session scratchpad, and the C2, C3 and C5 commands use `$ZD` or `$D`. Rebuild the split zero files first (§6.0).
- **Do not overwrite archived outputs when re-running.** Some scripts write into `experiments/results/`. Copy them, redirect output where an argument allows it, and compare hashes.
- **Correlated verification.** Producers and verifiers are related models. Agreement among agents that share a prompt is not independent evidence (`methodology.md` §6(ii)).
- **Reviewed records are not rewritten.** A repair receives a new identity, and claim IDs are never recycled (host AGENTS.md).

### 4.7 Wording pitfalls

These are misreadings to avoid (`proposals/ranked_research_directions.md` §5).

- **Quasi-RH.** It says nothing about Re s = 1/2. It gives neither DH for σ ≤ Θ, nor Lindelöf on the line, nor Bombieri–Vinogradov beyond level 1/2, nor better short-interval exponents (DOSSIER §3).
- **Two thirds.** It is a lim inf density statement, and gives nothing at any finite height.
- **Siegel exclusion.** It concerns real zeros near s = 1 only. It is not Chowla's conjecture, says nothing about complex zeros, and leaves Linnik's constant unchanged (CON-0027).
- **"Optimality" (Liu)** means the optimum of a fixed inequality system. **"Lean claimed"** does not mean replayed. **"Possibly new"** in a campaign file is a search-limited label (C1-J2, C4-B).
- **Host distinctions** (AGENTS.md):
  - fixed-P61 control is not growing-prime control;
  - a positive Galerkin upper section is not a lower certificate;
  - a family identity is not principal-member extraction.

---

## 5. Verification protocols to reuse

- **P-1. The three-stage campaign** (C1–C5).
  - An investigator, an independent skeptic and an adjudicator, each with their own code, and every output hashed.
  - The adjudicator re-verifies all hashes and writes a FINAL.md containing a disagreement-resolution table, a final-status claims table, negative knowledge, reproducibility commands and next steps.
  - Use this for any new campaign.
- **P-2. Finding classes and the witness rule** (`methodology.md` §6).
  - Seven classes.
  - An alleged error needs an explicit witness, produced independently of the agent that raised it.
  - Published errata are reported as such.
  - Unverified items stay in `unresolved_findings.md` and are never publicly characterized.
  - Model of scoped public wording: FND-0003.
- **P-3. The Level-2 section audit** (`audits/quasi_rh/`).
  1. An architecture map (`ARCHITECTURE.md`) lists the load-bearing points.
  2. One auditor per section.
  3. Numerical identity checks with negative controls: positive tests at relative error ≤ 4·10⁻¹⁵, and negative controls that must fail.
  4. A dossier separating what was proved, what was audited, and what was imported but not re-proved.
  5. The adversarial round (still missing there).
- **P-4. Two-sided adjudication of flags** (`audits/claims_2026/*/adjudication_*.md`; `audits/L2_flag_audits/`). Each flag ends as not_an_issue, repaired, or verified_error with a witness.
- **P-5. Certified numerics.**
  - Krawczyk tests (C2-01) and Rouché–Cauchy discs for isolated zeros.
  - Argument-principle counts with exact corners, plus certified sign changes on the line, for completeness (214 = 204 + 2·5).
  - The monotonicity lemma C1-ADJ-MONO, which turns one certified pair into an all-d statement.
  - Three independent implementations for counts (C3).
  - Interval covers in log T for margins (`adj_thmB_arb.py`).
  - Exact-rational test functions for certified negativity (`adj_witness.py`).
  - Exact integer arithmetic over finite fields (C5).
- **P-6. Classify before computing** (C1 FINAL §4, reading guide). Before any criterion computation, compute its implication horizon from RH(T₀) and its single-defect scale. A computation inside the implication horizon is not evidence.
- **P-7. The pre-review filter for claimed proofs, human or AI** (D-08): the countermodel and hitting-set screen (C2 FINAL §4), then the 20-item checklist (C3 FINAL §6; `history/abandoned_approaches.md` §20).
- **P-8. The Lean replay procedure** (`audits/lean_replay/README.md`; DOSSIER §1.3). *Needs permission.*
  1. Pin the toolchain and the manifest, and verify the lakefile patches.
  2. `lake build`.
  3. `comparator` with `lean4export`, and an independent kernel.
  4. `#print axioms`.
  5. A human review of statement fidelity.
  6. Record the hashes of all artifacts.
- **P-9. Literature verification.**
  - One drafting agent per area, and an independent skeptic for every record.
  - Ledger verdicts: confirmed_fulltext, confirmed_abstract_or_secondary, corrected, superseded_by_newer, rejected.
  - Bridge verdicts: confirmed, confirmed_with_correction, relation_overstated.
- **P-10. Headers and frozen identities.**
  - Every file opens with the five-field block.
  - Sources are pinned by SHA and hash.
  - A repair gets a new id, and nothing is strengthened silently (host AGENTS.md).

---

## 6. Executable continuation plan

### 6.0 Environment (first 30 minutes)

```bash
OBS=/home/user/riemann/research/exploratory/riemann-observatory    # adjust to your checkout
cd "$OBS/experiments"
sha256sum -c results/zeros/SHA256SUMS                  # EXP-0001; the file records an absolute path
(cd results/C2-countermodel-zoo/adjudicator && sha256sum -c SHA256SUMS)
(cd results/C5-function-field-transfer/adjudicator && sha256sum -c SHA256SUMS)
# C1, C3 and C4 adjudicator hashes: results/<campaign>/adjudicator/manifest_adjudicator.json
ZD=<your scratch directory>/data; mkdir -p "$ZD"
zcat results/zeros/zeta_zeros_1_100000_arb.tsv.gz | head -n 50000  > "$ZD/zeros_1_50000.tsv"
zcat results/zeros/zeta_zeros_1_100000_arb.tsv.gz | tail -n +50001 > "$ZD/zeros_50001_100000.tsv"
sha256sum "$ZD"/zeros_*.tsv   # compare with 6a7eb7ab...cc88 and 494b5c10...5e5a (C3 and C5 FINAL headers)
```

- If the two hashes differ (the session copies may have had a different column format), regenerate the files with `python3 code/zeros_arb.py 1 50000 …` and `python3 code/zeros_arb.py 50001 50000 …` at 96 bits (about 1059 s and 1283 s).
- Then point C1's `common.py` (variable `SCR`) and the `$ZD` / `$D` arguments at your directory.

### 6.1 Cheap end-to-end checks (under 10 minutes of compute)

Run these before anything else. Redirect output where the script takes an output argument; where it does not, run from a copy.

- **C1:** `adjudicator/adj_numbers.py` (0.13 s). Its output should hash to 35acfbaf0de771b46d09e7360ad57aae968e2a8b5c3b6c01554fa9c706d78eb2 (`manifest_adjudicator.json`).
- **C2:** `adjudicator/adj_side_checks.py <out-dir>` (3 s): the F_c functional equation and the BST threshold. Compare with `adj_side_checks.json` (8ced43c0…).
- **C5:** `adjudicator/adj_exact_checks.py` (11 s). Read its usage line first.
- **C3:** `adjudicator/adj_debranges_S.py 100000 20000 <zeros> <out>` (261 s). Recompute the sha256 of the comma-joined failing indices; it should be d8dfc93cbb3c2bbaa063ad57d960e778cdbb414dee1b6776738c840ec77ef65c. This is the cheapest end-to-end check of C3-ADJ-S.

### 6.2 Level-1 reading queue, ordered by what each item unblocks

Read the LaTeX source where it exists, and record the sha256 of every text read. Add Level-1 records as new entries; do not overwrite reviewed records.

| # | Work | Corpus id and level | Unblocks |
|---|---|---|---|
| 1 | Trudgian 2014, bound for S(t) (arXiv:1208.5846) | PAPER-0570, L0 | The one imported input whose failure would invalidate C4-B, C4-B2, C4-ADJ-C and C4-ADJ-INV (C4 FINAL, gap (c)) |
| 2 | Zhu, arXiv:2608.24827v2 | not in corpus | V-8; the C4-ADJ-BLIND numbers; LED-POS-7 |
| 3 | Brown 2005, Li's criterion and zero-free regions | PAPER-0600, L0 | H-9; C1 §8.6 |
| 4 | Yoshida 1992; Bombieri 2003 (variational approach) | PAPER-0667, L0; PAPER-0491, L0+ | primary source of Pos((log 2)/2); C4 §6.7 |
| 5 | Burnol, math/0203120 and math/0103058 | PAPER-0673, L0; PAPER-0606, L0+ | completeness of Sonine systems against window size; C1-N2 |
| 6 | Csordas–Varga 1988 (Zbl 0696.30007); Craven–Csordas–Smith 1987; Csordas–Norfolk–Varga 1986 | first not located in the corpus; PAPER-0523, L0+; PAPER-0583, L0 | the imported inputs of C2-14, C2-17(a) and C2-ADJ-6; prior art for Turán at t = 0 |
| 7 | Bateman–Grosswald 1964 | not in corpus | prior art for C2-ADJ-2 (V-16) |
| 8 | Liu–Wu, arXiv:2503.24275 | not in corpus | V-16(b) |
| 9 | Montgomery 1983; Odlyzko–te Riele 1985 | PAPER-0660, L0; PAPER-0199, no access | C3 primary texts (C3 §9.7) |
| 10 | Chassé 2013; Oesterlé 2000 typescript | PAPER-0871, L0; not in corpus | C1 primary-source gaps (C1 §8.6) |
| 11 | Weil 1948, Weil 1952 (explicit formulas), Laumon 1987 | PAPER-0176, L0+; PAPER-0473, L0; PAPER-0596, L0 | C5 ingredients now cited only via Milne (C5 §9.6) |
| 12 | Sra, arXiv:2611.02944 | not in corpus | local PF and Laguerre criteria (C1-ADJ-LOCAL; C1 §8.7); host XI_PICK programme |
| 13 | Danesh arXiv:2611.10726; Suzuki arXiv:2610.32704 and 2610.41115; Andrews–Connes–La Gatta (PAPER-0544) | not in corpus / L0 | related work for C4 and C5 |
| 14 | OpenAI 7/8 manuscript | PAPER-0528, L0 (structure read in DOSSIER) | V-18 |
| 15 | Ji arXiv:2611.16665; de Faveri arXiv:2610.04045 | PAPER-0155, L0+; not in corpus | the only QRH route independent of OpenAI (V-21) |
| 16 | X.-J. Li, arXiv:0807.0090 v5–v10 | PAPER-0885, L0+ | V-19 |
| 17 | Ki–Lee 2012 (Funct. Approx. 47, Thm 5) | not checked | CRIT23 F2: the pre-2026 distinct-zero baseline |

### 6.3 Lean replays (only with explicit user permission, in an isolated environment)

| Target | Repository and pin | Toolchain | What to run | Extra check | Source |
|---|---|---|---|---|---|
| Quasi-RH 7/8 (ζ, Dirichlet, Hecke) | github.com/openai/math @ 4eaee87548250b2682affda7d05d947c05554bae, `lean/` | v4.34.1; Mathlib d13f23b7… | `lake build` of `OAI.NumberTheory.DirichletL.Nonvanishing` and `...Hecke.Nonvanishing`; comparator + lean4export on the three challenge JSONs; nanoda; `#print axioms` | V-2 fidelity of the Hecke statement | `audits/lean_replay/README.md` |
| Siegel zeros (OpenAI) | same | same | `OAI.NumberTheory.SiegelZeros.Main`; `comparator ComparatorChallenges/SiegelZeros.json` with nanoda | read the 642-line chain-A assembly | SIEGEL §8(2) |
| Kimura | cln-imq-2k @ e66ab86 | per repository | `B4.Chi8.zero_gap_all` | gives c = 5.811·10⁻⁴ | SIEGEL §8(2) |
| Alpöge–Furman | anthropics/zeta-23-lean, tag v1.0 | v4.33.0-rc2; Mathlib 51e6992efd06 | `#print axioms` on the three main theorems; comparator against `Multiplicity.lean` | finding F5 | CRIT23 §8(2) |
| Lamzouri | github.com/AxiomMath/ZetaZerosV2 | per repository | Thm 1.1 | record the two hypotheses it assumes | CRIT23 §1 |
| Knausgård | github.com/kristianmk/839 (and arXiv ancillary files) | per repository | build; list the three run-axioms | replace them by V-6 | CRIT23 §1 |
| Cureton–Thorner | AxiomProver development ("CTLean") | — | the exact formal statement; `#print axioms` | which consumers use 1 − 1/6000 and which use 31/32 | UQ A14 |

A successful replay certifies statements relative to the kernel and Mathlib's definitions. It does not certify any paper's argument. Record the outcome, with hashes, under `audits/lean_replay/` as a new record.

### 6.4 Audits to deepen, in order

1. The 7/8 manuscript and the first adversarial round (V-18).
2. Human-review targets for paper2, in risk order (DOSSIER §5(3)):
   - the Dunn–Radziwiłł transcription of Patterson's Thm 8.1 and the Kubota multiplier, against Patterson 1977 itself;
   - Goldmakher–Louvel Thm 1.1 for the family (x/k)₂κ_λ^{e_k};
   - the multiplier case analysis at l.3175–3196, and Lemma 6.3;
   - the constants of Lemma B.2.

   Agents can prepare an exact-SHA review packet; the review itself needs a human expert.
3. The CRIT23 residues V-5, V-6 and V-7. Then F2 (Ki–Lee), and the out-of-scope items AF Thm B, Rem. 7.1–7.2 and KN §7 (CRIT23 §8).
4. Siegel: the κ = 1/2 variants, pinned with hashes, and one core to version-of-record standard (D-03; Guo Prop. 3.1 is the shortest).
5. V-21: Ji and de Faveri; Cureton–Thorner; Li–Liu; Yang–Yang.
6. Live proof claims (V-19).
7. Sra arXiv:2611.02944, placed in the C1 implication/detection framework (C1 FINAL §8.7). Danesh arXiv:2611.10726, compared with C4-B (C4 FINAL §1 row 2).
8. Resolution of FND-0005 and FND-0011 (V-17, V-9).

### 6.5 Theorem attempts, in order

- **Order:** T-1, T-2, T-4, T-5, T-8, T-9, T-10, T-11, T-12, T-3, T-13. Attempt Tier 3 only with a specific new input in hand.
- **First deliverable for each:** a statement file with the five-field header, the exact quantifiers, and the smallest statement whose failure would invalidate it.
- **Before any draft circulates,** run P-7 on it.

### 6.6 Record maintenance (one batch; add notes and new records, do not rewrite reviewed ones)

- Update `proposals/independent_campaigns/README.md` to reflect five adjudications.
- Propagate the §0.3 table into these files:
  - `actionable_conjectures.md`: AC-15, -19, -20, -21, -28;
  - `ranked_research_directions.md`: D-16, D-23, D-29, D-33, §3, §5;
  - `unsolved_questions.md`: D5, D6, I2;
  - `missing_lemmas.md`: R1 (W-a), R12;
  - `known_obstructions.md`: OB-18, OB-24;
  - `strongest_connections.md`: §5.4.
- After V-16, propose findings-register entries for C2-07 and C2-ADJ-2.
- Apply, as new records, the reclassifications recommended in SIEGEL §8(8) (U2 and U3 not_an_issue; U4 narrowed) and the Lu–Zaman–Zhao citation (Math. Comp., DOI 10.1090/mcom/4268).
- Sync bibliography audit levels with audit pointers; add the missing arXiv ids; add the out-of-corpus works read by campaigns as candidates.
- Reconcile the 231/232 and 77/78 counts in `quality/`.

### 6.7 Output conventions and stop rules

- **Where new work goes.** Put new mathematics in a separately labelled proposed object, preserve inherited scope, and publish on your own branch through a PR (host AGENTS.md).
- **Stop and report** if:
  - a replay fails;
  - a zoo member satisfies every input of a step you rely on;
  - a load-bearing import cannot be read at Level 1;
  - a permission is missing;
  - the rigor class of a number cannot be established.

---

## 7. What not to do (negative knowledge)

- **Criterion computations.** Do not run larger Li, Jensen, ψ/π, Robin, Mertens, Nyman–Beurling or Λ computations as tests of RH beyond T₀ (C1 FINAL §4–§5).
- **Window locality.** Do not use "Nyquist locality" as design guidance for window families; it is REFUTED (C4 FINAL).
- **Quasi-RH routes already ruled out:**
  - order-2 row extraction left of 11/12, which is circular (CON-0014);
  - QRH from proven mollified second moments, which needs mollifier length above 1 against the proven 4/7 and 17/33 (CON-0031);
  - a generic sextic large sieve in place of the theta coefficients, which gives only the trivial bound (DOSSIER §4.3 (C4)).
- **Siegel exclusion.** Do not expect Siegel-type methods to give zero-free strips or anything about complex zeros (SIEGEL §7). Do not try to lower Linnik's L = 5 through Siegel exclusion (CON-0027).
- **Other consequences ruled out.** Do not pursue Artin's conjecture by Hooley's route from 7/8 (CON-0020), or short-interval exponents from any half-plane θ₀ ≥ 7/10 (CON-0028).
- **Positivity shortcuts.** Do not use Turán inequalities, fixed-degree Jensen, or infinite log-concavity as a proof of RH (C2-14, C2-ADJ-6, CON-0033), or heat flow "with room to spare" (Rodgers–Tao).
- **Function fields.** Do not formally transfer a function-field proof: the fakes satisfy rationality, the functional equation and an Euler product (C5-E1), and the number-field tensor-power trick is equivalent to RH (C5-D1).
- **Status.** Do not cite Pos(0.8), the 7/8 half-plane or Knausgård's constants as theorems. Do not characterize the subjects of FND-0005 or FND-0011 as errors.

