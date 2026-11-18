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
