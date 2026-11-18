# Detecting the rightmost zeta zeros with reflected integer combs

The [one-sided Weil estimate](nov18b-euler-comb.md) is unconditional on the full space on each comb. This note tests the coupling to its reflection with a single smooth coefficient sequence. The high-frequency sampling error admits a power saving independent of any separation of zeta zeros. The remaining term is a signed sum over primes near products of two comparable integers.

Write \(z_\rho=\rho-1/2\) and \(d=\sup_\rho\Re z_\rho\), with multiplicities counted in all zero sums. Fix \(\omega>0\) smaller than the one-sided threshold, \(w=\omega/N\), and a real \(C_c^\infty(0,1)\) function \(k\) of integral one. Take a fixed real \(A\in C_c^\infty(1/2,1)\) such that
\[
 B(z)=\int A(v)v^z\,dv
\]
has no zeros on \(|\Re z|<1/2\) and double zeros at \(z=\pm1/2\). Here is one construction. In the logarithmic variable convolve symmetric uniform probability measures of half-widths \(2^{-j-6}\) for \(j\ge1\), and translate the result inside \((\log(1/2),0)\). Its bilateral Laplace transform is a nonvanishing exponential times \(\prod_j\sinh(2^{-j-6}z)/(2^{-j-6}z)\). The tail converges locally uniformly to a nonzero limit away from the displayed zeros, since the widths are square summable. On bounded vertical strips any fixed number of factors give the corresponding polynomial decay in the ordinate. Thus the density is smooth. Tilt it by \(e^u\), moving all zeros to \(\Re z=-1\), and apply \((\partial_u^2-1/4)^2\). This gives the smooth compactly supported density \(e^uA(e^u)\) with the claimed transform.

Use the integer comb and its reflection:
\[
 g_N(u)=\frac1{Nw}\sum_n A(n/N)k((u-\log n)/w),\qquad
 \check g_N(u)=g_N(-u),\qquad C_N=W(g_N,\check g_N).
\]
The complex sesquilinear form is the polarization of the [one-sided quadratic form](nov18b-euler-comb.md). Since our functions are real, \(C_N\) is real. We claim
\[
 C_N=\sum_\rho N^{2z_\rho} B(z_\rho)^2+
 O_{\epsilon,A,k,\omega}\big(N^{\min(2d/3,\,6/65)+\epsilon}\big).             \tag{1}
\]
In particular
\[
 \limsup_{N\to\infty}\frac{\log^+|C_N|}{\log N}=2d.                         \tag{2}
\]
This identifies the exact obstruction to combining the two positive one-sided spaces. Indeed \(W(g_N)=W(\check g_N)=O(\log(2N))\). The prime term has this bound by (2) of the one-sided note and \(\mathcal D_N\ll\log(2N)\|g_N\|^2\), using the same divisor and Chebyshev sums. The gamma upper bound follows by Plancherel, \(\|g_N\|=O(1)\), \(\|g_N'\|=O(N)\), and \(\log(2+|t|)\le \log(2N)+O(1+t^2/N^2)\). The pole bound follows directly from support inside a fixed-width neighborhood of \(\log N\). Thus if RH fails, infinitely many \(N\) give a negative Weil direction among the two real vectors \(g_N+\check g_N\) and \(g_N-\check g_N\).

## Spectral calculation

For \(K(s)=\int k(y)e^{sy}dy\), set \(B_N(z)=N^{-1}\sum_n A(n/N)(n/N)^z\). The bilateral Laplace transform of \(g_N\) is \(N^zK(wz)B_N(z)\). Reflection and reality therefore give the exact zero sum \(C_N=\sum_\rho N^{2z_\rho}K(wz_\rho)^2B_N(z_\rho)^2\) by the Weil explicit formula. Every sum converges absolutely for fixed \(N\).

For \(|\Re z|\le1/2\) and \(|\Im z|\le cN\), with \(c>0\) sufficiently small, Poisson summation gives \(B_N(z)=B(z)+O_j(N^{-j})\) for any fixed \(j\). For a nonzero dual integer \(h\), the phase in the integral is \((\Im z)\log v-2\pi hNv\). Its first derivative is bounded away from zero by \(\gg |h|N\) on the support, and every fixed higher derivative is \(O_j(N)\). Repeated integration by parts gives a summable \(O_j((|h|N)^{-j})\). In this range \(K(wz)=1+O((1+|\Im z|)/N)\). Rapid decay of \(B\) and the unit-interval zero count \(O(\log(2+|\Im z|))\) bound the resulting total multiplier error by \(O(N^{2d-1})\).

For \(cN\le |t|\le N^{1+\nu}\), the second derivative test for \(t\log(n/N)\), with partial summation of the smooth amplitude, gives
\[
 |B_N(\sigma+it)|\ll \sqrt{|t|}/N+1/\sqrt{|t|}\ll N^{-1/2+\nu/2}
 \qquad(|\sigma|\le1/2).
\]
The zeros on the left of the critical line therefore cost \(O(N^{O(\nu)}\log N)\) in this band. For the right-hand zeros, write \(a=\Re z_\rho\in[0,d]\). By Ingham's estimate and Guth–Maynard (1.4) a real-part bin at \(a\) has at most \(N^{D(a)+O(\nu)+\epsilon}\) zeros, where
\[
 D(a)=\min\{1,\,3(1/2-a)/(3/2-a),\,(30/13)(1/2-a)\}.
\]
Here bins of width smaller than \(\epsilon\) suffice, with endpoints fixed independently of \(N\). Their implied constants may depend on that partition. The exponent spent by each bin is at most \(2a-1+D(a)+O(\nu+\epsilon)\). Ingham's bound gives \(2a(1/2-a)/(3/2-a)\le 2a/3\). This expression increases up to \(a=1/5\), where it is \(6/65\); on \(a\ge1/5\), using the Guth–Maynard bound gives the decreasing expression \((2-4a)/13\). These are upper bounds on the entire bin sum. For \(|t|>N^{1+\nu}\) the arbitrary-order decay of \(K(wz)\), the trivial bound on \(B_N\), and the zero count make the total \(O_j(N^{-j})\) on choosing sufficiently many integrations by parts depending on \(\nu,j\). The same holds for the tail of \(B(z)^2\). Taking \(\nu\) sufficiently small in terms of the desired \(\epsilon\) proves (1). [Ingham's density bound and modern explicit versions](https://arxiv.org/abs/2507.15184) · [Guth and Maynard, equation (1.4)](https://arxiv.org/abs/2405.20552)

For (2), put \(S(y)=\sum_\rho e^{y z_\rho} B(z_\rho)^2\). It is \(O(e^{dy})\) for \(y\ge0\) and its derivative has the same bound. Its Laplace transform equals \(\sum_\rho B(z_\rho)^2/(s-z_\rho)\) for \(\Re s>d\). This last series is meromorphic throughout the plane by rapid decay and the zero count. Every distinct zero supplies a pole, since its residue is its multiplicity times \(B(z_\rho)^2\ne0\). Hence for \(d>0\) and any fixed \(0<a<d\), \(S(y)\) is not \(O(e^{ay})\). Every large \(y\) is within \(O(1/N)\) of some \(2\log N\), costing \(O(N^{2d-1})\) by the derivative bound. As \(\min(2d/3,6/65)<2d\) when \(d>0\), (1) yields (2). For \(d=0\) the upper bound and the definition of \(\log^+\) suffice.

## The arithmetic term left by reflection

For all large \(N\), the off-diagonal gamma term is \(O(1/N)\). The two supports have log-distance \(2\log N+O(1)\) and bounded \(L^1\) norms, so this follows from the exponentially decaying kernel in the [one-sided proof](nov18b-euler-comb.md). Both pole products are \(O_j(N^{-j})\), by Poisson summation for \(B_N(\pm1/2)\) and the zero moments. In the prime term only the orientation that goes from \(-\log m\) to \(\log n\) can contribute. With \(J=k*k\) the resulting expression is
\[
 C_N=-\frac1{N^2w}\sum_{m,n}A(m/N)A(n/N)
       \sum_r\frac{\Lambda(r)}{\sqrt r}\,
       J\!\left(\frac{\log(r/(mn))}{w}\right)+O(1/N).                      \tag{3}
\]
Thus (1)–(2) concern a single fixed threshold on an explicitly signed sum over prime powers \(r\asymp N^2\), with \(|r-mn|\ll N\) and \(m,n\asymp N\). Small variation of the leading Mellin signal or large individual entries of the matrix in (3) do not settle its sign or its norm.
