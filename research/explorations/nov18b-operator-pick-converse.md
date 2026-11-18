# Detecting a displaced zeta zero using only large positive real nodes

**Proposed theorem.** There is an absolute constant \(C\) with the following property. If \(\rho=1/2+d+i\gamma\) is a zeta zero with \(d>0\) and \(\gamma\ge10\), choose any distinct real numbers \(a_1,\dots,a_k\in[\gamma,2\gamma]\). Whenever
\[
 k\ \ge\ C\frac{\gamma}{d}\log(2+\gamma)\log(2/d), \tag{1}
\]
the matrix
\[
 \left[\frac{F(a_j)+F(a_l)}{a_j+a_l}\right]_{j,l=1}^k,\qquad
 F(z)=\frac{\xi'}{\xi}(1/2+z),
\]
has a strictly negative eigenvalue. The nodes are all on the real axis where the defining prime Dirichlet series is absolutely convergent. The bound is uniform in other zeros, including multiplicity and arbitrarily close neighbors. The constant is not optimized or evaluated.

Combined with the [unconditional lower bound on the first failing order](nov18b-operator-moving-bands.md), this identifies a target at the same height up to logarithmic and displacement factors. In particular a real-node programme need test only one suitably large packet of its choice in each required interval. The estimate concerns mathematical definiteness and makes no numerical conditioning guarantee.

## A lower bound on a circle about the zero

There exists \(r\in[d/8,d/4]\) such that on \(|s-\rho|=r\),
\[
 |\zeta(s)|\ge\exp[-C_1\log(2+\gamma)\log(2/d)]. \tag{2}
\]
Here and below the constants are absolute. On the fixed-radius disk \(|s-(2+i\gamma)|\le4\), \(\zeta\) is holomorphic and bounded by \((2+\gamma)^{C_2}\). This polynomial bound on the fixed strip follows, for example, from Euler–Maclaurin continuation with four Bernoulli terms. The Euler product gives \(|\zeta(2+i\gamma)|\ge1/\zeta(2)\). Jensen's formula therefore bounds the number of zeros in the disk of radius \(7/2\) by \(C_3\log(2+\gamma)\). Choose a radius \(b\in[3,7/2]\) avoiding zeros and divide out the disk Blaschke factors of its zeros. For the resulting zero-free \(h\), the disk-boundary maximum is still at most \(M=(2+\gamma)^{C_2}\), and \(|h(2+i\gamma)|\ge1/\zeta(2)\). The Harnack inequality applied to \(\log(M/|h|)\) bounds \(|h|\) from below by \((2+\gamma)^{-C_4}\) on the concentric disk of radius two, which contains the circles under consideration.

For a removed zero \(s_j\) the modulus of its disk factor on the smaller disk is at least \(|s-s_j|/6\). At fixed radius \(r\), this is at least \(|r-|s_j-\rho||/6\). On any interval of length \(L\le1\) the average of \(\log^+(1/|r-a|)\) is at most \(1+\log(2/L)\), by centering that interval at \(a\). Sum this estimate over the at most \(C_3\log(2+\gamma)\) factors on the radius interval \([d/8,d/4]\). At one radius the sum is no greater than its average. Combining the factors with the lower bound for \(h\) gives (2), with no zero on the selected circle.

## What positivity on a real packet would imply

Suppose the matrix is positive semidefinite. Half-plane Nevanlinna–Pick interpolation gives a holomorphic \(G\) on \(\Re z>0\) with \(\Re G\ge0\) and \(G(a_j)=F(a_j)\). This is the usual Schur-class theorem after the Cayley transforms of both half-planes. At \(a=a_1\), \(0<F(a)\ll\log(2+a)\): the strict positivity follows by pairing the Hadamard log derivative over the strip (equivalently \(F(a)=\sum_\lambda \Re(a-\lambda)^{-1}\) at real \(a>1/2\)); the upper estimate follows from the digamma term and absolutely convergent prime series. By Schwarz–Pick,
\[
 |G(z)|\le F(a)\frac{|z+a|^2}{a\Re z}. \tag{3}
\]

Let \(s=1/2+z\) and define
\[
 g(s)=\frac1s+\frac1{s-1}-\tfrac12\log\pi+\tfrac12\psi(s/2),\quad
 D(z)=\frac{(s-1)^2}{(z+3)^7}\big[\zeta'(s)+(g(s)-G(z))\zeta(s)\big].
\]
The double polar factor at \(s=1\) is removed. On the half-plane \(\Re z>d/4=h_0\), the function \(D\) is holomorphic and bounded by \(C_5(2+a)^3/d\). For example the identity \(\zeta(s)=s/(s-1)-s\int_1^\infty\{x\}x^{-s-1}\,dx\) and its derivative give uniform polynomial bounds for \((s-1)\zeta\) and \((s-1)^2\zeta'\) there. The digamma term is \(O(\log(2+|s|))\) on \(\Re s\ge1/2\), and (3) bounds the remaining term.

Each \(a_j\) is a zero of \(D\). Dividing by their finite half-plane Blaschke product preserves this bound, so
\[
 |D(z)|\le \frac{C_5(2+a)^3}{d}
    \prod_{j=1}^k\left|\frac{z-a_j}{z+a_j-2h_0}\right|. \tag{4}
\]
On the circle from (2), written in the centered variable, \(\Re z-h_0\ge d/2\) and \(|\Im z-\gamma|\le d/4\). Each factor's squared modulus equals \(1-4(\Re z-h_0)(a_j-h_0)/|z+a_j-2h_0|^2\), hence is at most \(1-c d/\gamma\) for an absolute \(c>0\). Using (2) in (4) now gives on the whole circle
\[
 |F(z)-G(z)|\le d^{-1}\exp\{C_6\log(2+\gamma)\log(2/d)-c_1 kd/\gamma\}. \tag{5}
\]
With the absolute constant in (1) sufficiently large, the right side is below \(1/d\). The normalized contour integral of \(F-G\) has modulus at most \(r/d\le1/4\). It also equals the positive integer counting all zeros inside, since \(G\) is holomorphic and the center itself is a zero. This contradiction proves the theorem.

For very uneven node sets (4) retains the exact product and can be used directly. The same argument applies to a confluent positive-real interpolation problem at \(a\in[\gamma,2\gamma]\), using its order-\(k\) Carathéodory–Fejér criterion in place of the distinct-node theorem. The missing arithmetic estimate is positivity at the scale of (1). The proof supplies an obstruction when a specified zero exists.
