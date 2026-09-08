# Execution and trust boundaries

The following commands were executed in this authoring session, not merely
proposed. New checks use Python's standard library, exact Fraction arithmetic,
and an explicit Q(i) class. No floats or external zero table enter them.

## New continuation

    python verify_pass2.py --check exact_result.json
    python -O verify_pass2.py --check exact_result.json

Both performed 4,104 finite checks and produced byte-identical JSON. Groups
include global-tail constants, the small-time core and infinite-band majorant
constants, the finite parameter comparison for M=10^15, exact mixed/heat/
Laguerre identities, Bernstein mass and degree elevation, Hardy norm bounds,
Mobius normalization, and the parent's false-closure polynomial control.
The whole 10^15 order range is a consequence of the analytic parameter
theorem. It was NOT enumerated by this program.

Two deliberately corrupted retained JSON files were rejected, with nonzero
return codes: an altered check count under normal Python, and a false RH
status under optimized Python. See execution_validation.json. These test
fail-closed replay behavior, not mathematical truth of arbitrary statements.

## Parent replay, with bytes preserved

The uploaded parent archive was extracted without rewriting its content.
All 12 original Git blob IDs were independently recomputed and matched the
publication receipt for bc3c35d8f434949748a2185783bf831d3afd9126.
All 11 entries in its original SHA256SUMS passed.

The parent's verify_exact.py passed its 225 checks in both modes, with
identical outputs. Its verify_low_zero.py also ran in both modes; each output
was byte-identical to the original low_zero_result.json. That interval
calculation verifies a sign change, not a complete zero census. Its mpmath
1.3.0 interval Gamma implementation remains an explicit software dependency.

## What is not claimed

- No proof assistant checked any of the analytic theorems.
- No independent referee or second mathematical agent reviewed this pass.
- No Platt--Trudgian full verification was rerun.
- No direct infinite-zero heat computation was performed.
- No source-side exp(o(n)) theorem or full RH proof was established.
- No remote commit, CI run, or publication of this continuation occurred.

## Patch and transport

The downloadable patch is add-only under the new pass2/ directory. It was
applied in an isolated reconstruction containing the authenticated original
12 files; every resulting new byte matched the authored packet and every
original blob remained unchanged. The replay from that applied patch also
passed. The reconstruction is not represented as a full checkout of the
historical repository.

The application helper checks the ACTUAL repository HEAD against the frozen
parent, verifies the original blobs, refuses a dirty tree or a pre-existing
pass2 path, and runs git apply --check before applying. It does not commit,
push, merge, or infer that a mathematical review succeeded.

SOURCE_LOCK.json records dependencies; SHA256SUMS authenticates the new
packet's exact bytes. These hashes establish identity, not mathematical
soundness. The release-level DELIVERY_RECEIPT.json records patch identity
and application-test results separately.
