# Validation boundary and reproducibility

MCE26, 2026-09-13. Numerical certificates are conditional on the written
analytic remainder arguments in NUMERICS.md and PROOF.md. They are not
independent mathematical acceptance or machine-formal proofs.

## Accepting and weaker modes

`check.py --check result.json` authenticates this packet, reconstructs every
centered-F5 integral through degree28, every theta moment through degree32,
the complete source tails, all interval moment matrices, the perturbation
box, the permanent all-N coefficient tube, and the rational comparator.
Its result is compared using canonical JSON text, preserving numeric types.
Ordinary and optimized modes use the same 512-bit primitive.

`check.py --check result.json --receipt-only` instead authenticates the packet
and reruns its finite algebra using the stored source intervals. Its output
explicitly says it has NOT recomputed native integrals. This is the mode used
for the suites' pristine CLI control and most altered-receipt tests. It must
not be represented as a new native-source certificate.

`--emit PATH` freshly reconstructs the complete source but is producer-only.
A separate comparison/replay is required for acceptance.

## Test scope

The five-method suite checks exact power sums of 21 finite positive products,
five exact Gaussian-quadrature rational identities, five exact full-polynomial
differential residual identities, a fresh mesh320 theta computation and both
of its matrix signs, and actual altered-copy CLI tests. The two theta meshes
use one primitive; their agreement is supplementary and not an error estimate.

Each suite has one pristine RECEIPT-ONLY subprocess acceptance and ten actual
subprocess refusals: duplicate JSON, Boolean/integer alias, false RH status,
inflated moment degree, zeroed witness, altered rational numerator, altered
native coefficient, a resealed power-sum-recurrence code mutation, an extra
file, and a resealed changed gamma rate. Nine cases use receipt/finite-algebra
mode. The changed-rate case invokes full mode and fails its exact endpoint
source guard BEFORE quadrature; it is not a whole altered-integral replay.
All except the extra file are resealed to reach parser, algebra or source
checks rather than fail the original file digest. No symlink test is claimed.

## Development history and omissions

An ordinary mpmath scout suggested a rational negative vector for F5. It used
uncertified grids and did not define the accepting source intervals. Additional
uncertified N6/N7 explorations did not become certificates and are not used in
any theorem. No successful native rational-residual window was produced.

Early foreground attempts to integrate F5 were interrupted by the execution
wrapper; no completion is claimed for them. A later complete prototype run
and the final source reconstructions are distinguished in the delivery logs.
A trial permanent-tube threshold 2^160 failed the interval positivity test;
that failure was not called a native negative sign. The accepted threshold is
2^192, not a purported optimal threshold.

The qualitative moment criterion and Gaussian-quadrature construction are
classical. The proofs of source identification, Hamburger existence, entire
factorization, and uniform convergence are written/imported mathematics, not
proved by finite script execution. No prior gamma zero-certificate campaign,
new Xi zero, repository-wide build, Lean proof, remote CI, global arithmetic
covariance estimate, cofinal dimension sequence, or all-order Ising theorem
was established in this pass.

## Publication and archive checks

The inspected #875 parent is 177cf75e93b5614c5d5f0db1e4721ac69727e5ce. This
sibling standalone addition leaves earlier sealed directories untouched.
The direct GitHub connector exposed no create/push action; plugin discovery
found the installed read-capable GitHub integration. Direct Git failed to
resolve github.com. This author session does NOT claim remote publication.

Final executed command outcomes, exact code/result hashes and delivery
roundtrips are recorded outside this packet in DELIVERY.json and evidence/.
The publisher targets the existing #875 branch, checks ancestry and a clean
worktree, refuses existing packet paths, uses no force-push, and verifies the
actual remote and PR heads. It has not been run in this session.
