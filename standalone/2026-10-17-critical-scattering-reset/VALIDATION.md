# Finite validation and reproducibility

The written infinite statements require mathematical review. These scripts
check finite algebra, coverage on declared finite prefixes, and numerical
normalizations. Their pass status is not an RH proof or a certification of
an infinite Euler product, functional equation or contour argument.

## Commands

From this packet directory, with standard-library Python:

```bash
python replay.py
python replay.py --with-probe
```

The replay authenticates every direct file against SHA256SUMS, checks complete
manifest coverage, compiles every Python source, and runs the four component
checkers in both ordinary Python and `python -O`. Both modes must reproduce
the archived report bytes. It uses explicit exceptions rather than assertions.
The optional probe is rerun in ordinary binary64 and compared with its
archived sample. The two commands are alternatives; it is enough to run the
second to include everything.

All eight component executions and the optional probe passed on the frozen
local packet in this session. Normal and optimized component outputs were
byte-identical to their archived reports. Independent agent execution preceded
the main agent's final replay. No remote CI or whole-repository test result is
claimed.

The first aggregate replay found a formatting-only difference in the Fourier
archive: one array had been placed on a single line. Its parsed JSON, all
counts and the stream digest were identical to the actual output. The archive
was replaced by unedited checker stdout before the final strict byte replay;
no mathematical input or checker source was changed.

## Component coverage

| Script and report | Coverage | Arithmetic and boundary |
|---|---|---|
| `verify_audit_components.py`, `VERIFICATION.json` | 48 local Poisson substitutions, two identities each; 27 paired inner-function modulus identities. Total 123 finite identities. | Exact rational substitutions. Complements the general algebraic proof; does not test the infinite canonical product. |
| `check_fourier_transfer.py`, `FOURIER_CHECK_RESULTS.json` | 96 coefficient cases through 256; local coefficients through degree 20; 24,480 independent support comparisons; 192 global forward/inverse convolutions; 480 phase-dilation checks; 17 Parseval and 17 all-shift identities; 51 complete Fejér filters. | Exact rational arithmetic. Fixtures have real rational profiles and degrees 2, 4, 6; arbitrary complex profiles and other degrees are covered by the written majorants. |
| `check_pole_calibration.py`, `POLE_CHECK_RESULTS.json` | Eight rational-complex Gram/projection cases with pole orders 1--4; factorial/sign controls; finite cyclic character actions for 5, 7, 11; full rational ideal prefix through 30 for Gaussian transforms and energy, plus prime/continuum checks at widths 1 and 0.01. | Mixed exact rational algebra and non-directed binary64 Simpson quadrature. The finite character action is not a number-field calculation. |
| `check_memory_and_scattering.py`, `MEMORY_CHECK_RESULTS.json` | Complete integer Möbius prefix through 512; 1,033 exact prime-log convolution checks; 20 exact rational causal-control checks; six finite Gaussian identity evaluations. | Exact integer/rational checks plus separate non-directed binary64 Gaussian values. Product coverage in the finite memory check is explicitly restricted to the same prefix. |

The largest finite Gaussian memory residual was
`2.4424906541753444e-15`. In the pole report, the two finite transform errors
were below `1.2e-14`; the narrow-width continuum quadrature error at one point
was about `1.18e-12`. These are floating-point residuals against declared
regression tolerances, not certified enclosures of the infinite functions.

Negative controls reject reversing the Möbius-memory sign, deleting the
negative-time energy of the causal control, deleting covariance signs,
discarding one shift orientation, retaining only the diagonal, omitting
phase dilation, or using the wrong differentiated-pole factorial. They test
specific failure modes; they do not certify all possible proof errors.

The Fourier case-stream digest is
`8f9f1dfc9ac8455360395b7c4d99148c31c9731ce5d4b434bfe79d2301b6d13c`.
The report bytes and every source file have independent entries in SHA256SUMS.
The manifest commits to this packet when read from its frozen Git commit; a
self-consistent manifest alone is not independent source authentication.

## Direct prime-side experiment

`prime_detector_probe.py` produces `PRIME_PROBE_RESULTS.json` with defaults:

* `F=Q`, `S` empty, height zero;
* Gaussian width `a=0.01`;
* all 18,120 prime-power terms with integer norm at most 200,000;
* 73 samples on logarithmic scales `0<=x<=9`;
* the exact erfc continuum from PRIME_DETECTOR.md, evaluated in binary64.

The largest absolute sampled detector was `1.095236580074712`. This checks a
usable finite implementation of the proposed diagnostic. A bounded finite
sample is not an asymptotic bound or evidence that all zeros are critical.
No zero data are used in the computation.

There is a separate analytic bound for the omitted prime tail. For integer
cutoff `P`, horizon `U>=0`, `r=log(P)-U>a`, and

\[
1/\log P-1/2-r/(2a)<0,
\]

the complete omitted tail, uniformly for `0<=x<=U`, is at most

\[
\sqrt{a/\pi}\,e^{U/2+a/4}
\left(1+\frac{U+a}{r-a}\right)
e^{-(r-a)^2/(4a)}.
\]

Indeed `Lambda(n)<=log n`, and the resulting positive summand is decreasing
for `n>=P`. Compare its integer tail with the integral from P. Substituting
`v=log n-x` and completing the square gives a Gaussian centered at `a`;
integrating its linear part exactly and applying the ordinary Gaussian tail
inequality to the constant part gives the display. P is an integer, so the
sum/integral comparison uses the correct lower endpoint.

The formula evaluates to approximately `2.4106878789174236e-110` for the
defaults. Its logarithm and value in the JSON are ordinary binary64
evaluations. That analytic truncation bound does not cover summation roundoff,
erfc evaluation error, cancellation in the subtraction, or unsampled x.
No directed numerical certificate is claimed.

## Not performed

No Lean build or transitive axiom audit; no reconstruction of all CT,
Kazhdan--Patterson, BGL or de Faveri proofs; no all-height zero verification;
no reciprocal-derivative data; no numerical computation in a nontrivial number
field; no RH-strength upper estimate. The optional Kummer construction is a
written algebraic argument, not a computationally certified family.

All computational results are finite. The new infinite conclusions are the
component theorems in the written notes, with their stated classical imports
and open estimates. External mathematical review remains necessary.
