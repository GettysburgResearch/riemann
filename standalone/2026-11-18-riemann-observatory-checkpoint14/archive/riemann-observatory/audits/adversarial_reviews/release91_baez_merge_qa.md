# Independent Round 13 Báez-Duarte identity and archive QA

18 November 2026. I independently compared the live source merge with frozen checkpoint 9, checked the local source bytes, and built the index in a disposable tree. The source merge and the corrected alias export passed. The checkpoint 9 ZIP still hashes to `4677a1e77c2f60c04860456eea0ce7f450ca2ee88bf3ac1f6fe1c9a22ae45a3c`.

## Source identity and audit scope

The bibliography now contains one canonical work, `PAPER-E014`, with `PAPER-E001` as its historical May-deposit alias. The alias row links two distinct identity reviews. The expanded May abstract names February as the first version, and the author's 2003 self-citation identifies the May deposit as the Lincei preprint. The only removed canonical bibliography ID is `PAPER-E001`. The source-only build has 999 catalogued works, 998 selected, 954 selected full texts, 126 complete readings and six whole-work Level 3 entries. The two new complete readings, von Mangoldt and Gonek, remain Level 1.

The exact preferred edition is `2003 Lincei journal scan, pp. 5–11, with two BDIM front sheets` with SHA-256 `9bfb3943ec8d7690d452b8ac7d50fb10614b4e814738dc091390e6ab4994f0b8`. I hashed the local PDF, counted nine PDF pages and confirmed the journal imprint and seven article pages. The hash, edition and Level 3 agree in the bibliography, access manifest and promotion register. The two distinct complete reconstructions and director adjudication exist at the recorded paths.

I also rehashed all three preprint PDFs against the manifestation ledger. The preserved May and February v2 manifestation objects match every field of their original contributor rows. Both contributor rows and the May historical source note match the frozen checkpoint 9 bytes. The May hash is `13a2dcc763d3fdd5b52afc87845c6d77c83764a56aab06f574a91ee43c8a152b`. Both source record IDs and both arXiv deposit IDs remain in the work record, and the version graph contains all four exact manifestation nodes.

[Director review](director_baez_whole_round13.md) · [Manifestation ledger](../../quality/baez_manifestation_identity_round13.json) · [Promotion register](../../quality/whole_work_audit_promotions.jsonl)

## Claim and finding continuity

The theorem ID set, statements and hypotheses are unchanged. `THM-E001` now points to E014 with the separate May Theorem 1.1 and journal Theorem 1 locators. `THM-E-D204` points to E014 with May Proposition 3.1 and journal Theorem 2 preserved as locators for one result. I confirmed the numbering in the archived PDFs. The graph retains explicit edges to the May and journal manifestation nodes. The existing `THM-E-D202` and `THM-E-D203` lemma records and every existing dependency edge involving those two lemmas or `THM-E-D204` match checkpoint 9.

The finding overlay updates `FIND-008` and `FIND-R207` after contributor normalization. The new canonical paper references, statuses, scopes and review evidence match the update ledger. The original evidence and contributor files remain intact, and the merged rows retain the update fields and source in `status_update_history` and `status_update_evidence`. Both findings remain accessible from E014. The 51 finding IDs and count of verified author errors are unchanged.

[Claim ledger](../../theorems/theorems.jsonl) · [Finding update ledger](../../quality/finding_status_updates.jsonl) · [Version graph](../../graphs/baez_versions_round13.jsonl)

## Alias indexing and historical links

Before the exporter correction, a shadow rebuild removed the old E001 generated view and omitted three retained historical references from E014. The exporter now resolves paper aliases when building claim and finding links. It also generates alias redirect pages and fingerprints the alias register in the index. The original JSON payload keeps historical identifiers.

A corrected shadow rebuild passed SQLite integrity and foreign-key checks. It retained 999 canonical paper views and generated two separately counted alias redirects. It attached `LEM-C106-ANCHOR`, `LEM-WC-R2-1` and `THM-WC-R2-1` to E014 while preserving their original E001 fields. The E001 redirect links to the canonical E014 view and `papers/PAPER-E001.md`. The earlier `PAPER-BESSEL-S02` alias likewise links to `PAPER-BK001` and to its historical note. Neither alias became a paper row. The corrected tree has 195 paper-to-claim links, compared with 192 in the shadow build before alias resolution.

The lexical merge initially left May numbering in E014's top-level result summary while showing the journal as preferred. The director is updating the preferred summary and notation. The original wording remains in the preserved May object. This QA did not rebuild the live SQLite database, live views or rendered synthesis.

[Exporter documentation](../../graphs/archive_index.md)
