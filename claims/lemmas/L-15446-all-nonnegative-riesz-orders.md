# L-15446 — Harris positivity holds at every nonnegative Riesz order

Claim ID: `L-15446`  
Title: Every nonnegative fractional Green primitive of the Jordan discrepancy and regular smoothed tail is positive; the unresolved endpoint lies exactly beyond order zero  
Status: `PROPOSED — COMPLETE HARRIS/RIESZ ARGUMENT; NEGATIVE-ORDER ENDPOINT OPEN`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: `L-15428`, `L-15430`; Harris association for product measures; Tonelli and fractional Riesz kernels  
Cross-route connections: `L-15431/L-15434`; PRs #158/#216/#222/#224/#226  
Scope: unconditional positivity of all softened prefix/Bohr coordinates; this does not prove the unsmoothed regular density nonnegative

## 1. Jordan measure

Fix

\[
0<s<1,
\qquad
F_s(n)=\prod_{p\mid n}(1-p^{-s}),
\qquad
c_s={1\over\zeta(1+s)}.
\tag{L-15446.1}
\]

Put

\[
\boxed{
 d\nu_s(u)
 =\sum_{n\ge1}{F_s(n)\over n}\delta_{\log n}(du)
 -c_s\,du.}
\tag{L-15446.2}
\]

`L-15428` is the order-zero assertion

\[
\nu_s([0,t])\ge0.
\]

## 2. All fractional prefix orders

For every real

\[
\alpha\ge0
\tag{L-15446.3}
\]

and `t>=0`, define

\[
\boxed{
\mathcal R_{s,\alpha}(t)
={1\over\Gamma(\alpha+1)}
\int_{[0,t]}(t-u)^\alpha d\nu_s(u).}
\tag{L-15446.4}
\]

Then

\[
\boxed{\mathcal R_{s,\alpha}(t)\ge0}
\qquad(\alpha\ge0,t\ge0).
\tag{L-15446.5}
\]

### Harris proof

Fix `beta>1` and choose a zeta-distributed integer

\[
\Pr_\beta(N=n)={n^{-\beta}\over\zeta(\beta)}.
\tag{L-15446.6}
\]

Its prime exponents are independent geometric variables. Both

\[
F_s(N)
\tag{L-15446.7}
\]

and

\[
W_{t,\alpha}(N)
=(t-\log N)_+^\alpha
\tag{L-15446.8}
\]

are coordinatewise decreasing in those exponents for every `alpha>=0`. Harris association gives

\[
\sum_{n\le e^t}
{F_s(n)\over n^\beta}(t-\log n)^\alpha
\ge
{1\over\zeta(\beta+s)}
\sum_{n\le e^t}{(t-\log n)^\alpha\over n^\beta}.
\tag{L-15446.9}
\]

The support is finite. Letting `beta downarrow1` yields

\[
\sum_{n\le e^t}{F_s(n)\over n}(t-\log n)^\alpha
\ge
c_s\sum_{n\le e^t}{(t-\log n)^\alpha\over n}.
\tag{L-15446.10}
\]

The function

\[
x\longmapsto{(t-\log x)^\alpha\over x}
\tag{L-15446.11}
\]

is nonnegative and decreasing on `[1,e^t]`. Therefore its left Riemann sum dominates its integral:

\[
\sum_{n\le e^t}{(t-\log n)^\alpha\over n}
\ge
\int_1^{e^t}{(t-\log x)^\alpha\over x}dx
={t^{\alpha+1}\over\alpha+1}.
\tag{L-15446.12}
\]

Equations (L-15446.10)--(L-15446.12) are exactly (L-15446.5).

For integer `alpha=k`, this proves positivity of every repeated Green primitive, not only the first one used in `L-15428`.

## 3. Laplace characterization

Let

\[
A_s(q)
={\zeta(1+q)\over\zeta(1+s+q)}
=\int e^{-qu}\sum_n{F_s(n)\over n}\delta_{\log n}(du).
\tag{L-15446.13}
\]

The Laplace transform of (L-15446.4) is

\[
\boxed{
\widehat{\mathcal R}_{s,\alpha}(q)
={A_s(q)-c_s/q\over q^{\alpha+1}}.}
\tag{L-15446.14}
\]

Thus

\[
\boxed{
q\longmapsto
{1\over q^{\alpha+1}}
\left[
 {\zeta(1+q)\over\zeta(1+s+q)}-{c_s\over q}
\right]
\text{ is completely monotone}}
\tag{L-15446.15}
\]

for every `alpha>=0`.

This is an unconditional infinite total-positivity hierarchy on the real axis.

## 4. Every nonnegative Riesz primitive of the regular tail is positive

Let `n_s>=0` be the beta-resolvent density of `L-15430`. The regular density has transform

\[
\widehat Y_s(q)
=\widehat n_s(q)
\left[A_s(q)-{c_s\over q}\right].
\tag{L-15446.16}
\]

Combining (L-15446.14) with the positive Laplace transform `widehat n_s` gives

\[
\boxed{
{\widehat Y_s(q)\over q^{\alpha+1}}
\text{ is completely monotone}}
\qquad(\alpha\ge0).
\tag{L-15446.17}
\]

Equivalently, for every `alpha>=0`,

\[
\boxed{
\mathcal I_{\alpha+1}Y_s(t)
:={1\over\Gamma(\alpha+1)}
\int_0^t(t-u)^\alpha Y_s(u)du
\ge0.}
\tag{L-15446.18}
\]

Thus every nonnegative fractional smoothing of the final regular density already has the desired sign.

## 5. The exact total-positivity boundary

The Abel–Riesz representation of `L-15431` contains the endpoint kernel

\[
\left(1-{U^2\over N^2}\right)^{s/2-1},
\tag{L-15446.19}
\]

whose order satisfies

\[
-1<{s\over2}-1<-{1\over2}.
\tag{L-15446.20}
\]

This is a **negative** fractional order. It lies immediately beyond the range in which the cutoff weight `W_(t,alpha)` is decreasing and Harris association has the favorable sign.

For `alpha<0`, the weight

\[
(t-\log N)_+^\alpha
\]

is increasing toward the admission boundary and singular there. Harris association reverses direction rather than proving (L-15446.5). This is not a technical defect in the proof: it is exactly the endpoint-localization that retains the RH obstruction.

Hence the repository-wide geometry is now:

```text
all nonnegative Green/Riesz orders:
    positive unconditionally;

full-period / Bohr energies:
    positive or critically bounded unconditionally;

negative fractional endpoint order:
    RH-bearing local-to-Bohr sign.
```

## 6. Consequences for the global routes

### Smoothed-Jordan route

Any negative value of `Y_s` must be invisible to every nonnegative fractional prefix integral. It is necessarily an endpoint-localized defect of the exact type isolated by `L-15431`.

### Selberg/prime/totient routes

The Bohr diagonalizations of `L-15444` and PR #226 are softened coefficient averages. Their unconditional positivity is the global-frequency counterpart of (L-15446.18). The missing local-to-Bohr theorem is a negative-order trace estimate, not another positive moment.

### Computation

A directed endpoint certificate should include correlated checks of several positive primitives (L-15446.18). A candidate negative cell that violates any one of them is a producer or normalization error.

## 7. Proof boundary

Closed exactly:

- Harris positivity for every real `alpha>=0`;
- the fractional Riesz integral and Laplace formulas;
- positivity of all nonnegative fractional primitives of `Y_s`;
- identification of the negative-order boundary in the endpoint kernel.

Open:

- positivity at order zero of the density itself;
- any extension of Harris association into the singular negative-order range;
- the endpoint lattice inequality and RH.

This lemma does not prove RH. It proves that the full obstruction is concentrated exactly at the negative fractional/local trace boundary.