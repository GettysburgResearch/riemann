# An explicit logarithmic fourth-power tail for \(C_2\)

Let \(C_2\) be the derivative series over the critical-line zeros from the tapered prime-array theorem. For \(Y\ge16\), write \(H_Y=\log(4Y)\). Then
\[
 \boxed{\sum_{|\gamma|>Y}
 \frac{|\zeta'(1/2+i\gamma)|^2|2^{1/2-i\gamma}-1|^2}{1/4+\gamma^2}
 \le\frac{6.24\cdot10^6}{Y}
       (H_Y^4+4H_Y^3+12H_Y^2+24H_Y+24)
 \le\frac{2.1\cdot10^7 H_Y^4}{Y}.}
\]
The sum is over distinct critical-line zeros, including multiple zeros with zero derivative. Both the upper bound and the enclosed derivative series are unconditional. RH identifies this series with the limit of the scaled tapered prime-array errors. The earlier Heap–Li–Zhao application gives the leading asymptotic for this same series tail under RH. The constants below come from continuous positive second moments and Rolle's theorem. [Tapered-array constant](director_tapered_prime_array_round9.md) · [Heap–Li–Zhao specialization](director_hlz_prime_torus_round9.md)

## From one strip mean-square bound to the discrete moment

Let \(T\ge16\), \(H=\log(4T)\), \(U=T+1\), and \(r=1/H\). The continuous input is the elementary bound
\[
 \int_{-U}^{U}|\zeta(\sigma+it)|^2\,dt\le3000\,TH
 \quad\text{for}\quad |\sigma-1/2|\le r.                              \tag{1}
\]
Its proof follows below. Introduce on \(1/4<\Re s<3/4\) the holomorphic function
\[
 A(s)=\pi^{-(s-1/2)/2}
       \left(\frac{\Gamma(s/2)}{\Gamma((1-s)/2)}\right)^{1/2},
 \qquad A(1/2)=1,
 \qquad \mathcal Z(w)=A(1/2+iw)\zeta(1/2+iw).
\]
The logarithms of the gamma functions on their right half planes give this branch. The functional equation and conjugation show that \(\mathcal Z(t)\) is real and even for real \(t\). In particular \(\mathcal Z'(0)=0\). At a real zero \(\gamma\), \(|\mathcal Z'(\gamma)|=|\zeta'(1/2+i\gamma)|\), since \(|A(1/2+i\gamma)|=1\).

To bound \(A\) off the center line, use the series for \(\psi(z)\), with \(\Re z\ge1/8\) and \(z=s/2\) or \((1-s)/2\). Throughout \(|t|\le U\) and \(|\Re s-1/2|\le r\), both arguments satisfy \(|z-1|\le U\). Put \(J=\lceil U+2\rceil\). In the part with \(1\le n<J\), the real part of \(1/(n+1)-1/(n+z)\) lies between \(-1/(n(n+1))\) and \(1/(n+1)\). The \(n=0\) term is between \(-7\) and \(1\). The tail has absolute value at most \(U/(J-1)\le1\), by bounding each denominator \( |(n+1)(n+z)|\) below by \(n^2\). With \(|\gamma_E|\le1\) and \(J\le4T\), these inequalities give \(|\Re\psi(z)|\le H+6\). Hence
\[
 |\partial_\sigma\log|A(\sigma+it)||\le\tfrac12\log\pi+\tfrac12(H+6)
 < H/2+4.
\]
Integration from the critical line gives \(|A|^2\le e^3<21\), because \(r(H/2+4)<3/2\).

Cauchy's derivative formula on a circle of radius \(r\) in the \(w\) plane, followed by Cauchy–Schwarz in the angle, gives for \(j=1,2\)
\[
 |\mathcal Z^{(j)}(t)|^2\le (j!)^2r^{-2j}
       \int_0^{2\pi}|\mathcal Z(t+r e^{i\theta})|^2\frac{d\theta}{2\pi}.
\]
On integrating \(0\le t\le T\), each angular term has its \(s\)-real part in the strip of (1), and its \(s\)-imaginary interval within \([-U,U]\), with Jacobian one. Thus
\[
 \int_0^T|\mathcal Z^{(j)}(t)|^2\,dt
 \le65000(j!)^2 TH^{2j+1}.
\]

Order the distinct real zeros in \((0,T]\). The first one has a stationary point at \(0\) before it, and each subsequent one has a stationary point in the previous gap by Rolle's theorem. For each right zero integrate \((\mathcal Z'^2)'=2\mathcal Z'\mathcal Z''\) from its preceding stationary point to the zero. These intervals are disjoint. Cauchy–Schwarz and the two continuous moments give
\[
 \sum_{0<\gamma\le T}|\zeta'(1/2+i\gamma)|^2
 \le2\int_0^T|\mathcal Z'(t)\mathcal Z''(t)|\,dt
 \le 260000\,TH^4.                                                \tag{2}
\]
No zero separation enters. The reflection factor \(2\) and \(|2^{1/2-i\gamma}-1|^2<6\) bound the two-sign weighted counting sum \(F(T)\) by \(3.12\cdot10^6TH^4\).

Apply partial summation against \((t^2+1/4)^{-1}\). The upper boundary term at infinity vanishes by (2), and the strict-tail lower boundary term \(-F(Y)/(Y^2+1/4)\) is nonpositive. Thus the tail is at most \(6.24\cdot10^6\int_Y^\infty t^{-2}\log^4(4t)\,dt\). Four integrations by parts give the polynomial in the boxed bound. Since \(H_Y>4\), its ratio to \(H_Y^4\) is at most \(103/32\), and the constant \(2.1\cdot10^7\) follows.

## Proof of the continuous bound

Put \(M=\lceil2U\rceil\), so \(2U\le M\le3T\) and \(M\le3U\). Write \(s=\sigma+it\) with \(|t|\le U\) and \(|\sigma-1/2|\le r\). The Euler summation formula gives
\[
 \zeta(s)=\sum_{n\le M}n^{-s}+\frac{M^{1-s}}{s-1}
    -\tfrac12 M^{-s}-s\int_M^\infty B_1(\{x\})x^{-s-1}\,dx,\qquad
 B_1(v)=v-\tfrac12.
\]
To control the last integral use the Fourier modes of \(B_1\), with coefficient magnitude \(1/(2\pi n)\) for each of the two signs of frequency \(n\ge1\). For one such mode the phase is \(\phi(x)=\pm2\pi nx-t\log x\). On \(x\ge M\),
\[
 |\phi'(x)|\ge 5n,\qquad |\phi''(x)|=|t|/x^2 .
\]
Integration by parts on the positive decreasing amplitude \(x^{-\sigma-1}\) gives the bound
\[
 \left|\int_M^\infty e^{i\phi(x)}x^{-\sigma-1}\,dx\right|
 \le M^{-\sigma-1}\left(\frac{2}{5n}
         +\frac{U}{25n^2M(\sigma+2)}\right)
 \le \frac{M^{-\sigma-1}}{2n}.
\]
The expansion can first be Abel-damped: convolution by the positive periodic Poisson kernel preserves the bound \(1/2\), and converges away from the integer jumps, permitting dominated convergence. The integrated Fourier terms converge absolutely by the displayed estimate. Since \(\sum n^{-2}\le2\) and \(|s|\le M\), the last two terms of the Euler formula together have modulus at most \(M^{-\sigma}\). Their squared integral is at most \(3T\). The pole term has squared integral at most \(4\pi M^{2-2\sigma}\le4\pi e^2 M<300T\), since \(1-\sigma\ge1/4\) and \(\log M\le H\).

For the Dirichlet polynomial, the integral over \([-U,U]\) is bounded by \(e\) times the whole-line integral with Gaussian weight \(e^{-t^2/U^2}\). This weighted integral has matrix entries \(\sqrt\pi U\exp[-U^2(\log(n/m))^2/4]\). For \(m,n\le M\) use \(|\log(n/m)|\ge |n-m|/M\) by integration of \(1/x\). After dividing out \(\sqrt\pi U\), each row sum is at most
\[
 1+2\sum_{j\ge1}e^{-j^2/36}\le 1+6\sqrt\pi<12 .
\]
The quadratic form is bounded by this row sum times the squared coefficient norm, by applying \(2|ab|\le|a|^2+|b|^2\) to the symmetric matrix. As
\[
 \sum_{n\le M}n^{-2\sigma}
 \le e^2\sum_{n\le M}n^{-1}\le e^2(1+\log M)\le10H,
\]
the Dirichlet polynomial has squared integral at most \(640TH\). Here \(12e\sqrt\pi U<60U\le64T\). The squares of the three separate bounds add with a final factor 3 by Cauchy–Schwarz, giving \(3(640TH+303T)\le3000TH\) and proving (1).

## Impact on the certified enclosure

At \(Y=100\), this bound is below \(1.715\cdot10^8\), reducing the earlier certified tail bound \(5.102\cdot10^{16}\) by over eight orders of magnitude. The previously certified finite derivative sum below 100 is between \(0.25253801685456458\) and \(0.25253801685456460\). The resulting enclosure for the series is \(C_2\in[0.25253801685456458,1.716\cdot10^8]\).

As a sufficient 1% criterion, target a total interval width below \(0.0025253801685456458\), one percent of the certified lower bound at height 100. The boxed first bound is above this target at \(Y=5\cdot10^{15}\), and below \(0.00235\) at \(Y=6\cdot10^{15}\). Thus a complete finite sum through \(6\cdot10^{15}\), certified with width below \(0.00017\), would meet the criterion. This is a sufficient height for this particular bound. The actual tail could be much smaller. No such large list was computed. The finite-\(N\) total remainder also involves the separate near part of the kernel beyond the cutoff, for which the previous power bound still applies. [Earlier finite-\(N\) remainder and height-100 certificate](prime64_finite_remainder.md)

The arithmetic constants and three height evaluations were checked at 128 bits with Arb. [Reproducible arithmetic checks](../../scripts/prime64_explicit_log4_tail_checks.py)
