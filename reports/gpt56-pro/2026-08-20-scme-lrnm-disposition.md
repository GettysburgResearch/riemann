# SCME/LRNM proof attempt — exact disposition

The requested proof attempt produced a decisive asymmetric result.

```text
SCME100704  false;
LRNM100704  true, with eventually zero negative part.
```

The short sector contains all singleton prime blocks. Their weighted PNT main
term is

```text
-kappa_0 sqrt(X)/log(X),
kappa_0=8 log(2)(1-2^(-1/2))^2.
```

Every composite short block together is only `O(sqrt(X)/log^2 X)`. Hence the
short `L2` mass is of order `2^L/L^2`, not subpower.

The full compact Möbius wavelet is exponentially smaller than this main term by
the classical zero-free-region Mertens estimate. Therefore the long sector
has the opposite positive asymptotic and is eventually positive.

The implication-matrix lesson is binding: the short/long partition is a valid
source partition but not a valid *absolute-norm* partition. Its leading prime
carrier cancels only after the two regions are recombined.
