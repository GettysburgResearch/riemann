# Hostile review specification

Reject `L-97400` upon any of:

1. a coefficient-convolution mismatch in (L-97400.3);
2. a missed noninteger activation breakpoint;
3. a primitive interval not containing the exact `sqrt`, `log`, or
   `zeta(1/2)` value;
4. a finite endpoint outside `3..10^6` not owned by the analytic tail;
5. a missing P61 divisor or tail interval;
6. an incorrect constant in the scalar asymptotic.

Reject `R-97401` only if the consumed PR #565 parent can be exhibited as one
single typed packet that simultaneously:

```text
has canonical P61 marginals F,M;
has its p-divisible subpacket in the swapped channel;
and retains the actual rough Euler root coefficient.
```

Reject `R-97402` only if `L-96651` supplies a separate theorem comparing the
Hall-complement scalar to the reserved child scalar without spending either
source twice.

The replay does not prove the open source-complete producer or RH.
