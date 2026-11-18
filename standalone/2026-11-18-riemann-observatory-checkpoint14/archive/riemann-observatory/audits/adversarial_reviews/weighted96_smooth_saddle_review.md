# Independent review of the averaged one-sided saddle replacement

I checked the new compact-local argument in the adjudication, including the HLZ conventions in (27)–(29) and Lemma 7. The smoothed saddle replacement does have a power saving at the proposed scale. It removes the separate saddle obstacle for this formulation and leaves one signed nonprincipal arithmetic remainder. The proof restores sharp endpoints in the zero sum. The sharp saddle estimate for the arithmetic sum remains a separate matter. [Adjudication](analytic95_pure_fourth_adjudication.md) · [HLZ journal](../../sources/classical63_derivative_moments/hlz2022print.pdf)

## Averaging both edges and taking derivatives

Fix \(T\asymp Y\) and a compact interval of comparable heights. Use smooth nonnegative endpoint densities \(r_-,r_+\) of mass one, each on an interval of width \(O(H)\) about its endpoint, with disjoint supports and derivatives \(r_\pm^{(j)}\ll_j H^{-j-1}\). The averaged rectangle is the expectation of the rectangle with lower and upper endpoints at those two random heights. The time weight on every vertical side and on the residues is
\[
 w_T(t)=\int_{-\infty}^t (r_-(v)-r_+(v))\,dv .
\]
It is real, compactly supported, between zero and one, and differs from the sharp interval indicator only in the two transition regions. Reflection across the critical line in the original upper-half rectangle retains this same time weight. One can equivalently subtract two averaged rectangles with a shared fixed bottom. The averaged identity uses no complex extension of \(w_T\).

On either endpoint interval, let
\[
 R(t)=\int_{\sigma_L}^{\sigma_R}
        |(\zeta'/\zeta)(\sigma+it)|\,d\sigma .
\]
The fixed-strip local partial fractions, RH and integration of each pole term bound \(R(t)\) by \(O(\log T)+O(\sum_{|\gamma-t|\le1}\log(2+1/|t-\gamma|))\) outside the measure-zero ordinates. On a unit interval the sum has \(O(\log T)\) terms, counted with multiplicity. Cauchy–Schwarz over these terms and integrability of the square of the logarithm give \(\int_I R(t)^2dt\ll(H+1)\log^2T\). The convexity factor for the product of the two zeta functions at the microscopic shifts is \(T^{1/2+\epsilon}\) uniformly over the strip. The Dirichlet mean-value estimate, followed by Sobolev in \(\sigma\) with one fixed log cost per derivative, gives
\[
 \int_I \sup_{\sigma_L\le\sigma\le\sigma_R}|P(\sigma+it)|^2dt
 \ll Hy(\log T)^C,
 \qquad y=Y^{4b},
\]
because \(H>y\). The reflected polynomial obeys the same bound. Multiplying the two \(L^2\) bounds using \(\|r_\pm\|_\infty\ll H^{-1}\) bounds the averaged horizontals by \(T^{1/2+\epsilon}\sqrt y\). Gamma-factor connectors use a bounded logarithmic factor in place of \(R(t)\) and obey the same bound. This justifies averaging over the entire endpoint density, including arbitrary approaches to the good-height exceptional set. Bounds are uniform for the complex shifts, with \(a_T-1\) chosen as a sufficiently large fixed multiple of \(1/\log T\).

All differentiated quantities before the saddle approximation can be defined as holomorphic functions of the shifts on a common microscopic polydisk, using the real time convolution above. The vertical contour is absolutely convergent on its right line after expanding the Dirichlet series. The local horizontal bound gives domination independent of the shifts, and the weighted zero sum is finite. To estimate a holomorphic remainder by Cauchy the tapered arithmetic cutoff must use the real unshifted argument \(w_T(2\pi m/k)\). The intermediate cutoff with an imaginary-part translation is only used for a pointwise comparison, as below.

## Saddle normalizer and errors

From the journal convention \(\zeta(s)=\chi(s)\zeta(1-s)\), the factor expanding \(\zeta(1-s+\beta)\) is \(\chi(1-s+\beta)\). The line below (27) uses the reciprocal convention in its written symbol, while Lemma 7 uses \(\chi(1-s)\) and the correct saddle sign. Replacing \(s\) by \(s-\beta\) on the weighted parameter line is a direct reparametrization. It gives real line \(c'=a_T-\Re\beta\) and weight \(w_T(t+\Im\beta)\); no weighted contour deformation is needed. With \(x=m/k\) the resulting face integral is
\[
 \frac{1}{2\pi}\int_{\mathbb R}
  \chi(1-c'-it)x^{-c'-it}w_T(t+\Im\beta)\,dt.
\]
The outer coefficient is \(c_k k^{-1+\beta}B_\beta(m)m^{-\beta}\) as in the adjudication. This change preserves absolute Dirichlet convergence by the fixed shift margins.

Uniform vertical Stirling for \(t\asymp T\) has amplitude \(x^{-c'}(t/2\pi)^{c'-1/2}(1+E(t))\), with \(E^{(j)}(t)=O_j(T^{-1-j})\), and phase \(t\log(t/(2\pi x))-t-\pi/4\). At \(t_0=2\pi x\) the second derivative of the phase is \(1/t_0\). The saddle amplitude there is \(x^{-1/2}\), and multiplying this by \(\sqrt{2\pi t_0}/(2\pi)\) gives one. The Fresnel phase \(e^{i\pi/4}\) cancels the Stirling phase, leaving \(e(-x)\).

For \(x\asymp T\), write \(t=Tu\) and \(u_0=2\pi x/T\). The exact signed-root change maps the normalized phase increment to \(v^2/2\). Since the second derivative in \(u\) is \(1/u\), on a fixed positive compact interval enclosing the saddle and support the signed-root change and inverse have uniformly bounded derivatives, with first derivatives bounded away from zero. Choose that interval with a guard region around the support so the transformed amplitude extends by zero smoothly even when the saddle misses the support. After absorbing the Jacobian and extracting the factor \(T^{-1/2}\) from the original amplitude, the integral has the form \(T^{1/2}\) times a compactly supported quadratic oscillatory integral, with constant phases and normalizations. If \(\delta=H/T\), its amplitude \(A\) obeys \(\|A^{(j)}\|_1\ll_j\delta^{-j}\). Fourier inversion against the Fresnel kernel yields the error
\[
 O\!\left(T^{-1}\int_{\mathbb R}|\xi|^2|\widehat A(\xi)|\,d\xi\right)
 =O(T^{-1}\delta^{-3}).
\]
For the equality as an upper bound, at \(|\xi|\le\delta^{-1}\) use \(\|A\|_1=O(1)\), and above it use \(|\widehat A(\xi)|\ll \delta^{-4}|\xi|^{-4}\). This argument can be made with a Gaussian damping of the quadratic integral and dominated convergence on the Fourier side. It is uniform in the saddle position and does not introduce a sharp endpoint term. Relative Stirling amplitude correction at the leading term is \(O(T^{-1})\). Replacing \(w_T(t_0+\Im\beta)\) by \(w_T(t_0)\) costs \(O(H^{-1}/\log T)\), uniformly before taking derivatives. This removes the temporary nonholomorphic dependence.

If \(x\) is outside a larger fixed comparable range, the derivative of the distorted phase in the original time parameter is \(\log(t/(2\pi x))\), of absolute value bounded below on the support. Repeated integration by parts gives \(O_j(T^{c'+1/2}x^{-c'}H^{-j})\), since differentiating inverse phase gradients and the Stirling symbol costs \(O_j(T^{-1})\) per derivative or better. Its sum is legitimate. Together with the outer powers, \(x^{-c'}\) gives \(k^{a_T-1}m^{-a_T}\). The \(k\)-sum costs \(O(y)\) by the common coefficient bound, and the \(m\)-sum is bounded by fixed log powers by absolute convergence of the four Dirichlet factors. Thus any sufficiently large fixed \(j\) makes the far-range contribution negligible.

In the comparable range \(m\asymp Tk\), the outer absolute coefficient mass is \(O(T^{1+\epsilon}y)\) by \(|c_k|\le24\), the fixed divisor envelope and the bounded scaled shifts on \(m\ll Ty\). The three resulting exponent bounds come from \(Ty\,T^2/H^3\), \(Ty/T\), and \(Ty/H\), each with a small power loss. Writing \(\theta=4b\), all save a power for \((2+\theta)/3<\kappa<1\) and \(H=T^\kappa\). In particular this choice implies \(\kappa>\theta\). For the two-transition weights one can also sharpen the auxiliary Fourier bound by using \(\|A'\|_1=O(1)\) and \(\|A^{(4)}\|_1=O(\delta^{-3})\), since cutoff derivatives are supported on two intervals of length \(O(\delta)\). Splitting at \(\delta^{-1}\) then yields \(O(\delta^{-2})\) for the Fourier integral. The displayed conclusion already follows from the coarser bound and does not require this sharpening. In the unreflected orientation \(k=1\); the additional numerator convolution has a fixed divisor envelope and the same argument applies.

## Remaining term and sharp zero endpoints

The additive main term and remaining Gauss sum use the **same** real cutoff. The principal term equals the average of the sharp principal terms by Fubini. The Perron variable for one-sided supports ranges between fixed multiples of \(T^{1-\theta}\) and \(T^{1+\theta}\), so the principal analysis retains its zero-free margin on the compact height block. The normalized main coefficients vary by \(O(H\log^C T)\) in unnormalized contour units under the endpoint displacement. The nonprincipal part is exactly the difference of the additive phase and its principal projection, with the auxiliary shift retained in \(B_\beta\). A sufficient estimate is \(o(T\log T)\) on the microscopic product circles, giving \(o(T\log^4T)\) after the three Cauchy derivatives. A real estimate after those derivatives would suffice. The proved saddle and edge errors save a power and tolerate these three derivatives. In the compact-local range every primitive conductor \(q>1\) in the decomposition inherits a band prime divisor of \(k\), so \(q\ge Y^a\). The signed remainder still includes full moduli \(q=k\), where the stated HLZ large-modulus bounds have the square-root threshold.

After differentiation, \(|\zeta'(\rho)|\ll T^\epsilon\) on RH. On a transition of length \(O(H)\), bound the sum of \(|D(\rho)|^4\) using unit-interval Sobolev for \(D^2\) and the \(O(\log T)\) unit zero count. The continuous Dirichlet mean value for \(D^2\) and its derivative costs \(O(T^\epsilon(H+Y^{2b}))\), since its coefficient square sum with weight \(1/n\) is bounded and the derivative costs log factors. This also controls zeros exactly at endpoints and the replacement of the sharp indicator by the smooth cutoff, with \(o(T)\) cost after the derivative weight. For the remote tail, the existing mixed square bound gives \(\sum_{0<\gamma\le t}|\zeta'(\rho)|^2 |D(\rho)|^4\ll t\log^4t\) uniformly for \(t\ge Y\). Partial summation makes its normalized mass beyond \(RY\) tend to zero as \(R\to\infty\), after \(Y\to\infty\). These steps justify the compact-local sufficient formulation for the full strict tail. I found no estimate for the remaining signed nonprincipal sum in the supplied sources. No canonical record was changed.
