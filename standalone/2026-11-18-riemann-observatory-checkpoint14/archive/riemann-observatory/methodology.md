# Methodology and coverage taxonomy

Execution date and search cutoff: 2026-11-17 UTC. This is a live, incomplete research checkpoint, not the completed thousand-work program.

## Corpus construction

Discover through controlled searches for mathematical structures, then expand citations and dependencies. Provider metadata creates a **candidate**, not a verified record or a substantive reading. Preserve raw query responses, retrieval dates, canonical IDs and exclusion reasons. Deduplicate primarily by DOI, arXiv identity and provider ID, then flag normalized-title collisions for manual resolution. Preprint and publication manifestations must ultimately be linked, not automatically counted twice. Aim 2,000–3,000 candidates and approximately 1,000 selected works; neither target licenses automatic admission of tangential results.

Families: A classical analysis; B zeros/statistics; C equivalent criteria; D spectral/operators; E geometry/arithmetic/L-functions; F dynamics/alternative analysis; G failed or disputed approaches; H adjacent methods. Families overlap. Historical strata: 1859–1900, 1901–1950, 1951–1980, 1981–2000, 2001–2015, 2016–2023, 2024–cutoff. Future dates, translations, republications and editions need manual reconciliation.

Selection rubric: historical importance (0–3), theorem/technique depth (0–3), dependency centrality (0–3), contemporary frontier relevance (0–3), precise research-transfer potential (0–3), source accessibility (0–2). Scores are triage, never mathematical evidence. No single citation-count ranking defines the primary corpus. Reserve coverage for original non-English sources, objections/corrections, finite-field analogues and precise adjacent tools. A candidate remains pending until an evidence-backed selection decision. Rejected candidates remain in the database with a reason; unreviewed is not rejected.

## Evidence and audit units

- Discovered: metadata or bibliography identifies a work.
- Accessed: source bytes/text were actually obtained and identified.
- Level 0: identity/version/source verified against a source. Access alone does not establish all bibliographic fields.
- Level 1: substantive source reading with exact results, assumptions and architecture. A specified section can be substantively read without claiming the entire work was read. Whole-work reading has its own field.
- Level 2: central technical passage reconstructed and checked; scope always explicit. A checked lemma is not a whole-paper audit.
- Level 3: two independent reconstructions plus adjudication of the precise claim. Agent agreement without independent reasoning is insufficient. Formal and numerical checks have distinct status.

Per-work audit_level is conservative. Scoped Level-2 checks are separately listed and do not automatically raise a whole work to Level 2. No work is called fully audited when only one useful theorem was inspected. Downstream theorems cited by a paper remain external dependencies unless their original proofs were checked here.

## Mathematical discipline

Every mathematical graph edge needs a source locator, status and assumptions. States: source-stated, reconstructed, independently checked scoped claim, conjectural, refuted in model class, unresolved. Counterexamples must identify the function class they inhabit. Generic real entire functions do not automatically satisfy Euler products, Dirichlet-series axioms, gamma factors, arithmetic coefficients or zero-counting laws of completed zeta. Proportions tending to one do not exclude sparse exceptions. Fixed-test asymptotics do not license a test depending on height without uniform estimates.

## Adversarial process

Advocate and skeptic start from the same explicit proposed statement and independently reason without reading one another's files. A third reviewer checks their derivations, endpoints and experiments. Preserve rejected statements and corrected formulas. An issue in notation or counting conventions is recorded as ambiguity until version and interpretation are resolved. No public allegation of a paper error follows from an agent's first impression.

## Persistence, distribution, updating

All durable state is inside this directory. Private downloaded source files are kept in sources/ during execution but are omitted from the distributable ZIP unless redistribution permission is established. The ZIP contains original analysis, short quotations, authoritative source URLs, source hashes and retrieval instructions. Raw provider responses are retained locally; public candidate extracts retain provenance. Scripts must avoid reassigning stable IDs on update and must never silently overwrite curated paper records.

Run scripts/validate_archive.py before packaging. Continue from CONTINUATION.md and corpus pending states. The checkpoint reports exact counts and missing targets; requested top-100/top-25 files contain only supported material and explicitly expose any shortfall.
