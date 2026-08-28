# Review specification — T-107000

Frozen parent:

```text
PR #758
070be728e8d434bfb72645e23f9894acf920d3c0
```

Reconstruct in this order:

1. Verify convergence and support of the logarithmic box cascade.
2. Prove local-uniform convergence of its entire Laplace product.
3. Check that every zero of every box factor lies on the imaginary axis.
4. Reproduce the first-\(N(t)\)-factor Fourier bound.
5. Derive the every-power tail at
   `T_A(X)=C_A log X (loglog X)^2`.
6. Confirm that convolution preserves every open-half-plane reciprocal-zeta
   pole and the exact beta source.
7. Derive the Fourier-series Parseval identity with the factor `1/P_X`.
8. Bound the discrete sample tail, not merely the continuous tail.
9. Verify the `O(log^2 X loglog^2 X)` sample count.
10. Confirm that the theorem proves an RH-equivalent criterion, not RH.

Immediate falsifiers:

```text
an X-dependent smoothing kernel;
a Laplace zero in Re(s)>0;
using an interval shorter than the physical support;
replacing beta by a completed or squared source;
claiming low rank implies a small norm;
claiming the replay proves NBV107000 or RH.
```
