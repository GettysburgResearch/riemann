# A cusp obstruction to the unweighted signed level projector

Status: exact obstruction to one proposed estimate, 23 October 2026. It does not rule out a correctly centered paired projector or a different spectral construction.

Let E(w,s) be the ordinary Gaussian Eisenstein series with incoming term y^s and outgoing coefficient phi(s)y^(2-s). Let E_(d^2) restrict its primitive bottom row by d^2 dividing the lower-left entry. The exact identity in PR1016, `QUARTIC_SPECTRAL_INTERFACE.md`, section 3, at commit `7ea66551190f291101b0dd44fb1fc9b3331c560d`, is

\[
 E_{d^2}(w,s)=(Nd)^{-s}\prod_{p\mid d}(1-(Np)^{-s})^{-1}
       \sum_{e\mid d}\mu(e)(Ne)^{-s/2}E(T_{d^2/e}w,s), \tag{L1}
\]

for squarefree d, where T_r(z,y)=(rz,|r|y). Work away from a fixed bad set, including the prime above 2. Fix real 1/2<u<1 at which E and phi are regular and phi(u) is nonzero. These exclusions are discrete; the argument applies to every remaining u.

The outgoing coefficient of L1 is exactly

\[
 \phi(u)(Nd)^{2-2u}\prod_{p\mid d}{1-(Np)^{-1}\over1-(Np)^{-u}}. \tag{L2}
\]

Indeed the e summand contributes (Nd)^(2-2u)(Ne)^-1, before the finite Euler correction. The incoming coefficient is one, as required by the original normalization.

Define the unweighted signed sum

\[
 F_R(w,u)=\sum_{Nd\le R}\mu(d)E_{d^2}(w,u).
\]

Its outgoing coefficient is phi(u) A_u(R), where

\[
 A_u(R)=\sum_{Nd\le R}\mu(d)(Nd)^{2-2u}
             \prod_{p\mid d}f_u(Np),\qquad
 f_u(q)={1-q^{-1}\over1-q^{-u}}. \tag{L3}
\]

## 1. Exact reciprocal factor and a surviving zero

For large Re(s), the coefficient Dirichlet series equals

\[
 \mathcal A_u(s)=\sum_d {\mu(d)(Nd)^{2-2u}\prod_{p\mid d}f_u(Np)\over(Nd)^s}
 =\prod_{p\notin S}(1-f_u(Np)(Np)^{-z})
 ={E_u(z)\over\zeta_F^S(z)},\qquad z=s+2u-2, \tag{L4}
\]

where

\[
 E_u(z)=\prod_{p\notin S}{1-f_u(Np)(Np)^{-z}\over1-(Np)^{-z}}. \tag{L5}
\]

Because f_u(q)=1+O_u(q^-u), this product converges normally on compact subsets of Re(z)>1-u. The denominators have no zeros there. At any point with Re(z)>=1/2, its numerator local factors are nonzero: for u>1/2 and odd Gaussian q>=5,

\[
 f_u(q)<{1-q^{-1}\over1-q^{-1/2}}=1+q^{-1/2}<q^{1/2}.
\]

Thus |f_u(q)q^-z|<1. Absolute convergence then makes E_u(z) nonzero on Re(z)>=1/2. Removing finitely many bad Euler factors does not create a zero or pole in this region, since their possible zeros have real part zero.

Choose any nontrivial zero rho of the Gaussian Dedekind zeta function with Re(rho)>=1/2. Such a zero exists; for example the ordinary zeta function has nontrivial zeros and its functional equation pairs them across 1/2, while zeta_F(s)=zeta(s)L(s,chi_-4) cannot cancel a zeta zero in the critical strip. No RH premise is needed. The standard zero facts are recorded in [DLMF section 25.10](https://dlmf.nist.gov/25.10).

Equations L4--L5 then give a genuine pole at

\[
 s_0=\rho+2-2u,\qquad \Re s_0\ge5/2-2u. \tag{L6}
\]

There is no finite Euler cancellation of this pole: L5 was shown nonzero at rho. Its multiplicity is the multiplicity of the zeta zero.

## 2. What growth is impossible

If A_u(R)=O(R^gamma) for some gamma<5/2-2u, partial summation would represent its Dirichlet series as

\[
 \mathcal A_u(s)=s\int_1^\infty A_u(x)x^{-s-1}\,dx,
\]

normally on Re(s)>gamma. This would be a holomorphic continuation across s0, contradicting L6. Therefore no such bound is possible. The same conclusion holds for a bound O_epsilon(R^(gamma+epsilon)) when gamma<5/2-2u, by choosing epsilon below the gap.

In particular, the proposed level exponent gamma=(1-u)/2 is impossible for this unweighted projector throughout 1/2<u<1.

Suppose one sought the uniform pointwise estimate

\[
 |F_R(w,u)|\ll R^\gamma Y(w)^{2-u}, \tag{L7}
\]

with a constant independent of R and w and the usual invariant height Y. At the infinity cusp w=(0,y), divide by y^(2-u) and let y tend to infinity for fixed R. The incoming term tends to zero because 2u-2<0; the nonconstant Fourier terms tend to zero; and Y(0,y)=y for sufficiently large y. L7 would imply |phi(u)A_u(R)|<<R^gamma, contradicting the preceding paragraph for gamma<5/2-2u. This rules out L7 as a shortcut to a small level cost.

## 3. Centering does not follow from this computation

One can formally subtract the outgoing constant coefficient phi(u)A_u(R)y^(2-u) in a cusp truncation, and also subtract the incoming coefficient if desired. That produces a different function, and a global automorphic realization requires compatible cutoffs and all cusps. It is not automatically the finite arithmetic diagonal in the inverse moment.

In particular, a paired sieve vector may contain extra density factors, lcm weights, or cross terms absent from F_R. This obstruction does not estimate or disprove that paired object. To use such a construction one must derive its exact finite-level kernel and identify its constant-term subtraction with the original arithmetic diagonal. This note supplies neither identification. It shows why diagonalizing only the unweighted sum of ordinary E_(d^2) cannot deliver the proposed small exponent.
