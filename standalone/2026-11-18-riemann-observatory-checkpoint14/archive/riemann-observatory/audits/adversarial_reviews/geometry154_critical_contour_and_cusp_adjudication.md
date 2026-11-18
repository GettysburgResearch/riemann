# Third check of the critical contour and the compact cusp

2026-11-18. The signed inclusive-height formula holds with the critical \(p=0\) strip weight and local \(H^1\) at logarithmic coordinate zero. It therefore holds with every \(p\ge0\). The literal Bombieri–Lagarias conditions (A)(B) imply the required continuity and local regularity once the critical norm is finite. Separately, the continuous compact cusp has finite \(p=3\) strip norm and raw symmetric sums tending to \(+\infty\). It lies outside (A). These are next-round checks with no canonical edits. [Contour construction](weighted152_signed_p1_campaign.md) · [Independent contour reconstruction](uniform153_contour_signed_critical_review.md) · [Cusp construction](uniform147_signed_endpoint_adversarial.md)

## Sharp inversion at the critical weight

Write \(w_0(t)=\sqrt{1+t^2}\), and \(N_0^2=\iint_{\beta\in[-\epsilon,1+\epsilon]}w_0(t)|h(\beta+it)|^2\,dt\,d\beta\), with \(\epsilon\) below the value-decay exponent. Fixed disks in the enlarged strip give the supremum bound \(C_\epsilon N_0/\sqrt{w_0(t)}\) in the inner strip. Integrating the same disk submean inequality in \(t\) gives vertical line norms and uniform tails: the integral for \(|t|>R\) on each inner line is bounded by a constant times the area norm squared on \(|t|>R-r\), where \(r\) is the fixed disk radius. No pointwise tail inference from a single line integral is required.

Let \(F_\beta(u)=e^{\beta u}f(e^u)\). For continuous \(f\), the value envelopes make this family bounded and uniformly continuous in \(u\), uniformly over the compact range of \(\beta\) under discussion. This follows by uniform continuity on a fixed compact \(u\) interval and uniform exponential tails. Gaussian inversion therefore tends to \(F_\beta\) uniformly in \(u,\beta\). For the difference from sharp inversion let \(m_T(t)=\mathbf1_{|t|\le T}-e^{-t^2/T^2}\). Exactly at \(p=0\),
\[
\int |m_T(t)|^2/w_0(t)\,dt
\le \int_{\mathbb R}|\mathbf1_{|v|\le1}-e^{-v^2}|^2/|v|\,dv<\infty.
\]
Near zero the numerator is \(O(v^4)\); outside the compact interval it is Gaussian. On any fixed bounded frequency interval \(m_T\to0\) uniformly; on the complement use the uniform vertical tail above and Cauchy–Schwarz. This proves uniform sharp inversion, without absolute Fourier integrability. A single fixed line argument would already suffice on the contour’s two vertical edges.

## Finite contour, gamma part and limit

I checked Titchmarsh §9.6(A), eq. (9.6.1), printed p. 217, stored PDF p. 113. It gives the local logarithmic derivative for \(-1\le \sigma\le2\) with \(O(\log T)\) remainder. A bounded interval about any target height contains \(O(\log T)\) ordinates counted with multiplicity, so deleting small intervals of radius \(c/\log T\) leaves admissible heights. The local terms have size \(O(\log^2 T)\) on those horizontals. The logarithmic derivative of the completed function adds only \(O(\log T)\) there. Thus the horizontal errors are \(O(N_0\log^2 T/\sqrt T)\) on a rectangle with fixed vertical edges \(1-a,a\), \(a=1+\epsilon/2\), after restricting \(\epsilon\) if necessary. The inclusive cutoff at any other nearby height differs by \(O(N_0\log T/\sqrt T)\), including multiple zeros at the exact endpoint. [Titchmarsh scan](../../sources/selberg_round2/titchmarsh_zeta.pdf)

The left edge is downward. Substitution \(s\mapsto1-s\) and \(\xi'/\xi(1-s)=-\xi'/\xi(s)\) give the positive reflected term \(h(1-a-it)\) on the right edge, alongside \(h(a+it)\). The \(\zeta'/\zeta\) series on \(a>1\) integrates termwise for each finite height by absolute series convergence and boundedness on that finite contour. Its limiting terms after sharp inversion are
\[
-\sum_n\Lambda(n)n^{-a}\big(F_a(\log n)+F_{1-a}(-\log n)\big)
=-\sum_n\Lambda(n)(f(n)+n^{-1}f(1/n)).
\]
Uniform sharp inversion and \(\sum_n\Lambda(n)n^{-a}<\infty\) dominate the exchange. No bound on the unweighted \(L^1\) norm of the vertical transforms is needed.

Set \(Q(s)=1/s+1/(s-1)-\tfrac12\log\pi+\tfrac12\Gamma'(s/2)/\Gamma(s/2)\). On the right line its expansion is \(\frac12\log|t|-\frac12\log(2\pi)+i\frac{\pi}{4}\operatorname{sgn}(t)+O_a(|t|^{-1})\). The remainder is absolutely integrable against the vertical tests by the weighted \(L^2\) estimate. At \(p=0\) the constant and imaginary sign terms cannot be dismissed by assuming absolute integrability or by symmetry of a single right vertical test. On each half-axis localize \(F_\beta\) by a compact smooth cutoff \(\chi=1\) near zero supported in the local \(H^1\) interval. The near transform is absolutely integrable against \(1+\log(2+|t|)\) by \(H^1\) and Cauchy–Schwarz. For the far part put \(G_\beta=\mathcal F_+[(1-\chi)F_\beta/(iu)]\) with \(\mathcal F_+\) using \(e^{itu}\). Then \(G_\beta'=\mathcal F_+[(1-\chi)F_\beta]\). The smooth bounded multiplier \((1-\chi)/(iu)\) and all its derivatives are in \(L^2\), hence its transform is in polynomially weighted \(L^1\). Weighted Young's inequality gives \(G_\beta,G_\beta'\in L^2(w_0)\). Local Sobolev on unit intervals gives \(G_\beta(t)=O(N_0/\sqrt{w_0(t)})\). Integration by parts leaves a vanishing log boundary and an absolutely integrable \(G_\beta(t)/t\) tail. For the constant and sign contributions on each axis the primitive boundary itself vanishes. This proves convergence and continuity of the gamma functional under \(N_0\) plus local \(H^1\).

Cutoff and compact mollification give convergence in the area norm and local \(H^1\): the cutoff acts as a uniformly bounded approximate identity in frequency under the moderate weight, and the compact mollifier acts via its bounded exponentially tilted Fourier multiplier on each line. Choose sufficiently small mollification radii after each cutoff. The original exponential value envelopes persist uniformly, so prime values, poles and the compensator’s far region pass to the limit. Close to \(x=1\) the compensated numerator is \(O(|x-1|^{1/2})\) uniformly, by local \(H^1\). Thus the compact smooth formula identifies the limiting gamma expression with the p. 6 printed compensated arithmetic expression. This avoids using the unrestricted assertion under (A)(B) alone. [Rendered manuscript formula, PDF p. 6](../../sources/uniform121_bombieri_lagarias/bombieri_lagarias_author.pdf#page=6)

## Literal manuscript (A) at \(p=0\)

The \(p>1\) proof used Fourier \(L^1\) inversion to exclude jumps; that argument is unavailable at \(p=0\). The central trace here gives \(F(u)=e^{u/2}f(e^u)\in H^{1/2}(\mathbb R)\). If a first-kind discontinuity has a nonzero jump at \(u_0\), the difference between values on opposite sides is bounded below for \(u_0-\eta<u<u_0<v<u_0+\eta\). The Gagliardo seminorm is then infinite because
\[
\int_0^\eta\int_0^\eta (r+s)^{-2}\,dr\,ds=\infty.
\]
Hence no actual jumps are possible. The prescribed midpoint fixes the point value. The printed first-kind condition on both \(f\) and \(f'\) gives bounded one-sided derivatives locally, so the continuous function is locally Lipschitz across the finite exceptional set, yielding the local \(H^1\) premise. This repairs the continuity inference without weakening the exact manuscript condition or inserting an extra local assumption for tests that satisfy it. [Rendered manuscript (A)](../../sources/director_round15_bl/page5.png)

## Separate compact continuous cusp

Take \(k\) positive, smooth, even, equal to \(1/(|t|\log^2|t|\log\log|t|)\) at large heights. Then \(k\in L^1\cap L^2(w_3)\), and \(\int k(t)\log|t|\,dt=\infty\) at infinity. Let \(K=\mathcal F_+^{-1}k\), \(D=\phi*\tilde\phi\) for a real even nonzero smooth compact bump with nonzero integral, and \(F=DK\). This is continuous, real, even and compact; the associated \(f(x)=x^{-1/2}F(\log x)\) satisfies the endpoint envelopes for all positive exponents. Smoothness away from zero follows from dyadic decomposition of the symbol \(k\), since its \(j\)-th derivatives are \(O_j(|t|^{-1-j})\), and repeated integration by parts controls arbitrary physical derivatives locally away from zero. On the central line \(H=(k*|\widehat\phi|^2)/(2\pi)\ge0\) and \(H(t)\gg k(t)\) for large \(|t|\), by integrating where the fixed nonnegative convolution kernel is positive near zero. On other vertical lines the compact factor is \(e^{(\beta-1/2)u}D\), whose Fourier transform is uniformly Schwartz on the compact strip. Weighted Young supplies finite area norm at \(p=3\).

The cusp has an independent divergence proof by the same *finite* contour, without a local primitive or Selberg estimate. The prime side still converges and the horizontal and arbitrary-height errors still vanish. Move only the folded \(Q(s)[h(s)+h(1-s)]\) right integral to the middle line. The crossed pole at \(1\) gives \(h(1)+h(0)\), and the fixed-length horizontal connectors vanish by the trace estimate. In the middle integral change \(t\mapsto-t\) in the reflected term. Then
\[
Q(1/2+it)+Q(1/2-it)=-\log\pi+\Re\frac{\Gamma'}{\Gamma}(1/4+it/2).
\]
The rational parts cancel, and the last expression is \(\log|t|+O(1)\) for large \(|t|\). Accordingly the middle integral grows to \(+\infty\) for this \(H\ge0\), with the \(O(1)\) integral uniformly bounded by its \(L^1\) norm. The inclusive raw zero sum tends to \(+\infty\) at every height. This proves the claimed result independently of the separate Selberg projection proof.

The archimedean divergence is genuine. Fourier inversion gives \(F(0)-F(u)=\pi^{-1}\int_0^\infty H(t)(1-\cos(tu))dt\ge0\). Tonelli and \(\int_0^{at}(1-\cos v)dv/v=\log t+O_a(1)\) imply \(\int_0^a (F(0)-F(u))du/u=\infty\). In the printed integral, \(x=e^u\) yields
\[
f(e^u)+e^{-u}f(e^{-u})-2e^{-2u}f(1)
=2e^{-u/2}(F(u)-F(0))+O(u).
\]
The exact kernel is \(e^{2u}/(e^{2u}-1)=1/(2u)+O(1)\). The integral before the printed minus sign diverges to \(-\infty\), matching a positive divergence on the spectral side. Local \(H^1\) would make this Dini integral finite, so the cusp violates that local premise and the literal first-kind derivative requirement. This example is distinct from the smooth \(p=3\) absolute-divergence example, which vanishes near one and now has signed convergence. It is also distinct from the smooth raw-height counterexample whose arithmetic side is finite. No assertion about negative \(p\), a weakest local premise, or publication priority follows.
