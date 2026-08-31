# Architecture E closure: source polarization, Hermite kernel, Stieltjes endpoint, and the exact remaining theorem

Status: **PROVED EQUIVALENCE / GAP AUDIT; RH REMAINS UNPROVED.**

This note carries the proposed source--Hermite--Stieltjes architecture to its
exact endpoint.  It proves all translation arrows between the actual Riemann
theta source, the Hermite--Bezout kernel, the companion generalized-Schur
kernel, the safe Euler-axis Pick kernel, and a Stieltjes representation.  It
also identifies the source polarization with the `omega=0` kernel in the
current Weyl--Volterra programme.

The final positivity assertion is not proved here.  It is equivalent to RH.
A tempting Volterra multiplier shortcut is audited in Section 9: its stated
pointwise contraction does not survive the non-isometric compression without
an additional weighted inequality, and that weighted inequality expands to
the original source positivity target.

This packet changes no frozen predecessor theorem.  It is a theorem-sized
synthesis and a firewall against silently promoting an equivalent
contraction into a proof.

## 1. Normalization

Use the centered completed function and full-line Fourier convention

\[
 X(z)=\xi_{\rm R}(1/2+iz)
     =\int_{\mathbb R}\Phi(u)e^{izu}\,du,
\]

where

\[
 \xi_{\rm R}(s)
 =\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

The actual kernel `Phi` is the positive even full-line kernel fixed in
[`XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md`](XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md).
In particular it is twice the historical half-kernel used in some older
sources.  The factor does not affect any sign below, but fixing it prevents
a factor-four error in the source polarization.

All identities below initially hold where absolute convergence makes every
operation immediate and then extend by analyticity or in the tempered
distribution/form sense stated explicitly.

## 2. Companion Schur kernel is the Hermite--Bezout kernel

For fixed `lambda>0`, put

\[
 E_\lambda(z)=X(z)+i\lambda X'(z),\qquad
 \Theta_\lambda(z)
 =\frac{X(z)-i\lambda X'(z)}
        {X(z)+i\lambda X'(z)}.
\]

After the usual removable cancellations, define

\[
 {\cal B}_X(z,w)
 =\frac{X'(z)X(\bar w)-X(z)X'(\bar w)}
        {\bar w-z}.
 \tag{E2.1}
\]

A direct expansion gives

\[
 \boxed{\;
 \frac{1-\Theta_\lambda(z)\overline{\Theta_\lambda(w)}}
      {2\pi i(\bar w-z)}
 =
 \frac{\lambda}
      {\pi E_\lambda(z)\overline{E_\lambda(w)}}
 {\cal B}_X(z,w).
 \;}
 \tag{E2.2}
\]

Indeed the numerator before division is

\[
 (X+i\lambda X')(z)(X-i\lambda X')(\bar w)
 -(X-i\lambda X')(z)(X+i\lambda X')(\bar w)
\]

and equals

\[
 2i\lambda\bigl(X'(z)X(\bar w)-X(z)X'(\bar w)\bigr).
\]

Thus every finite generalized-Schur matrix is a positive diagonal
congruence of the corresponding Hermite--Bezout matrix.  Its inertia is
independent of the chosen positive `lambda`.

On the real diagonal,

\[
 {\cal B}_X(x,x)=X'(x)^2-X(x)X''(x).
 \tag{E2.3}
\]

This is the ordinary Laguerre expression.  The raw-innerness theorem in
[`XI_RAW_INNERNESS_RH_EQUIVALENCE_FIREWALL.md`](XI_RAW_INNERNESS_RH_EQUIVALENCE_FIREWALL.md)
already proves that Schur/inner behavior for one positive `lambda` is
RH-equivalent.  Formula (E2.2) identifies the exact kernel carrying that
equivalence.

## 3. Negative squares and nonreal zero locations

The symmetric genus-one product for `X` gives, away from its zeros,

\[
 \boxed{\;
 \frac{{\cal B}_X(z,w)}
      {X(z)X(\bar w)}
 =
 \frac{X'(z)/X(z)-X'(\bar w)/X(\bar w)}
      {\bar w-z}
 =
 \sum_{\rho\in Z(X)}
 \frac{m_\rho}
      {(z-\rho)(\bar w-\rho)}.
 \;}
 \tag{E3.1}
\]

The affine regularization terms in the logarithmic derivative cancel in
the divided difference.

A real zero `r` contributes the positive rank-one kernel

\[
 m_r\frac1{z-r}\overline{\frac1{w-r}}.
 \tag{E3.2}
\]

For a nonreal conjugate pair `rho,bar(rho)`, write
`u_rho(z)=1/(z-rho)`.  The paired contribution is

\[
 m_\rho\left(
 u_\rho(z)\overline{u_{\bar\rho}(w)}
 +u_{\bar\rho}(z)\overline{u_\rho(w)}
 \right),
 \tag{E3.3}
\]

whose coefficient matrix on the two Cauchy features is

\[
 m_\rho
 \begin{pmatrix}0&1\\1&0\end{pmatrix}.
 \tag{E3.4}
\]

It has one positive and one negative direction.  Distinct Cauchy features
are linearly independent: a finite linear relation is a rational function
with distinct poles and hence has every residue zero.  Consequently every
finite collection of distinct conjugate pairs supplies that many negative
directions.  Conversely, (E3.1) is the orthogonal direct sum, at the feature
level, of positive real-zero blocks and one `(1,1)` Pontryagin block for
each distinct nonreal conjugate pair.  Finite exhaustion and local pole
separation give

\[
 \boxed{\;
 {\rm sq}_{-}({\cal B}_X)
 =
 \#\bigl(Z(X)\cap{\mathbb C}_+\bigr)_{\rm distinct}.
 \;}
 \tag{E3.5}
\]

If the right side is infinite, the kernel has arbitrarily many negative
squares.  Multiplicity scales a Cauchy feature but does not create a new
independent negative direction.  One off-critical Riemann quartet gives two
upper-half-plane zero locations and hence two negative squares.

In particular

\[
 \boxed{\quad
 {\rm RH}
 \iff {\cal B}_X\succeq0
 \iff \Theta_\lambda\hbox{ has zero negative squares}.
 \quad}
 \tag{E3.6}
\]

Only (E3.6), not a multiplicity-weighted count, is needed below.

## 4. Exact source polarization

Define the source product already used in the odd-current packets,

\[
 H_\xi(d)
 =
 \Phi\left(\frac{\xi-d}{2}\right)
 \Phi\left(\frac{\xi+d}{2}\right).
 \tag{E4.1}
\]

For real `a,b`, define

\[
 \boxed{\;
 {\cal A}_\Phi(a,b)
 =
 \frac12\int_{|a+b|}^{\infty}
 \xi H_\xi(a-b)\,d\xi.
 \;}
 \tag{E4.2}
\]

The theta tail makes this integral absolutely convergent.  If `a+b>=0`,
the change of variable `xi=a+b+2r` gives

\[
 \boxed{\;
 {\cal A}_\Phi(a,b)
 =
 \int_0^\infty
 (a+b+2r)\Phi(a+r)\Phi(b+r)\,dr.
 \;}
 \tag{E4.3}
\]

For `a+b<0`, evenness gives

\[
 {\cal A}_\Phi(a,b)={\cal A}_\Phi(-a,-b).
 \tag{E4.4}
\]

In the open half-planes `a+b>0` and `a+b<0`, differentiation under the
integral gives the transport equation

\[
 (\partial_a+\partial_b){\cal A}_\Phi(a,b)
 =-(a+b)\Phi(a)\Phi(b).
 \tag{E4.5}
\]

The exact double Fourier--Laplace transform is

\[
 \boxed{\;
 {\cal B}_X(z,w)
 =
 \iint_{\mathbb R^2}
 e^{iza}e^{-i\bar w b}
 {\cal A}_\Phi(a,b)\,da\,db.
 \;}
 \tag{E4.6}
\]

Proof: multiply (E4.5) by the exponential and integrate by parts.  The
left side transforms to `i(bar(w)-z)` times the transform of
`A_Phi`.  The right side transforms to

\[
 i\bigl(X'(z)X(\bar w)-X(z)X'(\bar w)\bigr).
\]

Division gives (E4.6).  Boundary terms vanish by the superexponential theta
tail.  The same identity holds on the natural Schwartz test space without
any restriction on the imaginary parts of `z,w`.

Fourier transformation is unitary and has dense exponential test families.
Therefore, in quadratic-form sense,

\[
 \boxed{\quad
 {\cal A}_\Phi\succeq0
 \iff {\cal B}_X\succeq0
 \iff {\rm RH}.
 \quad}
 \tag{E4.7}
\]

This is the exact strengthening of positive-source theory required by
Architecture E.  Pointwise positivity of `Phi`, `H_xi`, or
`A_Phi(a,b)` is not positive definiteness of the two-variable kernel.

## 5. Identification with the omega-zero Weyl kernel

The current Weyl--Volterra programme uses

\[
 K_\omega(a,b)
 =
 \frac12\int_{|(a+b)/2|}^{\infty}
 y\cosh(2\omega y)
 \Phi\left(y+\frac{a-b}{2}\right)
 \Phi\left(y-\frac{a-b}{2}\right)\,dy.
 \tag{E5.1}
\]

At `omega=0`, the substitution `xi=2y` in (E4.2) gives the exact identity

\[
 \boxed{\qquad {\cal A}_\Phi(a,b)=4K_0(a,b).\qquad}
 \tag{E5.2}
\]

Consequently the Architecture-E source theorem is neither a new kernel nor
a uniform-in-`omega` requirement:

\[
 K_0\succeq0
 \iff {\cal A}_\Phi\succeq0
 \iff {\rm RH}.
 \tag{E5.3}
\]

The direct transform (E4.6) removes the need for a separate
`KLM -> de Branges` bridge at `omega=0`.  Uniform positivity for all
`omega` would be stronger than what this architecture needs.

## 6. Safe Euler axis is a restriction of the same kernel

Put

\[
 Y(x)=\xi_{\rm R}(1/2+x)=X(ix),\qquad
 F(x)=\frac{Y'(x)}{Y(x)}.
 \tag{E6.1}
\]

A direct derivative calculation in (E2.1) yields, for positive real `x,y`,

\[
 \boxed{\;
 {\cal B}_X(ix,iy)
 =
 Y(x)Y(y)\frac{F(x)+F(y)}{x+y}.
 \;}
 \tag{E6.2}
\]

Thus the safe Pick kernel

\[
 {\cal H}(x,y)=\frac{F(x)+F(y)}{x+y}
 \tag{E6.3}
\]

is exactly the imaginary-axis restriction of the Hermite kernel, up to a
positive diagonal congruence.  Combining (E4.6) and (E6.2),

\[
 Y(x)Y(y){\cal H}(x,y)
 =
 \iint_{\mathbb R^2}
 e^{-xa-yb}{\cal A}_\Phi(a,b)\,da\,db.
 \tag{E6.4}
\]

For `x=1/2+q`, `q>0`, the entry is Euler-safe:

\[
 \begin{aligned}
 F(1/2+q)
 ={}&
 \frac1q+\frac1{1+q}
 -\frac12\log\pi
 +\frac12\psi\left(\frac{1+q}{2}\right)\\
 &-\sum_{n\ge2}\frac{\Lambda(n)}{n^{1+q}}.
 \end{aligned}
 \tag{E6.5}
\]

The prime series is absolutely convergent.  The integrated Xi-Pick packet
proves positivity through order three; order four is the first unproved
finite order.  Formula (E6.2) shows that this is not a competing programme:
it is a one-dimensional compression of the same source theorem.

## 7. Exact Stieltjes endpoint

Set

\[
 p(t)=\frac{F(\sqrt t)}{\sqrt t},\qquad t>1/4.
 \tag{E7.1}
\]

Under RH, the centered product gives

\[
 \boxed{\;
 p(t)=2\sum_{\gamma>0}\frac{m_\gamma}{t+\gamma^2}.
 \;}
 \tag{E7.2}
\]

Thus `p` is a Stieltjes function with positive measure

\[
 d\mu(r)=2\sum_{\gamma>0}m_\gamma\,\delta_{\gamma^2}(r).
 \tag{E7.3}
\]

Conversely, suppose the known values of `p` on `(1/4,infinity)` admit a
Stieltjes continuation

\[
 p(t)=\int_0^\infty\frac{d\mu(r)}{t+r},
 \qquad \mu\ge0.
 \tag{E7.4}
\]

Then, for `Re x>0`,

\[
 \widetilde F(x)=xp(x^2)
 =
 \frac12\int_0^\infty
 \left(
 \frac1{x-i\sqrt r}+\frac1{x+i\sqrt r}
 \right)d\mu(r)
 \tag{E7.5}
\]

is analytic and has nonnegative real part.  It agrees with `Y'/Y` on
`x>1/2`, hence by the identity theorem is its analytic continuation to the
right half-plane.  Therefore `Y` has no zero there.  Evenness and
conjugation symmetry put every zero of `Y` on the imaginary axis, which is
RH.

Hence

\[
 \boxed{\quad
 {\rm RH}
 \iff p(t)=F(\sqrt t)/\sqrt t
 \hbox{ is a Stieltjes function}.
 \quad}
 \tag{E7.6}
\]

The Stieltjes measure gives a two-channel Gram factorization of the safe
kernel:

\[
 \begin{aligned}
 {\cal H}(x,y)
 &=
 \int_0^\infty
 \frac{r+xy}{(x^2+r)(y^2+r)}\,d\mu(r)\\
 &=
 \int_0^\infty
 \left[
 \frac{\sqrt r}{x^2+r}\frac{\sqrt r}{y^2+r}
 +
 \frac{x}{x^2+r}\frac{y}{y^2+r}
 \right]d\mu(r).
 \end{aligned}
 \tag{E7.7}
\]

Constructing this positive measure directly from the theta/prime source,
rather than from the unknown zeros, would complete the architecture.

## 8. Explicit prime-shift accretivity formulation

Let `e_x(t)=exp(-xt)` on `L^2(0,infinity)` and let

\[
 A_0=-\frac{d}{dt},\qquad A_0e_x=xe_x
 \tag{E8.1}
\]

on the finite exponential span.  Define `T=F(A_0)` there.  The Euler formula
(E6.5) gives the exact operator expression

\[
 \boxed{
 \begin{aligned}
 T={}&
 (A_0+\tfrac12)^{-1}
 +(A_0-\tfrac12)^{-1}
 -\tfrac12\log\pi\\
 &+\tfrac12\psi\left(\frac{A_0+\tfrac12}{2}\right)
 -\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
   e^{-(\log n)A_0}.
 \end{aligned}}
 \tag{E8.2}
\]

For every finite exponential polynomial
`g=sum_j c_j e_{x_j}`, `x_j>1/2`,

\[
 2\Re\langle Tg,g\rangle
 =
 \sum_{i,j}\bar c_i c_j
 \frac{F(x_i)+F(x_j)}{x_i+x_j}.
 \tag{E8.3}
\]

Therefore

\[
 \boxed{\quad
 {\rm RH}
 \iff
 2\Re\langle Tg,g\rangle\ge0
 \quad\hbox{for every finite exponential polynomial }g.
 \quad}
 \tag{E8.4}
\]

The last series in (E8.2) consists of literal translation-semigroup
operators with prime-power labels.  This is the exact arithmetic theorem
to prove.  Bounding the prime translations after a nonorthogonal quotient,
ratio mask, or gauge inversion is not source-faithful; the barriers on
PR #770 show why those shortcuts can lose a power.

## 9. Volterra multiplier shortcut: exact gap

A proposed continuum route introduces the scalar multiplier

\[
 \kappa(r)=\frac{1-r}{1+r},\qquad r\ge0,
 \tag{E9.1}
\]

so that `|kappa(r)|<=1`, and then compresses multiplication by `kappa`
between a lifting map `E` and an integration map `C`.  The asserted
implication

\[
 \|K\|\le1,\quad CE=I
 \quad\Longrightarrow\quad
 \|CKE\|\le1
 \tag{E9.2}
\]

is false without compatibility of `C` with the norm in which `K` is a
contraction.

An exact two-dimensional counterexample is

\[
 C=\begin{pmatrix}M&0\\0&1\end{pmatrix},\qquad
 K=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 E=C^{-1},\qquad M>1.
 \tag{E9.3}
\]

Then `CE=I` and `||K||=1`, but

\[
 CKE=\begin{pmatrix}0&M\\M^{-1}&0\end{pmatrix},
 \qquad \|CKE\|\ge M>1.
 \tag{E9.4}
\]

Kernel/fibre orthogonality is vacuous here because `C` is invertible, so it
cannot repair the inference.  The correct needed inequality is the weighted
contraction

\[
 E^*K^*C^*CKE\le E^*C^*CE.
 \tag{E9.5}
\]

In the actual lifted variables, for two source ratios `r,q`,

\[
 \boxed{\;
 1-\kappa(r)\kappa(q)
 =
 \frac{2(r+q)}{(1+r)(1+q)}.
 \;}
 \tag{E9.6}
\]

The lifted `plus` factors contribute `(1+r)(1+q)`.  Thus the defect in the
desired weighted contraction is exactly the original signed factor
`2(r+q)`, i.e. the source/Hermite quadratic form.  Proving (E9.5) therefore
does not follow from pointwise `|kappa|<=1`; after expansion it is the target
(E4.7) itself.

This does not refute a future source-compatible Volterra proof.  It states
the missing theorem precisely: one must prove that the selected lift is
contractive in the compressed positive metric, or exhibit a genuine
intertwining/commutation that makes (E9.5) automatic.  A pointwise scalar
bound before non-isometric integration is insufficient.

## 10. Relation to the first-Hermite frontier

The repository already has a separate exact Weil-square criterion

\[
 {\cal M}(q,x)
 =
 \sum_\rho m_\rho(\gamma_\rho-x)^2
 e^{-q(\gamma_\rho-x)^2}\ge0
 \quad(q>0,\ x\in\mathbb R),
 \tag{E10.1}
\]

equivalent to RH.  Its prime-side formula is positive in the proved wedge

\[
 q\le(4-\epsilon)\log\log(2+|x|),
 \tag{E10.2}
\]

while the phase-blind argument stops at the constant-four boundary and
the prime-power saddle `n about (log |x|)^4`.  That unresolved signed
cancellation is another compression of the same negative-square defect.
It is not discharged by (E9.1).

Architecture E therefore has two exact arithmetic fronts:

1. prove the all-order accretivity (E8.4), beginning with the four-node
   Schur complement;
2. prove the phase-sensitive first-Hermite inequality at the constant-four
   frontier.

Either route must retain the signed prime structure rather than replacing it
with an absolute envelope.

## 11. Closed arrows and single remaining theorem

The following arrows are now exact:

\[
 \begin{array}{c}
 {\cal A}_\Phi=4K_0\\
 \Updownarrow\\
 {\cal B}_X\succeq0\\
 \Updownarrow\\
 \Theta_\lambda\hbox{ has zero negative squares}\\
 \Updownarrow\\
 {\cal H}(x,y)\succeq0\hbox{ on every finite safe packet}\\
 \Updownarrow\\
 p(t)\hbox{ is Stieltjes}\\
 \Updownarrow\\
 {\rm RH}.
 \end{array}
 \tag{E11.1}
\]

The one remaining theorem can be stated in any of four exactly equivalent
forms:

\[
 \boxed{
 \begin{array}{ll}
 {\rm (S)} & {\cal A}_\Phi\succeq0,\\
 {\rm (W)} & K_0\succeq0,\\
 {\rm (P)} & T+T^*\succeq0\hbox{ on the exponential core},\\
 {\rm (St)}& p(t)\hbox{ admits a positive Stieltjes measure}.
 \end{array}}
 \tag{E11.2}
\]

Proving any line from the actual theta/prime source without importing the
unknown zero locations completes Architecture E and proves RH.  This packet
does not prove that final line.

## 12. Finite exact checks and scope

The companion stdlib checker verifies, over exact rational/Gaussian-rational
arithmetic:

- the companion congruence algebra (E2.2), with the common factor `pi`
  suppressed;
- the Stieltjes two-channel algebra (E7.7);
- the factor four in (E5.2);
- the multiplier defect identity (E9.6);
- the counterexample (E9.3)--(E9.4).

These checks authenticate bounded algebra only.  They do not certify the
entire-function product, Fourier inversion, positivity, a continuum
operator norm, or RH.
