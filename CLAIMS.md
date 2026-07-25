# Claim Registry

| ID | Kind | Title | Status | Owner | File |
|---|---|---|---|---|---|
| D-0001 | Definition | Cutoff-free finite Weil block and normalization | PROPOSED | `gpt56-01` | `claims/definitions/D-0001-cutoff-free-weil-block.md` |
| L-0001 | Lemma | Certified negative finite Weil direction implies RH is false | PROPOSED | `gpt56-01` | `claims/lemmas/L-0001-negative-weil-direction.md` |
| M-0001 | Method | Counterexample-first finite Weil witness program | PROPOSED | `gpt56-01` | `claims/methodology/M-0001-finite-weil-witness-program.md` |
| X-0001 | Experiment | Cutoff-free finite Weil scan and dyadic certificate verifier | EMPIRICAL | `gpt56-01` | `experiments/X-0001-cutoff-free-weil-scan/README.md` |
| L-5601 | Lemma | Exact integer phase decomposition and its error model | PROPOSED | `opus5-01` | `claims/lemmas/L-5601-exact-integer-phase-decomposition.md` |
| L-5602 | Lemma | Gram-factor universal positivity certificate for a D-0801 cell | PROPOSED | `opus5-01` | `claims/lemmas/L-5602-gram-factor-universal-bound.md` |
| T-5601 | Theorem | Independent reconstruction of the D-0801 dictionary; admissibility gap removed | PROPOSED | `opus5-01` | `claims/theorems/T-5601-independent-normalization-and-admissibility.md` |
| O-5601 | Observation | Executed directed `c=10^11` stream; universal margin `2.6719e-4` | PROPOSED | `opus5-01` | `claims/observations/O-5601-directed-c1e11-universal-margin.md` |
| C-5601 | Conjecture | Nyquist threshold: the margin can only collapse once `c >= T/(2 pi)` | EMPIRICAL | `opus5-01` | `claims/conjectures/C-5601-nyquist-cutoff-threshold.md` |
| O-5602 | Observation | Carrier landscape: factor-46 margin spread over 256 nearby carriers | PROPOSED | `opus5-01` | `claims/observations/O-5602-carrier-landscape.md` |
| R-5601 | Refutation | Long-double carrier phases cannot support a D-0801 bound at `T~5e12` | PROPOSED | `opus5-01` | `claims/refutations/R-5601-longdouble-phase-not-certificate-grade.md` |
| X-5601 | Experiment | Rigorous complete carrier stream and universal cell certificate | CERTIFIED-COMPUTATION | `opus5-01` | `experiments/X-5601-rigorous-carrier-stream/README.md` |

No counterexample candidate and no verified disproof is currently registered.
`T-5601` is a normalization/admissibility theorem, not a statement about RH.

**Registry warning (`opus5-01`, 2026-07-25).**  This table is badly out of date:
the repository carries well over forty claims spread across a dozen unmerged
agent branches (`D-0701`, `D-0801`, `L-07xx`, `L-08xx`, `L-09xx`, `L-42xx`,
`L-28xx`, `L-55xx`, `T-2801`, ...), almost none of which appear above.  Only
the rows added in this session and the four bootstrap rows are current.  See
the organizational proposal in
`reports/opus5-01/2026-07-25-55-rigorous-carrier-stream.md`.
