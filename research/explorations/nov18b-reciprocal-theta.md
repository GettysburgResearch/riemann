# A height-uniform Möbius test from a single zeta zero

Let `T=2+|γ|` and let `ρ=β+iγ` be any nontrivial zero with `1/2≤β<1`. There are absolute positive constants `C,c,X₀` with the following property. At **every** real `X≥X₀`, put `L=C√(T log(2XT))`. Some real endpoints `X/L≤a<b≤XL` obey
\[
 \left|\sum_{a<n\le b}\mu(n)n^{-i\gamma}\right|
 \geq c\,X^\beta\frac{T^{\beta/2-1}}{\log(2T)}.                 \tag{1}
\]
For the untwisted sum the same statement holds with an additional factor \(T^{-1}\) on the right. No simplicity, spacing, assumption about other zeros, or estimate of a reciprocal derivative is required. The explicit test works at a multiple zero as well. For a fixed off-line zero, a further consequence below forces positive signed short-shift correlations on every sufficiently late collar.

## A Gaussian with a polynomial height cost

Write \(D=t\,d/dt\), choose \(z=\exp(i\operatorname{sgn}(\gamma)(\pi/2-1/T))\), and define
\[
 g(t)=D(D+1)e^{-\pi zt^2}=(4\pi^2 z^2t^4-6\pi zt^2)e^{-\pi zt^2},
 \qquad \Phi_z(t)=\sum_{m\ge1}g(mt).
\]
For \(\Re s>0\), integration by parts gives
\[
 G(s)=\int_0^\infty g(t)t^s\frac{dt}{t}
 =\frac{s(s-1)\Gamma(s/2)}{2(\pi z)^{s/2}} .
\]
The power uses the principal logarithm. Poisson summation for the even Gaussian and the identity
\(D(D+1)[t^{-1}f(1/t)]=t^{-1}[D(D+1)f](1/t)\)
give exactly \(\Phi_z(t)=z^{-1/2}t^{-1}\Phi_{1/z}(1/t)\). The constant and linear polar terms are killed in this identity. Thus \(\widehat\Phi_z(s)=G(s)\zeta(s)\) on the whole strip by continuation from absolute convergence to the right of one. In particular the full \(\rho\)-moment of \(\Phi_z\) vanishes.

The elementary Gaussian sum estimates and reciprocity give
\[
 |\Phi_z(t)|\le C T^{5/2}\min(1,t^{-1})
       \exp[-c\max(t^2,t^{-2})/T],\qquad
 \int_0^\infty |\Phi_z(t)|\frac{dt}{t}\ll T^{5/2}\log(2T).
                                                               \tag{2}
\]
For \(t\ge1\), use \(\Re z\asymp 1/T\) and
\(\sum_{m\ge1}(mt)^j e^{-c(mt)^2/T}\ll T^{(j+1)/2}t^{-1}e^{-c'(t^2/T)}\) for \(j=2,4\), by absorbing polynomial factors into the Gaussian and comparing its sum with its integral. For \(t<1\) apply reciprocity. Stirling's formula gives \(|G(\rho)|\asymp T^{3/2+\beta/2}\) uniformly on the stated range. The exponential factor in the gamma modulus is compensated by \(\exp(\gamma\arg(z)/2)\). For bounded ordinates uniformity follows by compactness and the classical absence of nontrivial zeros near 0 or 1.

## Exact finite-scale arithmetic observation

Let
\[
 Q(v)=\frac{v^{-\beta}}{G(\rho)}\int_v^\infty\Phi_z(t)t^{\rho-1}\,dt .
\]
The upper primitive equals the negative lower primitive because \(\widehat\Phi_z(\rho)=0\). Absolute convergence and the divisor identity \(\mu*1=\delta_1\) give
\[
 X^{-\beta}\sum_{n\ge1}\mu(n)n^{-i\gamma}Q(n/X)
 =\frac1{G(\rho)}\int_{1/X}^{\infty}g(t)t^{\rho-1}dt
 =1+O\big(X^{-2-\beta}/|G(\rho)|\big).                        \tag{3}
\]
At each fixed lower integration limit the absolute sum over integer pairs is finite by Gaussian decay. This identity compares the truncation at a single scale to one known number, even in the presence of nearby zeros.

The bounds (2) on the lower and upper primitives imply
\[
 |Q(v)|\ll T^{3}\exp[-c\max(v^2,v^{-2})/T].
\]
For \(v\le1\) use \(v^{-\beta}\int_0^v t^{\beta-1}dt\le2\) after extracting a fixed fraction of the exponential. For \(v\ge1\) use the upper primitive and absorb the elementary Gaussian tail into the displayed polynomial. Thus after multiplication by \(X^{-\beta}\) the sum outside \([X/L,XL]\) in (3) costs at most \(CT^4(1+X)e^{-c'L^2/T}\), less than \(1/4\) with a sufficiently large absolute constant in \(L\).

By Fubini applied to the absolute lower primitive,
\[
 \int_0^\infty |Q(v)|\frac{dv}{v}
 \le \frac{1}{\beta |G(\rho)|}\int_0^\infty |\Phi_z(t)|\frac{dt}{t},
 \qquad
 \int_0^\infty|Q'(v)|\,dv
 \le \frac{2}{|G(\rho)|}\int_0^\infty |\Phi_z(t)|\frac{dt}{t}.
\]
Partial summation on the retained range, with \(\sup |Q|\le\int|Q'|\), proves (1). For the untwisted case absorb \(v^{-i\gamma}\) into \(Q(v)\); its additional variation is at most \(|\gamma|\int|Q(v)|dv/v\). The coefficient of every integer in (3) is explicit in the specified zero.

## Forced signed short-shift correlations

Fix an off-line zero as above and any \(\delta>0\). For all large \(X\) and all integers \(1\le h\le X^{1-\delta}\),
\[
 \sum_{X/(2L)<n<2LX}\left|\sum_{0\le j<h}\mu(n+j)\right|^2
          \gg_{\rho,\delta} h^2 X^{2\beta-1}.                     \tag{4}
\]
The same conclusion holds with the twist \((n+j)^{-i\gamma}\). To see this, take \(F(v)=v^{-i\gamma}Q(v)\) for the untwisted bound or \(F(v)=Q(v)\) for the twisted bound. All derivatives are rapidly decreasing at both ends, by (2), the integral expressions and their differentiated Gaussian series. For each fixed integral \(k\), every derivative through order \(k\) obeys the same two-sided Gaussian bound after decreasing its positive exponential constant, with a constant depending on \(k,\rho\).

For \(y=h/X\), take \(P_{h,y}(v)=\sum_{r<k}c_{r,h}y^r F^{(r)}(v)\). Choose the coefficients as the first \(k\) Taylor coefficients of the inverse of \(h^{-1}\sum_{j<h}\exp(-jz/h)\) at zero. The constant term is 1 and the higher Taylor coefficients before inversion are bounded by \(1/r!\), so the \(c_{r,h}\) are uniformly bounded for fixed \(k\). Taylor's formula now gives
\[
 \sum_{m\in\mathbb Z}\left|h^{-1}\sum_{j<h}P_{h,y}((m-j)/X)-F(m/X)\right|
       \ll_{k,\rho} X y^k,
\]
extending the functions by zero on the negative half-line. For the summed Taylor remainder use the uniform lattice sum \(\sum_m\sup_{|u-m/X|\le y}|F^{(k)}(u)|\ll_{k,\rho}X\) for \(y\le1\), from smoothness and rapid decay. Choose \(k>(1-\beta)/\delta\). The resulting error is \(o(X^\beta)\). Insert the averaged weight in (3) and exchange the finite shift sum with the absolutely convergent integer sum. The contribution with \(n\notin[X/(2L),2LX]\) is negligible after enlarging the absolute constant in the Gaussian collar if needed: derivatives introduce only polynomial factors in \(v,v^{-1}\), absorbable using a fixed fraction of the original Gaussian exponent for all fixed \(k\). Finally \(\sum_n|P_{h,y}(n/X)|^2\ll_{k,\rho}X\). Cauchy–Schwarz proves (4).

When \(2(1-\beta)<\alpha<1\) and \(h=\lfloor X^\alpha\rfloor\), the diagonal contribution to the left of (4) is at most \(O(hLX)\), which is little-oh of the lower bound. Hence an off-line zero forces the *signed off-diagonal* sum
\[
 \sum_{X/(2L)<n<2LX}\ \sum_{0\le i<j<h}\mu(n+i)\mu(n+j)
       \gg_{\rho,\alpha} h^2 X^{2\beta-1}                         \tag{5}
\]
on every late collar. Fixed-shift logarithmic Chowla estimates do not control these growing shifts. The standard almost-all short-interval cancellation for Möbius supplies a relative little-oh saving on the trivial \(h^2X\) scale of a dyadic shell. A bound of order \(hX^{1+o(1)}\) on a suitable sequence of such collars at these lengths would contradict (4), since \(\alpha>2(1-\beta)\). The actual uniform upper estimate required to exclude a zero in this way remains open. [Matomäki and Radziwiłł, *Multiplicative functions in short intervals*](https://arxiv.org/abs/1501.04585)
