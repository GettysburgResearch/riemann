# A power gain in the native Möbius sawtooth tail

Put \(B(x)=\{x\}-1/2\) and \(S_N(u)=\sum_{n\le N}\mu(n)B(u/n)\). For every fixed \(\eta>0\) there is \(c_\eta>0\) such that
\[
 \int_{N^{35/24+\eta}}^\infty |S_N(u)|^2\frac{du}{u^2}
      \ll_\eta N^{-c_\eta}.                                      \tag{1}
\]
The imported input is the zero-free half-plane \(\Re s>7/8\). Below we use it for short twisted Möbius factors, and derive the estimate for the native sharp arithmetic coefficients. The same conclusion holds with \(S_N\) replaced by its fixed linear combination of dilations. The interval starting at \(u=N\) remains open for this approximant. [Frozen theorem and kernel receipts](nov18b-reciprocal-formal-audit.md) · [Fourier reduction and previous tail bounds](nov18b-reciprocal-sawtooth.md)

## A twisted Möbius factor

Throughout, \(N\) is a large integer. Factors \(N^\epsilon\) below can be taken for any fixed \(\epsilon>0\), by reducing \(\epsilon\) in intermediate estimates. For \(m\le N^C\), set \(f_m(n)=\mu(n)1_{(n,m)=1}\), \(g_m(n)=1_{(n,m)=1}\). Uniformly over \(1\le M\le N\), intervals \(I\subset[M,2M]\), and \(|t|\le N^C\),
\[
 \left|\sum_{n\in I} f_m(n)n^{-it}\right|
       \ll_{\epsilon,C} N^\epsilon M^{7/8}.                       \tag{2}
\]
Here are details of the zero-free-strip consequence. On each narrower half-plane \(\sigma\ge7/8+\delta\), \(1/\zeta(\sigma+it)\ll_{\delta,\kappa}(2+|t|)^\kappa\) for every \(\kappa>0\). At large \(|t|\), take concentric discs centered at \(2+it\) in the zero-free half-plane, with a branch of \(\log\zeta\) chosen by the Euler product at the center. Polynomial growth of \(\zeta\) and Borel–Carathéodory first give \(|\log\zeta|\ll_\delta\log |t|\) on the disc of radius \(2-7/8-\delta/4\). The same function is bounded on the disc of radius \(1/2\). Hadamard's three-circles theorem bounds it by \(O_\delta((\log|t|)^{a_\delta})\), \(a_\delta<1\), on the disc of radius \(2-7/8-\delta/2\). The remaining real parts follow from the Euler product, and the inverse is analytic at 1 with a zero there.

The extra factor \(\prod_{p\mid m}(1-p^{-s})^{-1}\) in the Dirichlet series of \(f_m\) costs \(N^\epsilon\) on each such half-plane. For large \(p\), its logarithmic cost is at most an arbitrarily small multiple of \(\log p\), and the remaining primes cost a constant. For half-integer cutoffs \(x\asymp M\), apply truncated Perron to this series at \(s+it\), starting at \(\Re s=1+1/\log N\) and height \(N^{C+10}\). The endpoint error is \(O(M\log^2(2N)/N^{C+10})\), by \(|f_m|\le1\) and the half-integer separation. Move to \(\Re s=7/8+\delta\). The horizontal sides cost \(O(N^{-2})\), and the vertical side costs \(O(M^{7/8+\delta}N^\epsilon)\) by the bound just proved. Taking differences and decreasing \(\delta,\epsilon\) proves (2).

## Three-factor mean square

Use \(1\le T\le Q\le N\), \(Q\) dyadic, and the parameters \(m,t\) in the ranges above. For each product block of the decomposition below, with its product restricted only by separate dyadic bounds on its three factors, one has
\[
 \int_{T}^{2T} |P(t)|^2\,dt
 \ll_\epsilon N^\epsilon Q^2
      \bigl(Q^{-1/12}+TQ^{-5/8}+T^{-1}\bigr).                    \tag{3}
\]
Here \(P\) is the product of the three Dirichlet polynomials. The estimate holds on negative height intervals by conjugation, and on fixed positive multiples of the height interval by covering. We only use blocks with product of lengths comparable to \(Q\).

Take \(Y=\lceil\sqrt{2Q}\rceil\) and \(f_{m,Y}(n)=f_m(n)1_{n\le Y}\). The convolution \(f_m*g_m\) equals the unit \(\delta_1\). The sequence \((\delta_1-f_{m,Y}*g_m)^{*2}\) is supported above \(Y^2\). Convolving with \(f_m\) shows, for \(Y<q\le2Q\),
\[
 f_m(q)=-(f_{m,Y}*f_{m,Y}*g_m)(q).                               \tag{4}
\]
Split the three variables into independent dyadic blocks of lengths \(A,B,C\), so \(ABC\asymp Q\), \(A,B\ll Q^{1/2}\). Dyadic blocks meeting the cutoff \(Y\) are truncated individually. Let \(M=\max(A,B,C)\), \(R=Q/M\). In the mean-square integral, put the factor of length \(M\) in the supremum. The product of the others has coefficients bounded by the divisor function and support in \([1,O(R)]\). The elementary Dirichlet polynomial mean-value theorem bounds its mean square by \(N^\epsilon(T+R)R\). The same theorem applied to the full product gives \(O(N^\epsilon Q^2)\) for \(T\ll Q\).

If a Möbius factor is largest, (2) gives, on dividing by \(N^\epsilon Q^2\),
\[
 M^{-1/4}(1+TM/Q)\ll Q^{-1/12}+TQ^{-5/8},
\]
since \(Q^{1/3}\ll M\ll Q^{1/2}\). If the ordinary coprime factor is largest, its polynomial on any subinterval of \([C,2C]\) satisfies both bounds
\[
 \ll N^\epsilon(\sqrt T+C/\sqrt T),\qquad
 \ll N^\epsilon(T+C/T).
\]
For the first, expand the coprimality condition over \(d\mid m\) and apply the second-derivative test to \(-t\log n\) on the interval of length scale \(C/d\). For the second, use the first-derivative test if \(C/d\) exceeds a sufficiently large absolute multiple of \(T\), and the trivial bound otherwise. Each sum over \(d\) costs at most \(\tau(m)\ll N^\epsilon\). Empty intervals cost zero.

If \(C\le T^{3/2}\), the ratio from the first bound is
\[
 (T/C^2+1/T)(1+TC/Q)
 \ll TQ^{-2/3}+T^{-1}+T^2Q^{-4/3}+T^{3/2}/Q.
\]
If \(C>T^{3/2}\), the second gives
\[
 (T^2/C^2+T^{-2})(1+TC/Q)\ll T^{-1}+T^{3/2}/Q .
\]
For \(TQ^{-5/8}\le1\), each positive power of \(T\) on the right of these last two displays costs \(O(TQ^{-5/8})\), since \(TQ^{-2/3}\le1\). Otherwise the full-product mean-value bound suffices. This proves (3).

## Transfer to the reciprocal phase

Retain \(q\ge N^{7/8}\), \(1\le |j|\le N^{1/8}\), and restrict temporarily to \(N^{35/24}\le V\le 2N^{1.51}\). In a dyadic block \(q\asymp Q\) write \(T=|j|V/Q\). Here \(N^{0.45}\ll T\ll N^{0.77}\) and \(T\ll Q\). For every interval \(I\subset[Q,2Q]\) from this range and \(m\le N^C\),
\[
 \int_V^{2V}\left|\sum_{q\in I} f_m(q)e(ju/q)\right|^2du
 \ll_\epsilon N^\epsilon\frac{Q^3}{|j|}
       \bigl(Q^{-1/12}+TQ^{-5/8}+T^{-1}+N^{-1/8}\bigr),          \tag{5}
\]
where \(e(v)=\exp(2\pi iv)\).

First replace the indicator of \(I\) by a smooth weight \(w(\log(q/Q))\), supported inside \(I\) and equal to one except within log-distance \(O(N^{-1/8})\) of its ends. For an interval shorter than twice that width take zero. At most \(O(QN^{-1/8})\) coefficients change. Their frequencies \(j/q\) have separation \(\gg |j|/Q^2\). The large sieve in the physical variable \(u\) costs \(O((V+Q^2/|j|)QN^{-1/8})\), which gives the last term in (5). Choose the smoothed weight by convolving an interior shortened interval with a fixed nonnegative smooth compactly supported mollifier of log-width \(N^{-1/8}\). Its Fourier transform has \(L^1\) norm \(O(\log N)\), with arbitrarily large power decay in \(L^1\) for frequencies above \(N^{1/3}\).

Take a fixed compactly supported smooth cutoff \(\psi\) equal to one on \([-\log 2,\log 2]\), and \(K(x)=\psi(x)e(\operatorname{sgn}(j)T e^x)\). With \(y=\log(u/V)\), the phase equals \(K(y-\log(q/Q))\) for \(u\in[V,2V]\). By Plancherel in \(y\), extending the nonnegative integral to the real line, its unweighted square norm in \(u\) is at most
\[
 \ll V\int_{\mathbb R}|\widehat K(t)|^2
  \left|\sum_q f_m(q)w(\log(q/Q))q^{-it}\right|^2dt .
\]
On \(cT\le |t|\le C_1 T\), the second-derivative test gives \(|\widehat K(t)|\ll T^{-1/2}\). Outside this band, with \(c,C_1\) chosen from the fixed support, integration by parts gives \(\ll_a(T+|t|)^{-a}\) for every fixed \(a\). In the smoothed polynomial insert (4) and split into \(O(\log^3 N)\) product blocks with \(ABC\asymp Q\). Fourier inversion of \(w\) shifts \(t\) by at most \(N^{1/3}=o(T)\), apart from a negligible tail. Apply Minkowski, (3) on fixed multiples of the original height band, and \(\|\widehat w\|_1\ll\log N\). This costs \(N^\epsilon VQ^2/T\) times the bracket in (3), as required.

## Summing all coefficients

At a reduced frequency \(j/q\), the Fourier coefficient of \(S_N\) is \(-(2\pi i j)^{-1}\sum_{k\le N/q}\mu(qk)/k\). Discarding \(q<N^{7/8}\) or \(|j|>N^{1/8}\) costs
\[
 \ll (V+N^2)N^{7/8}\log^2 N
\]
in integrated square by spacing \(N^{-2}\). In the retained region \(\mu(qk)1_{(q,j)=1}=\mu(k) f_{|j|k}(q)\). Apply (5) and sum the norms with weights \(1/(|j|k)\). The \(k\)-sum costs \(O(\log N)\). For each contribution, the dyadic \(Q\)-sum is bounded by its increasing power at \(Q=N\). The \(j\)-sums are convergent except for the harmonic sum in the second term below. The resulting square-root bound is
\[
 \|S_N\|_{L^2[V,2V]}
 \ll_\epsilon N^\epsilon
 \bigl(N^{35/24}+V^{1/2}N^{11/16}+V^{-1/2}N^2+N^{23/16}\bigr).
\]
For \(V\ge N^{35/24+\eta}\), division by \(V\) gives a power saving termwise. Sum the weighted integrals on dyadic shells up to \(N^{1.51}\). Beyond that point use the full-coefficient large sieve \(\int_V^{2V}|S_N|^2\ll(V+N^2)N\) from the linked Fourier reduction. This proves (1), also for larger choices of \(\eta\) by monotonicity.
