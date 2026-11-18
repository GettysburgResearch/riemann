# A short sum of ordinary integers forced by a regularly spaced off-line plateau

**Proposed estimate.** A plateau in the model of [Maynard and Pratt, §8](https://arxiv.org/abs/2206.11729) can be hard to detect by a short polynomial over the primes. In the middle range of spacings, sampling the ordinary approximate functional equation on the putative zeros gives a different detector. Its coefficients are all one, and its location is fixed to within a subpower factor by the spacing. A long plateau also forces the summation interval to be short.

Fix \(1/2<\sigma<1\), \(1/3<a<1/2\), and \(2a\sigma>1/2\). Let \(T\to\infty\), \(t\in[T,2T]\), \(N=T^{a+o(1)}\), \(d=2\pi/\log N\), and \(H\to\infty\) with \(H\le T^{1/10}\). Suppose
\[
 \zeta(\sigma+i(t+jd))=0 \qquad (j\in\mathbb Z,\ |jd|\le H).
 \tag{1}
\]
Then there is an interval \(I\) of integers \(n=T^{a+o(1)}\) satisfying
\[
 \left|\sum_{n\in I}n^{-it}\right|\ge T^{a\sigma-o(1)} . \tag{2}
\]
If \(H=T^{\eta+o(1)}\) with \(\eta>0\), then \(|I|\le T^{a-\eta+o(1)}\). All subpower factors can be taken uniformly when the lower bound on \(H\) tends to infinity uniformly and \(\log N/\log T\to a\) uniformly. In particular, under Lindelöf no such plateaus can have growing length in this range. The standard Lindelöf bound for unweighted dyadic zeta sums is \(N^{1/2}T^{o(1)}\), also for partial intervals. [Tao, Trudgian and Yang, Lemma 34(i)](https://arxiv.org/abs/2501.16779)

## Extracting the arithmetic sum

Put \(M=\lfloor\sqrt{t/(2\pi)}\rfloor\). For \(u=jd\), \(|u|\le H\), the ordinary balanced approximate functional equation and Stirling give
\[
 \zeta(\sigma+i(t+u))=
 \sum_{n\le M} n^{-\sigma-i(t+u)}
 + \chi(\sigma+it)e^{-iu\log(t/(2\pi))}
       \sum_{n\le M}n^{\sigma-1+i(t+u)}
 +O_\sigma(T^{-\sigma/2}+H^2T^{-(1+\sigma)/2}).
 \tag{3}
\]
Here \(\zeta(s)=\chi(s)\zeta(1-s)\). Moving the truncation back to \(M\) changes at most a bounded number of terms of size \(O(T^{-\sigma/2})\). The change in the gamma factor after its displayed linear phase is \(O(T^{1/2-\sigma}(H+1)^2/T)\), and the absolute size of the dual sum before that factor is \(O(T^{\sigma/2})\). [Ivić, *The Riemann Zeta-Function*, Theorem 4.1](https://books.google.com/books?vid=ISBN9780486428130)

Choose \(r=\lceil 20\log T\rceil\) and \(L=\lfloor H/(rd)\rfloor\); ultimately \(L\asymp H\). Average (3) with \(j\) the sum of \(r\) independent uniform integers on \([-L,L]\). This distribution is supported on the available indices. Its characteristic function in cycles is
\[
 B(v)=\left(\frac{1}{2L+1}\sum_{\ell=-L}^L e^{2\pi i\ell v}\right)^r.
\]
It has \(B(0)=1\), \(|B|\le1\), \(|B'|\le 2\pi rL\). For \(\|v\|\ge 1/L\) the geometric sum and \(|\sin(\pi v)|\ge 2\|v\|\) give \(|B(v)|\le 4^{-r}\). Here \(\|v\|\) is distance to the nearest integer. This finite filter works for any growing \(H\), including very slowly growing lengths.

Write \(D=\lceil N^{1/L}\rceil=T^{o(1)}\). Before averaging, multiply (3) by \(\sum_{b\le D}\mu(b)b^{-\sigma-i(t+u)}\). The error in (3) remains \(o(1)\) after this multiplication. The direct coefficients for products \(q=bn\le D\) are exactly zero except at \(q=1\), where the coefficient is one. All terms of the direct sum for which \(\|(\log q)/(\log N)\|\ge1/L\) have total contribution \(o(1)\) by the preceding estimate and a trivial absolute sum. Since \(q\le DM=T^{1/2+o(1)}\) and \(2a>1/2\), the only remaining direct range is
\[
  N^{1-1/L}\le bn\le N^{1+1/L}. \tag{4}
\]

The dual frequency is \(\log(n/(b t/(2\pi)))/\log N\). Its surviving terms have \(n=(bt/(2\pi))N^{-k}\exp(O(\log N/L))\). Exactly one integer \(k\) can contribute: \(k\le1\) gives \(n>M\) and \(k\ge3\) gives \(n<1\), for sufficiently large \(T\). For \(k=2\), \(n=T^{1-2a+o(1)}\); summing absolute values over \(b\le D\) and these \(n\) gives \(O(T^{1/2-2a\sigma+o(1)})=o(1)\), including the gamma factor. Thus the contribution from (4) has modulus at least \(1-o(1)\).

For each fixed \(b\), the factor \(B(\log(bn)/\log N)\) has variation \(O(r)\) on (4), since its argument ranges over an interval of length \(2/L\). Partial summation, including the factor \(n^{-\sigma}\), and summation over \(b\le D\) yield (2) with \(I\) contained in (4) divided by some \(b\le D\). When \(H=T^{\eta+o(1)}\), the logarithmic width in (4) is \(O((\log T)/H)\), giving the short-interval assertion.

## Counting actual zeta zeros in these configurations

The following counts include all zeros in the middle halves of qualifying plateaus. Each plateau is an interval \([t_0-2H,t_0+2H]\) with a grid of zeros of real part \(\sigma\) at step \(d\), as in (1) with width \(2H\). The mesh can vary between plateaus. Every point in its middle half is within \(O(1/\log T)\) of a grid point around which (1) applies with width \(H-O(1/\log T)\). Select a maximal one-separated set \(W\) of such grid centers in the union, extending the middle halves by one step when necessary. Its fixed-size neighborhoods cover the middle halves, which therefore contain \(O((|W|+1)\log T)\) zeros by Riemann–von Mangoldt. Counting the centers suffices.

For each fixed positive integer \(k\), the discrete mean-value theorem at one-separated heights, followed by a maximal interval decomposition, bounds \(|W|\) by
\[
 T^{\max(1,ka)-2ka(\sigma-1/2)-(k-1)\eta+o(1)}.
 \tag{5}
\]
Use \(\eta=0\) without the power-length assumption. For completeness, first split the potential \(n\) into dyadic scales \(N_0=T^{a+o(1)}\). A partial interval of length at most \(U=T^{a-\eta+o(1)}\) is a union of \(O(\log T)\) dyadic subintervals of lengths at most \(U\). For a block of length \(s\), the \(k\)-fold product polynomial has coefficients bounded by the divisor function \(d_k\), coefficient square-sum at most \(s^kT^{o(1)}\), and length at most \((2N_0)^k\). The discrete mean-value theorem bounds the sum of its squares over \(W\) by \((T+N_0^k)s^kT^{o(1)}\). Sum over \(O(N_0/s)\) blocks at each dyadic length, divide by the threshold \(T^{2ka\sigma-o(1)}\), and absorb logarithms. For \(k=1\) the sum over lengths costs another logarithm. This gives (5).

A further estimate, valid already for \(H\to\infty\) arbitrarily slowly, comes from Guth–Maynard applied to the square of an ordinary dyadic sum. For \(\sigma=3/4\) it gives
\[
 |W|\le T^{\max(6a/5,\,1-6a/5)+o(1)} . \tag{6}
\]
To handle variable partial intervals without a power loss, Perron summation at half-integer endpoints bounds their supremum by a constant times
\[
 1+\int_{-N_0^2}^{N_0^2}
   \frac{\big|\sum_{N_0\le n<2N_0} n^{-i(t+v)}\big|}{1+|v|}\,dv .
\]
One may use real abscissa \(1/\log N_0\) in the finite Perron formula, whose endpoint error is \(O(N_0\log N_0/N_0^2)\). The resulting fixed weights \((n/N_0)^{-1/\log N_0}\) are bounded above and below by constants and can be retained in the polynomial. Summing over \(W\) and pigeonholing finds one common shift and a threshold \(V'\ge N_0^{\sigma-o(1)}\) such that at least \(|W|N_0^{\sigma-o(1)}/V'\) translated one-separated points exceed \(V'\) on that full block. The square has Dirichlet coefficients bounded by \(T^{o(1)}\) and length comparable to \(N_0^2\), up to a bounded number of dyadic pieces. In the notation of the [large-value inequality, equation (16)](https://arxiv.org/abs/2501.16779), the count is at most
\[
 T^{o(1)}\max(N_0^4/V'^4,\ N_0^{36/5}/V'^8,\ T N_0^{24/5}/V'^8).
\]
Each power of \(V'\) decreases sufficiently fast to absorb the pigeonholing cost using just \(V'\ge N_0^{\sigma-o(1)}\). Substitution of \(\sigma=3/4\) gives (6). [Guth and Maynard, Theorem 1.1](https://arxiv.org/abs/2405.20552)

For instance, at \(a=2/5\) the bound (6) is \(T^{13/25+o(1)}\), below the general zero-density exponent \(5/9\). For \(H=T^{\eta+o(1)}\), (5) with \(k=3\) gives \(T^{3/5-2\eta+o(1)}\), reaching the density-hypothesis exponent at \(\eta=1/20\). If \(\eta>a(1-\sigma)\), the size requirement (2) exceeds even the length of \(I\), excluding the progression. At \(a=5/12\), (6) itself reaches the density-hypothesis exponent even for arbitrarily slowly growing duration. These conclusions use exact lattice zeros in the stated middle range. A short irregular cluster or an isolated off-line zero need not furnish the required samples.

## Smoothly changing ordinates and real parts

The detector survives smooth curvature on power-length plateaus. Here is one precise version allowing the local spacing to change by a fixed factor. Fix \(0<\eta\le 1/5\), \(H=T^\eta\), and an interval of indices \(|j|\le J\) with \(J\asymp H\log T\). Let
\[
 t_j=t_*+H\phi(j/J),\qquad
 \beta_j=b(j/J),\qquad \zeta(\beta_j+it_j)=0 ,
 \tag{7}
\]
where \(t_j\in[T,2T]\), \(1/2<\sigma\le b\le1\), and \(0<c\le\phi'\le C\). All derivatives of each fixed order of \(b,\phi\) are bounded independently of the plateau and \(T\). The functions can depend on \(T\). The local reciprocal spacing has exponent
\[
 a(v)=\frac{2\pi J}{H\phi'(v)\log T}.
\]
Require its range to stay in a fixed compact subset of \(\{1/3<a<1/2,\ 2a\sigma>1/2\}\). Arbitrarily many overlapping qualifying plateaus are allowed.

For \(\sigma=3/4\), the number of zeta zeros with ordinates in the union of the middle portions \(\{t_*+H\phi(v):|v|\le1/2\}\) is at most
\[
 T^{\max(5/9-4\eta/9,\ (6/11)(1-\eta/2))+o(1)} . \tag{8}
\]
This is strictly below the general exponent \(5/9\) at each fixed \(\eta>0\). At \(\eta\ge1/6\) it gives the density-hypothesis exponent or better. For exact, constant mesh and fixed real part, the corresponding bound replaces \(\eta/2\) by \(\eta\) throughout the optimization below. In particular \(H\ge T^{1/12}\) suffices uniformly over the compact middle range in that case.

**Local proof.** Put \(h=H^{1/2}\). At an interior index \(j_c\) take a window of \(J'=hJ/(H\phi'(j_c/J))\asymp h\log T\) indices on each side. Let \(v=(j-j_c)/J'\), \(t_c=t_{j_c}\), and write \(t_j=t_c+h\phi_c(v)\). On \(|v|\le1\) one has \(\phi_c'(v)=1+O(h/H)\) and all derivatives of orders at least two are \(O_r(h/H)\). The local mesh parameter is \(\log N_c=2\pi J'/h=a(j_c/J)\log T\). Freeze the approximate-functional-equation cutoff at \(\lfloor\sqrt{t_c/(2\pi)}\rfloor\) as in (3). In the dual use Stirling in the form
\[
 \chi(b_j+it_j)=(t_c/(2\pi))^{1/2-b_j} e^{i\theta_c}
  e^{-i(t_j-t_c)\log(t_c/(2\pi))}\{1+O((1+h)^2/T)\},
\]
where \(b_j=b(j/J)\) and the constant phase is independent of \(j\) and \(b_j\). The total error is \(o(1)\), since \(h\le T^{1/10}\). Average over \(j\) with a fixed nonnegative smooth bump \(w(v)\) supported on \((-1,1)\), of integral one, and divide by \(J'\).

Poisson summation in \(j-j_c\) gives phases \(h(\ell v\log N_c-\phi_c(v)\log n)\) on the direct side. Outside
\[
 |\log n-\ell\log N_c|\le C(h/H)\log T+T^\epsilon/h \tag{9}
\]
the phase derivative divided by \(h\) has magnitude comparable to \(D=|\log n-\ell\log N_c|\). Choose \(C\) larger than twice the derivative-drift constant. All higher derivatives of the phase divided by \(h\) are \(O_r(D)\). All fixed derivatives of its amplitude \(w(v)n^{-b((j_c+J'v)/J)}\) are \(O_r(n^{-\sigma}(1+\log T)^r)\). Repeated integration by parts bounds the transformed term by \(O_r(n^{-\sigma}(1+\log T)^r(hD)^{-r})\). The distant \(\ell\) tail is summable. For fixed \(\epsilon>0\), choosing \(r\) sufficiently large makes the total discarded contribution \(o(1)\). The \(\ell=0\) mode retains just \(n=1\) if \(\epsilon<\eta/2\). All other direct terms retained are in (9) with \(\ell=1\). The dual calculation replaces \(\log n\) by \(\log[t_c/(2\pi n)]\); its amplitude and derivatives are bounded by \(T^{1/2-\sigma}n^{\sigma-1}(1+\log T)^{O_r(1)}\). Only \(\ell=2\) can then remain, and its absolute sum is \(O(T^{1/2-2a(j_c/J)\sigma+o(1)})=o(1)\) uniformly by the compact-range hypothesis.

Equivalently, discard the entire original averages for integers outside the surviving ranges, bounding each by the Poisson calculation. The resulting sum over the integers in the direct range (9) must cancel the constant \(1+o(1)\). Its absolute value is bounded above by the average, over \(j\) in the window, of partial unweighted zeta sums at \(t_j\) times \(T^{-a(j_c/J)\sigma+o(1)}\), by partial summation with \(n^{-b_j}\). Thus the mean of their maximal moduli is at least \(T^{a(j_c/J)\sigma-o(1)}\). Their summation intervals have length \(T^{a(j_c/J)-\eta/2+O(\epsilon)+o(1)}\).

Choose local windows around grid points throughout the middle portions. A disjoint selection in height covers all middle ordinates after a bounded dilation, since the derivative of the spacing is bounded and each original window has length comparable to \(h\). Each selected window has \(\asymp h\log T\) sample points; its dilate contains \(O(h\log T)\) total zeta zeros. The union of the undilated samples can be partitioned into \(O(\log T)\) one-separated sets, using the lower bound on adjacent spacing and disjointness of the windows. Group windows by the dyadic scale of \(N_c\). Jensen's inequality on each window now permits the proof of (5) with the short length saving \(\eta/2-O(\epsilon)\). For (6), sum the mean-modulus lower bounds and use the same first-moment Perron argument. Its cost linear in the larger threshold is absorbed by the large-value inequality. Send \(\epsilon\) to zero.

Finally set \(u=\eta/2\). At any given local exponent \(a\), (5) with \(k=2,3\) and (6) give the least of \(1-a-u,\ 3a/2-2u,\ \max(6a/5,1-6a/5)\). For \(a\le5/12\), the increasing line \(3a/2-2u\) intersects the decreasing line \(1-6a/5\) at height \(5/9-8u/9\). For \(a\ge5/12\), the increasing line \(6a/5\) intersects the decreasing line \(1-a-u\) at height \(6(1-u)/11\). The smaller line in each comparison never exceeds the intersection height. This proves (8), also when a crossing lies outside a particular compact range. In the exact case the same optimization uses \(u=\eta\).

This extension permits power-length smooth drifts. Stationary-phase leakage from arbitrary nonsmooth microscopic jitter is a separate obstacle. For example, fixed-size errors on the scale of one zero spacing cannot be inserted in (7) without controlling their derivatives or their Fourier content.
