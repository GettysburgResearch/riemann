# A logarithmic Möbius taper on the full dilation-averaged target

The [fixed-shape obstruction](nov18b-reciprocal-first-shell.md) allows cutoffs whose shape changes with \(N\). For the coefficients \(\mu(n)(1-\log n/\log N)\), \(1\le n\le N\), the interior residual is an explicit prime-counting error. After a fixed smooth average of dilations, the full squared error obeys
\[
 \|R_N^{\mathrm{av}}\|_{L^2(du/u^2)}^2
 \ll \frac{1+\int_1^N M(x)^2\,dx/x^2}{(\log N)^2}.
 \tag{1}
\]
In particular the weak Mertens hypothesis gives \(O(1/\log N)\) on the full physical half-line. The proof gives a direct bound in terms of finite arithmetic data for each \(N\). The averaged target detects every zero of real part greater than \(1/2\).

## The unsmoothed interior

Let \(D_q f(u)=f(u/q)\), \(P=(1-D_2)(1-2D_2)\), \(p(s)=(1-2^{-s})(1-2^{1-s})\), \(F=P\lfloor\cdot\rfloor\), and \(g=P1_{u\ge1}\). Put \(L=\log N\), \(N\ge2\). The physical residual is
\[
 R_N=g-\sum_{n\le N}\mu(n)(1-\log n/L)F(\cdot/n).
\]
Here \(F\) is bounded, since \(P\) kills linear functions, and \(g\) is supported in \([1,4]\). For \(u\le N\), every contributing integer is at most \(N\). Möbius inversion and \((\mu\log)*1=-\Lambda\) give exactly \(R_N(u)=-P\psi(u)/L\).

On RH, with \(m_\rho\) the multiplicity of a distinct nontrivial zero,
\[
 \int_0^N |R_N(u)|^2\frac{du}{u^2}
   =\frac{C_P+o(1)}{\log N},\qquad
 C_P=\sum_{\rho\ {\rm distinct}}m_\rho^2\frac{|p(\rho)|^2}{|\rho|^2}>0.
 \tag{2}
\]
Indeed at \(u=e^v>8\) the explicit formula gives \(e^{-v/2}P\psi(e^v)\) as the exponential series with coefficients \(-m_\rho p(\rho)/\rho\), plus an exponentially decaying term. The main linear term cancels, and bounded initial intervals are immaterial. To justify taking the logarithmic mean square, the sums of absolute coefficients in the integer ordinate bands are \(O(\log(2+|j|)/(1+|j|))\) by the zero count, with multiplicities. For a finite frequency sum, integration against a nonnegative Schwartz majorant of \([0,V]\) of scale \(V\ge1\) bounds its mean square, divided by \(V\), by a constant times the sum of the squared band masses. This follows from the decay of its Fourier transform between nonadjacent bands and Cauchy–Schwarz for the resulting summable convolution. The band tails therefore converge uniformly in this mean-square bound, also locally in \(L^2\), where the distributional explicit formula identifies the limit. For finite sums the distinct frequencies are orthogonal in the limiting mean. Passing to the limit proves (2). The multiplier \(p\) has no zero in the open critical strip.

## A fixed smooth average with nonvanishing Mellin transform

Let \(\varphi\) be the probability density of a sum of independent uniform random variables on \([0,2^{-j}]\), \(j=1,2,\ldots\). Its support is \([0,1]\). It is smooth since the convolution of any first \(k\ge2\) uniform densities is \(C^{k-2}\), and convolution with the remaining probability measure preserves that regularity. Its Laplace transform is
\[
 \Phi(s)=\prod_{j\ge1}\frac{1-e^{-s2^{-j}}}{s2^{-j}},
\]
where each factor at zero is defined by continuity. The product converges locally uniformly. Each factor is nonzero on \(\Re s>0\), and the sum of their deviations from one converges locally uniformly, so \(\Phi\) is nonzero there.

Use \(Jf(u)=\int_0^1\varphi(a) f(e^{-a}u)\,da\) and set \(R_N^{\rm av}=J R_N\). For any \(\Re s>0\), the Mellin transforms with measure \(u^{-s-1}du\) of \(Jg,JF\) are respectively \(\Phi(s)p(s)/s\) and \(\Phi(s)p(s)\zeta(s)/s\), by absolute convergence where \(\Re s>1\) and analytic continuation. Both functions vanish on \(u<1\); \(JF\) is bounded and \(Jg\) is compactly supported. Evaluation of the Mellin transform on \(\Re s>1/2\) is bounded on this supported \(L^2(du/u^2)\) space by Cauchy–Schwarz. Thus a zero \(\rho\) with \(\Re\rho>1/2\) annihilates all the approximating dilates \(JF(\cdot/n)\) but gives \(\Phi(\rho)p(\rho)/\rho\ne0\) on \(Jg\). In particular norm convergence to this target would imply RH.

## Proof of the full bound

Extend all logarithmic variables to the whole real line and write
\[
 K(v)=e^{-v/2}JF(e^v),\quad G(v)=e^{-v/2}Jg(e^v),
 \quad h(v)=e^{-v/2}M(e^v).
\]
All three vanish for \(v<0\). The \(u\)-norm of a residual is exactly the ordinary \(v\)-norm of the normalized function. The kernel \(K\) is the convolution of \(e^{-v/2}F(e^v)\) with \(e^{-a/2}\varphi(a)\). The latter is smooth and compactly supported, so \(K\) and \(K'\) are bounded by \(C e^{-v/2}\) on \(v\ge0\). In particular \(K\) and \(v(K'+K/2)\) belong to \(L^1\).

Distributionally \(m=(\partial+1/2)h=\sum_{n\ge1}\mu(n)n^{-1/2}\delta_{\log n}\), including the atom at zero. Set \(T=K'+K/2\). Möbius inversion gives \(K*m=G=T*h\), with all convolutions locally finite or locally integrable by support.

Take \(b_L(v)=1\) for \(v<0\) and \((1-v/L)_+\) for \(v\ge0\). The normalized weighted approximant is \(K*(b_Lm)\). The product rule gives \(b_Lm=(\partial+1/2)(b_Lh)-b_L'h\), valid also at the two corners by continuity of \(b_L\). Thus the normalized residual is
\[
 (1-b_L(v))G(v)
 +\int_0^\infty T(t)\bigl[b_L(v)-b_L(v-t)\bigr]h(v-t)\,dt
 +K*(b_L'h)(v).
\]
The first term has norm \(O(1/L)\), since \(G\) has fixed compact support. For the second, causality is essential: if \(v-t\ge L\), both taper values are zero, and if \(v-t<0\) the function \(h\) is zero. On the remaining interval the absolute taper difference is at most \(t/L\). Young's inequality bounds this term by \(L^{-1}\|tT(t)\|_1\|h\|_{L^2(0,L)}\). The last term is at most \(L^{-1}\|K\|_1\|h\|_{L^2(0,L)}\). Squaring proves (1).

Weak Mertens bounds \(\int_0^L |h|^2\) by \(O(L)\); the weaker condition \(o(L^2)\) already implies convergence in this explicit construction. These are additional arithmetic hypotheses. Inequality (1) does not supply them. The smooth average is used in the proof exactly where the derivative of the sawtooth kernel is estimated in an integrable norm.

## A taper chosen from the actual Mertens function

The same argument gives a criterion using a harmonic average of recent normalized Mertens energy. Set
\[
 A(r)=1+|h(r)|^2+\int_0^r e^{-(r-w)/4}|h(w)|^2dw,\qquad
 D(L)=\int_0^L\frac{dr}{A(r)} .
\]
For every \(L>0\) there is an explicit taper with coefficients supported on \(n\le e^L\) whose full squared error is at most \(C/D(L)\). Thus \(D(L)\to\infty\) implies RH. More quantitatively, if a zero \(\rho=\beta+i\gamma\) has \(\beta>1/2\), then
\[
 \int_0^\infty\frac{dr}{A(r)}
 \ll \frac{|\rho|^4}{(2\beta-1)|p(\rho)|^2}
 \ll \frac{|\rho|^4}{2\beta-1}.
 \tag{3}
\]
The last absolute inequality uses the established \(\beta\le7/8\), which bounds both factors of \(p(\rho)\) away from zero uniformly. In particular the total Lebesgue measure of \(\{r\ge0:A(r)\le Y\}\) is \(O_\rho(Y)\) for every \(Y>0\) if such a zero exists. This is a restriction on the full infinite logarithmic-time axis.

For (3) take the simpler average with \(\varphi=1_{[0,1]}\). Its Laplace transform is \((1-e^{-s})/s\). The derivative of \(JF(e^v)=\int_{v-1}^v F(e^w)dw\) exists almost everywhere and is bounded by \(2\|F\|_\infty\), so the same exponential kernel bounds hold. Let \(b\) be a Lipschitz taper equal to one before zero and zero after \(L\). With \(b\) in the preceding commutator identity, its compact target term has squared norm \(O(\int_0^L|b'(r)|^2dr)\), by Cauchy–Schwarz on the fixed support of \(G\). The last term costs \(O(\int_0^L |b'(r)|^2 |h(r)|^2dr)\). For the middle term Cauchy–Schwarz first in \(t\) with the weight \(e^{-t/2}\), then on \([v-t,v]\), bounds its squared absolute value by
\[
 C\int_0^\infty e^{-t/2}t\, |h(v-t)|^2
                  \int_{v-t}^{v}|b'(r)|^2dr\,dt .
\]
On integrating in \(v\), setting \(w=v-t\), and using
\(\int_{r-w}^\infty t e^{-t/2}dt\ll e^{-(r-w)/4}\) for \(r\ge w\), this costs at most \(C\int_0^L |b'(r)|^2(A(r)-1-|h(r)|^2)dr\). Hence the full error is bounded in square by \(C\int_0^L A(r)|b'(r)|^2dr\). Its minimizing taper on \([0,L]\) is
\[
                       b(v)=1-D(v)/D(L).
\]
It is Lipschitz since \(A\ge1\); its weighted energy is \(1/D(L)\). All coefficients use the actual \(M(x)\) only through \(x\le e^L\).

For an off-line zero the Mellin value of the residual is the fixed nonzero number \((1-e^{-\rho})p(\rho)/\rho^2\). The squared norm of Mellin evaluation on \(u\ge1\) is \(1/(2\beta-1)\). The resulting lower bound for the squared error, together with \(|1-e^{-\rho}|\ge1-e^{-1/2}\), gives (3) for every \(L\), and then for its increasing limit. The arithmetic issue is whether \(D(L)\) grows without bound. Formula (3) alone gives no lower estimate for it.

## An all-scale lower bound from an individual zero

For every zero \(\rho=\beta+i\gamma\) with \(\beta\ge1/2\) and every \(X\ge e^4\),
\[
 \frac{1}{\sqrt X}\int_1^X \frac{M(u)^2}{u^{3/2}}du
 \gg \frac{|p(\rho)|^2}{|\rho|^4}X^{\,2\beta-1}.
 \tag{4}
\]
The implied constant can be taken as \(1/2000\). This gives a one-sided-in-time mean-square counterpart to the [localized Möbius sum test](nov18b-reciprocal-theta.md). As a consequence the cumulative normalized Mertens energy has an actual growth exponent:
\[
 \lim_{X\to\infty}
 \frac{\log\!\left(1+\int_1^X M(u)^2\,du/u^2\right)}{\log X}
       =2\Theta-1 .
 \tag{5}
\]
The pointwise bound \(M(u)\ll_\epsilon u^{\Theta+\epsilon}\) gives the upper limit. The integral on the left of (4) is bounded by \(\int_1^X M(u)^2du/u^2\). Taking the lower limit using each fixed off-line zero and then their supremum proves (5). When \(\Theta=1/2\) nonnegativity suffices for the lower limit in (5). Even on that boundary (4) gives a positive absolute lower bound on the weighted energy at every large scale by selecting any fixed critical-line zero.

Use the uniform averaging window of (3) and fix a real cutoff \(e^\tau\) with \(\tau>\log4+1\). The sharp approximant uses \(\mu(n)\) for every \(n\le e^\tau\). Its normalized residual vanishes for \(v<\tau\), by causal Möbius inversion. For \(v>\tau\) the normalized target \(G(v)\) vanishes. The residual there is the negative of the Stieltjes integral of \(K(v-w)\) against \(m\) over \(w\le\tau\). Integration by parts writes this integral as
\[
              K(v-\tau)h(\tau)+\int_0^\tau T(v-w)h(w)\,dw .
\]
The displayed upper-end term takes the right-continuous value of \(M\), permitting an integer cutoff. The exponential kernel bounds and Cauchy–Schwarz give a full squared-norm bound of
\[
 C\bigl[|h(\tau)|^2+B(\tau)\bigr],\qquad
 B(\tau)=\int_0^\tau e^{-(\tau-w)/2}|h(w)|^2dw .
\]
Indeed, factor \(e^{-(v-\tau)/2}\) from both terms. The square of the remaining weighted \(L^1\) integral is at most \(2B(\tau)\). Integrating in \(v\) now costs an absolute constant.

The residual's Mellin value at \(\rho\) is the target value \((1-e^{-\rho})p(\rho)/\rho^2\). Integrating the preceding pointwise envelope against \(e^{-(\rho-1/2)v}\) on \(v\ge\tau\) bounds this Mellin value by \(C e^{-(\beta-1/2)\tau}[|h(\tau)|^2+B(\tau)]^{1/2}/\beta\). This integration converges also at \(\beta=1/2\), since the physical tail has exponential decay in \(v-\tau\). Thus
\[
 |h(\tau)|^2+B(\tau)\gg
 e^{(2\beta-1)\tau}|p(\rho)|^2/|\rho|^4 .
\]
Set \(L=\log X\). For each \(\tau\in[L-1,L]\) one has \(B(\tau)\le e^{1/2}B(L)\), and some such \(\tau\) also has \(|h(\tau)|^2\le e^{1/2}B(L)\). Since \(0\le2\beta-1<1\), moving \(\tau\) to \(L\) loses at most an absolute factor. Finally \(B(L)=X^{-1/2}\int_1^X M(u)^2u^{-3/2}du\), which proves (4).


For the numerical constant in (4), \(F(x)\) equals \(0,1,-1,0\) on the four successive unit intervals modulo 4, so \(|K(v)|\le e^{-v/2}\) on \(v\ge0\). The uniform average gives \(T(v)=e^{-v/2}(F(e^v)-F(e^{v-1}))\), of absolute value at most \(2e^{-v/2}\). Thus the pointwise envelope above is explicitly \(e^{-(v-\tau)/2}(|h(\tau)|+2\sqrt{2B(\tau)})\). At the selected \(\tau\), comparison with the exact Mellin value yields the valid absolute coefficient
\[
 \frac{e^{-3/2}(1-e^{-1/2})^2}{4(1+2\sqrt2)^2}>\frac1{2000}.
\]
