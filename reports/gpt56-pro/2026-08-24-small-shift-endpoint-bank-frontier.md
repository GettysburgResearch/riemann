# Small-shift endpoint bank: an exact \(0.5\%\) source budget

## Purpose

Continue the remotely repaired T-106400 endpoint-companion programme and use
the freedom in the companion shift.  The all-pass winding does not depend on
which positive \(\lambda\) is chosen, while the endpoint-Turán leakage is linear
in \(\lambda\).

## Exact source theorem

Truncate the positive Xi Fourier half-source to \([0,L]\) and choose

```text
lambda L = 1/200.
```

The two same-sign Hankel channels have squared relative constant

```text
64/39601 < 1/600.
```

The two reflected Toeplitz orientations have squared relative constant

```text
640000/1568239201 < 1/2400.
```

Paying all four channels gives

```text
6348928/1568239201
 = 0.0040484436...
 < 1/200.
```

This is an exact source inequality, not a frozen Möbius model estimate.

## Conditional conclusion

If the finite two-boundary source is identified cofinally with the actual Xi
endpoint denominator bank, with normalized negative denominator trace \(o(d)\)
and all Fourier-tail, endpoint and confluent ledgers \(o(d)\), then the inverse
frame costs at most two after \(o(d)\) deletion.  The exact two-rung descent then
gives the safe conditional lower bound

```text
N0/N > 94741/100000 = 0.94741.
```

The sharper retained arithmetic is approximately `0.949311209632`.

## Exact open interface

```text
ENDPOINTBANK106410:
  source-for-source two-boundary endpoint-bank realization;
  o(d) normalized negative denominator trace;
  o(d) Fourier-tail, endpoint, common-zero and confluent ledgers.
```

The source contraction, numerator sign, companion index and inverse-frame
quantile are no longer open.  `ENDPOINTBANK106410` remains unproved, so neither
ninety percent nor RH is claimed.
