## T-105520 checkpoint — physical normalization and a signed 90% cut

The conditional T-105510 model has been re-audited at the actual half-order
normalization.

New exact results:

```text
half-order symbol normalization                    REPAIRED
scaled prime-simplex law D_K(alpha)                PROVED
K=4, alpha=2 residual energy < 1/7000             PROVED
holomorphic compression does not require a unit    PROVED
safe-line accretive resolvent identity              PROVED
negative-trace index absorption                     PROVED
```

The new conclusion-facing gate is one-sided:

```text
STRIPNEG105520:
  after the source-owned Hardy/Wick coordinate is normalized by its safe-line
  Gram, the negative trace of the complete strip-transfer remainder is
  < (1/20-o(1)) times the compression dimension.
```

Together with an asymptotically full-dimensional source-owned frame and the
confluent full-signature theorem, `STRIPNEG105520` implies more than 90% of
zeta zeros lie on the critical line.

This is not established here.  The packet also records the exact polarization
firewall: a scalar pointwise multiplier contributes `p p#` on an off-real
Hermitian contour, not the formal `p^2` source identity.  The missing strip
intertwiner remains load-bearing.
