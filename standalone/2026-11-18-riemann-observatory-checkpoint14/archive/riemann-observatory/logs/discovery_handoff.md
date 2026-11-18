# Corpus-discovery handoff

Completed network discovery on 2026-11-17. Do not rerun network searches simply to reproduce the existing snapshot: `python scripts/discover_corpus.py --offline` reconstructs metadata from the raw cache; `python scripts/discover_screen_candidates.py` reconstructs the conservative screening. **Note:** offline reconstruction writes the base summary; the historical/language/raw-index enrichment in the delivered `candidates_summary.json` must be preserved or regenerated before reporting metrics.

- `corpus/candidates.jsonl`: 5,203 discovered metadata records, NOT selected corpus entries.
- `corpus/candidates.csv`: same records in spreadsheet-friendly form.
- `corpus/candidates_screening.csv`: all 5,203 candidate decisions; 56 deterministic title collisions rejected, 5,147 pending relevance review.
- `corpus/candidates_rejected.jsonl`: explicit rejected records and reasons.
- `corpus/candidates_summary.json`: quantitative snapshot, query counts and coverage.
- `corpus/candidates_schema.json`: metadata schema; never interprets these records as read/audited.
- `corpus/raw_discovery_index.jsonl`: 56 API request URLs, timestamps, SHA-256 hashes, byte sizes (86,869,323 bytes total raw JSON).
- `corpus/candidates_primary_seeds.jsonl`: THREE separately source-grounded bibliographic landing-page seeds (Riemann1859, Deligne1974, Deligne1980). These may overlap other records; do not add three to any unique count without DOI/title deduplication. This agent did not read their mathematical texts.
- `corpus/candidates_methodology.md`: biases, deduplication, selection recommendations and limitations.

Candidate ID is SHA-256 prefix of lowercase DOI URL where available, else provider identifier; seeds without provider ID use source URL. Identifier corrections must preserve aliases. Main-candidate `metadata_evidence` records the raw response containing the provider identity. `openalex_id`, `doi`, `canonical_url`, `pdf_url` and `oa_url` are distinct; provider OA labels and canonical URLs have NOT been individually verified. `family_candidates` expresses search scope, not mathematical classification. `audit_level=null`, `selected=false`, `relevance_review=pending` are deliberate.

Do not distribute source PDFs merely because provider metadata says open access. The response cache itself contains bibliographic metadata, references and provider classifications. It can be omitted from the downloadable archive for size, provided the hash/URL index and regeneration limitation are kept. A response URL/hash alone does not guarantee future provider responses will reproduce this snapshot.

Next substantive discovery stage: review the 124 title/year duplicate flags; ground authoritative primary bibliography; filter broad method and historical Riemann-surface matches against exact RH obstacles; expand theorem-level backward/forward citation dependencies; then select an importance-reviewed ~1,000 corpus. No algorithmic citation-rank selection is presented as a completed expert corpus.
