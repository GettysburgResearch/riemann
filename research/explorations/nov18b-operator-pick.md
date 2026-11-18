# Uniform positivity of the actual xi Pick form through order 100,000

**Proposed theorem for review.** Write \(H=3{,}000{,}175{,}332{,}800\), the published Platt–Trudgian height, and
\[
 X(z)=\xi(1/2+z),\qquad F(z)=X'(z)/X(z),\qquad
 K(z,w)=\frac{F(z)+\overline{F(w)}}{z+\bar w}.
\]
For every \(1\le k\le 100{,}000\) and every set of distinct complex nodes \(z_1,\ldots,z_k\) satisfying \(\Re z_j>0\) and \(|\Im z_j|\le H/2\), the matrix \((K(z_j,z_l))\) is positive definite. There is no upper bound on the real parts, minimum node separation or lower bound on the positive real parts. The proof also allows a rational test with repeated poles of total multiplicity at most \(k\).

This addresses the actual polarized form in the [finite Pick programme](../integrated/xi/finite-pick-controls.md) and includes the unrestricted positive real nodes in the [infinitesimal safe-node problem](../integrated/xi_pick/ORDER_THREE_CANONICAL.md). Its inputs are the published verification through \(H\) and an unconditional Riemann–von Mangoldt error estimate. Every unverified dyadic band has a positive *total* contribution on the specified rational tests. Its zeros may lie anywhere in the critical strip. [Platt and Trudgian, Theorem 1](https://doi.org/10.1112/blms.12460) · [Brent, Platt and Trudgian, footnote 1 and equation (4)](https://arxiv.org/abs/2009.13791)

## 1. The signed resolvent form

Put \(\lambda=\rho-1/2\), with multiplicity. The symmetric Hadamard product of the even entire function \(X\), which is nonzero at zero, gives the absolutely locally convergent regularized series
\(F(z)=\sum_\lambda((z-\lambda)^{-1}+\lambda^{-1})\). Under reflection \(\lambda\mapsto-\bar\lambda\) the regularizers in the two summands defining \(K\) cancel. Thus
\[
 K(z,w)=\sum_\lambda \frac1{(z-\lambda)(\bar w+\lambda)}.
\]
This last series converges absolutely. The nodes lie off the zero set by the verified height. With \(R(v)=\sum_j c_j/(z_j-v)\), the quadratic form, with coefficients conjugated according to the chosen convention, is
\[
 \sum_\lambda R(\lambda)\overline{R(-\bar\lambda)}. \tag{1}
\]
We prove positivity also for \(R=P/Q\) proper, with poles in the stated domain and denominator degree at most \(k\). Simple partial fractions then give the claimed ordinary matrices. Every zero through height \(H\) contributes \(|R(i\gamma)|^2\).

## 2. A polynomial sampling estimate using all ordinates

For \(T\ge H\) write \(x_\gamma=2\gamma/T-3\) for \(T<\gamma\le2T\), so the real interval is \((-1,1]\). Set
\[
 D=\frac{T}{4\pi}\log\frac{T}{2\pi},\qquad m=4k+80.
\]
For each complex polynomial \(p\) of degree at most \(m\), with the unweighted \(L^2(-1,1)\) norm,
\[
 0.55D\|p\|_2^2 \le \sum_{T<\gamma\le2T}|p(x_\gamma)|^2
       \le 1.5D\|p\|_2^2. \tag{2}
\]
Indeed the zero count is \(N(t)=\frac t{2\pi}\log\frac{t}{2\pi e}+\frac78+E(t)\), with \(|E(t)|\le0.28\log t\) for \(t\ge2\pi e\). The same bound holds for the one-sided counts by taking a one-sided limit. The main integral for (2) lies between \(D\|p\|_2^2\) and \(1.03D\|p\|_2^2\). Stieltjes integration by parts bounds the absolute error by
\[
 .28\log(2T)\bigl(2\|p\|_\infty^2+2\|p\|_2\|p'\|_2\bigr)
 \le .56\log(2T)(m+1)^2\|p\|_2^2.
\]
For the last estimate expand in the orthonormal Legendre polynomials \(e_n=\sqrt{(2n+1)/2}P_n\). The bound \(|P_n|\le1\) gives \(\|p\|_\infty\le(m+1)\|p\|_2/\sqrt2\). Cauchy–Schwarz and \(\int_{-1}^1(P_n')^2=n(n+1)\) give \(\|p'\|_2\le(m+1)^2\|p\|_2/2\), since \(\sum_{n=0}^m\|e_n'\|_2^2=m(m+1)^2(m+2)/4\). Here \((m+1)^2/T<0.054\), and \(\log(2T)/\log(T/(2\pi))<1.10\). Hence the error is less than \(0.419D\|p\|_2^2\), yielding (2). In particular there are at most \(3D\) zeros on this band.

## 3. Rational approximation on one band

Use \(r(x)=R(iT(3+x)/2)\). Every pole \(b\) of this rational function has \(\Re b\le-2\), hence \(|b|\ge2\). The same conclusion holds for \(r(x)=R(-iT(3+x)/2)\) on the negative band. Put \(M=\|r\|_{\infty,[-1,1]}\). On the closed Bernstein ellipse \(E_2\), with semimajor axis \(5/4\), one has
\[
 |r|\le8^k M. \tag{3}
\]
For the numerator polynomial the usual Bernstein–Walsh inequality costs at most \(2^k\). The ratio between the maximum of each denominator factor on the segment and its value on the ellipse costs at most \((|b|+1)/(|b|-5/4)\le4\). Multiplication proves (3). The polynomial inequality follows as well by the maximum principle after substituting \(x=(w+w^{-1})/2\) on the exterior disk.

Let \(p\) be the degree-\(m\) truncation of the Chebyshev expansion of \(r\). The coefficients past degree zero are bounded by \(2\,8^k 2^{-n}M\) by Cauchy's formula in the same ellipse variable. On \(E_{9/8}\), geometric summation gives
\[
 |r-p|\le e M,\qquad e=\frac{2\,8^k(9/16)^{m+1}}{1-9/16}<10^{-19}.
\]
This ellipse contains every \(x+iy\) with \(-1\le x\le1\), \(|y|\le1/T\), as follows from its semiaxes \(((9/8)\pm(8/9))/2\). The real-segment bound gives \(M\le(m+1)\|p\|_2/(\sqrt2(1-e))\). Consequently throughout that strip
\[
 |r-p|<10^{-8}\|p\|_2. \tag{4}
\]
If \(R\ne0\), then \(M>0\) and \(p\ne0\).

## 4. Paying for every possible displacement off the line

For either sign let \(x_\gamma+i\tau_\gamma\) be the argument corresponding to \(\lambda\) or \(-\bar\lambda\) in the expression for \(r\). Both have \(|\tau_\gamma|\le1/T\) because \(|\Re\lambda|<1/2\). Taylor's formula, the triangle inequality on the entire vector of ordinates, (2) applied to each derivative, and the iterated Legendre derivative bound give
\[
 \Big(\sum_\gamma |p(x_\gamma+i\tau_\gamma)-p(x_\gamma)|^2\Big)^{1/2}
 \le \sqrt{1.5D}\bigl(e^{(m+1)^2/(2T)}-1\bigr)\|p\|_2.
\]
All sums here are over the selected band with multiplicities. By (4) and its count bound, the distance between either displaced \(r\) vector and the undisplaced \(p\) vector is less than \(0.035\sqrt D\|p\|_2\). Their real inner product is at least
\[
 [0.55-2\sqrt{1.5}\,(0.035)-(0.035)^2]D\|p\|_2^2
 >0.46D\|p\|_2^2. \tag{5}
\]
Reflection preserves the band, so the complete sum there is real. Apply (5) to both signs of the ordinates and all dyadic \(T=2^jH\). The absolutely convergent sum (1) is strictly positive for every nonzero test. Distinct simple poles make a nonzero coefficient vector a nonzero rational function. This proves the assertion.

**Remaining scale.** The argument bounds \((4k+81)^2/T\) on the first unverified band and keeps the poles away from that band. An arbitrary-order result at fixed \(H\), or unrestricted complex node height even at order one, requires additional input. The signed high-zero contribution itself was bounded uniformly here without individual high-zero data.
