# TP2 endpoint order-inversion continuation

## Motivation

The Boolean/equal-pair normal form `T-102990` removes the owner-gauge choice, but the radial/Plücker coordinate remains useful because it exposes a signed endpoint current. The missing analytic question was whether the common-mother kernel itself could create an adverse endpoint sign.

It cannot.

## Exact results

The positive ratio-four half-kernel has the explicit logarithmic spline

\[
a(u)=
\begin{cases}
2(e^{u/2}-1),&0<u<\log2,\\
2\sqrt2(1-e^{(u-2\log2)/2}),&\log2<u<2\log2.
\end{cases}
\]

It is strictly log-concave, so its translation kernel is `TP_2`.

The derivative companion `A_-=(D-1/2)A` has a strictly decreasing likelihood ratio `A_-/A`. Hence, for `n<m`,

\[
A_-(X/n)A(X/m)-A(X/n)A_-(X/m)\le0
\]

pointwise.

Every antisymmetric owner endpoint determinant expands coefficient-exactly as

\[
\sum_{n<m}
(\mu_n\nu_m-\mu_m\nu_n)
\mathcal W_{n,m}(X).
\]

Thus every order-concordant Plücker minor is one-sided. Only source minors whose sign disagrees with physical product order can be adverse.

The integrated endpoint kernel also has the exact finite log-ratio budget

\[
\int_0^{2\log2}\int|W_\delta(u)|\,du\,d\delta
=24\log2-16,
\]

and vanishes for source ratios at least four.

## Correct new route

```text
order-concordant endpoint current   pointwise closed;
order-inverting endpoint current    DORI103010, open;
```

On the concentrated-owner route,

```text
DORI103010
 -> COCURL102980
 -> OICP102960
 -> HMO102940
 -> RH.
```

The canonical equal-pair route `BCI102990` remains parallel and owner-gauge invariant.

## Boundary

A two-atom source mutation reverses the physical sign while leaving the same `TP_2` kernel. Therefore the kernel theorem does not prove the arithmetic inversion estimate.

```text
TP2 / Wronskian geometry       PROVED EXACT
order-concordant sector        POINTWISE ONE-SIDED
DORI103010                     OPEN / RH-BEARING
BCI102990                      OPEN / RH-BEARING
Riemann Hypothesis             UNPROVED
```