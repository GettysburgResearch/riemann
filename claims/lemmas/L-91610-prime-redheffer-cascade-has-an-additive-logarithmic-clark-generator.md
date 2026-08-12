# L-91610 — The prime Redheffer cascade has an additive logarithmic Clark generator

Claim ID: `L-91610`  
Status: **PROVED EXACT POSITIVE-REAL LOGARITHMIC LINEARIZATION; COMPLETED INTERCONNECTION OPEN**  
Created: 2026-08-12  
Depends on: `L-91323/L-91324`; `L-91510`  
RH status: **unproved**

## 1. One safe local Euler node

Retain the local lossless Euler–Julia node

\[
 m(z)=c\frac{1-\alpha z}{1-\beta z},
 \qquad
 d(z)=\delta\frac{1-z}{1-\beta z},
 \qquad 0<\alpha<\beta<1,
\]

with

\[
 c=\frac{1-\beta}{1-\alpha},
 \qquad
 \delta^2=\frac{(\beta-\alpha)(1-\alpha\beta)}{(1-\alpha)^2},
\]

so that

\[
 |m(e^{i\theta})|^2+|d(e^{i\theta})|^2=1.
\]

The zero of `m` and its pole are at `1/alpha` and `1/beta`, both outside the
closed unit disk.  Hence `m` is zero free in the disk, `m(0)=c in (0,1)`, and
the principal analytic logarithm below is unambiguous.

## 2. Additive logarithmic generator

Define

\[
 \boxed{\ell(z)=-\log m(z).}
\]

Since `m` is Schur and zero free,

\[
 \Re\ell(z)=-\log|m(z)|\ge0
 \qquad(|z|<1).
\]

Thus `ell` is a positive-real function.  Its Herglotz kernel

\[
 \boxed{
 \mathscr K_\ell(z,w)
 =\frac{\ell(z)+\overline{\ell(w)}}{1-z\overline w}
 \succeq0
 }
\]

is positive semidefinite on every finite disk packet.

Let

\[
 h(z)=\frac{1-m(z)}{1+m(z)}
\]

be the parity Cayley impedance of `L-91510`.  Then exactly

\[
 \boxed{
 \ell(z)=2\operatorname{artanh}h(z).
 }
\]

Indeed `(1+h)/(1-h)=1/m`.  The nonlinear Redheffer law for `h` is therefore
the hyperbolic-coordinate image of ordinary addition of `ell`.

## 3. Boundary Julia entropy

On the unit circle put

\[
 x=|m|^2,
 \qquad
 q=|d|^2=1-x.
\]

Then

\[
 \boxed{
 2\Re\ell
 =-\log|m|^2
 =\int_0^1\frac{|d|^2}{|m|^2+t|d|^2}\,dt.
 }
\]

The proof is the elementary integral

\[
 \int_0^1\frac{1-x}{x+t(1-x)}dt=-\log x.
\]

Thus the logarithmic loss of the returned Euler state is a positive resolvent
average of the exact Julia-detail energy.  No new defect square is introduced.

At the prime resonance `z=1`,

\[
 m(1)=1,
 \qquad d(1)=0,
 \qquad \ell(1)=0.
\]

Prime-atom isolation therefore carries zero entropy loss and remains entirely
in the coefficient-one returned state.

## 4. Finite cascades

For local nodes `m_1,...,m_N`, put

\[
 M_N=\prod_{j=1}^Nm_j,
 \qquad
 \ell_N=-\log M_N.
\]

Because every factor is zero free and anchored positively at zero,

\[
 \boxed{
 \ell_N=\sum_{j=1}^N\ell_j.
 }
\]

Equivalently, if `h_N=(1-M_N)/(1+M_N)`, then

\[
 \boxed{
 h_N=\tanh\left(\frac12\sum_{j=1}^N\ell_j\right).
 }
\]

This is precisely the iterated Redheffer/tanh law of `L-91510`, now in an
additive coordinate.

The total boundary entropy is likewise additive:

\[
 -\log|M_N|^2
 =\sum_{j=1}^N[-\log|m_j|^2].
\]

## 5. Infinite safe prime cascade

On every line `sigma>1`, `L-91324` gives normal convergence of the ordered
Euler–Julia cascade.  The local factors satisfy

\[
 \sum_p|1-m_{p,a,\sigma}(z)|<\infty
\]

locally uniformly, so their anchored logarithms also converge locally
uniformly.  Therefore

\[
 \boxed{
 \ell_{a,\sigma}(z)
 :=-\log\frac{Q_a(\sigma+iz)}{Q_a(\sigma)}
 =\sum_p\ell_{p,a,\sigma}(z)
 }
\]

and `ell_(a,sigma)` is positive real.

Its Herglotz kernel is the limit of the finite prime kernels, and its boundary
real part is the sum of the local Julia entropies.  The complete safe prime
channel is therefore one additive Clark source rather than a nonlinear
infinite Redheffer object.

## 6. Strategic consequence

The prime part of the final completed interconnection may be carried in either
of two equivalent coordinates:

```text
Schur scattering coordinate:       M_(a,sigma);
positive-real parity coordinate:    h_(a,sigma);
additive Clark coordinate:          ell_(a,sigma)=-log M_(a,sigma).
```

The logarithmic coordinate is the one naturally compatible with the additive
annular Green mass of `L-91520` on the sibling route.

## 7. Exact boundary

```text
local analytic logarithm                         EXACT
positive-real / Herglotz kernel                  EXACT
ell = 2 artanh h                                 EXACT
Julia entropy resolvent identity                 EXACT
finite Redheffer cascade linearized additively   EXACT
infinite safe prime logarithmic generator        EXACT
completed signed gamma/pole interconnection      OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVED
```
