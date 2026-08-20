# Hardy-tail and divisor-GCD attack on the final owner-packing frontier

## Frozen inputs

```text
canonical scalar/GPMOC base:
  PR #659
  83c17b32a99ac9e1aa5aec3168535550eb286636

native first-owner Littlewood--Paley packet:
  PR #660
  ca3c055307e6804ae904cb9105594dd3f2408ba3
```

## Question attacked

The live conclusion-facing gate was the signed off-diagonal Poisson packing
`GPMOC99800`. The phase integral obscured what geometric quantity actually had
to be controlled, while the first-owner square function lived in a different,
labelled Hilbert space.

## Exact resolution of the phase interface

For every finite packet `c`,

\[
Q_\tau(c)
=|\sum c_n|^2
+2\tau\int_1^\infty t^{2\tau-1}
 |\sum_{n\ge t}c_n|^2dt.
\]

Thus `GPMOC99800` is exactly a Hardy/Carleson estimate for all truncated
physical tails. No phase cancellation remains hidden.

## Multiplicative alternative

A product Poisson evaluation on the prime torus gives

\[
|\sum c_n|^2
\le\sum_dJ_{2\tau}(d)|\sum_{d\mid n}c_n|^2.
\]

This is a second positive square which retains divisor ownership. It may be
better adapted to the exact logarithmic-owner, prime-exchange, or continuous
Jordan identities than the additive-frequency packet.

## Native source interface

Transporting the coefficient-exact first-owner identity directly into the
Hardy-tail Hilbert space gives

\[
Q_\tau(Ff)
\le s_kQ_\tau(f)+\sum_i\lambda_iQ_\tau(\Delta_i^{\rm fut}f).
\]

This bypasses the generic labelled-collapse norm. It reduces the conclusion to
the actual future-completed owner currents in the actual physical tail norm.

## Hostile boundary

A distinct-integer cluster has Poisson quadratic form more than 63 times its
diagonal already at 64 terms. The ratio grows linearly in the cluster size.
Therefore the diagonal bound proved in PR #659 and the free labelled energy of
PR #660 cannot close the route without arithmetic tail/divisor packing.

## Scientific verdict

The requested proof of RH was not obtained. The exact surviving theorem is now
one of two equivalent/sufficient source-specific statements:

```text
HTOC99810:
  inverse-weighted Hardy norms of the truncated native tails are subpower;

DGOC99810:
  inverse-weighted Jordan divisor-owner squares are subpower.
```

Both are free of the previously refuted native-coefficient, alpha-child,
common-parent, phase-evaluation, inverse-filter, and Landau interfaces. The
remaining content is the genuine signed squarefree-core correlation. It may
not be replaced by diagonal energy or source-blind Cauchy--Schwarz.
