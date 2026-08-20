# Research report — exact Euler-cube flow and the PXGC parity barrier

## Result

The missing local cut-compression problem was solved exactly. Every weighted
Boolean cube admits an explicit Hasse flow whose sole residual is the Euler
parity product \(\prod_i(1-r_i)\). The factor-67 box decomposes into complete
activation layers, where this flow applies, and a partial collar with an
explicit power-scale estimate.

The same theorem supplies a binding no-go: under the product activation
constraint the parity residual cannot be smaller than order
\(1/\log\log Y\). Hence independent source-blind cube matching cannot prove
the half-order PXGC bound.

## Consequence

The remaining cancellation is necessarily cross-core and phase-sensitive. It
must be extracted before equal integer products are collapsed. Generic PSD
completion, independent cube flow, or unrestricted path reachability cannot
supply it.

## Exact status

```text
complete local cube transport             proved
activation collar                         proved
local source-blind closure                refuted
EPXGC99900 cross-core flow                open
RH                                        unproved
```
