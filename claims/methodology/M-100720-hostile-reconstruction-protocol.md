# M-100720 — Hostile reconstruction protocol for the cubic hinge frontier

Review against the exact audited base `PR #695 / 7b61f6b...`.

## Required reconstruction order

1. Verify the hinge identity and the carrier/collar decomposition in square-root
   coordinate.
2. Expand the finite interior Euler product and recover the four-term
   compensated reciprocal prefix with the exact chain-rule coefficients.
3. Check that Tao's theorem is used only for `|A_P(x)|<=1`, not for a sign.
4. Differentiate the compact cubic collar three times and verify every
   `d^-2`, `p^-3/2`, `q^-3/2` coefficient and support threshold.
5. Reconstruct the left and right Taylor formulas including the positive
   initialization and the nonnegative deep carrier.
6. Verify `R-100721`: the uncut left certificate grows quadratically after the
   collar support and may not be integrated globally.
7. Verify the adaptive partition is determined by `L,R`, not by the sign of the
   physical packet.
8. Reconstruct the reciprocal-level pairing in `L-100724` and the threshold
   `A<e`.
9. Check finite-cutoff convergence in total variation before passing to the
   complete source.
10. Reconstruct the centered-cubic Mellin--Landau consumer on the same source
    normalization.

## Immediate falsifiers

```text
wrong endpoint chain-rule factor;
using the withdrawn divisor-restriction renewal from PR #691;
charging L after the right collar has vanished;
replacing the joint min--max law by separate owner marginals;
claiming bounded regularity implies subpower negative mass;
claiming APCC or DPCC has been proved by the finite replay.
```

## Exact status

The packet proves the algebraic and analytic interfaces into the adaptive
collar gate. It does not prove `APCC100723`, `DPCC100723`, or RH.
