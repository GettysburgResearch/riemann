# T-23705 — Centered digital Hardy proof candidate

Claim ID: `T-23705`  
Title: A uniform centered Hardy bound for the fifth-aligned cumulative carry shell proves the Riemann Hypothesis  
Status: **FULL CONDITIONAL PROPOSAL — ONE SOURCE-SPECIFIC UNIFORM HARDY BOUND OPEN**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Dependencies: `L-23709`, `L-23715`, `L-23716`; reflected Selberg algebra and scope repair on PR #241  
Scope: corrected front door after `R-23706/R-23707`

## 1. Explicit arithmetic state

Let

\[
C(y)=
\sum_{n\le y}
\frac{
\mu(n)-\mathbf1_{5\mid n}\mu(n/5)
}{\sqrt n}
\left(4\sqrt{y/n}-4-\log(y/n)\right).
\tag{T-23705.1}
\]

Its Mellin transform is

\[
\boxed{
\widehat C(z)
=
\frac{(1-5^{-(z+1/2)})(z+1/2)}
 {z^2(z-1/2)\zeta(z+1/2)}.
}
\tag{T-23705.2}
\]

Put

\[
s=z+\frac12,
\qquad
h(z)=\frac{s(1-5^{-s})}{(s-1)\zeta(s)},
\]

so that

\[
\widehat C(z)=\frac{h(z)}{z^2}.
\tag{T-23705.3}
\]

The explicit positive linear coefficient is

\[
\boxed{
a_5=h(0)
=-\frac{1-5^{-1/2}}{\zeta(1/2)}>0.
}
\tag{T-23705.4}
\]

## 2. Corrected centered state and energy

Define

\[
Z(y)=C(y)-a_5\log y,
\qquad
\mathcal Z(t)=Z(e^t),
\]

and

\[
\boxed{
V(t)=\mathcal Z'(t)+\frac12\mathcal Z(t).
}
\tag{T-23705.5}

Its exact Hardy multiplier is

\[
\boxed{
\widehat V(z)
=
\frac{(z+1/2)(h(z)-h(0))}{z^2}.
}
\tag{T-23705.6}

The zero-frequency double pole has been removed. The remaining simple pole at zero is permitted and corresponds to a constant physical mode. Critical-line zeta zeros give boundary poles with finite Hardy mass; off-line zeros give interior poles.

## 3. Sole proposed theorem: `CDHB(5)`

> **Centered Digital Hardy Bound at base five.** There are absolute constants `sigma_0,C>0` such that
> \[
> \boxed{
> \sup_{0<\sigma\le\sigma_0}
> \sigma
> \int_{-\infty}^{\infty}
> \left|
> \frac{(z+1/2)(h(z)-h(0))}{z^2}
> \right|^2d\tau
> \le C,
> \qquad z=\sigma+i\tau.
> }
> \tag{T-23705.7}

Equivalently, by Laplace Plancherel and Abel--Cesaro,

\[
\boxed{
\int_0^T|V(t)|^2dt=O(T).
}
\tag{T-23705.8}

This is the exact viable energy scale. The stronger uncentered and centered little-`o` conditions are refuted by `R-23706` and `R-23707`.

## 4. Digital descent

`L-23715` proves that the centered base-five forcing is bounded. `L-23716` then gives the exact recurrence

\[
Z(y)
\ge
2^{-1/2}Z(y/2)
-\kappa_5\sqrt{\mathcal E_{5,c}(y)}
-O(1),
\tag{T-23705.9}
\]

where

\[
\mathcal E_{5,c}(y)
=
\sum_{m=2}^{\lfloor y\rfloor-1}
 m^2
\left|
 m^{-1/2}Z(y/m)
 -(m+1)^{-1/2}Z(y/(m+1))
\right|^2.
\]

The continuous energy dominates this discrete one:

\[
\mathcal E_{5,c}(e^T)
\le
\int_0^{T-\log2}|V(t)|^2dt.
\tag{T-23705.10}
\]

Thus CDHB(5) implies

\[
\mathcal E_{5,c}(y)=O(1+\log y).
\]

Iterating (T-23705.9) gives

\[
\boxed{
Z(y)\ge-O(\sqrt{\log y}).
}
\tag{T-23705.11}

Consequently

\[
\boxed{
C(y)
\ge
a_5\log y-O(\sqrt{\log y})>0
}
\tag{T-23705.12}

for every sufficiently large `y`.

## 5. Landau completion

Eventual positivity of the nonzero function `C` is enough for Landau's one-sign theorem: subtracting a compact initial segment changes its Mellin transform by an entire function.

The explicit transform (T-23705.2) is regular at every positive real `z`; the apparent point `z=1/2` is removable against the pole of `zeta(1)`. Therefore its convergence abscissa is at most zero and the transform is holomorphic in `Re z>0`.

Every zeta zero `rho` with `Re rho>1/2` would give an uncancelled pole at

\[
z=\rho-\frac12,
\]

contradiction. Functional-equation symmetry yields

\[
\boxed{\mathrm{RH}.}
\tag{T-23705.13}

## 6. Exact reflected-Selberg interface

Write

\[
B_5(s)=\frac{1-5^{-s}}{\zeta(s)},
\qquad
A_5(s)=B_5(s)^{-1}=\frac{\zeta(s)}{1-5^{-s}}.
\]

The inverse coefficients are

\[
a_5(n)=v_5(n)+1\ge1,
\]

and the generalized prime weights are

\[
\Lambda_5^\#(n)
=
\Lambda(n)+(\log5)\mathbf1_{n=5^k}\ge0.
\]

The generalized Selberg coefficient identity and its two-frequency reflected form therefore apply with coefficientwise positive forcing. Multiplying the reflected logarithmic-derivative square by `|B_5|^2` gives the positive derivative energy `|B_5'|^2`.

The remaining proof obligation is precise:

```text
positive reflected derivative reserve for B_5
+ rational factor s/(s-1)
+ exact anchor h(0)
+ Hardy/Poincare control of the difference quotient
=> CDHB(5) with one finite uniform constant.
```

A derivation returning the complete left energy to the forcing side is only the tautology `2E=2E`. A proof must exhibit a strict reserve and retain the full fifth-aligned source.

## 7. Why this is reviewable

The proposal now has exactly one open inequality, (T-23705.7). Every other object is explicit:

- a finite Möbius formula for `C`;
- its Mellin multiplier;
- the exact principal-part subtraction;
- the bounded centered digital forcing;
- the centered discrete and continuous energies;
- the base-five endpoint ledger;
- the conditional Landau deduction.

The exact annulus `X-23704` remains a normalization regression, not a substitute for CDHB(5).

## 8. Rejection tests

Reject the proposal upon any of:

1. a wrong principal-part coefficient `a_5`;
2. failure of the bounded centered-forcing calculation;
3. a missing digital endpoint;
4. an incorrect continuous-to-discrete energy orientation;
5. a one-frequency physical-block substitution;
6. a Hardy bound containing the same target energy on its right side;
7. loss of the fifth Euler-aligned source;
8. a finite computation promoted to CDHB(5);
9. reuse of either refuted little-`o` condition.

## 9. Exact status

```text
cumulative shell and Mellin transform          PROPOSED EXACT
principal-part extraction                      PROPOSED EXACT
bounded centered digital forcing               PROPOSED COMPLETE
centered energy descent                         PROPOSED COMPLETE CONDITIONAL
CDHB(5)                                         OPEN / RH-BEARING
CDHB(5) -> eventual positivity -> RH             PROPOSED COMPLETE
Riemann Hypothesis                              UNPROVED
```
