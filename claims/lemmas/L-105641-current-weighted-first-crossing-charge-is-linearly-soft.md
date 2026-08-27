# L-105641 — The current-weighted first-crossing charge is linearly soft

Claim ID: `L-105641`  
Status: **PROVED EXACT SOURCE-CHARGE BOUND**  
Created: 2026-08-25  
Depends on: `L-105620--L-105640`  
RH status: **not assumed**

## 1. The actual base-Xi profile

For base `b>=0`, microscope scale `h>0`, and total analytic height

\[
H=b+h,
\]

the current-normalized first-chaos profile is

\[
r_{b,h}(\xi)
={h e^{-H\xi}\Lambda_2(\xi)\over j_H(\xi)},
\qquad \xi\ge0.
\tag{L-105641.1}
\]

The positive current hierarchy gives

\[
j_H(\xi)\ge H\Lambda_2(\xi).
\]

Hence

\[
\boxed{
0\le r_{b,h}(\xi)
\le {h\over H}e^{-H\xi}.
}
\tag{L-105641.2}
\]

This estimate is source-exact and does not use a zero-free hypothesis.

## 2. Charge of one crossed derivative zero

Let a simple anti-inner factor have depth

\[
\delta=\operatorname{Im}\rho-H>0
\]

below the moving boundary.  Its normalized Paley–Wiener model vector is

\[
\phi_{\rho,H}(\xi)
=\sqrt{2\delta}
 e^{-\delta\xi}e^{-i(\operatorname{Re}\rho)\xi}.
\]

The actual current-weighted charge is

\[
\mathfrak q_{b,h}(\rho)
=\langle M_{r_{b,h}}\phi_{\rho,H},
               \phi_{\rho,H}\rangle
=2\delta\int_0^\infty
 r_{b,h}(\xi)e^{-2\delta\xi}\,d\xi.
\tag{L-105641.3}
\]

Using (L-105641.2),

\[
\boxed{
\mathfrak q_{b,h}(\rho)
\le
{2h\delta\over H(H+2\delta)}
\le
{2h\delta\over H^2}.
}
\tag{L-105641.4}
\]

Thus a derivative zero which has crossed only depth `delta` carries only
`O(delta)` of the current-weighted source energy.

## 3. Exact boundary derivative

For any integrable nonnegative source profile `r`, put

\[
q_r(\delta)
=2\delta\int_0^\infty r(\xi)e^{-2\delta\xi}\,d\xi.
\]

Dominated convergence gives

\[
\boxed{
q_r(\delta)
=2\delta\int_0^\infty r(\xi)\,d\xi
+o(\delta)
\qquad(\delta\downarrow0).
}
\tag{L-105641.5}
\]

The static weighted charge vanishes at the boundary, while its transverse
flux has the finite value

\[
\boxed{
q_r'(0+)=2\int_0^\infty r(\xi)\,d\xi.
}
\tag{L-105641.6}
\]

This is the weighted form of the rank-one kernel derivative in `L-105640`.

## 4. The missing unit escapes to high source frequency

The unweighted model vector always has norm one, but for every fixed finite
band `L`,

\[
\int_0^L|\phi_{\rho,H}(\xi)|^2d\xi
=1-e^{-2\delta L}
\longrightarrow0
\qquad(\delta\downarrow0).
\tag{L-105641.7}
\]

Thus the topological unit does not disappear.  It escapes to frequencies of
order `1/delta`, where the exponentially decaying current weight assigns
vanishing mass.  This is the exact frequency-space realization of the
zero-height/spatial-escape alternative of `T-105446`.

## 5. Consequence for proof architecture

No fixed-band, fixed-weight energy inequality can prevent the first
anti-inner crossing by a uniform positive gap.  A valid descent must retain at
least one of:

```text
an adaptive bandwidth L comparable with 1/delta;
the signed endpoint/model-space index complementary to the source band;
the transverse spectral-flow derivative before delta is set to zero;
a pointwise Clark/zero-height charge.
```

This is not a no-go for the combined programme.  It proves why the pointwise,
source-energy and endpoint-index components must be recombined before taking
the boundary limit.

## 6. Scope

The lemma does not prove that a crossing occurs and does not estimate a
multiple nonorthogonal divisor.  It supplies the exact simple-factor charge and
a universal Xi upper bound.  Confluent clusters use the Laguerre model-space
formulas of `L-106430`.  RH remains unproved.
