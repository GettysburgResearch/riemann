# Validation and exact evidence scope

This packet contains mathematical proofs and exact finite diagnostics. The diagnostics check selected algebraic identities, signs, multiplicities, and interpolation bookkeeping. They do not prove an asymptotic Möbius estimate, either capture hypothesis, a full source moment, a zero-free improvement, or RH. No Lean formalization or external peer review is claimed.

## 1. Executed finite checks

All four checkers were run successfully by the root after the contributing agents supplied their files. All comparisons use exact integers or rational arithmetic; none uses a floating-point tolerance.

| Checker | Primitive input and coverage | Result and limit |
| --- | --- | --- |
| `checks/check_periodic_transfer.py` | Four independently specified piecewise-linear rational sources, 479 rational scales, 1,916 direct-dilation/partitioned-Abel-integral and sign comparisons; 10,000 periodic-prefix checks. Both positive and negative outputs occur. | PASS. Checks the causal boundary and the one-sided identity on these finite inputs, not the general operator theorem. |
| `checks/check_abelian_companions.py` | Independently generated ideal reciprocal coefficients from the splitting types in the degree-four field `Q(zeta_12)`. Six restoration masks, 7,200 coefficient comparisons through integer norm 1,200. Four controls that deduplicate equal prime-ideal norms fail as expected. | PASS. Verifies an example of the abelian coefficient bridge, including ramified and repeated-norm factors. It does not prove estimates uniform in a growing field. |
| `checks/check_zeta_bridge_capture.py` | 729 assignments of six prime ideals to a deleted set, replica support, or neither; 116,640 coefficient comparisons through norm 160; eight formal local patterns through degree 12; six rejected incorrect constructions. 11,089 node patterns and 55,445 rational interpolation evaluations; all subsets for block length at most 12 and declared edge/spread patterns beyond that. Two pinned source hashes replayed from the parent commit. | PASS. The larger grid census is deliberately partial. No arithmetic capture or universal interpolation theorem is inferred from it. |
| `checks/check_native_heat_defect.py` | 26,411 counted identity checks over all 2,401 (`7^4`) sextic-root/nonunit-zero coordinate patterns, with actual prime-norm multiplicity weights. Includes local decomposition, masked gcd decomposition, the coprime defect, heat intertwining, and the Möbius gauge. | PASS. Its pointmass witness is a finite algebraic witness, not a counterexample using the physical radial Schwartz row measure. |

The committed output records are in `results/`. The heat checker prints 28,812 by adding its 2,401-pattern census to its 26,411 identity counters; the table separates those quantities. The bridge and heat records bind the exact checker and proof hashes they ran; the publication manifest binds all other files. The heat checker also passed under `python -O`, with the same result bytes. The source inventories verify 21 exact repository snapshots.

## 2. Reproduction

From this packet directory, using any Python 3 environment with the standard library:

```bash
python checks/check_periodic_transfer.py
python checks/check_abelian_companions.py
python checks/check_zeta_bridge_capture.py --repo ../.. --manuscript EXACT_ZETA_BRIDGE_AND_SPARSE_CAPTURE.md --report /tmp/riemann_zeta_bridge_capture.json
python checks/check_native_heat_defect.py --proof NATIVE_HEAT_DEFECT_AND_PRIME_REMOVAL.md --output /tmp/riemann_native_heat_defect.json
```

The explicit proof/report paths account for the checkers being stored in `checks/`. The two JSON-report checkers reproduce the committed reports when run against the stated frozen source files and parent objects. The other two print their deterministic JSON reports on standard output.

## 3. Analytic proofs and independent review

The theorem files were frozen in source commit `ea94f3e40b2755de0ffb9ac7727faa820e0c4cd0`, tree `6622be6afbf5e293a07c71b2a9b556640557cc3f`, with parent `ab98878279cd5614fe79bb94aa916e97c9ee50b4`. Formal review was requested only after that actual GitHub commit existed and was fetched locally. Every receipt identifies the exact `git show` bytes it reviewed. A following commit appends review and replay records, this validation update, and the publication verifier without changing any reviewed theorem file.

The review assignments are deliberately separated from authorship. The periodic, abelian, and native heat notes have a review by `signed_sector`; the bridge and literal short-factor extension have a review by `descent_synthesis` and a primary-agent review; the average, base collision theorem, and exact signed endpoint have a fresh review by `fresh_frozen_review`. The primary agent also checked the signed endpoint. The review by `descent_synthesis` discloses its contribution to that endpoint sharpening and authorship of the base collision dependency, so it is not presented as an independent check of those contributions. Each report records its own narrower scope and earlier collaboration.

The reports and exact target hashes are indexed in [REVIEW_INDEX.json](REVIEW_INDEX.json), with the full receipts in `reviews/`. These are AI mathematical reviews within one collaboration. A separate-author check is not external peer review, proof-assistant verification, or a guarantee of correctness.

The frozen bridge checker was independently rerun by `descent_synthesis`, including six original commit:path comparisons against packet snapshots; its report reproduces the committed result exactly. `signed_sector` extracted all three other frozen checkers and ran each under normal and optimized Python; all paired output reports were byte-identical. Its three explicit optimized-mode fault probes were rejected without changing source bytes. The supporting driver and extracted inputs are preserved in `reviews/frozen_review/`; its historical absolute scratch paths in extraction metadata are provenance, not needed by the relative-path replay driver. These are independent executions of the authors' checkers, not independently developed mathematical oracles.

The source copy of `paper2.tex` retains its original trailing whitespace so that its hash matches the imported source. The whitespace check passes for the authored changes. The bridge manuscript's author-stage report name `zeta_bridge_capture_diagnostic.json` is published here as `results/zeta_bridge_capture.json`, whose bytes and hashes are recorded above.

## 4. Publication integrity

`SOURCE_FREEZE_MANIFEST.json` records the 43 source files present before review, excluding that manifest itself. `MANIFEST.json` records the final packet files, excluding itself. The sole changed file from the frozen packet is this validation record; the theorem, checker, source-snapshot and other frozen bytes remain unchanged. The root README navigation is also checked against the frozen source commit.

From this directory, run:

```bash
python checks/verify_packet.py
```

The verifier checks the final file inventory, frozen source commit/tree/parent, original source-file hashes, unchanged reviewed bytes, all 21 source-snapshot hashes, report hashes and exact review targets, and at least one separate-author review for each of the eight proof notes. It checks publication integrity and the disclosed review coverage. It does not decide whether a mathematical proof or imported input is true.

The elementary bridge, periodic and abelian transfer, capture implications, principal-average analysis, native finite heat identities, and collision lower bounds do not assume the imported OpenAI quasi-Riemann theorem. Their explicitly named classical inputs remain visible. The retrospective audit reports some older claims at their source-conditional scope; its discussion is not an independent certification of the imported theta foundation or the external conductor theorems.

The missing arithmetic statements remain open after every finite check and review. In particular, review of an implication from a signed-quantile estimate does not establish that estimate for actual Möbius sums.
