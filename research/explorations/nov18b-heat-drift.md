# A local lower bound for the surviving heat defect

**Proposed theorem.** Use \(F_u(s)=8H_{4u}((s-1/2)2/i)\), so \(F_0=\xi\). Let \(L=\log(2T)\) and
\[
 e_T=C\,\frac{\log\log L}{\log L}.
\]
For some absolute \(C,B,T_0\), suppose \(\xi(1/2+\delta+iT)=0\), \(T\ge T_0\), \(0<\delta<1/2\), \(u\ge0\), and \(\delta-uL>e_T\). Then \(F_u\) has a zero \(\rho_u\) with
\[
 |\Im\rho_u-T|\le B,\qquad
 \Re\rho_u>1/2+\delta-uL-e_T .                             \tag{1}
\]
In particular the classical de Bruijn–Newman constant satisfies
\[
 \Lambda\ \ge\ \frac{4(\delta-e_T)}{\log(2T)} .
\]
The factor four converts our time \(u\) to Polymath15's time \(t\). The additive loss tends to zero and is independent of the zero configuration. In terms of a fixed positive defect, the predicted time is at least \((4\delta-o(1))/\log T\), with a surviving nearby zero throughout that range. The [disk result](nov18b-heat-persistence.md) applies even to arbitrarily small defects. Both are implications of a hypothetical off-line zero. [Polymath15, Remark 9.4 and §10](https://arxiv.org/abs/1904.12438)

## Slow variation inside a local zero-free half-strip

Write \(G,\alpha,D_u,g_u\) for the quantities in the [growth and anchor calculation](nov18b-heat-persistence.md). We have \(u\le1/L\) throughout. Assume \(1/2\le b\le1\) and that \(F_u(s)\ne0\) for \(\Re s>b\), \(|\Im s-T|<B\), with a sufficiently large fixed \(B\). The classical de Bruijn strip bound in fact excludes any \(\Re s>1\) at positive time automatically. Define the holomorphic branch \(U=\log D_u\) by the branch on \(4+i[T-B,T+B]\) where \(|D_u-1|<0.8\). On the whole substrip \(b+\eta/8\le\sigma\le4\), \(|v-T|\le B-5\),
\[
 |U(\sigma+iv)|\ll L/\eta\qquad(0<\eta<1/8).
\]
Indeed \(\log|D_u|\le CL\) on the fixed disks about \(4+iv\) of radius \(4-b\) by the growth bound, Gaussian normalization and Stirling. Borel–Carathéodory with the bounded anchor \(U(4+iv)\) gives the assertion, taking the open boundary limit.

For \(l=b+\eta/8\) consider the rectangle \([l,4]\times[T-B+5,T+B-5]\). Its right side has \(|U|\le C_1\); the other sides have \(|U|\le M=C_2L/\eta\). For \(k=\pi/[2(B-5)]\), the harmonic function
\[
 h(\sigma,v)=\frac{\sinh(k(\sigma-l))}{\sinh(k(4-l))}\cos(k(v-T))
\]
vanishes on three sides and lies in \([0,1]\) on the right side. The subharmonic maximum principle gives \(\log|U|\le\log M-h\log(M/C_1)\). On \(|v-T|\le B/2\), \(h\gg \sigma-l\) if \(B\ge30\). Taking
\[
 \eta=K\,\frac{\log\log L}{\log L}
\]
with a sufficiently large absolute \(K\), the half-strip \(b+\eta\le\sigma\le 3\), \(|v-T|\le B/2\) therefore has \(|U|\ll L/(\log L)^{12}\). We enlarge \(T_0\) so \(\eta<1/8\). Cauchy's estimates in radius \(\eta/4\) give on \(b+2\eta\le\sigma\le2\), \(|v-T|\le B/2-1\),
\[
 |U'|+|U''|\ll L/(\log L)^9 .                              \tag{2}
\]
The constants in these estimates can be taken uniformly for all sufficiently large fixed \(B\): the displayed \(h\gg\sigma-l\) is uniform there.

## Inverting the heat flow at the displaced saddle

Let \(s=1/2+\delta+iT\), take \(b=1/2+\delta-uL-4\eta\), and suppose \(b\ge1/2\). If no zero in (1) exists with \(e_T=4\eta\), the preceding bounds apply at this \(b\). Set \(f=\log F_u\) on the relevant rectangle. Then \(f'=\alpha+2u\alpha\alpha'+U'\), where \(\alpha=\tfrac12\log(T/(2\pi))+i\pi/4+O_B(1/T)\) on its bounded central region with imaginary coordinate \(T+O(B)\) (variation in that approximation is \(O_B(1/T)\)), and \(\alpha'=O(1/T)\), \(\alpha''=O(1/T^2)\). The center
\[
 s_c=s-2u\alpha(s)
\]
has real part \(b+4\eta+O(1/L)\). By (2) the map \(w\mapsto s-2u f'(w)\) maps the closed disk of radius \(\eta/4\) about \(s_c\) strictly into itself and has Lipschitz constant \(o(1)\) there. Let \(s_*\) denote its fixed point and \(h_*=(s_*-s)/i=2iu f'(s_*)\). In particular \(|\Re h_*|\ll u(1+L/(\log L)^9)\), \(|\Im h_*|=O(1)\).

Translate the full real line in the reverse Gaussian integral \(\xi(s)=\int g_u(h)F_u(s+ih)\,dh\) to \(h_*+\mathbb R\). The vertical integrals at the two ends tend to zero by (2) of the [companion proof](nov18b-heat-persistence.md), uniformly on the bounded imaginary shifts involved. Divide by the nonzero factor \(e^{-h_*^2/(4u)}F_u(s_*)\). For \(|x|\le\eta/4\), the resulting exponent is
\[
 -x^2/(4u)-h_*x/(2u)+f(s_*+ix)-f(s_*)
     =-x^2/(4u)+O(x^2 L/(\log L)^9).
\]
The linear terms cancel exactly. Its normalized integral differs from 1 by \(o(1)\), since \(u\le1/L\), \(\eta^2/u\to\infty\), and the Gaussian dominates the stated error.

For \(\eta/4\le |x|\le B/2-2\), Stirling at fixed real part, together with the bound on \(U\), gives
\[
 \log|F_u(s_*+ix)/F_u(s_*)|\le O_B(1)+O(L/(\log L)^{12}) .
\]
The additional linear term in the Gaussian costs at most \(C(1+L/(\log L)^9)|x|\). Both losses are \(o(x^2/u)\) uniformly in this range. The normalized contribution is \(o(1)\).

For \(|x|>B/2-2\), the global growth bound gives \(\log|F_u(s_*+ix)/F_u(s_*)|\le C(L+|x|+u\log^2(2+|x|))\). For the denominator use the lower bound for \(\Re U(s_*)\) and Stirling. Here \(C\) is absolute, independent of \(B\), after increasing \(T_0(B)\): the real parts involved stay in a fixed strip and \(|\Im s_*-T|=o(1)\). First choose \(B\) large enough in terms of this global growth constant. Then the Gaussian, even including the preceding linear loss, leaves an integrable bound \(e^{-x^2/(8u)}\). This last region also costs \(o(1)\) in the normalized integral. Thus \(\xi(s)\ne0\), which proves (1) by contradiction. At \(u=0\) the conclusion follows from the original zero itself.

This is a one-sided propagation result. To turn it into a resolution of RH one would need an upper bound excluding the heat zeros that (1) forces, at times arbitrarily close to zero.
