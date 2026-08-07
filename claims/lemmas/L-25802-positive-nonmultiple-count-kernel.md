# L-25802 — Positive nonmultiple-count kernel

Claim ID: `L-25802`  
Title: Every multiplicative radix has a positive causal counting kernel whose transform is the stable zeta-cancelling multiplier `(1-Q^-s)zeta(s)/s`  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #258  
Dependencies: elementary summation by parts  
Scope: every integer radix `Q>=2`

## 1. Arithmetic nonmultiple kernel

Let `delta_Q` be the arithmetic atom at `Q` and define

\[
a_Q=\mathbf1*(\varepsilon-\delta_Q).
\tag{L-25802.1}
\]

Then

\[
\boxed{
a_Q(n)=1-\mathbf1_{Q\mid n}.}
\tag{L-25802.2}
\]

Thus `a_Q` is the indicator that an integer is not divisible by `Q`.
Its Dirichlet series is

\[
\boxed{
\sum_{n\ge1}{a_Q(n)\over n^s}
=(1-Q^{-s})\zeta(s),
\qquad \Re s>1.}
\tag{L-25802.3}
\]

The factor `1-Q^-s` is important: after the square-root shift its causal inverse
has norm bounded by a geometric series with ratio `Q^-1/2`.

## 2. Positive physical primitive

For real `t`, put

\[
N(t)=\lfloor e^t\rfloor
\]

and define

\[
\boxed{
\mathcal C_Q(t)
=e^{-t/2}
\left(
 N(t)-\left\lfloor{N(t)\over Q}\right\rfloor
\right)
\mathbf1_{t\ge0}.}
\tag{L-25802.4}

The bracket counts the positive integers at most `N(t)` which are not divisible
by `Q`. Therefore

\[
\boxed{\mathcal C_Q(t)\ge0.}
\tag{L-25802.5}
\]

On every open interval between logarithmic integer knots,

\[
(\partial_t+1/2)\mathcal C_Q=0.
\]

At `t=log n`, the jump is

\[
{1\over\sqrt n}
\left[
 n-\left\lfloor{n\over Q}\right\rfloor
 -(n-1)+\left\lfloor{n-1\over Q}\right\rfloor
\right]
={a_Q(n)\over\sqrt n}.
\]

Hence, in distributions,

\[
\boxed{
\left(\partial_t+{1\over2}\right)\mathcal C_Q
=\sum_{n\ge1}{a_Q(n)\over\sqrt n}\delta_{\log n}.}
\tag{L-25802.6}
\]

## 3. Exact transform

Put

\[
s=z+\frac12.
\]

For `Re s>1`, integration by parts against the atomic derivative gives

\[
\boxed{
\widehat{\mathcal C_Q}(z)
=\int_0^\infty \mathcal C_Q(t)e^{-zt}dt
={1-Q^{-s}\over s}\zeta(s).}
\tag{L-25802.7}
\]

Equivalently, direct step summation gives

\[
\int_0^\infty
\left(
 N(t)-\left\lfloor{N(t)\over Q}\right\rfloor
\right)e^{-st}dt
={1\over s}
\sum_{n\ge1}{1-\mathbf1_{Q\mid n}\over n^s}.
\]

The multiplier has three structural features:

1. `zeta(s)` cancels one reciprocal-zeta factor;
2. `1-Q^-s` is a stable causal multiplicative difference;
3. `1/s` is the causal exponential primitive.

## 4. Dyadic relation

At `Q=2`,

\[
N-\lfloor N/2\rfloor
\]

is the number of odd integers at most `N`. Thus `C_2` is the cumulative
odd-count companion of the positive parity comb `P_2` on PR #236.

The two kernels expose different useful factorizations:

```text
parity comb P_2:
    transform eta(s)/s,
    exact three-tap interaction with the dyadic Möbius shell;

nonmultiple count C_2:
    transform (1-2^-s)zeta(s)/s,
    stable causal difference and exact top-source recovery.
```

The present proposal uses `C_Q` for recovery and keeps `P_2` as a mandatory
mutation and transport test.

## 5. Stable difference inverse

Let

\[
H_Q=(\varepsilon-\delta_Q)^{-1}
=\sum_{j\ge0}\delta_{Q^j}.
\tag{L-25802.8}
\]

The sum is pointwise finite on every finite coefficient range. In the
square-root normalized logarithmic coordinate its atomic kernel is

\[
H_Q^\#
=\sum_{j\ge0}Q^{-j/2}\delta_{j\log Q},
\]

so

\[
\boxed{
\|H_Q^\#\|_{\rm TV}
={1\over1-Q^{-1/2}}.}
\tag{L-25802.9}
\]

This is bounded uniformly as `Q` increases.

## 6. Proof boundary

Closed exactly:

- the arithmetic nonmultiple indicator;
- positivity of the physical kernel;
- the distributional derivative;
- the Mellin/Laplace transform;
- the stable causal difference inverse.

Not closed:

- coercive inversion of the zeta factor;
- a top-source transport estimate;
- `PADT(K)` or RH.
