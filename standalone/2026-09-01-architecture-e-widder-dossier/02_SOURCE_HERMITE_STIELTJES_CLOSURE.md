# Source–Hermite–Stieltjes closure of Architecture E

Status: **PROPOSED COMPLETE EQUIVALENCE CHAIN; INDEPENDENT REVIEW REQUIRED; FINAL POSITIVITY AND RH REMAIN UNPROVED.**

This note gives the full analytic chain from the actual Riemann theta source to the generalized-Schur, Hermite–Bezout, safe Pick and Stieltjes formulations.  The same chain is present in successor PR #784; it is reproduced here so that this standalone dossier is self-contained and so that the imported/new boundary can be reviewed in one place.

## 1. Normalization

Use

\[
 \xi_{\rm R}(s)
 =\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

and the centered entire function

\[
 X(z)=\xi_{\rm R}(1/2+iz).
\]

With the reviewed full-line convention,

\[
 X(z)=\int_{\mathbb R}\Phi(u)e^{izu}\,du,
\]

where `Phi` is real, positive, even and superexponentially decaying.  Some historical repository packets use a half-kernel normalization; the present convention is fixed throughout to prevent a factor-four error in the source polarization.

## 2. The companion generalized-Schur kernel is Hermite–Bezout

For `lambda>0`, put

\[
 E_\lambda(z)=X(z)+i\lambda X'(z),
 \qquad
 \Theta_\lambda(z)=
 \frac{X(z)-i\lambda X'(z)}
      {X(z)+i\lambda X'(z)},
\]

with all removable common factors cancelled when interpreting the quotient.

Define

\[
 \boxed{
 \mathcal B_X(z,w)=
 \frac{X'(z)X(\bar w)-X(z)X'(\bar w)}
      {\bar w-z}.
 }
 \tag{2.1}
\]

A direct expansion gives

\[
 \boxed{
 \frac{1-\Theta_\lambda(z)\overline{\Theta_\lambda(w)}}
      {2\pi i(\bar w-z)}
 =
 \frac{\lambda}
      {\pi E_\lambda(z)\overline{E_\lambda(w)}}
 \mathcal B_X(z,w).
 }
 \tag{2.2}
\]

Indeed,

\[
 \begin{aligned}
 &(X+i\lambda X')(z)(X-i\lambda X')(\bar w)\\
 &\qquad -(X-i\lambda X')(z)(X+i\lambda X')(\bar w)\\
 &=2i\lambda
 \bigl(X'(z)X(\bar w)-X(z)X'(\bar w)\bigr).
 \end{aligned}
\]

Every finite generalized-Schur matrix is therefore a positive diagonal congruence of the corresponding Hermite–Bezout matrix.  Its inertia is independent of `lambda>0`.

On the real diagonal,

\[
 \mathcal B_X(x,x)=X'(x)^2-X(x)X''(x),
\]

the ordinary Laguerre expression.

## 3. Negative squares count distinct nonreal zero locations

The symmetric genus-one canonical product for `X` gives, away from the zeros,

\[
 \boxed{
 \frac{\mathcal B_X(z,w)}{X(z)X(\bar w)}
 =
 \frac{X'(z)/X(z)-X'(\bar w)/X(\bar w)}
      {\bar w-z}
 =
 \sum_{\rho\in Z(X)}
 \frac{m_\rho}{(z-\rho)(\bar w-\rho)}.
 }
 \tag{3.1}
\]

The affine regularizing terms cancel in the divided difference.

A real zero `r` contributes

\[
 m_r\frac1{z-r}\overline{\frac1{w-r}},
\]

a positive rank-one kernel.

For a nonreal conjugate pair `rho,bar(rho)`, define

\[
 u_\rho(z)=\frac1{z-\rho},
 \qquad
 u_{\bar\rho}(z)=\frac1{z-\bar\rho}.
\]

The paired contribution is

\[
 m_\rho\left[
 u_\rho(z)\overline{u_{\bar\rho}(w)}
 +u_{\bar\rho}(z)\overline{u_\rho(w)}
 \right],
\]

with coefficient matrix

\[
 m_\rho
 \begin{pmatrix}
 0&1\\
 1&0
 \end{pmatrix}.
\]

It has inertia `(1,1)`.  Distinct Cauchy features are linearly independent because a finite relation would be a rational function with distinct poles and every residue zero.  Hence every finite collection of distinct conjugate pairs supplies that many negative directions.

Conversely, the feature representation has one negative coordinate for each distinct pair and no other negative coordinate.  Finite exhaustion, or equivalently local pole separation followed by negative diagonal dominance, yields

\[
 \boxed{
 \operatorname{sq}_{-}(\mathcal B_X)
 =
 \#\bigl(Z(X)\cap\mathbb C_+\bigr)_{\rm distinct}.
 }
 \tag{3.2}
\]

Multiplicity scales the block but does not create a new independent negative direction.  This distinction is required because removable common-factor cancellation in the companion quotient also sees zero locations rather than algebraic multiplicity.

Therefore

\[
 \boxed{
 \mathrm{RH}
 \iff
 \mathcal B_X\succeq0
 \iff
 \Theta_\lambda\text{ has zero negative squares}.
 }
 \tag{3.3}
\]

One off-critical Riemann quartet gives two upper-half-plane zeros of `X` and hence two negative squares.

## 4. Exact source polarization

Define the two-point theta source used in the current and double-scaling packets:

\[
 H_\xi(d)=
 \Phi\left(\frac{\xi-d}{2}\right)
 \Phi\left(\frac{\xi+d}{2}\right).
\]

For real `a,b`, define

\[
 \boxed{
 \mathcal A_\Phi(a,b)
 =\frac12\int_{|a+b|}^{\infty}
 \xi H_\xi(a-b)\,d\xi.
 }
 \tag{4.1}
\]

The theta tail makes the integral absolutely convergent.  If `a+b>=0`, the substitution `xi=a+b+2r` gives

\[
 \boxed{
 \mathcal A_\Phi(a,b)
 =\int_0^\infty
 (a+b+2r)\Phi(a+r)\Phi(b+r)\,dr.
 }
 \tag{4.2}
\]

If `a+b<0`, evenness gives

\[
 \mathcal A_\Phi(a,b)=\mathcal A_\Phi(-a,-b).
\]

In either open half-plane `a+b\ne0`, differentiation under the integral yields

\[
 \boxed{
 (\partial_a+\partial_b)\mathcal A_\Phi(a,b)
 =-(a+b)\Phi(a)\Phi(b).
 }
 \tag{4.3}
\]

For `a+b>0`, the integrand in (4.2) has directional derivative equal to its `r` derivative, so the identity is the boundary term at `r=0`; the negative half-plane follows by evenness.

## 5. Double Fourier transform

Let

\[
 \widehat{\mathcal A}(z,w)=
 \iint_{\mathbb R^2}
 e^{iza}e^{-i\bar w b}
 \mathcal A_\Phi(a,b)\,da\,db.
\]

Multiply (4.3) by the exponential and integrate by parts.  The left side is

\[
 i(\bar w-z)\widehat{\mathcal A}(z,w).
\]

The right side is

\[
 i\bigl[X'(z)X(\bar w)-X(z)X'(\bar w)\bigr].
\]

Thus

\[
 \boxed{
 \mathcal B_X(z,w)=
 \iint_{\mathbb R^2}
 e^{iza}e^{-i\bar w b}
 \mathcal A_\Phi(a,b)\,da\,db.
 }
 \tag{5.1}
\]

All boundary terms vanish by the theta tail.  The identity holds first in an absolute-convergence region and then on the natural Schwartz test space and by analytic continuation.

Fourier transformation is unitary.  Therefore, in quadratic-form sense,

\[
 \boxed{
 \mathcal A_\Phi\succeq0
 \iff
 \mathcal B_X\succeq0
 \iff
 \mathrm{RH}.
 }
 \tag{5.2}
\]

This is the exact repair of ordinary positive-source theory.  Pointwise positivity of `Phi`, `H_xi`, or even of the entries `A_Phi(a,b)` is not positive definiteness of the two-variable kernel.

## 6. Identification with the zero-frequency Weyl kernel

The current Weyl–Volterra programme uses

\[
 K_\omega(a,b)=
 \frac12\int_{|(a+b)/2|}^{\infty}
 y\cosh(2\omega y)
 \Phi\left(y+\frac{a-b}{2}\right)
 \Phi\left(y-\frac{a-b}{2}\right)\,dy.
\]

At `omega=0`, the substitution `xi=2y` in (4.1) gives

\[
 \boxed{
 \mathcal A_\Phi(a,b)=4K_0(a,b).
 }
 \tag{6.1}
\]

Consequently

\[
 K_0\succeq0
 \iff
 \mathcal A_\Phi\succeq0
 \iff
 \mathrm{RH}.
\]

No separate uniform-in-`omega` theorem is needed for this endpoint, and no separate `KLM -> de Branges` bridge is needed once (5.1) is available.

## 7. The safe Euler axis is the same kernel

Put

\[
 Y(x)=\xi_{\rm R}(1/2+x)=X(ix),
 \qquad
 F(x)=\frac{Y'(x)}{Y(x)}.
\]

Using the functional equation to evaluate the derivatives at `ix` and `-iy` gives

\[
 \boxed{
 \mathcal B_X(ix,iy)
 =Y(x)Y(y)\frac{F(x)+F(y)}{x+y}.
 }
 \tag{7.1}
\]

Thus the safe Pick kernel

\[
 \mathcal H(x,y)=\frac{F(x)+F(y)}{x+y}
\]

is the imaginary-axis restriction of the Hermite kernel, up to a positive diagonal congruence.

Combining (5.1) and (7.1),

\[
 Y(x)Y(y)\mathcal H(x,y)
 =
 \iint e^{-xa-yb}\mathcal A_\Phi(a,b)\,da\,db.
\]

For `x>1/2`, the logarithmic derivative is Euler-safe:

\[
 \boxed{
 \begin{aligned}
 F(x)={}&
 \frac1{x+1/2}+\frac1{x-1/2}
 -\frac12\log\pi
 +\frac12\psi\left(\frac{x+1/2}{2}\right)\\
 &-\sum_{n\ge2}\frac{\Lambda(n)}{n^{x+1/2}}.
 \end{aligned}
 }
 \tag{7.2}
\]

## 8. Exact Stieltjes endpoint

Set

\[
 p(t)=\frac{F(\sqrt t)}{\sqrt t},
 \qquad t>1/4.
\]

Under RH, the centered genus-zero product gives

\[
 \boxed{
 p(t)=2\sum_{\gamma>0}
 \frac{m_\gamma}{t+\gamma^2}.
 }
 \tag{8.1}
\]

Hence `p` is a Stieltjes function with positive measure

\[
 d\mu(r)=2\sum_{\gamma>0}m_\gamma\,\delta_{\gamma^2}(r).
\]

Conversely, suppose the known values on `t>1/4` admit a Stieltjes continuation

\[
 p(t)=C+\int_0^\infty\frac{d\mu(r)}{t+r},
 \qquad C\ge0,
 \quad \mu\ge0.
\]

The actual asymptotic gives `p(t)->0`, so `C=0`.  For `Re(x)>0`, the cut-plane map `x^2` avoids `(-infinity,0]`, and

\[
 \widetilde F(x)=xp(x^2)
 =\frac12\int_0^\infty
 \left[
 \frac1{x-i\sqrt r}+\frac1{x+i\sqrt r}
 \right]d\mu(r)
\]

is analytic with nonnegative real part.  It agrees with `Y'/Y` for real `x>1/2`; the identity theorem then continues it through the right half-plane.  Therefore `Y'/Y` has no pole there and `Y` has no right-half-plane zero.  Evenness and conjugation symmetry put all zeros on the imaginary axis, which is RH.

Thus

\[
 \boxed{
 \mathrm{RH}
 \iff
 p(t)=F(\sqrt t)/\sqrt t
 \text{ is a Stieltjes function}.
 }
 \tag{8.2}
\]

## 9. Two-channel Gram factorization

A Stieltjes measure gives

\[
 \begin{aligned}
 \mathcal H(x,y)
 &=\int_0^\infty
 \frac{r+xy}{(x^2+r)(y^2+r)}\,d\mu(r)\\
 &=\int_0^\infty
 \left[
 \frac{\sqrt r}{x^2+r}
 \frac{\sqrt r}{y^2+r}
 +
 \frac{x}{x^2+r}
 \frac{y}{y^2+r}
 \right]d\mu(r).
 \end{aligned}
 \tag{9.1}
\]

This is the canonical two-channel feature map.  The Segre/exterior-power machinery can organize determinants of such a map, but it cannot create the positive measure `mu`; that measure is the missing purity datum.

## 10. Loewner decomposition

For positive nodes `x_i`, put `t_i=x_i^2` and let `L_h[t]` denote the Loewner matrix of `h`.  With `D_x=diag(x_i)`, direct algebra gives

\[
 \boxed{
 \mathcal H[\mathbf x]
 =L_{tp}[\mathbf t]
 -D_xL_p[\mathbf t]D_x.
 }
 \tag{10.1}
\]

For `i\ne j`, the numerator is

\[
 t_ip(t_i)-t_jp(t_j)-x_ix_j[p(t_i)-p(t_j)]
 =(x_i-x_j)[x_ip(t_i)+x_jp(t_j)],
\]

and division by `(x_i-x_j)(x_i+x_j)` proves the off-diagonal identity; the diagonal is `(tp)'-tp'=p`.

If `p` is Stieltjes, then

\[
 -L_p[\mathbf t]_{ij}
 =\int_0^\infty
 \frac{d\mu(r)}{(t_i+r)(t_j+r)},
\]

and

\[
 L_{tp}[\mathbf t]_{ij}
 =\int_0^\infty
 \frac{r\,d\mu(r)}{(t_i+r)(t_j+r)}.
\]

Both are Gram matrices.  Scalar monotonicity pays only the lowest orders; all-order matrix monotonicity is the Stieltjes/RH endpoint.

## 11. Explicit prime-shift accretivity

Let

\[
 e_x(t)=e^{-xt}
\]

in `L^2(0,infinity)` and define `A_0=-d/dt` on the finite exponential span, so `A_0e_x=xe_x`.  Put `T=F(A_0)` on this core.  Then

\[
 \mathcal H(x,y)
 =\langle Te_x,e_y\rangle
 +\langle e_x,Te_y\rangle.
\]

The Euler formula (7.2) gives

\[
 \boxed{
 \begin{aligned}
 T={}&(A_0+1/2)^{-1}+(A_0-1/2)^{-1}
 -\frac12\log\pi\\
 &+\frac12\psi\left(\frac{A_0+1/2}{2}\right)
 -\sum_{n\ge2}
 \frac{\Lambda(n)}{\sqrt n}
 e^{-(\log n)A_0}.
 \end{aligned}
 }
 \tag{11.1}
\]

For every finite exponential polynomial

\[
 g(t)=\sum_jc_je^{-x_jt},
 \qquad x_j>1/2,
\]

the series is absolutely convergent term by term.  The all-order safe Pick theorem is therefore

\[
 \boxed{
 \mathrm{RH}
 \iff
 2\operatorname{Re}\langle Tg,g\rangle\ge0
 \quad\text{for every finite exponential polynomial }g.
 }
 \tag{11.2}
\]

The last sum consists of literal prime-power translation-semigroup operators.  This is the source-faithful operator form of the remaining theorem.  Applying a ratio mask, nonorthogonal quotient or gauge inversion before estimating it is forbidden by the #770 barriers unless the full metric and connection are carried through.

## 12. Source-quadrant anticommutator form

On the positive quadrant define the Hankel operator

\[
 (H_\Phi f)(a)=\int_0^\infty\Phi(a+r)f(r)\,dr
\]

and let `M` be multiplication by the coordinate.  Formula (4.2) gives the operator identity

\[
 \boxed{
 \mathcal A_\Phi
 =MH_\Phi^2+H_\Phi^2M+2H_\Phi M H_\Phi
 =\{H_\Phi,\{M,H_\Phi\}\}.
 }
 \tag{12.1}
\]

This explains why entrywise source positivity is inadequate: the target is an anticommutator, not a manifest square.

## 13. Exact boundary

```text
companion Schur/Hermite congruence          PROPOSED COMPLETE / REVIEW
negative squares versus zero locations      PROPOSED COMPLETE / REVIEW
source polarization and Fourier bridge      PROPOSED COMPLETE / REVIEW
A_Phi = 4 K_0                              PROPOSED COMPLETE / REVIEW
safe-axis restriction                       PROPOSED COMPLETE / REVIEW
Stieltjes endpoint and two-channel Gram      PROPOSED COMPLETE / REVIEW
Loewner and prime-shift formulations         PROPOSED COMPLETE / REVIEW
source/Hermite positivity                    OPEN / RH-EQUIVALENT
Riemann Hypothesis                           UNPROVED
```
