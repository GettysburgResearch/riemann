# Conditional phase law of the derivative-weighted tail

17 November 2026. This audit assumes the fixed-rational limit below. The harmonic-analysis conclusions are independent of how that limit is obtained. Heap–Li–Zhao, published Theorem 5, §4, p. 1605, is the analytic input for the fixed-polynomial specialization. [Published primary text](../../sources/classical63_derivative_moments/hlz2022print.pdf)

## Assumption and normalization

Under RH, consider the finite symmetric measure

\[
 \nu=\sum_{\rho\,\mathrm{simple}}\frac{|\zeta'(\rho)|^2}{|\rho|^2}\,\delta_{\Im\rho},\qquad
 B_Y=\nu(|\gamma|>Y),\qquad
 F_Y(t)=\int_{|\gamma|>Y}e^{-it\gamma}\,d\nu(\gamma).
\]

Assume that these tails have positive mass for sufficiently large \(Y\) and that for every pair of fixed positive integers \(m,n\),

\[
 \frac{F_Y(\log(m/n))}{B_Y}\ \longrightarrow\ \frac{\gcd(m,n)}{\sqrt{mn}}. \tag{H}
\]

The symmetric normalization includes both signs of the ordinate. Thus \(F_Y/B_Y\) is real and even, and equals 1 at the origin. The order in (H) holds \(m,n\) fixed while \(Y\) tends to infinity. A one-sided analogue requires complex Fourier convergence, or a separate argument controlling the imaginary part. Symmetric convergence alone supplies only its real part.

A sufficient analytic precursor on the symmetric truncation is an asymptotic \(S_r(x)=c_r A x\log^4 x+o(x\log^4 x)\) for the cumulative \(\sum_{0<|\gamma|\le x}|\zeta'(\rho)|^2 e^{-i\gamma\log r}\), where \(A=1/(12\pi)\) for the two-sided normalization, \(c_1=1\), and \(c_{m/n}=\gcd(m,n)/\sqrt{mn}\). The one-sided untwisted constant is \(1/(24\pi)\). With \(w(x)=(x^2+1/4)^{-1}\), partial summation gives the exact tail formula

\[
 F_Y(\log r)=-w(Y)S_r(Y)-\int_Y^\infty w'(x)S_r(x)\,dx
    =c_r A\frac{\log^4Y}{Y}+o\!\left(\frac{\log^4Y}{Y}\right).
\]

The endpoint term is required for the strict tail. The integral has leading coefficient \(2c_r A\), and the endpoint subtracts \(c_r A\). The remainder estimate follows by taking the supremum of \(|S_r(x)-c_r A x\log^4 x|/(x\log^4 x)\) over \(x\ge Y\). Multiple zeros give zero summands at this derivative power on RH.

## Product law on the prime torus

Let \(\mu_Y=B_Y^{-1}\nu|_{|\gamma|>Y}\). Push \(\mu_Y\) forward by

\[
 \iota(\gamma)=(e^{-i\gamma\log p})_{p\,\mathrm{prime}}\in\mathbb T^{\mathcal P}.
\]

For any finitely supported integer vector \(a=(a_p)\), choose coprime \(m=\prod_{a_p>0}p^{a_p}\), \(n=\prod_{a_p<0}p^{-a_p}\). The Fourier coefficient of this pushforward is \(F_Y(\log(m/n))/B_Y\), and (H) yields

\[
 \mathbb E_{\mu_Y}\prod_p \iota_p(\gamma)^{a_p}
      \ \longrightarrow\ \prod_p p^{-|a_p|/2}.
\]

For \(0<r<1\), set

\[
 d\mathsf P_r(e^{i\theta})=\frac{1-r^2}{1-2r\cos\theta+r^2}\frac{d\theta}{2\pi}.
\]

The geometric series gives the absolutely convergent Fourier expansion of its density, \(\sum_{j\in\mathbb Z}r^{|j|}e^{ij\theta}\). Consequently the law with these coefficients is \(\bigotimes_p\mathsf P_{p^{-1/2}}\), and the fixed-prime phases are independent in the limit. The countable product torus is compact, and the finite-character algebra separates its points, is closed under complex conjugation, and contains constants. Stone–Weierstrass therefore yields weak convergence on the whole compact product against each fixed continuous test, as well as weak convergence on every fixed finite block. For a nonempty finite block, every pushforward from the atomic \(\nu\) is countably supported and its limiting Poisson product assigns that support mass zero. Their total variation distance, with the supremum-over-events convention, is exactly 1 for every \(Y\).

The torus is the compact dual of \(\log\mathbb Q_{>0}\) endowed with its discrete topology. Equivalently it is the quotient of the full Bohr compactification \(b\mathbb R=\widehat{\mathbb R_{\mathrm{disc}}}\) obtained by retaining the rational-log characters. The flow \(\iota(\mathbb R)\) is dense, since \(\log p\) are rationally independent by unique factorization. The limiting coefficients on the dense subgroup \(\log\mathbb Q_{>0}\subset\mathbb R\) are discontinuous in the usual real topology. In particular, \(\log((n+1)/n)\to0\) while \(((n+1)n)^{-1/2}\to0\), and the coefficient at 0 is 1. There is no probability on the ordinary real line with these Fourier values. Independently, \(\mu_Y\) has no weakly converging subsequence on the real line as \(Y\to\infty\), since its mass on every bounded interval is eventually zero.

One can extend the coefficient function to all discrete real frequencies by assigning zero to every frequency outside \(\log\mathbb Q_{>0}\). This is positive definite: every finite matrix of differences decomposes into blocks of frequencies in one coset of \(\log\mathbb Q_{>0}\), and the blocks are positive by the product law. It gives one probability on \(b\mathbb R\) by compact-group Fourier theory. Assumption (H) determines the quotient law and leaves the remaining real-frequency coefficients open.

## Covariance of the factorial targets

For \(k\ge1\), let \(Q_k(s)=k^{1-s}-1\) and \(q_k(\gamma)=Q_k(1/2+i\gamma)=\sqrt{k}\,e^{-i\gamma\log k}-1\). The exponential is the product of prime coordinates with exponents \(v_p(k)\). The limiting mean is \(\sqrt{k}/\sqrt{k}-1=0\). Taking the conjugate in the second factor gives

\[
 \lim_{Y\to\infty}\int q_k\overline{q_\ell}\,d\mu_Y
  =\sqrt{k\ell}\,\frac{\gcd(k,\ell)}{\sqrt{k\ell}}
     -\sqrt{k}\,k^{-1/2}-\sqrt\ell\,\ell^{-1/2}+1
  =\gcd(k,\ell)-1. \tag{1}
\]

Since \(\sum_{d\mid a}\varphi(d)=a\), the kernel has the exact divisor representation

\[
 \gcd(k,\ell)-1=\sum_{d\ge2}\varphi(d)\,\mathbf 1_{d\mid k}\,\mathbf 1_{d\mid\ell}.
\]

Thus for any finitely supported complex coefficients \(c_k\), the limiting normalized squared tail norm on these factors is

\[
 \sum_{d\ge2}\varphi(d)\left|\sum_{d\mid k}c_k\right|^2.
\]

This is positive definite on every finite family of distinct indices \(k\ge2\): if the form vanished, the largest index with nonzero coefficient would contribute by itself at the divisor equal to that index. Index 1 gives the zero target. Coprime indices are orthogonal, in particular distinct primes, and the limiting squared norm at index \(k\) is \(k-1\). The prime-index variables are also independent in their joint limit because each is a function of its own prime coordinate. If a separate prime-array error theorem identifies derivative-weighted error forms, (1) is their normalized high-tail part. It does not replace that separate theorem or assert the value for the full untruncated error form.

## Uniformity boundaries and countermodels

**Fixed tests and growing prime sets.** Every finite covariance matrix converges in operator norm, simply by entrywise convergence with dimension fixed. A diagonal argument gives some undefined cutoff \(K(Y)\to\infty\) on which the operator norm still converges for indices \(2\le k\le K(Y)\): for every fixed integer \(j\), take a threshold after which its finite matrix discrepancy is at most \(1/j\), then use a monotone sequence of these thresholds. A prescribed growing cutoff or a rate needs an estimate uniform in the rational frequencies, or in the allowed polynomial coefficients and dimension. The source statement must supply this independently. Pointwise convergence cannot be uniform over all rational frequency choices. For each fixed \(Y\), the continuity of \(F_Y/B_Y\) at zero and the sequence \((n+1)/n\) give supremum discrepancy at least 1. The same limit of discrepancies occurs for ratios of distinct primes: there are arbitrarily large consecutive primes of ratio arbitrarily close to 1, since an eventual lower bound greater than 1 on all consecutive prime ratios would contradict Euler's divergence of \(\sum_p p^{-1}\). Along such pairs, the limiting coefficient \(1/\sqrt{pq}\) tends to zero. The normalized off-diagonal matrix entry \(\int q_p\overline{q_q}\,d\mu_Y/\sqrt{pq}\) tends to 1 along these pairs at fixed \(Y\), as its three remaining terms have total magnitude at most \(p^{-1/2}+q^{-1/2}+(pq)^{-1/2}\).

**A moving single-prime countermodel.** Work with any locally finite symmetric discrete model satisfying (H), with positive half ordinates increasing to infinity and positive summable weights \(w_n\). Write \(b_n=\sum_{i\ge n}w_i\). Choose consecutive index blocks \([n_j,n_{j+1})\) with \(b_{n_{j+1}}/b_{n_j}\le1/j\), possible by summability. Enumerate the primes \(p_j\). For each index in block \(j\), replace the positive ordinate by a strictly larger-than-previous ordinate whose first \(j\) prime phases differ by at most \(1/j\) from the original ones, and whose \(p_{j+1}\) phase differs by at most \(1/j\) from 1. Keep the weights and reflect the new ordinates to keep symmetry. Such choices exist arbitrarily high by finite-dimensional Kronecker density. To see the needed positive-time version directly, each nontrivial character of this flow has average tending to zero over \([0,T]\), by explicit integration and rational independence of the frequencies. Trigonometric approximation then gives Haar time averages and arbitrarily late visits to any open ball. The new ordinates may also be required to be at least the index, ensuring local finiteness.

For each fixed rational, the products of prime phases before and after replacement differ by at most \(\sum_p|v_p(r)|/j\) on all sufficiently late blocks. Both the old and new cutoff tails run through the same ordered index suffixes, so this preserves every assertion (H), including convergence over arbitrary cutoffs between atoms. At the start of block \(j\), however, the normalized \(p_{j+1}\) coefficient tends to 1: the block has relative weight at least \(1-1/j\) and its phase is within \(1/j\) of 1. The predicted Poisson coefficient at this moving prime tends to 0. A related construction preserves the first \(j\) prime phases while imposing extra phase near \(+1\) or \(-1\) at any frequency \(\alpha\) outside the rational span of \(\log p\). These are two models with identical limits in (H) and distinct limits at \(\alpha\). Alternating the imposed sign over tail-dominant blocks even gives nonconvergence at \(\alpha\). This exhibits the precise difference between the prime torus and the full Bohr compactification.

**Unweighted observations and invisible ordinates.** Independently of the above re-embedding, insert any locally finite set of distinct new positive ordinates \(x_j\) into a fixed discrete model with tail mass \(B_Y\). In increasing order of these new points, assign weight \(w'_j=2^{-j}B_{x_j}\) on each of \(x_j\) and \(-x_j\). Then the new mass beyond \(Y\) is at most \(2B_Y\sum_{x_j>Y}2^{-j}=o(B_Y)\). The change in every normalized Fourier coefficient is at most twice the added relative mass, uniformly in frequency. Hence (H) survives. For either \(\eta=1\) or \(-1\), place the new ordinates in disjoint shrinking intervals around successive positive solutions to \(e^{-ix\log 2}=\eta\). Let batch \(j\) have at least \(j\) times one plus the number of original positive ordinates through the right endpoint of the next batch. For every height from the end of batch \(j\) through the end of batch \(j+1\), the original points are then at most a fraction \(1/j\) of the enlarged count. The unweighted mean of the prime-2 phase over positive ordinates up to height \(T\) tends to \(\eta\), since all added phases from late batches are close to \(\eta\). The same holds for the normalized unweighted annulus \(T<|\gamma|\le2T\) along subsequences where a batch dominates that annulus, if its size is also chosen to exceed \(j\) times the number of all previous added points. Thus the derivative-weighted fixed-rational limits allow incompatible unweighted statistics even among abstract models whose atoms all have positive weight. Arbitrary zero-weight points are exactly invisible, which describes the information loss for multiple zeros upon taking \(|\zeta'(\rho)|^2\). These are measure countermodels to inference from (H) alone. They do not assert that re-embedded ordinates or assigned weights occur for the zeta function or preserve additional analytic or unweighted counting hypotheses.

Independent-prime phase variables here describe a single weighted draw from the high ordinates. A statement about spacings or joint statistics of neighboring zeros needs an additional multi-ordinate input. The harmonic-analysis deductions use standard compact-group Fourier analysis and make no claim of priority.
