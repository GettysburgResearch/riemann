# High zeros on the Dwars curves under the negative heat flow

**Status.** Proposed asymptotic theorem for review. In the normalization of Dobner write \(t=-4a\), \(a>0\), and set
\[
 Z_a(s)=\sum_{m\ge1}e^{-a(\log m)^2}m^{-s},
 \qquad J_a(s)=s+a\operatorname{Log}(s/(2\pi)).
\]
Dwars observed families of complex zeros of the deformed Riemann xi near deterministic curves. Tao identified the curves by balancing two consecutive Dirichlet terms. Dobner's Theorem 4 justifies the approximation of the deformed xi by the log-Gaussian Dirichlet series on sufficiently high images of bounded vertical strips. The explicit growing number of simple zero lattices below, their completeness in the intervening cells, and the circular first-correction law specify the scope of our argument. [Tao, Polymath15 eleventh thread, 2018](https://terrytao.wordpress.com/2018/12/28/polymath-15-eleventh-thread-writing-up-the-results-and-exploring-negative-t/) · [Dobner, §1, Fig. 2 and Theorem 4](https://arxiv.org/abs/2005.05142)

Write \(\lambda_n=\log n\), \(\delta_n=\log((n+1)/n)\), \(\sigma_n=-a(\lambda_n+\lambda_{n+1})\), and
\[
 s^0_{n,k}=\sigma_n+i\tau_{n,k},\qquad
 \tau_{n,k}=\frac{(2k+1)\pi}{\delta_n}.
\]
There are absolute \(c,C,K>0\) with the following property. If \(a/(N+1)^2\ge K\), the zeros of \(Z_a\) in \(\Re s\ge\sigma_N-1/\delta_N\) consist of exactly one simple zero in each disk
\[
 |s-s^0_{n,k}|<C\delta_n^{-1}\exp(-c a/(n+1)^2),
 \qquad 1\le n\le N,\ k\in\mathbb Z .
\]
In the high images under \(J_a\) of any bounded vertical strip containing the indicated transition bands and intervening cells, the same localization and completeness hold for \(\xi_{-4a}\), with the disk bound multiplied by an absolute constant. The upper boundary of the strip can be chosen arbitrarily far to the right, keeping it fixed in the height limit. Each sufficiently high disk contains exactly one simple zero of the composition. Its image gives one simple zero of the deformed xi. For every \(B>0\), choosing \(N=\lfloor c_B\sqrt{a/\log a}\rfloor\) gives absolute errors \(O_B(a^{-B})\) in these coordinates as \(a\to\infty\). The height beyond which the xi conclusion holds can depend on \(a,N\) and the strip.

For fixed \(a,N\) in this range, the physical zero ordinates on the \(n\)-th curve are within \(O(\delta_n^{-1}e^{-ca/(n+1)^2})+o_{a,n}(1)\) of \(\tau_{n,k}+a\pi/2\), and their real parts are within the same error of \(a\log(\tau_{n,k}/(2\pi n(n+1)))\) as \(k\to\infty\). These curves have exactly \(T\log(N+1)/(2\pi)+O_{a,N}(1)\) positive-ordinate zeros through height \(T\) above a fixed sufficiently high starting height. They all lie strictly to the right of the critical line there. Reflection gives the corresponding left-hand curves.

## Uniform two-term estimate and exclusion of further model zeros

Divide the series at \(s=\sigma_n+w\) by its \(n\)-th term. The terms indexed by \(n,n+1\) give \(1+e^{-\delta_n w}\). For \(|\delta_n\Re w|\le1\) the modulus of the term indexed by \(m\) relative to the \(n\)-th is at most
\[
 \exp\{-a(\lambda_m-\lambda_n)(\lambda_m-\lambda_{n+1})
             +(n+1)|\lambda_m-\lambda_n|\}.
\]
Here \(1/\delta_n\le n+1\). For every \(m\notin\{n,n+1\}\) the last exponent term can be absorbed in one half of the quadratic decay as soon as \(a/(n+1)^2\ge K\), since \(|\lambda_m-\lambda_{n+1}|\ge1/(n+2)\). For \(m<n\) the product in the exponent is at least \((n-m)(n+1-m)/(n+1)^2\). For \(n+2\le m\le2(n+1)\) it is at least \((m-n)(m-n-1)/(4(n+1)^2)\), by integrating \(1/x\). Both sums after absorption are \(O(e^{-c a/(n+1)^2})\) by geometric comparison. The rest is at most
\[
 \sum_{j\ge1}2^{j+1}(n+1)e^{-a(j\log 2)^2/2}
 \ll(n+1)e^{-a(\log 2)^2/2}
 \ll e^{-c a/(n+1)^2}.
\]
All constants are absolute. Denote the full error bound by \(\eta_n\).

On \(|\Re z|\le1\) one has \(|1+e^{-z}|\ge e^{-1}\operatorname{dist}(z,i\pi(2\mathbb Z+1))\): translate to the nearest odd multiple of \(i\pi\) and use \(|1-e^{-x-iy}|^2=(1-e^{-x})^2+4e^{-x}\sin^2(y/2)\) for \(|y|\le\pi\). Thus every zero in this band is within \(e\eta_n/\delta_n\) of a center. Taking radius \(2e\eta_n/\delta_n\) and increasing \(K\) keeps the circles within the band and mutually disjoint. Rouché gives one zero counted with multiplicity per circle.

Adjacent bands are disjoint for \(K\) large, since \(\sigma_n-\sigma_{n+1}=a(\delta_n+\delta_{n+1})\). In the intervening cell \(\sigma_n+1/\delta_n\le\Re s\le\sigma_{n-1}-1/\delta_{n-1}\), divide by term \(n\). All higher terms decrease relative to it as \(\Re s\) increases. At the lower endpoint their sum of absolute ratios is at most \(e^{-1}+\eta_n\). All lower terms decrease relative to it as \(\Re s\) decreases. Their bound from the upper endpoint is \(e^{-1}(1+\eta_{n-1})\), since term \(n\) there is \(e\) times the magnitude of term \(n-1\). The combined ratio is less than one. At \(n=1\) only the higher terms are present. This proves the claimed completeness and gives a strict uniform margin in each cell.

Dobner's Theorem 4 gives \(\xi_{-4a}(J_a(s))/\gamma_{-4a}(s)=Z_a(s)+o(1)\) uniformly in every fixed vertical strip as \(\Im s\to\infty\), with nonvanishing normalization there. The modulus of each dividing \(n\)-th term is bounded away from zero for fixed \(n,a\) and bounded real part. Thus the same exclusion estimates and contour arguments work at sufficiently high ordinates. The map \(J_a\) is univalent on a high upper half-plane because \(|J_a'(s)-1|=a/|s|<1/2\) there and the domain is convex. Also \(J_a'(s)=1+o(1)\) uniformly on high bounded-width rectangles. Expansion at the centers gives the displayed real and imaginary coordinates. Counting one disk for every odd multiple of \(\pi/\delta_n\) gives the stated total after summing \(\sum_{n\le N}\delta_n=\log(N+1)\).

## The first displacement is asymptotically uniform on a circle

Fix \(n\). Put
\[
 d_n=(\lambda_{n+2}-\lambda_n)(\lambda_{n+2}-\lambda_{n+1}),\qquad
 L_n=\lambda_{n+2}-\lambda_n .
\]
The \(n+2\)-th term uniquely minimizes the positive exponent \((\lambda_m-\lambda_n)(\lambda_m-\lambda_{n+1})\) among all other terms. On the right the product increases, while for \(n>1\) the first term on the left has exponent \(\delta_{n-1}(\delta_{n-1}+\delta_n)>\delta_{n+1}(\delta_{n+1}+\delta_n)=d_n\). If \(s_{n,k}\) denotes the model zero, uniformly in \(k\),
\[
 \delta_n(s_{n,k}-s^0_{n,k})=-e^{-a d_n-i\tau_{n,k}L_n}
                         +O_n(e^{-a(d_n+\epsilon_n)})
\]
for some \(\epsilon_n>0\). Indeed on a fixed small circle about the center the noncentral terms have total modulus \(O_n(e^{-a d_n})\) after normalization. This follows by extracting the first term and summing the remaining Gaussian tail at any fixed positive \(a_0\). The zeros are consequently \(O_n(e^{-a d_n})\) from the center. Taylor-expand the central pair there, whose linear derivative is \(\delta_n\), and retain term \(n+2\) at the center. Its displacement contributes \(O_n(e^{-2a d_n})\). The remaining terms give the exponential separation just proved.

For fixed sufficiently large \(a\), the inverse image under \(J_a\) of the physical zero differs by \(o_{a,n}(1)\) from its matching model zero as \(k\to\infty\). To see uniform stability, the normalized analytic remainder in a fixed-width disk about each center is \(O_n(e^{-ad_n})\), so Cauchy's inequality gives the same derivative bound on a smaller disk. The derivative of the normalized function at its root has modulus at least \(\delta_n/2\) for \(a\) large, and its second derivative on the disk is uniformly bounded. Every sufficiently small circle of fixed radius \(r\) about this root therefore has boundary modulus at least \(\delta_n r/4\). Dobner's uniform approximation and Rouché give the assertion by taking \(r\downarrow0\).

Finally \(L_n/\delta_n\) is irrational. If its value were \(p/q>1\) in positive integers, one would have \((n+2)^q n^{p-q}=(n+1)^p\), contradictory to coprimality. Thus \(e^{-i\tau_{n,k}L_n}\) is equidistributed on the unit circle. Write \(z_{n,k}\) for the physical zero at time \(-4a\). For each bounded continuous \(f:\mathbb C\to\mathbb C\),
\[
 \lim_{a\to\infty}\limsup_{M\to\infty}\left|
 \frac1M\sum_{k=1}^M f\big(\delta_n e^{a d_n}(z_{n,k}-J_a(s^0_{n,k}))\big)
 -\frac1{2\pi}\int_0^{2\pi} f(e^{i\theta})\,d\theta\right|=0 .
\]
A finite initial segment before the high-zero correspondence may be omitted. The estimate follows from uniform continuity on a fixed compact neighborhood of the circle, the model displacement formula, and \(J_a'=1+o_{a,n}(1)\). In particular the rescaled horizontal deviations approach the arcsine distribution on \([-1,1]\) in this order of limits. The theorem concerns large negative time; its estimates do not continue the lattice through time zero.

## Explicit circles at the times used for numerical illustrations

At \(t=-30\), the first lattice has an inverse-coordinate disk of radius \(0.072135\) about each center containing one simple model zero. At \(t=-50\) the corresponding radii for the first two lattices are \(0.014427\) and \(0.345283\) (the exact certified radii before rounding upward are \(r/\delta_n\) in the checker). The same Rouché argument applies to the heat-deformed xi in the image of every sufficiently high such disk. On the circle \(|w|=r\), Taylor's formula gives \(|1-e^{-w}|\ge1+2r-e^r\). The [directed checker](check_dobner_curves_nov18.py) sums the absolute noncentral terms at their worst disk real part through 128. For \(m>128\) their relative magnitudes are bounded by \((m/n)^{-q}\), \(q=a\log(128/(n+1))-r/\delta_n>1\). Integral comparison gives the remaining tail. The strict boundary margins respectively exceed \(0.0095,0.0060,0.0205\). Each radius may be reported as an outer enclosure of the located root; uniqueness is asserted on the exact tested circles.
