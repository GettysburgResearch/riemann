# Confluent zero-heat continuation — 2026-08-11

**Branch:** `research/gpt56-pro/375-confluent-zero-heat-monotonicity`  
**Base:** PR #375 at `a3662f62ac0f1a7ec21bca3498938fedcbeeddba`  
**Status:** new abstract reality theorem, zeta criterion, and finite linear witness interface  
**RH:** unproved

## Main advance

The target-depth parameter in PR #375 can be removed exactly. Its normalized three-Gaussian residue kernel

\[
-2e^{q(z^2-y^2)}
\left(\frac{\sinh(qyz)}{\sinh(qy^2)}\right)^2
\]

has confluent limit

\[
y^2W_{q,y}(z)\longrightarrow-2z^2e^{qz^2}.
\]

This produces the universal first-Hermite Gaussian square

\[
(z-x)^2e^{-q(z-x)^2}.
\]

For any conjugation-invariant multiset in a bounded strip with subquadratic horizontal counting, all points are real exactly when the sum of these squares is nonnegative for every `q>0,x in R`.

## New terminal graph

For upper-half-plane points `t+iy` and `u+id`, define

\[
t+iy\to u+id
\quad\Longleftrightarrow\quad
 d^2-(u-t)^2\ge y^2.
\]

An infinite threat chain would satisfy

\[
\sum|t_{n+1}-t_n|^2<a^2,
\qquad |t_n-t_0|<a\sqrt n,
\]

which contradicts subquadratic counting. A terminal pair therefore exists. At its ordinate,

\[
\frac{\mathcal M(q,t_0)}{2y_0^2e^{qy_0^2}}\to-m_0.
\]

This gives a strict negative witness under any nonreal zero.

## Zeta criterion

For centered zeta zeros `gamma_rho=(rho-1/2)/i`,

\[
\mathrm{RH}
\iff
\sum_\rho m_\rho(\gamma_\rho-x)^2
 e^{-q(\gamma_\rho-x)^2}\ge0
\quad(q>0,x\in\mathbb R).
\]

Equivalently, the unnormalised zero heat trace is monotone in heat time. Positive integer `q` and rational `x` already form a complete countable criterion.

## Prime-side interface

The inverse autocorrelation is

\[
k_{q,x}(u)=
\frac{e^{-ixu}}{4\sqrt\pi q^{3/2}}
\left(1-\frac{u^2}{2q}\right)e^{-u^2/(4q)}.
\]

Guinand--Weil therefore gives one explicit first-Hermite Gaussian prime inequality. Its tail is superconvergent in `log n`; `Lambda(n)<=log n` supplies a closed all-integer tail envelope. False RH would have a finite rational-parameter, finite-prime strict negative certificate.

## What this closes

```text
pair-depth-adapted Gaussian parameter          removed by confluent limit
abstract nonreal-pair terminal theorem         proposed complete
first-Hermite reality criterion                proposed complete
zero-heat monotonicity criterion               proposed complete
zeta specialization                            proposed complete
countable parameter reduction                  proposed complete
finite linear witness under false RH           proposed complete
```

## What remains

The prime inequality itself remains RH-equivalent. No phase-blind estimate or finite regression proves it. The next legitimate attacks are:

1. a source-ordered square or reflection-positive representation of the first-Hermite prime sum;
2. a heat-flow comparison theorem for the pole-subtracted logarithmic derivative;
3. a Brownian/Dirichlet-Hermite approximation that preserves first-Hermite positivity cofinally;
4. a directed computational search over rational `(q,x)` using the explicit Gaussian tail certificate.
