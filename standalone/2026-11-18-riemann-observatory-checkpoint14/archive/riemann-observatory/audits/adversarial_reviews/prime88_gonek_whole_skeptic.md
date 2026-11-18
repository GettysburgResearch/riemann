# Independent whole-paper review of Gonek (1984)

S. M. Gonek, “Mean values of the Riemann zeta-function and its derivatives,” Inventiones Mathematicae 75 (1984), 123–141. Reviewed the complete 19-page [journal scan](../../sources/classical63_lfunctions/gonek1984.pdf), SHA-256 dfdd2444a2f62f1947c897e87101080225714dbf1f21db8ca19096d2a6e80fc3. References below use printed pagination.

## Statement and normalization

With \(L=(2\pi)^{-1}\log(T/(2\pi))\), \(\delta=\alpha/L\) and fixed nonnegative integers \(\mu,\nu\), (4) is unconditional and uniform for real \(|\alpha|\le L/2\). The sum over \(1\le\gamma\le T\), counted with multiplicity, is
\[
\sum \zeta^{(\mu)}(\rho+i\delta)\zeta^{(\nu)}(1-\rho-i\delta)
=(-1)^{\mu+\nu}\frac{T}{2\pi}(\log T)^{\mu+\nu+2}
\left[\frac1{\mu+\nu+1}-H(\mu,\nu,2\pi\alpha)-H(\nu,\mu,-2\pi\alpha)\right]
+O_{\mu,\nu}(T\log^{\mu+\nu+1}T).
\]
Its entire factor has the integral representation
\[
H(\mu,\nu,c)=\mu!\sum_{j\ge0}\frac{(ic)^j}{(j+\mu+1)!(j+\mu+\nu+2)}
=\int_0^1\int_0^t(t-v)^\mu t^\nu e^{icv}\,dv\,dt.
\]
The beta integral proves equality and gives bounds for \(H,H'\) over the real axis and in bounded-imaginary-part strips.

Cor. 1, (5)–(6), applies RH to identify \(1-\rho-i\delta\) with \(\overline{\rho+i\delta}\) for real \(\delta\). At zero shift the diagonal coefficient is \(\mu^2/[(2\mu+1)(\mu+1)^2]\), giving the stated comparison ratio \((\mu/(\mu+1))^2\) to the continuous mean per point for \(\mu\ge1\) from Ingham and zero counting. In particular the bracket for \(\mu=\nu=1\) is \(1/3-2/(2!\,4)=1/12\). Therefore under RH
\[
 A(T)=\sum_{0<\gamma\le T}|\zeta'(1/2+i\gamma)|^2
 =\frac{T\log^4T}{24\pi}+O(T\log^3T).
\]
Changing the lower endpoint to zero costs at most a fixed contribution. The residues of \(\xi'/\xi\) include each zero with its exact multiplicity. Multiple zeros have zero weight in this derivative measure. The proof uses no simplicity assumption.

## Whole proof checks

- **§2, pp. 125–127.** The functional equations, Stirling with derivatives and the local logarithmic-derivative formula give the gamma saddle factor, derivative signs and endpoint estimates. On \(s=a+it\), \(1<a<3/2\), the gamma factor \(\chi(1-s)\) leads with \(e^{-i\pi/4}(t/(2\pi))^{a-1/2}\exp(it\log(t/(2\pi e)))\), and \(\chi^{(j)}(1-s)\) multiplies that by \((-\log(t/(2\pi)))^j\). The right-edge expansion of \(\xi'/\xi\) is \(\zeta'/\zeta+\frac12\log(t/(2\pi))+i\pi/4+O(1/t)\). A local \(O(\log T)\) zero count gives a good height within a bounded interval at distance \(c/\log T\) from ordinates for sufficiently small fixed \(c>0\), sufficient for every contour error. Fixed-order convexity bounds follow from ordinary convexity and Cauchy estimates.
- **Contour, pp. 127–129.** Integrate the summand with \((\xi'/\xi)(s)\) over the rectangle with sides \(1-a,a\) and bottom at height 1. The zeta derivative factors have no poles inside for the stated shift range. The top error is \(O(T^{a-1/2+\epsilon})\) with logs absorbed, and the bottom error is bounded. The left side is \(I_3(\mu,\nu,\delta)=\overline{I_1(\nu,\mu,\delta)}\) for real \(\delta\). The conjugation bar is visible in the scan and determines the sign of the reflected shift.
- **Lemmas 1–5, pp. 129–133.** The phase \(t\log(t/(er))\) has its nondegenerate saddle at \(r\). Rescaling \(t=r(1+x)\) gives the normalized saddle term \((2\pi)^{1-a}r^a e^{-ir+i\pi/4}\) and error \(O(r^{a-1/2})\). On a dyadic interval \([A,B]\), the second derivative bound controls endpoints within \(O(\sqrt A)\) of the saddle and integration by parts gives endpoint terms of size \(A^{a+1/2}/(|A-r|+\sqrt A)\) and its \(B\)-analogue away from it. Partial summation inserts log powers. For \(r=2\pi n\) and \(b_n\ll_\epsilon n^\epsilon\), the endpoint terms sum by a harmonic bound in the comparable range and absolute summability in the remote range with \(\epsilon<a-1\). The Gaussian phase cancels the gamma phase, \(e^{-2\pi in}=1\), and the magnitude cancels \(n^{-a}/(2\pi)\). Dyadic assembly gives the sharp sum \(\sum_{n\le T/(2\pi)}b_n(\log n)^m\), with error \(O(T^{a-1/2}\log^m T)\). An exact saddle on an endpoint falls in the near-endpoint error.
- **Lemmas 6–10, pp. 133–136.** The differentiated gamma factor follows from its logarithmic derivatives. The divisor coefficients \(A_n\) of \(\zeta^{(\mu)}\zeta^{(\nu)}\) have partial sum \((-1)^{\mu+\nu}\mu!\nu!x\log^{\mu+\nu+1}x/(\mu+\nu+1)!+O(x\log^{\mu+\nu}x)\). The coefficients \(B_n\) of its product with \((\zeta'/\zeta)(s-i\delta)\) additionally convolve with \(-\Lambda(d)d^{i\delta}\). The ordinary PNT and partial summation reduce this to a shifted beta integral, giving the main term
\[
(-1)^{\mu+\nu+1}\mu!\nu!x(\log x)^{\mu+\nu+2}
\sum_{j\ge0}\frac{(i\delta\log x)^j}{(j+\mu+\nu+2)!}
\]
and error \(O(x\log^{\mu+\nu+1}x)\). The integral controls uniformity for the full real interval of shifts even if the argument of the series grows. Log weighting preserves the error by partial summation, with the zero weighting power immediate. Lemma 10's finite identity follows by representing \(k!/(\lambda+k)!\) as \(\int_0^1 t^k(1-t)^{\lambda-1}\,dt/(\lambda-1)!\) and summing the binomial \((1-t)^\nu\).
- **§5, pp. 136–140.** Shift the right edge to the integration variable \(s+i\delta\) and apply the differentiated functional equation with the \((-1)^k\) factor on \(\zeta^{(k)}(s)\). The \(\frac12\log(t/(2\pi))\) branch gives \(1/[2(\mu+\nu+1)]\), the \(\zeta'/\zeta\) branch gives \(-H(\mu,\nu,\delta\log(T/(2\pi)))\), and \(i\pi/4\) is lower by one log. Reflection doubles the first branch and adds the swapped-index, opposite-sign \(H\). Reinsert the \(O(\log T)\) ordinates from a good height \(T'\) to the desired height \(T\), with combined cost \(O(T^{1/2+\epsilon})\) by convexity. Hold the physical shift \(\delta\) fixed, using \(\alpha'=\delta L_{T'}\) at \(T'\). The uniform derivative bound for \(H\) gives main-term variation \(O((\log T)^{\mu+\nu+2})\) over this bounded displacement, and the physical shift remains in range. The final replacement of the amplitude log by \(\log T\) costs the declared error.

The accepted external inputs are the functional equations, Stirling and fixed derivative bounds, ordinary zeta convexity, classical zero counting and local logarithmic-derivative estimates, effective ordinary PNT, and elementary stationary phase and oscillatory-integral bounds. The bibliography identifies Davenport [1], Levinson [4], Titchmarsh [9], and Whittaker–Watson [10] for classical machinery. Hardy–Littlewood [2] supplies the continuous mean used in §6 and Ingham [3] supplies the derivative comparison. Selberg [8] and Montgomery [5] are introductory context. The large-gap application is credited to Mueller [6,7]. This review does not claim a separate audit of each reference.

## Complex shifts and Cauchy differentiation

The printed result gives a real coupled shift, and already states the needed derivative case. For an independent Cauchy derivation, the underlying zero-order contour proof extends to \(|\delta|\le c_0/\log T\) for fixed \(c_0>0\). The shifted right segment can be moved back to the line \(a+it\) by endpoint connectors of length \(O(1/\log T)\), at real parts a fixed distance to the right of 1. Its upper error is \(O(T^{a-1/2+\epsilon})\), and the lower error is bounded. The \(\xi'/\xi(s-i\delta)\) argument remains right of 1. The factors \(d^{i\delta}\) are bounded by \(d^{c_0/\log T}\) globally, preserving the fixed \(n^\epsilon\) envelope for sufficiently large \(T\), and bounded uniformly on \(d\le x\ll T\). The ordinary PNT partial summation then uses \(|u^{i\delta}|\ll_{c_0}1\) and the usual derivative bounds over its finite integration interval. Stirling, the horizontal estimates and endpoint restoration remain uniform there. Reflection reads \(I_3(0,0,\delta)=\overline{I_1(0,0,\bar\delta)}\). Thus the continued zero-order result has \(O_{c_0}(T\log T)\) error across the disk.

The coefficient of \(\delta^2\) in each product is \(\zeta'(\rho)\zeta'(1-\rho)\), since both factors vanish at zero shift. The zero-order bracket is \(1-2(1-\cos c)/c^2=c^2/12+O(c^4)\), \(c=\delta\log(T/(2\pi))\). Cauchy extraction with radius \(c_0/\log T\) sends the uniform error to \(O(T\log^3 T)\) and recovers the same prefix after applying RH. This is a single complex parameter and a microscopic disk.

## Corollaries 2 and 3

In Cor. 2, \(H(0,0,c)+H(0,0,-c)=2(1-\cos c)/c^2\) by the integral above. This gives the stated sinc-squared profile, including zero by continuity. For fixed \(\beta>0\), integration over \([-\beta/2,\beta/2]\) followed by conversion to height gives interval mass \(F(\beta)T\log T+O(T)\) for the sum of the arcs around the ordinates, where \(F(\beta)=\int_{-\beta/2}^{\beta/2}[1-(\sin(\pi\alpha)/(\pi\alpha))^2]\,d\alpha\).

On p. 140 the assertion that arcs of radius \(\beta/(2L)\) centered at \(1\le\gamma\le T\) cover all of \([1,T]\) is too strong literally, since the early centers have fixed gaps while the radius shrinks. To repair it take \(\lambda<\beta'<\beta\), where \(\lambda\) is the stated normalized limsup, and restrict to \([\epsilon T,(1-\epsilon)T]\) for fixed \(0<\epsilon<1/2\). Zero counting places the flanking centers within \([1,T]\) and at ordinates comparable to \(T\). Their gaps are eventually at most \(\beta' 2\pi/\log\gamma<\beta/L\). Coverage and the Hardy–Littlewood mean give \(F(\beta)\ge1-2\epsilon\). Let \(\epsilon\) tend to zero to get \(F(\beta)\ge1\), which is sufficient by continuity and \(F(1.9)<1\) to prove \(\lambda>1.9\).

The strict numerical margin can be checked by
\[
F(\beta)=\beta\left[1-\sum_{j\ge0}\frac{(-1)^j2(\pi\beta)^{2j}}{(2j+2)!(2j+1)}\right].
\]
The absolute term ratio is \((\pi\beta)^2(2j+1)/[(2j+4)(2j+3)^2]\), less than 1 beyond \(j=20\) at \(\beta=19/10\). Arb at 100 bits gave partial value \(0.997266199977644853304274175\) with ball radius \(1.19\cdot10^{-28}\) and the next-term error at most \(1.288\cdot10^{-23}\). The strict margin survives both.

## Tail use and effectivity

Strict cutoff Stieltjes partial summation gives
\[
\sum_{\gamma>Y}\frac{|\zeta'(1/2+i\gamma)|^2}{\gamma^2}
=-\frac{A(Y)}{Y^2}+2\int_Y^\infty\frac{A(t)}{t^3}\,dt
=\frac{\log^4Y}{24\pi Y}+O\!\left(\frac{\log^3Y}{Y}\right)
\quad(\mathrm{RH}).
\]
Adding negative ordinates doubles both sides. The analytic inputs, including the PNT for the fixed Riemann zeta function, allow effective constants in principle. The paper does not supply explicit numerical tail constants or a cutoff threshold. The §6 arc repair has no impact on the tail or the normalization of its RH probability law.
