# Global weighted Hardy variation for the critical-line derivative series

18 November 2026. A single lower transition applied to \(Q_2 Z/t\), followed by a weighted Montgomery–Vaughan estimate on geometric intervals, gives
\[
 \mathcal T(10000)<0.48494,
 \qquad
 0.61649875288731141829<C_2<1.10144.
\]
Here \(\mathcal T(Y)\) is the part of \(C_2\) with \(|\gamma|>Y\), and \(C_2\) sums
\(\left|\zeta'(1/2+i\gamma)Q_2(1/2+i\gamma)\right|^2/(1/4+\gamma^2)\)
over distinct critical-line zeros, with both signs of \(\gamma\). This estimate uses the existing complete partial sum through \(10000\) and no new zero census. The series estimate is unconditional. Its identification with the previously studied full tapered prime-array limit is under RH. [Earlier reviewed bound and finite census](director_weighted_rolle_round10.md)

## One variation inequality for the entire tail

Let \(w=100\), \(T_0=Y-w\ge9900\), \(q(t)=Q_2(1/2+it)=\sqrt2e^{-it\log2}-1\), and \(G=qZ\). Let \(\varphi\) be \(3x^2-2x^3\) with \(x=(t-T_0)/w\) on \([T_0,Y]\), and \(1\) beyond \(Y\). Set \(f=\varphi G/t\) on \([T_0,\infty)\). The cutoff obeys
\[
 0\le\varphi\le1,\quad
 \|\varphi'\|_\infty \le 3/(2w),\quad
 \|\varphi''\|_\infty\le 6/w^2
\]
with the second derivative understood almost everywhere; both derivatives vanish beyond the transition. Also \(f'(T_0)=0\). The block estimates below show that \(G^{(j)}/t\in L^2\) for \(j=0,1,2\), so \(f',f''\in L^2\). For either real component \(u\) of \(f\), \((u'^2)'=2u'u''\) is integrable. Thus \(u'^2\) has a limit at infinity, which is zero since \(u'\in L^2\).

For any finite selection of critical zeros above \(Y\), apply Rolle's theorem to each real component between consecutive selected zeros. At each selected zero the square of that component's derivative is counted in both the rise and fall of \(u'^2\) between neighboring stationary points (using \(T_0\) and the zero limit at infinity at the ends). Taking the supremum over finite selections and then summing the two component inequalities gives
\[
 \sum_{\gamma>Y}|f'(\gamma)|^2\le \int_{T_0}^{\infty}|f'||f''|\,dt
 \le \|f'\|_2\|f''\|_2 .
\]
At the selected zero, \(|f'(\gamma)|=|\zeta'(1/2+i\gamma)q(\gamma)|/\gamma\). Since \(1/(\gamma^2+1/4)\le1/\gamma^2\), conjugation gives \(\mathcal T(Y)\le2\|f'\|_2\|f''\|_2\).

Let \(A_j\) majorize \(\|G^{(j)}/t\|_{L^2[T_0,\infty)}\) and \(B_j\) majorize its norm restricted to \([T_0,Y]\). Differentiating gives the implemented bounds
\[
 \|f'\|_2 \le A_1 + A_0/T_0 + 3B_0/(2w),\qquad
 \|f''\|_2 \le A_2 + 2A_1/T_0 + 2A_0/T_0^2
                +3(B_1+B_0/T_0)/w+6B_0/w^2.
\]

## Weighted polynomial estimates on one interval

Let \([T,U]\) have \(T\ge9900\), \(T<U\le 3T/2\). Set \(d=7/25\), \(M=\lceil dT\rceil\),
\[
 b=\tfrac12\log\frac{\sqrt{TU}}{2\pi},\quad
 \ell_n=\log n-b,\quad
 W=1/T-1/U.
\]
Writing \(P(s)=\sum_{n\le M}n^{-s}\), the polynomial \(Q_2P\) has coefficients \(a_n=-1\) at odd indices \(n\le M\), \(a_n=1\) at even indices \(n\le M\), and \(a_n=2\) at even indices \(M<n\le 2M\); all others vanish. For \(P_j(t)=\sum_n a_n n^{-1/2}\ell_n^j e^{-it\log n}\), let
\[
 \begin{split}
 D_j&=\sum_n |a_n|^2\ell_n^{2j}/n,\\
 J_j&=D_j+\sum_{n\le M}\ell_n^{2j}
       +2\sum_{\substack{M<n\le2M\\n\ {\rm even}}}\ell_n^{2j}
       +2\mathbf 1_{M\ {\rm odd}}\ell_{M+1}^{2j}.
 \end{split}
\]
Then
\[
 \|P_j/t\|_2^2 \le W D_j + 3\pi J_j/T^2. \tag{1}
\]
Indeed, integration by parts of the off-diagonal time integral against \(t^{-2}\) gives two boundary Hilbert forms and an integral of those forms against \(2t^{-3}\). The weighted Hilbert inequality bounds each form by \(3\pi/2\) times the sum of squared coefficients divided by local gaps. The combined weights have total mass \(T^{-2}+U^{-2}+\int_T^U2t^{-3}\,dt=2T^{-2}\). In the original support the gap is at least \(1/(n+1)\). In the even tail it is at least \(2/(n+2)\) except when \(M\) is odd and \(n=M+1\). At that index \(1/(n+1)\) is valid and the extra cost is \(2\ell_n^{2j}\). This yields \(J_j\). [Weighted Hilbert inequality, Theorem G.16](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf)

For the finite blocks the script sums the first 32 harmonic terms and bounds the remaining sums using one-dimensional primitives and total variation. Precisely, for consecutive nodes \(x_k=a+kh\), \(0\le k\le m\), and continuously differentiable \(F\),
\[
 \sum_{k=0}^m F(x_k)
 \le \frac1h\int_a^{a+mh} F(x)\,dx
   +\frac{F(a)+F(a+mh)+\operatorname{Var}_{[a,a+mh]}F}{2}.
 \tag{2}
\]
On each mesh interval the trapezoid error relative to the mean integral equals the integral of \(F'\) against a linear function bounded in magnitude by \(1/2\). The densities are \((\log x-b)^p\) and \((\log x-b)^p/x\) for \(p=0,2,4\). The possible internal turning points are \(e^b\) for positive \(p\), and \(e^{b+p}\) additionally for positive \(p\) in the harmonic density. Their values and the endpoints compute total variation. The antiderivatives in the script follow by substitution in the harmonic case and repeated integration by parts in the other. An ambiguous Arb comparison includes a candidate turning point; inserting its value cannot decrease the sum of absolute differences.

## Euler remainder and the Hardy multiplier

Let \(A(s)\) denote the holomorphic Hardy multiplier, with \(A(1/2+it)=e^{i\theta(t)}\), using the same choice as in the prior moment estimate. Write
\[
 R(z)=A(1/2+iz)\bigl(\zeta(1/2+iz)-P(1/2+iz)\bigr).
\]
For the following bounds let \(s=\sigma+iv\), with \(|\sigma-1/2|\le0.4\), \(T-0.4\le v\le U+0.4\), and put \(c=5.36\). In this rectangle \(v/M\le c\), \(|s|/M\le c\) by \(|s|\le v+0.9\), and \(M/v\le d+2/T\); the last assertion follows from \(M\le dT+1\) and \(d(0.4)+0.8/T\le1\).
Use Euler summation
\[
 \zeta(s)-P(s)=\frac{M^{1-s}}{s-1}-\tfrac12M^{-s}
    -s\int_M^\infty(\{x\}-\tfrac12)x^{-s-1}\,dx.
\]
For each Fourier mode, the oscillatory phase is \(\pm2\pi nx-v\log x\). The positive amplitude divided by the absolute phase derivative, \(x^{-\sigma}/(2\pi nx\mp v)\), decreases to zero on \([M,\infty)\). One integration by parts therefore bounds the absolute mode integral by \(2M^{-\sigma-1}/(2\pi n\mp v/M)\). The coefficients of the Abel-damped Bernoulli series have magnitude at most \(1/(2\pi n)\) for each sign. The Bernoulli series is bounded under Abel damping as it is the Poisson convolution of the bounded periodic Bernoulli function. Dominated convergence passes to the original integral, and the bounds on the integrated modes are summable. For the positive sign isolate \(n=1\) and use \(2\pi n-c\ge n(2\pi-c/2)\) for \(n\ge2\). For the negative sign use \(2\pi n+v/M\ge2\pi n\) for all \(n\). This gives
\[
 |\zeta(s)-P(s)| \le C(T)M^{-\sigma},\qquad
 C(T)=d+2/T+\tfrac12+\frac{c}{\pi}\left[
 \frac1{2\pi-c}+\frac1{2\pi}
 +(\pi^2/6-1)\left(\frac1{2\pi-c/2}+\frac1{2\pi}\right)\right].
 \tag{3}
\]

Use the prior explicit digamma comparison
\[
 |\Re\psi(x+iy)-\log |y||\le\frac{\pi}{2|y|}+\frac{x^2}{2y^2}.
\]
For \(A(s)\), the \(\sigma\) derivative of \(\log|A(s)|^2\) equals the average of the real parts of the two gamma digammas minus \(\log\pi\). The arguments have real parts between \(0.05\) and \(0.45\), and imaginary moduli \(v/2\). In the rectangle, the derivative differs from \(\log T\) by at most \(1.86\), using
\[
 \log\frac{2\pi}{1-0.4/T}+\frac{\pi}{T-0.4}+\frac1{T^2}<1.86
\]
at \(T=9900\) and monotonicity thereafter. The logarithm here majorizes \(|\log(v/(2\pi T))|\) since \(v/(2\pi T)<1\). Consequently \(|A(s)|^2\le e^{1.86 a}T^{\sigma-1/2}\) on a disk of radius \(a\) around a real point of \([T,U]\) in the \(z\)-plane. Combining with (3), the maximum in \(\sigma\) of the bound for \(|R|^2\) occurs at \(\sigma=1/2-a\) because \(T/M^2<1\). With \(a<1/2\),
\[
 |R(z)|\le C(T)e^{1.86a/2}d^{a-1/2}T^{(a-1)/2}.
\]
Cauchy's formula with \(a_1=0.16,\ a_2=0.32\), and direct evaluation for \(a_0=0\), bounds
\[
 E_j=\|R^{(j)}/t\|_2
 \le j!a_j^{-j} C(T)e^{1.86a_j/2}
       d^{a_j-1/2}T^{(a_j-1)/2}\sqrt W ,
 \tag{4}
\]
where \(a_0^0=1\). [Digamma comparison and definition of the Hardy multiplier](prime64_main_term_moments.md)

For real \(t\) the phase satisfies \(|\theta'(t)-b|\le \log(U/T)/4+\pi/(2T)+1/(16T^2)\), by the same digamma comparison at real part \(1/4\). The derivative series for \(\psi'\) gives \(|\theta''(t)|\le t^{-2}+\pi/(4t)\le1/T\) directly. Let \(V_j\) denote the square root of (1) and \(\beta\) the bound for \(|\theta'-b|\). On differentiating \(G=A Q_2 P+qR\), the three weighted norms of \(G,G',G''\) are at most
\[
 \begin{aligned}
 D^{*}_0&=V_0+p_0E_0,\\
 D^{*}_1&=V_1+\beta V_0+p_0E_1+p_1E_0,\\
 D^{*}_2&=V_2+2\beta V_1+(\beta^2+1/T)V_0+p_0E_2+2p_1E_1+p_2E_0,
 \end{aligned}
\]
where \(p_0=1+\sqrt2,\ p_1=\sqrt2\log2,\ p_2=\sqrt2(\log2)^2\). The \(P_j\) terms are centered at the constant \(b\), so the uncentered phase \(\theta\) appears in these formulas only through \(\beta\) and curvature.

## Infinite geometric remainder and verification

For each main interval \(U=rT\) with \(r=3/2\), let \(H=\log T\), \(\omega=1+2/H\), \(L=(H+2)/2\). For all \(1\le x\le2M\), \(|\log x-b|\le L\). The lower endpoint follows from \(b\le H/2\), and the upper endpoint follows from \(\log((2M/T)^2(2\pi/\sqrt r))<2\). The script checks the stronger inequality with \((2M/T)^2\) replaced by \(2(d+1/T)\le1\). For \(p=2j\) the original diagonal integral is at most \(2L^{p+1}/(p+1)\). Its quadrature correction from (2) is bounded by \(3L^p\), because there are at most three monotone pieces and \(0\le F\le L^p\). The tail even harmonic sum costs at most \(2(\log2+2/M)L^p\), by comparing its sum to the logarithmic integral from \(\lfloor M/2\rfloor\) to \(M\). For \(J_j-D_j\), bounding each power by \(L^p\) costs at most \((2M+3)L^p\). Hence, with
\[
 u_j=\frac{\omega^{2j+1}}{2j+1}
       +\frac{(3+2(\log2+2/(dT)))\omega^{2j}}{H},\qquad
 z_j=\frac{u_j}{T}+(2d+5/T)\frac{\omega^{2j}}H ,
\]
the normalized bound for \(V_j\), after division by \(H^{j+1/2}/\sqrt T\), is \(2^{-j}\sqrt{(1-1/r)u_j+3\pi z_j}\). Each factor decreases with \(T\). The corresponding normalized bound for (4) decreases with \(T\) because it is a positive constant times \(C(T)T^{(a_j-1)/2}H^{-j-1/2}\). In the normalized product rule, phase and curvature are divided by \(H\) and \(H^2\), respectively, and the coefficients \(p_1,p_2\) are divided by \(H,H^2\). These are also decreasing. The resulting normalized bound for the \(j\)-th weighted \(G\) norm is denoted \(c_j(T)\).

Sum squared norms over the first 28 geometric intervals based at \(9900\), then put \(S=9900(3/2)^{28}\) and \(h=\log S\). The remaining sum of squares in order \(j\) is bounded by
\[
 \frac{c_j(S)^2 h^{2j+1}}{S}
 \sum_{k\ge0}\exp\bigl(k\log r((2j+1)/h-1)\bigr).
\]
This follows from \((1+k\log r/h)^{2j+1}\le e^{(2j+1)k\log r/h}\). The ratio is less than one. The square root of the full sum gives \(A_j\); the same single-block formulas separately bound \(B_0,B_1\) on \([9900,10000]\).

At 128 bits the final upper expression \(2\|f'\|_{\rm bound}\|f''\|_{\rm bound}\) lies in \(0.48493999027926774129\ldots\) with ball radius below \(3.3\cdot10^{-37}\). Combining the rounded upper bound \(0.48494\) with the previously certified partial sum gives the claimed strict upper bound for \(C_2\). [Arb verification script](../../scripts/prime67_global_hardy_tail_checks.py) · [Recorded numerical result](../../experiments/results/prime67_global_hardy_tail_checks.json) · [Complete finite sum](prime64_q2_partial_tail_observation.md)

At height \(3\cdot10^6\), the same certificate gives \(\mathcal T(3\cdot10^6)<0.0059909\). A complete finite derivative sum through that height of interval width below \(0.00017\) would give a resulting total enclosure narrower than one percent of the existing certified lower bound. That finite census has not been run. [Height-three-million analytic replay](../../experiments/results/prime67_global_hardy_tail_3000000.json)
