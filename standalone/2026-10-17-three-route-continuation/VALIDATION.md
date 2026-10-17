# Validation contract and recorded outcomes

Date: 17 October 2026. All new mathematics remains **PROPOSED**. These
computations check specified finite identities, complete finite partitions
and two directed root certificates. They do not test the truth of RH,
compute the analytic family means, rebuild imported theorems or substitute
for the written mathematical review.

## One-command replay and complete byte inventory

From this directory:

```sh
python3 verify_packet.py
python3 verify_packet.py --replay
```

`MANIFEST.json` records every packet file other than itself, with relative
path, byte length, SHA-256 and Git blob identity. The verifier rejects a
missing, extra or changed file, ignoring Python bytecode caches. The replay
then regenerates six rational reports, the complete Newton audit and both
Lee--Yang receipts, comparing them with the stored objects. Temporary
Newton output is written outside the packet.

All replay dependencies are included. Standard Python 3 is sufficient;
no solver, external moment table, network call or third-party package is
used. The analytic primary sources are citations, not runtime inputs.

## Critical component checks

| Script | Exact scope | Recorded result |
|---|---|---|
| `critical/verify_interpolation.py` | 100 rational exponent instances; dependent-subset and omitted-conductor negative controls | PASS |
| `critical/verify_diagonal.py` | Four cleared algebraic identities, native missing-pole control, strict margin `2377/4860` | PASS |
| `critical/verify_local_domain.py` | 1,161 explicit predicates, including setup; all 20 surviving support-branch first terms, common period, all six assembled valuation cases and negative controls | PASS |
| `critical/review_theta_independent.py` | All 2,674 row exponents and full stated epsilon interval, independently reconstructed without importing the main checker | PASS |

All four scripts produce identical JSON under ordinary Python and
`python3 -O`; acceptance uses explicit failing guards. The first three
reports bind their corresponding proof and checker hashes. The local
finite predicates are not 1,161 independent analytic cases or prime
samples. Infinite support exhaustion and analytic convergence are proved
in the written argument.

## Proposed 9081/10000 comparison

`theta/verify_theta.py` enumerates every one of 2,674 classes with 2,673
thresholds: 173 second-mean, 1,700 interpolated and 801 convexity cases.
All required exponent inequalities hold over the whole interval
`0<e<=1/1000000`, using rational polynomial positivity, not a floating
point grid in `e`.

The least middle-class constant margin is

    20321474869/416197180000000.

The independent reconstruction reproduces it. The main checker also
checks the density substitutions, full-height losses, reciprocal disks,
contour domains, principal powers, changed small-norm cutoff and complete
large-tail gap. Ordinary and optimized output are identical.

Six deliberately corrupted executions were actually run and rejected at
the recorded guards: old numerator exponent; omitted conductor cost;
wrong partition count; old small cutoff; old Mellin shift; zero tail gap.
The optimized corrupted runs also fail. The saved
`theta/VALIDATION.json` gives each rejection and binds the corrected proof,
checker and complete report. These controls test that the corresponding
bookkeeping errors are detected; they are not tests of analytic premises.

## Proposed 49/54 fourth-mean composition

`theta/verify_fourth.py` uses 1,641 exact rational thresholds and all
1,642 classes: one second-mean class, 500 central fourth-mean classes,
1,140 interpolated fourth-mean classes and one final convexity class.
The frozen choices are

    a=4/9, h=5/9, theta=2/9, Mellin shift=37/54,
    z=2/5, small-norm cutoff=1/1000, small-norm z=1/3.

All inequalities are checked on `0<e<=1/1000000`. The least middle-class
constant margin is

    118384121/35223109200.

The good-class estimate has a zero-loss tie with a sufficient positive
epsilon budget. The actual small-norm line, principal corrections and
complete tails are included. No assertion about the boundary line follows.

Ordinary and optimized output are identical. Six actual optimized
corruptions fail: replacing the fourth mean with the old second mean;
omitting the conductor; wrong partition count; restoring the old small
line; changing the Mellin shift; and deleting the positive tail gap.
`theta/FOURTH_VALIDATION.json` records all failures and exact file hashes.
This is bookkeeping for the stated original density input, not a test
or import of #966's new selected-character density theorem.

## Native Newton replay

`newton/check_newton.py` completely checks 22 `(Y,q)` cases, using
`Y=1,2,3,4,7,10,15,31` and the distinct choices among
`q=1,2,bitlength(Y+1)`. It constructs the input Mobius prefix by trial
factorization and compares completed coefficients with an independent
linear Euler sieve. It checks all blocks, exact quadratic means, complete
orthogonal energy, deterministic detail bounds and source controls.

For the largest case the old prefix through 31 supplies every new cell
through 1023. The endpoint 1024 is excluded by the theorem and checked
against the actual square-endpoint defect. Positive and delta controls
verify that small discarded detail alone does not force a coarse-energy
saving.

This script uses assertions and explicitly rejects `-O` and `-OO` before
any assertion can be disabled. The packet replay checks that this rejection
occurs. Its ordinary audit is reproduced exactly in `newton/audit.json`.
The 22 finite cases do not numerically verify an asymptotic short-interval
theorem or determine its effective threshold.

## Full-source Lee--Yang certificates

Both `lee_yang/certify_tree.py` and `lee_yang/certify_edge.py` reconstruct
the original theta density, normalization, variance and moments through
18 from the included authenticated primitives. They use six explicit
indices, 98 cells, Taylor degree 120 and 320-bit outward integer arithmetic.
Every time tail and the entire omitted range of indices are included.
Exact rational inverse products and interval Jacobian bounds certify the
required roots and derivative inequalities.

The tree check certifies exact agreement through degree 16, all 280
strictly positive couplings, the next-moment gap `(0.034,0.035)`, and the
stated positive covariance. It also compares the conditional moment model
with direct enumeration of all 128 states of an independent seven-spin
encoding, through degree 18.

The edge check independently reconstructs the exact old D16 root and
certifies its compensated derivative in `(-0.785,-0.784)` with respect
to `tanh(J)`. No solver is run during either replay. The supplied centers
are rational data whose enclosing roots are established by contraction.

Fresh replays from the frozen component directory passed, with receipt
SHA-256 values:

    T16C  4c7728e71120821c3e9a727d46fc7604c9d684d98168544f12f34402077e0633
    CER   46111e87e0e4141290546dea42b211fd5017c809efebc043c70aa34031d6a39e

The component `SHA256SUMS` also passes. This uses the inherited #886
transcendental backend, not a second independently developed backend.
The graph enumeration independently checks the finite model encoding.
Neither receipt certifies a degree-18 realization, a global continuation
between boxes or the all-order limiting theorem needed for RH.

## Publication scope

The packet adds one new standalone directory on the exact #965 parent.
File authentication and complete packet replay bind the proposed content;
GitHub read-back is reported in the PR publication record. No remote CI,
repository-wide build, independent human referee or accepted integrated
status is implied by these local validation results.
