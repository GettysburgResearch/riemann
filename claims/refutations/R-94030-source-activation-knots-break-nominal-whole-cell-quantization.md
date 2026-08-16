# R-94030 — Source-activation knots break nominal whole-cell quantization

Claim ID: `R-94030`  
Status: **PROVED EXACT COUNTEREXAMPLE / SCOPE FIREWALL**  
Created: 2026-08-16  
Refutes at frozen head: PR #518 `L-92911` at `3277b831b30f4783ed3b087df57e95b9f7dfd7b0`  
RH status: **unproved**

## 1. The false implication

PR #518 uses an integer retained interval and concludes that every continuumized unit cell has no source-activation collar. It then maps a point `s in [n,n+1]` to the two endpoint states `n,n+1`, preserving the constant and `s^(-1/2)` modes.

Integer cell boundaries do not align with the arithmetic activation points

\[
 s=\frac Xk.
\]

## 2. Exact counterexample

Set

\[
 X=10^{12},
 \qquad k=3,
 \qquad n=\left\lfloor\frac X3\right\rfloor=333333333333,
\]

and

\[
 s_0=n+\frac16.
\]

The activation lies strictly inside the unit cell:

\[
 \frac X3=n+\frac13.
\]

The PR #518 lower endpoint is

\[
 K+2=\left\lfloor X/67\right\rfloor+3=14925373137,
\]

so `[n,n+1]` is a retained cell.

The label `k=3` is active at `n` and at `s_0` because

\[
 3s_0<X,
\]

but inactive at `n+1` because

\[
 3(n+1)=1000000000002>X.
\]

On the active side its SHARP target is

\[
 \widetilde T_3(s)
 =\frac{4\sqrt{X/(3s)}-3}{\sqrt3}.
\]

Its untruncated value at `n+1` is positive. Exactly,

\[
 16X>9\cdot3(n+1),
\]

since

\[
 16000000000000>9000000000018.
\]

Let `q_n(s_0),q_(n+1)(s_0)` be the positive two-point weights of `L-92911`. Affine preservation in `s^(-1/2)` gives

\[
 \widetilde T_3(s_0)
 =q_n(s_0)\widetilde T_3(n)
  +q_{n+1}(s_0)\widetilde T_3(n+1).
\]

Both `q_(n+1)(s_0)` and `T_3(n+1)` are positive. A source-exact realization must suppress the inactive endpoint term and therefore loses

\[
 q_{n+1}(s_0)\widetilde T_3(n+1)>0.
\]

A directed numerical display is

```text
q_(n+1)(s_0)              0.1666666666669791...
untruncated T_3(n+1)       0.5773502691873163...
lost target                0.0962250448647331...
```

If the endpoint term is retained, the quantizer creates a source occurrence outside causal support. Thus the stated map cannot preserve source incidence and exact target simultaneously.

## 3. Consequences

The same obstruction affects declared score and every component coordinate with a nonzero activation value. Differentiating a finite sum across such a unit cell must include the activation jump; the derivative estimate in `L-92912` does not.

One-sided values at the activation point have measure zero in direct integration but are not irrelevant to a positive endpoint stencil crossing the point.

```text
positive reciprocal-mode martingale        survives on fixed-support cells
integer cell endpoints remove activations  false
source-exact target-exact L-92911 map       false
L-92912 no-jump adjacent estimate           unproved
Riemann Hypothesis                          unproved
```
