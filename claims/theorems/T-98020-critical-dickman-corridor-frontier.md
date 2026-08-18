# T-98020 — The factor-67 producer is confined to one critical Dickman corridor

Claim ID: `T-98020`  
Status: **UNCONDITIONAL OFF-CRITICAL CLOSURE; CRITICAL PRODUCER OPEN**  
Created: 2026-08-18  
Depends on: `L-98020`, `L-98021`, `R-98020`; PRs #594, #599, #601, #602  
RH status: **unproved**

For a native state with endpoint `Y` and least allowed rough prime `z`, put

\[
u(Y,z)=\frac{\log Y}{\log z}.
\]

The live factor-67 portfolio now has matching positive and negative scale
information:

1. PR #594/#598 proves that every count-depth stopping mechanism satisfying
   `L log L=o(log log Y)` fails.
2. PR #602 proves positivity for every fixed power-scale least prime.
3. `L-98021` closes the entire expanding range

   \[
   u(Y,z)\le(1-\epsilon)
   \frac{\log\log Y}{\log\log\log Y}
   \]

   for every fixed `epsilon>0`.
4. `R-98020` proves that bounded-source absolute control cannot pass the same
   saddle.

Hence any negative state, and therefore any obstruction to the root producer,
must occur in the critical or supercritical corridor

\[
\boxed{
 u(Y,z)\ge(1-o(1))
 \frac{\log\log Y}{\log\log\log Y}.
}
\tag{T-98020.1}
\]

Equivalently,

\[
\boxed{
\log z
\le(1+o(1))
\frac{\log Y\,\log\log\log Y}{\log\log Y}.
}
\tag{T-98020.2}
\]

## Exact remaining correlation

Write

\[
b(t)=a_*\sqrt t+e(t).
\]

Then every state has the exact decomposition

\[
\boxed{
\mathcal F(Y,z)
=a_*\sqrt Y\,S(Y,z)
+
\sum_{m}
\frac{\mu(m)}{\sqrt m}e(Y/m).
}
\tag{T-98020.3}
\]

`L-98020` controls the first term by Dickman theory. The sole unresolved source
in the critical corridor is therefore the explicit bounded-remainder
correlation

\[
\boxed{
\mathrm{CBRC}_{67}(Y,z):
\qquad
\sum_m\frac{\mu(m)}{\sqrt m}e(Y/m)
\ge-a_*\sqrt Y\,S(Y,z).
}
\tag{T-98020.4}
\]

At root scope this is not asserted to be easier than `GPC67`; it is an exact
source decomposition that removes every off-critical state and every
homogeneous Dickman term.

If `CBRC67` holds throughout the remaining critical state family, then every
native state is nonnegative. In particular the root scalar `GPC67` is
nonnegative eventually, and the fixed zero-safe Mellin-Landau consumer gives
RH.

\[
\boxed{
\mathrm{CBRC}_{67}
\Longrightarrow
\mathrm{GPC}_{67}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-98020.5}
\]

`CBRC67` is not proved here.

```text
fixed power sectors                         CLOSED
near-critical u<(1-eps)L2/L3 sectors       CLOSED
subcritical count-depth mechanisms          REFUTED
bounded-remainder absolute continuation     REFUTED BEYOND SADDLE
critical bounded-remainder correlation      OPEN / RH-BEARING
root scalar GPC67                            OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVEN
```
