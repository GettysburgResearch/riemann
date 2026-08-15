# L-93601 — The complete Target-Lorenz proportional determinant is positive on the unbounded tail

Claim ID: `L-93601`  
Status: **PROPOSED COMPLETE ANALYTIC / EXACT-EVENT TAIL THEOREM — HOSTILE REPLAY REQUIRED**  
Created: 2026-08-15  
Depends on: `L-91682`, `L-91780`, `L-91782`, `L-93600`  
Replay: `X-93600-target-lorenz-tail`  
RH status: **unproved**

Let

\[
x=py,
\qquad p\ge67,
\qquad1\le y<67,
\qquad2\le j\le66.
\]

For the causal even/odd target and row totals, put

\[
\Theta_j(p,y)=O_T E_R^{(j)}-E_T O_R^{(j)}.
\]

Then

\[
\boxed{
 x\ge166000\quad\Longrightarrow\quad
 \Theta_j(p,y)>26>0.
}
\tag{L-93601.1}
\]

The theorem is uniform in real `p` and `y`; primality or integrality of `p` is
not used in the tail estimate.

## 1. Exact finite prefix data

For `sigma in {+,-}`, define the `P_61` divisor prefixes

\[
A_\sigma(z)=\sum_{\substack{d\mid P_{61},\ d\le z\\\mu(d)=\sigma}}\frac1d,
\quad
B_\sigma(z)=\sum_{\substack{d\mid P_{61},\ d\le z\\\mu(d)=\sigma}}\frac1{\sqrt d},
\]

\[
C_\sigma(z)=\sum_{\substack{d\mid P_{61},\ d\le z\\\mu(d)=\sigma}}
 \frac{\log d}{\sqrt d},
\quad
D_\sigma(z)=\sum_{\substack{d\mid P_{61},\ d\le z\\\mu(d)=\sigma}}d.
\]

Put `z=x/(j+1)`. On `d<=z`, insert the component-row expansion from
`L-93600.4`. On the sole boundary strip

\[
\frac{x}{j+1}<d\le\frac{x}{j},
\]

use the exact first-activation formula and the uniform upper bound

\[
q_j^{\rm strip}
=\frac{j+1}{(j-1)\sqrt j}\log\frac{j+1}{j}.
\]

This gives explicit envelopes

\[
\underline E_R^{(j)}(x),
\qquad
\overline O_R^{(j)}(x).
\]

The bulk remainder is charged with its sign by

\[
\frac{5C_j}{x^{3/2}}D_+(z),
\qquad
\frac{5C_j}{x^{3/2}}D_-(z),
\qquad C_j=\frac2{j(j-1)}.
\]

With the exact parent target prefixes, the parent determinant has the lower
envelope

\[
\underline\Theta_j^{\rm par}(x)
=T_-^{\rm par}(x)\underline E_R^{(j)}(x)
 -T_+^{\rm par}(x)\overline O_R^{(j)}(x).
\tag{L-93601.2}
\]

## 2. Finite exact-event reduction of the real tail

All prefix states in (L-93601.2) change only at

\[
x=d,
\qquad x=jd,
\qquad x=(j+1)d,
\qquad d\mid P_{61}.
\tag{L-93601.3}
\]

The generator enumerates all `2^18` divisors and sorts the `51,118,080`
row-event records as exact unsigned 128-bit integers. Between consecutive
events, with `t=sqrt(x)`, the lower envelope has the fixed form

\[
At^2+Bt\log t+Ct+D\log t+E+Ft^{-2}+Gt^{-3}.
\tag{L-93601.4}
\]

Its derivative is bounded term by term at the interval endpoints. The replay
returns the strict global margins

\[
\boxed{
\underline\Theta_j^{\rm par}(x)>79,
\qquad
\frac{d}{dt}\underline\Theta_j^{\rm par}(t^2)>0.23
}
\tag{L-93601.5}
\]

on every finite event interval. The computed parent minimum is

```text
79.237289759903788... at x=166000, j=66.
```

After the final event, the complete even/odd prefixes make the `t^2` and bare
`log t` coefficients cancel exactly. The remaining second derivative has the
sign of

\[
Bt^4+6Ft+12G.
\]

The generator checks this polynomial and its derivative at the final event;
both are positive, so the derivative bound persists on the final unbounded
interval.

## 3. Uniform child correction

Write `r=sqrt(y/x)`. Expanding the causal determinant gives

\[
\Theta_j(p,y)
=\Theta_j^{\rm par}(x)-rL_j(x,y)+r^2Q_j(y).
\tag{L-93601.6}
\]

All child terms lie on `1<=y<67`. Their target totals are bounded by the exact
`P_61` prefix through `67`, and their component rows by

\[
Q_Y(j)
\le
\frac{j+1}{(j-1)\sqrt j}\log\frac{67}{j}
 +\frac8{j(j-1)}\sqrt{67}.
\tag{L-93601.7}
\]

This yields an explicit nonnegative correction envelope
$\mathcal C_j(x)$. On a fixed event interval it has the form

\[
A_0+\frac{B_0\log t+C_0}{t}+\frac{D_0}{t^2},
\qquad A_0,B_0,C_0,D_0\ge0.
\tag{L-93601.8}
\]

Since `t>=sqrt(166000)>e`, (L-93601.8) is nonincreasing. Therefore the full
lower envelope is minimized at an event endpoint. The complete sweep proves

\[
\boxed{
\underline\Theta_j^{\rm par}(x)-\mathcal C_j(x)>26.
}
\tag{L-93601.9}
\]

The computed global minimum is

```text
26.786236008153155... at x=166000, j=66.
```

This proves (L-93601.1).

## 4. Replay and rounding contract

The published checker rebuilds the generator, reruns the complete event sweep,
checks the analytic `5Y^(-3/2)` reserve, checks the exact compact/tail join and
rejects five hostile threshold/domain mutations. Event ordering is exact; the
transcendental evaluation uses extended `long double` arithmetic with a
published one-unit reserve below the computed full minimum. The retained
minimum exceeds the theorem margin by more than `0.78`.

This is a proposed complete analytic/finite-event certificate for hostile
reconstruction. It does not turn the replay itself into an accepted proof of
RH.
