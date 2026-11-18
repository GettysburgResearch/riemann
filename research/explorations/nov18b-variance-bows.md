# Horizontal displacement in long clusters of zeta zeros

**Proposed unconditional estimate.** Maynard and Pratt describe a possible obstruction to short prime-polynomial zero detectors. The ordinates in their example follow an arithmetic progression with step comparable to the mean spacing, while their real parts rise from the critical line to a plateau and fall back. Inside a densely occupied plateau, the local geometric mean of the actual zeta function is large. The fourth moment gives the density-hypothesis exponent for plateaus that fill the local zero count. This argument uses no vertical-line rigidity hypothesis and allows extra zeros. It gives weaker bounds on thinner plateaus and no bound excluding a single off-line zero. [Maynard and Pratt, §8](https://arxiv.org/abs/2206.11729)

Let \(T\to\infty\), and let \(h=h(T)\to\infty\) with \(h\le T\). Write
\[
 D(I)=\sum_{\gamma\in I,\ \beta>1/2}(\beta-1/2)
\]
for the total rightward displacement of the nontrivial zeros \(\rho=\beta+i\gamma\), counted with multiplicity. For fixed \(\lambda>0\), take *all* intervals \(I\subset[T,2T]\) of length \(|I|\ge h\) satisfying
\[
 2\pi D(I)\ge\lambda |I|\log T .
 \tag{1}
\]
The number of zeros whose ordinates lie in the union of these intervals is
\[
 \ll T^{\min(1-4\lambda,\ 2-12\lambda)+o(1)}. \tag{2}
\]
All implied constants can depend on \(\lambda\). A negative exponent means the family is empty for sufficiently large \(T\). More generally a moment estimate \(\int_{T/2}^{3T}|\zeta(1/2+it)|^kdt\ll T^{M_k+o(1)}\) gives the exponent \(M_k-k\lambda\). A pointwise estimate \(|\zeta(1/2+it)|\ll T^{\theta+o(1)}\) makes the family empty if \(\lambda>\theta\). Bourgain gives \(\theta=13/84\). [Bourgain](https://arxiv.org/abs/1408.5794)

**Proof.** Littlewood's rectangle formula with vertical sides \(1/2\) and 2 gives, uniformly for \(I=[a,b]\subset[T,2T]\),
\[
 \int_a^b\log|\zeta(1/2+it)|\,dt=2\pi D(I)+O(\log T).
 \tag{3}
\]
On the side \(\Re s=2\), termwise integration of the absolutely convergent logarithmic Euler series is \(O(1)\), since the resulting sum is bounded by \(2\sum_{n\ge2}\Lambda(n)/(n^2\log^2 n)\). On the horizontal sides the argument continued from 2 is \(O(\log T)\) uniformly down to \(1/2\) by the standard Jensen–Backlund estimate. One can obtain the bound directly by applying Jensen's inequality in a fixed disk centered at 2 to \((\zeta(z+it)+\zeta(z-it))/2\). Its value at 2 is real and at least \(2-\zeta(2)>0\), its supremum on a fixed larger disk is polynomial in \(T\), and its zeros on the real radius count changes of sign of \(\Re\zeta(x+it)\). Small displacements of horizontal endpoints and the left side handle zeros on the contour by local integrability of the logarithm. Including all zeros at an endpoint changes \(D\) by \(O(\log T)\) from the usual local zero count.

For a disjoint subfamily \(\mathcal I\), Jensen's integral inequality now gives the actual moment bound
\[
 \sum_{I\in\mathcal I}|I|\exp\!\left(\frac{2\pi k D(I)-C k\log T}{|I|}\right)
 \le \int_T^{2T}|\zeta(1/2+it)|^k\,dt .
 \tag{4}
\]
It follows from (1) that \(\sum |I|\ll T^{M_k-k\lambda+O_k(1/h)+o(1)}\). For each zero in the union choose one witnessing interval. There are finitely many zeros. The greedy disjoint selection in order of decreasing length covers all their ordinates by the threefold dilations of the selected intervals. Such a dilation contains \(O((|I|+1)\log T)\) zeros by the unit-interval bound, so the same exponent applies to the number of zeros. Apply Ingham's fourth moment and Heath-Brown's twelfth-moment bound. The supremum assertion follows from (3) alone. [Heath-Brown, *The twelfth power moment of the Riemann-function*](https://doi.org/10.1093/qmath/29.4.443)

**Density at a specified abscissa.** Fix \(\sigma>1/2\). Suppose an interval contains at least
\[
 f\,|I|\frac{\log T}{4\pi}
 \tag{5}
\]
zeros with \(\beta\ge\sigma\), where \(f>0\) is fixed. Functional symmetry supplies equally many on the left. The two sides together therefore occupy a fraction at least \(f+o(1)\) of the Riemann–von Mangoldt count, uniformly as \(h\to\infty\). Each such interval satisfies (1) with \(\lambda=f(\sigma-1/2)/2\). For \(f=1-o(1)\), (2) gives \(T^{2(1-\sigma)+o(1)}\) for all the zeros in all such intervals. If \(\sigma>3/4\), the twelfth moment gives this exponent already for \(f\ge 1/3+1/[6(\sigma-1/2)]\). At \(\sigma=3/4\), the fourth-moment exponent is \(1-f/2\), below Guth–Maynard's general \(5/9\) whenever \(f>8/9\). These are bounds on the indicated subclass. [Guth and Maynard](https://arxiv.org/abs/2405.20552)

In particular, a plateau of right-hand zeros at real part at least \(3/4\), with consecutive specified ordinates spaced \((c+o(1))/\log T\) throughout an interval of length tending to infinity, satisfies (5) with \(f=4\pi/c+o(1)\). For \(c=4\pi\) their total count has exponent at most \(1/2\). For \(4\pi\le c<9\pi/2\) the bound beats \(5/9\). The proof also covers irregular spacings having the same local density. For larger \(c\), or for points that occur alone, (4) leaves room for an off-line zero. An upper bound on the fourth moment cannot by this argument force the horizontal displacement of every individual zero to vanish.
