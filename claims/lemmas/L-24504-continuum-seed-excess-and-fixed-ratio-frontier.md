# L-24504 — Continuum seed excess and a fixed-ratio frontier

Claim ID: `L-24504`  
Status: `PROPOSED — asymptotic reduction with explicit limiting profile`  
Scope: elementary analysis of the parabolic seed  
Issue: #245

Let

\[
b_X^{(0)}(m)=\sqrt X\,B(m/X),
\]

where

\[
B(t)=2\sqrt t\left[\log(1/t)-2(1-\sqrt t)\right].
\]

Then

\[
\boxed{B'(t)=\frac{4\sqrt t-\log t-4}{\sqrt t}.}
\tag{L-24504.1}
\]

For a fixed ratio `0<theta<1` and a sequence of prime powers `q=q_X` with `q/X->theta`, the divisor-gradient of the seed is

\[
v_q(b_X^{(0)})=\sum_{kq\le X}(b_X^{(0)}(kq)-b_X^{(0)}(kq+1)).
\]

A one-step Taylor expansion on each fixed `k` gives

\[
\sqrt X\,v_q(b_X^{(0)})
\longrightarrow
-\sum_{1\le k\le1/\theta}B'(k\theta).
\tag{L-24504.2}
\]

Meanwhile

\[
\sqrt X\,w_X(q)
\longrightarrow
\theta^{-1/2}\log(1/\theta).
\tag{L-24504.3}
\]

Hence the scaled constraint excess converges to the explicit finite-sum profile

\[
\boxed{
E(\theta)=
-\sum_{1\le k\le1/\theta}
\frac{4\sqrt{k\theta}-\log(k\theta)-4}{\sqrt{k\theta}}
-\theta^{-1/2}\log(1/\theta).
}
\tag{L-24504.4}
\]

The only discontinuities of this profile occur at reciprocal integers, because the number of terms changes there.

## Proposed fixed-ratio sign theorem

Numerical reconnaissance suggests that the final positive interval ends at one root

\[
\theta_*\approx0.0348520333855.
\]

The proof-facing theorem is:

\[
\boxed{E(\theta)<0\qquad(\theta_*<\theta<1),}
\tag{L-24504.5}
\]

with a rigorous rational upper enclosure `theta_*<7/200=0.035` sufficient for the application.

A uniform Taylor remainder would then imply that, for all sufficiently large `X`, every prime power

\[
q\ge X/28
\]

is already feasible for the uncorrected parabolic seed. Thus all initial positive excess lies in the fixed low-ratio range `q<X/28`.

## Why this helps PNC

A fixed low-ratio source has a large multiplicative reserve: every repair coordinate attached to `d<X/28` has many multiples inside a taper supported away from the endpoints. The primitive determinant-one leakage from such a source into an outer constraint `q` is then governed by a mean-zero periodic row and can be suppressed to high order before any balanced `qd\asymp X` interaction is reached.

This decomposes the proposed contraction into two stages:

1. prove the seed is feasible on the entire fixed outer ratio `q>=X/28`;
2. repair only `q<X/28`, using high-order divisor-comb cancellation to keep the repaired outer region feasible.

## Status boundary

The limiting profile formula is proposed elementary asymptotics. The uniform sign theorem (L-24504.5) and a proof-grade rational location of the last sign change are open and should be checked independently. The decimal value above is floating-point reconnaissance only.
