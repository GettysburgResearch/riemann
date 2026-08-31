# Review of the accepted single top witness

The accepted artifact is frozen at `4019ecd9d0b674fa6d9b26eee2c70c2717f33543`. Its executable contract remains the previously reviewed `596189377cb5d167c95334bfc5ddb74af2d1cc5f` contract.

| File | Git blob |
|---|---|
| `single_top_witness.py` | `148a8d9523b30a71b5b49ba92bf957e64a25dbe4` |
| `SINGLE_TOP_WITNESS_PREREGISTRATION.md` | `2ad3d6dc7140f185d9c1eb0ee0b0f4ecbc2d63ad` |
| `SINGLE_TOP_WITNESS_REPLAY.md` | `7e3dc118419af96630b57d5177828ff551c691e1` |
| `single_top_witness.verification.json` | `86795a55ffb4751bbcad7a93a0a44b8e62b461ec` |
| `tests/test_segre_hadamard_single_top_witness.py` | `92f6434a53b55dd6b7189d95141f1a29b6f12194` |

The reviewed working bytes agree with these frozen blobs. I previously read the complete producer, declaration, replay note and all 26 tests; the accepted artifact supplies the previously pending successful outcome. Its proof-object digest is `31507a0ebecc931dc2073cd2c81df45c1c25f182cf2da9c6ece483cd8d54ba0a`.

The first registered prime, 65521, succeeded. The failed first-lift reconstruction remains in the artifact, followed by acceptance at the second lift. Acceptance retains all 592 original central columns and all 49 older central multiples. The complete old-coordinate minor has nonzero determinant 2670 modulo 65521, while every one of its 49 gauge coordinates vanishes on the accepted nonzero primitive integer vector. The exact residual is empty against all 2190 supported original target rows. This is the required exact nonmembership certificate; it does not infer a rational nullity from a modular rank or omit unselected target rows.

The accepted top vector has 379 nonzero terms, degree seven and weight `(7,7,7)`. The complete polynomial output retains 29 `D3` columns, distributed as 11 in degree five, 17 in degree six and one in degree seven. The fresh polynomial ledger checks every `D1 D2` composition and every `D2 D3` composition, with all residuals zero. Earlier source maps and their proved rank/minimality inputs remain explicitly authenticated imports, rather than newly rerun lower-stage eliminations.

The complete-resolution conclusion uses the frozen central-top promotion theorem. The global dimensions 775 and 776 remain labeled deductions after acceptance, not measured whole-matrix dimensions. The artifact does not claim completion of the older full-kernel, full-composed or larger replay contracts, nor equivariance of the chosen polynomial lifts.

The coordinator reports write/check/optimized-check and all 26 ordinary plus 26 optimized tests passed before this freeze. I performed no scientific rerun: this is an independent source, contract, binding and artifact review, with execution attributed to the coordinator. No blocker was found.

Independence disclosure: I authored `CENTRAL_TOP_CLASS_GLOBAL_EXACTNESS.md`, so this report does not independently review that theorem. Its separate independent proof review is `REVIEW_ed8c7251.md`. My independent review here concerns the separately authored witness algorithm, its acceptance obligations, tests and recorded successful execution.
