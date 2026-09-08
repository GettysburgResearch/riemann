# Executed validation and evidence classes

Authoring runtime: Python 3.13.5; mpmath 1.3.0 for the interval script.
No Lean build, independent referee pass, remote CI claim, full zero census,
large theta/prime sweep, or Platt--Trudgian rerun is included.

## Exact rational replay

Commands executed successfully:

    python verify_exact.py > exact_result.json
    python verify_exact.py --check exact_result.json
    python -O verify_exact.py --check exact_result.json

Normal and optimized output files are byte-identical. The 225 checks per
mode split as follows:

    source polynomial / quartet bounds       11
    heat-budget and Gaussian primitive       10
    connected cumulants (3 laws, orders 1..7) 21
    marked covariance / discriminants        17
    finite high-tail controls                 5
    polynomial Bernstein counterexample      26
    real spectral Hausdorff identities       48
    Laguerre coefficient identities          63
    finite Poisson-escape coefficients       21
    invalid-probability refusal                3

These are finite checks of the declared algebra. They do not machine-prove
the infinite analytic statements. Synthetic probability controls are not
misidentified as samples of the actual theta law.

Two additional corrupted-result checks were run under optimized Python:
changing rh_proved from false to true, and changing integer checks_total=225
to floating-point 225.0. Both were rejected with nonzero exit status.
Canonical JSON comparison is type-sensitive, so integer/float/Boolean aliases
cannot pass as a fresh result. Neither extra check inflates the 225 count.

## Directed two-point interval calculation

Commands executed successfully:

    python verify_low_zero.py > low_zero_result.json
    python -O verify_low_zero.py > /tmp/astra-low-optimized.json
    cmp low_zero_result.json /tmp/astra-low-optimized.json

The output is byte-identical across modes. The script uses 80 decimal digits,
128 Euler-transformed eta terms, and an exact 2^(-80) complex-rectangle error
radius. It encloses Xi(14)>0 and Xi(15)<0; their real magnitudes are about
0.0002012944442 and -0.0007056979588. Imaginary enclosures contain zero, as
required by the separate exact reality identity.

Trust: mpmath.iv elementary functions and complex Gamma enclosure. This is a
software interval certificate with a proved truncation tail, not a Lean or
independent formally verified Gamma implementation. It proves at least one
line zero in (14,15), not completeness or simplicity. V100 is a separately
imported published theorem.

## Non-proof normalization spot check

A separate 35-digit ordinary-mpmath check compared the positive Phi integral
with X(u) at u=0 and u=1, using modes m=1..7 and tau in [0,3]. It returned
0.5 and 0.51167277264922943965209982790849587, matching the direct completed
zeta calculation to the working precision. This was a normalization
regression only: no directed tail was attached and no theorem depends on it.
The exact normalization is justified analytically in HEAT_BERNSTEIN.md.

## Release integrity

SHA256SUMS covers every other retained file in this directory, not itself.
It authenticates bytes, not truth of mathematical claims. Remote publication
must read back the branch head and Git tree entries and compare the blob
identities with the local files. The final PR reports that receipt separately.
