# A reverse Gamma average for detecting a nonreal xi zero

**Proposed theorem.** Let \(\Xi(w)=\xi(1/2+iw)=0\), \(T=\Re w\ge100\), \(0<\delta=|\Im w|<1/2\). For every integer
\[
 D\ge C T^2\log(2T)/\delta^2
 \tag{1}
\]
the ordinary normalized Jensen polynomial \(J_D(z)=\sum_{j\le D}(D)_{\underline j}a_j z^j/D^j\), \(\Xi(z)=\sum a_j z^j\), has a zero in \(B(w,\delta/2)\). Thus the classical even-coefficient Jensen polynomial of degree \(d\) at shift zero is nonhyperbolic whenever \(2d\) meets (1), by the finite Laguerre multiplier in [the first converse, §4](jensen-converse-nov18.md). Constants are absolute and unevaluated. The exponent of \(\log T\) in the degree bound decreases from the two in the [analytic-capacity argument](jensen-capacity-converse-nov18.md) to one.

## Bounds for the Jensen polynomial

Write \(L=\log(2T)\), \(z_c=T-2i\). For \(D\ge C_0 T^2 L\) with a sufficiently large constant,
\[
 |J_D(z)|\le e^{-\pi\Re z/4}T^{C_1}
 \quad(T/2-10\le\Re z\le2T+10,\ |\Im z|\le12),
 \qquad |J_D(z_c)|\ge e^{-\pi T/4}T^{-C_1}.
 \tag{2}
\]
Here are details of the anchor lower bound and uniformity in \(D\). With the usual bilateral theta density \(\Phi\),
\[
 J_D(z)=\int_{\mathbb R}\Phi(u)(1+izu/D)^Ddu .
\]
Translate to \(u=x+i(\pi/4-1/T)\). On that line, \(|(1+izu/D)^D|\le\exp(\Re(izu)+|zu|^2/(2D))\). For \(|x|\le2L\) this extra quadratic costs at most \(e^{C_2 L/C_0}\); outside, double-exponential theta decay absorbs it. By evenness and conjugation the absolute theta weight for \(x\ge0\) is bounded by \(C\sum_{k\ge1}k^4e^{9x/2}\exp(-c k^2 e^{2x}/T)\). These estimates prove the upper bound. For \(z=z_c\), the absolute integral against \(|e^{iz_cu}|\) on the translated line is specifically \(\ll e^{-\pi T/4} T^{9/4+2/2}\): integrating \(e^{(9/2+2)x}\) against each theta exponential gives a sum bounded by \(C\sum_k k^{4-(9/2+2)}\). Both tails \(|x|>2L\) are negligible even with the quadratic weight. The same contour estimate applies to \(\exp(iz_cu+t u^2)\), \(t=T^2/(2D)\).

On \(|x|\le2L\), a Taylor expansion of \(D\log(1+iz_cu/D)\) now replaces the Jensen factor by \(\exp(iz_cu+tu^2)\) with relative error \(O(L^3/T)\). Indeed the cubic is \(O(T^3L^3/D^2)\), and replacing \(z_c^2/(2D)\) by \(t\) costs \(O(T L^2/D)\). Taking \(C_0\) large makes \(e^{C_2L/C_0}\ll T^{1/10}\). The integrated replacement error is \(o(e^{-\pi T/4}T^{7/4+2/2})\) as \(T\to\infty\).

The heat integral at \(z_c\), on returning to the real Fourier contour, is \(\mathbb E\xi(s_c+V)\) where \(s_c=5/2+iT\), \(V\) is centered real normal with variance \(2t\). Write \(G(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\), \(\alpha=G'(s_c)/G(s_c)\). Stirling gives \(|G(s_c)|\asymp e^{-\pi T/4}T^{7/4+2/2}\), \(\Re\alpha=\tfrac12\log(T/(2\pi))+O(1/T)\), \(|\Im\alpha|=O(1)\), and \(G(s_c+v)=G(s_c)e^{\alpha v}(1+O(1/T))\) for \(|v|\le1/8\). On this interval \(|\zeta(s_c+v)-1|\le\sum_{n\ge2}n^{-19/8}<0.6\), by summing the first term and the integral from 2 to infinity. After tilting the Gaussian by \(e^{(\Re\alpha)v}\), its new center \(2t\Re\alpha\) has absolute value less than \(1/32\) for our fixed large \(C_0\). The phase average of \(e^{i(\Im\alpha)v}\) has modulus \(e^{-t(\Im\alpha)^2}=1-o(1)\), whereas the zeta-minus-one error costs at most 0.6 times the tilted mass. The truncation at \(|v|\le1/8\) and the contribution there omitted from the original heat integral are negligible after division by \(|G(s_c)|\). In detail, Stirling, the functional equation on the far left, and polynomial bounds on fixed vertical strips give
\[
 |\xi(s_c+v)|\le e^{-\pi T/4} T^{C_3}
       \exp(C_3|v|\log(T+|v|+2)).
\]
For \(|v|\ge1/8\) the Gaussian exponent \(-v^2/(4t)\) absorbs the last exponential and any fixed power of \(T\) by increasing \(C_0\). The angular term in Stirling on the right half-plane uses \(T\arctan((1+|v|)/T)\le1+|v|\). These facts prove the lower bound in (2) for sufficiently large \(T\). The remaining compact \(T\)-interval follows by locally uniform Jensen convergence to \(\Xi\) as \(D\to\infty\) and \(\xi(5/2+iT)\ne0\), increasing \(C_0\).

Suppose now \(J_D\) is zero-free on \(B(w,\delta/2)\). Apply disk Jensen and finite Blaschke factorization to \(e^{\pi T/4}J_D(z)\) on the disk of radius 8 about \(z_c\) using (2), exactly as in the [cluster-contour argument, §1](weil-contour-nov18.md). There are \(O(L)\) zeros in radius 7. Inside radius 5 the log-modulus of the nonvanishing quotient on a disk of radius between 6 and 7 is bounded in absolute value by \(O(L)\). Harnack and interior derivative estimates give first and second logarithmic derivatives \(O(L)\) there on any slightly smaller disk. The Blaschke denominators contribute the same order. Each zero numerator is at distance at least \(\delta/4\) on \(B(w,\delta/4)\), so
\[
 |(\log J_D)'|\ll L/\delta,\qquad
 |(\log J_D)''|\ll L/\delta^2\quad\text{on }B(w,\delta/4),
 \quad
 |J_D(w)|\ge e^{-\pi T/4-CL(1+\log(1/\delta))}.
 \tag{3}
\]
For \(|b|\le1\), even if a zero intervenes, the same factorization gives
\[
 |J_D(w+b)|/|J_D(w)|
 \le \exp(CL |b|)(1+2|b|/\delta)^{CL}.
 \tag{4}
\]
Indeed each numerator increases by at most the indicated factor, while the zero-free parts have log-modulus gradient \(O(L)\).

## Reverse averaging and the complex saddle

Use the exact identity
\[
 \frac1{D!}\int_0^\infty e^{-u}u^D J_D(Dw/u)\,du
 =\sum_{j\le D}a_j w^j .
 \tag{5}
\]
Termwise integration cancels the falling factorial. Set \(s=(u-D)/D\), \(r=\delta/(32T)\). Relative to \(J_D(w)\) the integrand is \(e^{F(s)}\) locally, up to the positive normalization \(D^{D+1} e^{-D}/D!\asymp\sqrt D\), where
\[
 F(s)=D(\log(1+s)-s)+g(s),\qquad
 g(s)=\log\{J_D(w/(1+s))/J_D(w)\},\qquad g(0)=0.
\]
This logarithm is analytic on \(|s|<3r\) by the zero-free hypothesis and \(|w|\le1.01T\). On \(|s|\le2r\), (3) gives \(|g'|\le C TL/\delta\), \(|g''|\le CT^2 L/\delta^2\). With the constant in (1) sufficiently large, the mapping \(s\mapsto (1+s)g'(s)/D\) maps \(|s|\le r/10\) strictly into itself and is a contraction. Its fixed point \(s_0\) satisfies \(F'(s_0)=0\) and \(|s_0|\ll TL/(D\delta)\). On \(|s|\le2r\),
\[
 |F''(s)+D|\le D/50 .
\]
Here \(r<1/6000\); the elementary second derivative \(-D/(1+s)^2\) and the bound on \(g''\) give the estimate. Taylor at 0 gives \(|F(s_0)|\ll(T L/\delta)^2/D\).

In the local integral shift the segment \([-r,r]\) to \(s_0+[-r,r]\) with two straight connectors. On the shifted segment,
\[
 F(s_0+x)=F(s_0)-Dx^2/2+E(x),\qquad |E(x)|\le Dx^2/100.
\]
Using \(|e^E-1|\le |E|e^{|E|}\) and integrating against the Gaussian shows that this integral equals \(e^{F(s_0)}\sqrt{2\pi/D}\) with relative error less than \(1/10\), including its omitted Gaussian tails when \(Dr^2\) is large. On both connectors the real part of \((s-s_0)^2\) is at least \(0.79r^2\), and the modulus of the quadratic Taylor error is at most \(D|s-s_0|^2/100\). Their normalized cost relative to \(e^{F(s_0)}\) is \(O(\sqrt D\,r e^{-Dr^2/3})\).

## The other parts of the Gamma integral

For real \(-1/2\le s\le1\), \(D(\log(1+s)-s)\le-cDs^2\) with an absolute \(c>0\). When \(|s|\ge r\) and \(|b|=|w/(1+s)-w|\le1\), (4) bounds the logarithmic gain relative to \(J_D(w)\) by
\(CL(|b|+\log(1+2|b|/\delta))\). Since \(|b|\le 3T|s|\), \(T|s|/\delta\ge1/32\), this is bounded by \(C' L(Ts/\delta)^2\). Increase the constant in (1) to retain at least \(-cDs^2/2\) net decay. When \(|b|>1\), (2) and (3) bound the gain by \(C[L(1+\log(1/\delta))+T|s|]\). Here \(T|s|\ge1/3\); the same net decay holds since \(1+\log(1/\delta)\ll\delta^{-2}\). The normalized total cost outside \([-r,r]\) in this range is therefore \(O(e^{-c'Dr^2})\) relative to \(J_D(w)\). The bound \(|F(s_0)|\ll(T L/\delta)^2/D\) is less than \(c'Dr^2/2\) after increasing the constant in (1), permitting comparison with the local saddle contribution.

For the external ranges \(u<D/2\) and \(u>2D\) use the original real Fourier kernel. Its absolute integrand prior to division by \(D!\) is bounded by
\[
 \int |\Phi(p)| e^{-u}(u+2T|p|)^D\,dp .
\]
Putting \(b=2T|p|\), translate to \(u+b\), acquiring a factor \(e^b\). If \(u>2D\), or if \(u<D/2\) and \(b<D/4\), the normalized Gamma tail is \(O(e^{-cD})\) by the elementary exponential-moment bound for a Gamma variable of shape \(D+1\). Moreover \(\int |\Phi(p)|e^{2T|p|}dp\le e^{C T\log(2T)}\) by double-exponential decay. For the remaining \(b\ge D/4\), bound the whole Gamma integral by one and use \(\int_{|p|\ge D/(8T)} |\Phi(p)|e^{2T|p|}dp\ll e^{-D}\), from the same decay and \(D\gg T^2L\). Thus the external cost is \(\ll e^{-cD+CT L}\) in absolute value. This is negligible relative to \(|J_D(w)e^{F(s_0)}|\) by (1) and (3).

We have proved that the left side of (5) has magnitude at least an absolute positive constant times
\[
 |J_D(w)|e^{-C(T L/\delta)^2/D}
 \ge \exp[-\pi T/4-C' L(1+\log(1/\delta))].
\]
The Taylor tail \(\sum_{j>D} a_j w^j\) has absolute value \(\ll 2^{-D}e^{CT L}\) by Cauchy on \(|z|=2|w|\); the global xi bound there follows also from the preceding real theta moment. This is smaller than the last lower bound, since \(D\gg T^2 L/\delta^2\). The full Taylor series consequently cannot vanish at \(w\), a contradiction. This proves (1).
