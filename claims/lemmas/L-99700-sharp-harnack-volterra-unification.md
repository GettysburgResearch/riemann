# L-99700 — The factor-67 SHARP defect is a positive Volterra transform of one reciprocal prefix

Claim ID: `L-99700`  
Status: **PROVED EXACT FINITE/REAL-VARIABLE IDENTITY**  
Created: 2026-08-20  
Depends on: the scalar definitions of `L-99270`  
RH status: **not assumed**

Put

\[
\beta(n)=\mu(n)-\mathbf 1_{67\mid n}\mu(n/67),
\qquad
T(y)=(4\sqrt y-3)\mathbf 1_{y\ge1},
\]

and

\[
h(x)=\sum_{n\le x}\frac{\beta(n)}{\sqrt n}T(x/n).
\tag{L-99700.1}
\]

Define the two reciprocal prefixes

\[
A_\beta(x)=\sum_{n\le x}\frac{\beta(n)}n,
\qquad
B_\beta(x)=\sum_{n\le x}\frac{\beta(n)}{\sqrt n},
\tag{L-99700.2}
\]

with zero extension below `1`. Direct expansion gives

\[
\boxed{
h(x)=4\sqrt x\,A_\beta(x)-3B_\beta(x).
}
\tag{L-99700.3}
\]

Abel summation, applied to the step function `A_beta`, gives exactly

\[
B_\beta(x)
=\sqrt x\,A_\beta(x)
-\frac12\int_1^x A_\beta(t)\frac{dt}{\sqrt t}.
\tag{L-99700.4}
\]

Writing `U(x)=sqrt(x) A_beta(x)`, one obtains

\[
\boxed{
h(x)=U(x)+\frac32\int_1^xU(t)\frac{dt}{t}.
}
\tag{L-99700.5}
\]

Solving (L-99700.4) for `U`, or checking by finite Fubini, yields the second exact form

\[
\boxed{
h(x)=B_\beta(x)
+2\sqrt x\int_1^x B_\beta(t)\frac{dt}{t^{3/2}}.
}
\tag{L-99700.6}
\]

Every kernel in (L-99700.5)--(L-99700.6) is positive. Consequently

```text
A_beta >= 0  => h >= 0;
B_beta >= 0  => h >= 0,
```

at the corresponding all-smaller-scales scope. More importantly, the live SHARP Harnack route and the reciprocal-Julia prefix route are not independent frontiers: they are joined by one explicit first-order Volterra resolvent.

In logarithmic coordinates `u=log x`, the transfer from `B_beta` to `h` has Laplace multiplier

\[
\frac{s+3/2}{s-1/2}=1+\frac2{s-1/2}.
\tag{L-99700.7}
\]

Thus the positive Volterra lift introduces no new off-line zero cancellation. It also shows exactly why a prefix estimate that is too weak by a factor `sqrt(x)` cannot be rescued by the SHARP kernel: the lift is positive but not contractive at the half-order mode.

All identities are finite at each `x`; no asymptotic interchange or form of RH is used.