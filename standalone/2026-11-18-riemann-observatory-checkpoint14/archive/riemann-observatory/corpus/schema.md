# Data schemas and update rules

UTF-8 JSON Lines contain one object per nonblank line. Unknown bibliographic fields remain null or absent. CSV nested values are JSON strings. Stable paper IDs use track prefixes; numeric continuity is not required. See [structured_data_schema.md](../quality/structured_data_schema.md) for the detailed field and evidence-state reference.

## Bibliography and selection

Canonical fields include id, title, authors, source_url, audit_level, whole_work_read, access_status, read_scope and record_path. Identity fields include year, date, venue, doi, arxiv, version and publication_status. Preprint and publication years remain distinct where supplied. Original *_records.jsonl tracks are retained. Access, complete reading and scoped technical verification are separate states; local theorem audits never silently promote a whole paper.

bibliography.jsonl contains selected and explicitly deferred supporting records. selection_status determines inclusion in selected counts. candidates.jsonl is a separate provider-discovered pool; candidate schemas and raw_discovery_index.jsonl preserve provenance. Search-family labels and possible duplicates are provisional, not importance judgments or verified identities. Generated metrics give current totals.

selection_decisions.csv records id, decision and reason. Pending relevance is neither selection nor rejection. An explicit candidate ID in a selected source record permits selected_via_canonical_work_record; title similarity alone does not. Original triage decisions remain in contributor files. Curated works and candidates overlap, so their counts must not be added.

## Claims, dependencies and connections

theorems/theorems.jsonl preserves id, paper_id (possibly null), statement, locator, status and track provenance, with explicit hypotheses and verification scope where supplied. A source-stated theorem is not an independent proof audit. Director status overlays preserve original contributor records.

proof_dependencies.jsonl has from, to, relation, evidence, locator and status. Direction depends on relation: uses/requires point from a dependent claim to its input; supplies_input_to points from input to consequence. Context edges are not implications. Compound paper:passage references become explicit source_passage nodes, not invented theorem audits. See [graph_schema.md](../graphs/graph_schema.md).

connections.jsonl records exact source references, compatible assumptions, established and conjectural parts, next steps, risks, tests and significance/difficulty. Contributor field names are preserved; director overlays update a connection without erasing its original state.

## Findings and counts

audits/findings.jsonl records id, classification, title, sources, evidence, scope, status and verified_author_error. The legacy boolean denotes an independently adjudicated counterexample to an exact versioned statement. It requires director adjudication, at least two independent reviews and an explicit witness. It does not characterize an entire work or its author. Current counts are generated. Historical corrections and provisional findings are separately scoped.

quality/metrics.json is generated. Candidate totals are provisional provider identities. source_file_hashes.jsonl records local bytes, not permission to redistribute them or evidence of complete reading. A distribution manifest hashes the exact payload of each released ZIP.
