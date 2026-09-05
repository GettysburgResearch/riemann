## T-106620 — mesoscopic frozen Riemann--Siegel gauge

A hostile check found a quantifier gap in the T-106610 height claim.
`L-106603` supplies a window-dependent Rouché threshold but no lower bound for
it; \(1/\vartheta'=O(1/\log T)\) is therefore not automatically small enough.

The corrected construction partitions the dyadic interval into
\((\log T)^B\) regular subwindows and freezes

```text
lambda_j = 1/theta'(t_j)
```

on each one. This gives simultaneously:

```text
constant-scale rank-one companion-height control;
total shift-height O(N/log T)=o(N);
carrier mismatch O(log(T)^(-B-1));
exact amplitude cancellation in the fifth Wronskian;
the same 3/4000 denominator-height budget;
the same 3/40 deep-model-space payment.
```

The sole live gate is now `MESORSGAUGE106620`: the sum of the shallow
canonical-correlation defects of these explicit finite zeta-derivative
cross-ratios must be below `11/500 N`. It implies more than 90%, but remains
open. T-106610's exact algebraic factorization is retained; only its
unquantified height inference is superseded.
