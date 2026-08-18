# M-95500 — Hostile review protocol for the SACF resonance packet

Review in this order:

1. Freeze PR #580 at `812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05`.
2. Reconstruct the bijection `m=da,n=db` for odd squarefree pairs.
3. Verify the local state table and
   `1-u-v+uv=(1-u)(1-v)`.
4. Check that the common-divisor exponent is exactly `s1+s2`; reject any
   normalization with a different `d` power.
5. Differentiate the triple series and verify that `log m=log a+log d`.
6. Audit every zero of `q`, `A2`, and `W_hat` in `0<Re z<1/2`.
7. Check pole orders: `M_o'` is one order higher than the `J1` term.
8. Reconstruct the parent identity
   `A(X)^2=S_H(X)+O_B(log^(B+2) X)`.
9. Apply the Mellin holomorphy argument for the exponent dictionary.
10. Verify the odd-Mertens identity and ten-band partial summation in `L-95504`.
11. Treat the classical zero-free-region estimate as an explicit imported theorem.
12. Treat every numerical scan as reconnaissance only.

Immediate rejection conditions:

```text
common divisor treated as carrying a Möbius sign;
d exponent not equal to s1+s2;
J1 allowed to cancel the M_o' leading pole;
positive autocorrelation claimed to give arithmetic cancellation;
the imported subexponential gain promoted to a fixed power;
a fixed SACF power saving called routine;
SACF or RH represented as proved.
```
