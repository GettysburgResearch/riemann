# A positive Fourier source with positive heat and every scalar shifted moment

Status: complete proposed analytic countermodel, extending the frozen cofinal
obstruction without modifying its bytes. No actual-Xi counterexample.
Scope: a qualitative even strictly positive Fourier source of order at most
one; a complete vertical zero strip; arbitrarily long unchanged real-root
census; positive complete heat trace at every time and every scalar shifted
moment at every order and nonnegative shift. Off-real zeros nevertheless
remain. No literal theta arithmetic or Euler identity is asserted.
Exact dependencies: the complete Bessel-source spectral and simplicity proof
in [COFINAL_MOMENT_OBSTRUCTION.md](COFINAL_MOMENT_OBSTRUCTION.md), SHA256
`7588200870a048a52a9da84cb884e3062808d0e36f9b25a978d449340b3e8d35`;
the elementary Rayleigh–Ritz/min–max principle for a selfadjoint half-line
Schrodinger operator; and complete series/Laplace arguments supplied below.
What was actually run: analytic derivation, no native numerical experiment.
Smallest remaining gap for actual RH: an identity or inequality specific to
the literal actual theta/prime source that excludes this qualitative model.

## PF1. An explicit spectral majorant for the real Bessel head

Fix a>0. The even entire source

\[
 G_a(z)=\int_0^\infty e^{-a\cosh u}\cos(zu)\,du=K_{iz}(a)
 \tag{PF1}
\]

has only simple real zeros. The frozen parent proof identifies its positive
zeros `gamma_n` with the eigenvalues `gamma_n^2` of

\[
 L_a=-\frac{d^2}{du^2}+a^2e^{2u}
 \quad (u>0),\qquad y(0)=0,
 \tag{PF2}
\]

with the square-integrable condition at infinity. The confining potential
gives a positive discrete spectrum, enumerated increasingly with multiplicity.
Every eigenvalue is greater than a^2. The Dirichlet eigencondition is exactly
`K_(i gamma)(a)=0`; the frozen energy and Green-identity argument establishes
the correspondence and simple zeros.

Fix a finite length ell>0. Extend the first n Dirichlet sine modes on
`[0,ell]` by zero to the half-line. They belong to the half-line quadratic
form domain: the value at ell is zero, so extension has an L2 weak derivative
and the potential integral has compact support. On their n-dimensional span,

\[
 \int_0^\infty|y'|^2\,du\le(\pi n/\ell)^2\|y\|_2^2,
 \qquad
 \int_0^\infty a^2e^{2u}|y|^2\,du
                       \le a^2e^{2\ell}\|y\|_2^2.
\]

Min–max therefore gives the COMPLETE spectral inequality

\[
 \gamma_n^2\le(\pi n/\ell)^2+a^2e^{2\ell}
             \le B^2n^2,
 \qquad B^2=(\pi/\ell)^2+a^2e^{2\ell},\qquad n\ge1.
 \tag{PF3}
\]

This is a variational upper bound on every real eigenvalue, not a numerical
census or an assumption about regular root spacing.

## PF2. Add arbitrarily late off-real zeros and retain the Fourier source

Fix A>0 and any prescribed finite census height H0. Choose X so large that

\[
                 X>H_0,\qquad X^2>4B^2+A^2,
 \qquad L=\pi/X.
 \tag{PF4}
\]

Define the normalized even entire source

\[
 F_X(z)=\frac{G_a(z)}{G_a(0)}
          \frac{\cosh(LA)+\cos(Lz)}{\cosh(LA)+1}.
 \tag{PF5}
\]

The cosine factor is strictly positive on the real axis and has exactly the
simple zeros

\[
        z=(2j+1)X\pm iA,\qquad j\in\mathbb Z.
 \tag{PF6}
\]

It leaves every real zero of G_a unchanged and simple. All added off-real
zeros lie beyond H0 in absolute real coordinate. Thus the entire simple real
census below H0 is exactly the Bessel census, while the complete zero source
still contains infinitely many off-real roots. There are no imaginary-axis
zeros, and all roots lie in the complete strip `|Im z|<=A`.

As established in the parent proof, `g(u)=exp(-a cosh u)/2` is a strictly
positive even superexponentially decaying Fourier kernel for G_a. Multiplying
by the cosine factor replaces it, up to a positive normalization, by

\[
 \cosh(LA)g(u)+\frac{g(u-L)+g(u+L)}2,
 \tag{PF7}
\]

still strictly positive, even and superexponentially decaying. Both factors
have entire order at most one; F_X retains that order bound and its complete
paired product with summable inverse-square zeros. These are qualitative
source properties, not the literal xi theta identities.

## PF3. The entire complex heat trace is dominated at every positive time

Write the complete heat traces, using positive-real-part representatives and
all multiplicities, as

\[
 K_G(u)=\sum_{n\ge1}e^{-\gamma_n^2u},\qquad
 K_C(u)=2\sum_{j\ge0}
       e^{-((2j+1)^2X^2-A^2)u}\cos(2(2j+1)XA u),
 \quad K_F(u)=K_G(u)+K_C(u).
 \tag{PF8}
\]

These series converge absolutely and normally on compact positive-time
intervals. For the cosine lattice this is a Gaussian integer sum. For G_a,
the complete paired-product summability bounds the Gaussian by a constant
times the inverse-square weights. No real or complex zero is omitted.

For each j>=0, condition PF4 gives

\[
 (2j+1)^2X^2-A^2>B^2(2j+2)^2.
 \tag{PF9}
\]

Indeed `2j+2<=2(2j+1)` and
`(2j+1)^2 A^2-A^2>=0`, with strictness from PF4. Applying PF3 twice,

\[
 e^{-\gamma_{2j+1}^2u}+e^{-\gamma_{2j+2}^2u}
       >2e^{-((2j+1)^2X^2-A^2)u}\qquad(u>0).
 \tag{PF10}
\]

Every Bessel mode appears in exactly one such pair. The complete cosine
pair contribution has absolute value at most the right-hand side of PF10.
Consequently the normally convergent series can be grouped in these pairs,
and every grouped term of K_F is strictly positive. In particular,

\[
                        K_F(u)>0\qquad\text{for every }u>0.
 \tag{PF11}
\]

One pair already provides strictness; summing the rest cannot reduce it.
This is a complete all-time inequality, not a finite-time sample or a
truncated heat approximation. The large-X choice works simultaneously for
all positive heat times, including arbitrarily small times.

## PF4. Every scalar shifted moment is positive, at every order and shift

All complete nodes have `Re(rho^2)>0`: for Bessel roots this follows from
reality and positivity, and for lattice roots it follows from `X^2>A^2`.
For every X0>=0 and integer k>=1, therefore,

\[
 \sum_{\operatorname{Re}\rho>0}
       m_\rho\int_0^\infty u^{k-1}
                |e^{-(X_0+\rho^2)u}|\,du
  =(k-1)!\sum_\rho\frac{m_\rho}
                          {(X_0+\operatorname{Re}\rho^2)^k}<\infty.
 \tag{PF12}
\]

The finite head has positive denominators; outside it they are comparable
to `|rho|^(2k)`, paid by complete inverse-square summability. Absolute
Fubini and the elementary Gamma integral now give

\[
 C_k(t)=\sum_\rho m_\rho(\rho^2+t^2)^{-k}
     =\frac1{(k-1)!}\int_0^\infty u^{k-1}e^{-t^2u}K_F(u)\,du>0
 \quad\text{for every integer }k\ge1\text{ and every }t\ge0.
 \tag{PF13}
\]

Conjugate grouping makes the complete sum real. Thus ALL unshifted scalar
moments and ALL scalar moments at ALL nonnegative shifts are strictly
positive despite the off-real lattice. The complete source logarithmic
derivative is completely monotone as a function of X0>0; its normalized
integral logarithm is a Bernstein function. This remains weaker than
complete monotonicity of K_F itself. By the complete noncanceling-pole
criterion, K_F cannot be completely monotone: some finite higher derivative
has a strict negative sign. Equivalently, some finite complete Hankel form
or mixed Hausdorff inequality must fail, as the companion criteria prove.

The countermodel simultaneously satisfies strictly positive Fourier source,
order at most one, complete fixed strip, absence of imaginary-axis roots,
arbitrarily long unchanged simple real census, complete all-time heat
positivity, and complete scalar shifted positivity at every order and shift.
These premises cannot force a cofinal real census or RH location. The actual
theta/Euler arithmetic, complete mixed inequalities, or another stronger
source condition must do additional work. No failure of those literal xi
conditions is asserted here.
