# Checkpoint 7 independent QA

17 November 2026. The [preflight](checkpoint7_preflight.md) records the initial inspection. This note records the contributor provenance repair and the checks on one sealed ZIP with its matching standalone artifacts.

## Source-passage attribution

Three connection records now retain their original wording in `original_source_theorems` and use seven machine-readable passage citations with versioned locators. The theorem IDs, original source records and scope statements are intact. [Formal connections](../../connections/formal_round2.jsonl)

| Record | Verified source passages |
| --- | --- |
| CONN-F002 | BGSTB arXiv:2306.04799v1 §2 p. 6 first paragraph, with the majorant at p. 4 eqs. (2.9)–(2.11). Alpöge–Furman arXiv:2608.13637v2 §2 eq. (2.8) p. 4 and Lemma 2.1 p. 5, and Theorem 5.7 p. 11 on the prime-side second moment. |
| CONN-F003 | Alpöge–Furman v2 Lemma 3.4 p. 6 and §6 pp. 11–12, for the distinction between Weyl operator control and the rank/trace/second-moment argument. |
| CONN-F004 | Alpöge–Furman v2 §7.2(d) and §7.2(f), both on p. 13, for the general Christoffel assertion and the source-specific conditional moment route. |

The two sine-Gram model edges now target a typed `PAPER-A004:Section7.2(f)` passage under “Sharpness and limits of the method,” with the old endpoint retained in `source_reference_history`. The prior model scope and evidence are intact. §7.2(f) addresses the sine-Gram moments under arithmetic hypotheses, while the separately numbered Remark 7.2 addresses the Dirichlet-family average. Both locally inspected PDF hashes match the canonical source pins. [Contributor graph](../../graphs/sine_gram_round3.jsonl) · [Alpöge–Furman source record](../../papers/PAPER-A004.md) · [BGSTB source record](../../papers/PAPER-A006.md)

## Sealed-byte check

Verified on 18 November 2026 against the immutable release copy. The ZIP is 13,114,889 bytes with SHA-256 `c5b135bb932f8165b7e955234e0685181669fd79d5198d84a11a8f359c6ffb17`. Its 1,223 entries are exactly the distribution manifest plus its 1,222 declared payloads. Every declared size and hash matches. All JSONL records parsed, graph endpoints resolve, records have unique IDs in their canonical tables, and excluded private source and cache paths are absent. The PNG, PDF and evidence included in the archive are the distributed files sealed by the manifest. [Read-only verifier](../../scripts/validate_sealed_checkpoint.py)

The derived and frozen tables agree on 481 catalogued works, 480 selected works, 437 selected full-text accesses, 11 selected primary excerpts, 80 complete readings, 400/79/0/1 selected whole-work Levels 0–3, 68 scoped adjudicated groups, 383 claim records, 63 connection records and 1,586 graph nodes with 1,434 edges. The three normalized connections have all seven citation edges, both sine-model edges reach the typed passage, and the obsolete pseudo-paper endpoint is absent. Five auxiliary findings are marked verified.

The sole whole-work promotion pins Manzur–Noor's seven-page arXiv 2610.03568v1, PDF SHA-256 `ba5c1ab46edf1dbef9741dd1e999ec492c0be59bc65d82cc7ac7dfab8520c076`. The label and source pin agree across the bibliography, access manifest and promotion registry. Two separate reviews and director adjudication are present. Both §6 covariance exponents need the negative sign. Theorem 5.1 remains valid, with the classical upstream inputs recorded separately. The Lee–Pańkowski target qualification is separately scoped. [Promotion registry](../whole_work_audit_promotions.jsonl) · [Findings](../../audits/findings.jsonl)

The original factorial-array run and independent replay both pin the archived v1 script (`11ee04883dec90fae9f1bf878f178140c5c06445467117eb1ea85efe9e62e559`). The separate N=10 v2 replay pins the hardened script (`65e6445595292e30faeb241310a7610aa1dafe88c1a89261cb392f80abf551d3`). Both K839 majorant receipts match their calculator. The two director receipts for the explicit derivative tail and finite remainder match the archived calculation scripts. All four interrupted second/third-window runs pin the byte-preserved reference files. The two completed adapted checkpoint runs remain separately identified. The Palomar cached full-curve query pins its query file and shows unchanged target module bytes. Its receipt is distinct from the completed pinned Solution build.

## Rendered synthesis

The standalone files match the corresponding ZIP payloads byte for byte. The PDF SHA-256 is `59da3d576bfffd9a91f09d7486eb9844e9663fd0bfe5924185fb0aec94ffb853`. The HTML SHA-256 is `2c663bd313cbb93ad3e73da725f8680633623ff51823e8a29b1ac1625b89fa93`. I inspected a page sheet for all 18 PDF pages, inspected the new theorem and figure pages at reading size, and checked extracted word bounds. Tables, formulas, page footers and the lattice escape figure fit. The executive summary fits on one page. Page 10 carries the final paragraphs of the comprehensive section before a forced page break.

The synthesis contains the prescribed-array asymptotic, the fixed-rational and growing logarithmic prime-block results with their distinct scopes, the explicit finite-zero remainder interface and derivative-tail bound, the lattice escape figure, and the Manzur–Noor and Lee–Pańkowski versioned source findings. The executive summary, comprehensive synthesis and task list record the completed explicit length remainder and the remaining work of tightening and instantiating it. The formal mathematical statements and evidence links are consistent with the adjudications.
