# L-15149 — Mellin gauge factorization of the Selberg operator

Claim ID: `L-15149`  
Title: The scale-subtracted Selberg operator is exactly a first derivative conjugated by `(z+1)zeta(z+1)`  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: `L-15147`; elementary Mellin transforms; the Euler-product logarithmic derivative in its initial half-plane  
Scope: exact analytic normal form and the true coercivity obstruction

## 1. Operator and Mellin convention

Extend functions on `[1,infinity)` by zero below `1`. Let

\[
 (\mathcal L f)(x)
 = (\log x)f(x)
 +\sum_{n\le x}{\Lambda(n)\over n}f(x/n)
 -{1\over x}\int_1^x f(t)\,dt.
\]

For a compactly supported smooth test, put

\[
 F(z)=\mathcal M f(z)
 =\int_1^\infty f(x)x^{-z-1}\,dx.
\]

Initially take `Re z` large enough that every interchange is absolute.

## 2. Three exact transforms

Differentiation under the integral gives

\[
 \mathcal M[(\log x)f](z)=-F'(z).
\]

For the von Mangoldt Volterra term, the substitution `x=ny` gives

\[
\begin{aligned}
 \mathcal M\left[
  \sum_{n\le x}{\Lambda(n)\over n}f(x/n)
 \right](z)
 &=\sum_{n\ge1}{\Lambda(n)\over n^{z+1}}F(z)\\
 &=-{\zeta'\over\zeta}(z+1)F(z).
\end{aligned}
\]

For the continuous average, Fubini gives

\[
 \mathcal M\left[{1\over x}\int_1^x f(t)dt\right](z)
 ={F(z)\over z+1}.
\]

Therefore

\[
 \boxed{
 \mathcal M(\mathcal Lf)(z)
 =-F'(z)
 -\left[
 {\zeta'\over\zeta}(z+1)+{1\over z+1}
 \right]F(z).}
 \tag{L-15149.1}
\]

## 3. Exact gauge conjugation

Define

\[
 q(z)=(z+1)\zeta(z+1).
\]

Then

\[
 {q'(z)\over q(z)}
 ={1\over z+1}+{\zeta'\over\zeta}(z+1).
\]

Hence (L-15149.1) is exactly

\[
 \boxed{
 \mathcal M(\mathcal Lf)(z)
 =-q(z)^{-1}{d\over dz}\bigl(q(z)F(z)\bigr).}
 \tag{L-15149.2}
\]

The identity holds first in an absolute-convergence half-plane and then meromorphically wherever both sides are defined.

Thus the apparently complicated arithmetic Volterra operator is a first derivative after multiplication by the completed Euler factor `q`.

## 4. Exact location of the obstruction

The zeros of `q` away from the removable factor at `z=-1` are exactly

\[
 z=\rho-1,
\]

where `rho` is a nontrivial zeta zero, together with the trivial-zero locations.
For the RH strip write

\[
 z=-{1\over2}+w.
\]

Then a nontrivial zero produces

\[
 w=\rho-{1\over2},
\]

whose real part is precisely

\[
 \operatorname{Re}\rho-{1\over2}.
\]

This is the explicit variable shift required in the rightmost-zero energy argument.

Mellin Plancherel on the line `Re z=-1/2+sigma` gives

\[
 \boxed{
 {1\over2\pi}
 \int_{\mathbb R}
 |F(-1/2+\sigma+it)|^2dt
 =\int_1^\infty |f(x)|^2x^{-2\sigma}dx.}
 \tag{L-15149.3}
\]

Thus the critical weighted-`L2` abscissa is measured in the `w` variable and equals the rightmost-zero displacement whenever the standard Hardy continuation hypotheses are supplied.

## 5. Consequence for coercivity proposals

Equation (L-15149.2) shows that an inverse estimate for `mathcal L` is not a routine consequence of the positivity of Selberg coefficients. In a zero-free half-plane one may formally write

\[
 q(z)F(z)
 =C-\int q(z)\mathcal M(\mathcal Lf)(z)\,dz,
\]

but every quantitative estimate for `F` requires control of `1/q`. If `q` has an off-line zero, the corresponding inverse necessarily develops the pole detected by the prime-energy criterion.

Therefore a localized Selberg–Poincare or Mourre theorem strong enough to cross all lines `sigma downarrow 0` carries the full zero-free content. It is not merely a finite-dimensional technicality left after the square identity.

This does not make the route circular: an arithmetic square completion could in principle prove the needed lower bound. It does mean that the lower bound must be established explicitly and cannot be inferred from `Lambda_2>=0` alone.

## 6. Relation to the dilation commutator

The Mellin multiplier of

\[
 (U_af)(x)=a^{-1/2}f(x/a)
\]

is `a^(-z-1/2)`. Commuting the derivative in (L-15149.2) through this exponential multiplier produces exactly

\[
 \mathcal LU_a=U_a\mathcal L+(\log a)U_a.
\]

Thus `L-15148` is the physical-coordinate form of the gauge derivative identity.

## 7. Proof boundary

Closed here:

- the exact Mellin transform of every term in `mathcal L`;
- the gauge factorization;
- the explicit `w=z+1/2` shift and Plancherel weight;
- identification of zeta zeros as the inverse/coercivity obstruction.

Not closed:

- the Hardy uniformity needed to promote every rightmost-zero transfer to reviewed theorem status;
- any unconditional lower bound for `|q|` in the critical half-strip;
- RH.