# Many finite changes of sign without GRH

**Proposed theorem.** Put \(L=\log(3Q)\). There are absolute positive constants \(c_1,c_2,c_3,c_4,C\) such that, among fundamental discriminants of either prescribed sign with \(Q<|D|\le2Q\), all but \(O(Qe^{-c_1\sqrt L})\) have at least \(c_2\sqrt L\) alternations between values
\[
 I_D(Y)>c_3L^{1/4}\quad\hbox{and}\quad I_D(Y)<-c_3L^{1/4},
 \qquad e^{c_4\sqrt L}\le Y\le e^{C\sqrt L}.
\]
Here \(I_D(Y)=(\log Y)Y^{-3/2}\int_2^Y\sum_{p\le t}\chi_D(p)\,dt\). This finite sign-change assertion is unconditional. For fixed \(A>0\), all but \(O_A(Q/(\log Q)^A)\) have both finite signs with amplitude exceeding \(c_A\sqrt L\) in \([Q^{b/4},Q^{b/2}]\), where \(b=1/(100\max(1,\lceil A\rceil))\).

Assuming GRH for an individual character outside an exceptional set of the same stated size, the first configuration occurs also arbitrarily late, inside a multiplicative interval with endpoint ratio at most \(e^{C\sqrt L}\). In particular the alternation count concerns the actual continuous integrated function.

## Forward prime sums

At every positive phase \(y>2\) there is an exact finite identity
\[
 I_D(y)=\sum_{p\le y} v_y(p)\chi_D(p),\qquad
 v_y(p)=\frac{\log y}{\sqrt y}(1-p/y).
\]
A parallel family of weights \(\tilde v_y(p)=(\log p)(1-p/y)/\sqrt y\) gives the zero profile on GRH:
\[
 J_D(\log y)=-2/3-K_D(\log y)
    =\sum_{p\le y}\tilde v_y(p)\chi_D(p)+O(1+L/\sqrt y).
\]
Indeed evaluate the [explicit formula](zhao-bias-kernel-nov18.md) with \(g(u)=k(u+\log y)\). Its transform has absolute value \(1/|(1/2+it)(3/2+it)|\) and hence the digamma term is uniformly bounded. The conductor term is \(O(L/\sqrt y)\). The prime sum using \(g(+\log n)\) is \(O((1+|L'/L(1,\chi_D)|)/\sqrt y)=O(L/\sqrt y)\) on GRH, by partial summation at \((\log(3Q))^6\). The term using \(g(-\log n)\) is the displayed finite sum with von Mangoldt weights; all prime powers of exponent at least two cost \(O(1)\) by Chebyshev. Abel damping justifies the boundary prime series as in the prime-tail identity.

## Transferring the two arithmetic estimates

For either set of forward weights, the full square sum is \(\sim (\log y)/3\) by the prime number theorem. For \(v_y\) this is the integral \(\int_0^1 (1-u)^2du=1/3\); for \(\tilde v_y\), the same computation applies after restricting \(u\ge\epsilon\), with the part below \(\epsilon y\) costing \(O(\epsilon\log y)\) for each fixed \(\epsilon>0\) and sufficiently large \(y\).

For the fixed-moment assertion use dyadic \(y\) in \([N^{1/4},N^{1/2}]\) with \(N=Q^b\) as in the [cubic-polynomial argument](zhao-bias-moments-nov18.md). Discard \(p\le N^{1/16}\) with deterministic error \(O(N^{-1/16}\log N)\) by the trivial count. For \(y\le z\) the inner product of the two normalized coefficient vectors is
\[
 \ll \frac{(\log y)(\log z)\pi(y)}
              {\sqrt{yz\log y\log z}}\ll\sqrt{y/z}.
\]
Here \(\log z\le2\log y\). All primality, coefficient-mass and bounded-variance estimates of the cubic-polynomial argument therefore hold, with the square-monomial local correction \(O_A(N^{-1/16})\). Taking the \(v_y\) weights proves the unconditional finite assertion.

For the stronger exceptional set use the geometric scales \(y_j=R^{M+j}\), \(1\le j\le M\), \(M=\lfloor\kappa\sqrt{\log Q}\rfloor\), as in the [independent-block proof](zhao-bias-blocks-nov18.md). Take the disjoint block \(y_j/R<p\le y_j\) and the remote part \(p\le y_j/R\). Discard \(p=2\) with negligible deterministic error. For either weight, the block squared norm \(s_j^2\asymp\log y_j\), with absolute constants independent of sufficiently large fixed \(R\), by the primes in \([y_j/3,y_j/2]\). Normalize by \(s_j\). In the independent local model the block forms \(U_j\) are independent with squared coefficient mass one, whereas the remote forms \(V_j\) have covariance majorized entrywise by the coefficient matrix product
\[
 (BB^{\mathsf T})_{jk}\ll
 \frac{\log y_j\log y_k}{s_j s_k\sqrt{y_j y_k}}\pi(y_j/R)
 \ll R^{-1}R^{-(k-j)/2}\quad (j\le k).
\]
The family transfer for their polynomial moments is unchanged: primes are bounded by \(N=R^{3M}\), and \(\kappa\) is small enough that \(N^{15M}e^{O(M\log M)}\le Q^{1/4}\). The Gaussian quadratic-form estimate makes \(\sum_j V_j^2<\eta M/64\) except with probability \(O(e^{-cM})\) for the absolute \(\eta>0\) of that proof, by enlarging \(R\).

## Counting alternations

For **each prescribed string** \(d_j\in\{-1,1\}\) the previous block-majorant proof bounds by \(O(e^{-c_0M})\) the probability of having at most \(\lfloor\eta M\rfloor\) block values with \(d_jU_j>1/4\). Indeed the signed forms are still independent and symmetric in the model, and the identical polynomial transfer applies. At most \(2\sum_{k\le\alpha M}\binom{M-1}{k}\) strings change sign at most \(\alpha M\) times. Choose a sufficiently small absolute \(\alpha>0\) with binary entropy \(H(\alpha)<c_0/2\). Outside an exceptional set of probability \(O(e^{-c'M})\), every such string has more than \(\eta M\) successful blocks. The remote-energy bound excludes at most \(\eta M\) corrupted coordinates, so every such string has some \(d_j(U_j+V_j)>1/8\).

Take the ordered subsequence of coordinates with \(|U_j+V_j|>1/8\). Were it to have at most \(\alpha M\) sign alternations, its opposite signs could be extended to a string on all coordinates with at most \(\alpha M\) sign changes, by holding each sign across each gap. This string contradicts the last conclusion. Thus more than \(\alpha M\) alternations have magnitude at least \(\min_j s_j/8\gg L^{1/4}\). With \(v_y\) this proves the unconditional theorem, including an intervening zero by continuity for each alternation.

Applying the same argument separately to \(\tilde v_y\) provides a packet of signed witnesses for the profile \(J_D\) on each character satisfying GRH outside a second exceptional set of the same size. Their phases span at most \(M\log R=O(\sqrt L)\). Since \(K_D\) is uniformly almost periodic, the whole finite packet recurs under a common sequence of arbitrarily large translations, and \(I_D(e^t)-J_D(t)\to0\) for the fixed discriminant. The width of the packet is preserved under translation. The [quantitative recurrence bound](zhao-bias-recurrence-nov18.md) also applies simultaneously to all its phases.

## Linearly many crossings in a polynomial conductor range

A second unconditional conclusion gives more crossings at larger amplitudes in a longer range. For each fixed \(A>0\), put \(r=\max(1,\lceil A\rceil)\), \(b=1/(200r)\), and \(N=Q^b\). Except for \(O_A(Q/(\log Q)^A)\) discriminants, there are \(\gg_A\log Q\) alternations of amplitude \(\gg_A\sqrt{\log Q}\) on \([N^{1/4},N^{1/2}]\). The same statement applies to the positive-time profile \(J_D\) under the individual GRH, and thereby gives arbitrarily late packets with multiplicative width at most \(N^{1/4}\). Here are the joint-moment details.

Use scales with fixed successive ratio \(R=e^{12}\) in the indicated range, discard \(p\le N^{1/16}\) as before, and normalize each prime vector to squared Euclidean norm one. Write its signed sum as \(Z_j\). In the Rademacher model, each consecutive pair tends jointly to a centered Gaussian with both variances one and correlation
\[
 \rho=R^{-1/2}(3/2-1/(2R))<1/100 .
\]
This applies for either forward weight. Indeed \(\int_0^1(1-u)(1-u/R)\,du=1/2-1/(6R)\) computes the covariance after the prime number theorem, and the two log scales have ratio tending to one. The largest normalized coefficient is \(O(\sqrt{\log y/y})\). Thus every fixed moment of each pair converges uniformly along the range, by expansion in independent signs (or summing higher cumulants).

For variables \(z,w\), write \(s=z^2+w^2\), \(u=zw\), and introduce the concrete polynomial
\[
 P(z,w)=(-u-1/4-s^2/1000)(1-u)^2 .
\]
A positive value forces opposite signs, \(s<500\), and both \(|z|,|w|>1/(4\sqrt{500})>1/100\). Its positive part is bounded by \(250\,(251)^2<16\,000\,000\). Under the limiting pair \((Z,W)\), its expectation exceeds one. Indeed Wick's formula gives
\[
 \mathbb E[-u(1-u)^2]=2+4\rho^2-10\rho-6\rho^3>1.89,
 \qquad \mathbb E(1-u)^2=2-2\rho+2\rho^2\le2.001.
\]
Also \(s\) is bounded in a Gaussian diagonalization by \(1.01\) times a chi-square variable on two degrees of freedom. Since \(|u|\le s/2\), this gives \(\mathbb E[s^2(1-u)^2]\le 2\mathbb E s^2+\mathbb E s^4/2<220\). Hence every tested pair has mean at least one for sufficiently large \(Q\).

Let \(H=\sum_jP(Z_j,Z_{j+1})\), over the \(m\asymp_A\log Q\) consecutive pairs. It has mean at least \(m\) and variance \(O(m)\) in the Rademacher model. For the variance, write \(a_j(p)\) for the nonnegative normalized coefficients and \(d_j(p)=a_j(p)+a_{j+1}(p)\). At a nonempty set \(S\), the Walsh coefficient of a pair polynomial is bounded by \(C\prod_{p\in S}d_j(p)\) for \(|S|\le8\), zero otherwise. To see this, expand each monomial of degree at most eight, reserve a single occurrence of each prime in \(S\), then group the remaining even occurrences into pairs and use \(\sum_p d_j(p)^2\le4\). Therefore the covariance at two pair indices is \(O(\langle d_j,d_k\rangle)\), and the earlier geometric covariance bound makes its sum \(O(m)\). Applying Boolean hypercontractivity at degree eight gives \(\mathbb E_\varepsilon |H-\mathbb E_\varepsilon H|^{2r}\ll_r m^r\).

This centered moment transfers to the family by the same squarefree calculation as in the fixed-moment proof. Its degree is at most \(16r\), all monomials have prime product at most \(N^{16r}\), and the sum of absolute coefficients is \(O_r(m^{2r}N^{16r})\). The residue-class error is \(O_r(Q^{-1/2}m^{2r}N^{48r})=o(1)\). The square-monomial main-term correction is \(O_r(N^{-1/16}m^{2r})\), by taking the Rademacher expectation after replacing coefficients by their magnitudes as in the cubic case. Markov's inequality now gives \(H>m/2\) except on an arithmetic event of probability \(O_r(m^{-r})\). Since each positively contributing pair costs at most \(16\,000\,000\) in this sum, there are at least \(m/32\,000\,000\) adjacent pairs with opposite signs and both normalized magnitudes exceeding \(1/100\). Each pair supplies a separate robust crossing. Restoring the norms \(\gg\sqrt{b\log Q}\) and the bounded errors proves the assertion.

## A limiting frequency on logarithmic grids

There is an explicit unconditional frequency at the expense of a qualitative density-one exception. Let \(S=S(Q)\to\infty\), with \(S=o(\log Q)\). For every \(\epsilon>0\) there is \(a_\epsilon>0\) such that a proportion tending to one of the discriminants have at least
\[
 \left(\frac{\sqrt3}{2\pi}-\epsilon\right)S
\]
sign alternations of amplitude at least \(a_\epsilon\sqrt S\) on \([e^S,e^{2S}]\).

For a fixed mesh \(h>0\), sample \(s_j=S+jh\le2S\) and write \(Z_j=I_D(e^{s_j})/\sqrt{s_j/3}\). The empirical fraction of adjacent pairs having opposite signs and both magnitudes greater than any fixed \(a\ge0\) converges in probability to the corresponding probability \(p_h(a)\) for a pair of standard Gaussians of correlation \(r_h=(3e^{-h/2}-e^{-3h/2})/2\). To prove this, apply the preceding fixed-order moment transfer jointly to any two or four coordinates: each prime is \(\le e^{2S}=Q^{o(1)}\), so the total arithmetic error for every fixed moment is \(Q^{-1/2+o(1)}\) using the independent quadratic local model. The maximum individual normalized coefficient tends to zero, and the covariance within an adjacent pair tends to \(r_h\) by the integral calculated above. Replacing \(\mathbb E B_p^2=p/(p+1)\) by one changes this limit by \(o(1)\), by first omitting the negligible primes \(p\le e^{S/4}\). Thus each pair tends to the stated Gaussian by its moments, uniformly over the mesh. Pairs of pairs with index separation greater than \(\sqrt{S}\) have all cross-covariances tending uniformly to zero by the geometric bound. Their joint law consequently tends to the product Gaussian law, so their crossing indicators have covariance \(o(1)\), since the threshold boundaries have limiting measure zero. The remaining pairs of pairs form a vanishing fraction. The mean and variance estimates prove the empirical convergence.

At \(a=0\) the bivariate Gaussian sign formula gives \(p_h(0)=\arccos(r_h)/\pi\). Since \(r_h=1-3h^2/8+O(h^3)\), its ratio to \(h\) tends to \(\sqrt3/(2\pi)\) as \(h\downarrow0\). First fix a sufficiently fine mesh, then a sufficiently small positive \(a\) using continuity of the Gaussian probabilities. Multiplication by the number of mesh intervals proves the claimed lower frequency for actual sign alternations. The argument specifies the limiting frequency on each fixed grid and a lower bound for crossings between all real arguments.
