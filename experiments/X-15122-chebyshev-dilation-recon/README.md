# X-15122 — Chebyshev dilation-energy reconnaissance

This discovery-only experiment evaluates the exact scale-difference signal

\[
 Q_a(\log t)
 =t^{-1/2}[\psi(t)-a\psi(t/a)]
\]

on complete logarithmic blocks using every prime power through `10^7`.

The producer uses an integer event sweep. A prime power `n=p^k` creates:

```text
+log(p)     at t=n,
-a log(p)   at t=a n.
```

Between events, `psi(t)-a psi(t/a)` is constant, so its contribution is
integrated by the exact antiderivative of `t^-2`. The diagonal Gram contribution
is accumulated independently from each prime-power basis function.

The retained run covers integer scales

```text
2, 3, 4, 5, 8, 16
```

and complete blocks

```text
j=2,...,15.
```

At scale four and block `j=15`:

```text
total energy          0.249166414237714545
diagonal             40.7125639348243382
off diagonal        -40.4633975205866250
total / diagonal      0.00612013565730221316
```

Thus more than `99.38%` of the diagonal is canceled off diagonal even before
the compact triangular smoothing of PR #216. Across blocks `5,...,15`, scale
four has mean total energy about `0.25648` and mean total/diagonal ratio about
`0.01276`.

The scale scan separates two scheduling objectives:

- scale two has the smallest mean absolute energy in the retained range;
- scale four has the smallest mean relative energy among the tested scales;
- larger scales reduce the final relative ratio further but increase absolute
  energy.

Classification:

```text
LONG_DOUBLE_RECONNAISSANCE
```

The prime-power enumeration is complete and the cell antiderivatives are exact
in formula, but arithmetic is ordinary long double. There is no outward
rounding, independent compiler replay, or global inference. These values are
empirical evidence for the signed scale-coherence mechanism, not evidence for
RH.