# Structured data and evidence states

UTF-8 JSON Lines files have one object per line. CSV companions quote nested values as JSON strings. Stable IDs never identify a source merely by title: canonical paper identity, version expression, DOI/arXiv and source hash remain separate fields. Missing fields are not invented. Contributor tracks retain their original additional fields; the master builder normalizes the keys below and preserves track provenance.

## Bibliography and access manifest

Canonical keys are id, title, authors, date/year, venue, doi, arxiv, source_url, version, publication_status, family, selection_status, access_status, audit_level, whole_work_read, read_scope, record_path and track_file. Optional source_sha256, version histories, manifestation records and source overlays preserve the inspected copies. A canonical record may describe several manifestations in prose; version expressions are not yet a fully normalized version ontology.

selected_checkpoint_priority_work is counted in the selected corpus. deferred_supporting_bibliographic_record is retained but excluded from selected counts. Access uses full_text_accessed, primary_source_excerpt_accessed, full_text_inaccessible or the retained source-specific state. Complete access and complete reading are distinct. whole_work_read=true records the reported full substantive reading of that work or an explicitly identified complete translation. audit_level2/3 requires a separate explicit whole-work coverage registry; locally checked theorems do not promote it. The counting correction for an earlier deferred record is preserved in counting_corrections_round5.md.

## Claims and proof dependencies

Theorems/theorems.jsonl requires id, statement, locator and provenance_file; paper_id can be null for program-level reconstructions. kind, hypotheses, scope, status, verification and novelty_claim further distinguish source statements, derived claims, conjectures, model controls and experiments. A source theorem entry is not itself an independent proof audit. The status overlay file records director adjudications without erasing the contributor record.

Proof dependencies have from, to, relation, locator/evidence, status and track provenance. A relation such as uses or requires normally points from the dependent claim to its input. supplies_input_to points in the opposite direction and is retained explicitly. A compound PAPER-ID:passage references a passage, not an invented full theorem audit. Every mathematical relationship has evidence and a verification state. A graph edge is not inferred merely because two sources share a term.

## Connections

Connection IDs identify separately scoped propositions or research interfaces. Source references, statement, compatible assumptions, already proved portion, unresolved portion, next precise step, potential counterexamples, tests, significance, difficulty and evidence are recorded in canonical director connections. Older contributor schemas use equivalent field names and remain visible; missing semantic normalization is a documented limitation. Reference edges alone do not assert implication.

## Findings and review groups

Findings normalize id, classification, title, sources, evidence, scope, verified_author_error and track_file. The legacy boolean verified_author_error means an exact versioned mathematical statement counterexample, not author competence or the falsity of an entire paper. A true value requires director_adjudication, at least two independent_reviews and an explicit_witness. The scope field is mandatory for interpretation. Finding aliases retain provisional contributor records under the single adjudicated issue; they do not count repeated reasoning as independent findings.

audits/reviewed_claim_groups.jsonl counts scoped adjudications, not whole papers, discoveries or publication novelty. A group may contain a mathematical theorem, its controls and repairs. The underlying proofs and independent reviews are the evidence; agreement alone is not a validation rule.

## Graph, experiments and snapshots

Graph rows have record_type node/edge; nodes use id, type, label, evidence and status, while edges use from, to, relation, provenance and status. See graphs/graph_schema.md. The graph is an index into full structured and prose records, not a formal proof object.

Experiment results distinguish exact arithmetic, validated intervals, ordinary numerical observations, source builds and proof-kernel/axiom queries. Files contain their inputs, precision/version and code references where applicable. Exact integer output is not an analytic infinite theorem without its accompanying proof. Formal component success is not a headline target success.

Checkpoint metrics describe canonical selected records at merge time. Distribution manifests hash exact file bytes in each ZIP. Raw draft files can be included while active research continues, but their labels do not change adjudicated counts. Source PDFs, extracted fulltexts and private compiler caches are excluded from redistribution; their hashes and canonical retrieval references remain.

Current-status overlays apply after source manifestation/event rows merge to canonical work IDs. Stable claim IDs with CAND, EFFECTIVE or PREFIX-FORMULA prefixes remain identities even after adjudication; their status field is authoritative. Graph references accept an existing registered claim ID regardless of prefix, while an unregistered arbitrary string is not invented as a theorem. Existing Suzuki author corrections are credited correction records and are not automatically new-error flags. The current count is derived from audits/findings.jsonl; each true flag remains versioned and scoped.
