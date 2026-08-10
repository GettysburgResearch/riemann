# Proposed results-index row after independent review

This snippet is intentionally not applied automatically. Insert it only after an exact-SHA analytic review and a clean external Lean replay.

| Registry family | Strongest surviving statement | Status / scope / residency | Dependencies, conflicts, and why it matters | Exact next step | Exact source and review |
|---|---|---|---|---|---|
| `EXTERNAL-ANTHROPIC-ZETA23` | Unconditionally, asymptotically at least `2/3` of zeta zeros are simple and on the critical line and at least `5/6` are distinct; optimized constants `0.67250...` and `0.83625...`. | `IMPORTED`; promote to `VERIFIED / global asymptotic / SOURCE_PINNED` only after repository-side review | Uses a finite Gabor compression of Weil's Hermitian form, hyperbolic off-line blocks, a rank–trace inequality, and the unconditional bandwidth-one pair-correlation second moment. It does not prove RH. | Complete clean Lean/comparator replay; source-dictionary review; then extract the theorem and B0 normalization packet. | Claude paper PDFs locked in `SOURCE_LOCK.json`; `anthropics/zeta-23-lean@3635e74826a4c1fcece7d1cd2b6fa75e43a00510`; repository-local review TBD. |
