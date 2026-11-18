# Independent audit of the critical Euler tilt and arithmetic phase CLT

18 November 2026. For every fixed \(D>0\), under RH, the centered cosine statistic of one derivative-weighted tail ordinate satisfies the stated normal limit at the growing cutoff \(P=(\log Y)^D\). This uses all rational characters from each fixed Fourier degree, not just covariances of the prime variables. The critical independent Poisson tilt is mutually singular with Haar on the full prime torus, despite strictly positive densities on each finite block. These are different assertions about different measures.

## Uniform arithmetic moment transfer

Use the normalized two-sided weight \(\mathbb P_Y\{\gamma\}\propto |\zeta'(1/2+i\gamma)|^2/(1/4+\gamma^2)\) on \(|\gamma|>Y\). Opposite ordinates have identical weights. For \(L=\log Y\) and \(g=(m,n)\), the earlier HLZ specialization gives
\[
 \mathbb E_Y e^{-i\gamma\log(m/n)}
 =\frac{g}{\sqrt{mn}}
 +O_{A,B}\left(\frac{g}{\sqrt{mn}}\frac{\log(mn/g^2)}L+L^{-B}\right)
 \qquad(1\le m,n\le L^A).
\]
This follows from (1) of the uniform prime-block proof after division by \(\sqrt{mn}\), even dropping that divisor in the final additive error. The imaginary term vanishes by reflection. This is precisely the symmetric scope established from journal Theorem 5, formulas (5), (24), and the uniform log-saving proof in §§4–5, including the ineffective small-conductor estimate from Proposition 10. Neither a separate one-sided complex phase result nor a new arithmetic independence premise is required. [Uniform estimate (1)](finite_moment63_uniform_prime_blocks.md) · [Source audit](uniform64_hlz_third_review.md)

Let \(\sigma\) be the independent Poisson measure with circle radii \(p^{-1/2}\). On the prime torus its Fourier coefficient at the character \(m/n\) is \(g/\sqrt{mn}\), by multiplying \(\prod_p p^{-|v_p(m)-v_p(n)|/2}\). Define
\[
 W_P=\sum_{p\le P}\frac{\cos\theta_p}{\sqrt p},\qquad
 H_P=\sum_{p\le P}p^{-1},\qquad
 V_P=\frac12\sum_{p\le P}(p^{-1}-p^{-2}).
\]
For the arithmetic model use \(\theta_p=\gamma\log p\bmod 2\pi\). The sign choice is immaterial for cosines and the two-sided character estimate. In the expansion of \(W_P^j\), every product is a sum with nonnegative real coefficients after replacing each cosine by half the sum of its forward and inverse character. Even when products share primes or cancel entirely, collecting like terms preserves nonnegativity. Every resulting rational has numerator and denominator at most \(P^j\), before and after reduction. Thus for a fixed maximum moment degree \(k\), choose \(A=Dk\) and apply the displayed estimate uniformly at every such character, of either sign. The reduced logarithm in the error is at most \(2j\log P\). Constant characters have exact expectation 1 under both measures.

The sum of all Fourier coefficients in \(W_P^j\) is its value at the identity and is \((\sum_{p\le P}p^{-1/2})^j\le(2\sqrt P)^j\). The sum weighted by the positive Poisson Fourier coefficients is exactly \(\mathbb E_\sigma W_P^j\). For any tuple of \(j\) primes, group repeated factors. A prime occurring once has expected weighted cosine \(1/p\); for a prime occurring \(e\ge2\) times, the absolute expectation of its weighted power is at most \(p^{-e/2}\le1/p\). Independence and grouping by partitions of the \(j\) positions therefore give \(\mathbb E_\sigma W_P^j=O_j(H_P^j)\) for \(H_P\ge1\). Nonnegativity of the Fourier expression also verifies that no cancellation is used for this bound. Consequently
\[
 |\mathbb E_Y W_P^j-\mathbb E_\sigma W_P^j|
 \ll_{D,k,B}\frac{\log P}{L}\,H_P^j+L^{-B}(2\sqrt P)^j
 \quad(1\le j\le k).
\]
The zeroth discrepancy is zero. Binomial centering may have alternating coefficients, so use the triangle inequality only at that stage. The centered \(k\)-th discrepancy divided by \(V_P^{k/2}\) is
\[
 O_{D,k,B}\left(\frac{\log P}{L}H_P^{k/2}
 +\frac{(H_P+2\sqrt P)^k}{L^B V_P^{k/2}}\right)=o(1).
\]
Here \(H_P\to\infty\), \(V_P=H_P/2+O(1)\), \(H_P\ll1+\log P\), and \(H_P\ll\sqrt P\) already by the integer reciprocal-square-root sum. Choose \(B>Dk/2+1\). Both constants \(A,B\) are fixed before taking \(Y\to\infty\) at each \(k\). This gives no estimate uniform in a growing moment degree, and no numerical onset because the cited small-modulus step is ineffective. The limiting covariance matrix alone does not imply any of these higher moment bounds.

Under \(\sigma\), each summand has mean \(1/p\) and variance \((1/p-1/p^2)/2\), since \(E\cos\theta=p^{-1/2}\) and \(E\cos(2\theta)=p^{-1}\). Write \(U_p=\cos\theta_p/\sqrt p-1/p\). Independence gives the model CLT by the Lindeberg condition, as \(|U_p|\le2/\sqrt p\) and \(V_P\to\infty\). For the claim of convergence of every fixed model moment, Lindeberg convergence needs a separate uniform-integrability step. For fixed real \(t\), Taylor expansion of the centered exponential factors gives
\[
 \log E_\sigma \exp\!\bigl(t\textstyle\sum_{p\le P}U_p/\sqrt{V_P}\bigr)
 =t^2/2+o(1).
\]
Indeed \(\sum_{p\le P}E|U_p|^3\) is bounded, so the Taylor errors are \(O_t(V_P^{-3/2})\), and the log-expansion squared terms are bounded by \(O_t(V_P^{-2}\sum_p p^{-2})\). This gives uniform exponential moments at \(t=\pm1\), and hence uniform integrability of every fixed power. Combined with the CLT this gives convergence of all model moments to Gaussian moments. Transfer yields the same for the arithmetic distributions. Their second moments give tightness. Along any weakly convergent subsequence, the higher even moment bounds justify passage of all moments to the limit. The Gaussian moment sequence is determinate, for example by Carleman's criterion. Thus the arithmetic normalized statistic converges in distribution to \(N(0,1)\). This also implies \(W_P/H_P\to1\) in probability along the arithmetic tail. With Mertens' prime reciprocal estimate, \(H_P=\log\log\log Y+O_D(1)\), and the variance scale is half that leading logarithm.

## The infinite tilt and a separating event

For a radius \(0<r<1\), the single-circle Poisson density relative to Haar is
\[
 \frac{1-r^2}{|1-re^{i\theta}|^2}.
\]
Multiplying with \(r=p^{-1/2}\) gives the finite-block density \(\prod_{p\le P}(1-p^{-1})\bigl|\prod_{p\le P}(1-p^{-1/2}e^{i\theta_p})^{-1}\bigr|^2\). Every factor is continuous, strictly positive, and integral one. The independent product law has these consistent finite marginals. This construction alone gives no positive density on the infinite product.

Under Haar the mean of each summand in \(W_P\) is zero and its variance is \(1/(2p)\). Under the tilt the mean is \(1/p\) and the centered variance is at most \(1/(2p)\). Enumerate primes in increasing order and write \(H_j=\sum_{\ell\le j}1/p_\ell\). For either measure, the centered independent increments divided by \(H_j\) have summable variances:
\[
 \sum_{j\ge2}\frac{1/p_j}{H_j^2}
 \le \sum_{j\ge2}\int_{H_{j-1}}^{H_j}x^{-2}\,dx<\infty.
\]
The Kolmogorov convergence criterion and Kronecker's lemma then give centered \(W_{p_j}/H_j\to0\) almost surely. Explicitly the weighted independent centered series converges by its square-summable variances, and the increasing \(H_j\to\infty\) gives the unweighted scaled convergence by summation by parts. Hence the event \(\lim W_{p_j}/H_j=1\) has tilt probability one and Haar probability zero. The event is Borel, since each partial sum is continuous. This proves mutual singularity even though finite-coordinate restrictions are mutually absolutely continuous. The arithmetic convergence proved above is scalar and in distribution, with no claim of absolute continuity, total variation convergence, or all-character convergence for the growing block.

The finite likelihood itself gives another separating statistic. Its one-prime log is
\[
 \ell_p(\theta)=\log(1-r_p^2)+2\sum_{j\ge1}\frac{r_p^j}{j}\cos(j\theta).
\]
The series is absolutely convergent. Its mean is \(\log(1-r_p^2)\) under Haar and \(-\log(1-r_p^2)\) under the Poisson tilt, using \(E_\sigma\cos(j\theta)=r_p^j\) and the power series of \(-\log(1-r_p^2)\). The centered size is \(O(r_p)\) with a uniform constant because \(r_p\le1/\sqrt2\). Hence the same variance criterion gives \(\sum_{p\le P}\ell_p/H_P\to-1\) under Haar and \(+1\) under the tilt, since \(\sum r_p^4\) converges. The finite densities tend to zero Haar-almost surely but cannot converge in Haar \(L^1\), as each has integral one. This observation is compatible with the singular infinite measure.

For every \(Y\) the arithmetic distribution on a nonempty prime block is carried by a countable set of phase vectors. The model's finite-block projections have continuous densities, so these two measures are singular at each finite \(Y\). Weak scalar convergence and moment convergence remain possible because neither implies total variation approximation to a continuous model.

## Remaining checks on the mature candidate

I checked the full candidate, including the off-critical identification, the covariance-only concentration estimate, and its finite truncation comment. For fixed \(\sigma>1/2\), the finite product densities have Haar mean one and form a martingale. Parseval gives each factor's squared integral \(1+2\sum_{j\ge1}r_p^{2j}=(1+r_p^2)/(1-r_p^2)\), so their product is uniformly bounded by \(\sum_p p^{-2\sigma}<\infty\) after taking logs. The Euler logarithm has a centered independent linear term with summable variances and absolutely summable higher terms. Its exponential therefore gives a finite nonzero limit almost surely. The square-modulus normalizing constant is \(\zeta(2\sigma)\) by the absolutely convergent Euler product. Martingale convergence in Haar \(L^2\) and testing cylinders identify the claimed product law, and its limit density is positive almost surely. This is genuinely equivalence for each fixed \(\sigma>1/2\), in contrast with the critical separating event. The one-coordinate Hellinger affinity also expands as \(1-r^2/4+O(r^4)\): the second-order integrand coefficient is \(-1+(3/2)(\Re U)^2\), with Haar mean \(-1/4\), and the integral is even in \(r\). The direct almost-sure argument above avoids depending on the Kakutani criterion.

I inspected Najnudel–Wei §1.2 Proposition 1.5, §3.1 Definition 3.1 (70) and §3.2 Lemma 3.1 (77)–(78). Their real tilt is normalized \(|\zeta(\sigma,X)|^{2s}\), and independence with the one-prime weighted densities is explicit. At \(s=1\), \(m_1(r)=1/(1-r^2)\) by the geometric series, giving exactly the claimed Poisson law. Their Gaussian result concerns \(-(2\sigma-1)L'(\sigma,X)\) under that random-model tilt as \(\sigma\downarrow1/2\); it does not provide the arithmetic \(W_P\) result. [Najnudel–Wei PDF](../../sources/analytic64_recent_frontier/complex_deriv.pdf)

The candidate's covariance-only estimate uses \(W_P-H_P=\Re\sum_p \sqrt{p-1}\,Z_p/p\) and \(\sum_p (\sqrt{p-1}/p)^2\le H_P\). This gives the upper bound on real-part variance from the full Hermitian covariance matrix; it cannot by itself give the exact factor \(1/2\) for real variance. The later moment argument yields \(\operatorname{Var}_Y W_P\sim V_P\). Reflection also shows that the law of this real cosine statistic is identical with the positive-ordinate restriction normalized separately, without making the corresponding assertion for arbitrary raw complex phase observables. The model moment bound in the candidate uses a second valid uniform-integrability proof: the log moment generating function of one centered coordinate has second derivative equal to a tilted variance, at most one quarter of the squared range. The range \(2/\sqrt p\) gives the displayed \(1/p\) bound and hence a uniform sub-Gaussian bound after normalization.

For the rational products in a raw moment of degree \(j\), the stronger \(mn\le P^j\) holds before reduction, because each of the \(j\) factors contributes exactly one prime to the numerator or denominator. Thus the candidate's \(\log(mn/g^2)\le j\log P\) is valid. My independent finite control at \(P=7\) enumerated all signed tuples through degree 5, checked \(mn\le7^j\) after reduction and used exact rational coefficients after multiplication by the model expectation (each prime exponent \(e+|a|\) is even). It obtained \(H=247/210\), \(V=33281/88200\), and \(E W^2=155299/88200=H^2+V\). For actual finite truncation, \(\sup |W_P|^j\le(2\sqrt P)^j\) gives the stated numerator-tail bound after multiplication by \(B_T\). This is a bound for fixed \(P\) in the truncation step, not a finite numerical zeta certificate.

The final candidate also notes \(B_T\le \mathcal T(T)/(\sqrt2-1)^2\) under RH, using the stated separate \(Q_2\)-weighted tail majorant at \(T\ge100\). This follows from \(|\sqrt2e^{-i\gamma\log2}-1|\ge\sqrt2-1\) pointwise and from identical weights and cutoff. It does not make the HLZ uniform asymptotic effective. [Weighted tail bound](prime64_sharper_moments.md)

Checked candidate SHA-256 c7fb2482cdc1899e12bc77ad69eb5a574a00667216201f05bd1972d7c1457eaf. Najnudel–Wei source SHA-256 8e606efd10bd1e46d7ad9bec6ffd65b277c85a2c32e8393e6c14d51b3b54f4e4. No canonical records changed.
