# L-91106 — The Xi Pick kernel is a Brownian two-copy reflection form

Claim ID: `L-91106`  
Status: **EXACT PROBABILISTIC TRANSFORM THEOREM**  
Created: 2026-08-11  
Depends on: the Biane--Pitman--Yor Brownian-range representation; `L-91105`  
RH status: **unproved**

## 1. Half-size-biased Brownian coordinate

Let `Y` be the normalized range of a standard Brownian bridge in the BPY identity

\[
 \mathbb E[Y^s]=2\xi(s).
\]

Under the half-size-biased law

\[
 \frac{d\mathbb P_{1/2}}{d\mathbb P}
 =\frac{Y^{1/2}}{\mathbb E Y^{1/2}},
 \qquad Z=\log Y,
\]

one has

\[
\boxed{
 M(r)=\mathbb E_{1/2}e^{rZ}
 =\frac{\xi(\frac12+r)}{\xi(\frac12)}.
}
\tag{L-91106.1}
\]

The functional equation makes `Z` symmetric.

## 2. Impedance as a bounded Brownian regression

For `a>0`, equations (L-91105.1)--(L-91105.2) become

\[
\boxed{
 \ell_a(r)
 =\frac{\mathbb E[e^{rZ}\sinh(aZ)]}
        {\mathbb E[e^{rZ}\cosh(aZ)]}.
}
\tag{L-91106.2}
\]

If

\[
 d\nu_{r,a}(z)
 =\frac{e^{rz}\cosh(az)}
        {\mathbb E[e^{rZ}\cosh(aZ)]}
   d\mathbb P_{1/2}(z),
\]

then

\[
\boxed{
 \ell_a(r)=\mathbb E_{\nu_{r,a}}[\tanh(aZ)].
}
\tag{L-91106.3}
\]

Thus the scalar impedance is the observed response of the bounded odd multiplier `tanh(aZ)`. Pointwise boundedness is not enough for the required Cauchy-space contraction; the observation map is the entire problem.

## 3. Two-copy entry formula

Let `Z_1,Z_2` be independent copies of `Z`, and put

\[
 S=Z_1+Z_2,
 \qquad
 \Delta=Z_1-Z_2,
 \qquad
 p=\frac{r+s}{2},
 \qquad
 q=\frac{r-s}{2}.
\]

Then the cross-multiplied kernel (L-91105.8) satisfies

\[
\boxed{
 \widetilde K_a(r,s)
 =\mathbb E\left[
   \cosh(q\Delta)\,
   \sinh(aS)\,
   \frac{\sinh(pS)}p
  \right],
}
\tag{L-91106.4}
\]

with the removable value `S` at `p=0`.

### Proof

Independence gives

\[
 M(r+a)M(s+a)-M(r-a)M(s-a)
 =\mathbb E[e^{rZ_1+sZ_2}(e^{aS}-e^{-aS})].
\]

Global sign symmetry and exchange of `Z_1,Z_2` reduce the right side to

\[
 2\mathbb E[\cosh(q\Delta)\sinh(pS)\sinh(aS)].
\]

Divide by `r+s=2p`.

## 4. Exact quadratic reflection form

For a finite exponential polynomial

\[
 F(x)=\sum_{j=1}^Nc_j e^{r_jx},
 \qquad r_j>0,
\]

let

\[
 \mathcal R_a(F)
 =\sum_{i,j}\overline{c_i}c_j\widetilde K_a(r_i,r_j).
\]

Then

\[
\boxed{
 \mathcal R_a(F)
 =\mathbb E\left[
  \sinh(aS)
  \int_{-S/2}^{S/2}
   \overline{F\!\left(x+\frac\Delta2\right)}
   F\!\left(x-\frac\Delta2\right)\,dx
 \right].
}
\tag{L-91106.5}
\]

The integral is oriented when `S<0`; its product with `sinh(aS)` is invariant under `(S,Delta)->(-S,-Delta)`.

### Proof

Use

\[
 \frac1{r_i+r_j}=\int_0^\infty e^{-(r_i+r_j)t}\,dt
\]

before summing over `i,j`. This gives

\[
 \mathbb E[(e^{aS}-e^{-aS})I(S,\Delta)],
\]

where

\[
 I(S,\Delta)
 =\int_0^\infty
 \overline{F(Z_1-t)}F(Z_2-t)\,dt
 =\int_{-\infty}^{S/2}
 \overline{F(x+\Delta/2)}F(x-\Delta/2)\,dx.
\]

Average with the globally reflected copy. The difference of the two half-line integrals is exactly the finite interval in (L-91106.5).

## 5. Brownian reflection-positivity criterion

Combining `L-91105` with (L-91106.5), RH follows from the source-specific inequality

\[
\boxed{
 \mathcal R_a(F)\ge0
}
\tag{L-91106.6}
\]

for every rational `0<a<1/2` and every exponential polynomial with positive rational exponents.

This is not generic probability. Symmetry, positive moments, log-convexity, and the pointwise bound `|tanh(aZ)|<1` do not imply (L-91106.6). The new target is a reflection-positivity theorem for the *specific* half-biased Brownian log-range law.
