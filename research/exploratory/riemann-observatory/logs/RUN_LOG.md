# Run log (2026-11-17)

```text
Status: PROCESS RECORD
Scope: every orchestrated workflow and background job of the Observatory run
Exact sources or dependencies: workflow journals in the orchestrator's session store (not redistributed)
What was actually run: listed below
Smallest remaining gap: n/a
```

Times are UTC on 2026-11-17. "Agents" counts sub-agent invocations. Models: Opus 5.5 unless marked (S) = Sonnet 5.5.

| # | Workflow / job | Purpose | Agents | Outcome |
|---|---|---|---|---|
| 1 | zbMATH harvest (script) | 27 MSC/keyword queries | — | 24,876 records |
| 2 | arXiv harvest (script) | 30 phrase queries | — | 5,737 records |
| 3 | citation expansion (script) | fetch highly cited referenced zbMATH ids | — | ~1,770 records |
| 4 | Arb zero computation (script) | first 100,000 zeros | — | EXP-0001 |
| 5 | observatory-seed-bibliography | nine family seed lists | 9 | 1,422 seeds; 1,356 auto-verified |
| 6 | observatory-frontier-ledger | 12 areas: draft + verify | 24 | 232 records |
| 7 | observatory-repo-bridge | 7 programmes: map + verify | 14 | 215 items |
| 8 | observatory-campaigns-1 | C1–C5: investigate, skeptic, adjudicate | 15 | 5 FINAL.md |
| 9 | 2024–2026 literature scout (agent) | recent stratum | 1 | 140 entries |
| 10 | observatory-quasi-rh-audit | map + 7 section audits + dossier | 9 | no error found |
| 11 | observatory-triage ×3 (S) | 2,750 candidates | 28 | 1,165 includes |
| 12 | observatory-L1-reading ×4 (S) | 232 works | 58 | 108 full, 46 partial |
| 13 | observatory-triage-supplement ×3 (S) | 623 supplementary candidates | 12 | 288 includes |
| 14 | observatory-2026-claims-audit | critical line 2/3; Landau–Siegel | 13 | FND-0004, FND-0010 |
| 15 | observatory-L2-flag-audits | 8 flagged issues | 12 | FND-0001…0008, 0011 |
| 16 | observatory-discovery | 8 mechanisms + verification | 16 | 39 proposals |
| 17 | observatory-synthesis-history | timeline, methods, abandoned approaches, notation | 4 (2 S) | 4 documents |
| 18 | observatory-synthesis-wave1 | frontiers, connections, proposals | 3 | 8 documents |
| 19 | observatory-final-synthesis | final synthesis + critic | 4 | final_synthesis/, executive report, START HERE |

Blocked action: building/replaying third-party Lean code (OpenAI quasi-RH formalization) was refused by the session's safety policy; see `audits/lean_replay/README.md`.

Approximate sub-agent token totals at the start of the final synthesis: Opus ≈ 2.5·10⁹ cache-read, 7.4·10⁷ cache-write, 2.8·10⁷ output tokens; Sonnet ≈ 2.0·10⁸ cache-read, 9·10⁶ cache-write, 4.5·10⁶ output tokens.
