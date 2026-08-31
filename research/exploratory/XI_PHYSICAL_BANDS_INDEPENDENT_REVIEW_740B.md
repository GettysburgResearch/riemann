# Independent fixed-SHA review: shrinking physical bands

Verdict: **PASS** for science
`740b497e99e6e6fb274684cc53599302402f2718`.
The physical interpretation remains conditional on the literal two-component
inner-function premise. No source-capture limit or RH statement is accepted.

Reviewed on 2026-08-31 in a separate worktree based on that exact science SHA.
The entire proof, producer, manifest and 32-test module were read. The frozen
science was not edited. The full fixture was authenticated and independently
processed, not transcribed through floating-point JSON.

## 1. Analytic review

The normalized kernel projection is
`P_(UH2)e_b = conjugate(U(b)) U e_b`.
Splitting its Laplace evaluation at D and applying Cauchy--Schwarz gives the
stated physical low-pass estimate with the exact denominator
`sqrt(1-exp(-2hD))`. Multiplication by U is not substituted for projection.

The two raw/reduced comparisons are scalar inequalities at b and ih only.
They are monotone in the required nonnegative moduli. There is no inference
of Loewner order after applying a frequency-band projection.

The finite-frame inequality follows from
`FF* <= C_prefix P_E` and trace positivity. The four inherited Gram ceilings
remain 2.342, 2.396, 2.414 and 2.420. A Carleson-box constant of one is NOT used
in their place. Enlarging E to K_B preserves these lower bounds, but does
not turn them into an infinite Hilbert--Schmidt norm.

The full-interval adjacent-gap argument controls every finite Carleson box:
summing consecutive inequalities between the first and last selected nodes
bounds all selected mass, including when a box omits intermediate nodes.
The singleton case uses its height. No infinite-family conclusion follows.

## 2. Independent primitive arithmetic

The adjacent review helper imports no author arithmetic for this part.
It uses the same pinned FLINT runtime at 384 bits, versus the producer's
256 bits, and an independently arranged calculation.

For each of the eleven heights, it evaluates zeta and its derivative using
the finite sums through n=64 plus the rigorous positive tail bounds

    sum_(n>64) n^(-sigma) <= 64^(1-sigma)/(sigma-1),
    sum_(n>64) log(n)n^(-sigma)
      <= 64^(1-sigma)[log(64)/(sigma-1)+1/(sigma-1)^2].

The summands are decreasing on the integration range. These are independent
of the author's zeta Taylor-series derivative route. Digamma supplies the
gamma logarithmic derivative. The fixed lambda_(64) and all 22 new
ell/Theta intervals are contained in the published enclosures.

For every positive cell, the review uses a monotone corner estimate rather
than repeating the producer's natural interval expression. Specifically,

    y/[(h+y)^2+x^2]

increases with y when y^2<h^2+x^2, and decreases with positive x. All inherited
rectangles satisfy this domain. Thus the lower-left height and upper-right
real coordinate give a rigorous Laplace lower bound. The minimum modulus
over the inherited raw-value rectangle and the independently evaluated
negative axis value complete the scalar bound. Every published positive
rational floor lies below this new directed lower bound.

Results:

- All 482 positive norm floors independently certified.
- All 838 zero floors retained; zero is conservative regardless of whether
  a sharper method could certify additional positive cells.
- All 1,320 grid entries, their node/width/height identities and complete
  maxima checked.
- All 12 squared-HS and norm prefix summaries reconstructed with exact
  Fraction arithmetic, including their strict decimal floors.
- All 39 adjacent full-interval gaps and 40 distinct unit memberships
  independently checked.
- An additional 780 contiguous-range span/mass inequalities all pass.
- Normal and optimized independent reports are byte-identical.

No boundary root census is reexecuted by this review. The forty root
certificates are inherited from accepted HA science. Its prior independent
review separately reconstructed boundary counts, local jets and Gram data.

## 3. Source identity and hostile acceptance controls

Fixture LF SHA-256:

    994483f138682e2b740ddc84bd93197e6d11c57e609be5e6fdd51daf55fbf3b5

Fixture payload SHA-256:

    6e3bded0999311462b06594d0a6e4434de5f90d3a6d23f3e76400e78e6845fe9

The independent helper authenticates all 35 frozen source Git-blob/LF pins,
all four artifact seals, the complete payload, local frozen scientific bytes,
and unchanged preregistered sections 1--4. Producer reconstruction also
authenticates the inherited runtime and recursive source closure.

Six additional independently resealed attacks are rejected by actual fresh,
unmocked producer reconstruction in EACH Python mode: omitting a zero cell,
claiming cofinal capture, duplicating a high axis height, replacing the inherited
Gram ceiling by one, falsifying a unit membership, and replacing a boolean
claim with integer one. These are not comparisons against a mocked expected
report. Their deterministic normal/optimized reports agree.

## 4. Final acceptance replay

- 32 tests normal: 184.891 seconds.
- 32 tests optimized: 185.299 seconds.
- Both producer --check runs pass.
- Both fixture emissions and both source-manifest emissions agree exactly
  with the frozen files after CRLF-to-LF normalization.
- Ruff lint/format, complete base-to-review whitespace checks pass.

Independent arithmetic report payload:

    283832bfbdbe5a3de2918108486eb8397de403211f20ce64392c633019fc9d6e

Independent hostile report payload:

    7be655ce09c5b788ae82f937833cfb7cc7617ae65e17871c1d289b10380707bd

Reproduce the independent checks:

    python -B research/exploratory/xi_physical_bands_independent_review_740b.py --check-report research/exploratory/xi_physical_bands_independent_review_740b.json
    python -B -O research/exploratory/xi_physical_bands_independent_review_740b.py --check-report research/exploratory/xi_physical_bands_independent_review_740b.json
    python -B research/exploratory/xi_physical_bands_independent_review_740b.py --hostile --check-report research/exploratory/xi_physical_bands_hostile_review_740b.json
    python -B -O research/exploratory/xi_physical_bands_independent_review_740b.py --hostile --check-report research/exploratory/xi_physical_bands_hostile_review_740b.json

Use the pinned native-xi-pass3-runtime interpreter for these commands.
The parent producer and tests remain the frozen science's own replay interface.

## 5. Accepted scope

This is a finite, conditional physical-band theorem at ONE lambda calibrated
at 64, not lambda=64 and not a mixture of separately calibrated operators.
All three widths have positive best witnesses for every one of the forty nodes.
All four prefix tables are retained verbatim. No extrapolation from their
finite growth is made.

The inner premise, cofinal weighted divergence, native decoder identity,
and RH remain unproved. Accepted source hashes and finite arithmetic do not
prove these analytic hypotheses. No external novelty claim is assessed here.
