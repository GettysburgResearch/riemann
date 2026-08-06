# L-9510 — Exact Bernoulli–Möbius decomposition of the parabolic totient error

Claim ID: `L-9510`  
Title: The minimal polynomial cutoff reduces the full RH error to two periodic Mertens channels  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: Möbius inversion for `phi(n)/n`; elementary Faulhaber and Bernoulli identities  
Scope: proof-facing arithmetic decomposition for `T-9503`  
Related counterexample candidates: none

## Exact parabolic cell sum

For real `y>1`, define

\[
S_1(y)=\sum_{1\le m<y}
 \left(1-\frac{m^2}{y^2}\right).
\tag{L-9510.1}
\]

Let

\[
B_2(u)=u^2-u+\frac16,
\qquad
B_3(u)=u^3-\frac32u^2+\frac12u.
\tag{L-9510.2}
\]

Then

\[
\boxed{
S_1(y)=
\frac{2y}{3}-\frac12
-\frac1y B_2(\{y\})
+\frac1{3y^2}B_3(\{y\}).}
\tag{L-9510.3}
\]

The formula is valid at integer `y`; the endpoint term vanishes because the
weight is zero at `m=y`.

### Proof

Put

\[
r=\lceil y\rceil-1=y-\{y\}
\]

with `r=y-1` at integer `y`. Then

\[
S_1(y)=r-\frac{r(r+1)(2r+1)}{6y^2}.
\]

Substitute `r=y-{y}` and collect the periodic terms. The result is exactly
(L-9510.3).

## Parabolic totient observable

For real `x>1`, define

\[
\boxed{
\mathcal P(x)=
\frac1x\sum_{1\le n<x}
 \frac{\varphi(n)}n
 \left(1-\frac{n^2}{x^2}\right)}
\tag{L-9510.4}
\]

and center it by

\[
\mathcal E_1(x)=
\mathcal P(x)-\frac4{\pi^2}.
\tag{L-9510.5}
\]

Using

\[
\frac{\varphi(n)}n
=\sum_{d\mid n}\frac{\mu(d)}d
\]

and (L-9510.3) at `y=x/d` gives the exact identity

\[
\boxed{
\begin{aligned}
\mathcal E_1(x)={}&
-\frac23\sum_{d\ge x}\frac{\mu(d)}{d^2}
-\frac1{2x}\sum_{d<x}\frac{\mu(d)}d\\
&-\frac1{x^2}\sum_{d<x}
 \mu(d)B_2\!\left(\left\{\frac xd\right\}\right)\\
&+\frac1{3x^3}\sum_{d<x}
 \mu(d)d B_3\!\left(\left\{\frac xd\right\}\right).
\end{aligned}}
\tag{L-9510.6}
\]

The main constant is

\[
\frac23\sum_{d\ge1}\frac{\mu(d)}{d^2}
=\frac2{3\zeta(2)}
=\frac4{\pi^2}.
\tag{L-9510.7}
\]

Compared with the quartic decomposition `L-9508`, only two bounded periodic
channels remain.

## Mertens transfer

Suppose that, for some `beta in [1/2,1]` and every `epsilon>0`,

\[
M(X)=\sum_{n\le X}\mu(n)
=O_\varepsilon(X^{\beta+\varepsilon}).
\tag{L-9510.8}
\]

Then

\[
\boxed{
\mathcal E_1(x)
=O_\varepsilon(x^{\beta-2+\varepsilon}).}
\tag{L-9510.9}
\]

### First two channels

Ordinary partial summation gives

\[
\sum_{d\ge x}\frac{\mu(d)}{d^2}
=O_\varepsilon(x^{\beta-2+\varepsilon}),
\]

and

\[
\sum_{d<x}\frac{\mu(d)}d
=O_\varepsilon(x^{\beta-1+\varepsilon}).
\]

### Periodic channels

For

\[
f_{0,x}(t)=B_2(\{x/t\}),
\]

and

\[
f_{1,x}(t)=tB_3(\{x/t\}),
\]

one has, on each reciprocal cell and with continuous matching at cell
boundaries,

\[
|f_{0,x}(t)|\ll1,
\qquad
|f_{0,x}'(t)|\ll x t^{-2},
\tag{L-9510.10}
\]

and

\[
|f_{1,x}(t)|\ll t,
\qquad
|f_{1,x}'(t)|\ll1+x/t.
\tag{L-9510.11}
\]

Piecewise partial summation therefore yields

\[
\sum_{d<x}\mu(d)f_{0,x}(d)
=O_\varepsilon(x^{\beta+\varepsilon}),
\]

\[
\sum_{d<x}\mu(d)f_{1,x}(d)
=O_\varepsilon(x^{\beta+1+\varepsilon}).
\]

After multiplication by `x^-2` and `x^-3`, both contribute
`O_epsilon(x^(beta-2+epsilon))`.

The continuity at reciprocal-cell boundaries is load-bearing:

\[
B_2(0)=B_2(1),
\qquad
B_3(0)=B_3(1)=0.
\]

Hence no jump term is lost.

## Minimal two-Green interpretation

Let

\[
w_1(u)=(1-u^2)\mathbf1_{0<u<1}.
\]

Its Mellin transform is

\[
\boxed{
\widehat w_1(z)=
\frac1z-\frac1{z+2}
=\frac2{z(z+2)}.}
\tag{L-9510.12}
\]

Thus the parabolic observable is the two-Green smoothing of the totient
measure. In logarithmic coordinates, the causal kernel is

\[
g_1(t)=e^{-t}-e^{-3t}.
\tag{L-9510.13}
\]

If

\[
P(r)=\mathcal P(e^r),
\]

then, in the distributional sense,

\[
\boxed{
\frac12(\partial_r+1)(\partial_r+3)P(r)
=\sum_{n\ge1}\frac{\varphi(n)}{n^2}
 \delta(r-\log n).}
\tag{L-9510.14}
\]

The constant main term satisfies

\[
\frac12(1)(3)\frac4{\pi^2}
=\frac6{\pi^2},
\]

so the centered error is the two-Green solution of the exact signed source

\[
\sum_{n\ge1}\frac{\varphi(n)}{n^2}
 \delta(r-\log n)-\frac6{\pi^2}dr.
\tag{L-9510.15}
\]

This is the minimal polynomial Green depth at which the RH exponent is obtained
with a proof-facing Mertens transfer.

## Gap audit

- The exact identity does not prove the Mertens estimate.
- Partial summation must be performed piecewise across reciprocal cells.
- Replacing the Bernoulli functions by independent absolute maxima discards
  their shared endpoint cancellation.
- A finite exact table does not prove the uniform exponent.

## Independent-review targets

1. Verify the cell formula and strict-cutoff convention.
2. Reconstruct all factors in (L-9510.6).
3. Audit the cellwise derivative bounds and absence of jump terms.
4. Check the distributional two-Green identity and delta normalization.
