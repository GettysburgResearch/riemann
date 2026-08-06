# O-21503 — Quartic totient criterion: exact finite packaging, classical Mertens frontier

Claim ID: `O-21503`  
Title: The quartic totient observable gives an exact finite RH coordinate but does not weaken the classical Mertens theorem required  
Status: `PROPOSED INTEGRATION/AUDIT OBSERVATION`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Source snapshot: current `main` through `cec3fa9b8ad7b474097fdd863ecf08a3e7a49b49`  
Dependencies: proposed `L-9508/T-9502`; `L-21501/T-21501`

## 1. Exact finite observable

Current main proposes

\[
\mathcal Q(x)
={1\over x}\sum_{1\le n<x}{\varphi(n)\over n}
\left(1-{n^2\over x^2}\right)^2,
\tag{O-21503.1}
\]

with

\[
\mathrm{RH}
\iff
\mathcal Q(x)-{16\over5\pi^2}
=O_\varepsilon(x^{-3/2+\varepsilon}).
\tag{O-21503.2}
\]

Its rational Mellin kernel

\[
{8\over z(z+2)(z+4)}
\tag{O-21503.3}
\]

has no zeros and therefore does not cancel any shifted nontrivial-zero pole `z=rho-1`. This is a particularly clean finite arithmetic coordinate of the rightmost-zero exponent.

## 2. Exact Bernoulli–Möbius decomposition

The quartic cell sum collapses to Bernoulli polynomials, yielding five explicit channels:

\[
\begin{aligned}
\mathcal Q(x)-{16\over5\pi^2}
={}&-{8\over15}\sum_{d\ge x}{\mu(d)\over d^2}
-{1\over2x}\sum_{d<x}{\mu(d)\over d}\\
&-{4\over3x^3}\sum_{d<x}\mu(d)d B_3(\{x/d\})\\
&+{1\over x^4}\sum_{d<x}\mu(d)d^2 B_4(\{x/d\})\\
&-{1\over5x^5}\sum_{d<x}\mu(d)d^3 B_5(\{x/d\}).
\end{aligned}
\tag{O-21503.4}
\]

Subject to review of the endpoint convention and piecewise partial summation, this is an exact and useful proof-facing identity.

## 3. What is genuinely gained

The quartic weight improves on the semicircle kernel operationally:

1. the finite sum is rational at rational `x`;
2. the Mellin kernel decays cubically and has no zero-cancellation issue;
3. the entire error is exposed as bounded periodic weights against the Möbius measure;
4. the RH implication follows directly from the classical Mertens estimate without a delicate contour bound.

This removes analytic clutter and creates an excellent exact checker target.

## 4. What is not gained

The proof of the RH-scale error assumes

\[
M(X)=\sum_{n\le X}\mu(n)
=O_\varepsilon(X^{1/2+\varepsilon}),
\tag{O-21503.5}
\]

which is itself a classical RH-equivalent statement. The exact five-channel decomposition does not prove new cancellation in `M(X)` or a weaker condition sufficient for all five channels.

Therefore `T-9502` is a clean equivalence and transfer theorem, not yet a positive advance over the classical Mertens frontier. The new research question is whether the coupled Bernoulli channels admit cancellation that is provable without controlling raw `M(X)` at square-root scale.

Demanding each channel separately satisfy the target may be strictly stronger than necessary, just as termwise absolute estimates lose cancellation in the Bessel–Möbius and terminal-prime routes.

## 5. Relation to the prime polygon

The quartic and polygon observables see the same rightmost-zero displacement through dual arithmetic measures:

```text
quartic totient:
  smoothed Möbius/Farey coordinate;

prime polygon:
  cumulative von-Mangoldt quantile coordinate.
```

A genuinely new bridge would express the polygon margin or its block increments as a positive average of the five centered Möbius channels, or conversely transfer a block prime-transport surplus into cancellation of the combined quartic error. No such positivity-preserving duality is proved here.

## 6. Status boundary

- The source theorem and decomposition remain `PROPOSED` pending independent review.
- The exact finite identity is meaningful progress in representation and verification.
- The RH-scale estimate remains the classical Mertens problem in coupled form.
- No RH proof or counterexample is claimed.
