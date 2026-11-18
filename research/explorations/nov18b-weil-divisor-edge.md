# The full fixed spectral edge of the finite prime divisor matrix

**Proposed unconditional theorem.** Let \(A_N\) be the real symmetric matrix indexed by \(1\le n\le N\), with zero diagonal and edge weight \(\Lambda(d)/\sqrt d\) between \(n\) and \(dn\le N\). These are the exact prime shifts within one [Mellin comb](nov18b-weil-combs.md). Form the nondecreasing list \(0=\ell_1\le\ell_2\le\cdots\) of the finite sums
\[
 \sum_{p\in S}\left(j_p+\frac p{p-1}\right)\log p,
 \qquad S\text{ finite},\quad j_p\in\{0,1,2,\ldots\},
 \tag{1}
\]
counting all choices with multiplicities. For each fixed \(i\), the \(i\)-th largest eigenvalue satisfies
\[
 \lambda_i^\downarrow(A_N)=\log N-\gamma_E-\ell_i+o_i(1).
 \tag{2}
\]
In particular the gap below the top eigenvalue tends to \(2\log2\). Every sequence of unit vectors with Rayleigh quotient \(\log N-\gamma_E-o(1)\) approaches the line spanned by \((n^{-1/2})_{n\le N}\). The boundary \(n\le N\) couples all prime exponents; simply tensoring the one-prime operators would not prove (2). The proof below controls that boundary and large primes before passing to a product.

## The finite energy and its two boundary estimates

Put \(U=\log N\), \(H_N=\sum_{n\le N}1/n\), and give \(\{1,\ldots,N\}\) the probability measure \(\mu_N(n)=1/(nH_N)\). Under \(a_n=b_n/\sqrt{nH_N}\), the residual of \(A_N\) is
\[
 \langle(U-A_N)a,a\rangle=\mathcal E_N(b)+
              \sum_n\mu_N(n)R(N/n)|b_n|^2,
 \quad
 \mathcal E_N(b)=\frac1{H_N}\sum_{dn\le N}\frac{\Lambda(d)}{dn}|b_{dn}-b_n|^2.
 \tag{3}
\]
Here \(R(t)=\log t-\sum_{d\le t}\Lambda(d)/d\) is bounded and tends to \(\gamma_E\) by the prime number theorem with classical remainder and partial summation. The constant is given by the expansion at 1 of \(-\zeta'/\zeta\). Equation (3) is completion of squares using \(\sum_{d\mid n}\Lambda(d)=\log n\).

Below consider unit vectors with \(\mathcal E_N(b)\le K\), with \(K\) fixed. For \(0<D<U\),
\[
 \sum_{\log n>U-D}\mu_N(n)|b_n|^2\ll (K+1+D)/(U-D).
 \tag{4}
\]
Indeed multiply \(\log n=\sum_{d\mid n}\Lambda(d)\) by \(\mu_N(n)|b_n|^2\) on that set and bound \(|b_n|^2\le2|b_n-b_{n/d}|^2+2|b_{n/d}|^2\). At each lower endpoint \(m=n/d\) the resulting outgoing sum of \(\Lambda(d)/d\) across this band is \(O(1+D)\) by the first Mertens estimate. In particular (4) implies \(\sum\mu_N R(N/n)|b_n|^2=\gamma_E+o(1)\), uniformly over these vectors, by taking e.g. \(D=\sqrt U\).

For \(P\ge2\), let \(s_P(n)\) be the largest divisor of \(n\) with prime factors at most \(P\). The same difference bound and \(\log s_P(n)=\sum_{d\mid n,\,d=p^a,\,p\le P}\Lambda(d)\) give
\[
 \sum_n\mu_N(n)|b_n|^2\log s_P(n)\ll K+1+\log P.
 \tag{5}
\]
This time the total outgoing sum is at most \(\sum_{p\le P}\log p/(p-1)\ll1+\log P\).

## Removing the large prime factors

For any complex \(b\) and \(2\le P<N\) one has
\[
 \sum_n\mu_N(n)|b_n-b_{s_P(n)}|^2
   \ll \frac{1+\log(U/\log P)}{\log P}\,\mathcal E_N(b).
 \tag{6}
\]
Remove the full exponents of primes above \(P\), in bins \(P^{2^j}<p\le P^{2^{j+1}}\) taken in increasing \(j\); stop at \(N\). The number of bins \(J\) is \(O(1+\log(U/\log P))\). Cauchy bounds the squared total difference by \(J\) times the sum of squared within-bin differences.

Fix one bin. Its starting integer \(u\) arises from \(n=ut\), where the previously removed primes of \(t\) lie in \((P,P^{2^j}]\). Their total harmonic weight after dropping the size bound is at most \(\prod_{P<p\le P^{2^j}}(1-1/p)^{-1}\ll2^j\) by Mertens' product theorem. Within the bin, average over uniform random orders of the distinct primes present, each time removing the full exponent. Consider an edge from state \(m\) down to \(m/p^{v_p(m)}\) when \(m\) has \(k\ge1\) remaining bin primes. A starting state with \(l\) extra distinct bin primes has the form \(ms\), \((m,s)=1\), and the probability of using this edge is \(1/[k\binom{k+l}{l}]\). Cauchy on that path costs \(k+l\). The harmonic sum of possible \(s\) with \(l\) distinct bin primes is at most \(Z^l/l!\) where \(Z=\sum_{p\text{ in bin}}1/(p-1)\ll1\), again by Mertens. The expected total coefficient on this edge, apart from the earlier factor \(O(2^j)\), is at most
\[
 \frac1m\sum_{l\ge0}\frac{Z^l}{l!}\frac{k+l}{k\binom{k+l}l}
 =\frac1m\sum_{l\ge0}\frac{(k-1)!Z^l}{(k+l-1)!}\le \frac{e^Z}m.
\]
The actual energy contains this edge with weight \((\log p)/m\) before dividing by \(H_N\), and \(\log p\ge2^j\log P\). Thus the contribution for each bin is bounded by \(C/\log P\) times its own energy. Summing the distinct bins and including the initial Cauchy factor proves (6).

## Passing to a product without imposing an independent cutoff

For large \(N\) take \(P=\exp((\log U)^2)\) and \(D=U^{1/4}\). Write \(n=sr\) with \(s=s_P(n)\) and all prime factors of \(r\) above \(P\). The rectangle
\[
 \log s\le D,\quad \log r\le U-D
\]
consists entirely of admissible integers. Equations (4) and (5) show that the squared mass of every unit bounded-energy vector outside it is \(o(1)\), uniformly for fixed \(K\). The bounds apply to \(\log s>D/2\) as well after changing the constant in (5).

Let \(Z_r=\sum 1/r\) over this common restricted rough range, and \(Z_s=\prod_{p\le P}(1-1/p)^{-1}\). On all \(P\)-smooth integers use the product probability \(\nu(s)=1/(sZ_s)\). Under it \(\mathbb E\log s=\sum_{p\le P}\log p/(p-1)\ll1+\log P\), so \(\nu(\log s\le D)=1-o(1)\). Applying the rectangle mass assertion to the constant vector gives
\[
 t_N:=Z_r Z_s/H_N=1+o(1).
\]
For \(\log s\le D\) let \(\beta(s)=Z_r^{-1}\sum_r b_{sr}/r\) over the same rough range. Equation (6) tends to zero for the chosen \(P\). Hence replacing \(b_{sr}\) by \(\beta(s)\) on the rectangle loses \(o(1)\) squared norm: this conditional average minimizes that error and the alternative \(b_s\) has the stated bound. It follows that \(\sum_{\log s\le D}\nu(s)|\beta(s)|^2=1+o(1)\). Jensen and (5) likewise give \(o(1)\) of this squared mass at \(\log s>D/2\). All statements are uniform for fixed \(K\).

For each smooth edge \(s\to sd\) with \(\log(sd)\le D\), all the rough factors in the average remain admissible at both ends. Jensen applied to the differences yields
\[
 t_N\sum_{s,d:\,\log(sd)\le D}\frac{\Lambda(d)}{Z_s sd}|\beta(sd)-\beta(s)|^2
 \le\mathcal E_N(b),
\]
where \(d\) runs over powers of primes at most \(P\). Extend to the full smooth product by taking \(B(s)=\chi(\log s/D)\beta(s)\) on the core, zero outside. Use a fixed Lipschitz \(0\le\chi\le1\) equal to one on \([0,1/2]\) and zero on \([1,\infty)\). Then \(\|B\|_{\nu}^2=1+o(1)\). For the full product energy \(\mathcal E_P\), decompose the difference at \(s,sd\) into \(\chi(sd)\Delta\beta+\Delta\chi\,\beta(s)\) (here \(\chi(s)\) denotes the scaled cutoff). The first part is zero if \(sd\) is outside the core. Use the weighted squared-sum bound with coefficients \(1+\delta,1+1/\delta\). The second part costs
\[
 O\!\left((1+1/\delta)D^{-2}
      \sum_{p\le P,\ a\ge1}\frac{\log p}{p^a}(a\log p)^2\right)
 \ll (1+1/\delta)D^{-2}(1+\log P)^3.
\]
The final estimate follows by partial summation from Chebyshev for the first powers, as higher powers contribute a convergent series. Choosing \(\delta\to0\) slowly gives the linear map \(b\mapsto B\) with
\[
 \|B\|_{\nu}^2=1+o(1),\qquad
 \mathcal E_P(B)\le\mathcal E_N(b)+o(1)
 \tag{7}
\]
uniformly on unit bounded-energy balls. This step excludes a spurious low state escaping to rough primes, to the support boundary, or to a large smooth part.

## One-prime diagonalization and min–max

The exponent of \(p\) under \(\nu\) has geometric law \((1-1/p)p^{-a}\), independently at different primes. Apart from its \(\log p\) factor the positive generator on that coordinate is
\[
 (L_p h)(a)=\sum_{j=1}^a(h(a)-h(a-j))
              +\sum_{j\ge1}p^{-j}(h(a)-h(a+j)).
\]
Besides the constant function, a complete orthogonal basis consists of the nested-tail contrasts which vanish below level \(j\), equal \(-1/(p-1)\) at \(j\), and one above \(j\), for each \(j\ge0\). Their weighted means on the corresponding tails are zero. Completeness follows by recovering each singleton indicator from the constants and successive contrasts and then using density. Direct substitution gives eigenvalue \(j+p/(p-1)\), including at \(a<j\) where the tail mean vanishes. Tensor products give (1) with \(p\le P\) for the product generator. The finite-smooth support cutoffs in (7) are in its form domain; alternatively the lower variational comparisons follow by expansion in this orthogonal basis. Any fixed initial segment of (1) stabilizes as \(P\to\infty\).

For the upper comparison on the finite residual, lift the finitely many tensor eigenfunctions giving the first \(i\) levels to their actual prime exponents on \(n\le N\). They are bounded and depend on a fixed finite set of primes. The harmonic measure of any prescribed divisibility event \(d\mid n\) tends to \(1/d\), by \(H_{\lfloor N/d\rfloor}/(dH_N)\). The finite-level contrasts are linear combinations of these indicators, so inner products converge to their product values. Only edges from those fixed primes can change a test. For a fixed \(p^k\), omitting \(n>N/p^k\) costs \(o(1)\) normalized harmonic mass. Summable domination by a constant times \(\sum_k(\log p)/p^k\) therefore gives convergence of their energy matrices. The potential in (3) tends to \(\gamma_E\) on this finite space by (4).

Conversely the upper comparison bounds the energy uniformly on the span of the lowest \(i\) finite residual eigenvectors, since \(R\) is bounded. The map (7) is injective on this space for large \(N\) and transfers all unit vectors there with \(o(1)\) error in the appropriate variational direction. Equation (4) removes the same potential. Min–max on the full smooth product now gives the opposite inequality for the \(i\)-th residual and establishes (2). The assertion about near-maximizing vectors follows either from (7) and the product gap, or from (2), the window gap, and the Rayleigh quotient of \(b=1\) in (3).

The [rational-label prime graph](nov18b-prime-graph.md) uses both signs of each prime valuation. Here valuations are nonnegative, the integer size cutoff is imposed before diagonalization, and the source is the finite prime block itself. The theorem gives no sign for the cross block joining the two Mellin families in a full Weil test.
