# One real derivative per order for the native 5:3 detector

Use the genuine Laplace transform \(F(z)=[6+P(1/2+z)/\zeta(1/2+z)]/z^2\) and the affine coefficients \(A,B\) from [the detector calculation](detector-nov18.md). For an integer \(k\ge1\) and real rate \(s>1/2\), put
\[
 M_k(s)=\frac{s^k(-1)^{k-1}}{(k-1)!}F^{(k-1)}(s)
       =\mathbb E\,w(V),\qquad V\sim\operatorname{Gamma}(k,\text{rate }s).
\]
This is a single real derivative in the absolute-convergence half-plane. In the primitive Möbius coefficients \(q(n)\) it equals
\[
 \frac1s\sum_{n\ge1}q(n)n^{-1/2-s}
     \sum_{j=0}^{k-1}(k-j)\frac{(s\log n)^j}{j!},
\]
by integrating each hinge against the Erlang density.

For **every** nondecreasing sequence \(s_k>1/2\) tending to infinity with \(u_k=k/s_k\to\infty\), each sign satisfies
\[
 \limsup_{k\to\infty}\frac{\log(1+M_k(s_k)_\pm)}{u_k}
 =\theta,\qquad \theta=\sup_\rho\Re\rho-1/2.                    \tag{1}
\]
In particular subexponential diagonal negative parts already imply RH. For the specific integer schedule \(s_k=2+\lfloor\log_2 k\rfloor\), there is a sharper equivalence: RH holds **if and only if** \(M_k(s_k)>0\) for every sufficiently large \(k\), equivalently for every integer \(k\ge1\) by the finite replay and the uniform estimate below. In this schedule the finite real-derivative signs have been certified over the range specified below.

## Positive rate refinement and the converse

For fixed initial \(s>1/2\), take \(V\sim\operatorname{Gamma}(k,s)\). Conditional on \(V\), run a Poisson process of intensity \(V\) on the rate interval \([s,\infty)\) and put \(K_r=k+N_{r-s}\). The posterior given the points up to \(r\) is \(\operatorname{Gamma}(K_r,r)\): its density is the prior times \(V^{K_r-k}e^{-(r-s)V}\), up to normalization. Thus \(M_{K_r}(r)\) is a uniformly integrable conditional-expectation martingale. Equivalently, refinement from \(s\) to \(r>s\) uses the nonnegative negative-binomial weights \(\binom{k+j-1}{j}(s/r)^k(1-s/r)^j\) on \(M_{k+j}(r)\).

If \(s\le s_k\), stop at the first \(R\ge s\) with \(R\ge s_{K_R}\). The monotone target rates jump only upward, while the running rate moves continuously between Poisson jumps. A Poisson jump at one of the deterministic boundary values has probability zero, so \(R=s_{K_R}\) almost surely. Conditional on \(V\), \(K_r/r\to V>0\); hence \(s_{K_r}/r\to0\) and the stop is finite. Optional stopping gives exactly
\[
 M_k(s)=\mathbb E M_{K_R}(s_{K_R}),\qquad K_R\ge k.           \tag{2}
\]
The same argument applies to any extra row \(C e^{dv}\) on \(v\ge0\) when \(s>d\). In particular, nonnegative diagonal moments in all sufficiently large orders imply eventual nonnegative Taylor coefficients of the corresponding transform at **each fixed rate** \(s\) in the absolute-convergence half-plane.

For the upper bound in (1), \(|w(v)|\ll_b e^{bv}\) for each \(b>\theta\) by [shifted inversion](detector-positive-isolation-nov18.md). Consequently \(|M_k(s_k)|\ll_b(1-b/s_k)^{-k}\) for large \(k\). For the lower bound, if one sign had upper exponent less than \(\theta\), choose \(d>0\) strictly between it and \(\theta\), and choose the sign of \(w\) for which these small parts are negative. The modified row \(\pm w(v)+Ce^{dv}\) has nonnegative diagonal moments eventually: \((1-d/s_k)^{-k}\ge e^{du_k}\). Its transform \(\pm F(z)+C/(z-d)\) continues holomorphically along the real interval \((d,\infty)\). But choose a genuine off-line pole \(z_0=a+i\gamma\) with \(a>d\), and a fixed sufficiently large \(s\) that \(|s-z_0|<s-d\). The Taylor series at zero of \(\pm F(s-z)+C/(s-z-d)\) has finite radius at most \(|s-z_0|\), with eventually nonnegative coefficients by (2). Pringsheim's theorem, after deleting a finite initial polynomial, requires a singular point at its positive real radius. This contradicts real-axis regularity. The lower bound for \(\theta=0\) is immediate. The argument with unmodified row gives the eventual-sign converse as well.

## A uniform finite zero-census estimate for all higher derivatives

The following bound is valid under a finite RH census to height \(H\ge20000\), with the known first ordinate above 14; simplicity is unnecessary. For real \(50\le s\le H^2-2\) and integer \(k\ge8000s^4\log(2s)\),
\[
 |M_k(s)-Ak/s-B|<1.                                          \tag{3}
\]
Under global RH the upper restriction on \(s\) disappears. For \(s=s_k=2+\lfloor\log_2 k\rfloor\), one has \(k\ge2^{s-2}\ge8000s^4\log(2s)\) at \(s=50\) and thereafter, by monotonicity of the ratio. This proves the forward eventual-sign implication.

For detail put \(r=\sqrt{s^2+1}\), \(D(z)=F(z)-A/z^2-B/z\), and take the circle \(|z-s|=r\). Every shifted nontrivial zero \(d=\rho-1/2\) has \(|s-d|^2\ge s^2+2\): for \(\Re d\le0\) use \(|\Im d|>14\); for \(\Re d>0\) use \(|\Im d|>H\), \(2\Re d<1\) and \(s\le H^2-2\). Under RH only the first case is needed. The trivial zeros and the removed affine singularity cause no pole of \(D\) in the disk. The entire centered xi product, pairing \(\pm d\), reads
\[
 \xi(1/2+z)=\xi(1/2)\prod_{\{d,-d\}}(1-z^2/d^2).
\]
The unconditional estimate \(\sum_d |d|^{-2}<1\) follows from \(\sum_\rho \Re(1/\rho)=1+\gamma_E/2-\log(2\sqrt\pi)<0.1\): pair \(\beta+i\gamma\) with \(1-\beta+i\gamma\) to get \(\sum_\rho(1+\gamma^2)^{-1}\le2\sum\Re(1/\rho)\), then use \(|\gamma|>14\). For \(|d|\le4s+4\) the distance from both \(\pm d\) to the circle is at least \(1/(8s)\) by the squared-radius gap. There are at most \(25s^2\) such roots, and each reciprocal product factor costs at most \(1600s^4\). For the remaining pairs, \(|z|\le2s+1\) and \(|z|/|d|<1/2\); their total reciprocal log cost is at most \(2|z|^2\sum |d|^{-2}\). These estimates imply the convenient crude bound
\[
 \max_{|z-s|=r}|D(z)|\le \exp(1000s^2\log(2s)).
\]
Indeed \(|\xi(1/2)|>0.4\) by the interval checker. The gamma prefactor in \(1/\zeta(1/2+z)\) costs less than \(\exp(10s\log(2s))\): the real part of its gamma argument lies between \(1/5\) and \(s+1\), so split the gamma integral at 1 to bound its absolute value by \(5+\lceil s+1\rceil!\). The two rational factors, the powers of \(\pi\), \(|P|<20\), \(|z|\ge1/(3s)\), and \(|A|,|B|<10\) are absorbed by the displayed large constant. The same checker encloses the affine coefficients. Cauchy's coefficient estimate now costs at most
\[
 s(s/r)^{k-1}\exp(1000s^2\log(2s))<1
\]
under (3), since \(\log(r/s)\ge1/(4s^2)\). This proves the estimate.

## Reproduced prefix

The [python-flint interval checker](check_detector_gamma_nov18.py) evaluates all 63 initial real derivatives at 160 bits, with the Taylor-series cap increased to the full order of each block. For integer \(8\le s\le49\) it encloses \(D\) on every point of the circle of radius \(r=\min(s+2,\sqrt{s^2+100})\) about \(s\). The circles enclose no unremoved pole: the real left edge stays above \(-2.5\), the critical ordinate threshold exceeds 14, and an off-line zero would have to lie above the verified census. At \(k_0=2^{s-2}\) the checker requires the Cauchy error \(s(s/r)^{k_0-1}\max|D|\) strictly below \(Ak_0/s+B-1\). The error decreases and the affine lower bound increases for every later order in the block. The replay accepted 20252 circular interval boxes. With (3) this proves \(M_k(s_k)>0\) for all \(2+\lfloor\log_2 k\rfloor\le H^2-2\). The local zero replay permits \(H=20000\); the [Platt–Trudgian census](https://arxiv.org/abs/2004.09765) permits \(H=3\cdot10^{12}\). This very large finite-order coverage follows from the slow growth of the chosen rates and does not prove their cofinal signs.

## Every proportional block of diagonal centers

In fact for every fixed \(0\le r<1\),
\[
 \lim_{T\to\infty}\frac1T\log\!\left(1+
    \sup_{rT\le u_k\le T}M_k(s_k)_\pm\right)=\theta.          \tag{4}
\]
One can take the supremum of an empty set of nonnegative values to be zero. The statement holds even if the centers \(u_k\) move backwards at jumps of the monotone rates.

For a fixed sufficiently large rate \(s\) when \(\theta>0\), the closest pole of \(F\) to \(s\) has distance \(R_s<s\). The minimum is over a finite nonempty set of shifted off-line zeros: for any fixed \(a+i\gamma\) in the right half-plane, \(|s-a-i\gamma|<s\) eventually. Write \(\lambda_s=s\log(s/R_s)>0\). Testing fixed zeros and using \(R_s\ge s-\theta\) show \(\lambda_s\to\theta\) as \(s\to\infty\). At the closest poles of largest multiplicity the Taylor-coefficient expansion has a nonzero real trigonometric polynomial in the integer index \(k\), times a positive constant scale \((s/R_s)^k k^{m-1}\), up to a relatively \(o(1)\) additive error before taking signs. This is ordinary partial-fraction extraction on a slightly larger pole-free circle, after removing all nearest principal parts. The phases are the distinct arguments of the nearest conjugate poles relative to \(s\), modulo \(2\pi\), and none is zero. Their first and second discrete means over length-\(L\) intervals converge uniformly in the initial index to zero and a strictly positive value, respectively. Thus both signs have peaks \(\gg_s e^{\lambda_s k/s}\) in every sufficiently long fixed block of orders. In particular the infimum of rates with infinitely many strictly negative derivatives (in the alternating normalization) is
\[
 \inf_{\rho=1/2+a+i\gamma,\ a>0}\frac{a^2+\gamma^2}{2a},
\]
with infinity if there is no off-line zero. Below this number the affine pole at zero is uniquely closest and gives eventual strict positivity. Behavior at a finite equality is unnecessary for the infimum.

In (2) the stopped center \(Y=K_R/R\) equals \(\mathbb E[V\mid\mathcal F_R]\). For \(0<\eta<1/4\), conditional Jensen and the gamma exponential moment give
\[
 \mathbb P(|Y-k/s|>\eta k/s)\le 2e^{-c\eta^2k}
\]
with absolute \(c>0\), by applying the Chernoff bound to \(e^{tY}\) at the two optimizing rates for a gamma variable. On the stop \(R\ge s\), the native subexponential bound gives \(|M_{K_R}(R)|\ll_b\exp(b_sY)\) for \(b>\theta\), \(b_s=-s\log(1-b/s)\), provided \(s>b\). A second conditional Jensen bound on \(e^{2b_sY}\) and Cauchy–Schwarz show that the exceptional part of (2) is at most a constant times
\[
 \exp\!left[\left(-\tfrac{s}{2}\log(1-2b_s/s)-\tfrac{c\eta^2s}{2}\right)k/s\right].
\]
For fixed \(b,\eta\) this exponent is negative at sufficiently large \(s\). For each large \(T\) take a fixed-rate peak of the desired sign with \(k/s=(1-2\eta)T+O_s(1)\). Then \(s_k\ge s\) eventually and (2) forces a diagonal peak of comparable magnitude with \(|Y-k/s|\le\eta k/s\). Choosing \(\eta\) small in terms of \(r\) places it inside the interval in (4). Let \(s\to\infty\) and then \(\eta\downarrow0\). This proves the lower exponent; the upper bound was shown for (1).
