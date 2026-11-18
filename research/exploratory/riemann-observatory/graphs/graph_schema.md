# Knowledge-graph and record schemas

All machine-readable files are UTF-8 JSON Lines (one JSON object per line) unless the extension says CSV. Identifiers are stable across incremental updates (see `methodology.md` §10).

## Identifiers

| Prefix | Object | Example |
|---|---|---|
| `PAPER-####` | selected corpus work | `PAPER-0001` |
| `CAND-#####` | candidate considered for the corpus (selected or not) | `CAND-00042` |
| `THM-PAPER-####-k` | theorem/lemma/definition/criterion extracted from a paper | `THM-PAPER-0123-2` |
| `LED-<AREA>-k` | frontier ledger record (current best results) | `LED-ZFR-3` |
| `FND-####` | audit finding | `FND-0007` |
| `CON-####` | proposed cross-paper connection | `CON-0012` |
| `OBS-####` | known obstruction / barrier | `OBS-0004` |
| `BRG-<PROG>-k` | repository-literature bridge item | `BRG-ROBIN-2` |
| `EXP-####` | experiment | `EXP-0003` |
| `TECH:<slug>` | technique node | `TECH:mollifier` |
| `CRIT:<slug>` | RH-equivalent criterion node | `CRIT:li` |
| `STRUCT:<slug>` | mathematical structure node | `STRUCT:de-branges-space` |
| `AUTH:<slug>` | author node (zbMATH author code when available) | `AUTH:selberg.atle` |

## `graphs/knowledge_graph.jsonl`

Each line is either a node or an edge.

```json
{"kind":"node","id":"PAPER-0005","type":"paper","label":"Montgomery 1973, The pair correlation of zeros of the zeta function","props":{"year":1973,"families":["B"],"stratum":"S3","audit_level":"L1"}}
{"kind":"edge","id":"E-000123","src":"THM-PAPER-0005-1","dst":"CRIT:pair-correlation","type":"proves","status":"established","evidence":{"paper":"PAPER-0005","location":"Theorem 1, p. 184","evidence_level":"fulltext_read"},"confidence":"high"}
```

Node `type` ∈ `paper, author, theorem, lemma, definition, criterion, conjecture, technique, obstacle, counterexample, experiment, structure, ledger_record, finding, connection, obstruction`.

Edge `type` ∈ `cites, authored_by, proves, uses, generalizes, strengthens, requires, equivalent_to, conditional_on, contradicts, special_case_of, repairs_gap_in, suggests_route_to, improves_record, supersedes, refutes, instance_of_technique, about_structure, obstructs`.

Edge `status` ∈
* `established` — relation stated in a source that was read at L1 or higher (location given), or a standard textbook fact with citation;
* `reported` — relation taken from index content (abstract/review) or a secondary source, not checked in the primary text;
* `citation_only` — a `cites` edge from zbMATH resolved references (no claim about mathematical use);
* `speculative` — proposed by the Observatory (connections/conjectures), not established;
* `refuted` — a proposed relation that failed testing (kept as negative knowledge).

`confidence` ∈ `high, medium, low` reflects the reviewer's confidence that the edge is correctly stated, not the probability that a conjecture is true.

## `corpus/bibliography.jsonl`

Fields: `paper_id, cand_id, title, title_original, title_en, authors[], year, stratum, venue, doc_type, doi, arxiv, zbmath_id, zbl, msc[], language, families[], work_type, selection_score, in_pool_citations, seed_lists[], access{fulltext_url, open_access, format}, audit_level, record_path`.

## `theorems/theorems.jsonl`

Fields: `thm_id, paper_id, kind (theorem|lemma|proposition|corollary|definition|criterion|conjecture|conditional_theorem|computation), label_in_source, statement (normalized LaTeX), statement_original_notation, hypotheses[], conclusion, scope (finite|local|conditional|asymptotic|global), conditional_on[], location, evidence_level, normalization_notes, depends_on[] (thm_ids or citations)`.

## `theorems/proof_dependencies.jsonl`

Fields: `edge_id, from (thm_id), to (thm_id or external citation), relation (uses|requires|special_case_of|generalizes|equivalent_to), location, evidence_level`.

## `audits/findings.jsonl`

Fields: `finding_id, paper_id, location, classification (see methodology §6), claim, witness (counterexample / computation / precise step), independent_checks[], adjudication, status (verified|suspected|unresolved|withdrawn), public_characterization_allowed (bool)`.

## `connections/connections.jsonl`

Fields: `con_id, kind (hypothesis_matching|missing_lemma|transplantation|strengthening|weakening|rediscovery|compatibility|negative_synthesis|conjecture), source_theorems[], proposed_link, compatibility_checks, new_claim, already_proved, conjectural, next_step, potential_counterexamples, tests, significance (1-5), difficulty (1-5), status (proposed|tested_supported|tested_refuted|established), reviews[]`.

## `frontiers/ledger.jsonl`

Fields: `led_id, area, quantity, statement, value, status, conditional_on, source{authors,year,title,venue,arxiv,doi}, location, evidence_level, history[], caveats, verification{verdict, checked_against, correction}`.
