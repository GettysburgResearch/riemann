# Signed prime translations on two families of arithmetic wave packets

**Proposed unconditional estimate.** Fix a large real number \(q\), put \(T=2\pi q\), and use the Weil normalization \(\widehat g(t)=\int g(u)e^{itu}du\). There is an explicit space of dimension \(2(\lfloor\sqrt q/4\rfloor-1)\) in \(C_c^\infty(0,\log q)\) on which
\[
 |P(g)|\ll (1+\log\log q)\|g\|_2^2,\qquad
 G(g)=(\log q+O(1))\|g\|_2^2,\qquad
 |Z(g)|\ll_A q^{-A}\|g\|_2^2.
\]
Here \(W=G-P+Z\) is the actual Weil form, with the full sum over prime powers and the two pole evaluations. All constants are independent of real \(q\) and of the coefficient vector. Thus \(W(g)\ge(\log q-O(1+\log\log q))\|g\|_2^2\). Translating the log interval gives radius \(\tfrac12\log(T/(2\pi))\). There is no exceptional set of carriers and no imported critical-line zero count. The estimates use the ordinary primes. The space here differs from a consecutive block of Mellin Fourier modes.

## The packets

Write \(x=e^u\), \(g(u)=x^{1/2}f(x)\) for \(x>0\), extending \(f\) evenly to \(\mathbb R\). All positive-line norms below equal half the corresponding full squared norms. The prime term is exactly
\[
 P(g)=2\Re\sum_{d\ge2}\Lambda(d)\int_0^\infty f(dx)\overline{f(x)}\,dx.
\]
The factor \(d^{-1/2}\) in the logarithmic prime translation cancels the change in the square root. Let \(\mathcal F f(y)=\int_{\mathbb R} f(x)e^{-2\pi ixy}\,dx\). For every even Schwartz input, Plancherel and a dilation show that the Hermitian prime form is invariant under \(f\mapsto\overline{\mathcal F f}\) provided the sum converges. In the proof all inputs and their Fourier transforms vanish at zero.

Take a real even nonnegative smooth probability bump supported in \((-1/10,1/10)\). Its convolution \(\phi\) with the indicator of \([-1/2,1/2]\) equals one on \([-2/5,2/5]\), is supported in \([-3/5,3/5]\), and has \(\widehat\phi(k)=0\) at every nonzero integer with the additive Fourier convention above. For \(2\le n\le N=\lfloor\sqrt q/4\rfloor\), let \(k_n\) be a nearest integer to \(q/n\). Define on \(x>0\)
\[
 f_n(x)=\phi(x-n)e^{2\pi i k_n(x-n)},\qquad F_n=\overline{\mathcal F f_n},
\]
where the Fourier transform uses the even extension. The positive-line integral of \(f_n\) is zero by the integer zero of \(\widehat\phi\). Thus \(F_n(0)=0\). Fourier inversion gives \(\int F_n=0\) as well. On the whole real line,
\[
 F_m(y)=e^{2\pi i m y}\widehat\phi(y-k_m)+e^{-2\pi i m y}\widehat\phi(y+k_m).
\]
The second term is rapidly decreasing on the positive line, with an arbitrarily large saving in \(q\). Near zero the two terms together vanish to second order by evenness. The intervals supporting the \(f_n\) have bounded overlap and each has an exclusive central interval of length \(4/5\). Their Gram matrix has fixed positive lower and upper bounds. The \(F_m\) have the same property by unitarity. Since \(k_m\ge 4\sqrt q-1\) and the \(f_n\) live below \(\sqrt q/4+1\), the cross Gram matrix has norm \(O_A(q^{-A})\), by Schwartz decay even after summing all entries. It follows that
\[
 \Big\|\sum a_n f_n+b_n F_n\Big\|_{L^2(0,\infty)}^2\asymp \sum(|a_n|^2+|b_n|^2).
 \tag{1}
\]

## Prime interactions within one family

For \(m,n\) as above, substitute \(y=dx-m\) into \(\int f_m(dx)\overline{f_n(x)}dx\). The two bump supports force \(m\asymp dn\). Integrating by parts in \(y\) uses frequency \(k_m-k_n/d\), and the other bump has derivatives bounded uniformly since \(d\ge2\). The rounding errors total at most one. Hence, for each fixed \(j\),
\[
 \left|\int f_m(dx)\overline{f_n(x)}dx\right|
 \ll_j d^{-1}\mathbf 1_{m\asymp dn}
       (1+q|m-dn|/m^2)^{-j}.
 \tag{2}
\]
In particular \(q/m^2\ge 16\). Group the indices into dyadic blocks \(m\asymp M, n\asymp B\), taking a block to mean \([M,2M)\) or its intersection with the index set. Only \(d\asymp D=M/B\) enter. At fixed \(n\) the sum of (2) over \(m\) and \(d\), with weight \(\Lambda(d)\), is \(O(1)\) by \(\sum_{d\asymp D}\Lambda(d)/d\ll1\). This dyadic estimate is Chebyshev's elementary bound. At fixed \(m\) the sum is likewise \(O(1)\) by first summing in \(n\). It also has the stronger bound \(O(\log(2q)/D)\): put \(h=dn\), bound \(1/d\ll1/D\), and use \(\sum_{d\mid h}\Lambda(d)=\log h\) before summing the decaying function of \(h-m\). Thus the operator norm of this rectangular block, even after taking entrywise absolute values, is
\[
 \ll \min(1,\sqrt{\log(2q)/D}).
 \tag{3}
\]
The same bound applies on the Fourier side by additive Plancherel, which exchanges the two orientations of each dilation. Only constants are lost when a bounded number of neighboring dyadic indices are interchanged.

## The cross term and the hyperbola

Consider \(\int F_m(dx)\overline{f_n(x)}dx\). For the main Fourier packet substitute \(y=dx-k_m\). The integral has absolute value
\[
 d^{-1}\left|\int \widehat\phi(y)\phi((k_m+y)/d-n)
                         e^{2\pi i (m-k_n/d)y}\,dy\right|.
\]
For \(d\asymp q/(mn)\) this is bounded by
\[
 C_j d^{-1}\big(1+\max(n,m)|1-q/(dmn)|\big)^{-j}.
 \tag{4}
\]
Indeed the spatial mismatch \(|k_m/d-n|\) gives decay by the Schwartz envelope and compact support of the second bump, and the mismatch \(|m-k_n/d|\) gives decay by integration by parts. Any fixed number of derivatives of the integrand retain the spatial decay. Both mismatches differ by at most one from the corresponding unrounded values. Outside the comparable range, if \(dx\) is less than \(k_m/2\) on the bump, or greater than \(2k_m\), the integral is \(O_A((k_m+dn)^{-A})\) directly. Choosing sufficiently wide absolute comparability constants ensures one of these alternatives for the omitted \(d\). Since \(k_m\gg\sqrt q\), the total omitted operator is \(O_A(q^{-A})\) after summing \(d,m,n\). The reflected packet at \(-k_m\) obeys this bound for every \(d\).

For the other orientation \(\int f_n(dx)\overline{F_m(x)}dx\), one has \(x\le(N+1)/d\). All derivatives of fixed order of \(F_m\) on this region are \(O_A(q^{-A})\). Evenness and its zero at the origin give \(|F_m(x)|\ll_A q^{-A}\min(1,x^2)\) there. The bound is summable in \(d\) after the change of variables, and the whole orientation is \(O_A(q^{-A})\).

In a block \(m\asymp M,n\asymp B\) now put \(D=q/(MB)\). Suppose \(M\ge B\). Since (4) concentrates \(m\) within \(O(1)\) of \(q/(dn)\), the row sum at fixed \(n\) is \(O(1)\) by the same dyadic Chebyshev estimate. The column sum at fixed \(m\) is \(O(1)\) as well. To improve the latter estimate for separated blocks group by the integer \(h=dn\asymp DB\). The weight in (4) is at most \(C_j(1+|h-q/m|/(DB/M))^{-j}\). The divisor identity therefore bounds the column by
\[
 \frac{C\log(2q)}{D}\big(1+ DB/M\big)
       \ll \log(2q)\,B/M,
\]
using \(M^2\le q\). Exchanging \(m,n\) in the majorant covers \(B\ge M\). The rectangular block norm is
\[
 \ll \min\left(1,\sqrt{\log(2q)\min(M,B)/\max(M,B)}\right).
 \tag{5}
\]
For fixed dyadic index, summing (3) or (5) over the other index costs \(O(1+\log\log q)\): there are \(O(1+\log\log q)\) near scales and a summable geometric tail. Apply the scalar Schur test to the matrix of block norms. This proves the claimed prime bound on the uncut sum in (1).

## Gamma, poles and compact support

For the low packets, \(\widehat g_n(t)=\int_0^\infty f_n(x)x^{-1/2+it}dx\). Off \(cq\le |t|\le Cq\), with fixed sufficiently small \(c\) and large \(C\), the derivative \(2\pi k_n+t/x\) has magnitude \(\gg(q+|t|)/n\) on the bump. Integration by parts gives \(O_j(n^{-1/2}[n/(q+|t|)]^j)\); successive derivatives of the normalized reciprocal phase and of the amplitude are bounded on these unit intervals. The Fourier side has the same Mellin mass on this symmetric band and its complement, by the Mellin formula for the even additive Fourier transform. Its factor at \(s=1/2+it\) is \(2(2\pi)^{-s}\Gamma(s)\cos(\pi s/2)\), of absolute value one. Thus the total mass outside the band, also weighted by \(1+|\log(2+|t|)|\), is \(O_A(q^{-A})\) per unit squared coefficient norm. On the band Stirling gives \(\Re\psi(1/4+it/2)-\log\pi=\log q+O(1)\). Plancherel and (1) give the assertion about \(G\). Before truncation one pole evaluation vanishes because every input has zero integral, and the other is finite by the zero at the origin.

Finally multiply the positive-line input by a smooth cutoff supported in \((1,q)\) and equal to one on \([5/4,3q/4]\), with fixed-scale derivatives at the left and scaled derivatives at the right. This leaves all low packets intact. For any fixed \(j,A\) and unit coefficient vector, the removed high-packet tail, with its first \(j\) logarithmic derivatives \((x\partial_x)^a\), is bounded by \(C_{j,A}q^{-A}\min(x,x^{-2})\). This follows from the common zero of order at least two at the origin, the bounds \(4\sqrt q-1\le k_m\le q/2+1\), and Schwartz decay. The complete input obeys the same bound with a fixed power of \(q\) in place of \(q^{-A}\) for each fixed \(j\). Both pole integrals then change by \(O_A(q^{-A})\); Plancherel and one derivative bound the gamma loss. For the prime loss integrate \(\min(dx,(dx)^{-2})\min(x,x^{-2})\) in \(x>0\), obtaining \(O(d^{-2}\log(2d))\), summable against \(\Lambda(d)\). These bounds justify compactification and preserve (1).

The remaining modes include the true Mellin phase \(x^{iT}\). Linearizing its phase on a unit interval at \(n\) leaves a quadratic phase variation of order \(q/n^2\). Near \(n\asymp\sqrt q\) this has bounded size. Farther down the interval it grows without bound. The packet estimate exploits the resulting additive-frequency separation for nondivisible prime shifts in (2). Restoring the full Mellin curvature can remove that separation. The present proof gives no lower bound for this missing sector, or for its coupling to the displayed subspace. The [previous centred Fourier estimate](weil-prime-average-nov18.md) uses a different space and averages over carriers.
