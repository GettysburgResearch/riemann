# Validation record

Date: **2026-10-09 UTC**. Status: **source integrity and exact finite algebra
passed; imported analytic theorems and proposed transfers remain under review**.

The companion is based on Riemann commit
`31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6` (PR #908). The complete logical source
view is pinned to OpenAI commit
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`; the inherited core retains its
separate original pin. The PR description identifies the exact published
companion head. The checked scripts and source-manifest hashes are recorded in
[validation-context.json](checks/artifacts/validation-context.json).

## Checks actually performed

| Check | Result and exact scope | Evidence |
| --- | --- | --- |
| Source selection versus frozen Git tree | PASS: all 11,940 paths, Git blobs, SHA-256 hashes, byte counts and modes; complete selected manuscript directories and internal imports | [Source verification](checks/artifacts/source-verification.json) |
| Original core preservation | PASS: the inherited verifier checked all 3,286 historical source files, including comparison against its original frozen Git tree; no core file is changed in this contribution | Same source verification and the PR diff |
| Resident-only integrity and closure | PASS during assembly: required files, canonical origins, lexical closure and recorded audit agree; this mode does not authenticate full directory completeness without Git | [Assembly run](checks/artifacts/assembly.json) |
| New checker fixtures | PASS: 21 isolated cases, including rejected corrupt bytes, invalid policy metadata, omitted dependencies/PDFs, duplicate storage, symlinks, stale audits and unsafe paths | [Fixture results](checks/artifacts/source-bundle-fixtures.json) |
| Fresh assembled view | PASS: separately enumerated every path and checked every SHA-256, size and executable mode; no extra or missing files | [Assembly comparison](checks/artifacts/assembly-comparison.json) |
| Complete upstream drift | PASS: 1,185 changed paths globally; six modified and one new metadata file in the selected view; zero changed selected implementation modules | [Drift report](checks/artifacts/upstream-drift.json) |
| Internal formal-source inventory | 11,576 implementation modules / 1,414,189 lines; zero missing static internal imports or scanned implementation markers; 762 external module imports recorded | [Lexical audit](checks/artifacts/dependency-audit.json) |
| Exact Möbius identities and completed energies | PASS: every prefix through 512, with independent ordinary-Möbius and norm-Euler constructions | [Arithmetic results](checks/artifacts/native-mobius-check.json) |
| Rational floor endpoints | PASS: 1,539 inputs, including strict-left/closed-right interval boundaries | Same arithmetic results |
| Gram identities | PASS: all 4,900 entries through cutoff 24, compared in three exact forms | Same arithmetic results |
| Native block means | PASS: all 169 cubic-mesh blocks through input 12, in native, ideal-source and old-prefix Newton coordinates | Same arithmetic results |

The checker fixtures intentionally mock the original core verifier on small
temporary examples to isolate the new code. The real source verification and
assembly use the unmodified historical verifier; no mock is used there. A
positive fixture confirms the stated offline limit: deleting an unreferenced
manuscript file cannot be discovered without the full upstream Git inventory.

The arithmetic checker uses integers and `fractions.Fraction`, with no
floating-point tolerances. It explicitly rejects three tempting shortcuts:
omitting the local restoration at 3, replacing signed norm coefficients by
their absolute values, and assuming those coefficients are one-bounded. These
are checks of finite identities and their implementation, not evidence for an
unproved asymptotic bound.

## Mathematical and source review

The source-selection review checked all ten companion families, 22 additional
manuscript directories, and eight new comparator pairs, alongside the four
inherited pairs. Resident links and the pinned upstream references in the
related-results review were checked against the selected source tree.

The native bridge was checked against the inherited boundary-energy and NRC32
definitions, including the reciprocal weights, endpoint cell counts, Newton
range, completion term and monotone state. The research programme retains the
failed full MHB32 bootstrap and CAP36's restricted difference estimate. These
are focused source and algebra reviews, not a complete independent proof audit
of the imported papers or an exact-head acceptance review by an integrator.

## What was not performed

No fresh Lean elaboration, kernel run, Comparator equivalence check, independent
Nanoda run, external-package implementation audit, or complete analytic proof
reconstruction was performed. `lean`, `lake`, `comparator`, `landrun`, and
`lean4export` were unavailable in the execution environment. Their absence does
not change the source checks into formal verification.

No all-scale native covariance inequality, smooth-to-sharp analytic transport,
or new zero-free strip is established by these runs. Inherited numerical
campaigns were not rerun. RH remains open.

## Reproduction

The commands and toolchain requirements are in [REPRODUCE.md](REPRODUCE.md).
After assembly, the independent file comparison is:

```sh
python checks/check_assembled_view.py /tmp/openai-riemann-selected
```

Review the mathematical notes and exact source selection before extending the
analytic programme. A subsequent proof or formal replay should receive a new
scoped record at its own frozen commit.
