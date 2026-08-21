# L-91024 — The normalized Cauchy gate is a completely monotone positive heat-band transform

Claim ID: `L-91024`  
Status: **PROPOSED COMPLETE EXACT HEAT/RESOLVENT THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91022`; the critical-line zero expansion of the Cauchy gate  
RH status: **unproved**

## 1. Squared-scale normalization

Put

\[
 t=a^2
\]

and, for one real critical-line displacement `u`, define

\[
 \boxed{
 F_u(t)
 ={1\over t^2}\left[n_{2\sqrt t}(u)-n_{\sqrt t}(u)\right].
 }
 \tag{L-91024.1}
\]

Using `n_a(u)=a^4/(a^2+u^2)^2`, one obtains the elementary normal form

\[
 \boxed{
 F_u(t)
 ={1\over(t+u^2/4)^2}-{1\over(t+u^2)^2}.
 }
 \tag{L-91024.2}
\]

This is nonnegative for every `t>0` and real `u`.

## 2. Complete monotonicity

For every integer `m>=0`,

\[
 \boxed{
 (-1)^m\partial_t^mF_u(t)
 =(m+1)!\left[
 {1\over(t+u^2/4)^{m+2}}
 -{1\over(t+u^2)^{m+2}}
 \right]\ge0.
 }
 \tag{L-91024.3}
\]

Thus each critical-line atom is a completely monotone function of squared
scale.

## 3. Positive Laplace heat band

The exact Laplace representation is

\[
 \boxed{
 F_u(t)
 =\int_0^\infty
  q e^{-tq}
  \left(e^{-qu^2/4}-e^{-qu^2}\right)dq.
 }
 \tag{L-91024.4}
\]

The density is pointwise nonnegative.  It compares one Gaussian zero heat at
time `q/4` with the same heat at time `q`.

Equivalently,

\[
 F_u(t)
 =-\partial_t\left[
 {1\over t+u^2/4}-{1\over t+u^2}
 \right].
 \tag{L-91024.5}
\]

## 4. Completed zeta gate under RH

Let

\[
 \mathcal F_x(t)
 =\mathcal E_x(\sqrt t)
 =t^{-2}\left[
  \mathcal N_x(2\sqrt t)-\mathcal N_x(\sqrt t)
 \right].
 \tag{L-91024.6}
\]

Under RH, summing (L-91024.2) over critical-line zeros gives

\[
 \boxed{
 \mathcal F_x(t)
 =\sum_\gamma m_\gamma
  \left[
  {1\over(t+(\gamma-x)^2/4)^2}
  -{1\over(t+(\gamma-x)^2)^2}
  \right].
 }
 \tag{L-91024.7}
\]

The sum and all positive derivatives converge locally uniformly for `t>0`.
Consequently

\[
 \boxed{
 (-1)^m\partial_t^m\mathcal F_x(t)\ge0
 \quad(m\ge0).
 }
 \tag{L-91024.8}
\]

Thus `F_x` is completely monotone.

## 5. Zero-heat representation

Define the unnormalised critical-line zero heat

\[
 Z_x(q)=\sum_\gamma m_\gamma e^{-q(\gamma-x)^2}.
 \tag{L-91024.9}
\]

Then under RH

\[
 \boxed{
 \mathcal F_x(t)
 =\int_0^\infty
 q e^{-tq}\left[Z_x(q/4)-Z_x(q)\right]dq.
 }
 \tag{L-91024.10}
\]

Every bracket is nonnegative term by term.  The transform chain is therefore

```text
positive Gaussian heat band
 -> Laplace transform in squared scale
 -> normalized Cauchy gate
 -> sixteenfold dyadic recurrence.
```

## 6. The dyadic storage law is one sample of the semigroup

Since a completely monotone function is decreasing,

\[
 \mathcal F_x(t)\ge\mathcal F_x(4t).
 \tag{L-91024.11}
\]

This is exactly

\[
 \mathcal E_x(a)\ge\mathcal E_x(2a),
\]

the coefficient-one recurrence of `T-91005`.

At the single-atom level,

\[
 F_u(t)-F_u(4t)
 =a^{-4}\left[d_a(u)-{1\over16}d_{2a}(u)\right]
 \tag{L-91024.12}
\]

with `t=a^2`; `L-91022` gives its three-square rational factorisation.

## 7. False-RH singularity

For a reflected pair at its matching ordinate, replace `u` by the real depth
`y`.  The pair contribution contains

\[
 -{2m\over(t-y^2)^2},
 \tag{L-91024.13}
\]

plus terms regular at `t=y^2`.  Hence it tends to `-infinity` as `t` approaches
`y^2` from above.  No positive completely monotone representation can survive.

Therefore positivity of `F_x(t)` for all `x,t` is the original Cauchy gate and
is RH-equivalent; complete monotonicity is an equivalent strengthening under
RH.

## 8. Source-side significance

Equation (L-91024.10) replaces an infinite order-by-order scale calculation by
one positive heat band.  A prime-side proof may therefore target either:

```text
complete monotonicity in squared scale;
positivity of the Gaussian heat-band density after completed recombination;
or the three-square dyadic residual of L-91022.
```

The representations are exact transforms of one another.

## 9. Boundary

Closed:

```text
continuous squared-scale normalization;
all-order complete monotonicity under RH;
explicit positive heat-band Laplace density;
continuous semigroup origin of the factor 16;
false-RH negative double-pole obstruction.
```

Open:

```text
unconditional prime-side heat-band positivity;
source-complete semigroup realization;
RH.
```
