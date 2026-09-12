# BHF26: two-tail analytic continuation and complete collision balance

**PROPOSED research, not an RH proof. Independent mathematical review is required.**

This continues the actual beta/uniform fixed-point source of PR #876 at `8002444ec4d4bd1c6f8fa073820bcc575cb218e1`. It is an additive packet based on main at `f99d9e3908dde4865377c75d9ca051c1f545bf4f`; it does not modify #876, #851, #864, or the integrated scientific status.

## What is proved in the proposed manuscript

The weighted norm `sup |h(t)| / [(2t/5)^3/(1+2t/5)^5]` controls both cubic cancellation at zero and quadratic decay at infinity. The actual nonlinear source map is uniformly contractive with constant at most `3/5` on the gamma-bounded state class. A parameter Lipschitz bound of `20` and a full complex-parameter extension to `dist(zeta,[0,1])<1/4096` follow. The first response and every higher parameter coefficient have explicitly invertible source equations and full-tail remainder bounds.

The reflected Mellin family is jointly holomorphic on that parameter neighborhood and `-5<Re(s)<6`. This supplies the regularity needed to handle arbitrary finite-height zero collisions, including persistent repeated factors. Weighted finite-height zero costs are absolutely continuous; the correct repeated-root velocity uses `partial_s^m H`, not a zero denominator `H_s`.

A new explicitly labeled diagnostic uses weight

    (sigma-1/2)^2 [sigma(1-sigma)]^2 sech(pi t)

on the open critical strip, and zero outside. It has a complete uniform height tail `(5/54) exp(-pi T/2)`. Its endpoint cost equals an iterated limit of a source-only regularized logarithmic integral; higher collisions, vertical crossings and infinity are not discarded. This is the beta-homotopy counterpart of the different gamma-path Jensen programme, not a claim to have invented the general method.

## The missing completion

RH is equivalent to the final signed integral being zero. The required upper bound by zero has NOT been proved. The Green kernel has both signs and the positive-law Mellin response is oscillatory. Separate absolute bounds do not supply its cancellation.

No native flux value, native collision, new xi zero, or increased verified height is computed in this packet. Analytic source regularity is not a spectral positivity theorem.

## Read and reproduce

Read `PROOF.md` for the exact domains, constants, collision proof and remaining sign; `SOURCES.md` for frozen dependencies and omissions; `VALIDATION.md` for what was actually run.

Python standard library only:

```sh
python -I check.py --check results.json --self-test
python -I -O check.py --check results.json --self-test
```

The checker freshly reconstructs exact finite rational/radical identities, source moments through order 12 at five stated rational parameters, the strict analytic-ball inequalities, and synthetic multiplicity controls. It is NOT a proof checker for the analytic theorems or RH. All acceptance checks use explicit exceptions, not removable Python assertions.
