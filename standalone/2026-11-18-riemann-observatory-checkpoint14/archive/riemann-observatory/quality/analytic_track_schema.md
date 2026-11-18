# Analytic/formal track schemas and update semantics

This is one track of the archive, not a global coverage report. Its canonical paper IDs are PAPER-A001–A008. Fold records in this order bystable paper_id:

1. papers/analytic_records.jsonl: six original works.
2. papers/analytic_round2_records.jsonl: one new work(A007).
3. papers/analytic_round2_updates.jsonl: scope/metadata overlays for existingA004,A005, never additional works.
4. papers/analytic_round4_records.jsonl: newA008, with exactv5 statement/withdrawal-history scope.

The resulting track has8 bibliographically verified/full-text-accessed works and3 completed substantive readings(A002,A003,A004) at this checkpoint. No entire work is labeledLevel2or3. Theorems, exact experiments, source-semantic checks and local compilation components have their own statuses and must not inflate paper-level counts.

Paper records use paper_id,title,authors,year,version/date,publication_year/preprint_year,arxiv_id,doi,venue,canonical_url,source_url,source_sha256,access_date,audit_level,substantive_reading,audit_scope. date/version_date identifies the inspected preprint version; access_date identifies retrieval. A004 preserves a genuinely shorter arXiv/PDF-metadata title and the longer visible PDF title via source_title/title_variants. publication_year is not silently substituted for the source-version date. Corrections/objections and access limits remain scope text rather than categorical completeness claims.

Theorems in theorems/analytic_track.jsonl and theorems/formal_round2.jsonl have stable theorem_id,paper_id,kind,statement,verification_status,evidence and scope/novelty fields. Formal-round2 IDs THM-F001–F014 identify scoped mathematical or certificate claims. The statement and limits are authoritative: a conditional zeta consequence is not an independently established analytic premise; an actual submodule build is not a successful full theorem build. Directed proof edges in formal_round2_dependencies.jsonl use source_id,relation,target_id,locator/status/evidence. Relations such as shows_limitation_of do not mean contradicts.

Findings in audits/formal_round2_findings.jsonl use finding_id,paper_id,one of the user-requested category labels,scope,result,verification_status,limit,provenance. New synthetic countermodels are explicitly separated from alleged published errors. The Christoffel issue is a missing qualification in an informal generic remark; its specific four-moment conditional certificate survives.

Connections in connections/formal_round2.jsonl use connection_id,source_theorems,mathematically_explicit_connection,compatible_assumptions,already_proved,conjectural_or_pending,next_precise_step,counterexamples_or_barriers,tests,significance,status,evidence. All source/prerequisite matching and conjectural boundaries are textual and explicit. The classical Vinogradov–Korobov input is used from an inspected source statement; the original classical proof is not labeled audited.

Experiments/results JSON files are scoped execution evidence. kind and scope distinguish exact rational/finite integer checking, original C++ execution, static Lean source inspection, actual Lean compilation and source-reported output. A manifest/hash proves identity, not mathematics. Bundled MIT inputs have separate pinned PROVENANCE and license files; source PDFs, complete repositories, toolchains and build caches stay private and are not redistributed.

For actual formal completion read formal_ranktrace_build.json and formal_multiplicity_build.json, checking real exits and query results. The first is completed module-level evidence; the second is a live long-running target until its own output says otherwise. If interrupted, resume_formal_safely.py checks the actual PID/command/checkout and avoids duplicate builds. Static import counts were corrected after the original dotted-name parser missed aggregate imports; they are estimates, not proof results.
