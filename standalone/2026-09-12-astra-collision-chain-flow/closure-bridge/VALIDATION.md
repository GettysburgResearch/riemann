# Validation and claim boundary

## Executed on the authored bytes

The accepting reconstruction is `certify_chain.py --check chain_result.json`.
It was executed successfully through the full subprocess suites in BOTH normal
and optimized Python modes. Both returned the same reconstructed receipt:

    SHA256 48214985839908297606dfc1b7064dcd3744d0033d3ca2b9db1fa6dcdc6dc423

In EACH mode, the bounded four-method suite and full two-method suite passed,
with no failures, errors or skips. The full suite performs one pristine CLI
acceptance and one changed-numerical-receipt CLI refusal; the latter completes
the entire fresh source and tail reconstruction before rejecting at the actual
receipt comparison. The four additional actual CLI refusals in the bounded
suite cover duplicate JSON keys, a Boolean numeric alias, wrong claim status,
and changed parent source bytes. Thus there are FIVE actual refusals per mode,
not five extra source reconstructions. The normal and optimized full suites
completed in approximately112 seconds each while running concurrently; these
are historical execution receipts, not a performance guarantee.

The bounded tests additionally check:
- 3,854 exact native Newton prefix coefficients, the collar identity and
  its bound at all eleven crossing cuts through31;
- 28 complete bond-subset panels for three small graphs, against independent
  enumeration of all spin configurations and their characteristic values;
- five moment orders and their parameter derivatives by direct spin enumeration
  versus the formal Fourier recurrence at two weight patterns, three q values,
  and three derivative choices; all six split/reversed-join panels are checked;
- nine exact base coefficients for the all-future tangent majorants;
- eleven dyadic joint-feasibility budgets and the rational/exponential constants
  behind the tripling inequality, native interaction floor and N5 obstruction.

The separate bounded reconstruction fingerprint is

    3a7a7174743f2f0f7b4ea3716cb4715d6c7b714e9565aec6a9cc32b9fa476465

These finite checks do not establish an unbounded sequence of successful
Ising/gamma moment matches, a native covariance bound, or RH.

## Numerical scope

Acceptance uses integer/Fraction arithmetic and outward512-bit dyadic intervals,
including interval automatic derivatives of the finite defining equations.
It freshly reconstructs the full native theta moments through ten. The entire
infinite chain tail is bounded analytically, including prefix-tail covariance;
it is not made independent or set to zero. The head-calibration Simpson,
Euler-constant and Euler--Maclaurin errors enter the Brouwer map. Its continuous
remainder is not differentiated by assumption. Printed receipt decimals are
outward-rounded30-place enclosures of computations accepted at full precision.

The mathematical existence implication uses Brouwer and the inherited proposed
source/Lee--Yang/growth arguments. No proof assistant or independent referee
has checked those analytic arguments in this pass. The two Python modes use
one backend. Direct small-spin checks are independent finite representations,
not an independent implementation of the full transcendental integral.

## Development failures and exclusions

A first implementation failed immediately on an interval/dual type mismatch
in the calibration integrand. It supplied no accepted result. That dispatch
was repaired before the reported reconstructions. A temporary absolute parent
path used during development was removed; final execution uses only the
relative, hash-authenticated parent directory.

Floating NumPy/Numba/SciPy exploration selected the rational center and
preconditioner. It suggested an eighth-moment crossing near q=.018145; those
floating moments and residuals are NOT accepting inputs. The accepting target
is freshly evaluated from the actual theta source. The only retained scout
outputs are rational center/preconditioner/scale choices whose validity is
subsequently tested on the complete box. The complete equations are not
rounded-fit equations. No uniqueness of the Brouwer root is certified.

No source campaign for the imported #867 zero/triple certificate or #858 N5
nonreal zero was rerun. No actual gamma or xi zero, spectral census, new
zero-free height, cofinal feasibility sequence, parent six-moment replay,
repository-wide build/validator, Lean proof or remote CI is claimed.

## Delivery checks

The addition is confined to the `closure-bridge/` child of the prior packet.
All earlier files are preserved. `SHA256SUMS` binds the new authored files.
The delivery archive retains the complete prior packet so its four required
parent dependencies are available. Publication receipts belong to the PR
conversation and the final response; no guessed remote head is embedded here.
