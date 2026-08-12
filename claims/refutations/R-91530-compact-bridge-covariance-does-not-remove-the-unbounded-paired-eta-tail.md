# R-91530 — Compact-bridge covariance does not remove the unbounded paired-eta tail

Claim ID: `R-91530`  
Status: **EXACT TAIL-SECTOR FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91530/L-91531`; `R-91408`  
RH status: **unproved**

## 1. Why the compact bridge is bounded

The dyadic/gamma bridge lives on the finite interval

\[
 0<t<\log2.
\]

Its change of exponential tilt has bounded Radon--Nikodym derivative, so the
multiplication unitary of `L-91531` intertwines every carrier and delay.

## 2. The paired eta channel has unbounded support

Using

\[
 (2m-1)^{-s}-(2m)^{-s}
 =s\int_{2m-1}^{2m}x^{-s-1}dx,
\]

put `y=log x` and

\[
 E=\bigcup_{m\ge1}
 [\log(2m-1),\log(2m)].
\]

Then

\[
\boxed{
 \frac{\eta_D(s)}s
 =\int_E e^{-sy}\,dy
 \qquad(\Re s>0).
}
\tag{R-91530.1}

\]

Changing the real exponent from `1` to `1-2omega` multiplies the common
physical carrier vector by

\[
 e^{\omega y}.
\]

Because `E` is unbounded,

\[
\boxed{
 \operatorname*{ess\,sup}_{y\in E}e^{\omega y}=\infty.
}
\tag{R-91530.2}

\]

On the truncation ending near `2N`, the multiplication norm grows like

\[
\boxed{
 (2N)^\omega.
}
\tag{R-91530.3}

\]

Thus the analogue of the finite-interval carrier-covariant map is unbounded in
one fixed paired source space.

## 3. Consequence for the Householder construction

The one-vector Householder of `L-91431` is valid at its declared one-node
scope. It cannot be promoted to a bounded full-carrier intertwiner by adjoining
the compact bridge. The unbounded eta tail survives after the pole component
has been regularized.

A valid completion must do at least one of:

```text
work only at the one-node source vector;
use a rigged graph space for the unbounded multiplication;
entangle the eta tail with the residual beta/gamma source before norms;
construct a positive environment for the Gram mismatch.
```

## 4. What has nevertheless been closed

The earlier obstruction contained two distinct effects:

```text
one unstable free gamma pole;
one unbounded paired arithmetic tail.
```

`L-91530/L-91531` remove the first completely, including full carrier
polarization. Only the second remains.

## 5. Exact boundary

```text
dyadic/gamma pole bridge                         COMPACT AND COVARIANT
paired eta support                               UNBOUNDED
same-space full-carrier tilt map                 UNBOUNDED
one-node paired eta Householder                  EXACT
eta-tail + beta/gamma entangled completion       OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVED
```
