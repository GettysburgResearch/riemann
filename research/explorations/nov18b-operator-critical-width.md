# The critical inverse-pole sum for Pick matrices escaping along the real axis

**Proposed theorem.** Let \(W_*\) be the infimum of the widths of intervals supporting a complex smooth compactly supported test on which the full Weil form of the Riemann zeta function is negative. Set \(W_*=\infty\) when no such test exists. Consider real-node Pick packets with \(A\le a_j\le C A\), where \(C\) is fixed and \(A\to\infty\), and set \(S=\sum_j1/a_j\), counting multiplicities. The transition for the exact polarized form is at \(S=W_*/2\).

* For every fixed \(L<W_*/2\), all sufficiently large packets with \(S\le L\) are strictly positive on their nonzero rational test spaces, uniformly in the count and spacing.
* For every fixed \(L>W_*/2\), every sufficiently large packet with \(S\ge L\) has a negative direction. This implication requires only \(\min a_j\to\infty\), and allows unbounded ratios between the nodes.

These assertions allow distinct or repeated poles. For the repeated pole \(a\) let \(k_-(a)\) denote the least pole multiplicity at which a negative direction exists, with value infinity if none exists. Thus
\[
 \lim_{a\to\infty}\frac{k_-(a)}a=\frac{W_*}{2}
\]
in the extended sense. By the Weil criterion, \(W_*=\infty\) exactly under RH. The [earlier proposed coercivity proof at radius \(8/3\)](weil-eight-thirds-nov18.md) gives \(W_*\ge16/3\), hence positivity for every such escaping packet with \(S\le8/3-\epsilon\). This includes unbounded interpolation orders proportional to the real abscissa. The [unconditional small-density theorem](nov18b-operator-unbounded-sector.md) gives a separate uniform estimate without an asymptotic passage.

## The form on a fixed interval

Use \(G(z)=\int g(u)e^{zu}du\), \(\lambda=\rho-1/2\), and \(\mathcal W(g)=\sum_\lambda G(\lambda)\overline{G(-\bar\lambda)}\). On a fixed bounded interval, the explicit formula expresses this as the Fourier integral with multiplier \(\Re\psi(1/4+it/2)-\log\pi\), up to bounded quadratic forms on \(L^2\) coming from two polar evaluations and finitely many prime-power translations. The gamma multiplier is \(\log(2+|t|)+O(1)\). The form is therefore closed and semibounded on the completion with the Fourier norm \(\int\log(2+|t|)|G(it)|^2 dt\). This domain embeds compactly into \(L^2\), by compact spatial support and the Fourier tail bound. Smooth compactly supported functions form a core: a small affine compression into the interval followed by smoothing converges in the weighted Fourier norm. Translation preserves the form, including the off-line summands.

For every \(W<W_*\) the form on a support interval of width \(W\) has a strictly positive lower bound times \(\|g\|_2^2\). Indeed a nonnegative closed form with the compact embedding above has its bottom eigenvalue attained. If a nonzero null vector existed, translate it through all small displacements keeping it in a fixed larger interval of width \(W'<W_*\). Its translates have zero quadratic form there, so by nonnegativity and polarization they belong to the nullspace. These translates span an infinite-dimensional space: a finite linear relation would require an exponential polynomial to vanish on an open set of the Fourier transform. This contradicts finite nullity from compactness. This also establishes strict coercivity in every finite smaller window when RH holds.

## Every negative continuum test transfers to the real packets

Let \(P_0(z)=1\), \(P_j(z)=\prod_{l\le j}(a_l+z)/(a_l-z)\) and \(u_j=2\sum_{l\le j}1/a_l\). Given a smooth test supported in the interior of \((0,2L)\), define
\[
 R(z)=\sum_j \frac{2}{a_j-z}P_{j-1}(z)g(u_{j-1}).
\]
This proper rational function has the specified poles. For packets with \(S\ge L\) one can truncate at the first index where \(u_j\ge2L\). For fixed \(z\), the mesh of this partition tends uniformly to zero, and \(P_j(z)=\exp(zu_j+o(1))\) uniformly through the truncation. This follows by expanding \(\log((a_l+z)/(a_l-z))\), since \(\sum a_l^{-3}\le S/(\min a_l)^2\). Thus \(R(z)\to G(z)\) by ordinary Riemann summation.

For \(|\Re z|\le1/2\), each \(|P_j(z)|\) is bounded by a constant depending only on \(L\), using \(\log((a_l+1/2)/(a_l-1/2))\ll a_l^{-1}\). Also \(2P_{j-1}/(a_j-z)=(P_j-P_{j-1})/z\). Summation by parts bounds \(|R(z)|\ll_{g,L}(1+|\Im z|)^{-1}\) on this strip; near zero use the original sum. Since the zero-counting measure integrates \((1+|\Im z|)^{-2}\), the rational resolvent form tends to \(\mathcal W(g)\), uniformly in the choice of sufficiently fine meshes in the sequential sense. When \(L>W_*/2\), translation supplies a negative such \(g\). This proves the negative implication.

## Every positive-margin window controls the packets below it

Suppose \(S\le L<W_*/2\) and \(A\le a_j\le CA\). Fix \(2L<U<V<W_*\), with finite \(V\). Let \(R\) be a proper rational function with these poles, and write it as \(R(z)=\int_0^\infty g(u)e^{zu}du\) on \(\Re z< A\). Normalize \(\|g\|_2=1\). For \(0<\sigma<A\), dividing out the full product \(P_k\) converts \(R/P_k\) into a proper rational function with poles in the left half-plane. Its Hardy norm on \(\Re z=\sigma\) is no greater than its boundary norm at zero, which equals that of \(R\) by unimodularity. Plancherel gives
\[
 \|e^{\sigma u}g\|_2\le\prod_j\frac{a_j+\sigma}{a_j-\sigma}.
\]
Choose a fixed small \(\theta>0\) and put \(\sigma=\theta A\). The logarithm of the bound is at most \(2\sigma L\operatorname{arctanh}(\theta)/\theta\), strictly below \(\sigma U\) by a fixed multiple of \(\sigma\) if \(\theta\) is small enough.

The same tail bound, times a polynomial in \(A\), holds for the ordinary derivative \(g'\) on \(u>0\). Here are details ensuring uniformity even at coalescent nodes. The functions
\[
 v_j(z)=\frac{\sqrt{2a_j}}{a_j-z}P_{j-1}(z)
\]
are an orthonormal basis of the packet in the boundary norm \((2\pi)^{-1}\int |R(it)|^2 dt\). This follows successively from the elementary Hardy kernel at \(-a_j\), or by contour integration after canceling the common unimodular factors. The inverse transform of \(v_j\) has right limit \((-1)^{j-1}\sqrt{2a_j}\) at zero by its expansion at negative infinity. Its derivative has transform \(-g_j(0)-zv_j(z)\), a proper rational function of the same allowed poles. Since \(zv_j=a_jv_j-\sqrt{2a_j}P_{j-1}\), telescope the difference \(P_{j-1}-(-1)^{j-1}\) on the boundary. Each elementary factor plus 1 has boundary norm \(\sqrt{2a_l}\), and the other factors are unimodular. Hence \(\|g_j'\|_2\ll kCA\), and Cauchy–Schwarz gives \(\|g'\|_2\ll k^{3/2}CA\) and \(|g(0)|\le\sqrt{2kCA}\). Also \(k\le CAL\). Applying the preceding Hardy argument to the transform of \(g'\) proves the assertion.

Choose a smooth cutoff \(\chi\) equal to one on \([0,U]\) and zero beyond \(V\). The preceding bounds and Cauchy–Schwarz imply
\[
 \int_U^\infty e^{u/2}(|g(u)|+|g'(u)|)du\ll e^{-cA},
\]
for all sufficiently large \(A\), absorbing the fixed polynomial. The corresponding full integrals, including the initial value, grow at most polynomially in \(A\). Integrating once by parts in the oscillatory variable therefore bounds each transform of \(g\) or \(\chi g\) on the zero strip by \(A^{O(1)}/(1+|\Im z|)\), and the transform of their difference by \(O(e^{-cA}/(1+|\Im z|))\). The form of \(g\) differs from that of \(\chi g\) by \(O(e^{-c' A})\) uniformly on the packet unit sphere. The cutoff lies in the closed form domain on \([0,V]\), including its allowed endpoint jump at zero, and its \(L^2\) norm tends uniformly to one. Strict coercivity at width \(V\) proves the positive implication.

This is a limit theorem for the actual normalized matrices and the complete source form. Increasing the pole count while keeping \(S\) bounded does not by itself control larger support. The arithmetic burden for RH is positivity at unbounded widths, equivalently positive packets with unbounded inverse-pole sum along the escaping real regime.
