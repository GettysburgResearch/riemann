# Candidate discovery, not corpus completion

The discovery script queries **title fields**, rather than assuming that every full-text mention of RH makes a work a useful corpus entry. The completed discovery run uses 51 capped query scopes (41 initial terms, six recent date-ranked scopes and four historical scopes) covering classical analysis, zeros, equivalent criteria, spectral methods, geometry and selected adjacent methods. Results are sorted by provider citation count. A bibliographic API record is evidence of a discovered identity; it is **not a verified primary-source bibliography, a substantive reading, or an audit**.

Every row records its discovery queries, provider identifier, DOI if present, primary landing/PDF locations returned by the provider, date, and the exact raw response containing its evidence. Query categories are candidate scopes, not reviewed mathematical classifications. The execution cutoff is 2026-11-17. Provider access timestamps and raw responses are retained. No inference that the provider has exhaustively indexed work through that date is warranted.

## Deduplication

A DOI, where present, is the preferred deduplication key; otherwise the OpenAlex work identifier is used. Potential identical-title/year duplicates with different identifiers are flagged, **not silently collapsed**, because they may be versions or genuinely different works. Publication and preprint versions are not automatically conflated. Versions and corrections require primary-source verification.

## Recommended selection decisions

1. Preserve an authoritative historical seed set even where citation ranking or English title search misses it. This includes German and French primary texts, landmark monographs and papers indexed under altered transliterations.
2. Assess relevance to a *specific theorem, lemma, technique, obstruction or dependency*. Reject keyword collisions (for example, a generic use of “canonical system” without a concrete mathematical transfer).
3. Prioritize historical significance, precise mathematical depth, dependency centrality, contemporary relevance and the ability to resolve an explicit obstacle. Citation count is a discovery aid only.
4. Keep quota *targets*, not forced minimums, across A–H and the seven historical strata. A thin stratum triggers further search, not invention or inclusion of low-value work.
5. Verify titles, authors, dates, versions and URLs against a canonical source. Only then assign audit Level 0. Resolve duplicate/version flags at that stage.
6. Select approximately 1,000 after this review, retain deferred and rejected candidates with reasons. Do not label the top 1,000 citation-ranked records as a rigorously selected corpus.
7. Retrieve and read the selected texts. Record access/read/audit as independent fields and preserve inspected-page scope. No template record upgrades a source's evidence level.

## Known biases and corrective searches still needed

Title queries miss multilingual early work, papers with uninformative titles, important lemmas buried in unrelated papers, and theorem-level forward/backward dependencies. Citation sorting favors older or broader work and can amplify inherited indexing errors. The initial metadata list will include off-topic candidates, generalized-RH results that do not establish anything about classical RH, duplicate versions and unverified proof claims. The next discovery stage must expand verified primary bibliographies and citation neighborhoods, inspect original sources and extend the explicit 2024–2026 date-ranked searches beyond the six capped scopes already executed. No claim that any field's best current bound was established by this discovery pipeline is made.

## Reproduction

Run `python scripts/discover_corpus.py`. Existing `corpus/raw_discovery/*.json` files are reused. Delete an individual raw page only when deliberately refreshing that query; retain the earlier evidence elsewhere first. The script uses only Python standard-library modules. API errors are logged and unsuccessful queries remain visible in the summary. Rerun to fill missing pages. A future run should update the cutoff explicitly rather than silently changing what the snapshot represents.

## Snapshot outcome

The completed title/query discovery snapshot contains **5,203 unique metadata candidates** from **5,480 query hits**. Conservative title screening rejects 56 clear lexical or out-of-scope collisions and leaves 5,147 pending relevance review. No candidate was selected, substantively read, or technically audited by this pipeline. There are 124 rows flagged as potential title/year duplicates across distinct identifiers. This is a discovery pool, not a claim to have found 5,203 important RH works.

The historical searches fill an initial absence of pre-1900 records but introduce broad Riemann-function/surface material requiring review. Their 132 candidate rows must not be reported as 132 foundational RH sources. The historical-source landing-page seed file is separate and may overlap other records; do not add its count without deduplication.

The raw metadata cache is 86,869,323 bytes across 56 API responses. `raw_discovery_index.jsonl` retains request URLs, SHA-256 hashes, timestamps and byte counts if the heavy cache is omitted from distribution. Raw URL/hash metadata does not replace archival possession of the returned response: provider data can change.
