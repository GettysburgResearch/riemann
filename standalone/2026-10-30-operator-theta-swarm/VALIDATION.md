# Validation, review, and reproducibility

This packet separates written analytic proofs, exact finite certificates, and exploratory numerics. Passing a finite program is not a proof of the infinite-dimensional or cofinal statements. Those statements depend on the arguments in the manuscripts and the classical inputs cited there.

## Exact arithmetic and algebra

| Program | Recorded result | Execution and mathematical scope |
|---|---|---|
| `spectral/verify_anchor_flow.py` | 96 exact rational matrix cases, maximum dimension 25; full transport identity, trace, corner-mutation rejection, and boundary spectral invariants | Author, independent theta reviewer, and parent replay passed; the all-order identity is proved entrywise in the manuscript |
| `spectral/verify_spectral.py` | 221 exact checks: 80 Laguerre generating coefficients, 80 observation coefficients, 45 projection errors, 12 dissipation identities, 4 scalar margins | Author, independent theta reviewer, and parent replay passed; its remaining 24 tests are floating diagnostics and are treated separately |
| `theta/verify_polya_obstruction.py` | Full-source eighth derivative strictly between `-8951861` and `-8951860` | Author and independent reviewer ran ordinary and optimized isolated Python; the parent replay matches the saved certificate. Rational pi/exponential enclosures and an analytic infinite-tail bound are included |
| `theta/review_theta_derivative.py` | Eight finite-prefix derivative interval comparisons passed | Independent formal-exponential expansion replaces the author's Bell recurrence; it shares the inspected interval primitives. Parent replay matches the reviewer receipt |
| `theta/verify_bessel_m3.py` | Eight actual-source M=3 sign intervals: six pass the sufficient boundary gate, two fail | Author and independent arithmetic reviewer ran ordinary and optimized isolated Python; parent replay matches the certificate. Both the theta and Bessel infinite tails are bounded |
| `arithmetic/verify.py` | Three-point complex logarithmic quadratic has a rational sixteen-term upper enclosure below `-1.434`; all omitted terms have the negative sign proved in the note | Author, independent spectral reviewer, and parent replay passed. Real/imaginary-part controls are positive. This is a source-specific phase obstruction, not an approximation-error upper bound |

The actual Python runtime used was Python 3.12.14. The spectral and Skellam floating diagnostics used NumPy 2.3.5 and SciPy 1.17.0. The rational programs and Decimal Bessel programs need only the standard library.

The root replay compares parsed JSON and, where deterministic formatting is preserved, exact bytes against the checked-in receipts. `PACKET_CHECKS.json` records final packaging checks. `MANIFEST.sha256` binds the delivered files other than the manifest itself.

## Independent review scope

| Review | Reviewer and inspected material | Independence boundary |
|---|---|---|
| [Spectral and flow review](spectral/REVIEW_SPECTRAL_AND_FLOW.md) | Theta lane independently reconstructed the moving-anchor proof, uniform remainder estimate, Laguerre realization/completeness, and boundary-flow signs | Replayed the authors' finite programs; did not build a second numerical backend or reprove every classical input |
| [Theta review](theta/REVIEW_THETA.md) | Arithmetic lane read the full original theta proof and certificate implementation | Added a second formal derivative algorithm while sharing the reviewed outward-interval primitives; did not rely on the floating root search |
| [Bessel review](theta/REVIEW_BESSEL.md) | Arithmetic lane reviewed the final rational reduction, self-adjoint form, pole/common-factor handling, local theorem, and exact M=3 certificate | High-degree Decimal signs and pole searches remain exploratory; no complete complex pole census is claimed |
| [Arithmetic review](arithmetic/REVIEW_ARITHMETIC.md) | Spectral lane checked the signed Levy density, exact noise threshold, symmetrization, native target normalization, and finite phase witness | Replayed the exact certificate; recent overlapping external asymptotics were not fully audited |

Every review names immutable SHA-256 identities for its primary source files. A source may be copied into a differently named publication directory without changing its bytes. The original theta and spectral proofs were frozen before their continuations were written; those continuations have separate reviews.

Two substantive repairs were made before the final source identities were frozen: downward anchor transport loses the **positive** boundary part, and the finite-variation-noise exclusion in the arithmetic note carries the finite-second-moment assumption used by its uniqueness proof. The boundary notes also use the radial derivative `y'(0)=a K'(a)` consistently.

These are independent AI-agent mathematical reviews within one research session. They are not external human peer review, formal proof-assistant verification, or acceptance by repository maintainers.

## Exploratory computations

`spectral/SPECTRAL_CHECKS.json` additionally contains 24 ordinary floating diagnostics: safe-half-plane Cauchy coefficients, finite eigenvalues, semigroup identities, and synthetic critical/off-critical zero controls. The source truncation is in `Re(s)>50`; the theorem bounds the full remainder independently of those numerical samples.

`theta/SKELLAM_DIAGNOSTIC.json` records source-kernel errors and transform roots located by a limited numerical search. It does not count all zeros or exclude nonreal zeros. The parent did not rerun the optional heavy quadrature/root exploration, and no proof depends on it.

`theta/BESSEL_JACOBI_SUMMARY.json` summarizes the first failed continued-fraction sign at 180 and 360 decimal digits. Both precisions agreed for all fourteen tested `(a,M)` pairs. The higher-degree coefficient calculations have ordinary Decimal rounding; they do not provide outward intervals, exact gcd cancellation, or certified pole locations.

`theta/BESSEL_LOW_POLES_SUMMARY.json` contains the sign-changing real poles located below E=500 by the 360-digit probe. A step-one scan followed by refinement can miss extra roots, complex poles, and multiple poles. Residues as small as about `3e-75` make a coarse complex grid particularly unreliable. The parent inspected the implementation and summary but did not rerun this exploratory search; the author executed it. Full detailed stage/pole output can be regenerated by the scripts and is omitted to keep the research packet readable.

The unstable preliminary complex-grid and large-energy Weyl-function quadratures were excluded from the packet's evidence. No numerical positivity sample substitutes for a uniform sign theorem.

## Reproduction commands

Run these from the packet directory:

```sh
python -I -S -B spectral/verify_anchor_flow.py
python -I -S -B theta/verify_polya_obstruction.py
python -I -S -B theta/verify_bessel_m3.py
python -I -S -B theta/review_theta_derivative.py theta/verify_polya_obstruction.py
python -I -S -B arithmetic/verify.py
python -I -B spectral/verify_spectral.py
```

Adding `-O` to the standard-library commands permits optimized-mode replay. The programs use explicit exceptions for their acceptance conditions rather than relying on removable `assert` statements. The spectral script writes its receipt next to itself; the other exact scripts print JSON to standard output.

Optional diagnostics:

```sh
python theta/skellam_diagnostic.py
python theta/bessel_jacobi_diagnostic.py 180
python theta/bessel_jacobi_diagnostic.py 360
python theta/bessel_low_poles_diagnostic.py
```

The Decimal scripts write their detailed outputs next to themselves. The checked-in summary files retain the conclusions and selected digits used in the manuscript.

## Delivery boundary

This is an additive standalone research directory on a new branch from the inspected live main commit. It changes no accepted-status file, integrated theorem, repository-wide dependency, or runtime code. No repository-wide test suite or Lean build was run: the deliverable is the new mathematical packet and its own finite checks. The final publication is a draft pull request, not a merge or a certification of RH.
