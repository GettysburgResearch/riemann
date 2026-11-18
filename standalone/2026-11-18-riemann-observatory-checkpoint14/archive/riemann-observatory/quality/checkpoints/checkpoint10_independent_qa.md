# Independent checkpoint 10 seal QA

**PASS.** The corrected release ZIP is 20,024,472 bytes with SHA-256 `25d0735dd17499cb3b33b109209f91fb26a72c95cbe907ea8d46e033e2975a7b`. The 2,658 manifest payloads and the manifest itself match both the exact ZIP member set and frozen stage bytes. The sealed validator also passed all 21 code pins with the separately stored PDF and HTML supplied for byte comparison.

| Field | Verified |
| --- | ---: |
| Provider metadata candidates | 5,203 |
| Catalogued / selected works | 1,002 / 1,001 |
| Selected full texts / primary excerpts only | 956 / 13 |
| Complete substantive readings | 126 |
| Whole-work Level 0 / 1 / 2 / 3 | 875 / 119 / 0 / 7 |
| Scoped adjudicated groups | 103 |
| Claim / connection records | 449 / 85 |
| Graph nodes / edges | 2,614 / 2,492 |
| Findings / witnessed version-specific assertions | 52 / 10 |

The SQLite index passed integrity and foreign-key checks. Seven input hashes match the archived inputs. The package contains 1,002 canonical paper views plus two separately counted alias redirects. The three historical E001 claim links attach to E014 while their original payload fields retain E001. The index contains 199 paper-to-claim and 84 paper-to-finding links.

All seven whole-work promotions match their bibliography and access-manifest versions and source hashes. I independently hashed all seven private source PDFs against the archive pins. These include the Báez-Duarte journal and the Hughes–Rudnick journal. The archive contains exactly the six allowed original PDFs. It excludes the primary source PDFs, private scan pages, pending RMT source staging, raw discovery payloads and build caches. The archived Lean source and replay receipt both match the checksum ledger. The proof checks the scalar implication given two estimates.

The 19-page PDF has 251,569 bytes and SHA-256 `36a0e61a3d8841b0cf4840a9015b7fa9177f7c863e2b993c55afdfdaa86f4a54`. The HTML has 249,357 bytes and SHA-256 `09d856f6cc786a429ff940403d2efb488e5a0a1e6e7462181beabcb865476137`. Both exactly match the corresponding files in the ZIP and standalone release artifacts. I reviewed every page, including the ranked guide, current and historical tables, dense formulas, chart and footers. Page text stays within x=42.00–552.00 pt and y=48.26–820.81 pt on A4. All 19 corrected renders are pixel-identical to the original visual pass. The source-audits heading falls at a page break, and a few inline formulas retain literal Markdown delimiters. Text remains readable.

The repaired renderer resolves local links from the Markdown section that owns them. All 48 local HTML links, seven HTML anchors and 53 PDF file annotations point to existing targets in the extracted archive. Links to local evidence require the extracted directory structure. The earlier navigation candidate, SHA-256 `f1cc24bc96d128e149a8c288bf65ceb352b41c21910469e9913e7f7c9f9f6383`, had 13 unresolved HTML links and was withheld. Its manifest differs from this release only in the renderer, regenerated PDF and HTML, and one added navigation receipt. No mathematical payload changed. The separate premature-render draft, SHA-256 `b4dd0747320ce2c8aa50650dc9fb5d4f60c3cad8fff9aeb47084e390dde6a181`, was also withheld.

[Machine-readable QA receipt](checkpoint10_independent_qa.json)
