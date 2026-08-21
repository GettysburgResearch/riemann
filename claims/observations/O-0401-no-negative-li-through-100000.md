# O-0401 — No negative Li coefficient observed through 100000

Claim ID: O-0401  
Title: Two-radius exploratory scan found no negative standard Li coefficient through `n=100000`  
Status: EMPIRICAL  
Authoring agent: `gpt56-04`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: L-0401; X-0401  
Scope: non-rigorous discovery result for Issue #14  
Related counterexample candidates: none

## Statement

Using the Cauchy--FFT discovery implementation in X-0401, two scans evaluated
all standard Li coefficients with `1<=n<=100000` using the same sample count
`M=262144` but distinct radii:

| alpha | radius `exp(-alpha/100000)` | required low-height audit `H(r)` | negative count |
|---:|---:|---:|---:|
| 10 | `0.9999000049998333` | `70.7142136820` | 0 |
| 12 | `0.9998800071997120` | `64.5535954589` | 0 |

Both scans placed the smallest observed value at `n=1`.  From `n>=1000`, the
smallest value in either recorded scan occurs at `n=1000` and is approximately
`2326.05316`.  The checkpoint values from the two radii differ by at most
`1.41e-4`, attained at the `n=100000` checkpoint, while that coefficient is
approximately `4.62581e5`.

The result is **not certified**.  It is an empirical exclusion of this search
range for the present discovery implementation, not a proof that every
coefficient in the range is positive and not evidence that all later
coefficients are positive.

## Definitions

The normalization and generating function are exactly those of L-0401.  The
scan uses binary64 complex samples, NumPy's FFT, and a 40-decimal `mpmath`
fallback at isolated points where the binary64 zeta derivative fails to
converge.

## Motivation

A strict certified negative coefficient would disprove RH.  Recording a wide
failed search prevents duplicated work, identifies the observed sign margins,
and focuses future effort on either substantially larger indices or a different
criterion.

## Computational evidence

The committed result files are:

- `results/scan-n100000-alpha10.json`, SHA-256
  `71126df63e002dc243abfc08dfe066f6483fd21f9b2547d73e5ded0c6380df5c`;
- `results/scan-n100000-alpha12.json`, SHA-256
  `815f66d7577236d35104fe44f4a0239695b647be7a09f2d8ec678aa877595ed7`.

The small-index calibration independently compares the Stieltjes/eta recurrence
with a direct 100-decimal Cauchy extraction through `n=50`.  Its maximum
reported discrepancy is
`4.61109413898154153607909649279e-75`, and every coefficient is positive.
That calibration is also non-rigorous.

## Analytic domain audit

For the two radii, L-0401 reduces zero-freeness of the transformed disks to
verification of critical-line location below heights `70.72` and `64.56`,
respectively.  The reduction does not certify sampled function values,
quadrature, FFT aliasing, or roundoff.

## Dependency audit

- L-0401 supplies the coefficient identity and radius reduction.
- X-0401 supplies exact commands, source code, environment, and JSON outputs.
- T-0303 in draft PR #21 supplies the imported implication from a strict
  negative coefficient to falsity of RH; it is not used to interpret this
  all-positive scan as a theorem.

## Gap audit

- The `rough_roundoff_absolute` field is only a diagnostic and explicitly is
  not a rigorous error bound.
- The two radii share most of the implementation and are not independent proof
  backends.
- The FFT has unbounded, though exponentially damped, alias contributions from
  omitted coefficients.
- The recorded minimum near `lambda_1` is smaller than the pessimistic global
  diagnostic at large `alpha`; only the 100-decimal calibration resolves the
  small coefficients accurately.
- No conclusion is drawn beyond `n=100000`.

## Adversarial tests

- The alpha-10 and alpha-12 scans perturb the contour while keeping the number
  of samples fixed.
- The imaginary residual is recorded; it is nonzero, exposing numerical error
  rather than hiding it.
- Binary64 zeta-derivative failures are counted and recomputed at 40 decimal
  digits.
- Small coefficients are separately calibrated by a different recurrence.

## Remaining uncertainty

The observation could contain undetected floating-point or aliasing errors.
The large positive margins for `n>=1000` make a missed sign reversal there
numerically implausible, but that judgment is heuristic and is not a proof.

## Suggested next attack

Do not merely rerun the same FFT at a slightly larger cutoff.  Either add a
rigorous ball-arithmetic coefficient enclosure with a proven aliasing tail, or
use the recurrence to search for a conditioning transition that can nominate a
specific index for certification.
