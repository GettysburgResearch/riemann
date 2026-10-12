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

The intended theorem files and hashes will be frozen in one source commit before requesting formal review. Independent reviewers will identify that exact commit and the file hashes they inspect in separate reports. A following commit may append those reports and update this validation record without changing the reviewed mathematical source bytes.

The elementary bridge, periodic and abelian transfer, capture implications, principal-average analysis, native finite heat identities, and collision lower bounds do not assume the imported OpenAI quasi-Riemann theorem. Their explicitly named classical inputs remain visible. The retrospective audit reports some older claims at their source-conditional scope; its discussion is not an independent certification of the imported theta foundation or the external conductor theorems.

The missing arithmetic statements remain open after every finite check and review. In particular, review of an implication from a signed-quantile estimate does not establish that estimate for actual Möbius sums.
