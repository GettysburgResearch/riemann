# Detecting an off-line zero by a Jensen polynomial using analytic capacity

**Proposed unconditional local theorem.** Write \(\Xi(z)=\xi(1/2+iz)\), and let \(J_D(z)=\sum_{j\le D}(D)_{\underline j}[z^j]\Xi(z)\,z^j/D^j\) denote its ordinary normalized Jensen polynomial, with the coefficient extraction acting on \(\Xi\) only. Suppose \(\Xi(w)=0\), \(\Re w=T\ge100\), \(0<|\Im w|=\delta<1/2\). For every integer
\[
 D\ \ge\ C\,T^2(\log T)^2/\delta^2
\]
the disk \(B(w,\delta/2)\) contains a zero of \(J_D\). The constants are absolute and unevaluated. By the Laguerre multiplier argument of the [previous converse, §4](jensen-converse-nov18.md), the classical even-coefficient Jensen polynomial at zero shift and degree \(d\) is nonhyperbolic whenever \(2d\) satisfies this inequality. The new contour removes the earlier factor \((\log\log T)^2\). No separation between the original zeros is assumed.

## A separating contour

Use the local Blaschke factorization and bounds from [the cluster contour, §1](weil-contour-nov18.md) in the disk of radius between 4 and 5 about \(2+iT\). By the isometry \(s=1/2+iz\), view its multiset of zeros as \(a_1,\ldots,a_N\) in the \(z\)-plane. Here \(N\ll\log T\). Use the positive atomic measure \(\mu=\sum_j\delta_{a_j}\), counting multiplicities. Choose \(Q=C_0\log T/\delta\), with \(C_0\) a sufficiently large absolute constant.

There is a compact exceptional set \(E\) of analytic capacity \(\gamma(E)\ll N/Q\) containing all the atoms such that for \(z\notin E\)
\[
 \left|\sum_j\frac1{z-a_j}\right|\le Q,\qquad
 r_j(z)\ge j/Q\quad(1\le j\le N),
 \tag{1}
\]
where \(r_j\) are the increasing distances from \(z\) to the atoms. For the first bound use the closed rational lemniscate \(E_1=\{|\sum_j (z-a_j)^{-1}|\ge Q\}\), including its poles. Outside the atoms this set lies in \(\{C_*\mu>Q/2\}\), where \(C_*\) is the maximal truncated Cauchy transform. Tolsa's weak estimate for \(\gamma_+\) and his comparison \(\gamma\asymp\gamma_+\) yield \(\gamma(E_1)\ll N/Q\). The finite pole set has zero capacity. For the second bound adjoin \(E_2=\bigcup_{j=1}^N\{r_j\le j/Q\}\). For every point in this set some closed disk of radius \(j/Q\) about it contains at least \(j\) atoms. The five-times covering lemma bounds the set by disks of total radii at most \(5N/Q\) (an arbitrarily small enlargement allows open disks). Indeed the selected disjoint disks contain disjoint atom sets. Semiadditivity, together with the disk capacity formula, gives \(\gamma(E_2)\ll N/Q\) and the same bound on \(E=E_1\cup E_2\). [Tolsa, Proposition 2.1](https://mat.uab.cat/~xtolsa/gam4.pdf) · [Tolsa, Theorems 1.1 and 1.4](https://arxiv.org/abs/math/0204027)

Every connected component of \(E\) has diameter at most \(4\gamma(E)<\delta/16\). This uses the elementary bound \(\gamma(K)\ge \operatorname{diam}(K)/4\) for a compact connected set, by the exterior Riemann mapping theorem and the Koebe quarter theorem after inversion. Both \(E_1\) and \(E_2\) are compact semialgebraic sets (the latter is a finite union of intersections of disks), so \(E\) has finitely many components. Adjoin to \(\overline B(w,\delta/4)\) all the components that intersect it. The resulting compact set is contained in \(B(w,3\delta/8)\) and is at positive distance from the remaining components. A small smooth bounded neighborhood \(\Omega\) of this compact set consequently satisfies
\[
 w\in \Omega\subset \overline\Omega\subset B(w,\delta/2),\qquad \partial\Omega\cap E=\varnothing .
\]
For instance take a sufficiently fine smooth approximation to the distance from the compact set and a sufficiently small positive regular level. Thus (1) holds on the entire boundary. Holes in the neighborhood cause no difficulty for the argument principle.

## Relative bounds and the Jensen multiplier

For \(z\in\partial\Omega\), (1) implies
\[
 \sum_j|z-a_j|^{-2}\le (\pi^2/6)Q^2,\qquad
 \sum_j\log^+(1/|z-a_j|)\le\sum_{j\le N}\log^+(Q/j)
 \ll (1+\log(1/\delta))\log T=:H.
\]
In the last estimate \(Q\ge N\) and \(N\log(eQ/N)\) is increasing for \(N\le Q\). The second inequality and the cited Blaschke bound give \(|\Xi(z)|\ge \exp(-\pi T/4-C_1H)\). The nonvanishing factors remaining after the zero numerators are removed have log-modulus gradients \(O(\log T)\) throughout \(B(z,1/8)\), by Harnack, interior gradient bounds and Stirling as in [the earlier converse, §1](jensen-converse-nov18.md). The elementary inequality \(\log|1+b|\le\Re b+|b|^2/2\), applied to each zero numerator, and both bounds in (1) yield
\[
 |\Xi(z+v)|/|\Xi(z)|\le\exp(CQ|v|+CQ^2|v|^2),\qquad |v|\le1/8.
\]
The signed sum in (1) is important in the linear term. With \(K=\lceil C_2H\rceil\), the constants can be chosen so that \(\sqrt K/Q\le1/8\). Choose \(C_2\) first sufficiently large for the tail below and then increase \(C_0\) if needed; the lower modulus bound can use a fixed initial \(C_0\) and contour, and the derivative estimate allows an independently enlarged \(Q\). Cauchy on radii \(\sqrt j/Q\) now gives
\[
 |\Xi^{(j)}(z)|/|\Xi(z)|\le (C_3 Q\sqrt j)^j\qquad(1\le j<K).
\]

For completeness the coefficients of \(B_D(v)=e^{-v}(1+v/D)^D\) satisfy \(c_0=1,c_1=0, |c_j|\le(e/(jD))^{j/2}\), by Cauchy's estimate. Hence the sum of \(|c_j z^j \Xi^{(j)}(z)|/|\Xi(z)|\) over \(2\le j<K\) is at most \(\sum_{j\ge2}(C_4 TQ/\sqrt D)^j<1/4\) for the asserted degree. The [Fourier tail estimate, §3](jensen-converse-nov18.md) bounds the remaining absolute error by \(2^{-K}e^{-\pi T/4}T^{C_5}\), uniformly for every such boundary point; that argument depends only on the real and imaginary part bounds on \(z\). This is less than \(|\Xi(z)|/4\) for the selected \(C_2\). Rouché gives equality of the zero counts of \(J_D\) and \(\Xi\) in \(\Omega\), including multiplicity. The domain contains \(w\) and is disjoint from the real axis, proving the theorem.
