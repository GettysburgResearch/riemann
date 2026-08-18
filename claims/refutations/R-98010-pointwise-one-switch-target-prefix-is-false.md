# R-98010 — Pointwise one-switch target-prefix positivity is false

Claim ID: `R-98010`  
Status: **PROVED EXACT COUNTEREXAMPLE**  
Created: 2026-08-18  
Depends on: `L-98012`  
RH status: **unproved**

The pointwise sufficient theorem `OSTP67` proposed as a search target in `T-98010` is false even in the canonical `P_61` state.

Take

\[
P=P_{61},\qquad X=600,\qquad Y=100,
\qquad K=X/Y=6.
\]

The strict one-switch cutoff in `L-98012` is `d<K`. Among divisors of `P_61`, the only active indices are

\[
1,2,3,5.
\]

Therefore

\[
\sum_{d<6}{\mu(d)\over d}
=1-{1\over2}-{1\over3}-{1\over5}
=-{1\over30},
\]

and

\[
\sum_{d<6}{\mu(d)\over\sqrt d}
=1-{1\over\sqrt2}-{1\over\sqrt3}-{1\over\sqrt5}.
\]

The exact target prefix is

\[
\begin{aligned}
\mathcal T_{P_{61}}(600;100)
&=4\sqrt{600}\left(-{1\over30}\right)
-3\left(1-{1\over\sqrt2}-{1\over\sqrt3}-{1\over\sqrt5}\right)\\
&=-{4\sqrt6\over3}-3
+{3\over\sqrt2}+\sqrt3+{3\over\sqrt5}.
\end{aligned}
\tag{R-98010.1}
\]

This is strictly negative by elementary rational bounds. Indeed,

\[
\sqrt6>{12\over5},
\qquad
{3\over\sqrt2}<{13\over6},
\qquad
\sqrt3<{7\over4},
\qquad
{3\over\sqrt5}<{27\over20}.
\]

Hence

\[
\mathcal T_{P_{61}}(600;100)
< -3-{16\over5}
+{13\over6}+{7\over4}+{27\over20}
=-{14\over15}<0.
\tag{R-98010.2}
\]

All inequalities are verified by squaring positive rational endpoints.

## Exact consequence

The implication

\[
\mathrm{OSTP67}\Longrightarrow\text{all Euler-minus hinges}
\]

remains algebraically valid, but its premise is false. It must not be used as a closure target.

This counterexample does **not** refute the hinge itself. By `L-98012`, an Euler-minus hinge is the cumulative integral

\[
(\mathcal E_PH_\lambda)(X)
=\int_\lambda^6\mathcal T_P(X;Y_u)\,du.
\]

A negative pointwise target prefix can be paid by positive prefixes at larger marginal levels. The exact surviving target is therefore cumulative one-switch positivity, not pointwise positivity.

```text
ordered marginal ratio                         PROVED
one-switch target-prefix formula                PROVED
pointwise target-prefix positivity OSTP67       FALSE
cumulative hinge-integral positivity            OPEN
root lambda=0 integral / GPC67                  OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVEN
```
