# PAPER-A005 — Knausgård: local interaction certificates

Kristian Muri Knausgård, [*More than 83.9% of the zeros of the Riemann zeta function are distinct and more than 67.35% are simple and on the critical line*, arXiv:2610.08965v1](https://arxiv.org/abs/2610.08965v1), 6 October 2026, preprint. Accessed 17 November 2026. **Initial L0 reading checkpoint (later component checks below):** abstract, introduction, main statements, selected certificate principle and §8/Table5 pp32–36. Whole-paper reading, computational replication and proof audit are not claimed.

Theorem1.1 states liminf Nd(T)/N(T)≥1645064/1960733=0.83900459… . Corollary1.2 gives Ns/N≥2Nd/N−1 (simple zeros anywhere); this must not be presented as a simple-critical-zero bound. Theorem1.3 separately concerns N0s/N, at least 0.67353… . These claims use local interactions among seven/eight consecutive zeros and telescope storage-function corrections. This is mathematically more specific than merely optimizing a single cosine window.

**Formal evidence boundary:** the abstract explicitly states three additional computational search axioms; Table5 identifies their dependencies. §8 pp35–36 says the search soundness is proved, while its full successful evaluation is carried out by native code/interpreter and recorded as an axiom. Thus “no sorry” is not synonymous with “kernel replay of every finite inequality.” The stated trust boundary includes Lean compiler/interpreter/runtime for three searches; the separate ceiling propositions7.2,7.3 are reported to use only standard axioms. This is a disclosed computational trust boundary, **not a verified mathematical error**.

The described branch counts exceed 60 million, 535 million and 572 million; they have not been rerun here. Numeric improvements on later webpages are candidates requiring dated source/certificate capture, not accepted records. No claim that this paper's constants remain the latest.

Actionable follow-up: pin repository commit and toolchain; inspect exported theorem types/axioms; replay search using an independently written integer checker; convert accepted leaves into small proof objects checked by the kernel. Track proof of search soundness, actual success, exact statement anchoring and analytic prerequisites separately.


Round2 scoped component update: the first-window author C++ search has since been reproduced, all three kernel tables independently checked, and separate finite-transfer/statement-semantic reviews completed; see audits/formal_artifact_round2.md and its evidence files. These later checks supersede the original no-execution checkpoint for those components only. The entire43-page paper has not been substantively read or fully audited, and no complete K839 Lean/analytic-zeta proof is certified here.

Current numeric update,17November2026: both later continuum searches completed through the independently reviewed checkpoint adapter and matched all five author-recorded counters. The first full search used byte-unmodified code; the later byte-unmodified attempts remain recorded as interrupted. See audits/839_later_window_search_formal62.md. This does not claim a local K839 Lean replay.
