# Third independent review of the critical logarithmic Mellin condition

18 November 2026. The sufficient \(p>3\) result passes. The weighted area norm supplies the zero trace and the Dini modulus on the specified central line, and the density argument converges in that same norm. A separated smooth packet example verifies strict enlargement over the union of positive-power Sobolev strip classes. Neither the raw formula at \(p=3\) nor optimality is decided. [Proposed proof](analytic135_critical_log_mellin_repair.md) · [Second review](weighted135_critical_log_repair_review.md)

## Spectral trace and endpoint modulus

Let \(w_p(t)=\sqrt{1+t^2}\log^p(e+|t|)\), with \(p>3\), and take the excess norm strip inside the strip where the Mellin integral represents \(h\). Fixed-radius disk submean of \(|h|^2\) bounds its cell supremum by the square root of the local weighted strip energy divided by \(w_p(n)^{1/2}\), up to a constant depending on the radius and \(p\). Weight comparability holds uniformly for \(|t-n|\le5/4\) because both the square-root factor and the shifted logarithm are comparable under bounded translations. Expanded height cells of length at most \(3/2\) have overlap at most two. The unconditional zero count with multiplicities costs \(O(\log(2+|n|))\) per half-open cell \([n,n+1)\). Applying Cauchy–Schwarz to the cell contributions leaves the scalar sum
\[
 \sum_{n\in\mathbb Z}\frac{\log^2(2+|n|)}{w_p(n)}.
\]
It converges for \(p>3\). For \(|\Im\rho|\ge T\), the contributing cells lie in \(|n|>T-1\), as with the polynomial Sobolev weight. The scalar tail is \(O_p(\log(2+T)^{3-p})\) by the integral test for \(1/(t\log^{p-2}t)\). Taking the square root yields the stated exponent \((3-p)/2\) and does not invoke RH.

Disk submean integrated in height controls the weighted norm on each fixed interior vertical line. One may for example use all lines in \([-\epsilon/2,1+\epsilon/2]\) and a radius strictly smaller than \(\epsilon/2\). This provides the central trace \(h(1/2+it)\) even if the only initial square-integrability information was the area integral. For \(F(u)=e^{u/2}f(e^u)\), the positive-phase Fourier transform is that trace. Since \(w_p^{-1}\) is integrable, its transform is in \(L^1\) by Cauchy–Schwarz and the inverse agrees with the original continuous profile. For \(R=1/|v|\) and small \(|v|\), the square of the difference bound is proportional to
\[
 \int_{\mathbb R}\frac{\min(4,|v|^2t^2)}{w_p(t)}\,dt.
\]
The regions below \(\sqrt R\), between \(\sqrt R\) and \(R\), and above \(R\) contribute respectively \(O(R^{-1})\), \(O_p(\log^{-p}R)\), and \(O_p(\log^{1-p}R)\). The resulting modulus \(O(\log(e/|v|)^{(1-p)/2})\) is Dini for \(p>3\). The matching thresholds are those of these sufficient majorants. Their divergence at the boundary is not a counterexample to the raw formula.

At the archimedean endpoint use \(x=e^u\). The numerator of the compensated term is \(e^{-u/2}(F(u)+F(-u))-2e^{-2u}F(0)\), bounded by a constant times the common Dini modulus plus \(O(u)\) as \(u\downarrow0\). Multiplication by \(e^{2u}/(e^{2u}-1)\) is integrable there. Exterior interior-line traces separately give the endpoint value decay \(f(x)\ll N_p(h)x^{\epsilon/2}\) below 1 and \(f(x)\ll N_p(h)x^{-1-\epsilon/2}\) above 1. These control the ordinary integrals, the prime sum, and the compensated term away from 1. The corresponding bounds for differences show continuity of every term in the strip norm on this class.

## Density in the full strip norm

The square-root weight \(m_p=w_p^{1/2}\) is moderate: \(m_p(t+v)\ll_p m_p(t)m_p(v)\) by the polynomial bracket inequality and \(\log(e+|t+v|)\le\log(e+|t|)+\log(e+|v|)\), with both logarithms at least one. For scaled compact smooth cutoffs \(\chi(u/R)\), \(R\ge1\), the Fourier kernels have uniform weighted \(L^1(m_pdt)\) norms after changing variables. Weighted Young yields uniform multiplication on each slice. Strong convergence follows first on physical Schwartz profiles by their decay and then on the full slice by weighted Fourier density. Dominated convergence in the slice parameter proves convergence of the full excess strip norm.

At fixed cutoff, mollify the central profile by \(\varphi_\tau\). The general slice sees the convolution kernel \(e^{(\beta-1/2)u}\varphi_\tau(u)\); its ordinary \(L^1\) norm is uniformly bounded, and the Fourier multiplier tends pointwise to one. Integrated dominated convergence again applies to the full strip norm. The approximants are smooth with compact log support, so the classical compact smooth explicit formula applies. The norm-continuity estimates above permit the two limits. No differentiability or independent central-line Sobolev premise enters this density argument. A compact jump test from Bombieri–Lagarias has no continuous central Fourier representative and remains covered by its separate symmetric midpoint argument. [Earlier Sobolev adjudication and pinned formula](uniform133_mellin_repair_adjudication.md)

## A smooth witness of strict enlargement

Fix \(0<\epsilon<1\) and a nonzero nonnegative \(\psi\in C_c^\infty((-1/8,1/8))\). Define
\[
 \Gamma_j=2^{j^2},\qquad
 a_j=\Gamma_j^{-1/2}[\log(e+\Gamma_j)]^{-p/2}j^{-2}e^{-2j},
 \qquad
 F(u)=\sum_{j\ge1}a_j\psi(u-j)\cos(\Gamma_j u),
 \qquad f(x)=x^{-1/2}F(\log x).
\]
The packets have disjoint physical supports. The sum is locally finite and \(f\) is smooth at every \(0<x<\infty\). It vanishes near zero and is \(O(x^{-5/2})\) at infinity, since the coefficient on the lone supported packet is \(O(e^{-2j})\) and \(u=j+O(1)\). Thus the value hypothesis holds with \(\delta_0=1\). No bounded derivative at infinity is needed. Smoothness on the open half-line does not impose such an endpoint bound.

Put \(b=\beta-1/2\), with \(-1/2-\epsilon\le b\le1/2+\epsilon\). A slice packet's weighted Fourier norm is
\[
 \ll a_j e^{bj}m_p(\Gamma_j)
 \ll j^{-2}e^{-(2-b)j},
\]
by modulation and moderation, since the transforms of \(e^{bu}\psi(u)\) are uniformly Schwartz for this compact \(b\)-range. The translation contributes only a unit phase after extracting \(e^{bj}\). The bound is summable uniformly, giving the required finite area norm.

For the positive-phase Fourier convention, restrict to \(|t-\Gamma_j|\le1\) and remove the phase \(e^{i(t-\Gamma_j)j}\) from the matching carrier. Its remaining real part is bounded below by a fixed positive multiple of \(a_je^{bj}\) because \(\psi\ge0\), \(e^{bu}>0\), and \(\cos((t-\Gamma_j)u)\) is positive on the bump support. All other signed carriers, including the same packet's opposite sign, are at distance \(\gg\Gamma_j\) from these intervals for large \(j\). Their combined absolute contribution is \(O_M(\Gamma_j^{-M})\), from the uniform Schwartz bounds and \(\sum_i a_i e^{bi}<\infty\) uniformly in \(b\). It is \(o(a_je^{bj})\) uniformly on the norm strip: the leading carrier has only the loss \(\Gamma_j^{-1/2}\) times powers of \(j\) and an exponential in \(j\), while \(\Gamma_j^{-M}\) decays as an exponential in \(j^2\).

Hence for any fixed \(s>1/2\) the polynomial Sobolev area norm has a lower bound by a positive constant times
\[
 \sum_j \Gamma_j^{2s}a_j^2 e^{-3j}
 =
 \sum_j \Gamma_j^{2s-1}[\log(e+\Gamma_j)]^{-p}j^{-4}e^{-7j}
 =\infty.
\]
We used \(b>-3/2\) and the fixed positive width of the carrier intervals. The same lower bound works on every narrower positive-area strip inside the specified one. Conversely, \(w_p(t)\ll_{p,s}(1+t^2)^s\) for each \(s>1/2\), so every former strip class embeds in the logarithmic one. This is a strict enlargement within smooth physical tests satisfying the original value bounds.

No canonical record was changed. The proof is unconditional and asserts only sufficiency of the stated condition, with no endpoint, sharpness or source-priority claim.
