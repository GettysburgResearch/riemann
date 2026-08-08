# T-21705 — Nörlund half-plane stability would prove RH directly

Claim ID: `T-21705`  
Title: A zero-free right half-plane for the one-sided Brownian–Nörlund Dirichlet splines implies the Riemann Hypothesis by Hurwitz  
Status: **FULL GLOBAL PROPOSAL — ONE FINITE HALF-PLANE STABILITY THEOREM OPEN**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-21706`, `L-21707`; Hurwitz or Rouché theorem; Bernstein's theorem for the stronger sufficient form  
RH status: **UNPROVED**

## 1. The one-sided finite functions

Retain

\[
\overline m_N(s)
=\pi^{-s/2}\Gamma(1+s/2)\overline D_N(s)
\tag{T-21705.1}
\]

from `L-21706`, where `overline D_N` is the explicit finite exponential polynomial

\[
\overline D_N(s)
=\sum_{n=1}^N(\alpha_{N,n}+s\beta_{N,n})n^{-s}.
\tag{T-21705.2}
\]

`L-21707` gives the exact derivative-sampling form

\[
\overline D_N(s)
=-\sum_{n\ge1}
 \left.\frac{d}{dx}
 \left[x^{1-s}B_N(x)\right]\right|_{x=n}
\tag{T-21705.3}
\]

for one nonnegative positive-definite cardinal kernel `B_N`.

## 2. Preferred finite theorem — NHS

> **NHS — Nörlund Half-plane Stability.** There is an unbounded sequence
> `N_j`—more strongly, every `N`—such that
> \[
> \boxed{
> \overline D_{N_j}(s)\ne0
> \qquad\left(\operatorname{Re}s>\frac12\right).}
> \tag{NHS}
> \]

This is a finite exponential-polynomial stability theorem. It does not mention
zeta zeros, primes, a limiting operator, or an asymptotic prime estimate.

## 3. NHS implies RH

By `L-21706`, locally uniformly in the open critical strip,

\[
\overline m_N(s)\longrightarrow2\xi(s).
\]

The gamma factor in (T-21705.1) is nonzero there, and therefore

\[
\boxed{
\overline D_N(s)
\longrightarrow2(s-1)\zeta(s)}
\tag{T-21705.4}
\]

locally uniformly.

Suppose that `rho` is a nontrivial zeta zero with

\[
\operatorname{Re}\rho>\frac12.
\]

Choose a closed disk around `rho`, contained in the open critical strip and in
the right half-plane `Re(s)>1/2`, whose boundary contains no zeta zero. Equation
(T-21705.4) and Rouché's theorem force `overline D_(N_j)` to have the same
positive number of zeros in that disk for every sufficiently large `j`. This
contradicts NHS.

Hence zeta has no zero to the right of the critical line. Functional-equation
symmetry gives

\[
\boxed{\mathrm{NHS}\Longrightarrow\mathrm{RH}.}
\tag{T-21705.5}
\]

This argument is shorter than the symmetrized `BLNRZ` consumer: the one-sided
finite function already converges to the zeta factor carrying every off-line
zero.

## 4. Stronger real-axis sufficient theorem — RCM

A proof-facing sufficient theorem is:

> **RCM — Reciprocal Complete Monotonicity.** For the same unbounded sequence,
> \[
> \boxed{
> x\longmapsto
> \frac{\overline D_N(1/2)}
>      {\overline D_N(1/2+x)}
> \text{ is completely monotone on }[0,\infty).}
> \tag{RCM}
> \]

Bernstein's theorem then supplies a probability measure `nu_N` on `[0,infinity)`
such that

\[
\frac{\overline D_N(1/2)}
     {\overline D_N(1/2+x)}
=\int_0^\infty e^{-xt}\,d\nu_N(t)
\qquad(x\ge0).
\tag{T-21705.6}
\]

The right side has a holomorphic extension to `Re(z)>0`. By uniqueness of
analytic continuation, it equals

\[
\frac{\overline D_N(1/2)}
     {\overline D_N(1/2+z)}
\tag{T-21705.7}
\]

wherever the latter is initially defined. A zero of the denominator in the
right half-plane would create a genuine pole, while the Laplace transform in
(T-21705.6) is holomorphic there. Thus no such zero exists and

\[
\boxed{\mathrm{RCM}\Longrightarrow\mathrm{NHS}.}
\tag{T-21705.8}
\]

RCM also gives the boundary minimum-modulus inequality

\[
\boxed{
|\overline D_N(1/2+it)|
\ge\overline D_N(1/2)
\qquad(t\in\mathbb R).}
\tag{T-21705.9}
\]

## 5. Why this is a genuine new attack

The finite objects in NHS/RCM are built from:

```text
finite gamma convolutions with rates 1^2,...,N^2;
positive logarithmic cutoff weights 1/(K H_N);
binomial-cardinal squares R_K(x)^2;
integer derivative samples;
a finite exponential polynomial.
```

A production proof may use finite delay-system stability, total positivity,
canonical systems, an inverse-Laplace renewal, or a direct Hermite–Biehler
factorization. It need not prove WSTS, Mertens cancellation, balanced Type II,
or a Weil-form inequality first.

The theorem remains RH-bearing. In particular, finite derivative checks or
finite-height winding counts cannot be promoted to RCM/NHS.

## 6. Relationship to BLNRZ

The original PR #296 target `BLNRZ` asks that the symmetrized approximants

\[
\mathcal X_N(s)
=\overline m_N(s)+\overline m_N(1-s)
\]

have only critical-line zeros. NHS is a different and more direct sufficient
theorem. It proves RH without first proving a finite real-zero theorem for the
symmetrization.

A future Hermite–Biehler proof may still combine NHS with a suitable exponential
gauge to recover BLNRZ, but that extra step is not a dependency of
(T-21705.5).

## 7. Automatic rejection conditions

Reject a claimed NHS/RCM proof if it:

1. verifies only finitely many derivatives or heights;
2. assumes the limiting zero-free half-plane of zeta;
3. replaces the logarithmic weights by Cesàro weights;
4. ignores the derivative term in (T-21705.3);
5. proves zero-freeness only for `Re(s)>1`;
6. derives a Laplace representation with signed mass;
7. uses the raw cutoff producer, which has a right-half-plane mutation;
8. assumes complete monotonicity from log-convexity alone.

## 8. Exact status

```text
finite cardinal/derivative algebra          PROPOSED COMPLETE + exact replay
local uniform limit to 2(s-1)zeta(s)        PROPOSED COMPLETE
RCM -> NHS                                  COMPLETE CONDITIONAL
NHS -> RH                                   COMPLETE CONDITIONAL
reciprocal complete monotonicity             OPEN / RH-BEARING
Norlund half-plane stability                 OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVED
```
