# L-96650 — The 5:3 scalar has a positive unsieved dictionary and a zero-safe reciprocal-zeta numerator

Status: **EXACT**

For `R_X=5c_X(2)+3c_X(3)`, the unsieved dictionary is

```text
q*(1)=0, q*(2)=15, q*(3)=6, q*(4)=3, q*(n)=6 for n>=5.
```

Its Mellin transform is

```text
6/s^2 - 3(1-2^-z)(2-2^-z)/(s^2 zeta(z)), z=s+1/2.
```

The finite numerator has no zero in `Re z>0` because `|2^-z|<1` there.
