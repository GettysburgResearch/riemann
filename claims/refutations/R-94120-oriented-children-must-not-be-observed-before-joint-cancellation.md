# R-94120 — An oriented rough child cannot be exposed as a separate positive physical row

Claim ID: `R-94120`  
Status: **PROVED EXACT OBSTRUCTION / NORMATIVE COMPILER FIREWALL**  
Created: 2026-08-16  
Inputs: review PR #512; proposal PR #514; native/rough normalization firewall  
RH status: **unproved**

For the paired `P_61` stopping line, signed observation gives

```text
finite forcing observation         = native + rough reservoir,
actual oriented child observation  = - rough reservoir.
```

At ordinary column `q=2`, the single rough factor `m=67` contributes

\[
 C_{\rm rough}(2)
 \ge \frac{\log(X/134)}{\sqrt{134}}
 \qquad (X>134).
\]

At `X=536`,

\[
\frac{\log4}{\sqrt{134}}>\frac19.
\]

Indeed `log 4>4/3` by
`log t >= 2(t-1)/(t+1)` at `t=2`, and `sqrt(134)<12`.  Therefore

\[
 C_{\rm child}(2)<-\frac19.
\]

The same witness survives in radix-four detail because the `4q` term is zero
at this support boundary.  A separately nonnegative physical row has
nonnegative ordinary response, so the oriented child block cannot be
physicalized branchwise.

This does **not** obstruct a paired source recursion.  In the controlling
compiler, the negative child incidence remains unobserved until it is coupled
with its parent inside a terminal Target–Lorenz leaf.  Only the resulting
nonnegative leaf row is physically observed.  A positive terminal child created
by the exact causal budget is a different incidence and keeps its own source
owner.

Reject any implementation that:

```text
observes an oriented child before terminal coupling;
identifies the oriented child with a full child capacity;
applies q/4q detail separately on child branches;
or erases the parity/orientation label before gluing.
```
