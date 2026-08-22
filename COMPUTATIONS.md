# Computational and formal artifacts

> **No heavy campaign was rerun for the 2026-08-22 review or integration.**

A computational record has separate mathematical, method, artifact, and replay statuses. A retained hash does not mean an independent recomputation, and a finite certificate does not imply an infinite theorem.

| Computation | Family | Final status | Canonical scope | Method status | Artifact status | Heavy replay |
|---|---|---|---|---|---|---|
| `COMP.REVIEW.A.LIGHT` | **review_infrastructure** | `VERIFIED_WITH_FIXES` | review evidence | LIGHT_REPLAY_AND_REGISTRY_AUDIT | RETAINED | `NOT_APPLICABLE` |
| `COMP.REVIEW.B.LIGHT` | **review_infrastructure** | `VERIFIED_WITH_FIXES` | review evidence | INDEPENDENT_LIGHT_REPLAY | RETAINED | `NOT_APPLICABLE` |
| `COMP.REVIEW.C.FINAL` | **review_infrastructure** | `VERIFIED` | coverage/provenance lock | FIVE_FAIL_CLOSED_LIGHT_VALIDATORS | SHA256SUMS 35/35 at frozen head | `HEAVY_CAMPAIGN_NOT_RE_RUN` |
| `COMP.REVIEW.DIRECT_MAIN` | **review_infrastructure** | `VERIFIED` | direct-main audit lock | LIGHT_STRUCTURAL_AND_SYMBOLIC_REPLAY | SHA256SUMS retained | `HEAVY_CAMPAIGN_NOT_RE_RUN` |
| `COMP.XI.ORDER3.HISTORICAL_REPLAY` | **xi_pick** | `VERIFIED_WITH_FIXES` | order-three local algebra only | SOURCE_SCRIPT_UNRUNNABLE | CORRUPT_HISTORICAL_CHECKER | `HEAVY_CAMPAIGN_NOT_RE_RUN` |
| `COMP.XI.EXTERNAL_ZERO_HEIGHT` | **xi_pick** | `RETAINED_HEAVY_CERTIFICATE` | external input only | SOURCE_AND_USE_AUDITED | EXTERNAL_PUBLICATION | `HIGH_ZERO_VERIFICATION_NOT_RE_RUN` |
| `COMP.TARGET_LORENZ.51M` | **native_hall** | `GAP_BLOCKED` | method firewall/history | ROUNDING_INCLUSION_INVALIDATED_BY_PR516 | HASH_LOCKED_BYTES | `HEAVY_CAMPAIGN_NOT_RE_RUN` |
| `COMP.C4MBI.1E9` | **c4mbi** | `RETAINED_HEAVY_CERTIFICATE` | finite theorem only | OUTWARD_DYADIC_METHOD_AUDITED | RETAINED_ARTIFACT_HASH_VERIFIED | `HEAVY_CAMPAIGN_NOT_RE_RUN` |
| `COMP.HARNACK.2E9` | **factor67_lorenz** | `RETAINED_HEAVY_CERTIFICATE` | finite computer-assisted theorem | SCANNER_COMBINER_VERIFIER_AUDITED | RETAINED_ARTIFACT_HASH_VERIFIED | `HEAVY_CAMPAIGN_NOT_RE_RUN` |
| `COMP.SHARP.H67.1E8.PR647` | **sharp_native** | `RETAINED_HEAVY_CERTIFICATE` | finite theorem only | DIRECTED_INTERVAL_LOGIC_AUDITED | RETAINED_ARTIFACT_HASH_VERIFIED | `HEAVY_CAMPAIGN_NOT_RE_RUN` |
| `COMP.SHARP.H67.1E8.PR653` | **sharp_native** | `RETAINED_HEAVY_CERTIFICATE` | second finite provenance chain | ARTIFACT_AND_METHOD_AUDIT | HASHES_RETAINED | `HEAVY_CAMPAIGN_NOT_RE_RUN` |
| `COMP.P61.BIAS` | **factor67_lorenz** | `VERIFIED_WITH_FIXES` | finite/local theorem | ENDPOINT_CONTRACT_AUDITED | RETAINED | `HEAVY_CAMPAIGN_NOT_RE_RUN` |
| `COMP.Q4.ANNULAR_KERNELS` | **q4** | `VERIFIED_WITH_FIXES` | finite Q4 reduction | LIGHT_EXACT_REPLAY_AND_METHOD_AUDIT | RETAINED | `BROAD_ENDPOINT_SCAN_NOT_RE_RUN` |
| `COMP.Q4.FIVE_MILLION_RECON` | **q4** | `EMPIRICAL_ONLY` | historical observation | NOT_REVIEWED_AS_PROOF | RETAINED_OBSERVATION | `NOT_RERUN` |
| `COMP.BROWNIAN.BOHR` | **brownian_weil** | `VERIFIED_WITH_FIXES` | mechanism firewall | REVIEW_IMPORTED_AND_RECONSTRUCTED | RETAINED | `BROWNIAN_SCANS_NOT_RE_RUN` |
| `COMP.FINITE.ROBIN` | **finite_certificates** | `RETAINED_HEAVY_CERTIFICATE` | finite theorem only | IMPORTED_REVIEW | RETAINED | `LARGE_SCAN_NOT_RE_RUN` |
| `COMP.FINITE.PICK_BOXES` | **finite_certificates** | `RETAINED_HEAVY_CERTIFICATE` | finite exclusion only | IMPORTED_REVIEW | RETAINED | `MATRIX_SEARCH_NOT_RE_RUN` |
| `COMP.FREDHOLM.FIXED_DEGREE` | **brownian_weil** | `VERIFIED_WITH_FIXES` | no-go theorem | METHOD_AUDITED | RETAINED_FIXTURES | `NYSTROM_AND_MATRIX_SWEEPS_NOT_RE_RUN` |
| `COMP.DIRECTMAIN.P79.INVALID_CERT` | **direct_main_p79** | `FALSE` | method refutation | EXACT_CAUSAL_SUPPORT_COUNTEREXAMPLE | RETAINED_HISTORICAL_SOURCE | `HEAVY_CAMPAIGN_NOT_RE_RUN` |
| `COMP.DIRECTMAIN.L91355` | **direct_main_p79** | `VERIFIED_WITH_FIXES` | source-ledger theorem only | LIGHT_EXACT_REPLAY | HASH_LEDGER_PRESENT | `NOT_APPLICABLE` |
| `COMP.DIRECTMAIN.T99930` | **direct_main_taylor** | `VERIFIED_WITH_FIXES` | local algebra and standalone supercritical theorems | LIGHT_EXACT_REPLAY | RETAINED | `NO_HEAVY_CAMPAIGN` |
| `COMP.FORMAL.LEAN` | **formalization** | `GAP_BLOCKED` | formalization backlog | DEPENDENCY_LOCKS_INCOMPLETE | EXCLUDED_FROM_CURRENT_EXTRACTION | `FULL_BUILDS_NOT_RUN` |

## Canonical wording

For retained campaigns the release uses:

```text
RETAINED ARTIFACT HASH VERIFIED
METHOD / CONTRACT AUDITED
HEAVY CAMPAIGN NOT RE-RUN
```

The major retained campaigns include finite Robin and Pick controls, primitive-prefix and Harnack scans, SHARP finite ranges, Q4 kernels, Target-Lorenz artifacts, external high-zero verification, and formal-build references. Their exact limitations are in [`integration/2026-08-22/COMPUTATIONS.tsv`](integration/2026-08-22/COMPUTATIONS.tsv).
