# T-103010 — TP2 endpoint order-inversion frontier

Claim ID: `T-103010`  
Status: **MAJOR UNCONDITIONAL KERNEL-SIDE CLOSURE; RH UNPROVED**  
Created: 2026-08-25  
Depends on: `L-103000--L-103003`; `R-103000`; `T-102980--T-102990`; PR #730 `T-105440--T-105450`  
RH status: **unproved**

The common-mother and Boolean-incidence programmes now have an exact order-theoretic interface.

## 1. Complete kernel geometry

`L-103000` proves that the positive ratio-four half-kernel `A` is strictly log-concave in logarithmic scale and that its translation kernel is `TP_2`.

`L-103001` proves that the signed companion

\[
A_-=(D-\tfrac12)A
\]

has the pointwise Wronskian sign

\[
 n<m
 \quad\Longrightarrow\quad
 A_-(X/n)A(X/m)-A(X/n)A_-(X/m)\le0.
\]

Thus the analytic endpoint kernel is fully oriented before arithmetic coefficients are inserted.

## 2. Exact Plücker transport

For two literal endpoint source measures `mu,nu`, `L-103003` gives

\[
F_\mu^-F_\nu^+-F_\mu^+F_\nu^-
=
\sum_{n<m}
(\mu_n\nu_m-\mu_m\nu_n)
\mathcal W_{n,m}.
\]

The coefficient is the exact source Plücker minor. This is precisely the two-coordinate endpoint determinant underlying:

```text
the radial actual-owner differences;
the minimum/equal-pair Hodge change;
the four-label Pluecker rectangles;
the augmentation local-system trace.
```

No physical norm or Cauchy inequality is used in this identification.

## 3. Order-concordant sector is closed pointwise

Split every source minor by the sign of

\[
(\mu_n\nu_m-\mu_m\nu_n)(m-n).
\]

The order-concordant projection is the part whose sign agrees with one declared monotone-likelihood order of the two source measures. By `L-103002`, this complete projection has a fixed physical sign at every scale.

Consequently its adverse logarithmic mass is exactly zero. It may be removed before any negative part is taken.

## 4. Exact remaining theorem

Define

```text
DORI103010:
  after the frozen carrier, Boolean-Vaughan, common-core, owner/core-renewal,
  endpoint-color and finite-boundary recombinations, the order-inverting
  Pluecker minors in the complete minimum-owner radial endpoint current have
  subpower logarithmic negative mass in the fixed derivative/outer
  observation.
```

Equivalently, `DORI103010` controls precisely those literal source pairs for which the sign of the endpoint Plücker minor disagrees with the order of their physical products.

All order-concordant endpoint pairs are already closed by the kernel theorem.

## 5. Implication graph

On the concentrated-owner route,

\[
\boxed{
\mathrm{DORI}_{103010}
\Longrightarrow
\mathrm{COCURL}_{102980}
\Longrightarrow
\mathrm{OICP}_{102960}
\Longrightarrow
\mathrm{HMO}_{102940}
\Longrightarrow
\mathrm{RH}.
}
\]

The canonical equal-pair theorem `BCI102990` remains a parallel, owner-gauge-invariant route. `DORI103010` does not replace it; it proves that the alternative radial/Plücker route has no kernel-side sign obstruction outside the explicit order-inversion sector.

## 6. Exact boundary

```text
explicit common two-box spline                 PROVED EXACT
log-concavity / TP2                            PROVED EXACT
derivative-companion Wronskian sign            PROVED EXACT
source Pluecker -> physical Wronskian           PROVED EXACT
order-concordant endpoint current               POINTWISE ONE-SIDED
order-inverting current DORI103010              OPEN / RH-BEARING
BCI102990                                       OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```

`R-103000` is binding: a signed source may reverse the kernel sign. A full proof still requires genuine arithmetic control of the order-inverting source minors.