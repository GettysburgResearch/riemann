# Validation and adversarial boundaries

Status: same-author mathematical reconstruction and finite checks. No
independent mathematical referee, formal proof assistant, full-repository
validator, upstream theta rebuild, or remote CI run.

## Mathematical points checked in the written argument

- Ideal norm fibers include both split conjugates and every common core.
- The sign uses ordinary a_p=1 and m>=4; the m=3 counterexample is retained.
- The all-phase upper theorem uses a positive MAJORANT, not a false sign
  assertion on arbitrary physical rows. Nonunit masks remain zeros.
- Common p or q factors in k produce the e=1 and e=m terms and are retained.
- Continuation uses multiplying zeta factors, not inverse zeta. Missing-prime
  products are continued directly, avoiding unsupported division by Q_p(s)
  on contours where it could vanish.
- Both Laurent derivatives of the moving local quotient are retained.
- The CDF Mellin integral has the correct -beta shift, 1/z, and constant
  term C_pq/2. Its power error is uniform in moving p,q.
- Short prime-pair LOWER counting uses binning and Cauchy, not a short-
  interval PNT. The upper count is proved by explicit Selberg weights.
- The m-uniform upper bound uses the positive real Rankin estimate; the
  fixed-m contour width is not silently made uniform as m tends to infinity.
- A positive selected covariance does not lower-bound the full PSD energy.

## Exact executed coverage

`checks/check.py` uses only the standard library and explicit exceptions,
so acceptance is not disabled by python -O.

Four full supported-ideal norm censuses cover EVERY rational norm through
131072: native Mobius; m=4 complex phases; m=6 unit phases; m=6 complex phases.
A rational-prime/SPF assembly agrees with a separately implemented traversal
of all labelled prime-ideal supports. The native census contains 36999
supported ideals; the m=6 censuses contain 37001 and include the first
powerful norm 7^6=117649 with both split ideals. Equal-norm cancellation and
zero fibers are retained. These are algebraic principal-phase fixtures,
not a census of actual theta or physical sextic-character values.

Each census checks every ordered pair of distinct split primes <=43 and
EVERY common integer core whose two shifted norms are within the cap:
131940 cases per census. Thus 527760 exact pair identities and the same
527760 signs are checked. These are repeated finite cases, not that many
independent analytic theorems.

Additional checks cover local even degrees 4,6,8,10 and exact odd degrees
5,7,9 in Q(i,sqrt(p)); an uncapped four-prime-ideal fixture includes common
powerful factors; arbitrary Gaussian-integer unit phases and every mask on
four labelled prime ideals verify the norm and pair majorants. The two norm
constructors share the classical splitting law, not an independently
certified number-field backend.

Exact Selberg quadratic forms, divisor inversion, and interval remainder
bounds are checked for cutoffs 1 through 25. Actual finite prime pair
bin-count inequalities are checked at eight Y values. Rational Gaussian
square completions and Laurent residue arithmetic are checked separately.
The full breakdown, including repeated setup guards, is in outputs/EXACT.json.

Normal and optimized full runs reproduced outputs/EXACT.json byte-for-byte.
Five SEPARATE corrupted `python -O` processes were rejected: omit a split
conjugate; omit the shared-power term; omit complex conjugation; extend the
sign to m=3; reverse the CDF shift. outputs/MUTATIONS.json records the errors.
No new asymptotic inequality is inferred from a finite test count.

## Optional numerical checks actually run

At 55 decimal digits, direct physical Gaussian integration and the explicit
CDF pair kernel agree to relative error <1e-40 on three finite common-core
fixtures, with 27 nonzero terms each. Normal/optimized reports were compared.
These are NOT directed/certified intervals and contain no quantified infinite
source tail. They validate normalization only, not the mesoscopic asymptotic.
See outputs/NUMERICAL.json and checks/check_numerical.py.

## Development correction

The first version of the intended "complex" phase fixture accidentally
chose opposite roots at every split pair. Its sum b_++b_- was always zero,
so it did not challenge the conjugation in |b_++b_-|^2. This was detected
before final acceptance; the fixture was corrected to adjacent fourth roots.
The full exact and numerical checks were rerun. The no-conjugation mutation
now fails. No theorem statement depended on that initial fixture.

## Smallest load-bearing remaining review questions

Adversarial review should start with the uniform product construction after
(21), the moving-prime Laurent coefficients (22)--(23), the all-T error in
(25), the elementary pair count (32), and the phase-uniform real Rankin
argument (37a)--(37b). The infinite proof remains a proposed same-author proof,
not certified by the scripts. The full critical signed energy is still open.
