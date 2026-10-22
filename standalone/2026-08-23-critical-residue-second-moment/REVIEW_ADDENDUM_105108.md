# Review addendum — L/T/R/M-105108 Green–Gram conditioning

Checkpoint base:
`cf07de0ba009e8b288eb98b6b4a0ed1d8f12e251`.

## What changed

The exact minimum-norm selector from L-105107 is decomposed into:

1. full-event positive-Green target loads
   \(|y_c|=|\gamma_c|r(c)^{d_c-1}e^{\sum n_ag(c,a)}\); and
2. the target-only normalized-Gram interaction
   \(\tau=\|G^{-1/2}D_yG^{1/2}\|_2\).

This yields sharp spectral, centered, target-cardinal, product-separation,
pairwise, domain-comparison, and Euclidean collision bounds.

## Hostile checks

- Confirm \(g=-\log\rho\), with no factor two.
- Confirm other targets have exponent \(d_a-1\) in \(|y_c|\), but full
  exponent \(d_a\) in the uncentred cardinal upper envelope.
- Confirm raw magnitudes do not determine \(\tau\): norms two versus four
  for equal versus opposite phases at the same two nodes.
- Confirm all pair restrictions miss the stated three-target obstruction.
- Confirm fixed-data domain enlargement cannot reduce the optimum.
- Confirm rectifiability is invoked only for the contour consequence.
- Confirm no Xi/cofinal or RH implication is stated.

Exact replay:

    python -B experiments/X-105108-green-gram-selector-conditioning/tests/test_verify.py
    python -B -O experiments/X-105108-green-gram-selector-conditioning/tests/test_verify.py

Expected verdict and digest:

    PASS_T105108_GREEN_GRAM_SELECTOR_CONDITIONING
    15/15 normal / 15/15 optimized
    6c2484c4e63612b238f1ec6044c9b8778b725899d4be643d7e80b6a6dc345cdb

Xi manifests, certified conformal coordinates, cofinal Green–Gram and
quotient-edge estimates, strict coherence, RCMV104530, and RH remain open.
