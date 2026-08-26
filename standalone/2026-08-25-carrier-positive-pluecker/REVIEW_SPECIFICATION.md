# Hostile review specification — T-103030

Mandatory checks:

1. reconstruct the six edge weights in `L-103007.1` from the extreme-pair source;
2. verify the compression to `S=a+b-ab`;
3. check the monotonicity bounds involving the intermediate survival products `A,B`;
4. verify both sign cases for `2c-S(1-c)`;
5. verify the convex quadratic argument and both minimizer regimes;
6. reconstruct the positive rectangle average of `L-103006`;
7. identify the exact homogeneous carrier used in the frozen source ledger;
8. verify that carrier subtraction occurs before every negative part;
9. reproduce `R-103001` and reject scalar-to-operator promotion;
10. confirm `CCPF103030`, `PLC103020`, `BCI102990`, and RH remain unproved.

Immediate falsifiers:

```text
using unordered activities in L-103007;
replacing distinct shifts by scalar activities in the physical theorem;
dropping the centered translated fluctuation;
claiming the rational replay proves operator positivity;
claiming carrier positivity proves RH.
```
