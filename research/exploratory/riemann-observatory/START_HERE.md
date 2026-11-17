# Start here: a one-day guide to the Riemann Observatory

```text
Status: READING GUIDE (exploration layer). It orders existing archive files for a researcher with one day and
        adds no result. RH is open. The 2026 claims mentioned are unrefereed:
          - quasi-RH 11/12: Level-2 audited by the Observatory with no error found; imports not re-proved;
          - quasi-RH 7/8: not audited; Lean claimed, not replayed;
          - >= 2/3 on the line: one proof step repaired (FND-0004);
          - Landau-Siegel exclusion: FND-0010.
Scope: 15 files (or file sections) in reading order, with timings, and a one-hour version.
Exact sources or dependencies: the files listed in the schedule. Their section numbers were checked against
        the files as delivered on 2026-11-17.
What was actually run: reading of every listed file and section; nothing else.
Smallest remaining gap: timings are estimates for a reader fluent in analytic number theory. The schedule skips
        the 1,000 paper records, the theorem database and the knowledge graph, which are reference material
        rather than reading.
```

## Five rules before you open anything

1. **RH is open.** No file here proves or disproves it. Finite computations carry no global implication.
2. **Precedence.** Campaign `FINAL.md` files outrank their `REPORT.md` and `SKEPTIC_REVIEW.md`. Then come the audits, the frontier ledger (always use the verifier-corrected value), the connection verdicts, the frontier and proposal syntheses, history and quality.
3. **Keep the label.** Every statement carries a status: THEOREM (with its source, or "Observatory-proved" for campaign items), IMPORTED, CONDITIONAL, NUMERICAL-RIGOROUS, NUMERICAL-NONRIGOROUS, HEURISTIC, CONJECTURE, REFUTED, or "announced, unrefereed". Keep it when you cite.
4. **Two phrases mean less than they sound.** "Lean claimed" does not mean replayed; nothing was compiled here. "No error found" means no error in the inspected portion, found by AI agents; it is not a referee report.
5. **Stale files.** These files predate the C2, C4 and C5 adjudications and are superseded where they disagree with a `FINAL.md`:
   - [proposals/independent_campaigns/README.md](proposals/independent_campaigns/README.md);
   - [proposals/ranked_research_directions.md](proposals/ranked_research_directions.md) and [proposals/actionable_conjectures.md](proposals/actionable_conjectures.md);
   - [frontiers/missing_lemmas.md](frontiers/missing_lemmas.md), [frontiers/known_obstructions.md](frontiers/known_obstructions.md) and [frontiers/unsolved_questions.md](frontiers/unsolved_questions.md);
   - [connections/strongest_connections.md](connections/strongest_connections.md).

   The superseded entries are listed in [final_synthesis/open_problems_for_future_agents.md](final_synthesis/open_problems_for_future_agents.md) §0.3.

## Schedule

### Morning, 09:00–12:30: what the archive is and what was verified

| # | File | Time | What to look for |
|---|---|---|---|
| 1 | [README.md](README.md) | 10 min | The directory map and the headline facts. Note where each register lives: FND (findings), LED (ledger), CON (connections), BRG (bridge), PAPER (corpus). |
| 2 | [executive_report.md](executive_report.md) | 25 min | §2, the counts; §3.1, the status table of the four 2026 claims; §3.3, the C1 and C4 corrections; §5, the recommendations. |
| 3 | [methodology.md](methodology.md) §5–§8 and Addendum A | 20 min | The meaning of L0, L0+, L1, L2 and L3. The seven finding classes and the witness rule §6 (i)–(iv), which governs what may be called an error. A.4, model tiering; A.5, reports materialized from structured returns. |
| 4 | [quality/evidence_audit.md](quality/evidence_audit.md), then [quality/limitations.md](quality/limitations.md) | 20 min | §1, who checked what; §3, the Observatory's self-corrections; §4, systematic risks (text extraction, OCR, model recollection, correlated agents). |
| 5 | [audits/verified_findings.md](audits/verified_findings.md) and [audits/unresolved_findings.md](audits/unresolved_findings.md) | 25 min | The column "Main theorem affected?". The allowed public wording for each finding. Why FND-0005 and FND-0011 are not called errors. |
| 6 | [audits/quasi_rh/DOSSIER.md](audits/quasi_rh/DOSSIER.md) §1.1–§1.3, §3, §4.1–§4.2, §5 | 60 min | The exact claims Q1–Q5, E1–E2, L1, and the coverage table. Which imports were not re-proved. Lean challenge fidelity, including the caveat on the Hecke statement. "What is NOT implied". The method floors β(n, h) and B(ℓ) = 11/12 − ℓ/4. |
| 7 | [audits/claims_2026/CRIT23/DOSSIER.md](audits/claims_2026/CRIT23/DOSSIER.md) §0–§1 and §7.5; [audits/claims_2026/SIEGEL/DOSSIER.md](audits/claims_2026/SIEGEL/DOSSIER.md) §0–§1 and §6–§7 | 40 min | The exact liminf statements and the FND-0004 repair. The Lean caveats: Knausgård's three run-axioms, and Lamzouri's formalization assuming two inputs as hypotheses. Why 100% would not be RH. For Siegel: the mechanism, the four proofs, the constants, the ceiling near 0.17, and what is not implied. |

### Afternoon, 13:30–17:00: the five campaigns and the ledger

| # | File | Time | What to look for |
|---|---|---|---|
| 8 | [C1 FINAL](proposals/independent_campaigns/C1-detection-horizons/FINAL.md): header, §3.1, §4, §5 | 40 min | Theorem C1-L2 (RH(T) ⇒ λ_n > 0 for n ≤ T²). The T₀ table, with its implication and single-defect columns. Which published computations are logical consequences of RH(T₀). The refuted sentence on de Bruijn–Newman. |
| 9 | [C4 FINAL](proposals/independent_campaigns/C4-weil-window-locality/FINAL.md): header, §1 rows 5–8, §3.3, §3.6 | 40 min | The refutation of the Nyquist heuristic. Detection under H1 at L ≈ (1/(2δ)) log log T (C4-B). The blindness radius (C4-ADJ-BLIND). Under H1, window positivity adds information beyond T₀ only for L > 6.49 (C4-ADJ-INV). Galerkin values are upper bounds. |
| 10 | [C2 FINAL](proposals/independent_campaigns/C2-countermodel-zoo/FINAL.md): header, §3.1, §3.3–§3.5, §4 | 30 min | The RH-false Euler product F_c (M10). Turán inequalities for every H_t. The predicates P1–P11 and the hitting-set rule. The blind spot is the full Selberg class. |
| 11 | [C3 FINAL](proposals/independent_campaigns/C3-failure-anatomy/FINAL.md): §3.2, §5, §6 | 30 min | The identity tying the de Branges condition to S(γ_n) mod 2. The failure taxonomy. The 20-item checklist for any claimed proof. |
| 12 | [C5 FINAL](proposals/independent_campaigns/C5-function-field-transfer/FINAL.md): header, §3.3 (statement), §3.5, §5, §6 | 35 min | The sharp window theorem over F_q. Why "no finite window over ℚ" is false as stated (C5-ADJ-LOG). The model theorem C5-ADJ-MODEL. The missing lemmas ML-W0, ML-C1 and EFR. |
| 13 | [frontiers/records_ledger.md](frontiers/records_ledger.md), areas VERIF, ZFR, ZDE, CRIT, DBN, POS | 35 min | Read the "Verifier verdict" column first and use corrected values. Keep "announced_unrefereed" separate from theorems. Check the history of each record. |

### Evening, 19:00–21:00: synthesis and what to do next

| # | File | Time | What to look for |
|---|---|---|---|
| 14 | [connections/strongest_connections.md](connections/strongest_connections.md) §0–§1, §4–§5 | 35 min | The ranked corrected claims (CON-0032 first), what the repository bridge does not license, and the refuted sub-claims. |
| 15 | [final_synthesis/open_problems_for_future_agents.md](final_synthesis/open_problems_for_future_agents.md) §0–§2 and §4, with the "Priority digest" of [frontiers/unsolved_questions.md](frontiers/unsolved_questions.md) | 60 min | The stale-file table. The problems sorted by tractability. The pitfalls: text extraction, countermodels, finite-horizon traps, conditional citations. |
| — | Your own notes | 25 min | Write a one-paragraph status summary with archive references and check it against the five rules above. |

The day totals 9 hours. If you have spare time, or want to go deeper:
- [history/abandoned_approaches.md](history/abandoned_approaches.md) §19–§20, the reusable quick tests;
- [history/evolution_of_methods.md](history/evolution_of_methods.md) §11–§13;
- [history/recent_developments_2024_2026.md](history/recent_developments_2024_2026.md);
- [proposals/ranked_research_directions.md](proposals/ranked_research_directions.md) §3–§5 (negative knowledge, gating, misreadings);
- [experiments/reproducibility.md](experiments/reproducibility.md).

## If you only have one hour

| Min | File | What to take away |
|---|---|---|
| 5 | [README.md](README.md), "Headline facts" | The three 2026 claims, and the fact that RH is untouched. |
| 15 | [executive_report.md](executive_report.md) §1 and §3.1 | The exact status of each 2026 claim, and what our audits did and did not check. |
| 5 | [audits/verified_findings.md](audits/verified_findings.md), the opening table | No finding affects a main theorem unless it says so. |
| 10 | [C1 FINAL](proposals/independent_campaigns/C1-detection-horizons/FINAL.md) §4, table and reading guide | Li, Jensen and ψ/π computations inside horizons of size about T₀² are logical consequences of RH(T₀). The other criteria are uninformative beyond T₀ only heuristically. |
| 10 | [C4 FINAL](proposals/independent_campaigns/C4-weil-window-locality/FINAL.md), the header Status block and §3.6 | Windows see large-δ defects at doubly-logarithmic size. Blindness is proved only astronomically close to the line. |
| 10 | [audits/quasi_rh/DOSSIER.md](audits/quasi_rh/DOSSIER.md) §3 "What is NOT implied" and §5(1) | A half-plane says nothing about Re s = 1/2. Keep the status vocabulary. |
| 5 | [final_synthesis/open_problems_for_future_agents.md](final_synthesis/open_problems_for_future_agents.md) §1 | The state of play in one table. |

