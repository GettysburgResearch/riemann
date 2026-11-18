# Independent audit of global weighted Hardy variation

A separate analytic construction gives \(\mathcal T(10000)<0.491\). I also checked the sharper derivation against its implementation and replayed it at 192 bits. Its upper bound \(\mathcal T(10000)<0.48494\), combined with the previously certified finite sum, gives the unconditional enclosure \(0.61649875288731141829<C_2<1.10144\) for the critical-line derivative series. The identification with the tapered-array limit requires RH. [Independent implementation](../../scripts/weighted67_independent_checks.py) · [Sharper proof and checks](prime67_global_hardy_tail.md) · [Prior finite certificate audit](positivity65_q2_weighted_rolle_skeptic.md)

## Endpoint and block structure

Use \(G=Q_2Z\), \(f=\phi G/t\), with the cubic \(\phi=3u^2-2u^3\) for \(u=(t-9900)/100\) on the transition, and \(\phi=1\) above 10000. Both components of \(f'\) vanish at 9900. The estimates for \(G^{(j)}/t\) below show that \(f',f''\in L^2\). For each real component \(f_i\), the locally absolutely continuous function \((f_i')^2\) has integrable derivative \(2f_i'f_i''\). Its limit at infinity exists and is zero by integrability of \((f_i')^2\). For any finite selection of distinct critical-line zeros, componentwise Rolle points give disjoint rises and falls of \((f_i')^2\), using the lower endpoint and the zero limit at infinity for the extreme rises and falls. The component Rolle points need not agree. Summing their variation bounds and applying Cauchy–Schwarz twice gives \(\sum_{\gamma>10000}|f'(\gamma)|^2\le\|f'\|_2\|f''\|_2\). Conjugation and \(\gamma^2+1/4\ge\gamma^2\) give \(\mathcal T(10000)\le2\|f'\|_2\|f''\|_2\). This argument applies without a simplicity or spacing assumption.

For \(A_j=\|G^{(j)}/t\|_{L^2([9900,\infty))}\), \(B_j=\|G^{(j)}/t\|_{L^2([9900,10000])}\), and \(T_0=9900\), differentiation gives
\[
\begin{aligned}
\|f'\|_2&\le A_1+A_0/T_0+0.015B_0,\\
\|f''\|_2&\le A_2+2A_1/T_0+2A_0/T_0^2+0.03(B_1+B_0/T_0)+0.0006B_0 .
\end{aligned}
\]
The phase center is constant within each local representation. Changing it at a block endpoint changes the decomposition of the same Hardy derivative. The weighted norms sum over blocks, and variation is applied directly to the global function.

## Sparse coefficients and mean squares

On \([T,U]\) with \(T\ge9900\) and \(1<U/T\le3/2\), put \(M=\lceil 7T/25\rceil\) and \(c=\frac12\log(\sqrt{TU}/(2\pi))\). The centered polynomials are
\[
 P_j(t)=\sum_n d_n n^{-1/2}(\log n-c)^j e^{-it\log n}.
\]
The coefficients \(d_n\) are \(\pm1\) through \(M\), 2 on the extra evens through \(2M\), and zero elsewhere. With \(p=2j\), let \(D=\sum_n (d_n^2/n)|\log n-c|^p\). Integration by parts against \(w(t)=t^{-2}\) bounds \(\|P_j/t\|_2^2\) by \(D(1/T-1/U)+3\pi J/T^2\). The two endpoint Hilbert forms and the integrated derivative of \(w\) contribute at most \((3\pi/2)(w(T)+w(U)+\int|w'|)=3\pi w(T)\). In the dense part each nearest log gap is at least \(1/(n+1)\). On the even tail the gap is at least \(2/(n+2)\), except when the immediately preceding dense index is \(n-1=M\) with \(M\) odd. There \(1/(n+1)\) is valid and the additional correction is at most \(2|\log n-c|^p\). When \(M\) is even the first tail index is two integers past the preceding dense term and retains the ordinary sparse bound. The highest tail even can use its preceding neighbor. Consequently
\[
 J\le D+\sum_{n\le M}|\log n-c|^p+
 2\!\sum_{\substack{M<n\le2M\\2\mid n}}|\log n-c|^p+
 2\,1_{M\ {\rm odd}}|\log(M+1)-c|^p.
\]
[Hilbert inequality and earlier gap audit](positivity65_q2_weighted_rolle_skeptic.md)

Let \(m=\log M-c\) and \(b=\log(2M)-c\), which are positive. In the independent implementation the dense diagonal is bounded by
\[
 \frac{m^{p+1}-(-c)^{p+1}}{p+1}+c^p+
 1_{p>0}e^{-c}(p/e)^p .
\]
For \(p>0\), the integrand \(x^{-1}|\log x-c|^p\) decreases to zero on the left and has at most one maximum on the right, bounded by \(e^{-c}(p/e)^p\). Comparing summands with following unit integrals, the excess is at most the downward variation plus the terminal value. For \(p=0\) the integrand is decreasing. For the tail-even diagonal the same comparison with following length-two integrals, divided by two, gives
\[
 \frac{2(b^{p+1}-m^{p+1})}{p+1}+8b^p/M .
\]
Here the integrand is unimodal and bounded by \(b^p/M\). For \(J-D\), the dense unweighted moment is bounded by its integral plus \(c^p+m^p\), and the tail even unweighted moment by half its integral plus \(b^p\). With the parity exception this gives \(J\le D+\int_1^{2M}|\log x-c|^p\,dx+c^p+m^p+4b^p\).

The sharper implementation uses the trapezoid rule for each progression. On one grid step the difference between the normalized trapezoid and the mean integral equals an integral of the derivative of the density against a centered affine weight bounded by \(1/2\). Over the progression the error is bounded by half the total variation, with the first and last values each adding a half to restore their full weight. The turning points of the two densities are \(e^c\), and also \(e^{c+p}\) for \(x^{-1}|\log x-c|^p\) when \(p>0\). Including a possible turning point when its ball overlaps a boundary can only increase the sum of absolute differences. I checked the antiderivatives, grid endpoints, and the 32 individually summed harmonic terms.

## Euler disk and phase

Write \(d=7/25\), \(v=\operatorname{Im}s\), \(\sigma=\operatorname{Re}s\), and \(P(s)=\sum_{n\le M}n^{-s}\). On every radius-\(1/3\) disk in the complex height variable around \(t\in[T,U]\), one has \(|s|/M<5.36\), \(M/|s-1|\le d+2/T\), and \(\sigma\ge1/6\). For either sign of the \(n\)-th Bernoulli Fourier mode in Euler summation, the amplitude divided by the absolute phase derivative is \(x^{-\sigma}/(2\pi nx\mp v)\), decreasing to zero. Integration by parts bounds the mode integral by \(2M^{-\sigma-1}/(2\pi n\mp v/M)\). All denominators are positive because \(5.36<2\pi\). Pair the signs, retain the \(n=1\) denominators separately, and use \(2\pi n-5.36\ge n(2\pi-2.68)\) for \(n\ge2\). The integrated modes are absolutely summable. The Abel-regularized Bernoulli function is bounded by its original essential supremum via Poisson convolution, so dominated convergence applies with the integrable amplitude. Euler summation then bounds the scalar remainder by \(C(T)M^{-\sigma}\) with
\[
 C(T)=d+2/T+\tfrac12+\frac{5.36}{\pi}
 \left[\frac1{2\pi-5.36}+\frac1{2\pi}
 +(\pi^2/6-1)\left(\frac1{2\pi-2.68}+\frac1{2\pi}\right)\right].
\]

The Hardy multiplier \(A\) is holomorphic on the rectangle enclosing these disks. The defining gamma ratio has no poles or zeros there, and its square root can be fixed to the real-line phase. The log derivative of its squared modulus in \(\sigma\) is the average of the real parts of the two digammas minus \(\log\pi\). Its difference from \(\log T\) is bounded by
\[
 \log\frac{2\pi}{1-1/(3T)}+\frac{\pi}{T-1/3}+\frac1{T^2}<1.85.
\]
This follows from the previous bound \(|\Re\psi(x+iy)-\log|y||\le\pi/(2|y|)+x^2/(2y^2)\), now used for \(1/12\le x\le5/12\) and \(|y|\ge(T-1/3)/2\). On the real height line \(|A|=1\). Integrating horizontally gives \(|A|^2\le e^{1.85|\sigma-1/2|}T^{\sigma-1/2}\). Since \(M\ge dT\) and \(d^2T>1\), the resulting bound for \(|R|=|A(\zeta-P)|\) on radius \(a\le1/3\) is
\[
 C(T)e^{1.85a/2}d^{a-1/2}T^{(a-1)/2}.
\]
The maximum of the majorant occurs at the smallest \(\sigma=1/2-a\), so this bound is uniform in the entire complex disk. Use the direct bound at order zero and Cauchy radii \(1/6,1/3\) at orders one and two. Multiplying by \((1/T-1/U)^{1/2}\) gives the weighted norm bounds for these three derivatives.

On the real block the phase shift \(|\theta'-c|\) is at most \(\log(U/T)/4+2/T\). The digamma comparison gives the sharper error \(\pi/(2T)+1/(16T^2)\), as used by the proponent. The trigamma series gives \(|\theta''|\le T^{-2}+\pi/(4T)\le1/T\). In differentiating \(A Q_2P\) once use \(iA((\theta'-c)P_0-P_1)\). Twice use \(A((i\theta''-(\theta'-c)^2)P_0+2(\theta'-c)P_1-P_2)\). Multiply the Euler remainder by \(Q_2\) after Cauchy, using the real-axis product constants \(1+\sqrt2,\sqrt2\log2,\sqrt2(\log2)^2\). The proponent uses bound 1.86 on the multiplier's log derivative across its larger radius-\(0.4\) rectangle and the smaller Cauchy radii \(0.16,0.32\). I checked that its phase speed \(5.36\), digamma comparison, and \(M/|s-1|\) bounds remain valid across that enlarged rectangle. [Prior multiplier and digamma formulas](prime64_main_term_moments.md)

## Infinite residual and replay

For the independent residual, \(U=3T/2\), \(H=\log T\), and \(L=(H+1)/2\). The log coefficient range lies within \([-L,L]\) by bounding its endpoints. The preceding integral and discretization estimates give \(D\le(H+5)L^p\) and \(J\le D+(2dT+8)L^p\). The disk bound at radius \(1/3\) is at most \(12T^{-1/3}\). The resulting normalized polynomial, remainder, and phase coefficients after dividing the weighted norms by \(H^{j+1/2}/\sqrt T\) decrease with the lower height. Sum the remaining squares using successive term ratio at most \((1+\log(3/2)/\log V)^{2j+1}/(3/2)\), with \(V=9900(3/2)^{32}\). The separate lower-transition calculation uses \(U=10000\) and the same local formulas.

I checked the sharper residual's alternative choices, including its bound \(J-D\le(2dT+5)((H+2)/2)^p\). The support count charges \(M\) dense terms, at most \((M+1)/2\) extra even terms of weight two, and at most two for the parity exception. The coefficient \(2dT+5\) follows from \(M\le dT+1\). Its normalized diagonal bound uses the dense integral bounded by \(2((H+2)/2)^{p+1}/(p+1)\) plus a quadrature excess of at most \(3((H+2)/2)^p\). The extra even harmonic contribution is at most \(2(\log 2+2/M)((H+2)/2)^p\), by logarithmic integral comparison. The exponential relaxation \(1+x\le e^x\) bounds the ratio in the geometric residual. The normalized remainder order \(j\) includes the decay \(T^{(a_j-1)/2}(\log T)^{-j-1/2}\), and each product-rule term that lowers log order carries its powers of \(1/\log T\). This verifies the required uniform monotonicity.

The independent 128-bit Arb run bounds the tail by \(0.490714832598944208741456993498720083\ldots\). The sharper 192-bit replay gives a ball centered at \(0.484939990279267741291340450704153251948668\ldots\) with radius \(3.46\cdot10^{-56}\). The replay at \(3\cdot10^6\) centers at \(0.00599089891771064542392840815877964328801456\ldots\) with radius \(6.11\cdot10^{-58}\). A complete derivative sum through that height of width less than \(0.00017\) would thus yield an enclosure narrower than one percent of the existing lower bound. No larger finite census was used in this audit.

Run the independent check from the repository root with PYTHONPATH=/workspace/riemann-runtime python scripts/weighted67_independent_checks.py.
