# L-91018 — The positive pole-subtracted tail pays both Cauchy detail ports by one exact Gram kernel

Claim ID: `L-91018`  
Status: **PROPOSED COMPLETE EXACT POSITIVE-EMISSION THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91013`, `L-91015`  
RH status: **unproved**

## 1. Physical detail filters

Use the Fourier convention

\[
 \widehat f(u)=\int_{\mathbb R}f(t)e^{-iut}\,dt.
\]

The two rational detail channels of the dyadic Cauchy square have inverse
Fourier transforms

\[
 \boxed{
 \phi_{1,a}(t)
 =\frac{i\sqrt6\,a}{3}\operatorname{sgn}(t)
  \left(e^{-a|t|}-e^{-2a|t|}\right),
 }
 \tag{L-91018.1}
\]

and

\[
 \boxed{
 \phi_{2,a}(t)
 =\frac{\sqrt{15}\,a}{6}
  \left(-e^{-a|t|}+2e^{-2a|t|}\right).
 }
 \tag{L-91018.2}
\]

Both have zero integral, exactly reflecting `g_(j,a)(0)=0`.

For `t>=0`, their total pointwise energy is

\[
 \boxed{
 |\phi_{1,a}(t)|^2+|\phi_{2,a}(t)|^2
 =a^2\left[
  \frac{13}{12}e^{-2at}
  -3e^{-3at}
  +\frac73e^{-4at}
 \right].
 }
 \tag{L-91018.3}
\]

The bracket need not be treated coefficientwise; it is a sum of two literal
squares by (L-91018.1)--(L-91018.2).

## 2. Positive tail source

For the dyadic pole-subtracted recurrence of `L-91015`, write

\[
 D_a(s)=D_{a,a}(s)
 =-\int_0^\infty e^{-(s-1)t}W_a(t)\,dt,
 \qquad W_a(t)\ge0.
 \tag{L-91018.4}
\]

Define the two-component carrier vector

\[
 \Phi_{a,x}(t)
 =e^{-ixt}
 \begin{pmatrix}
  \phi_{1,a}(t)\\
  \phi_{2,a}(t)
 \end{pmatrix},
 \qquad t\ge0.
 \tag{L-91018.5}
\]

## 3. Exact emitted Gram kernel

Put

\[
 \boxed{
 \mathcal E_a(x,y)
 =\int_0^\infty
  W_a(t)\,
  \langle\Phi_{a,x}(t),\Phi_{a,y}(t)\rangle_{\mathbb C^2}
  \,dt.
 }
 \tag{L-91018.6}
\]

For every finite set of carriers `x_j` and coefficients `c_j`,

\[
 \boxed{
 \sum_{j,k}\bar c_jc_k\mathcal E_a(x_j,x_k)
 =\int_0^\infty W_a(t)
  \left\|\sum_jc_j\Phi_{a,x_j}(t)\right\|^2dt
 \ge0.
 }
 \tag{L-91018.7}
\]

Thus the complete independent-frequency emitted block is positive semidefinite,
not merely positive on its diagonal.

## 4. Four-evaluation formula

Using (L-91018.3) and (L-91018.4), with `Delta=x-y`,

\[
 \boxed{
 \begin{aligned}
 \mathcal E_a(x,y)
 =-a^2\Bigg[
 &\frac{13}{12}D_a(1+2a+i\Delta)\\
 &-3D_a(1+3a+i\Delta)\\
 &+\frac73D_a(1+4a+i\Delta)
 \Bigg].
 \end{aligned}
 }
 \tag{L-91018.8}
\]

Every sample on the right lies in the absolute half-plane of the positive tail
representation.  Equation (L-91018.8) is therefore a finite safe-source formula
for the entire two-port detail reserve.

## 5. Diagonal reserve

On the diagonal,

\[
 \boxed{
 \mathcal E_a(x,x)
 =\int_0^\infty W_a(t)
  \left(|\phi_{1,a}(t)|^2+|\phi_{2,a}(t)|^2\right)dt
 \ge0,
 }
 \tag{L-91018.9}
\]

independently of `x`.  More importantly, the full matrix positivity in
(L-91018.7) remains available before carrier localization or aggregation, so
this reserve may be spent once without a scalar-to-matrix polarization gap.

## 6. Exact source/scattering interpretation

`L-91015` splits the pole-subtracted sieve flow into

```text
one inherited coefficient-one state
+ one positive tail channel W_a.
```

`L-91013` splits the Cauchy scattering step into

```text
one returned coarse state
+ two emitted detail filters phi_(1,a), phi_(2,a).
```

Equation (L-91018.6) is their exact tensor pairing.  It proves that the new
tail forcing pays the complete two-port Hermitian detail block with no negative
mode, no independent-frequency loss, and no same-scale return.

## 7. Remaining interface

After this theorem, the emitted forcing is fully paid.  The only term not yet
identified with a positive Gram block is the inherited pole-subtracted
fluctuation

\[
 \widetilde H_a(s)
 \frac{Q_a(s+2a)}{Q_a(1+2a)}
\]

from `L-91015.12` after the actual explicit-formula/window coisometry.  A proof
must show that this term returns solely as the delayed coarse state, rather than
creating an additional current-scale signed boundary block.

## 8. Boundary

Closed:

```text
exact physical detail filters;
positive two-port tail Gram;
independent-frequency PSD before aggregation;
finite four-evaluation safe-source formula;
one-shot/no-double-spend detail payment.
```

Open:

```text
intertwining of the inherited fluctuation with the delayed coarse state;
absence of an extra current-scale boundary block;
coefficient-one dyadic recurrence;
RH.
```
