# A complete Gamma/prime heat trace and an exact real-spectrum criterion

Status: proposed complete actual-source identity and global equivalence.
Scope: actual Xi, the complete classical zero strip, every fixed positive
heat time and derivative order. A finite primitive negative test is possible
in principle. No complete monotonicity or negative test for actual Xi is
proved here, and no additional numerical experiment is claimed.
Exact dependencies: actual completed zeta and its functional equation,
the complete even order-one product, the Euler logarithmic derivative in
Re s>1, the classical digamma integral, the Gaussian Laplace identity, and
the explicitly imported Bernstein–Widder positive Laplace representation
theorem. The identities below preserve every source zero and prime tail.
Smallest remaining gap: prove complete monotonicity of the literal full
Gamma/prime expression, or authenticate a strict negative derivative test.

## HT1. Complete spectral heat trace without a real-zero assumption

Write every positive-half-plane zero of `Xi(z)=xi(1/2+i*z)` as rho=gamma+i*beta,
retaining its conjugate separately and retaining multiplicity m_rho. The
classical strip has |beta|<=A=1/2. Positive theta excludes imaginary-axis
zeros, and the complete paired product gives
`sum m_rho/|rho|^2<infinity`. Define, for u>0,

\[
 K(u)=\sum_{\operatorname{Re}\rho>0}m_\rho e^{-\rho^2u}.
 \tag{HT1}
\]

This is a COMPLETE real trace. For u in a compact subinterval of (0,infinity),
every derivative series converges absolutely and uniformly: each fixed
polynomial in |rho| times `exp(-gamma^2*u+u/4)` is eventually bounded by a
constant times |rho|^(-2). No unknown complex block is omitted.

For real X>1/4 the whole-source logarithmic derivative is

\[
 f(X)=\frac{d}{dX}\log\Xi(i\sqrt X)
      =\sum_{\operatorname{Re}\rho>0}\frac{m_\rho}{X+\rho^2}
      =\int_0^\infty e^{-Xu}K(u)\,du.
 \tag{HT2}
\]

The product proves the middle identity. To justify the last identity even
without RH, each denominator has `X+Re(rho^2)>=X-1/4>0`. Also

\[
 \sum m_\rho\int_0^\infty
         |e^{-(X+\rho^2)u}|\,du
 =\sum\frac{m_\rho}{X+\operatorname{Re}\rho^2}<\infty.
\]

Outside a finite set these terms are bounded by a constant times |rho|^-2.
Fubini therefore gives the complete Laplace identity. In particular K is
locally integrable at zero; its trace definition is not merely a formal
sum over numerically known zeros.

## HT2. Literal actual-source formula

Let v=sqrt X>1/2 and s=1/2+v. The completed-zeta formula gives

\[
 f(X)=\frac{1}{X-1/4}
       +\frac{\psi(v/2+1/4)-\log\pi}{4v}
       -\frac{1}{2v}\sum_{n\ge2}\Lambda(n)n^{-1/2}e^{-v\log n}.
 \tag{HT3}
\]

Here psi=Gamma'/Gamma and Lambda is the literal von Mangoldt function.
The first term combines the derivatives of s and s-1 exactly. The Euler
sum is absolutely convergent because s>1. The elementary Gaussian identity

\[
 \int_0^\infty e^{-Xu}\frac{e^{-a^2/(4u)}}{\sqrt{\pi u}}\,du
                  =\frac{e^{-a\sqrt X}}{\sqrt X},\qquad a\ge0,
 \tag{HT4}
\]

and the digamma identity, for positive z,

\[
 \psi(z)=-\gamma_E+
       \int_0^\infty\frac{e^{-q}-e^{-zq}}{1-e^{-q}}\,dq,
 \tag{HT5}
\]

give the exact full-source heat expression

\[
 \begin{split}
 K(u)={}&e^{u/4}\
 &+\frac{1}{4\sqrt{\pi u}}\left[-\gamma_E-\log\pi+
       \int_0^\infty
       \frac{e^{-q}-e^{-q/4}e^{-q^2/(16u)}}{1-e^{-q}}\,dq\right]\
 &-\frac{1}{2\sqrt{\pi u}}
       \sum_{n\ge2}\Lambda(n)n^{-1/2}e^{-(\log n)^2/(4u)}.
 \end{split}
 \tag{HT6}
\]

This is a transformed complete explicit formula, not a claim of a new
zero-count theorem. The prime sum converges absolutely for every fixed u>0:
on `exp(j)<=n<exp(j+1)`, its absolute contribution is bounded by
`e*(j+1)*exp(j/2-j^2/(4u))`. This is summable. On compact positive u ranges
the same argument permits every fixed derivative.

The integral in HT6 is also absolutely convergent. Near q=0 its numerator
is `-3q/4+O(q^2)`, and at infinity both terms decay. The joint absolute
integrability needed for its Laplace transform follows by splitting

```text
|exp(-q)-exp(-q/4)exp(-q^2/(16u))|
 <= |exp(-q)-exp(-q/4)|
    +exp(-q/4)*min(1,q^2/(16u)).
```

For 0<q<1 the integral in u against `u^(-1/2)exp(-Xu)` of the second
minimum is O(q): substitute u=q^2*w and bound
`integral_0^infinity w^(-1/2)min(1,1/(16w))dw`. Division by
`1-exp(-q)` therefore leaves an integrable q bound. The remaining q range
has exponential bounds. HT4 and Fubini then give the Gamma term of HT3.
For the prime term Tonelli and HT4 give the convergent Euler sum directly.

Thus HT6 and HT1 have identical Laplace transforms for X>1/4. Both are
continuous at every positive u and have the required exponential growth
bounds. For HT6 the displayed block estimate is a polynomial in u times
`exp(u/4)` for u>=1; the integral grows at most polynomially. For HT1,
`|K(u)|<=exp(u/4)*sum m*exp(-gamma^2)` for u>=1. Uniqueness of the Laplace
transform proves the pointwise equality. Equivalently this last uniqueness
statement may be applied after multiplying by `exp(-X0*u)`, X0>1/4,
to two absolutely integrable functions.

## HT3. Complete monotonicity is equivalent to RH

The exact criterion is

\[
 (-1)^r K^{(r)}(u)\ge0
       \quad\text{for EVERY integer }r\ge0\text{ and EVERY real }u>0.
 \tag{HT7}
\]

For actual Xi, HT7 holds if and only if every zero is real, namely RH.
Multiplicities are allowed; no simplicity conclusion is included.

If RH holds, HT1 is a positive sum of `exp(-gamma^2*u)`, and every HT7
follows by the already justified derivative convergence.

For the converse, the explicitly imported Bernstein–Widder theorem states
that a smooth function on (0,infinity) satisfying every HT7 has a positive
measure nu on [0,infinity) with
`K(u)=integral exp(-a*u)dnu(a)`, finite for every u>0. The measure may have
infinite total mass. Tonelli applied to HT2 gives, for X>1/4,

\[
 f(X)=\int_{[0,\infty)}\frac{d\nu(a)}{X+a}.
 \tag{HT8}
\]

This integral is finite, so `integral (1+a)^(-1)dnu(a)<infinity`. It defines
an analytic function on the slit plane `C\(-infinity,0]`. The complete
source meromorphic function `sum m/(X+rho^2)` converges normally away from
its poles; each pole has positive integer residue m. The map rho->rho^2 is
injective on the positive real half-plane, so distinct source poles do not
cancel. Identity continuation from X>1/4 makes HT8 equal to that complete
meromorphic source off its poles. If rho were off-real, `-rho^2` would be
a nonreal pole in the slit plane, contradicting analyticity of HT8 there.
Every rho is therefore real.

The sole representation import in this direction is the classical positive
Laplace representation theorem of Bernstein–Widder (for example D. V.
Widder, *The Laplace Transform*, Princeton University Press, 1941). It is
a general analytic theorem, not an imported zero-location result for Xi.

If an off-real zero exists, some HT7 must fail strictly at a finite r and
u. Derivative continuity supplies a rational positive u with the same
strict sign. Hence exact finite native enclosures of HT6 and its derivatives,
with complete integral and prime tails, give a possible refutation search.
No actual-Xi strict negative test is supplied in this packet.

## HT4. A complete finite derivative tail envelope

For a fixed integer r>=0 define the rational polynomial P_r by

\[
 P_0(z)=1,\qquad
 P_{r+1}(z)=(z-r-1/2)P_r(z)-zP'_r(z).
 \tag{HT9}
\]

Direct differentiation gives

\[
 \frac{d^r}{du^r}\left[u^{-1/2}e^{-a^2/(4u)}\right]
       =u^{-r-1/2}e^{-a^2/(4u)}P_r(a^2/(4u)).
 \tag{HT10}
\]

This yields every derivative of the prime term of HT6. For the Gamma
integral it gives the combined numerator
`P_r(0)*exp(-q)-exp(-q/4)*exp(-q^2/(16u))*P_r(q^2/(16u))`.
That numerator retains its cancellation at q=0. The constant
`-gamma_E-log pi` is multiplied by P_r(0). Differentiation is justified
uniformly on each compact positive u interval by the same Gaussian bounds.

Here is one explicit complete prime-tail bound. Write
`P_r(z)=sum_(j=0)^r p_j z^j`, fix `0<u_-<=u<=u_+`, and choose an integer
N>=2 with Q=log N satisfying

\[
                  Q\ge\max\{2(2r+1),4u_+\}.
 \tag{HT11}
\]

The absolute remaining rth derivative of the prime term is at most

\[
 \frac{u_-^{-r-1/2}}{2\sqrt\pi}
 \sum_{j=0}^r\frac{|p_j|}{(4u_-)^j}
      \frac{(8u_+)^{j+1}}2
      \Gamma\left(j+1,\frac{Q^2}{8u_+}\right).
 \tag{HT12}
\]

To prove this, use Lambda(n)<=log n and bound the exponential and polynomial
at u_+,u_- respectively. For j<=r the function
`(log x)^(2j+1)*x^(-1/2)*exp(-(log x)^2/(4u_+))` is decreasing for x>=N:
its logarithmic derivative in q=log x is
`(2j+1)/q-1/2-q/(2u_+)<=-q/(2u_+)<0` under HT11. Its sum over n>N is
therefore at most the integral from N to infinity. In logarithmic
coordinates this is

\[
 \int_Q^\infty q^{2j+1}e^{q/2-q^2/(4u_+)}dq
       \le\int_Q^\infty q^{2j+1}e^{-q^2/(8u_+)}dq,
\]

because Q>=4u_+. Substitution gives the incomplete Gamma factor in HT12.
For the integer index used here it is elementary:
`Gamma(j+1,z)=j!*exp(-z)*sum_(ell=0)^j z^ell/ell!`. The upper endpoint
can therefore be enclosed by ordinary convergent directed elementary
arithmetic. A finite prime sum must authenticate the actual prime powers
and their von Mangoldt weights. HT12 is an exact sufficient bound, with
no efficiency claim for large time or derivative order.

The Gamma integral likewise needs a complete directed quadrature and tail;
HT10 describes its cancellation-preserving integrand. This document does
not supply a finite quadrature implementation or an accepted derivative
certificate. Dropping either tail would invalidate the primitive test.

## HT5. Heat-trace positivity alone still allows off-real zeros

For a distinct finite polynomial source with positive-half-plane zeros
`1, 2+i/2, 2-i/2`, its complete heat trace is

\[
 K_*(u)=e^{-u}+2e^{-15u/4}\cos(2u)>0\qquad(u>0).
 \tag{HT13}
\]

For 0<u<=1/2, cos(2u)>0 because 2u<=1<pi/2. For u>=1/2,
`K_*(u)>=exp(-u)*(1-2exp(-11u/4))>0`, since
`exp(11/8)>1+11/8>2`. Thus positivity holds at EVERY positive heat time,
not only at the finitely tested times. Its logarithmic derivative is the
Laplace transform of this positive K_*, so it is completely monotone at
every X>0: all scalar shifted moments at all such shifts are positive.
Its integral logarithm is consequently a Bernstein function.

Nevertheless the source has the displayed off-real zeros. K_* itself must
fail a higher complete-monotonicity inequality by HT3's same pole argument.
This polynomial is not claimed to have a positive Fourier theta kernel;
the companion positive-kernel Bessel/cosine model supplies the separate
qualitative theta obstruction. Positivity of f, complete monotonicity of f,
and positivity of K must therefore be distinguished from complete
monotonicity of K, which is the universal real-spectrum criterion.

The full actual Gamma/prime expression in HT6 may be used to study the
criterion without assuming a complete real-zero census. The universal
sign theorem for that exact expression remains open.
