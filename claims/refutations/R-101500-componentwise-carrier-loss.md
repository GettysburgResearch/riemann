# R-101500: componentwise one-sided estimates can destroy the physical carrier cancellation

PR #694 at exact head

```text
e6d923c1069f5a481abdf0769ca6d870a8b5ae4b
```

proves that the natural short and long pieces of the compact ordinary-Mobius wavelet carry opposite leading terms of size `sqrt(X)/log X`, while their physical sum cancels this carrier.

Therefore the implication

```text
small one-sided mass of each unshifted component
-> small one-sided mass of the physical sum
```

is not a source-faithful route: taking negative parts, absolute values, or orthogonal energies before the sum may retain a power-sized artificial carrier.

L-101500 gives the exact repair. A common transfer is inserted with opposite signs and cancels identically in the physical sum before any one-sided estimate is taken.
