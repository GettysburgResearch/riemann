# R-91724 — Lipschitz interpolation alone does not prove native-relative root convergence

Claim ID: `R-91724`  
Status: **EXACT SCOPE CORRECTION TO L-91695**  
Created: 2026-08-14  
Depends on: no repository input  
Repair: `L-91724`  
RH status: **unproved**

## 1. The inference being corrected

`L-91695` argues that the complete typed root atom is piecewise Lipschitz and
that positive linear interpolation on a refining mesh therefore gives

\[
 \sup_x\|V_M(x)-V(x)\|_*\longrightarrow0,
\]

where the star norm divides each active coordinate by its native capacity.

That implication is not valid solely from unnormalized Lipschitz continuity
when the normalizing capacity vanishes at an activation knot.

## 2. Exact counterexample

On `[0,h]`, put

\[
 V(t)=c(t)=t^2.
\]

Both maps are Lipschitz.  The positive linear interpolant through the endpoint
values is

\[
 V_h(t)=ht.
\]

For `0<t<h`,

\[
 \boxed{
 \frac{|V_h(t)-V(t)|}{c(t)}
 =\frac ht-1.
 }
\tag{R-91724.1}
\]

At `t=h/N` the relative error is `N-1`.  Hence

\[
 \sup_{0<t\le h}
 \frac{|V_h(t)-V(t)|}{c(t)}
 =+\infty
\]

for every `h>0`, even though the absolute interpolation error tends uniformly
to zero as `h->0`.

Thus ordinary Lipschitz continuity does not establish the native-relative
claim.

## 3. What is and is not refuted

This counterexample does **not** prove that the actual factor-67 root atoms
have quadratic zeros or that a positive refinement is impossible.  It proves
only that the stated proof from raw Lipschitz continuity is incomplete.

`L-91724` repairs the step by:

```text
removing arbitrarily small positive collars around the finite activation set;
refining only on compact cells where every active capacity is bounded below;
using positive barycentric endpoint pushforward;
paying the resulting relative error from the explicit all-column reserve.
```

## 4. Boundary

```text
piecewise Lipschitz atom map                          compatible
raw linear interpolation absolute convergence        true
raw linear interpolation native-relative convergence not implied
positive collar/cellwise repair                       L-91724
factor-67 SONTR                                       still review-dependent
Riemann Hypothesis                                    unproved
```
