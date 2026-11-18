# Oscillation of the fixed 5:3 detector about its affine logarithmic term

Status — Proposed analytic result with a reproducible finite arithmetic constant.

For the fixed 5:3 detector, subtract the affine function of log scale supplied by its Mellin transform at zero. Each sign of the residual has cumulative logarithmic mass exceeding \(0.0536\log Y\) along an unbounded sequence. This holds unconditionally. It obstructs an approach that would approximate the detector by this affine function with one-sided \(o(\log Y)\) cumulative error. Subpower negative mass for the original detector remains open.

## Arithmetic source and normalization

Write \(u=\log X\), \(w(u)=5c_{e^u}(2)+3c_{e^u}(3)\). The exact normalization, including its affine contribution, is [L-99261 at 433fd366](https://github.com/GettysburgResearch/riemann/blob/433fd3662f7b2e4ba384ce64f196380e88624090/claims/lemmas/L-99261-five-three-row-zero-free-mellin-witness.md). For an independent description, set
\[
 q(n)=6{\bf1}_{n=1}-6\mu(n)+9{\bf1}_{2\mid n}\mu(n/2)
                 -3{\bf1}_{4\mid n}\mu(n/4),\quad
 w(u)=\sum_{n\le e^u}q(n)n^{-1/2}(u-\log n).
\]
Divisibility indicators suppress terms with nonintegral arguments. The Laplace transform equals \(H(s)/s^2\), initially for \(\Re s>1/2\), where
\[
 P(z)=-3(2^{-z}-1)(2^{-z}-2),\qquad
 H(s)=6+P(s+1/2)/\zeta(s+1/2).
\]
This follows by termwise integration in the absolutely convergent region. Since \(\zeta(1/2)\ne0\), define \(A=H(0)\), \(B=H'(0)\), \(e(u)=w(u)-Au-B\). Its transform continues as
\[
 D(s)=[H(s)-A-Bs]/s^2 .
\]
It is holomorphic at zero and along the positive real axis, including the removable point corresponding to the pole of zeta. In particular, \(A>6\) since \(P(1/2)<0\) and \(\zeta(1/2)<0\). Thus the lower bound below on the centered negative mass by itself gives no lower bound on negative mass of \(w\).

## A logarithmic mean oscillation bound

Write \(v_+=\max(v,0)\), \(v_-=\max(-v,0)\). For each sign separately,
\[
 \limsup_{T\to\infty}\frac1T\int_0^T e(u)_\pm\,du
 \ \ge\ \frac{2}{\pi}\frac{127}{128}
       \left|\frac{P(\rho_1)}{(\rho_1-1/2)^2\zeta'(\rho_1)}\right|
 \ >\ 0.0536 ,
 \tag{1}
\]
where \(\rho_1=1/2+i\gamma_1\) denotes the first nontrivial zero of positive ordinate. The two subsequences may differ.

**Step 1.** Fix a sign and write \(v=e\) or \(v=-e\), so the desired estimate concerns \(v_-\). If the left side is infinite there is nothing to prove for that sign. Otherwise, writing its limsup as \(L\), we have \(\int_0^T v_-\,du=O(1+T)\). Partial integration gives absolute convergence of \(\mathcal L v_-\) for \(\Re s>0\), and
\[
 \limsup_{\sigma\downarrow0}\sigma\,\mathcal L v_-(\sigma)\le L
\]
by splitting the integral \(\sigma^2\int_0^\infty e^{-\sigma T}\int_0^T v_-\,du\,dT\) at a sufficiently large fixed \(T_0\).

The transform of \(v_+\), initially convergent for \(\Re s>1/2\), equals \(\pm D+\mathcal L v_-\) there. If its real abscissa of convergence were positive, the right side would continue holomorphically through that real point. Landau's theorem for a nonnegative Laplace density excludes this. Hence \(\mathcal L v\) converges absolutely throughout \(\Re s>0\) and agrees there with \(\pm D\). This step permits boundary evaluation without assuming RH. [Landau proof and abscissa conventions](../../reviews/C/pass4-math-completion/proofs/MELLIN_ANALYTIC_GAPS.md)

**Step 2.** Take \(d=127\). Let \(p\) be the degree-\(d\) Fejér mean of the real \(2\pi\)-periodic function \(\operatorname{sgn}(\cos t)\). The normalized Fejér kernel has mass one and is nonnegative, hence \(|p|\le1\). Its constant and nonzero even coefficients vanish. For Fourier convention \(p(t)=\sum_k b_k e^{ikt}\), its coefficient \(b_1=b_{-1}=(2/\pi)d/(d+1)\) follows by integrating \(\operatorname{sgn}(\cos t)\cos t\) and applying the Fejér weight \(1-1/(d+1)\).

For any real phase \(\phi\), the test \(h(u)=(1+p(\gamma_1 u+\phi))/2\) lies between zero and one, so \(v_-(u)\ge-h(u)v(u)\). At \(s=i\gamma_1\) the residue of \(\mathcal L v\) is \(C=\pm P(\rho_1)/[(i\gamma_1)^2\zeta'(\rho_1)]\). At the conjugate point it is \(\overline C\). At \(s=0\) and at \(s=\pm ik\gamma_1\), odd \(3\le k\le127\), it is regular by the finite checks below. Therefore
\[
 \lim_{\sigma\downarrow0}\sigma\int_0^\infty e^{-\sigma u}
                 p(\gamma_1u+\phi)v(u)\,du
       =2b_1\Re(e^{-i\phi}C).
\]
This is a finite Fourier sum of radial limits. The constant in \(h\) has zero limit after multiplication by \(\sigma\). Choose \(\phi\) so that \(\Re(e^{-i\phi}C)=-|C|\). The preceding pointwise inequality gives
\(\liminf_{\sigma\downarrow0}\sigma\,\mathcal L v_-(\sigma)\ge b_1|C|\). Step 1 now proves (1).

## What a hypothetical off-line zero would cost

For \(\rho=1/2+a+i\gamma\) with \(a>0\) and multiplicity \(m\), define \(s_0=\rho-1/2\) and
\[
 C_m=\frac{m!\,P(\rho)}{s_0^2\,\zeta^{(m)}(\rho)}\ne0 .
\]
The uncentered detector itself satisfies, for each sign,
\[
 \limsup_{Y\to\infty}
 \frac{\int_1^Y w(\log x)_\pm\,dx/x}
      {Y^a(\log Y)^{m-1}}
 \ \ge\ \frac{|C_m|}{2a(m-1)!}.
 \tag{2}
\]
No rightmost-zero, simplicity, or separation assumption is needed. To prove it, take \(v=\pm w\), and suppose the relevant limsup \(K\) is finite. Step 1 with endpoint \(a\) gives absolute convergence for \(\Re s>a\) since the continuation is holomorphic on the real interval \((a,\infty)\). Partial integration gives
\[
 \limsup_{\delta\downarrow0}\delta^m\mathcal L v_-(a+\delta)
 \le a(m-1)!K .
\]
Indeed \(\int_0^T v_-\le(K+\eta)e^{aT}T^{m-1}\) eventually for each \(\eta>0\). The transform at \(a+\delta+i\gamma\) has modulus bounded by
\(\mathcal L v(a+\delta)+2\mathcal L v_-(a+\delta)\). Its modulus times \(\delta^m\) tends to \(|C_m|\), while \(\mathcal L v(a+\delta)\) stays bounded. This proves (2).

## Finite arithmetic and remaining gap

The [finite checker](check_detector_nov18.py) uses python-flint 0.9.0 at 128-bit precision. It calls FLINT's indexed zeta-zero enclosure for the first root, requires the real part to be exactly \(1/2\), excludes zero from the derivative enclosure obtained by series evaluation at the entire root ball, and excludes zero from each of the 63 complex zeta enclosures at the required positive odd harmonics. Conjugation handles negative frequencies. It compares the final lower bound to the exact rational \(536/10000\) using ball order. The zero index and all directed primitive arithmetic rely on FLINT. The script provides a single implementation.

Run the checker from the repository root with python-flint installed.

    python research/explorations/check_detector_nov18.py

Its script SHA-256 is 53c30094de1efb24ad9c6a442fad3a552339434812297d31e0243fd878f20a48. The returned enclosure of the constant was \(0.053609139775753104138850318229438313\) with printed error at most \(4.64\cdot10^{-37}\).

The open task is still to upper-bound the cumulative negative part of \(w\) for every horizon by \(O_\epsilon(e^{\epsilon T})\). Formula (1) limits the accuracy of an affine approximation. Formula (2) quantifies the growth forced by a hypothetical off-line zero.
