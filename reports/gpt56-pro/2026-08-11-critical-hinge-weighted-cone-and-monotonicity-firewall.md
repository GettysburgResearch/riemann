# Critical-hinge continuation: monotonicity fails, the exact weighted cone survives

**Date:** 2026-08-11  
**RH:** unproved

## Result

The top-half inverse has the exact criterion

\[
q(q-1)c(q)
=
q(q+1)[h(q)-h(q+1)]
+
2\sum_{m>q}m[h(m)-h(m+1)].
\]

This identifies a larger positive cone than decreasing targets.

The tempting staged induction through ordinary monotonicity fails exactly. For
the square-root hinge at \(T=894\), after four exact top-half eliminations,

\[
h_4(28)-h_4(29)<-4.637751038104930\times10^{-6}.
\]

Nevertheless the next coefficient remains positive:

\[
c_5(28)>0.006346716962584759.
\]

Thus the route must propagate the weighted-tail cone, not pointwise decrease.

## Verification

```text
PASS_X_90702_CRITICAL_HINGE_MONOTONICITY_FIREWALL
```

The replay uses no floating recursion: it pulls both quantities back to exact
rational linear forms in \(q^{-1/2}\) and evaluates them with directed
integer-square-root intervals.
