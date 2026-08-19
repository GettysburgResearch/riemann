# L-99440 — Exact disposition of the three vulnerable interfaces

Claim ID: `L-99440`  
Status: **PROVED SYNTHESIS OF LIVE EXACT RESULTS**  
Created: 2026-08-20  
Depends on: PRs #647–#649 and `R-99440`  
RH status: **unproved**

## Vulnerability 1 — smaller-endpoint child source

A child at endpoint \(Z\le Y\) is not the raw support restriction of the parent
SHARP row measure. The exact Radon–Nikodym derivative is

\[
\boxed{
R_{Z\mid Y}(t)
=
\mathbf1_{t\le Z}\frac{T(Z/t)}{T(Y/t)},
\qquad T(y)=4\sqrt y-3.
}
\]

It lies in \([0,1]\), satisfies the cocycle law, and gives literal disjoint
random-key child cylinders. This vulnerability is repaired exactly.

## Vulnerability 2 — causal parent versus Möbius Euler row

The positive causal identity reconstructs the positive parent:

\[
P^{\rm cur}+\alpha P_p=P.
\]

The Möbius Euler update is

\[
P-rP_p.
\]

Their discrepancy is the macroscopic half-order subsidy in `R-99440`. It cannot
be hidden in a bounded or holomorphic calibration. The full-row positivity
interpretation of the causal tree is therefore withdrawn.

## Vulnerability 3 — zero-dependent fixed-row noncancellation

The earlier analytic consumer selected a sufficiently large row depending on a
hypothetical zero. PR #649 replaces that interface by the single fixed
combination

\[
W_X=5c_X(2)+3c_X(3).
\]

Its canonical coefficients are positive:

\[
15h_2+6h_3+3h_4+6\sum_{m\ge5}h_m,
\]

and its reciprocal-zeta numerator factors as

\[
\boxed{
5P_2(z)+3P_3(z)
=
-3(2^{-z}-1)(2^{-z}-2).
}
\]

Neither factor vanishes in \(0<\Re z<1\). This vulnerability is repaired
exactly.

## Final disposition

```text
RN child ownership                         CLOSED
fixed analytic witness                     CLOSED
positive causal tree = Möbius Euler row    FALSE
bounded-defect/coboundary repair            IMPOSSIBLE FOR THE SUBSIDY
integrated 5:3 Harnack sign IHR67           OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVEN
```
