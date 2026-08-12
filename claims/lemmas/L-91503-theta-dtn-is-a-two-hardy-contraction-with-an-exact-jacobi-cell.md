# L-91503 — Theta DtN is a two-Hardy contraction with an exact Jacobi cell

Claim ID: `L-91503`  
Status: **EXACT KERNEL REDUCTION AND ONE-CELL PASSIVITY THEOREM — GLOBAL COUPLING OPEN**  
Created: 2026-08-12  
Depends on: `L-91105`--`L-91108`, `L-91302`, `T-91101`  
RH status: **unproved**

## 1. Xi impedance

In the theta strip, put

\[
M(q)=\int_0^\infty\Phi(t)\cosh(qt)dt>0
\]

and, for `r>0` with `r+a<1/2`,

\[
\ell_a(r)
=\frac{M(r+a)-M(r-a)}
       {M(r+a)+M(r-a)}.
\tag{L-91503.1}
\]

The target positive-real kernel is

\[
\mathsf K_a(r,s)
=\frac{\ell_a(r)+\ell_a(s)}{r+s}.
\tag{L-91503.2}
\]

Put

\[
D_a(r)=M(r+a)+M(r-a)>0.
\]

A direct cancellation gives the exact diagonal congruence

\[
\boxed{
D_a(r)D_a(s)\mathsf K_a(r,s)
=\frac{2}{r+s}
\left[
M(r+a)M(s+a)-M(r-a)M(s-a)
\right].
}
\tag{L-91503.3}
\]

Thus the theta DtN theorem is not a generic ratio estimate.  It is one precise
difference of two Cauchy-Hardy Grams.

## 2. Two Hardy synthesis operators

For a finite packet `r_1,...,r_N` and coefficients `c_j`, define

\[
(\mathcal J_{a,+}c)(t)
=\sum_jc_jM(r_j+a)e^{-r_jt},
\]

\[
(\mathcal J_{a,-}c)(t)
=\sum_jc_jM(r_j-a)e^{-r_jt},
\qquad t>0.
\tag{L-91503.4}
\]

Since

\[
\int_0^\infty e^{-(r+s)t}dt=\frac1{r+s},
\]

one has the fully polarized identity

\[
\boxed{
\sum_{j,k}\bar c_jc_k
D_a(r_j)D_a(r_k)\mathsf K_a(r_j,r_k)
=2\left(
 \|\mathcal J_{a,+}c\|_2^2
-\|\mathcal J_{a,-}c\|_2^2
\right).
}
\tag{L-91503.5}
\]

Consequently,

\[
\boxed{
\mathsf K_a\succeq0
\quad\Longleftrightarrow\quad
\|\mathcal J_{a,-}c\|_2
\le\|\mathcal J_{a,+}c\|_2
\text{ for every finite }c.
}
\tag{L-91503.6}
\]

The missing theta/Brownian boundary theorem is therefore one explicit
contraction between two scalar Hardy synthesis maps.  A valid DtN construction
must realize this contraction before taking the Cayley transform.

## 3. Brownian two-copy form

Let `Z_1,Z_2` be the two half-size-biased Brownian log-range variables and put

\[
S=Z_1+Z_2,
\qquad
\Delta=Z_1-Z_2.
\]

Expanding the two products in (L-91503.3), symmetrizing under exchange of the
two copies and then under `(S,Delta)->(-S,-Delta)`, gives the resident reflection
form

\[
\boxed{
\begin{aligned}
&M(r+a)M(s+a)-M(r-a)M(s-a)\\
&\quad=2\,\mathbb E\left[
 \cosh\!\left(\frac{r-s}{2}\Delta\right)
 \sinh(aS)
 \sinh\!\left(\frac{r+s}{2}S\right)
 \right].
\end{aligned}}
\tag{L-91503.7}
\]

Equation (L-91503.5) is therefore exactly the Brownian reflection quadratic of
`T-91101`, with no normalization ambiguity.

## 4. Exact one-cell tilted Jacobi operator

For one paired Gamma mode, let

\[
U\sim\mathrm{Beta}(2,2),
\qquad V=2U-1\in(-1,1).
\]

The un-tilted density is proportional to `1-V^2`.  The exact half-size
Brownian tilt contributes `(1-V^2)^(1/4)`.  Thus the one-cell tilted law is

\[
\boxed{
d\mu_{\rm cell}(V)
=Z^{-1}(1-V^2)^{5/4}dV.
}
\tag{L-91503.8}
\]

Its Beta-Jacobi Dirichlet form is

\[
\boxed{
\mathcal E_{\rm cell}(f)
=\frac14\int_{-1}^1
 (1-V^2)|f'(V)|^2d\mu_{\rm cell}(V).
}
\tag{L-91503.9}
\]

The associated nonnegative generator is

\[
\boxed{
\mathcal L_{\rm cell}f
=-\frac14\left[
 (1-V^2)f''-\frac92Vf'
\right].
}
\tag{L-91503.10}
\]

The Gegenbauer polynomials

\[
C_n^{7/4}(V)
\]

diagonalize this operator exactly:

\[
\boxed{
\mathcal L_{\rm cell}C_n^{7/4}
=\frac{n(n+7/2)}4C_n^{7/4}.
}
\tag{L-91503.11}
\]

Hence the one-cell spectral gap is

\[
\boxed{\lambda_1=\frac98,}
\tag{L-91503.12}
\]

and the sharp one-cell Poincaré inequality is

\[
\boxed{
\operatorname{Var}_{\mu_{\rm cell}}(f)
\le\frac89\mathcal E_{\rm cell}(f).
}
\tag{L-91503.13}
\]

This is a strict passive reserve, not merely nonnegativity of the local
carré-du-champ.

## 5. Hyperbolic tangent coordinate

With

\[
\Delta=\operatorname{artanh}V,
\]

the one-cell density becomes proportional to `sech(Delta)^(9/2)dDelta`, and
(L-91503.9) becomes

\[
\mathcal E_{\rm cell}(f)
=\frac14\int
 \cosh^2\Delta\,|\partial_\Delta f|^2
 d\mu_{\rm cell}(\Delta).
\tag{L-91503.14}
\]

For the full BPY reservoir, the exact tangent direction is

\[
\partial_\Delta-	anh\Delta\,\partial_S.
\]

Thus (L-91503.10)--(L-91503.14) identify the local Sturm--Liouville cell that
must be coupled along the invariant

\[
S+\log\cosh\Delta.
\]

## 6. Remaining global theorem

The global half-size tilt couples all Beta cells through

\[
(A^2-D^2)^{1/4}.
\]

The remaining theta/Brownian theorem is now sharply stated:

> Couple the exact Jacobi cells through the `(S,Delta)` invariant and prove that
> their tensorized/conditioned positive energy realizes a contraction
> `J_(a,-) <= J_(a,+)` in (L-91503.6), with the modular theta boundary atom
> retained.

A proof may proceed through a conditional spectral-gap theorem, a genuine
boundary triple, or a sum--difference Green identity.  The one-cell gap shows
that no local Beta mode is the obstruction; only the coupled boundary
identification remains.

## 7. Exact boundary

```text
Xi impedance -> two Cauchy-Hardy Grams             EXACT
full matrix sign -> one Hardy contraction           EXACT
Brownian reflection form normalization              EXACT
one tilted Beta cell                               EXACT GEGENBAUER SYSTEM
one-cell spectral gap 9/8                          EXACT
local Jacobi passivity                             CLOSED
coupled S-Delta DtN contraction                    OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVED
```
