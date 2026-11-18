# A first-shell obstruction for Möbius approximants

For the sharp cutoff studied in the [sawtooth tail estimate](nov18b-reciprocal-sawtooth.md), the single interval \(N<u<2N\) already prevents convergence in \(L^2(du/u^2)\). Its error has exact upper growth exponent \(2\Theta-1\), where \(\Theta\) is the supremum of the real parts of nontrivial zeta zeros. An obstruction persists for every fixed smooth cutoff depending on \(n/N\). The interval detecting it can then depend on the cutoff. Báez-Duarte studied the failure of natural Möbius approximants in the full norm. The calculations below localize the obstruction, give a contribution from each critical-line zero, and allow fixed dilation filters. [Báez-Duarte, §§4–5](https://doi.org/10.1155/S0161171202013248)

## Exact sharp shell

Write \(M(x)=\sum_{n\le x}\mu(n)\), \(D_qg(u)=g(u/q)\), \(P=(1-D_2)(1-2D_2)\) and
\[
 R_N=P\left(1_{u\ge1}+\sum_{n\le N}\mu(n)(\{u/n\}-1/2)\right).
\]
The operator kills constants and linear functions. Since \(\sum_{n\ge1}\mu(n)\lfloor u/n\rfloor=1_{u\ge1}\), its argument reduces after filtering to \(\sum_{N<n\le u}\mu(n)\lfloor u/n\rfloor\). For \(N<u<2N\) each floor here equals one and both dilated terms vanish. Hence \(R_N(u)=M(u)-M(N)\) on this interval, independent of any zeta-zero hypothesis.

For \(1<b\le2\) define
\[
 J_b(X)=\int_X^{bX}|M(u)-M(X)|^2\,\frac{du}{u^2},\quad
 L=\log b,\quad h(v)=e^{-v/2}M(e^v).
\]
At \(X=e^v\) the integrand in logarithmic coordinates is the square of
\(D(v,y)=h(v+y)-e^{-y/2}h(v)\), with \(0\le y\le L\). Regard \(D(v,\cdot)\) as a vector in \(L^2(0,L)\). Its squared norm is \(J_b(e^v)\). Initially for \(\Re s>1\),
\[
 \int_0^\infty e^{-(s-1/2)v}D(v,y)\,dv
  = \frac{e^{-y/2}(e^{sy}-1)}s\left(\frac1{\zeta(s)}-1\right).
 \tag{1}
\]
Indeed \(\int_1^\infty M(x)x^{-s-1}dx=1/(s\zeta(s))\), and \(M(x)=1\) almost everywhere on \([1,e^y]\). The subtraction on the right accounts for this lower endpoint.

For \(N=\lfloor X\rfloor\), \(J_b(X)-J_b(N)=o(1)\) uniformly as \(N\to\infty\). The lost lower segment has zero integrand. The added upper segment has bounded length, its numerator is \(o(N^2)\) by \(M(t)=o(t)\), and the denominator is comparable to \(N^2\).

If \(J_b(N)\ll N^{2a-1}\) for some \(a\ge1/2\), (1) defines a holomorphic vector on \(\Re s>a\). Its right side would have a pole at every zeta zero there, because the vector \(e^{-y/2}(e^{sy}-1)\) is nonzero. Thus \(\Theta\le a\). Conversely the standard zero-free half-plane estimate \(M(x)\ll_\epsilon x^{\Theta+\epsilon}\) gives
\[
 \limsup_{N\to\infty}\frac{\log(1+J_b(N))}{\log N}=2\Theta-1 .
 \tag{2}
\]
For the stated estimate on \(M\), Perron's formula shifted to \(\Theta+\epsilon\) uses the classical subpower reciprocal bound on each strictly narrower zero-free half-plane. The proof is spelled out for the particular boundary \(7/8\) in the [strip-tail note](nov18b-reciprocal-strip-tail.md). The same argument applies to every \(\Theta<1\), and the trivial bound suffices at \(\Theta=1\).

## A positive critical-line contribution

For every finite set \(\mathcal S\) of distinct simple critical-line zeros,
\[
 \liminf_{\epsilon\downarrow0}
 \epsilon\int_0^\infty e^{-\epsilon v}J_b(e^v)\,dv
 \ \ge\
 \sum_{\rho\in\mathcal S}
 \frac{\int_0^L e^{-y}|e^{\rho y}-1|^2dy}{|\rho\,\zeta'(\rho)|^2}.
 \tag{3}
\]
A zero to the right of the line makes the left side infinite. Indeed finiteness of the integral at \(\epsilon\) would, by Cauchy–Schwarz, continue (1) to \(\Re s>1/2+\epsilon/2\). On RH the elementary bound on \(M\) just used makes all these integrals finite. Use the probability measure \(\epsilon e^{-\epsilon v}dv\) and project the vector-valued function \(D\) onto the finite collection of scalar characters \(v\mapsto e^{i\Im\rho\,v}\), allowing coefficients in \(L^2(0,L)\). Their Gram matrix tends to the identity, and their inner products with \(D\) are \(\epsilon\) times (1) at \(s=\rho+\epsilon\). Taking residues gives (3). If there is a multiple critical-line zero of order \(m\), the same single-frequency bound grows at least as a positive constant times \(\epsilon^{2-2m}\).

The existence of critical-line zeros therefore gives \(\limsup_N J_b(N)>0\), including when \(\Theta=1/2\). A positive Abel lower bound implies that limsup lower bound, since every bounded initial interval has vanishing mass as \(\epsilon\) tends to zero. This proves failure on the first shell for the particular filtered sequence despite the power decay of its [far tail](nov18b-reciprocal-strip-tail.md).

The shell also characterizes the classical weak Mertens mean square:
\[
 \sum_{N\le X}\frac{J_b(N)}N\ll\log(2X)
 \quad\Longleftrightarrow\quad
 \int_1^X \frac{M(u)^2}{u^2}\,du\ll\log(2X).
 \tag{4}
\]
For the upper estimate, integrate \(\|D(v,\cdot)\|^2\) on \(0\le v\le V\) and use the triangle inequality to bound the result by \(O_L(\int_0^{V+L}|h(v)|^2dv)\). For the reverse estimate and \(L/2\le y\le L\), the norm on \(0\le v\le V-y\) of \(D(v,y)\) is at least
\((1-e^{-y/2})\|h\|_{L^2(0,V)}-O_L(1)\), by translation and the reverse triangle inequality. Integrating over these \(y\) gives the reverse control up to a constant. The comparison of \(J_b(X)\) with \(J_b(\lfloor X\rfloor)\) above and the comparability of \(1/N\) and \(\log(1+1/N)\) give (4) at integer scales.

## All fixed cutoff shapes

Let \(w\) be a bounded compactly supported function of bounded variation on \((0,\infty)\) with \(w(t)=1+O(t^\kappa)\) at zero for some \(\kappa>0\). Allow any fixed finite filter \(P=\sum_{j=1}^k c_jD_{q_j}\), with distinct positive \(q_j\), not all \(c_j\) zero, and \(\sum c_j=\sum c_j/q_j=0\). Define \(R_X\) as above using \(\mu(n)w(n/X)\) at all integers \(n\). Then there exist \(0<a<A<\infty\) for which
\[
       \limsup_{N\to\infty}
       \int_{aN}^{AN}|R_N(u)|^2\,\frac{du}{u^2}>0 .
 \tag{5}
\]
More precisely, any given off-line zero \(\rho\) with \(\Re\rho>1/2\) forces the limsup exponent of \(1+\int_{aN}^{AN}|R_N(u)|^2du/u^2\) to be at least \(2\Re\rho-1\) on some such shell. Logarithmic tapers with a shape varying with \(N\), such as \(1-\log n/\log N\) up to \(N\), are outside these hypotheses.

Put \(f=1-w\), \(F(x)=\sum c_j\lfloor x/q_j\rfloor\), which is bounded and zero near zero. Möbius inversion gives \(R_X(rX)=\sum_n\mu(n) f(n/X) F(rX/n)\). The Mellin transform in the **cutoff** \(X\), initially for \(\Re s>1\), gives
\[
 \int_0^\infty R_X(rX)X^{-s-1}dX
 =\frac{H_r(s)}{\zeta(s)},\qquad
 H_r(s)=\int_0^\infty f(t)F(r/t)t^{s-1}dt.
 \tag{6}
\]
The change of variables \(t=n/X\) proves the identity by absolute convergence. For \(r\) in a compact positive interval the numerator is holomorphic on \(\Re s>-\kappa\), locally uniformly in \(r\), since \(F(r/t)\) vanishes past a fixed upper bound on \(t\).

For every nontrivial zero \(\rho\) the function \(r\mapsto H_r(\rho)\) is nonzero on a set of positive measure in some compact positive interval. Indeed for \(\Re\rho<\Re z<\Re\rho+\kappa\) its Mellin transform in the **physical location** \(r\) is
\[
 \int_0^\infty H_r(\rho)r^{-z-1}\,dr
 =\left(\int_0^\infty f(t)t^{\rho-z-1}dt\right)
   \frac{\zeta(z)}z\sum_j c_j q_j^{-z}.
 \tag{7}
\]
The transform of \(F\) follows by summing floors on \(\Re z>1\) and continuing to \(\Re z>0\) by its boundedness; the apparent pole at one is removable by balance. Absolute convergence on the indicated strip justifies separation. The first factor is not identically zero by Mellin uniqueness, since \(f=1\) for large \(t\). The finite exponential polynomial of distinct exponents is not identically zero either. This proves the claim.

Choose a compact interval \(I\) where \(H_{\bullet}(\rho)\) has nonzero norm in \(L^2(I,dr/r^2)\). On that interval (6) has a genuine vector pole at \(\rho\). Restricting the \(X\) integral to \(X\ge1\) changes it by an entire vector because \(R_X(rX)=0\) for all sufficiently small \(X\), uniformly on \(I\). For a critical-line zero the normalized function \(X^{-1/2}R_X(rX)\) cannot tend to zero in this Hilbert space. Otherwise the transform multiplied by \(\epsilon\) at \(s=\rho+\epsilon\) would tend to zero by the elementary Abel final-value bound. This contradicts its nonzero residue for a simple zero, or a pole of higher order. For an off-line zero the same reasoning as for (2) precludes every strictly smaller exponent.

To pass to integer scales, keep the physical variable \(u\) fixed when comparing \(X\in[N,N+1)\) with \(N\). On a shell \(u\asymp N\) one has \(F(u/n)=0\) for \(n>C N\). The variation intervals with endpoints \(n/X,n/N\) have uniformly bounded overlap for \(n\le C N\): for fixed \(t\) in such an interval, \(Nt\le n\le Xt\) up to endpoint conventions and \(t\le C+1\). Bounding the sum of all endpoint differences by a fixed multiple of the variation (including any isolated point values) gives \(\sup_{u\asymp N}|R_X(u)-R_N(u)|=O(1)\). Its shell norm is \(O(N^{-1/2})\). A fixed enlarged shell contains \(XI\) throughout \(N\le X<N+1\), proving (5) and the asserted off-line variant.
