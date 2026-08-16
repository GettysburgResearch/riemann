# Research reset: positive Peano source, centered cubic scale innovation, and First-Hermite heat

## Executive result

This pass treats the repository as a library and rebuilds the independent Q4/heat programme around one source-complete scale architecture.

The main unconditional theorem is a positive factor-64 Peano bank:

\[
\Phi_{64}=(64-T)(16-T)(4-T)[x(1-x)^2_+],
\]

whose physical kernel is nonnegative and whose logarithmic form is the positive convolution

\[
\Phi_{64}(e^{-v})=8192(b_1*b_2*b_3)(v).
\]

Its curvature has a double Mellin zero at `s=1` and does not cancel any nontrivial zeta zero.

The centered-cubic potential is then shown to be the scale-four innovation of a positive Mellin smoothing of the same Peano potential. Finally, the carrier-resolved cubic field is connected exactly to the First-Hermite prime polynomial by a Schwartz transform whose `L2` cost grows only like `q^(1/4)`.

## What failed under hostile testing

Two plausible full-proof shortcuts are false.

First, positive source plus positive scale transport does not force positive second scale curvature. An exact cosine countermodel keeps the potential uniformly positive while its curvature changes sign.

Second, any coefficientwise absolute Gaussian prime envelope grows at exponential scale `e^(q/4)`, whereas a terminal off-line depth `y<1/2` grows only like `e^(q y^2)`. The strict gap `1/4-y^2` prevents absolute Gaussian domination from closing the final pointwise theorem.

## Exact remaining arithmetic theorem

The static cubic route is reduced to the balanced large-divisor form

\[
\sum_{m<\sqrt X}\log m
\sum_{\sqrt X<d\le X/m}\mu(d)W_C(md/X),
\]

after the small-divisor sector is paid unconditionally.

The heat route is reduced to an `L2` bound for the complete carrier-resolved cubic field. The exact Schwartz transform then transfers that bound to First-Hermite heat without exponential loss.

These are genuine signed arithmetic dispersion statements. They are not block-count, alignment, generic large-sieve, or positivity claims.

## Scientific boundary

```text
positive factor-64 Peano source          exact
centered-cubic positive smoothing        exact
cubic-to-First-Hermite transform         exact
source-blind curvature inference         false
absolute Gaussian depth closure          false
balanced Mobius dispersion               open / RH-equivalent
carrier-resolved scale dispersion        open / RH-equivalent
Riemann Hypothesis                        unproved
```
