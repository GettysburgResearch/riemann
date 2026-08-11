# Critical-hinge continuation: monotonicity and generic convexity fail; exact weighted targets survive

**Date:** 2026-08-11  
**RH:** unproved

## 1. Exact top-inverse cone

The top-half inverse has the exact criterion

\[
q(q-1)c(q)
=
q(q+1)[h(q)-h(q+1)]
+
2\sum_{m>q}m[h(m)-h(m+1)].
\]

This identifies a larger positive cone than decreasing targets.

## 2. Recursive monotonicity fails

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

## 3. Generic convexity also fails

Every decreasing convex target is a positive mixture of linear hinges

\[
H_K(q)=(K+1-q)_+.
\]

But the exact average-carry response to one such extreme ray is signed:

\[
a_{60}(11)=-\frac2{55},
\]

with positive neighbours `53/45` and `131/33`. Therefore no source-blind theorem saying that average-carry inversion preserves the entire decreasing-convex cone can prove CHS.

The square-root target has the exact representation

\[
h_T(q)=\sum_{K=2}^{T-1}\omega_{T,K}H_K(q),
\qquad \omega_{T,K}>0,
\]

and hence

\[
c_T(n)=\sum_{K=n}^{T-1}\omega_{T,K}a_K(n).
\]

The live theorem is the specific weighted cancellation of this signed response kernel under the square-root weights \(\omega_{T,K}\sim3K^{-5/2}/4\).

## Verification

```text
PASS_X_90702_CRITICAL_HINGE_MONOTONICITY_FIREWALL
PASS_X_90706_SIGNED_LINEAR_HINGE_RESPONSE
```

The first replay uses directed radical intervals. The second reconstructs the complete `E=60` inverse with exact `Fraction` arithmetic and verifies 95,040 hinge-basis decomposition identities.
