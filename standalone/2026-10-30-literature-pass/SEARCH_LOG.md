# Search coverage and source decisions

Cutoff: **30 October 2026 (UTC)**. The task was to find recent research relevant to the repository's existing Riemann, zero-free, moment, positivity and arithmetic programmes, and contribute a literature pass. This is a research screen with reproducible source pointers, not a systematic review or a certification of every linked proof.

## Coverage

The search emphasized the last ten days, then widened to October and relevant earlier 2026 dependencies. Three parallel research lanes covered zero-free/exceptional-zero results, analytic moment and density tools, and spectral/positivity/formalization alternatives. The final selection contains **28 annotated records** plus a short ledger of known sources and further leads.

Representative query families included:

- Riemann hypothesis, quasi-Riemann, zeta/Dirichlet/Hecke zero-free regions, new versions, and formal verification.
- Zeta zero density, large values of Dirichlet polynomials, short intervals, Möbius cancellation, signed and negative moments.
- Weil positivity, Hilbert–Pólya, reciprocal xi transforms, Pólya-frequency functions, Robin's criterion and finite-height verification.
- Landau–Siegel zeros, effective Brauer–Siegel, number-field generators and Frobenius prime sums.
- Exact titles, author pages, identifiers, repository names and tracker submissions discovered along those paths.

Both available web search engines were used; recent-event searches were checked against primary records. Scientific claims in the catalogue are attributed to author manuscripts, versioned repositories, journal records or primary abstracts. Search indexes and mirrors served as discovery aids, with incomplete access explicitly marked. No search-engine ranking or summary was treated as a mathematical verification.

## Repository comparison

The existing-work screen read the root instructions, contributing/review guidance, README, STATUS, OPEN_CUTS and relevant integrated result descriptions at main `f99d9e3908dde4865377c75d9ca051c1f545bf4f`. It also inspected the 40 most recent returned PR records (#984–#1023), changed-file lists for eight selected October PRs, and representative source reports at exact heads recorded in [REPO_MAP.md](REPO_MAP.md).

Targeted PR searches for literature and candidate names supplemented that screen. Absence from those results does not establish absence from every branch, comment or file. “New” in this packet means recent externally, or not found in the inspected repository sources; the catalogue states known overlaps separately.

The most relevant existing work was the family-density/return work in #1023, HLC transfer in #1022, signed selector in #1021, structured moments in #1020, Möbius projection in #1019, Weil packet in #1017, and the historical Liu import in #1009. Existing draft results retain their own qualifications.

## Date, version and identity decisions

| Issue | Decision used in this packet |
|---|---|
| Tracker PR #97 cached page said open | The live GitHub API reports merged on 30 October at 07:47:37 UTC. The source head and protected admission blob are recorded in `TRACKER_EVIDENCE.json`. |
| Liu's all-field paper | Use arXiv:2610.26835v2, revised 29 October. Retain the v1 import as historical work; no new decimal boundary is claimed. |
| Sra's positivity paper | Use the author's 29 October v2 PDF. Distinguish that version from Hexagon:2610.00584v1; do not manufacture an arXiv identity. |
| Frei–Kai and Cureton–Thorner | Use version histories rather than landing-page initial-deposit headers. Their identifiers are Hexagon, not arXiv. |
| Green's determinant paper | Hexagon:2610.00311v2, 18 October; already represented in the repository. |
| Pliego–Wang revision | Primary indexed v1 is supported. A mirror-only 22 October v2 lead remains explicitly unconfirmed. |
| Bui–Florea–Heycock seminar | The 5 November seminar is supporting author context, not the submission date or an event that has already occurred. |
| Finite-height Lean source | 30 October identifies the inspected repository tip. The reported build/check dates are 23/24 October. |
| Durkan–Page and Chen–Gupta–Li | August and July revisions are background dependencies, not new October publications. |
| Fourier optimization journal record | 22 October is the online journal date; the preprint already existed in February 2025. |
| Nic Johns deposit | Use the displayed 8 October deposit date, not the date of rediscovery in a fresh search. |
| Guo authors | Victor Zhenyu Guo's real-zero paper and Jizhou Guo's shifted-Möbius follow-up are different works by different authors. |

## Evidence levels and access limits

The catalogue distinguishes a primary theorem statement inspected, an abstract-only lead, author-reported verification, and an inspected protected formal-admission receipt. These labels describe what was available and checked in this pass. They do not rank authors or replace proof review.

For L01, the live PR, final theorem, canonical target, standard-function definitions and archived protected verification record were inspected. The receipt reports three kernel passes. Its 8,317-file source inventory was not completely audited and the kernels were not rerun. L04 and L14 have different evidence availability and are not assigned L01's receipt status.

Full primary text was unavailable for L08, L25 and L26 despite direct retrieval attempts. L28 was screened at journal abstract/metadata level. L18's author catalogue and explicit dependency disclosure were inspected, not its complete 65-page proof. L21–L24 retain their stated provenance and audit limitations. The additional Kominers lead is metadata-only.

No external numerical census, interval certificate, Schur certificate, or complete analytic proof was reproduced. RH-conditional moment/gap results remain conditional. Fixed-window positivity and finite-order total positivity remain finite. Real-axis zero exclusion is not promoted to complex zero exclusion, and zero density is not individual nonvanishing.

## Selection and omissions

Priority depends on a concrete connection to an inspected open interface, not just a title mentioning Riemann. Foundational older literature is included only where needed to interpret a revision or prevent duplicate work. General news coverage, duplicate indexes and unsupported proof announcements are not used as theorem sources.

The closed, explicitly unformalized `0.8392` submission and AI-community positivity notes remain labeled audit leads. Closing a tracker PR is not a mathematical refutation. Conversely, a lower advertised decimal, an exact scalar calculation, or an AI review is insufficient to establish its analytic input.

This is a dated snapshot. The search was broad but not exhaustive, and version status can change after the cutoff. Immutable source commits, versioned manuscript links and per-entry inspection notes support the next review. No third-party papers or dependency trees are redistributed in this packet.
