# L-15434 — Completed-xi transform of the regular smoothed-Jordan tail

Claim ID: `L-15434`  
Title: The final beta-smoothed Jordan density is exactly the inverse Laplace transform of one completed-xi ratio defect, whose every positive exponential moment is unconditionally positive  
Status: `PROPOSED — COMPLETE TRANSFORM IDENTITY; COMPLETE MONOTONICITY OPEN`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: `L-15428`--`L-15431`; the standard completed-xi normalization  
Scope: the trace-zero regular tail left after the endpoint collapse of `L-15433`  
Related counterexample candidates: none

## 1. Beta-resolvent normalization

Fix

\[
0<s<1,
\tag{L-15434.1}
\]

so that `s=2 omega` in the notation of `L-15430`.  Put

\[
F_s(n)=\prod_{p\mid n}(1-p^{-s}),
\qquad
c_s={1\over\zeta(1+s)}.
\tag{L-15434.2}
\]

Let `n_s` be the positive beta-resolvent density

\[
n_s(t)
={\pi^{s/2}\over\Gamma(s/2)}
 e^{-st}
 B_{1-e^{-2t}}
 \left({s\over2},{3\over2}-{s\over2}\right),
\qquad t\ge0.
\tag{L-15434.3}
\]

Its Laplace transform is

\[
\boxed{
\widehat n_s(q)
=\pi^{s/2}
 {\Gamma((3+q)/2)
  \over
  (q+s)\Gamma((3+s+q)/2)},
\qquad q>0.}
\tag{L-15434.4}
\]

Define the discrete beta convolution

\[
M_s(t)
=\sum_{\log n\le t}
 {F_s(n)\over n}
 n_s(t-\log n)
\tag{L-15434.5}
\]

and the continuous Euler-product comparator

\[
I_s(t)=\int_0^t n_s(r)\,dr.
\tag{L-15434.6}
\]

The final regular density from `L-15430` is

\[
\boxed{Y_s(t)=M_s(t)-c_sI_s(t).}
\tag{L-15434.7}
\]

Thus `Y_s=m'_(s/2)` in the previous notation.

## 2. Exact completed-xi ratio

The Jordan Dirichlet series is

\[
\sum_{n\ge1}{F_s(n)\over n^{1+q}}
={\zeta(1+q)\over\zeta(1+s+q)}.
\tag{L-15434.8}
\]

Therefore convolution and Fubini give

\[
\widehat M_s(q)
=\widehat n_s(q)
 {\zeta(1+q)\over\zeta(1+s+q)}.
\tag{L-15434.9}
\]

Use the standard completed function

\[
\xi(z)
={1\over2}z(z-1)\pi^{-z/2}
 \Gamma(z/2)\zeta(z).
\tag{L-15434.10}
\]

The gamma recurrence gives the exact identity

\[
\boxed{
\widehat n_s(q)
 {\zeta(1+q)\over\zeta(1+s+q)}
={1\over q}
 {\xi(1+q)\over\xi(1+s+q)}.}
\tag{L-15434.11}
\]

Indeed,

\[
{\Gamma((3+q)/2)\over\Gamma((3+s+q)/2)}
={1+q\over1+s+q}
 {\Gamma((1+q)/2)\over\Gamma((1+s+q)/2)},
\]

which supplies exactly the polynomial factors in the completed-xi ratio.

Since

\[
\widehat I_s(q)={\widehat n_s(q)\over q},
\tag{L-15434.12}
\]

we obtain the main formula:

\[
\boxed{
\widehat Y_s(q)
={1\over q}\left[
 {\xi(1+q)\over\xi(1+s+q)}
 -c_s\widehat n_s(q)
 \right].}
\tag{L-15434.13}
\]

Equivalently,

\[
\boxed{
q\widehat Y_s(q)
={\xi(1+q)\over\xi(1+s+q)}
 -{1\over\zeta(1+s)}
  \pi^{s/2}
 {\Gamma((3+q)/2)
  \over(q+s)\Gamma((3+s+q)/2)}.}
\tag{L-15434.14}
\]

The final divisor inequality is therefore not an isolated lattice statement.
It is the physical-space inverse transform of one explicit completed-xi ratio
minus its exact Euler-product boundary channel.

## 3. Every positive exponential moment is unconditionally positive

A useful fact not visible in the pointwise formulation is

\[
\boxed{
\widehat Y_s(q)>0
\qquad(q>0,\ 0<s<1).}
\tag{L-15434.15}
\]

From (L-15434.9), (L-15434.12), and (L-15434.7),

\[
\widehat Y_s(q)
={\widehat n_s(q)\over q}
\left[
 q{\zeta(1+q)\over\zeta(1+s+q)}
 -{1\over\zeta(1+s)}
\right].
\tag{L-15434.16}
\]

The beta factor is positive.  Moreover, for `q>0`, monotone integral
comparison gives

\[
q\zeta(1+q)>1,
\tag{L-15434.17}
\]

while strict monotonicity of zeta on `(1,infinity)` gives

\[
\zeta(1+s)>\zeta(1+s+q).
\tag{L-15434.18}
\]

Hence

\[
q{\zeta(1+q)\over\zeta(1+s+q)}
>{1\over\zeta(1+s+q)}
>{1\over\zeta(1+s)},
\]

which proves (L-15434.15).

In physical space,

\[
\boxed{
\int_0^\infty e^{-qt}Y_s(t)\,dt>0
\qquad(q>0).}
\tag{L-15434.19}
\]

Thus any negative excursion of the regular density must be compensated at
**every** positive exponential scale.  A single scalar Laplace test, no matter
how its scale is chosen, can never detect the missing sign.

## 4. Exact RH-bearing formulation

By `L-15430` and Bernstein--Widder, the following are equivalent for a fixed
`0<s<1`:

1. `Y_s(t)>=0` for every `t>=0`;
2. `widehat Y_s` is completely monotone on `(0,infinity)`;
3. the Hankel kernel
   \[
   (z,w)\longmapsto
   \widehat Y_s\left({z+\bar w\over2}\right)
   \]
   is positive semidefinite.

Using (L-15434.13), the exact positive-route target is therefore

\[
\boxed{
q\longmapsto
{1\over q}\left[
 {\xi(1+q)\over\xi(1+s+q)}
 -{\widehat n_s(q)\over\zeta(1+s)}
\right]
\text{ is completely monotone}}
\tag{L-15434.20}
\]

for every `0<s<1`.

Equation (L-15434.15) proves only the zeroth complete-monotonicity inequality.
The missing theorem is the infinite derivative hierarchy

\[
(-1)^k{d^k\over dq^k}\widehat Y_s(q)\ge0
\qquad(k=1,2,\ldots).
\tag{L-15434.21}
\]

This makes the full-problem boundary explicit: the regular tail is a
completed-xi **total-positivity** problem, not a scalar positivity problem.

## 5. Relation to the original `K_0`/Loewner attack

`L-15433` routes the complete summed endpoint channel into one positive
rank-one trace.  On the trace-zero range, (L-15434.13) is the scalar Mellin
shadow of the remaining regular Volterra form.

Consequently there are two mathematically equivalent proof interfaces for the
same global attack:

```text
physical space:
    prove the trace-zero original Volterra/K0 form positive;

Mellin space:
    prove complete monotonicity of the completed-xi ratio defect
    in (L-15434.20).
```

The first interface preserves all noncommutative branch geometry.  The second
is a one-variable total-positivity target with every arithmetic and
gamma-factor constant explicit.

No finite Schur, selected-zero, or compactness adapter remains between these
two statements.  What remains is the actual global sign.

## 6. Proof boundary

- The transform identities are exact for `q>0`, where every series and integral
  converges absolutely.
- The strict positivity (L-15434.15) is unconditional and elementary.
- Positive Laplace transforms do not imply positive inverse transforms.
- Complete monotonicity (L-15434.20) is not proved here and is the RH-bearing
  step.
- This lemma supplies a new completed-xi formulation and a zeroth-order positive
  theorem; it does not prove `Y_s>=0`, `K_0>=0`, or RH.
