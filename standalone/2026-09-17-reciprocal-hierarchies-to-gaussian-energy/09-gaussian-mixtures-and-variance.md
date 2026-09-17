# 09. Exact Gaussian mixtures, Fourier corrections, and a fixed sparse criterion

**Status:** established Pólya–Gamma input plus proposed exact source identities and complete component arguments. The final native Gaussian-energy upper bound remains OPEN. This chapter supersedes the short-interval turn's inconsistent normalizations and unsupported signed-kernel comparisons.

## 1. Correct additive Gaussian normalization

For A_X(theta)=sum_(X<n<=2X)mu(n)e^(2 pi i n theta) and
\[
S_{X,H}(x)=\sum_{X<n\le2X}\mu(n)e^{-(n-x)^2/(2H^2)},
\]
Fourier transform with e^(-2 pi i x xi) gives EXACTLY
\[
\int_{\mathbb R}|S_{X,H}(x)|^2dx
=2\pi H^2\int_{\mathbb R}e^{-4\pi^2H^2\xi^2}|A_X(\xi)|^2d\xi.
\]
Periodizing the Gaussian gives the equivalent integral over [-1/2,1/2] with weight
\(\mathscr W_H(\theta)=\sum_{k\in\mathbb Z}e^{-4\pi^2H^2(\theta+k)^2}\).

The prefactor is H^2, not H. A target variance XH X^(o(1)) requires weighted Fourier mass <=X^(1+o(1))/H. The erroneous turn alternated between this and a weaker bound missing 1/H. Only the corrected formula is retained as valid.

Also, entrywise comparability of sech and additive Gaussian entries does not compare signed quadratic forms. In a 2-by-2 matrix with diagonal 1 and off-diagonal a, increasing a helps (1,1) but hurts (1,-1). The proposed dyadic additive-Gaussian comparison was not proved. The exact logarithmic-Gaussian identity below replaces it; it does not retroactively justify it.

## 2. A logarithmic Gaussian energy

For omega>0 define
\[
G_\omega(N)=\frac14\sum_{m,n\le N}
\frac{\mu(m)\mu(n)}{\sqrt{mn}}
\exp\left[-\frac\omega2(\log(m/n))^2\right],
\]
\[
U_{\omega,N}(u)=\sum_{n\le N}\frac{\mu(n)}{\sqrt n}
 e^{-\omega(u-\log n)^2}.
\]
Completing the square gives
\[
\boxed{G_\omega(N)=\frac14\sqrt{\frac{2\omega}{\pi}}
\int_{\mathbb R}|U_{\omega,N}(u)|^2du.}
\]
Thus G is positive and uses the literal source. Its Fourier representation is
\[
G_\omega(N)=\frac1{8\pi}\sqrt{\frac{2\pi}{\omega}}
\int_{\mathbb R}e^{-\tau^2/(2\omega)}
|P_N(1/2+i\tau)|^2d\tau.
\]
This normalization, including all factors of 2 and pi, is fixed throughout the packet.

## 3. An exact positive mixture: no arithmetic signs are randomized

Let Z_k be independent Gamma(r,rate=1) variables and
\[
\Omega_r=\frac2{\pi^2}\sum_{k\ge1}\frac{Z_k}{(2k-1)^2}.
\]
This is the Pólya–Gamma law PG(r,0), with classical construction [PG]. The cosh product gives
\[
\mathbb E e^{-\Omega_r u^2/2}
=\prod_{k\ge1}\left(1+\frac{u^2}{\pi^2(2k-1)^2}\right)^{-r}
=\operatorname{sech}^r(u/2).
\]
Applying it to a finite source proves
\[
\boxed{Q_j(N)=\mathbb E G_{\Omega_{2j+3}}(N).}
\]
Randomness is in the kernel representation only. It is not an independent-prime or random-Möbius assumption.

The shape is a convolution parameter: Omega_(r+s) is distributed as the sum of independent Omega_r and Omega_s. Its cumulants are
\[
\kappa_k(\Omega_r)=r(k-1)!(2/\pi^2)^k(1-2^{-2k})\zeta(2k).
\]
In particular E Omega_r=r/4 and Var Omega_r=r/24. The appearance of even zeta values is a feature of the smoothing law, not a constraint on the nontrivial zeros.

Chernoff bounds give
\[
\Pr(\Omega_r<r/8)\le e^{-c_-r},\quad c_-=\log\cosh1-1/4>0,
\]
\[
\Pr(\Omega_r>r/2)\le e^{-c_+r},\quad c_+=1+\log\cos1>0.
\]
Let delta_r be their sum. Nonnegative Fourier multipliers, not matrix-entry comparison, give on r/8<=omega<=r/2
\[
\tfrac12G_{r/8}(N)\le G_\omega(N)\le2G_{r/2}(N).
\]
Since 0<=G_omega(N)<=N,
\[
\boxed{\frac{1-\delta_r}{2}G_{r/8}(N)
\le Q_j(N)\le2G_{r/2}(N)+N\delta_r,\quad r=2j+3.}
\]
At j=log^4N the additive error is superpolynomially small. This is a rigorous signed-energy comparison.

## 4. Fixed-Gaussian criterion, including arbitrary sparse cutoffs

**Proposed theorem.** For EVERY fixed omega>0,
\[
\mathrm{RH}\iff G_\omega(N)\le N^{o(1)}
\]
and, more strongly,
\[
\boxed{\mathrm{RH}\iff\exists N_k\to\infty:
G_\omega(N_k)\le N_k^{o(1)}.}
\]
The sparse criterion refers to upper subpolynomial bounds. It does not assert an asymptotic equivalence to 1. No assumption of simple zeros is made.

### Direct finite Mertens recovery

An exact Gaussian integral gives
\[
M(N)=\sqrt{\omega/\pi}\,e^{-1/(16\omega)}
\int_{\mathbb R}e^{u/2}U_{\omega,N}(u)du.
\]
Split at log N+L. Cauchy–Schwarz bounds the initial part by
\(C_\omega\sqrt N e^{L/2}\sqrt{G_\omega(N)}\).
On the tail,
\[
|U_{\omega,N}(u)|\le2\sqrt N e^{-\omega(u-\log N)^2}.
\]
Take \(L=\omega^{-1}+\sqrt{6\log(2N)/\omega}\). Completing the square bounds the tail by O_omega(N^(-2)), giving
\[
|M(N)|\le C_\omega\sqrt N e^{C_\omega\sqrt{\log(2N)}}
\sqrt{G_\omega(N)}+1.
\]
The exponential factor is subpolynomial. Thus all-cutoff subpower Gaussian energy implies RH via the Mertens criterion. Conversely, under RH partial summation gives |P_N(1/2+i tau)|<<_epsilon(1+|tau|)N^epsilon; insert this in the Gaussian Fourier formula.

### Why sparse cutoffs suffice: full noncausal tail accounting

Use d, nu_N, q_N, v and T=log(N+1) from Chapter 06. Put psi(u)=exp(-omega u^2), y_N=psi*q_N=d*U_(omega,N), and y_*=psi*v. Then
\[
\|y_N\|_2\le C_\omega\sqrt{G_\omega(N)}.
\]
The bilateral Laplace transform of psi is
\(\Psi(z)=\sqrt{\pi/\omega}\exp(z^2/(4\omega))\), which never vanishes.

Suppose rho=beta+i gamma is an off-critical zero with alpha=beta-1/2>0, z_rho=alpha+i gamma. The transforms converge at this fixed point, and
\[
\mathcal Ly_N(z_\rho)=0,\qquad
\mathcal Ly_*(z_\rho)=\Psi(z_\rho)(\rho-1)/\rho^2\ne0.
\]
For any b>0, exp(-omega u^2)<=exp(b^2/(4omega))exp(bu). Combining this with the complete q_N-v tail gives
\[
|y_N(t)-y_*(t)|\le C_{\omega,b}(1+T)e^{b(t-T)+T/2}.
\]
Fix 0<c<1. Choose b>alpha with b(1-c)>1/2. In the transform of y_N-y_*, the portion t<cT tends to zero by the last bound. The other portion is at most
\[
\frac{e^{-\alpha cT}}{\sqrt{2\alpha}}
(\|y_N\|_2+\|y_*\|_2)
\]
by Cauchy–Schwarz. It must account for a fixed nonzero number, so
\[
G_\omega(N)\ge C_{\rho,c,\omega}N^{c(2\beta-1)}
\]
for every sufficiently large N. Any unbounded subpower sequence contradicts this. Functional-equation symmetry concludes the sparse criterion. This proof does not use monotonicity, regularly spaced cutoffs, or an unproved Gaussian-to-sech reverse inequality.

## 5. Long additive windows are not automatically a weaker target

For a box window let
\[
B_{X,H}(x)=\sum_{X<n\le2X,\ x<n\le x+H}\mu(n),\quad
V_\Box=\int_{\mathbb R}|B_{X,H}(x)|^2dx.
\]
Its support has length X+H and its integral is H(M(2X)-M(X)). Therefore
\[
V_\Box(X,H)\ge\frac{H^2}{X+H}|M(2X)-M(X)|^2.
\]
At H=X/log^2X, an all-X bound V_Box<=XH X^(o(1)) gives square-root Mertens increments up to logarithms and therefore RH by dyadic summation. Conversely RH gives that bound from the pointwise Mertens estimate; log losses are subpolynomial. Averaging at this nearly full-length scale is not by itself a reduction of arithmetic strength.

The earlier additive-Gaussian claim needed integration over all centers, treatment of end intervals, correct Fourier factors, and a signed-operator comparison. Those missing steps are not silently filled by this box argument.

## 6. Why logarithmic discorrelation and generic Type-II counting stop short

The current v2 of [MRSTT] was submitted originally in November 2024 and revised in January 2026. Its displayed Theorem 1.1 uses X^(theta+epsilon)<=H<=X^(1-epsilon); part (i), theta=1/3, gives H/log^A X discorrelation for mu outside a logarithmically small exceptional set. Its abstract and surrounding discussion also discuss longer-range consequences. Therefore neither the claim that H=X/log^2X literally satisfies that displayed fixed-epsilon hypothesis nor a blanket claim that the paper excludes longer H is accurate.

More importantly, arbitrary fixed log savings do not give the variance scale XH X^(o(1)). Squaring H/log^A X, paying the exceptional set, and integrating yields only XH^2/log^B X for fixed B. The gap contains a factor approximately H, not a missing constant.

One cannot repeatedly apply a bound for the vector mu to its local averages as if it were an operator contraction on an invariant space. Local averaging destroys multiplicativity and the needed uniform spectral-gap statement was not proved.

For a generic Type-II component
\[
T(\theta)=\sum_{u\sim U,v\sim V}\alpha_u\beta_v e^{2\pi iuv\theta},\quad UV\asymp X,
\]
the desired narrow-band bound <=X^(1+o(1))/H is false for arbitrary divisor-bounded coefficients. Set alpha=beta=1. On |theta|<=c/X all phases lie in a short arc, so |T|>>X and the integral is >>X. At H=X/log^2X the proposed upper scale is only log^2X X^(o(1)). Near-diagonal counting alone cannot provide it.

The actual Möbius Newton identity in Chapter 07 retains cancellations between pieces. Taking absolute values of generic pieces discards exactly those cancellations. The function-field short-interval variance analogy mentioned in the chat is a research lead, not an imported theorem for integers.

## 7. Final interface

For fixed omega=1, it is enough to prove along some unbounded sequence
\[
\int_{\mathbb R}\left|\sum_{n\le N}\frac{\mu(n)}{\sqrt n}
 e^{-(u-\log n)^2}\right|^2du\le N^{o(1)}.
\]
Everything in the passage from this bound to RH has been specified here. The bound itself has not been obtained. The Gaussian mixture and fractional shape law simplify measurement; they do not randomize or estimate the deterministic inverse source.
