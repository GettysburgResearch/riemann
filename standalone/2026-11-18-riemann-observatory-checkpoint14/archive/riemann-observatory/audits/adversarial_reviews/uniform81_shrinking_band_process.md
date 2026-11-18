# Shrinking-exponent prime band process under derivative-square zero sampling

18 November 2026. Assume RH and use the probability on the strict tail \(|\gamma|>Y\) with masses proportional to
\[
 \frac{|\zeta'(1/2+i\gamma)|^2}{1/4+\gamma^2}.
\]
Fix \(0<r_0<1\), let \(L=\log Y\), and let \(b=b(Y)>0\) satisfy \(b\to0\) and \(bL\to\infty\). On \(r_0\le r\le1\) put
\[
 X_Y(r)=\sum_{Y^{r_0b}<p\le Y^{rb}}
                 \left(\frac{\cos(\gamma\log p)}{\sqrt p}-\frac1p\right).
\]
Then \(X_Y\Rightarrow (B_{\frac12\log(r/r_0)})_{r_0\le r\le1}\) in \(D([r_0,1]),J_1\), for standard real Brownian motion \(B\). The same conclusions below give an in-principle effective conditional bounded-Lipschitz onset given effective moduli of \(b\to0\) and \(bL\to\infty\) and the audited effective aggregate input. There is a fourth-moment bound \(C h^{3/2}\) for **every** subset of reciprocal mass \(h\) in the whole band. The proof obtains this scale from two estimates. A uniform \(C h^2\) bound down to all scales is not needed, and is not asserted. [Scalar aggregate input](analytic78_shrinking_band.md) · [Independent scalar review](weighted78_shrinking_band_review.md)

## 1. Subset-sensitive aggregate bound

Keep the set \(I\) of any primes in \((Y^{r_0b},Y^b]\) fixed as the prefix height \(T\ge Y\) varies. Let
\[
 h=\sum_{p\in I}p^{-1},\quad D_I(s)=\sum_{p\in I}p^{-s},\quad
 W_I=\Re D_I(1/2+i\gamma),\quad S_I=W_I-h.
\]
Write \(L_T=\log T\) and let \(E_T\) denote normalized positive-prefix \(|\zeta'(\rho)|^2\) expectation. There are uniform constants, for every fixed \(M>0\), such that for all \(T\ge Y\) and all such \(I\)
\[
 E_T|S_I|^4\ll_{M,r_0} h^2+L_T^{-M}.                              \tag{1}
\]
Here and below take \(Y\) large depending on a fixed finite degree only. The proof of (1) uses the Theorem 5 rather than Theorem 4 aggregate input, with coefficient envelopes fixed in degree. As in the scalar proof, for each raw moment through degree four use the finitely many pairings between \(D_I^u\) and \(D_I^v\), \(u+v\le4\). Their fixed bounded-coefficient envelopes and divisor-closed padding are valid for every \(I\). Their support is in the same declared length \(T^\theta\), fixed \(\theta<1/2\), since \(Y^{4b}=Y^{o(1)}\). Four-sign polarization and Cauchy differentiation incur \(O_M(L_T^{-M})\) once per aggregate. Thus the absolute error is independent of interval size. The relative kernel bound retains the positive lcm-weighted main term and is \(O(bL/L_T)\) times the raw Poisson moment. All comparisons may first be made on the support avoiding the possible exceptional prime \(\ell_T\), because the padding is divisor-closed and a conductor involving \(\ell_T\) then has \(a(kq)=0\). This is precisely the full-length protection of the scalar aggregate source, not a new proof of effective individual monomial estimates. [Bounded coefficient estimate](weighted70_hlz_cutoff_review.md) · [Theorem 5 journal source, pp. 1605 and 1615–1624](../../sources/classical63_derivative_moments/hlz2022print.pdf)

For the retained set write \(h'\le h\) for its mass. In the Poisson-circle model the centered independent coordinates have range lengths \(2/\sqrt p\), so their sum \(S_\star\) has the sub-Gaussian estimate \(E e^{tS_\star}\le e^{t^2h'/2}\). This follows by twice differentiating the log moment generating function and bounding the variance of each tilted coordinate by one quarter its squared range. Integrating the resulting tail bound gives \(E_\star|S_\star|^j\ll_j(h')^{j/2}\) for \(1\le j\le4\). The raw moments \(E_\star W_\star^j\) are nonnegative even for odd \(j\), by nonnegative Fourier coefficients and Poisson expectations. For every such \(j\),
\[
 0\le E_\star W_\star^j\ll_j (h')^j+(h')^{j/2}.
\]
In the centered fourth power each raw \(j\)-th moment has coefficient bounded by \(\binom4j(h')^{4-j}\). Thus the relative arithmetic error summed after centering is
\[
 \ll (bL/L_T)\sum_{j=1}^4(h')^{4-j}\big((h')^j+(h')^{j/2}\big)
 \ll_{r_0}(h')^2 .
\]
The degree-zero moment is exact and \(\sum_{p\text{ in band}}p^{-1}=O_{r_0}(1)\). The absolute error remains \(O(L_T^{-M})\). The retained model fourth moment is \(O((h')^2)\). The removed term, when present, is deterministically bounded in absolute value by \(2/\sqrt{\ell_T}\), so its fourth power is at most \(16 h^2\), including when \(I\) is a singleton. Using \(|x+y|^4\le8(|x|^4+|y|^4)\) restores the full subset fourth moment **before** tail transfer. Consequently the left side of (1) is the same fixed statistic for each \(T\), even if \(\ell_T\) varies.

## 2. An independent crude bound with exact local mass

For every \(I\) and \(T\ge Y\) there is also the effective estimate
\[
 E_T|S_I|^4\ll_{r_0} L_T^2 h^2.                                  \tag{2}
\]
The logarithmic loss is acceptable and the exact \(h^2\) on this crude bound is crucial. To prove (2), take \(F(s)=\zeta(s)D_I(s)^2\). On RH, \(F'(\rho)=\zeta'(\rho)D_I(\rho)^2\); this includes multiple zeros, where both sides vanish. For every analytic function on a disk of radius \(R=1/L_T\), its Taylor series gives
\[
 |F'(\rho)|^2\le \frac{2}{\pi R^4}
                       \iint_{|w-\rho|\le R}|F(w)|^2\,dA(w).
\]
All disks lie in the pole-free strip \(|\sigma-1/2|\le R\), for large \(T\). Their overlaps, counted with zero multiplicity, are \(O(L_T)\) by the unit-window Riemann–von Mangoldt bound. The ordinates in their union lie in \([-1,T+1]\).

The classical continuous fourth-moment estimate gives \(\int_{-1}^{T+1}|\zeta(\sigma+it)|^4dt\ll T L_T^4\) uniformly for \(|\sigma-1/2|\le1/L_T\). For completeness, on the right use the analytic function \(G(s)=(s-1)\zeta(s)e^{s^2/T^2}/(s+1)\) on \([1/2,2]\) in real part. The \(L^4(dt)\) norm on the line \(1/2\) is \(O(T^{1/4}L_T)\) by the ordinary critical-line fourth moment and a dyadic Gaussian-tail sum, and that at 2 is \(O(T^{1/4})\) by the Euler series. Hadamard three-lines applied to pairings with \(L^{4/3}\) test functions gives the same bound on the intervening strip. Imaginary translation of the line leaves the full \(L^4(dt)\) norm unchanged, and the Gaussian and pole removal supply holomorphy and growth requirements. On \(|t|\le T+1\) and \(1/2\le\sigma\le1/2+1/L_T\), the prefactors removed to recover \(\zeta\) are bounded away from zero. The functional equation gives the other side, since its gamma-ratio size \(\ll(1+|t|)^{1/2-\sigma}\) is uniformly bounded in this thin strip, including bounded \(t\). This uses only the classical continuous fourth moment with effective constants and Stirling. [Titchmarsh–Heath-Brown §7.21, (7.21.1)](../../sources/equivalence_round2/titchmarsh1986.pdf)

Write \(D_I(s)^4=\sum_{m\le y} a_m m^{-s}\), \(y=Y^{4b}\), \(0\le a_m\le4!\). Then
\[
 \sum_{m\le y}a_m^2m^{-2\sigma}
 \le4!\left(\sum_{p\in I}p^{-2\sigma}\right)^4\ll h^4
\]
in the full thin strip, since \(p^{2/L_T}\le e^{2bL/L_T}\). Integrating the squared polynomial in \(t\), the diagonal contributes \((T+2)\sum_m a_m^2m^{-2\sigma}\). The off-diagonal absolute contribution is \(O(y\log(2y)\sum_m a_m^2m^{-2\sigma})\): use \(1/|\log(m/n)|\le y/|m-n|\), the arithmetic–geometric mean bound on the product of the two coefficients with their weights, and the harmonic sum. Since \(y\le T^\theta\) eventually for fixed \(\theta<1\), this proves \(\int_{-1}^{T+1}|D_I(\sigma+it)|^8dt\ll T h^4\). By Cauchy–Schwarz the corresponding integral of \(|F|^2\) is \(O(TL_T^2h^2)\). Summing the disk bounds, paying \(L_T^4\) for the derivative, \(O(L_T)\) for overlaps, and \(O(1/L_T)\) for strip width, gives
\[
 \sum_{0<\gamma\le T}|\zeta'(\rho)|^2 |D_I(\rho)|^4
 \ll T L_T^6 h^2.
\]
Divide by the true untwisted positive-prefix mass \(A(T)\asymp T L_T^4\) and use \(|S_I|^4\le8(|D_I|^4+h^4)\), \(h=O_{r_0}(1)\). This proves (2), without requiring any independent Dirichlet \(L\)-function hypotheses. [Untwisted prefix, Gonek Corollary 1](../../sources/classical63_lfunctions/gonek1984.pdf)

## 3. Strict-tail transfer and small-scale moment

For the fixed centered statistic \(S_I\), let \(A_I(T)=\sum_{0<\gamma\le T}|\zeta'(\rho)|^2|S_I(\gamma)|^4\) and \(g(t)=(1/4+t^2)^{-1}\). The strict-tail numerator is
\[
 -g(Y)A_I(Y)+\int_Y^\infty(-g'(T))A_I(T)\,dT.
\]
The endpoint sign is favorable for upper bounds since \(A_I\ge0\), and the endpoint at infinity vanishes. Using inclusive prefixes excludes the atom at \(Y\) exactly. In the integral the extra factor \(L_T^2\) from (2) increases the estimate by at most \(O(L^2)\) after division by the tail mass \(\asymp Y^{-1}L^4\): substitute \(T=Yv\) and use \(\int_1^\infty v^{-2}(1+\log v)^6dv<\infty\). Apply (1) similarly, with \(L_T^{-M}\le L^{-M}\). Negative ordinates make identical contributions. Hence
\[
 E_Y |S_I|^4\ll_{M,r_0}\min\{h^2+L^{-M},\,L^2h^2\}.
\]
With \(M\ge6\), if \(h\le L^{-4}\) use \(L^2h^2\le h^{3/2}\); if \(h\ge L^{-4}\) use \(L^{-M}\le h^{3/2}\) and boundedness of \(h\). The empty subset has zero increment. This gives the desired subset-sensitive exponent \(3/2>1\). The same method yields any fixed exponent \(2-\eta\) for \(0<\eta<1\), using the crossover \(h=L^{-2/\eta}\) and \(M\ge2(2-\eta)/\eta\). An aggregate error of size only \(L^{-M}\), without (2), cannot itself be absorbed into \(h^2\) for every subset in the full subpower range. For example a singleton at \(\log p\asymp bL\) can have \(h^2\ll L^{-M}\) for every fixed \(M\). The proof here relies on the separate weighted sampling bound at fine scales.

## 4. Tightness, Gaussian identification and effectivity

Enumerate the band primes increasingly and set \(v_j=\frac12\sum_{i\le j}1/p_i\), \(v_0=0\). Interpolate the cumulative centered statistic linearly between these times in the reciprocal-mass clock, starting at zero. Extend it constantly to a fixed interval \([0,V]\) containing all the clocks for large \(Y\). The fourth bound gives grid increments \(\ll |v_j-v_i|^{3/2}\). Within a single cell, linear interpolation multiplies the fourth moment by a fractional fourth power, which is at most the fractional power \(3/2\) needed for the time distances. Across cells, split into at most three pieces and use Minkowski in \(L^4\), then \(\sum_{\ell=1}^3 \Delta_\ell^{3/8}\le 3^{5/8}(\sum_\ell\Delta_\ell)^{3/8}\). Thus the bound with exponent \(3/2\) holds at all times. Kolmogorov's criterion gives uniform-topology tightness of the interpolated processes, with no union over all the prime cutoffs. One explicit modulus argument uses dyadic adjacent increments with threshold \(A2^{-\alpha j}\) for \(0<\alpha<1/8\). The exceptional probability from levels \(j\ge k\) is \(O(A^{-4}\sum_{j\ge k}2^{-(1/2-4\alpha)j})\). Outside that event the usual continuous dyadic chaining bounds the modulus at scale \(2^{-k}\) by \(O_\alpha(A2^{-\alpha k})\).

Elementary reciprocal-prime Mertens summation gives, uniformly for \(r\in[r_0,1]\),
\[
 c_Y(r)=\tfrac12\sum_{Y^{r_0b}<p\le Y^{rb}}p^{-1}
       =\tfrac12\log(r/r_0)+O_{r_0}((bL)^{-1}).
\]
The elementary effective estimate follows from \(\sum_{p\le x}\log p/p=\log x+O(1)\) by integration by parts, with the common constant cancelling between endpoints. The step cutoff process is exactly the interpolated process evaluated at \(c_Y(r)\) under the inclusive upper cutoff convention. The uniform modulus estimate and clock approximation make it uniformly close in probability to the interpolation evaluated at \(c(r)=\frac12\log(r/r_0)\). Each actual jump is also deterministically at most \(2\exp(-r_0bL/2)\).

The finite-dimensional statements follow by projecting onto a fixed real vector and applying the scalar aggregate comparison to a piecewise constant vector of prime coefficients (the constants take finitely many bounded values). At each fixed moment order, the powers of the associated Dirichlet polynomial have bounded coefficients independent of \(Y\) and length \(Y^{o(1)}\). Absolute Fourier coefficients are majorized by the corresponding positive Poisson model on the whole band, so the relative error is \(O(b)\) after strict-tail transfer. The log-saving remainder is fixed degree as before, and the omitted term is \(O(\exp(-r_0bL/2))\) pointwise. It is restored before Stieltjes transfer by the higher even bounds and Hölder for each fixed moment. Under the independent model each coordinate is centered and the covariance at \(r,s\) is
\[
 \frac12\sum_{Y^{r_0b}<p\le Y^{b\min(r,s)}}(p^{-1}-p^{-2})
       \ \longrightarrow\ \tfrac12\log(\min(r,s)/r_0).
\]
The largest summand tends to zero, the total second moments are bounded, and each cumulant of fixed order \(j\ge3\) is bounded by a constant times the largest-coordinate bound to the power \(j-2\) times the total variance. The projected moments therefore converge to Gaussian moments, including the case of vanishing variance. Moment determinacy and Cramér–Wold give the joint Gaussian limit. This finite-dimensional covariance and continuity characterize the claimed Brownian clock limit. Uniform approximation implies \(J_1\) approximation, so it transfers the interpolated path conclusion to the original step process.

Effectivity uses the effective aggregate input and classical constants in (2), together with cutoff moduli. For fixed mesh and fixed tolerance the moment comparisons yield finite-dimensional bounded-Lipschitz onset as in the earlier fixed-dimensional proof. The dyadic modulus estimate discretizes bounded-Lipschitz path tests to the polygonal interpolation of those mesh values, and the clock error is effective uniformly in \(r\). Brownian motion has an effective modulus by its exact fourth moment at the same intervals. Combining these three effective errors gives the stated conditional onset, without assigning numerical values to source constants. [Earlier finite-dimensional moment-to-law argument](uniform65_joint_exceptional_prime_clt.md) · [Earlier reciprocal-clock interpolation](uniform67_brownian_prime_phase_process.md)
