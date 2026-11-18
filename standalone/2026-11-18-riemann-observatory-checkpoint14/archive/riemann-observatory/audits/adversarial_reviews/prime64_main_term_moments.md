# Effective Hardy derivative moments with centered frequencies

Let \(Z(t)\) be the real Hardy function and put
\[
 \mathcal T(Y)=\sum_{\substack{\rho=1/2+i\gamma\\|\gamma|>Y}}
       \frac{|\zeta'(\rho)|^2\,|2^{1-\rho}-1|^2}{|\rho|^2}.
\]
The sum and bounds in this note are unconditional. RH is needed for the identification of the full derivative series \(C_2\) with the scaled tapered-array limit. The previous analytic estimate used Cauchy's formula on the whole Hardy function. Here Cauchy's formula is used just for the small fixed Euler remainder. The main polynomial is differentiated directly, retaining the leading centered logarithmic moments.

## Explicit moment and tail formulas

For a base height \(V\ge400\) set \(h=\log V\) and, for \(j=0,1,2\), put
\[
 u_j=2^{-j}\sqrt{\frac{1.2}{2j+1}+\frac{6.4}{h}},
 \qquad e_j=12j!4^j V^{-3/8}h^{-j-1/2}.
\]
Define
\[
\begin{split}
 a_0&=u_0+e_0,\\
 a_1&=u_1+0.67u_0/h+e_1,\\
 a_2&=u_2+1.34u_1/h+(0.67^2+1/V)u_0/h^2+e_2,\\
 K(V)&=12\left(a_1+\frac{15a_0}{Vh}\right)
         \left(a_2+\frac{30a_1}{Vh}+\frac{600a_0}{V^2h^2}\right).
\end{split}
\]
For \(T\ge V\) the unweighted moments of \(Z^{(j)}\) on \([0.9T,2.1T]\) are bounded by \(a_j^2T(\log T)^{2j+1}\), and
\[
 \sum_{\substack{\rho=1/2+i\gamma\\T<|\gamma|\le 2T}}
      |\zeta'(\rho)|^2\,|2^{1-\rho}-1|^2
   \le K(V)T(\log T)^4.                                           \tag{1}
\]
In particular, with \(b=\log 2\) and
\[
 B(h)=2h^4+8bh^3+36b^2h^2+104b^3h+150b^4,
\]
one has for each \(Y\ge400\) and nonnegative integer \(J\)
\[
 \mathcal T(Y)\le
 \sum_{\ell=0}^{J-1} K(2^\ell Y)\,
                    \frac{\log^4(2^\ell Y)}{2^\ell Y}
 +\frac{K(2^JY)}{2^JY}B(\log(2^JY)).                               \tag{2}
\]
The last term bounds all remaining dyadic blocks, including \(T=2^JY\). The proof works with \(J=0\). Even then the leading coefficient in this upper bound, after dividing by \(\log^4Y/Y\), tends to \(28.8/\sqrt{960}<0.93\). The earlier explicit dyadic coefficient was \(900\). The constant \(1/(12\pi)\) in the RH-conditional asymptotic for the actual \(k=2\) tail is a different quantity and is smaller than this upper coefficient. [Earlier explicit bound](prime64_sharper_moments.md) · [Actual conditional asymptotic](director_hlz_prime_torus_round9.md)

## The fixed Euler polynomial and its remainder

Let \(T\ge400\), \(M=\lceil T/2\rceil\), \(H=\log T\), and \(P(s)=\sum_{n\le M}n^{-s}\). Use the holomorphic Hardy multiplier \(A(s)\) of the preceding bound, so that \(A(1/2+it)=e^{i\theta(t)}\). For \(|\sigma-1/2|\le1/4\) and \(0.89T\le t\le2.11T\), we use
\[
 |\zeta(\sigma+it)-P(\sigma+it)|\le6 M^{-\sigma},
 \qquad |A(\sigma+it)|^2\le(5/3)T^{\sigma-1/2}.                    \tag{3}
\]
Here is a direct check that the earlier Euler estimate remains valid on this enlarged interval. With \(s=\sigma+it\), the summation formula is
\[
 \zeta(s)-P(s)=\frac{M^{1-s}}{s-1}-\tfrac12 M^{-s}
       -s\int_M^\infty (\{x\}-\tfrac12)x^{-s-1}\,dx.
\]
Since \(t/M\le4.22\), for every mode \(n\ge1\) the phase
\(\phi(x)=\pm2\pi n x-t\log x\) has \(|\phi'|\ge2n\) on \(x\ge M\). Integration by parts as in the earlier proof bounds each mode integral by
\[
 M^{-\sigma-1}\left(\frac{1}{n}
             +\frac{4.22}{4n^2(\sigma+2)}\right)
 \le\frac{3}{2n}M^{-\sigma-1}.
\]
The Abel-damped Bernoulli series has coefficients bounded by \(1/(2\pi n)\) for each sign and passes to the original periodic function by dominated convergence. Its integrated mode series is absolutely convergent. Using \(\sum_{n\ge1}n^{-2}\le2\) gives \(3M^{-\sigma-1}/\pi\) for the integral. With \(|s|/M\le4.23\), \(M/t<0.57\), the first bound in (3) follows.

For the multiplier, the digamma comparison of left endpoints to integrals gives
\[
 |\Re\psi(x+iy)-\log |y||\le\frac{\pi}{2|y|}+\frac{x^2}{2y^2}
 \qquad(x>0,\ y\ne0).
\]
This is obtained by comparing the series of \(1/(n+x+iy)\) with the integral on each unit interval and integrating the derivative bound. In \(A(s)\) the gamma arguments have real parts in \([1/8,3/8]\) and imaginary parts of modulus \(t/2\). It follows that \(|\partial_\sigma\log|A|^2-\log T|<2\) since
\(\log(2\pi/0.89)+\pi/(0.89T)+(9/32)/(0.89T)^2<2\).
Integrate from \(1/2\), where \(|A|=1\), and use \(e^{1/2}<5/3\).

Now write \(R(w)=A(1/2+iw)(\zeta(1/2+iw)-P(1/2+iw))\).
If \(t\in[0.9T,2.1T]\), the \(w\)-disk of radius \(1/4\) fits in (3). Its pointwise squared bound is \(120T^{-3/4}\): letting \(d=\sigma-1/2\), (3) gives \(60 M^{-1}(T/M^2)^d\), and \(1/T\le T/M^2\le1\), \(|d|\le1/4\). Cauchy's formula followed by integration over the interval of length \(1.2T\) yields
\[
 \|R^{(j)}\|_2\le12j!4^j T^{1/8}.                                  \tag{4}
\]

## Centered logarithmic coefficients

Let \(b_M=(\log M)/2\), \(\ell_n=\log n-b_M\) and
\[
 Q_j(t)=\sum_{n\le M} n^{-1/2}\ell_n^j e^{-it\log n},
 \qquad j=0,1,2.
\]
The phase derivative on \([0.9T,2.1T]\) satisfies
\[
 |\theta'(t)-b_M|\le0.67,\qquad |\theta''(t)|\le1/T.                \tag{5}
\]
For the first inequality, \(\theta'(t)=\tfrac12(\Re\psi(1/4+it/2)-\log\pi)\); the digamma comparison above and \(T/2\le M\le0.5025T\) put \(\tfrac12\log(t/(2\pi M))\) within \(0.67\) even after adding the error. For the second, the differentiated series bounds \(|\psi'(1/4+it/2)|\le4/t^2+\pi/t\), by its zeroth term and a decreasing integral. Thus \(|\theta''|\le1/t^2+\pi/(4t)\le1/T\).

On any interval of length \(L\), the weighted Hilbert inequality gives
\[
 \int\left|\sum_{n\le M}c_n e^{-it\log n}\right|^2dt
 \le L\sum_{n\le M}|c_n|^2+3\pi\sum_{n\le M}(n+1)|c_n|^2.          \tag{6}
\]
Indeed expand the square and write each off-diagonal integral as the difference of two endpoint Hilbert forms. Their absolute values are each at most \((3\pi/2)\sum|c_n|^2/\delta_n\), with \(\delta_n=\min_{m\ne n}|\log n-\log m|\ge1/(n+1)\). The coefficient arrays at the endpoints differ by phases of modulus one. [Montgomery–Vaughan author text, Theorem G.16, equations (G.26)–(G.28)](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf)

Put \(S_j=\sum_{n\le M}n^{-1}\ell_n^{2j}\). The elementary estimate
\[
 S_j\le b_M^{2j}\left(\frac{\log M}{2j+1}+1+\frac2{\sqrt M}\right)
\]
keeps its leading coefficient. To see it, integrate \(q_j(x)=x^{-1}(\log x-b_M)^{2j}\) on \([1,M]\) to get \(b_M^{2j}\log M/(2j+1)\). On \([1,\sqrt M]\) the integrand is decreasing. Sum through \(\lfloor\sqrt M\rfloor\) with at most \(q_j(1)\) excess. On \([\sqrt M,M]\) it is nonnegative and unimodal, including the monotone case. The sum of excess over unit integrals plus the last endpoint is at most twice its supremum, which is at most \(b_M^{2j}/\sqrt M\). This covers both sides of the turning point without an alignment condition on \(\sqrt M\).

The correction term in (6) for \(c_n=n^{-1/2}\ell_n^j\) is at most \(3\pi(S_j+M b_M^{2j})\). Taking \(L=1.2T\), \(\log M\le H\), \(1+2/\sqrt M\le1.15\), and using that \((\log T+1.15)/T\) decreases for \(T\ge400\), gives
\[
 \|Q_j\|_2^2\le T(H/2)^{2j}\left(\frac{1.2H}{2j+1}+6.4\right).     \tag{7}
\]
The constant bound is \(1.2(1.15)+3\pi(0.5025+(\log400+1.15)/400)<6.4\).

With \(\beta(t)=\theta'(t)-b_M\), the first derivative of \(A P\) along the real \(t\) line is \(iA(\beta Q_0-Q_1)\). Its second derivative is \(A(-\beta^2Q_0+2\beta Q_1-Q_2+i\theta''Q_0)\). Use (5)–(7) and (4), including the zeroth order. For \(T\ge V\), after division by \(\sqrt T(\log T)^{j+1/2}\), each normalized coefficient has the corresponding bound \(a_j\) in the stated formulas. This uses only upper bounds that decrease with \(V\), so the same coefficient controls all later blocks.

## Two-sided cutoff and Rolle's theorem

Let \(p(x)=3x^2-2x^3\). Form a cutoff \(\varphi=1\) on \([T,2T]\), using \(p\) rescaled from \(0.9T\) to \(T\) and its reflection rescaled from \(2T\) to \(2.1T\). Then \(\varphi'=\varphi=0\) at the outer endpoints, \(0\le\varphi\le1\), \(|\varphi'|\le15/T\), \(|\varphi''|\le600/T^2\) almost everywhere. Set \(f=\varphi Z\). Between consecutive selected zeros, \(f'\) vanishes at a stationary point by Rolle's theorem. On both outer endpoints \(f'\) also vanishes. Thus the total variation of \(f'^2\) on the interval is at least twice the sum of its values at the selected zeros, including when there is only one. Since \(f'\) is absolutely continuous,
\[
 \sum_{T<\gamma\le2T}|\zeta'(1/2+i\gamma)|^2
 \le \int |f'f''| \le\|f'\|_2\|f''\|_2 .
\]
This keeps both rises and falls of \(f'^2\) instead of charging only one side. Reflection and \(|2^{1-\rho}-1|^2<6\) give the factor \(12\) in (1). The estimates for \(f'\) and \(f''\) are exactly the two product-rule factors in \(K(V)\). There is no simplicity, separation or RH assumption.

Divide (1) on each dyadic block by its lower \(T^2\). Beyond the first \(J\) blocks use the common coefficient \(K(2^JY)\), and sum the polynomial in \(\ell\log2+\log(2^JY)\) with weights \(2^{-\ell}\). The powers of \(\ell\) of orders 0 through 4 sum to \(2,2,6,26,150\), which gives (2).

## Numerical consequences

At \(Y=400\), using \(J=8\), the analytic bound in (2) is below \(83.05\). The previous independent Arb integration bounds the contributions from \((100,200]\) and \((200,400]\) by \(2.22\) and \(2.13\), respectively. The previously certified derivative sum through height 100 has upper bound \(0.253\). Combining those estimates gives
\[
 C_2\in[0.25253801685456458,\ 87.66]
\]
for the unconditional derivative series. Those finite certificates are used with their original hashes. No new zero list or long integration was needed. [Prior finite integrals](prime64_sharper_moments.md) · [Height-100 derivative certificate](prime64_finite_remainder.md)

At \(Y=2\cdot10^8\), the same \(J=8\) bound is below \(0.00192\). A complete finite derivative sum through that height with certified width below \(0.00060\) would give a total width below one percent of the existing certified lower bound. This sufficient cutoff was \(2\cdot10^{11}\) with the earlier dyadic estimate. The hypothetical large finite list was not computed.

The companion script checks constants and evaluates threshold choices at 128 bits. The source ledger records the explicit bounds that were inspected and the remaining uniformity issues. [Arithmetic checks](../../scripts/prime64_main_term_moments_checks.py) · [Source ledger](prime64_main_term_moments_sources.md)
