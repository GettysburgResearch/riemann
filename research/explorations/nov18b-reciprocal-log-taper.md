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
