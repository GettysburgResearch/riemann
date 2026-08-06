# L-15437 — Universal small-shift boundary-layer limit

Claim ID: `L-15437`  
Title: As `s downarrow 0`, the regular density tends to one at fixed translation and to `e^{-lambda}` on the natural scale `lambda=st` in the vague measure topology  
Status: `PROPOSED — COMPLETE COMPACT/VAGUE LIMIT; MICROSCOPIC LATTICE SIGN OPEN`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: `L-15434`, `L-15436`; elementary zeta/gamma expansions and continuity of Laplace transforms of locally finite positive measures  
Scope: the singular boundary layer left open by fixed-shift eventual positivity  
Related counterexample candidates: none

## 1. Fixed-translation limit

For every fixed

\[
t>0,
\tag{L-15437.1}
\]

one has

\[
\boxed{
\lim_{s\downarrow0}Y_s(t)=1.}
\tag{L-15437.2}
\]

The convergence is locally uniform for

\[
t\in[\delta,T]
\tag{L-15437.3}
\]

whenever `0<delta<T<infinity`.

### Proof

For fixed `t`, only finitely many integers satisfy `log n<=t`.  Moreover,

\[
F_s(1)=1,
\tag{L-15437.4}
\]

while, for every fixed `n>1`,

\[
F_s(n)
=\prod_{p\mid n}(1-p^{-s})
\longrightarrow0.
\tag{L-15437.5}
\]

The incomplete-beta formula and

\[
\Gamma(s/2)^{-1}\sim{s\over2}
\tag{L-15437.6}
\]

give

\[
\boxed{n_s(r)\longrightarrow1}
\tag{L-15437.7}
\]

locally uniformly for `r` in compact subsets of `(0,infinity)`.  The newly
admitted endpoint atom causes no issue because `n_s(0)=0` for every `s`.
Finally,

\[
c_s={1\over\zeta(1+s)}\sim s,
\tag{L-15437.8}
\]

and `I_s(t)` remains bounded on compact `t`-intervals.  Substitution in the
finite formula for `Y_s(t)` proves (L-15437.2).

Thus no counterexample can approach `s=0` while remaining in a bounded positive
translation interval.

## 2. Natural joint scaling

Put

\[
\lambda=st
\tag{L-15437.9}
\]

and define the rescaled signed density

\[
Z_s(\lambda)=Y_s(\lambda/s),
\qquad \lambda>0.
\tag{L-15437.10}
\]

Then

\[
\boxed{
Z_s(\lambda)d\lambda
\ \Longrightarrow_{m vague}\ 
 e^{-\lambda}d\lambda
\qquad(s\downarrow0).}
\tag{L-15437.11}
\]

Equivalently, for every continuous compactly supported function `phi` on
`(0,infinity)`,

\[
\boxed{
\lim_{s\downarrow0}
\int_0^\infty
 \phi(\lambda)Y_s(\lambda/s)d\lambda
=
\int_0^\infty
 \phi(\lambda)e^{-\lambda}d\lambda.}
\tag{L-15437.12}
\]

## 3. Laplace-transform proof of the boundary-layer law

For `r>0`, change variables `lambda=st`:

\[
\int_0^\infty e^{-r\lambda}Z_s(\lambda)d\lambda
=s\widehat Y_s(sr).
\tag{L-15437.13}
\]

The positive discrete component has transform

\[
\begin{aligned}
s\widehat M_s(sr)
&={1\over r}
 {\xi(1+sr)\over\xi(1+s(1+r))}\\
&\longrightarrow {1\over r},
\end{aligned}
\tag{L-15437.14}
\]

because `xi` is analytic and nonzero at `1`.

For the positive continuous comparator,

\[
\begin{aligned}
&s\,c_s\widehat I_s(sr)
={c_s\widehat n_s(sr)\over r}.
\end{aligned}
\tag{L-15437.15}
\]

Using `c_s~s` and the gamma formula for `widehat n_s`,

\[
\boxed{
c_s\widehat n_s(sr)
\longrightarrow {1\over1+r}.}
\tag{L-15437.16}
\]

Hence

\[
\boxed{
s\widehat Y_s(sr)
\longrightarrow
{1\over r}-{1\over r(1+r)}
={1\over1+r}.}
\tag{L-15437.17}
\]

The two terms in (L-15437.14)--(L-15437.15) are Laplace transforms of positive
locally finite measures.  After one fixed exponential tilt they are finite
measures, so the continuity theorem applies separately and permits subtraction.
Since `(1+r)^(-1)` is the Laplace transform of `e^{-lambda}`, this proves
(L-15437.11).

The positive components have the individual limits

\[
M_s(\lambda/s)d\lambda
\Longrightarrow d\lambda,
\tag{L-15437.18}
\]

\[
c_sI_s(\lambda/s)d\lambda
\Longrightarrow(1-e^{-\lambda})d\lambda.
\tag{L-15437.19}
\]

Their difference is the universal positive profile in (L-15437.11).

## 4. Exact remaining microscopic obstruction

The vague limit is positive, but it does not by itself prove pointwise
positivity.  In the boundary scaling, integer admission points occur at

\[
\lambda_N=s\log N,
\tag{L-15437.20}
\]

with spacing

\[
\lambda_{N+1}-\lambda_N
=s\log(1+1/N)
\sim{s\over N}.
\tag{L-15437.21}
\]

These cells become exponentially microscopic when

\[
N\asymp e^{\lambda/s}.
\]

A negative endpoint spike could therefore have vanishing mass and remain
invisible to vague convergence.  `L-15431` shows that every negative minimum
must occur at one of these endpoints; it does not supply a lower width for a
negative excursion because `n_s'(0+)` is singular.

Thus the entire unresolved global sign has been compressed into the following
sharp statement:

\[
\boxed{
Y_s(\log N)\ge0
\text{ uniformly in the microscopic regime }
 s\downarrow0,
 \quad N\asymp e^{\lambda/s}.}
\tag{L-15437.22}
\]

The macroscopic boundary-layer profile is already positive.

## 5. Consequence for a full-resolution proof

Combine:

1. `L-15436`: fixed-shift eventual positivity, uniform away from `s=0`;
2. (L-15437.2): positivity in the `s downarrow0` compact-translation limit;
3. (L-15437.11): the positive universal macroscopic boundary profile;
4. `L-15431`: every minimum lies at an integer deposition endpoint.

Any counterexample to the smoothed-Jordan theorem must be an arithmetic
**microscopic boundary-layer defect**, not a continuum, endpoint, large-height,
or fixed-shift phenomenon.

This provides a concrete full-resolution architecture:

```text
analytic estimates:
    remove every macroscopic region;

one directed arithmetic theorem/checker:
    exclude microscopic endpoint defects uniformly in
    s log N.
```

A sufficiently explicit uniform error term upgrading (L-15437.11) from vague to
pointwise convergence would finish the positive route and, through the existing
intertwiner chain, resolve RH.

## 6. Proof boundary

- The fixed-translation and Laplace-transform limits are exact.
- Vague convergence does not imply pointwise convergence for signed densities.
- No microscopic endpoint moat is proved.
- This lemma does not prove the smoothed-Jordan inequality or RH; it identifies
  the sole surviving double-scaling regime after the global asymptotic attack.
