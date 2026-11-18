# Independent checkpoint 8 seal QA

**PASS.** The exact release candidate is 17,831,332 bytes with SHA-256 `a300a2976ba42d29b400cb7ba1764444d5d0150f9a8e205a358afd737bfeca22`. The sealed validator checked the exact archive member set and hashes of all 2,051 manifest payloads. This review used the replacement seal and its standalone staged PDF and HTML. It did not compare the sealed records with post-freeze live data.

| Field | Verified |
| --- | ---: |
| Provider metadata candidates | 5,203 |
| Catalogued / selected works | 701 / 700 |
| Selected full-text access / primary excerpt only | 657 / 11 |
| Complete substantive readings | 100 |
| Whole-work audit levels 0 / 1 / 2 / 3 | 600 / 97 / 0 / 3 |
| Scoped adjudicated groups | 79 |
| Theorem, conjecture and exercise records | 406 |
| Connection records | 71 |
| Graph nodes / edges | 2,007 / 1,902 |

The PDF (471,329 bytes, SHA-256 `19b50b783b6a4e983f941f94f778b721db100bf4088969a87881c2125a98afad`) and HTML (609,169 bytes, SHA-256 `f2d12b5e13cd37e7300f8a34efeaa595140a7525352842a38ab455076986ec8e`) match their ZIP members. All 13 PDF pages were rendered and visually inspected. Text bounds on every page were inside the page margins at x=35–565 and y=30–830 points. Page 1 contains six separately rendered numbered steps. Tables, the two-law diagram, dense mathematical sections, and footer page numbers fit; pages 9 and 10 contain short sections and generous whitespace. Extracted text on page 8 distinguishes the unconditional critical-line enclosure, the RH identification and conditional leading coefficient, and quartic-based numerical observations. The evidence limits retain candidate scope for pending weighted-cutoff extensions.

Each Level 3 record matched its bibliography and access-manifest version and source SHA, with a director adjudication and two distinct independent review files in the ZIP.

| Paper | Edition | SHA-256 |
| --- | --- | --- |
| PAPER-MN2026-VERTICAL | arXiv 2610.03568v1 | `ba5c1ab46edf1dbef9741dd1e999ec492c0be59bc65d82cc7ac7dfab8520c076` |
| PAPER-SM63-POS-040 | arXiv 2306.08317v1 | `756288c39bfd743f08f24b1e5074bb8a4adbe8a959d42edd763af07678801830` |
| PAPER-R001 | arXiv math/0008177v2, 2001-05-06 | `49cd7ad205f153197c327fa2035dce5bd676738e06fa696ac5e15cca1e49e43c` |

Twelve JSON code and query pins resolve to actual ZIP members. The original and replay factorial receipts match the historical v1 script, and the n=10 v2 receipt matches the separate current script. All distributed targets of the finite Q2, full quartic and vector Rolle checksum ledgers match, including the finite enumeration script, vector checker, and main and height-10000 receipts. Cached PDFs cited in some ledgers are outside the publication bundle. This seal check compared recorded source hashes and reviewed the distributed provenance.

The finite Q2 receipt gives positive zero counts 29, 202, 649 and 10,142 at heights 100, 400, 1,000 and 10,000. The archived script separately obtains an exact integer multiplicity count from `arb.zeta_nzeros(T + 2^-10)` and critical-line enclosures from `acb.zeta_zeros`. It checks the enclosures are strictly ordered and disjoint, that the last counted root is below each cutoff and that the next enumerated root at interior cutoffs is above it, that each root is on the critical line, and that each derivative ball excludes zero. Equality with the all-zero count at the slightly higher height establishes completeness at the advertised cutoff. This QA inspected the archived CSV/JSON evidence and code and did not rerun the 10,000-height interval computation.
