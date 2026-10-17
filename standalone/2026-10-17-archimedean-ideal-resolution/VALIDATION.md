# Validation and exact limits

Status: same-author mathematical reconstruction and finite diagnostics.
No independent mathematical referee, external proof-assistant build, upstream
CT/DF theorem verification, remote CI or full-repository validator was run.
The written infinite estimates are proposed proofs, not consequences of the
number of finite predicates. A manifest authenticates bytes, not mathematics.

## Exact checker

`python check.py` and `python -O check.py` both reproduce CHECKS.json byte for
byte. The final report has **10,021 explicit predicates including setup**.
It uses Python integer/Fraction arithmetic, not floating-point tolerances.

Coverage:
- All 311 nonzero integral ideals through norm 512, generated as Eisenstein
  lattice orbits under all six units. All 512 norm counts agree with an
  independently assembled rational-prime Euler count. There are 95 prime
  ideals, 157 good ideals, and 147 good squarefree ideals in this cap.
- Exact generator, factorization and unit-independent angular-character
  identities; both norm-seven split ideals are retained.
- Every good squarefree column in each hard annulus (X/2,X], and every
  nonzero element row in its stated ball: (X,H)=(32,13),(64,79),(128,13).
  Column/row counts are (5,54),(7,294),(19,54). Orders two and four at angular
  modes -1,0,1 are assembled directly and through complete product ideals.
  The extra angular values are rational numbers in the report, not rounded.
- Local majorant/squared-weight identities at m=2,3,4,6,8 and nine good prime
  ideals through norm 31, using 720 exact weighted terms. These are local
  finite tests, not complete ideal censuses at the large powerful norms.
- Matching local factors at k=1,...,8, rational near-isometry constants,
  short-radial exponent/logarithm bookkeeping at k<=12, and two #959 theta/
  Mellin-shift identities. This is NOT a replay of all #959 proof gates.

Five deliberately corrupted optimized processes were executed. Each exits
nonzero, as recorded in MUTATIONS.json: erasing the nonunit mask, erasing the
angle, omitting the sixth unit power, collapsing ideal keys to norms, and
replacing the strict Schur constant by a false value. These controls test
specified algebraic conditions, not adversarial completeness of a proof.

## Non-certified numerical checks

`python numerics.py` and `python -O numerics.py` reproduce NUMERICS.json
byte for byte at 70 mpmath decimal digits. The 3,149 numerical predicates
include 20 discrete/wrapped Gaussian Fourier comparisons, four direct
log-scale integrals for the full Gaussian pair kernel, and the geometry of
all 40 ideals through norm 64. These are ordinary high-precision calculations,
NOT directed intervals, certified tail enclosures, or asymptotic evidence.
The discrete Fourier sum is truncated at 18R and the wrapped numerical sum
at five images on each side; the actual theorem uses the infinite sums.

The finite scalar fourth-moment example includes all seven good squarefree
columns in (32,64]. Its ideal-product diagonal is 91, its norm-product diagonal
is 289, and its principal unaveraged value is 625. The full finite hybrid mean
at R=64 is approximately 90.9999999993529, and at R=128 it differs from 91 by
less than the report's 25 displayed digits. Neither is an estimate at unbounded X.
The full Gaussian kernel checks keep the minus sign in the CDF shift.

## Corrections during development

An initial checker included an unjustified expectation that the complete
native moment is even in angular index l at fixed radial center. The actual
sextic row correlations need not have that symmetry. The failed assertion was
removed; both unequal exact values are now reported. The theorem only needs
unit invariance of psi and bounds uniform in centers, not this false symmetry.
No proof statement was based on it. A numerical report variable-shadowing bug
was corrected before the two successful complete replays. Failed runs are
not counted as successful validation.

## Reproduction

From this directory:

    python check.py > /tmp/exact.json
    cmp CHECKS.json /tmp/exact.json
    python -O check.py > /tmp/exact-opt.json
    cmp CHECKS.json /tmp/exact-opt.json
    python numerics.py > /tmp/numeric.json
    cmp NUMERICS.json /tmp/numeric.json
    python -O numerics.py > /tmp/numeric-opt.json
    cmp NUMERICS.json /tmp/numeric-opt.json
    python verify_manifest.py

For each name in MUTATIONS.json run `python -O check.py --mutate NAME` and
require a nonzero exit. Normal arithmetic needs only Python's standard library;
optional numerics needs mpmath. No software-library current-version claim is made.

## Publication and the remaining gap

Publication uses connected GitHub Git-data actions, not a claimed cloned clean
worktree. The intended parent is #959 at
7b845294207d96b883c1fa95028663082267804f. Only this new standalone directory
is added. Final remote SHA/blob read-back belongs to the PR receipt, not to
an assertion that independent mathematical review took place.

The main remaining problem is the critical original fixed-principal-twist
signed covariance. A full averaged theorem is not that pointwise theorem.
The new short-radial refinement improves logarithms in the SAME average;
the stronger hybrid theorem has an extra average and explicitly priced
volume. No 17/24, new Dedekind boundary, RH or zero-ordinate band is asserted.
