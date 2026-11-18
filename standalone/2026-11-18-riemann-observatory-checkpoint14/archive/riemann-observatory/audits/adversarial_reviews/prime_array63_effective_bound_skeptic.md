# An independent effective bound for the prescribed prime array at \(k=2\)

17 November 2026. Under RH, for every integer \(N\ge3\), the prescribed anchored prime array satisfies

\[
 E_N(2):=\left\|MR_2-\frac{\zeta B_{N,2}}s\right\|_{L^2(dt/(2\pi))}^2
 \le\frac{10^{27}}{\log N}.
\]

This is an independent numerical instantiation of the contour argument. The constants are coarse and require neither computed zero heights, simplicity, nor inverse-derivative moments. [Array and target definitions](director_tapered_prime_array_round9.md) · [Prior qualitative contour proof](generator63_tapered_prime_array_skeptic.md)

## A fixed-strip bound valid at every height

Put \(T_t=2+|t|\) and \(f(s)=(s-1)\zeta(s)/(s+1)\). On the closed strip \([-1/4,5/4]\), this is holomorphic and grows at most polynomially in height. The Euler summation identity that supplies the growth bound is

\[
 \zeta(s)=\frac1{s-1}+\frac12+\frac{s}{12}
 -\frac{s(s+1)}2\int_1^\infty B_2(\{u\})u^{-s-2}\,du,
 \qquad B_2(v)=v^2-v+\tfrac16.
\]

It follows first for \(\Re s>1\) from the floor integral and one integration by parts of the continuous periodic Bernoulli polynomial. Since \(|B_2(v)|\le1/6\), the formula continues to \(\Re s>-1\). The factor \(s-1\) removes the pole at 1 in \(f\), and the pole of \((s+1)^{-1}\) is outside the strip.

On \(\Re s=5/4\), absolute summation gives \(|f(s)|\le\zeta(5/4)\le5\). For the left edge use

\[
 \zeta(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)\zeta(1-s).
\]

For \(z=a+ib\) with \(a>0\), the exact Binet remainder in \(\log\Gamma(z)\) is bounded by \(1/(12a)\). Indeed the integrand's numerator \(1/(e^u-1)-1/u+1/2\) lies between 0 and \(u/12\), and Binet integrates this numerator against \(e^{-zu}du/u\). The numerator inequality is equivalent to \(0\le v\coth v-1\le v^2/3\) with \(v=u/2\). Its upper part follows by comparing power-series coefficients in \(v\cosh v-\sinh v\le(v^2/3)\sinh v\). Thus

\[
 |\Gamma(a+ib)|\le\sqrt{2\pi}(a+|b|)^{a-1/2}
 e^{-a-|b|\arctan(|b|/a)+1/(12a)}\qquad (a\ge1/2).
\]

At \(\Re s=-1/4\), take \(a=5/4\), \(b=-t\). The sine has modulus at most \(e^{\pi|t|/2}\), and \(|t|(\pi/2-\arctan(|t|/a))\le a\), also at \(t=0\) by continuity. Using \(\sqrt{2\pi}<3\), \(e^{1/(12a)}<2\), \(\zeta(5/4)\le5\), and \(|(s-1)/(s+1)|<2\) on the left edge gives \(|f(-1/4+it)|\le60T_t^{3/4}\).

Apply three lines to \(f(s)e^{(s-it)^2}\) for each fixed target height \(t\). For a boundary height \(v\), \(T_v\le T_t(1+|v-t|)\). The factors \(e^{1/16}\) and \((1+|v-t|)^{3/4}e^{-(v-t)^2}\) on the left are each at most 2. The right bound is at most \(5e^{25/16}<240\). The auxiliary function is bounded throughout the strip by the earlier polynomial growth and Gaussian decay. Evaluating at height \(t\) and discarding the factor \(e^{-(\Re s)^2}\) gives

\[
 |f(\sigma+it)|\le240T_t^{(5/4-\sigma)/2},\qquad -1/4\le\sigma\le5/4. \tag{1}
\]

On the radius-\(1/8\) disk about \(1/2+it\), \(|(s+1)/(s-1)|\le13/3<5\). The exponent in (1) is at most \(7/16\) and the height change contributes a factor at most 2. Therefore the disk supremum of \(|\zeta|\) is at most \(2400T_t^{7/16}\). Cauchy's formula at radius \(1/8\) proves the convenient common bound

\[
 |\zeta(1/2+it)|+|\zeta'(1/2+it)|\le10^5T_t^{7/16}. \tag{2}
\]

## Unit-window counts and the regularized derivative

Assume RH. Jensen's inequality for \(f\) centered at \(2+it\), with inner radius \(15/8\) and outer radius \(9/4\), counts every zero satisfying \(|\gamma-t|\le1\), with multiplicity. Its squared distance from the center is at most \(13/4<(15/8)^2\). The disk misses \(s=-1\), and the pole at 1 is removed in \(f\). Throughout the outer disk, (1) and the Euler series to the right of \(5/4\) give \(|f|\le720T_t^{3/4}\), since its ordinate shift is at most \(9/4\) and hence its shifted \(T\) is at most \(3T_t\). At the center one has \(|f(2+it)|\ge1/6\), using \(|\zeta(2+it)|\ge1/\zeta(2)\ge1/2\) from the reciprocal Dirichlet series and \(|(1+it)/(3+it)|\ge1/3\). Boundary zeros on the outer circle can be treated by a limit in the radius. Since \(\log(6/5)\ge1/6\) and \(4320<2^{13}\), the resulting count is at most \(6(13\log2+(3/4)\log T_t)\). In particular

\[
 \sum_{|\gamma-t|\le1}m_\rho\le100\log T_t. \tag{3}
\]

For distant zeros use both sides of each bin \(j\le|\gamma-t|<j+1\), \(j\ge1\). Their total multiplicity is at most \(200(\log T_t+\log(j+2))\). Since \(\log(j+2)\le2+\sqrt j\), the elementary integrals that bound the sums of \(j^{-2}\) and \(j^{-3/2}\) give

\[
 \sum_{|\gamma-t|>1}\frac{m_\rho}{|\gamma-t|^2}
 \le200(2\log T_t+7)\le2500\log T_t. \tag{4}
\]

Here and below use \(\log T_t\ge\log2>2/3\), as follows from the series for \(2\operatorname{arctanh}(1/3)\).

Let \(K=\zeta'/\zeta\), let \(X=\xi'/\xi\) for the standard completed xi-function, and set

\[
 D(z)=1/z+1/(z-1)-\tfrac12\log\pi+\tfrac12\psi(z/2),
 \qquad K=X-D.
\]

The difference of the genus-one Hadamard logarithmic derivatives at \(z\) and \(w=2+it\) is the absolutely convergent sum of \(m_\rho((z-\rho)^{-1}-(w-\rho)^{-1})\). For the radius-\(1/4\) disk about \(s=1/2+it\) and the evaluation at \(w\), the elementary terms in \(D\) are bounded by 9 in total. The digamma terms obey \(|\psi(u)|\le30\log T_t\) for all arguments used here with \(\Re u\ge1/8\), \(|u|\le T_t\). To check this, use

\[
 \psi(u)=-\gamma_E+\sum_{n\ge0}\big((n+1)^{-1}-(n+u)^{-1}\big).
\]

For \(J=\lceil|u|+2\rceil\), the zeroth term costs at most 9, the other terms below \(J\) at most \(2(1+\log J)\), and the tail at most \((|u|+1)/(J-1)\le1\). With \(|\gamma_E|\le1\) and \(J\le(5/2)T_t\), this is below \(30\log T_t\). Thus both values of \(D\) are bounded by \(30\log T_t\). Also \(|K(w)|\le\sum_{n\ge2}(\log n)n^{-2}\le2\), using \(\log n\le\sqrt n\).

Subtract from \(K(z)\) the terms \(m_\rho/(z-\rho)\) with \(|\gamma-t|\le1\), using this fixed zero list on the whole disk. The resulting function \(K_{\mathrm{reg}}\) is holomorphic there. The nearby subtracted terms evaluated at \(w\) cost at most \(100\log T_t\). For a far zero, \(|w-z|\le7/4\), \(|w-\rho|\ge|t-\gamma|\), and \(|z-\rho|\ge(3/4)|t-\gamma|\), so its paired difference costs at most \(3m_\rho/|t-\gamma|^2\). Equation (4) gives

\[
 |K_{\mathrm{reg}}(z)|\le8000\log T_t.
\]

Now write \(h(z)=2^{1-z}-1\), \(Z=-hK-h'\), and \(r_\rho=-m_\rho h(\rho)\). On this disk \(|h|<3\) and \(|h'|<2\). The analytic remainder after the same pole subtraction from \(Z\) is

\[
 Z_{\mathrm{reg}}(z)=-h(z)K_{\mathrm{reg}}(z)-h'(z)
   -\sum_{|\gamma-t|\le1}m_\rho\frac{h(z)-h(\rho)}{z-\rho}.
\]

The divided differences are each at most 2 by integrating \(h'\) on the connecting segments. Thus the disk supremum is at most \(25{,}000\log T_t\), and Cauchy at its center gives

\[
 Z'(s)=-\sum_{|\gamma-t|\le1}\frac{r_\rho}{(s-\rho)^2}+U_t,
 \qquad |U_t|\le10^5\log T_t. \tag{5}
\]

This regularization holds at all heights with the disk poles removed. No derivative of a moving cutoff has been taken.

## Left contour, horizontal limits and the anchor

On \(z=-1+it\), differentiating the same functional equation gives

\[
 K(z)=\log(2\pi)+\tfrac\pi2\cot(\pi z/2)-\psi(1-z)-K(1-z).
\]

The cotangent modulus is \(|\tanh(\pi t/2)|\le1\), including \(t=0\). The earlier digamma estimate at \(1-z=2-it\), together with \(|K(2-it)|\le2\), gives \(|K(z)|\le6+30\log T_t\). Since \(|h(z)|\le5\) and \(|h'(z)|\le4\), one has

\[
 |Z(-1+it)|\le250\log T_t. \tag{6}
\]

For the Perron shift one can take heights \(H\in[M,M+1]\), \(M\ge4\), at distance at least \(1/(1000\log(M+4))\) from all ordinates. Indeed (3) applied at \(M\) and \(M+1\) bounds the nearby count by \(200\log(M+4)\), so the total length of the deleted intervals is at most \(2/5\). Reflect those heights for the lower segment. On \(-1\le\Re z\le2\) at such heights the Hadamard difference from \(2+iH\) bounds the near sum by \(100\log T_H(2000\log T_H+1)\) and the far sum by \(3\cdot2500\log T_H\). For the gamma term use \(\psi(z/2)=\psi(1+z/2)-2/z\), with \(\Re(1+z/2)\ge1/2\), \(|1+z/2|\le T_H\) and \(|z|\ge4\). Both completed elementary terms are bounded by \(30\log T_H\). It follows that \(|K(z)|\le220{,}000\log^2T_H\) and \(|Z(z)|\le1{,}200{,}000\log^2T_H\) on the segments. This suffices to remove the horizontal integrals at every fixed \(N,s\).

Put \(L=\log N\). For \(s\) on the critical line away from zeros, or \(s=1\), the double Perron integral over \(\Re z=2\) with kernel \(N^{z-s}/(L(z-s)^2)\) gives the exact tapered polynomial \(A_N=A_{N,2}\). The absolute Dirichlet series on that line permits termwise inversion, and the endpoint coefficient has zero taper. Shift to \(\Re z=-1\). The quotient \(Z=-[\zeta h]'/\zeta\) is holomorphic at 1 because \(h(1)=0\) cancels the zeta pole in \(\zeta h\) and \(1/\zeta\) vanishes there. Trivial zeta zeros are left of the shift. The kernel point gives \(Z(s)+Z'(s)/L\), so

\[
 A_N(s)=Z(s)+\frac{Z'(s)}L+\frac1L\sum_\rho
 \frac{r_\rho N^{\rho-s}}{(s-\rho)^2}+I_N(s).
\]

The sum converges absolutely by (4) and the finitely many near terms. From (6), for \(\sigma=1/2\) or \(1\),

\[
 |I_N(\sigma+it)|\le\frac{250N^{-1-\sigma}}{2\pi L}
 \int_{\mathbb R}\frac{\log T_t+\log(1+|v|)}{1+v^2}\,dv
 \le\frac{1000N^{-1-\sigma}}L\log T_t. \tag{7}
\]

The second integral in the numerator is at most 12, by bounding the positive half up to 1 by 2 and the remaining half by \(2v^{-3/2}\) before doubling. The first integral is \(\pi\log T_t\).

At \(s=1\), \(Z(1)=0\) and Laurent expansion gives \(Z'(1)=\gamma_E\log2-(\log2)^2/2\), with modulus below 2. Under RH, \(|r_\rho|\le3m_\rho\) and \(|N^{\rho-1}|=N^{-1/2}\). From (3) for \(|\gamma|\le1\) and (4) beyond it, \(\sum m_\rho/|1-\rho|^2\le2900\log2<2900\). Equation (7) then gives the bound needed for the actual anchor

\[
 |A_N(1)|\le10^4/L. \tag{8}
\]

## Assembly in the full boundary norm

Put \(s=1/2+it\) and \(E_L(v)=(1-e^{-iLv})/(iLv)=\int_0^1e^{-iLuv}du\), with its continuous value at zero. By Plancherel, \(\int|E_L(v)|^2dv/(2\pi)=1/L\). On inserting (5), the near part of the residual \(\zeta(Z-A_N+A_N(1))/s\) is

\[
 P_N(t)=\sum_{|\gamma-t|\le1}r_\rho\frac{\zeta(s)}{s(s-\rho)}E_L(t-\gamma).
\]

Zeros themselves may be omitted when establishing the almost-everywhere identity. The line segment to a nearby zero and (2) bound \(|\zeta(s)/(s-\rho)|\le2\cdot10^5T_t^{7/16}\). Also \(T_t^2\le17(1/4+t^2)\) by Cauchy–Schwarz, giving \(|s|^{-1}\le5/T_t\). Weighted Cauchy–Schwarz with (3) therefore gives

\[
 |P_N(t)|^2\le9\cdot10^{14}T_t^{-9/8}\log T_t
                 \sum_{|\gamma-t|\le1}m_\rho |E_L(t-\gamma)|^2.
\]

On these integration intervals the outer weight is bounded by \(5T_\gamma^{-9/8}\log T_\gamma\), since \(T_t/T_\gamma\in[1/2,2]\). For \(j\le|\gamma|<j+1\), use (3) on both signs and \(\log(j+3)\le2\log(j+2)\). The resulting weighted zero sum is at most \(800\sum_{n\ge2}n^{-9/8}\log^2n\). The common series and integral bound used below is

\[
 \sum_{n\ge2}n^{-9/8}\log^2 n\le 32^2\int_1^\infty x^{-17/16}dx=16384,
\]

since \(\log x\le32x^{1/32}\) for \(x\ge1\). Consequently \(L\|P_N\|_2^2\le9\cdot10^{14}\cdot5\cdot800\cdot16384<10^{23}\).

For the residual remaining after \(P_N\), the four terms are the regular derivative in (5), the far residues, the left integral, and the anchor. Their bounds in units \(\log T_t/L\) are respectively \(100{,}000\), \(7500\), \(1000\), and \(15{,}000\), the last using (8) and \(\log T_t>2/3\). This sum is below \(2\cdot10^5\), so after multiplication by \(\zeta(s)/s\) the absolute remainder is bounded by \(10^{11}T_t^{-9/16}\log T_t/L\). Its squared norm multiplied by \(L\) is at most \(10^{22}\cdot16384/L<2\cdot10^{26}\), using the same integral estimate, the measure \(dt/(2\pi)\) and \(L\ge\log3>1\). Twice the sum of the near and remaining squared bounds is below \(10^{27}\). This proves the claimed inequality for the prescribed array at every integer \(N\ge3\), with the anchor already included. An exact rational arithmetic check independently verified the numerical multipliers in these final bounds.
