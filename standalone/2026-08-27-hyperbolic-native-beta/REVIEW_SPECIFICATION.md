# Hostile review specification — T-107020

Frozen base:

```text
PR #759
d1b8aa57b08db1ba9f2edf3b68238c2a129b7c33
```

Mandatory reconstruction:

1. Verify `Lh(s)=exp(1-cos s)` with the stated Fourier/Laplace convention.
2. Shift the Fourier contour only inside `|Im t|<pi/2`.
3. Check that one may choose a physical decay exponent larger than `1/2`.
4. Reconstruct the complete-to-prefix tail with `X_T=e^(7T)`.
5. Separate the bilateral multiplier from the one-sided negative-time
   holomorphic correction.
6. Re-run the one-sided Mellin--Landau argument for the noncausal field.
7. Verify the Poisson autocorrelation identity and its normalization.
8. Check the alias distance `P_X-L_X=2R_X`.
9. Reconstruct the `O(X)` compact-prefix autocorrelation `L1` bound.
10. Verify the discrete double-exponential tail at
    `T_A=loglog X+O_A(1)`.
11. Confirm the rank `O(log X loglog X)`.
12. Confirm the detector is fixed and the feature norm remains open.

Immediate falsifiers:

```text
claiming exact Nyquist equality for the noncompact field;
using a contour shift of size >=pi/2;
dropping the negative-time transform correction;
letting the smoother depend on X;
inferring cancellation from low rank;
claiming HNBV107020 or RH is proved.
```
