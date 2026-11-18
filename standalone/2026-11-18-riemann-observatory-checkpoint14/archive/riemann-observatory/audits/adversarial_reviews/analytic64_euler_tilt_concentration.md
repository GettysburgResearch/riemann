# Poisson Euler tilt and Gaussian concentration for growing prime blocks

18 November 2026. At fixed \(\sigma>1/2\), the prime-torus Poisson product of radii \(p^{-\sigma}\) is the random Euler product's normalized squared-modulus tilt of Haar. At \(\sigma=1/2\), the Poisson product is singular to Haar. For the actual derivative-weighted zero tail, RH and the established uniform twisted-moment estimate imply both a growing-prime phase bias and a Gaussian fluctuation theorem at every fixed polylogarithmic cutoff. The model facts are unconditional. The arithmetic conclusion uses the uniform estimate with the exact same tail weight. [Uniform prime-block estimate](finite_moment63_uniform_prime_blocks.md) · [Independent source audit](uniform64_hlz_third_review.md)

## Product tilt off the line and singularity at the boundary

Let \(\lambda\) be product Haar on \(\mathbb T^{\mathcal P}\), \(U_p\) its coordinate variables, and \(r_p=p^{-\sigma}\). For \(0<r<1\), the Poisson probability has density and Fourier coefficients
\[
 f_r(u)=\frac{1-r^2}{|1-ru|^2},\qquad
 \int_{\mathbb T}u^a f_r(u)\,dm(u)=r^{|a|}\quad(a\in\mathbb Z).
\]
This follows by multiplying the two geometric series. On primes up to \(P\), the density \(D_{\sigma,P}=\prod_{p\le P}f_{r_p}(U_p)\) is a Haar martingale as primes are added. Parseval gives
\[
 \mathbb E_\lambda D_{\sigma,P}^{\,2}
   =\prod_{p\le P}\frac{1+p^{-2\sigma}}{1-p^{-2\sigma}},
\]
uniformly bounded for each \(\sigma>1/2\). Thus the martingale converges in \(L^2(\lambda)\) and almost surely. The Euler product
\[
 \mathcal E_\sigma=\prod_p(1-p^{-\sigma}U_p)^{-1}
\]
itself converges almost surely to a nonzero value. For the logarithm, its linear terms are independent, centered and square-summable in variance, and all higher powers have an absolutely summable deterministic bound \(O_\sigma(\sum_p p^{-2\sigma})\). The limit of \(D_{\sigma,P}\) is therefore \(|\mathcal E_\sigma|^2/\zeta(2\sigma)\). Testing the martingale limit against any cylinder function gives the corresponding Poisson marginals. Its strict positivity Haar-almost surely also gives equivalence. This is the \(s=1\) case of the real-power Euler tilt of Najnudel–Wei, §3.1 and Lemma 3.1 in §3.2 on pp. 20–25. Their Proposition 1.5 treats the logarithmic derivative of the random Euler product as \(\sigma\downarrow1/2\). The arithmetic statistic below instead uses the ordinates of zeros and a growing prime cutoff at fixed critical-line radius. [Najnudel–Wei pinned source](../../sources/analytic64_recent_frontier/complex_deriv.pdf)

Now set \(r_p=1/\sqrt p\), \(H_P=\sum_{p\le P}p^{-1}\), \(W_P=\sum_{p\le P}p^{-1/2}\Re U_p\), and \(\mu_*=\bigotimes_p(f_{1/\sqrt p}\,dm)\). Euler's argument gives \(H_P\to\infty\), since the reciprocal Euler product dominates the harmonic sum and \(-\log(1-1/p)=1/p+O(p^{-2})\). Under \(\lambda\), the summands of \(W_P\) have mean zero and variance \(1/(2p)\). Under \(\mu_*\), their means are \(1/p\) and their variances are
\[
 \tfrac12(1/p-1/p^2).
\]
Indeed \(\mathbb E_{\mu_*}\Re U_p=r_p\) and \(\mathbb E_{\mu_*}(\Re U_p)^2=(1+r_p^2)/2\). In either product law, enumerate the primes \(p_j\) and set \(h_j=H_{p_j}\). The sum of the centered summands divided individually by \(h_j\) converges almost surely by the \(L^2\) martingale criterion. Its variance sum is bounded by a constant times \(\sum_j(h_j-h_{j-1})/h_j^2\), finite by comparison from \(j=2\) onward with \(\int_{h_1}^\infty t^{-2}dt\). Kronecker's lemma then gives
\[
 W_P/H_P\longrightarrow0\quad\lambda\text{-a.s.},\qquad
 W_P/H_P\longrightarrow1\quad\mu_*\text{-a.s.}
\]
The second event separates the laws and proves singularity. Kakutani's product-measure criterion gives the same dichotomy. The one-coordinate affinity \(\int\sqrt{f_r}\,dm=1-r^2/4+O(r^4)\) follows by Taylor expansion, using \(\mathbb E_m\Re U=0\), \(\mathbb E_m(\Re U)^2=1/2\) and symmetry under \(r\mapsto-r\). Thus the product of affinities vanishes just when \(\sum_p r_p^2\) diverges in the regimes above. Kakutani's paper is identified from the journal's issue record. The explicit separating event here is proved directly. [Kakutani, Annals of Mathematics 49 (1948), 214–224](https://doi.org/10.2307/1969123)

## Growing-prime arithmetic concentration

Assume RH and use the probability \(\mathbb P_Y\) on ordinates \(|\gamma|>Y\), with atom weights
\[
 \frac{|\zeta'(1/2+i\gamma)|^2}{B_Y(1/4+\gamma^2)},\qquad
 B_Y=\sum_{|\gamma|>Y}\frac{|\zeta'(1/2+i\gamma)|^2}{1/4+\gamma^2}.
\]
This is the untwisted derivative weight, and both signs occur. Multiple zeros have zero weight. Gonek's untwisted derivative moment and partial summation give \(B_Y\sim(\log Y)^4/(12\pi Y)>0\) asymptotically. Put \(U_p=e^{-i\gamma\log p}\), \(L=\log Y\), and \(P=L^D\) for fixed \(D>0\). The integer or prime cutoff is interpreted as \(p\le P\). The same notation \(W_P\) now denotes the statistic of this actual weighted draw. [Exact weights and both signs](finite_moment63_uniform_prime_blocks.md#uniform-entry-estimates) · [Gonek, Corollary 1](../../sources/classical63_lfunctions/gonek1984.pdf)

The uniform theorem uses \(e_m=m^{-s}\), \(Q_p=p e_p-1=\sqrt p\,U_p-1\), and the covariance of \(Z_p=Q_p/\sqrt{p-1}\). Its conclusion is \(\|\operatorname{Cov}_{Y}(Z)-I\|_{\rm op}=O_D((\log(2P))^2/L)=o(1)\). The same theorem with \(m=p,n=1\) gives \(\mathbb E_Y Q_p=O_D(\log(2P)/L)\) uniformly. Therefore
\[
 W_P-H_P=\Re\sum_{p\le P}c_p Z_p,\qquad c_p=\frac{\sqrt{p-1}}p,\qquad
 \|c\|_2^2=\sum_{p\le P}(1/p-1/p^2)\le H_P .
\]
This identity gives \(\mathbb E_Y W_P-H_P=O_D(H_P\log(2P)/L)\) and \(\operatorname{Var}_Y W_P\le(1+o(1))H_P\), using the complex squared norm as an upper bound for its real part. Since \(H_P\ll\log(2P)\), the mean error also satisfies the requested \(O_D((\log(2P))^2/L)\) bound. For every fixed \(\varepsilon>0\), Chebyshev gives
\[
 \mathbb P_Y(|W_P/H_P-1|>\varepsilon)\ll_{D,\varepsilon} H_P^{-1}.
\]
For the particular real statistic \(W_P\), reflection preserves its value at every ordinate. Normalizing the restriction to positive ordinates yields exactly the same distribution of \(W_P\). An analogous assertion for arbitrary complex character tests would need the one-sided version of the analytic input. [Second-moment and centering bounds](uniform64_hlz_third_review.md#strict-tails-and-dimension-control)

## Gaussian fluctuation at the same cutoff

Let \(V_P=\frac12\sum_{p\le P}(1/p-1/p^2)\sim H_P/2\). Under \(\mu_*\), the centered increments \(X_p=p^{-1/2}(\Re U_p-p^{-1/2})\) are independent and bounded in absolute value by 2. Since \(V_P\to\infty\), Lindeberg's condition holds and \((W_P-H_P)/\sqrt{V_P}\) tends in law to the standard normal. All its fixed moments converge as well. To control absolute moments, each \(X_p\) has mean zero and range of length \(2p^{-1/2}\). The second derivative of its log moment generating function at any real argument is the variance under an exponential tilt, at most \(1/p\) by the range bound. Integrating twice gives \(\mathbb E_*e^{t(W_P-H_P)}\le e^{t^2H_P/2}\). The two-sided subgaussian tail gives uniform integrability at every fixed power after division by \(\sqrt{V_P}\), and also \(\mathbb E_*|W_P|^j\ll_j H_P^j\) for \(H_P\ge1\).

The arithmetic comparison needs the reduced-rational remainder of the uniform theorem. For fixed \(D'>0\) and \(B>0\) it states, on the full range \(m,n\le L^{D'}\), that
\[
 \left|\mathbb E_Y e^{-i\gamma\log(m/n)}
           -\frac{g}{\sqrt{mn}}\right|
 \ll_{D',B}\frac{g}{\sqrt{mn}}\frac{\log(mn/g^2)}{L}
           +\frac{L^{-B}}{\sqrt{mn}},\qquad g=\gcd(m,n).
\]
This follows by dividing (1) of the uniform note by \(\sqrt{mn}\), as its left-hand term then converts into the character expectation. The main coefficient agrees with the Poisson product and is nonnegative. For a fixed nonnegative integer \(j\), expand the *raw* power
\[
 W_P^j=\left(\sum_{p\le P}
          \frac{U_p+U_p^{-1}}{2\sqrt p}\right)^j.
\]
Every Fourier coefficient in this expansion is nonnegative, even for odd \(j\). Each resulting frequency has \(m,n\le P^j\), allowing \(D'=Dj\) for \(j\ge1\), and \(\log(mn/g^2)\le j\log P\) by construction. The \(j=0\) expectation agrees exactly. The sum of the expansion's coefficients is \((\sum_{p\le P}p^{-1/2})^j\le(2\sqrt P)^j\). Consequently, for \(j\ge1\),
\[
 |\mathbb E_Y W_P^j-\mathbb E_*W_P^j|
 \ll_{Dj,B,j}\frac{\log(2P)}{L}\,\mathbb E_* W_P^j
             +L^{-B}(2\sqrt P)^j.
\]
The first term uses the positivity before centering, and the model expectation here is a sum of nonnegative Fourier contributions. A bare uniform absolute Fourier error would lose the factor \(g/\sqrt{mn}\) and would fail to give this bound for arbitrary fixed \(D,j\).

Fix an integer \(k\ge1\) and take \(D'=Dk\), \(B>Dk/2+2\) for all \(j\le k\). After binomially centering both moments at \(H_P\), the difference is at most
\[
 O_{D,k,B}\!\left(\frac{H_P^k\log(2P)}{L}
          + L^{-B}(2\sqrt P)^k (1+H_P)^k\right).
\]
After division by \(V_P^{k/2}\) both terms tend to zero, since \(H_P\ll\log(2P)=O_D(\log L)\). Thus the arithmetic normalization has all fixed moments converging to the Gaussian ones. The second moment gives tightness. Higher even moments give the uniform integrability needed to identify subsequential moments. The normal law is moment-determinate, since its moment-generating function is finite near zero. It follows that
\[
 \boxed{\frac{W_P-H_P}{\sqrt{V_P}}\ \Rightarrow\ N(0,1)
              \quad\text{under }\mathbb P_Y,\qquad P=(\log Y)^D,\quad D>0.}
\]
In particular \(\operatorname{Var}_Y W_P\sim V_P\), which the complex covariance operator alone need not give for a real part. The proof chooses \(B\) after the fixed moment order \(k\) and fixed cutoff exponent \(D\). It gives no growing-order moment bound or effective onset height. It concerns the law of one weighted ordinate and does not determine unweighted counts or joint statistics of neighboring ordinates. [Refined uniform theorem and analytic provenance](finite_moment63_uniform_prime_blocks.md) · [Published Heap–Li–Zhao, Theorem 5 and (24)](../../sources/classical63_derivative_moments/hlz2022print.pdf)

## Checks and next test

An exact finite-block calculation on primes \(2,3,5,7\) enumerated the signed Fourier words through order four and matched an independent multinomial recursion from the one-prime moments. For a word with counts \(a_p,b_p\) of the two signs, the contribution after multiplying by its Poisson Fourier expectation is the rational number \(2^{-j}\prod_p p^{-\max(a_p,b_p)}\). The check gives \(H_P=247/210\), \(V_P=33281/88200\), and raw second moment \(155299/88200\). All words had numerator and denominator at most \(7^j\), before or after reduction.

A numerical comparison on actual zeros would use the exact two-sign weights and \(B_Y\), with finite truncation errors bounded separately for the weighted moment numerator and its untwisted denominator. At fixed \(P\), the absolute tail numerator error beyond a numerical cutoff \(T\) is at most \((2\sqrt P)^j B_T\). An existing effective tail bound for the \(Q_2\)-weighted tail also bounds \(B_T\) after division by \((\sqrt2-1)^2\), because \(|Q_2|^2\ge(\sqrt2-1)^2\) at every critical-line ordinate. The coarse resulting margin can be propagated through both numerator and denominator before comparing to the model. No finite-height Gaussian fit or publication priority claim is made here. [Effective tail certificate](prime64_sharper_moments.md)
