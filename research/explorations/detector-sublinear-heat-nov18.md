# Sublinear heat preserves the native signed growth exponent

Let \(w(u)=5c_{e^u}(2)+3c_{e^u}(3)\), extended by zero to \(u<0\), and let \(H(t,u)=(G_t*w)(u)\) with Gaussian variance \(2t\). Write \(\theta=\sup_\rho\Re\rho-1/2\). The [linear heat calculation](detector-diffusion-nov18.md) gives global positivity for \(H(\epsilon u,u)\) at every \(\epsilon\ge10^{-6}\). The following statements address the narrower, nonstationary smoothing range.

Let \(\tau(u)>0\) be continuously differentiable for large \(u\), with
\[
 \tau(u)=o(u),\qquad \log^+(1/\tau(u))+\log^+|\tau'(u)|=o(u).
\]
Extend it continuously and positively to all real centers, bounded and constant on the negative half-line. Put \(h(u)=H(\tau(u),u)\). For every fixed \(0\le r<1\) and either sign,
\[
 \boxed{\quad
 \lim_{T\to\infty}\frac1T\log\!\left(1+\int_{rT}^T h(u)_\pm\,du\right)=\theta .
 \quad}                                                     \tag{1}
\]
In particular, subpower negative mass at arbitrarily sparse unbounded horizons for any such smoothing curve implies RH. Under RH the subpower bound holds throughout. This is an ordinary limit for each sign. No zero simplicity is assumed.

## Positive transfer from the sublinear curve

For each fixed \(b>\theta\), the [three-circles and shifted inversion proof](detector-positive-isolation-nov18.md) gives \(|w(v)|\ll_b e^{bv}\) for \(v\ge0\). Gaussian integration with exponential tilt shows that for every \(b>\theta\),
\[
 |h(u)|+|h'(u)|\ll_b e^{bu}\quad(u\ge1).
\]
Indeed use the native bound with any \(b_0\in(\theta,b)\). Tilt the Gaussian by \(e^{b_0 v}\), gaining the factor \(e^{b_0u+b_0^2\tau}\). The spatial derivative costs \(O_{b_0}(1+\tau^{-1/2})\); the time derivative costs \(O_{b_0}(1+\tau^{-1}+\tau^{-1/2})\), multiplied by \(|\tau'|\). All extra factors are \(e^{o(u)}\). Also \(h\) is bounded on the negative half-line. These bounds prove the upper part of (1).

For fixed \(\epsilon>0\) and large \(U\) one has \(\tau(U)<\epsilon U\). Start \(X_s=U+\sqrt2 B_s\) with standard Brownian motion and let \(S\) be the first time \(\epsilon U-s=\tau(X_s)\). Continuity gives \(0\le S\le\epsilon U\). The heat equation and optional stopping give
\[
 H(\epsilon U,U)=\mathbb E\,h(X_S).
\]
For justification the heat process \(H(\epsilon U-s,X_s)\) before time \(\epsilon U\) is the conditional expectation of \(w(U+\sqrt2 B_{\epsilon U})\), an integrable random variable. This avoids any derivative assumption on the boundary in the stopping argument itself.

When \(\theta>0\), set \(\lambda(\epsilon)=\sup_\rho\{a+\epsilon(a^2-\gamma^2)\}\), where \(\rho=1/2+a+i\gamma\). As \(\epsilon\downarrow0\) it tends to \(\theta\), by testing any fixed zero and using \(|\gamma|>14\). Once \(\lambda>0\), the finite-rectangle expansion in the diffusion note supplies peaks of each sign of magnitude at least \(c_\epsilon e^{\lambda U}\) in every sufficiently long fixed interval of large centers. Coincident leading real parts are handled by the nonzero mean-zero trigonometric polynomial there.

Fix small \(\eta>0\), \(b>\theta\). The reflection principle and Cauchy–Schwarz, with \(D=\sup_{s\le\epsilon U}|X_s-U|\), give
\[
 \mathbb E[|h(X_S)|\mathbf1_{D>\eta U}]
 \ll_b \exp\{(b+2b^2\epsilon-\eta^2/(8\epsilon))U\}.
\]
Indeed \(\mathbb P(D>y)\le4e^{-y^2/(4\epsilon U)}\), and the exponential moment of \(D\) is bounded by four times the corresponding positive Gaussian exponential moment by the reflection bound on each one-sided maximum. For each fixed \(b,\eta\), take \(\epsilon\) sufficiently small to make this exponent negative. At each linear-heat peak of either sign there is therefore a point of the same sign on the sublinear curve within \(\eta U\) with magnitude \(\gg_\epsilon e^{\lambda U}\).

For every large \(T\) take such a peak within bounded distance of \((1-2\eta)T\), with \(\eta\) small in terms of \(r\). Its sublinear point lies a positive fraction of \(T\) inside \([rT,T]\). The derivative bound transfers half its magnitude to an interval of length \(\gg \exp(\lambda U-bT)\), decreasing the implied constant if necessary. Hence the lower exponential rate for the integral is at least \(2\lambda(1-2\eta)-b\). First let \(\epsilon\downarrow0\), then \(\eta\downarrow0\) and \(b\downarrow\theta\). This proves (1). When \(\theta=0\) the nonnegative logarithm supplies the lower bound.

## A logarithmic heat time separates multiplicity from zero location

Take \(\tau(u)=c\log(2+u)\) at positive centers, for fixed \(c>0\). Then
\[
 \inf\{c>0:H(c\log(2+u),u)>0\text{ eventually}\}
 =
 \begin{cases}
 \displaystyle\sup_{\rho}\frac{(m_\rho-2)_+}{\gamma^2},&\mathrm{RH},\\[3pt]
 +\infty,&\text{otherwise}.
 \end{cases}                                                 \tag{2}
\]
If \(c>\sup_\rho (m_\rho-1)_+/\gamma^2\) and RH holds, then
\(H(c\log(2+u),u)=Au+B+O_c(u^{-d})\) for some \(d>0\), where \(A,B\) are the native affine coefficients. In particular, with the explicit choice \(c=5\cdot10^{-24}\), eventual strict positivity is equivalent to RH.

Here is the proof under RH. For \(u\ge2\), invert on \(\Re s=1/u\). Shifting from the absolute convergence line is justified first at each fixed \(u\) by the zero-free half-plane reciprocal bound and the Gaussian factor. For \(|t|\ge2\),
\[
 |1/\zeta(1/2+1/u+it)|\le \exp(C\log(2+|t|)\log(2u)).
\]
For this uniform estimate use the local partial fraction formula for \(\zeta'/\zeta\) in a fixed strip, subtracting the \(O(\log(2+|t|))\) nearby zero terms before horizontal integration from \(2+it\). Each endpoint distance at the left is at least \(1/u\) under RH, while the starting distances are bounded above by an absolute constant. Bounded heights follow from compactness and the finite orders of the poles. Consequently for every \(K>0\) the part of the integral with \(|t|>H_K\) is \(O_{c,K}(u^{-K})\) on choosing the fixed height sufficiently large: the Gaussian factor \((2+u)^{-ct^2}\) dominates the displayed bound, leaving an integrable tail. On the remaining finite rectangle shift left to a small fixed negative real part, with \(H_K\) chosen away from ordinates. The horizontal integrals obey the same power saving since \(e^{u\Re s}\le e\) there and the finite segments are pole-free; the left side decays exponentially. The pole at zero supplies \(Au+B\). Every crossed critical pole at \(s=i\gamma\) produces
\[
 e^{i\gamma u}(2+u)^{-c\gamma^2}\,
 \big(C_\rho u^{m_\rho-1}/(m_\rho-1)!+
 o(u^{m_\rho-1})\big),
\]
where \(C_\rho\ne0\) is its highest Laurent coefficient. For a simple pole the parenthesis is exactly \(C_\rho\). This follows by taking the residue of \(e^{us+c\log(2+u)s^2}F(s)\). Lower derivatives have lower degree in \(u\), up to powers of \(\log u\). Since \(m_\rho\ll\log(2+|\gamma|)\), only finitely many critical terms can exceed any prescribed power threshold. If every exponent \(m_\rho-1-c\gamma^2\) is below 1, the affine drift dominates. If some exponent exceeds 1, those at the largest exponent give a nonzero real trigonometric polynomial of zero mean; it has both signs bounded away from zero in each sufficiently long fixed interval. These statements give (2) without deciding possible equality at a positive threshold. An upper exponent strictly below zero at every zero similarly gives the stated power-saving remainder. If RH fails, (1) precludes eventual positivity for every \(c>0\).

For the numerical choice, the [Platt–Trudgian census](https://arxiv.org/abs/2004.09765), Section 2, counts disjoint critical-line sign changes until they exhaust the multiplicity-inclusive zero count through \(3\cdot10^{12}\), which also gives simplicity in this range. For a critical zero at height \(\gamma\), the positive real-part Hadamard identity at \(2+i\gamma\) gives \(2m_\rho/3\le\Re \xi'/\xi(2+i\gamma)\). The gamma factor and Euler product give \(m_\rho\le7+\log(1+|\gamma|)\). For detail, \(|\zeta'/\zeta(2+it)|\le\sum_{n\ge2}\log(n)/n^2<1.1\), the two rational terms in the logarithmic derivative have real part at most 1.5 in total, and \(\Re\psi(1+iy)\le3+\log(1+|y|)\) by splitting \(\sum y^2/[n(n^2+y^2)]\) at \(n=|y|\). The term \(-\frac12\log\pi\) decreases the bound. For \(|\gamma|>3\cdot10^{12}\), \((7+\log(1+|\gamma|))/\gamma^2<5\cdot10^{-24}\). Alternatively, the fully reproduced simple-zero prefix through 20000 gives \(c=5\cdot10^{-8}\) without the large census. Neither eventual assertion supplies an effective starting center.

## Reading the right edge one polynomial order below the exponential rate

The same contour gives an unconditional distinction between an attained and an unattained right edge. For \(c>0\) define the actual centered heat residual \(R_c(u)=H(c\log(2+u),u)-Au-B\), with \(\log0=-\infty\). Then
\[
 \limsup_{u\to\infty}\frac{\log|R_c(u)|-\theta u}{\log u}
 =\max_{\Re\rho=1/2+\theta}
       \{m_\rho-1+c(\theta^2-\gamma^2)\},                       \tag{3}
\]
with value \(-\infty\) for an empty edge. The maximum otherwise exists by \(m_\rho\ll\log(2+|\gamma|)\). When the edge is attained the leading residual has positive and negative peaks at this polynomial order in every sufficiently long fixed log window, irrespective of the presence of other zeros arbitrarily close to the right edge.

Indeed invert on \(\Re s=\theta+1/u\). Every zero has horizontal distance at least \(1/u\) from this line by definition of \(\theta\), so the previous local reciprocal estimate applies. For each fixed \(K\), frequencies beyond a sufficiently large fixed height contribute \(O(e^{\theta u}u^{-K})\). At that height and inside that finite rectangle shift the contour slightly to the left of \(\theta\), avoiding all poles strictly to its left. If \(\theta>0\) choose the new real part positive; if \(\theta=0\) the pole at zero contributes exactly the subtracted affine term. The horizontal sides cost \(O(e^{\theta u}u^{-K})\) by the same fixed-height Gaussian saving, while the left side has an exponential gap. For \(\theta>0\) the subtracted affine term also lies below the error. A rightmost pole contributes at its leading order
\[
 e^{\theta u}u^{m_\rho-1+c(\theta^2-\gamma^2)}
 \frac{C_\rho}{(m_\rho-1)!}
 e^{i\gamma[u+2c\theta\log(2+u)]}(1+o(1)).
\]
The maximizing terms thus give a nonzero real trigonometric polynomial with zero mean in the *same* time coordinate \(u+2c\theta\log(2+u)\), whose derivative tends to one. Its two signs occur at uniform positive magnitude on every sufficiently long interval. This proves (3); an empty right edge gives the arbitrary power saving for every \(K\).

When the edge is attained, its smallest positive ordinate \(\gamma_*\) and its multiplicity \(m_*\) are recoverable from the large-\(c\) behavior of (3): for sufficiently large \(c\) its right side is exactly \(m_*-1+c(\theta^2-\gamma_*^2)\). The finite-height gap to the next ordinate and the logarithmic multiplicity bound justify the eventual single pair. Under RH the numerical choice \(c=5\cdot10^{-24}\) already makes the first simple critical pair dominant. Below the verified census all poles are simple, and above it the numerical multiplicity bound gives \(m_\rho-1-c\gamma^2<-1\), far below the first exponent. Consequently under RH one has the explicit leading residual
\[
 R_c(u)=2(2+u)^{-c\gamma_1^2}\Re(C_1e^{i\gamma_1u})
             +o(u^{-c\gamma_1^2}),\qquad
 C_1=\frac{P(1/2+i\gamma_1)}{(i\gamma_1)^2\zeta'(1/2+i\gamma_1)} .
\]
Conversely this asymptotic implies RH by (1). The first residue has a verified enclosure in [the centered detector calculation](detector-nov18.md).

## Shorter windows by stopping from a locally constant heat time

Suppose in addition \(l_T=\sup_{T/2\le v\le2T}|\tau'(v)|\to0\). For every \(D_T=o(T)\) tending to infinity with \(\liminf D_T/(Tl_T)>0\), the integral over \([T-D_T,T]\) still gives the exact limit (1); interpret the quotient as infinity when \(l_T=0\). For instance if \(\tau(u)=u^p\), \(0<p<1\), **any** fixed positive multiple of \(T^p\) suffices. At logarithmic heat time, every arbitrarily slowly diverging log-window length suffices. If \(Tl_T=O(1)\) and the right edge is unattained, every fixed window length \(D>0\) suffices. If the positive right edge is attained and \(Tl_T=O(1)\), every sufficiently long fixed window suffices. The zero-exponent case already follows from the global upper bound.

To prove this for \(\theta>0\), fix an off-line target \(s_0=a+i\gamma\), \(a>0\), with its smooth compact positive isolating kernel \(K\) and safe line \(0<\alpha<a\) from the isolation note. Put \(D=D_T\), \(x_*=T-D/2\). For the moment take \(D\) larger than a fixed multiple of the support length of \(K\) plus one period of the target. Freeze the heat time at
\[
 t_T=\max_{|v-x_*|\le D/3}\tau(v).
\]
It is \(o(T)\). On convolving \(H(t_T,\cdot)\) with \(K\), the contour crosses just the selected pair; the left error is \(O(e^{\alpha v+\alpha^2t_T})\), since the Gaussian factor on the left line further damps the integrable transform of \(K\). The target contribution at \(v=x_*+O(1)\) is a nonzero conjugate pair of size \(e^{av+(a^2-\gamma^2)t_T}v^{m-1}\), times its cosine phase, with relative coefficient error \(o(1)\) before taking real parts. In fact the derivative factor is \((v+2s_0t_T)^{m-1}=v^{m-1}(1+o(1))\); all lower terms are relatively \(o(1)\). Keeping \(t_T\) frozen while moving the center through one period produces both signed peaks of size \(e^{aT-o(T)}\). Positivity of \(K\) gives peaks of the frozen heat function itself within a fixed support-length of those centers. Locate both within \(|v-x_*|\le D/8\) by enlarging the required constant multiple of the support and period. Translation of \(K\) can center its support.

Start the backward heat process from such a point \((t_T,v)\) and stop at the graph of \(\tau\). Let the protected region be \(|x-x_*|\le D/3\). If the process exits before stopping, it exits by time \(s_*=(2D/3)l_T\), since this bounds the oscillation of \(\tau\) on the protected region. For \(l_T=0\) the transfer is immediate. Otherwise the exit probability is at most \(4\exp[-c_0 D/l_T]\) by reflection, with an absolute \(c_0>0\); the starting distance to the boundary is at least \(5D/24\). The total stopping time is at most \(t_T=o(T)\). Cauchy–Schwarz and the Gaussian maximum bound used above therefore give an exceptional contribution to the expectation of \(|h|\) of at most
\[
 \exp\{bT+o(T)-c_0 D/(2l_T)\}\qquad(b>\theta).
\]
Choose \(a\) sufficiently close to \(\theta\) and \(b\) sufficiently close above it so that \(b-a<(c_0/2)\liminf D/(Tl_T)\). The frozen signed peaks then force peaks \(e^{aT-o(T)}\) of \(h\) inside the protected region. The derivative argument gives integrated lower exponent \(2a-b\) inside \([T-D,T]\). Sending \(a,b\) to \(\theta\) proves the claim for diverging \(D\), since every fixed target kernel and period fit eventually. For fixed \(D\) and unattained edge, choose targets approaching the edge with arbitrarily short combined support and period, as proved in the isolation note. For an attained edge take \(a=\theta\) with its fixed kernel and period, then let \(b\downarrow\theta\). This proves the fixed-window assertions.

## Constant heat and the growth of reciprocal derivatives

There is also an exact diagnostic at fixed heat time \(t>0\). The infima of \(t\) for each of the following three centered conditions coincide:
\[
 H(t,u)-Au-B=O(1),\quad
 \int_0^T|H(t,u)-Au-B|\,du=O(T),\quad
 \int_0^T(H(t,u)-Au-B)_-\,du=O(T).
\]
If RH or simplicity fails, all three infima are \(+\infty\). Under RH and simplicity they equal
\[
 L=\limsup_{\gamma\to\infty}
    \frac{\log^+|P(\rho)/((\rho-1/2)^2\zeta'(\rho))|}{\gamma^2}.
\]
This includes \(L=0\) and \(+\infty\). In particular reciprocal derivatives growing at most like \(e^{C\gamma^2}\) imply eventual strict positivity after a sufficiently large *constant* heat time, under RH and simplicity.

For necessity assume only the last one-sided bound. The unilateral transform of the centered row equals
\[
 D_t(s)=e^{ts^2}F(s)-A/s^2-B/s-\int_{-\infty}^0 e^{-su}H(t,u)du
\]
initially in \(\Re s>1/2\). The last integral is entire by the Gaussian left tail. At zero the combined transform is regular because the multiplier is \(1+O(s^2)\). Landau's nonnegative-density argument from the centered detector note gives absolute convergence on \(\Re s>0\) and \(\sup_y |D_t(\sigma+iy)|=O(1/\sigma)\) for \(0<\sigma\le1\), by bounding its total variation transform by \(D_t(\sigma)+2\mathcal L(H-Au-B)_-(\sigma)\). The nonvanishing dyadic multiplier then forces RH and simplicity. Taking radial residues gives \(e^{-t\gamma^2}|C_\rho|\le C_t\) for every ordinate, hence \(L\le t\).

Conversely, if \(t>L\) under RH and simplicity then \(\sum_\rho |C_\rho|e^{-t\gamma^2}<\infty\), by zero counting and the positive Gaussian margin. Invert on the initial line and shift to \(\Re s=-1\) as in the diffusion note. At cofinal safe heights the reciprocal costs at most \(\exp(O(\log^2 |\Im s|))\), dominated by the fixed Gaussian; on the left line the functional equation gives \(F(-1+iy)=O((1+y^2)^{-1})\). The critical residues converge absolutely and uniformly in the real center. Their sum and the \(O(e^{-u})\) remainder give the pointwise bounded condition. This proves the three infima without an assertion at equality.

## An explicit fixed aperture for every possible right edge

Add a secondary term to break any tie between the largest polynomial orders. For any fixed \(c,d>0\), take, for large \(u\),
\[
 t(u)=c\log(2+u)+d\log\log(e+u).
\]
For every fixed \(D>\pi/(3\cdot10^{12})\), however close to that value, the two native heat signs satisfy
\[
 \lim_{T\to\infty}\frac1T\log\!\left(1+\int_{T-D}^T H(t(u),u)_\pm\,du\right)=\theta.
\]
In multiplicative \(X\)-coordinates the aperture is the fixed ratio \(e^D\). The threshold uses the published verified zero census; the independently replayed prefix alone gives \(D>\pi/20000\).

The upper bound and zero-exponent case follow as before. For an unattained positive edge the preceding section applies because \(T l_T=O_{c,d}(1)\). For an attained positive edge use the finite rectangle in (3). Every edge pole now has first exponent \(p_\rho=m_\rho-1+c(\theta^2-\gamma^2)\) in \(u\), and second exponent \(q_\rho=d(\theta^2-\gamma^2)\) in \(\log u\). Among the finitely many maximizing first exponents, the smallest positive ordinate \(\gamma_*\) uniquely maximizes the second. Thus precisely one conjugate pair leads, with common phase \(\gamma_*[u+2\theta t(u)]\) plus a constant and a nonzero amplitude asymptotic to a constant times \(e^{\theta u}u^{p_*}(\log u)^{q_*}\). All remaining terms are relatively \(o(1)\) before taking the real oscillation. The derivative of the phase tends to \(\gamma_*\). Every interval longer than \(\pi/\gamma_*\) therefore contains an interval of uniformly positive length on which each prescribed cosine sign has a uniform positive lower magnitude. Across that interval the exponential scale is comparable to its value at \(T\). Since \(\gamma_*>3\cdot10^{12}\), the claimed absolute aperture suffices in every case. In particular along arbitrarily sparse cofinal horizons, subpower negative mass on **one such short window per horizon** would already imply RH.
