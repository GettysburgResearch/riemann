# L-103073 — Quarter power is the unique Boolean cutoff balance

Claim ID: `L-103073`  
Status: **PROVED EXACT EXPONENT LEDGER**  
Created: 2026-08-26  
Depends on: `L-103070--L-103071`  
RH status: **not assumed**

Write the core horizon as `W` and choose a power cutoff

\[
U=W^\alpha
\]

up to fixed dyadic constants.

The complete squarefree Type-I theorem gives

\[
\boxed{
\mathcal T_U
=
W^{\alpha-1/4+o(1)}.
}
\tag{L-103073.1}
\]

Every balanced core contains two disjoint factors larger than `U`, and hence

\[
a^2>U^4=W^{4\alpha}.
\tag{L-103073.2}
\]

The compact physical observation permits only `a^2<=W`.

Consequently:

```text
alpha < 1/4:
  Type I is power-saving, but the balanced row can remain;

alpha = 1/4:
  Type I is subpower and the balanced row is support-empty;

alpha > 1/4:
  the balanced row is support-empty, but the inherited Type-I estimate
  incurs a positive power.
```

Thus

\[
\boxed{\alpha=\frac14}
\]

is the unique cutoff exponent at which the two demands meet exactly. The
historical sixth-root choice optimized for a power saving; the conclusion-facing
negative-mass theorem is instead optimized at the quarter-power endpoint.
