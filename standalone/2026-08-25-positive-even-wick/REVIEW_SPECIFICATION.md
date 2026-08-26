# Hostile review specification — T-103060

Mandatory checks:

1. expand `1-tx_r=(1-x_r/2)-(t-1/2)x_r` coefficientwise;
2. verify every odd central moment on `[-1/2,1/2]` is zero;
3. verify
   \[
   \int_{-1/2}^{1/2}y^{2j}dy=1/[(2j+1)2^{2j}];
   \]
4. reconstruct the complete even-subset formula in `L-103009`;
5. recover the pair coefficient `1/12` and compare it with `L-103008`;
6. retain the midpoint factors on every unselected label;
7. verify `1-x/2=M(x)+x^2/2` and charge only the literal squared transfer;
8. reconstruct the source-owned equal-pair allocation of every nonempty even subset;
9. confirm `R-103002` remains binding and no TP2 shortcut drops the middle prefix;
10. verify the exact implication from the even-Wick rows to the canonical Boolean hierarchy;
11. confirm the replay checks only finite coefficient algebra;
12. confirm `BCI102990` and RH remain unproved.

Immediate falsifiers:

```text
using endpoint signs instead of the complete midpoint expansion;
dropping midpoint factors on unselected labels;
calling a positive Wick coefficient a positive physical observation;
charging one squared transfer more than once;
claiming SMEP/CCPF/HMO/CTZD are independent final gates;
claiming RH from T-103060.
```
