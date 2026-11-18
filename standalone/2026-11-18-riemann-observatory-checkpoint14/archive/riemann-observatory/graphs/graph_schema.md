# Knowledge graph schema and direction conventions

JSONL nodes and edges are distinguished by record_type. IDs remain stable across updates. Alias mappings in quality/paper_aliases.jsonl identify duplicate manifestations of one work; original track records remain available and aggregate references use the canonical ID.

Node fields: id, type, label, evidence, status. Types include paper, author, mathematical_claim, conjecture, definition, technique, open_obstacle, experiment, research_connection, external_claim, mathematical_structure, source_passage, formal_artifact and formal_theorem_declaration. Integer status on paper nodes is the conservative whole-work audit level. A mathematical_claim can be a source theorem, conditional reconstruction, experiment certificate or model exercise. Its full theorem record carries hypotheses and verification scope. Graph nodes copy claim_kind, hypotheses and verification_scope when explicitly present, and paper version/source/selection fields when supplied; missing values are not inferred.

Edge fields: from, to, relation, provenance, status; dependency edges additionally retain evidence, locator and track_file. All endpoints must exist. An association with a paper does not imply that the paper states a later derived proposition.

Direction conventions:

- author_of: author → work.
- associated_with_claim_record: work → indexed mathematical record. This is a catalogue association only; read kind/provenance to distinguish source theorem and later reconstruction.
- requires, uses, uses_proof_technique_of: dependent claim → required input. These relations preserve the source track direction.
- supplies_input_to, supplies_lower_bound, supplies_finite_dependency: input → consequence. Conditions are retained; a supplied lower bound does not assert equality or an upper bound.
- special_case_reconstructed: source general result → separately reconstructed special case.
- context: non-implicative historical/thematic context.
- has_input_reference: research_connection → cited theorem, paper or passage. This is not an automatic proof edge. Each connection record separately states compatible assumptions, established part, conjecture, next step and failure controls.

A source_passage node is a real cited passage whose theorem record has not yet been reconstructed. It is not an invented theorem. External claims retain their exact cited/inspected scope; a reference never implies that its historical proof ancestry was audited. Technique nodes similarly do not establish hypotheses by themselves.

Original dependency track schemas may use source/target or source_id/target_id rather than from/to; the builder normalizes names without reversing semantics. Claims can receive explicit director status overlays in quality/claim_status_updates.jsonl; original contributor records are preserved. Source-read scope overlays are separate from mathematical claim verification.

The graph is a partial research graph, not an exhaustive account of every source dependency or all metadata candidates. Every connection is queryable without equating speculative and established portions. Run `python scripts/query_graph.py THM-E004` for a node and incident edges. Coverage metrics are generated from actual records rather than hardcoded graph counts.
