# Explicit weighted curvature for the smooth totient moment kernel

Let \(L=\log x\ge1000\), \(s=xL\), and
\[
 h(u)=1-\frac{\log(1+(e^u-1)(1-e^{-u})^s)}u\quad(u>0),\qquad h(u)=1\quad(u\le0).
\]
With \(\kappa=-h''-h'\) the following uniform estimate holds:
\[
 \int_{\mathbb R}e^{u/2}|\kappa(u)|du<1.70\sqrt x .
\]
In particular the total contribution from any verified subset of critical-line zeros to \(\sum_\rho\int_{\mathbb R}h(u)e^{\rho u}du\) is less than \(0.080\sqrt x\), counting both signs and multiplicities. Integration by parts twice gives the factor \(1/[\rho(1-\rho)]\). On the critical line this is positive real, and the real parts of these weights are positive for all zeros in the strip. Their total is \(2+\gamma_E-\log(4\pi)<0.047\) by the xi product.

Put \(d=(e^u-1)^{-1}\), \(p=(s+1)d\), \(z=u+(s+1)\log(1-e^{-u})\), so \(z'=1+p\), \(z''=-p(1+d)\), \(z'+z''=1-pd\). Write \(F(z)=\log(1+e^z)\), \(f=F'\), \(K=F''=e^z/(1+e^z)^2\). On \(0<u\le L\) use \(h=1-F(z)/u\). On \(u\ge L\) use \(h=h_0-F(-z)/u\), where \(h_0=(s+1)b/u\), \(b=-\log(1-e^{-u})\). These are pointwise representations of the same smooth function, so the split creates no interface mass. At zero the extension is continuously differentiable with derivative zero.

Both transition curvatures have leading term \(K(z)(1+p)^2/u\). The lower-order terms in absolute value are at most
\[
 f(\pm z)\big(|1-pd|/u+2(1+p)/u^2\big)
       +F(\pm z)(u+2)/u^3
\]
with the sign chosen on the corresponding side. On \(|u-L|\le1\),
\[
 e^{(u-L)/2}\frac{1+p}{u}\le
 \frac{e^{1/2}}{L-1}+
 \frac{(L+e^{-L})e^{1/2}}{(L-1)(1-e^{1-L})}<1.66 .
\]
Changing variables to \(z\) and using \(\int K=1\) bounds the normalized weighted leading mass there by 1.66. On the same interval \(1+p<2.73L\), \(|1-pd|\le1\), and \(F(\pm z)<1\) on the respective sides, because \(z\) increases and \(-0.01<z(L)<0\). Thus the lower-order transition terms are bounded pointwise by \(0.0066\), and their normalized weighted mass is at most \(2e^{1/2}(0.0066)<0.022\).

For \(u\ge L\), \(b\le d\le1.001e^{-u}\) and
\[
 0\le (h_0''+h_0')/(s+1)
 =d^2/u+(2d-b)/u^2+2b/u^3 .
\]
Its normalized weighted integral is at most
\[
 (s+1)\left(0.67e^{-2L}/L+4.02 e^{-L}/L^2\right)<0.0041 .
\]
For \(u\ge L+1\), \(z\ge u-(s+1)d\ge u-0.37L\), \(1+p\le L\), and all three transition factors \(F(-z), f(-z), K(z)\) are at most \(e^{-z}\). The upper-tail transition curvature is consequently at most \(2L e^{-u+0.37L}\), with normalized weighted mass less than \(4Le^{-0.63L}<0.001\).

For \(1\le u\le L-1\) put \(y=(s+1)e^{-u}\ge eL\). Here \(d\le1.59e^{-u}\), \(p\le1.59 y\), \(|1-pd|\le1+y\), and the three lower-side transition factors are at most \(e^{u-y}\). The curvature is at most \(20(1+y)^2e^{u-y}\). Its normalized weighted integral is bounded by \(20e^L(eL+4)e^{-eL}<0.001\), by \(du=-dy/y\). For \(0<u<1\), use \(d\le1/u\) and \(e^z\le e u^4(1-e^{-1})^{s-3}\) in the same curvature formula. Its normalized weighted integral is at most \(40e(s+2)^2(1-e^{-1})^{s-3}<0.001\). Adding the six bounds gives the claim.

## Wider holomorphic strip and the upper cutoff

For \(1000\le L\le4{,}300{,}000\) and \(0<\beta<1\) one has the explicit high-frequency estimate
\[
 \left|\int_{\mathbb R}\kappa(u)e^{(\beta+i\gamma)u}du\right|
 \le 600000 L+3+70000 L^6\exp(L-3.10|\gamma|/L).             \tag{1}
\]
We give the details of the wider strip used in [the finite sign theorem](abundance-finite-horizon-nov18.md). Take \(w=u+iv\), \(u\ge0.9\), \(|v|\le3.12/L\). The branch of \(\log(1-e^{-w})\) is principal throughout. Write \(z=w+(s+1)\log(1-e^{-w})\).

* For \(0.9\le u\le10\) the inequality \(2\cos v-e^{-u}>1.5\) gives \(\log|1-e^{-w}|\le-0.75e^{-u}\), hence \(\Re z\le10-0.75(s+1)e^{-10}<-2\). For \(10\le u\le L-0.002\) one has \(2\cos v-e^{-u}>1.99994\), giving \(\log|1-e^{-w}|\le-0.99997e^{-u}\). The largest possible real part of \(z\) here is bounded by \(L-0.002-0.99997Le^{0.002}<-1.96\). Thus the small-\(e^z\) power-series patch has \(|e^z|<0.15\) on the entire left.
* For \(|u-L|\le0.002\), integrate the analytic logarithm vertically from the real axis. This gives \(|\Im z|\le(3.12/L)(1+(s+1)/(e^u-1))<0.00312+3.12(1.000001)e^{0.002}<3.132<\pi\). Therefore the principal logarithm of \(1+e^z\) is valid. Its modulus satisfies \(|1+e^z|\ge\cos(3.132/2)(1+e^{\Re z})>0.004(1+e^{\Re z})\). Also \(\Re z\le u\) because \(2\cos v>e^{-u}\). Consequently \(|\log(1+e^z)|\le u+10\) here.
* For \(u\ge L+0.002\), use \(|\log(1-e^{-w})|\le e^{-u}/(1-e^{-u})\). Then \(\Re z\ge u-(s+1)/(e^u-1)\ge L+0.002-1.000001Le^{-0.002}>1.99\), and \(|e^{-z}|<0.15\). Use the branch \(z+\log(1+e^{-z})\). On each overlap the branches agree by analytic continuation from the real axis; all boundary inequalities are strict, giving open overlap collars. All estimates cover both halves of the strip by their dependence on \(|v|\), equivalently by conjugation.

These patch estimates give \(|h(w)|<3\) uniformly. On the left use \(|\log(1+e^z)|<0.17\). In the middle use the displayed bound and \(u\ge L-0.002\). On the right the numerator of \(h\) is bounded by \((s+1)/(e^u-1)+0.17\). For \(u\ge1\), \(|v|\le3.10/L\), Cauchy at radius \(0.01/L\) thus gives \(|\kappa(w)|<61000L^2\).

Take \(U=L+4\log L\). On every radius-\(1/4\) disk about a point with \(u\ge U\) on the smaller strip, \(|(s+1)e^{-w}|<2/L^3\) (using \(s+1=(1+1/s)Le^L\)). The right-hand patch continues throughout the disk by its small-exponential series. Expanding there gives \(h(w)=s e^{-w}/w+O(20(s+1)^2 e^{-2\Re w}/|w|)\); for example expand each logarithm in the numerator \(-(s+1)\log(1-e^{-w})-\log(1+e^{-w}(1-e^{-w})^{-(s+1)})\), using \(|(s+1)\log(1-e^{-w})|<0.01\). Cauchy differentiation of the remainder on the disk gives
\[
 |\kappa(w)|\le s e^{-u}(u^{-2}+2u^{-3})+2000(s+1)^2e^{-2u}.
\]
The tail integral against \(e^{\beta u}\) is at most \(s(U^{-1}+U^{-2})+2000(s+1)^2e^{-U}<3e^L\). From 1 to \(U\) the strip bound costs at most \(61000L^2e^U=61000L^6 e^L\), using \(e^{\beta u}\le e^u\). Shift the ray upward or downward according to the sign of \(\gamma\). Its connector at 1 costs less than \(e(61000L^2)(3.10/L)<600000L\), while the end at infinity vanishes by the displayed tail. The real segment through 1 contributes less than 3 by the small-\(u\) estimate above (in particular \(|\kappa|<1\)). This proves (1).

At \(H=3\cdot10^{12}\), \(L/2-3.10H/L<-12790\) throughout the stated interval by monotonicity. Thus the last term in (1), divided by \(\sqrt x\), is below \(70000(4.3\cdot10^6)^6e^{-12790}\). With the published reciprocal-square tail \(<3.1\cdot10^{-12}\), the full omitted zero contribution, including the connector and the small real segment, is less than \(0.001\sqrt x\). The uniform square-prime and local exponent margins of the finite sign theorem then apply throughout this enlarged interval.

For a direct justification of the explicit-formula cutoffs, take an upper cutoff equal to 1 through \(R\), zero after \(2R\), with first two derivative bounds \(O(1/R),O(1/R^2)\). Near zero replace \(h\) by \(1+\chi(u/\delta)(h-1)\), with \(\chi\) zero below 1 and one above 2. The derivative of the resulting test has compact support in \((0,\infty)\). As \(R\to\infty\), the \(e^u\)-weighted \(L^1\) error in \(h''+h'\) tends to zero: the true tail is \(O_s(R^{-1}+e^{-R})\), and on the transition \(e^u(|h|+|h'|)\ll_s1/u\), so the cutoff derivatives cost \(O_s(R^{-1})\). As \(\delta\downarrow0\), \(h-1=O_s(u^s)\) and its first two derivatives are \(O_s(u^{s-j})\), giving an error \(O_s(\delta^{s-1})\) over \([0,2\delta]\). These errors bound the transform of the differentiated kernel simultaneously for every \(0<\Re\rho<1\); multiplying by the absolutely summable reciprocal-square weights justifies passing the whole zero series to the limit. On the original \(\psi-v\) integral the upper cutoff error also vanishes by the quantitative PNT (or by integrating \(h\) against the original signed discrepancy on the dyadic log range); the trivial-zero logarithm at the lower boundary is locally integrable against these vanishing derivatives.
