# Validation and unperformed checks

The scientific status is PROPOSED COMPONENT PROOFS / REVIEW REQUIRED.
Uniform full-source block gain, subpower full energy and RH are not proved.
No finite test count is an acceptance of those unbounded statements.

## Bounded replay commands

From `standalone/2026-09-06-astra-balanced-lift/`, with the two original sibling
packets present:

```bash
python3 scripts/replay.py --check
python3 -O scripts/replay.py --check
PYTHONDONTWRITEBYTECODE=1 python3 scripts/test_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -O scripts/test_replay.py
```

The replay reconstructs 3,884 controls per mode. Its scope is declared in
NUMERICS.md and the exact configuration in verification.json. Acceptance uses
canonical-JSON reconstruction plus a nonempty exact nine-file checksum inventory.
The manifest itself is intentionally excluded from its hash list.

Ten unit tests include twelve ACTUAL CLI corruption cases in each mode:
changed RH flag, changed subpower-proof flag, altered full-energy endpoint,
empty numerical scope, duplicate JSON key, float alias, altered primitive source,
wrong parent SHA, changed consumed parent code, changed proof without resealing,
empty checksum inventory, and an extra payload file. Result/semantic cases are
resealed where appropriate; refusals therefore test more than payload hashes.
Separate unit tests check bool/float memoization aliases, resource limits,
exact constraints including index 9, singular rational solve rejection, strict
JSON parsing, source authentication, and symbolic/duplicate inventory rejection.

The numerical full-norm fixtures are M=4,8,16 only. Their infinite-Gram tails
are included through a proved analytic remainder; no broad source horizon is
evaluated. The much longer middle range in BL26.E is a mathematical target,
not a computation that has been completed.

## What each validation layer establishes

- Rational KKT solves agree with the explicit divisor-incidence optimizer.
- The exact signed source agrees cellwise with its fractional-part definition.
- The complete infinite Gram, not a finite partial norm, gives the three full
  energy/target/error rows.
- The constrained coherent perturbations satisfy the two homogeneous equations,
  KKT orthogonality, exact plateau and quadratic energy comparisons.
- Corruptions do not silently become valid under optimized Python.
- Source hashes authenticate the consumed predecessor bytes, not their theorem
  status or the correctness of an arbitrary fully replaced checker.

The parent's numerical code is an explicit dependency, authenticated before
source-byte compilation. The original parent's cap-16 implementation and its
manifest are unchanged. The new cap-32 implementation reconstructs the same
analytic formula independently at the code level but shares the authenticated
interval primitives and their numerical remainder proof. The overlap tests
are not claimed to be an independent numerical library audit.

## Execution receipts and publication

Normal/optimized replay, unit/CLI logs, archive/patch checks and publication
status are retained in the delivery receipt outside this self-hashed packet.
Only successful commands recorded in that receipt are claimed executed. The
packet's content and checksum list can be regenerated offline from its inputs.

The frozen source has been observed through authenticated GitHub reads. No
branch push is implied by having a local artifact. The current pass's connector
exposes GET/read actions only, and the local Git connection failed DNS. A local
add-only patch and ZIP are delivered for publication; the exact existing PR/head
and any later successful remote operation are stated separately in the receipt.
No research branch, main, permissions, repository settings, canonical entry, or
Lean source has been altered by producing this local packet.

## Unperformed and unresolved

No Lean build, proof-kernel verification, independent referee review, Windows
execution, remote CI run, zero census, prime campaign, unbounded matrix campaign,
or full-repository checkout validation was performed. The original Windows
path portability issue in the predecessor is not silently repaired here.

The source-normalization and coefficient-rate proofs are new proposed arguments,
not imported PNT statements. The Mellin growth implication is analytic and not
machine-proved by the finite rational checker. BL26.E is the exact remaining
arithmetic estimate. Its validity is neither inferred from the three small
norms below one nor disproved by the deliberately perturbed coherent family.
