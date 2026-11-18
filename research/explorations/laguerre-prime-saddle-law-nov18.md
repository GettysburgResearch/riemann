# The positive prime saddle of the Laguerre detector

Write $D_n=L_n^{(-1)}$, $A_n=3\,2^{n-1}$ and $v=\log x$. On $v\ge4n/3$ put
$$
 dP_n(v)=A_n^{-1}\sum_{p:\,\log p\ge4n/3}
  (\log p)p^{-2}(-1)^n D_n(3\log p)\delta_{\log p}(dv),\qquad
 dQ_n(v)=A_n^{-1}(-1)^ne^{-v}D_n(3v)\,dv .
$$
Both measures are positive by the largest Laguerre root bound in the [physical saddle analysis](laguerre-prime-energy-nov18.md). Set $\omega_n=n^{3/5}(\log(2+n))^{-1/5}$. Unconditionally,
$$
 \sup_{x\in\mathbb R}|(P_n-Q_n)((-\infty,x])|\ll e^{-c\omega_n}.
 \tag{1}
$$
More generally the same bound holds with the integrand $e^{-itv}$ on either measure and an extra factor $1+|t|$ on the right. Their common approximate mass is one. The centered and rescaled prime saddle $(v-(3n+1)/2)/\sqrt{(3n+5)/4}$ converges weakly to the standard normal. The first two cumulants below refer to the full signed continuum. The true probability-normalized prime mean and variance differ from them by $O(e^{-c'\omega_n})$.

**Prime versus continuum.** On the generating circle $|w|=1/2$ the maximum of $\Re(-w/(1-w))$ is $1/3$. Thus
$$
 |D_n(3v)|+|\partial_v D_n(3v)|\ll 2^n e^v.
$$
For $H(v)=e^{-2v}D_n(3v)e^{-itv}$ this gives $|H|+|H'|/(1+|t|)\ll 2^n e^{-v}$. In Stieltjes partial summation against $d(\vartheta(e^v)-e^v)$ the Vinogradov–Korobov prime number theorem bounds the cumulative discrepancy by $O(e^v\exp[-c v^{3/5}(\log v)^{-1/5}])$. The endpoint terms and integrated derivative on any subinterval of $v\ge4n/3$ yield (1), after slightly decreasing $c$. The same argument absorbs any fixed power of $v$ in the integrand.

**Continuum.** Extend $Q_n$ to all $v\ge0$ by its original signed formula. The removed portion has total variation $\ll e^{2n/3}/A_n$, since $|D_n(3v)|\le2e^{3v/2}$ by Fejér's bound. For every $u$ near zero, integrating the generating function gives the exact Laplace transform of this extension,
$$
 (1-u)^{-2}\left(\frac{1+u/2}{1-u}\right)^{n-1}.
 \tag{2}
$$
The first and second derivatives of its logarithm at zero give the stated mean and variance. At $u=is/\sqrt{(3n+5)/4}$, multiplying by the centering phase and expanding the logarithm gives $e^{-s^2/2}(1+O_s(n^{-1/2}))$. These conclusions transfer to the probability-normalized prime statistic by (1), its Fourier form, and its polynomially weighted version.

**Growing-frequency cancellation.** For the pole-subtracted prime coefficient $d_n(t)$ of the [fixed-center criterion](laguerre-prime-detection-nov18.md), the physical PNT proof gives
$$
 |d_n(t)| \ll (1+|t|)2^n e^{-c\omega_n}.
 \tag{3}
$$
On the omitted range the absolute prime sum is $\ll \sum_{p\le e^{4n/3}}(\log p)p^{-1/2}\ll e^{2n/3}$. On $v\le Cn$ all higher prime powers cost $O_C(n)$ by the same Fejér estimate. On $v>Cn$ use the coefficient circle $|w|=1/3$, giving $|D_n(3v)|\le 3^ne^{3v/4}$, and sum over all integers to obtain $O(3^n(1+Cn)e^{-Cn/4})$. Take, for example, $C=12$. This proves (3) for the full von Mangoldt source.

The native prime characteristic function therefore agrees with the explicit continuous characteristic function (2) to relative error $O(e^{-c'\omega_n})$ uniformly for $|t|\le c_0 n^{-1/5}(\log n)^{-1/10}$ with $c_0$ sufficiently small. Indeed its modulus is bounded below by $\exp(-C n t^2)$ there. In the normalized measures subexponential coefficient growth would require error at most $2^{-n+o(n)}$ for bounded $t$. The unconditional bound (1) quantifies the precision already supplied by the prime number theorem.

## A finite centered energy bound from the verified census

Let $U$ be an RH verification height, for instance $U=3\cdot10^{12}$ by Platt–Trudgian. For $|t|\le U/2$ the centered coefficient satisfies uniformly
$$
 |d_n(t)|\ll \log(2+|t|)+\frac{\log U}{U}\exp(6n/U^2),\qquad n\ge1.
 \tag{4}
$$
Indeed in the logarithmic derivative the contribution of a zero $\rho$ is
$$
 -\frac3{(2+it-\rho)^2}
 \left(\frac{\rho+1-it}{\rho-2-it}\right)^{n-1}.
$$
This also holds for the trivial zeros: the logarithmic derivative of the genus-one product of $(s-1)\zeta(s)$ differs from the regularized single-zero resolvent sum by a constant. Coefficients of positive order can be summed absolutely by the local count and normal convergence around $w=0$. The known pole has already been subtracted. The trivial-zero multipliers have modulus at most one and their squared-denominator sum is bounded. The weights of critical-line zeros total $O(\log(2+|t|))$ by unit-interval zero counting. All remaining zeros have $|\gamma|>U$, where the squared modulus of the multiplier equals $1+(6\beta-3)/[(2-\beta)^2+(\gamma-t)^2]$. Its $(n-1)/2$ power is at most $\exp(6n/U^2)$, and the remaining sum of weights is $O((\log U)/U)$, again by unit-interval counting. This proves (4).

Thus the actual centered arithmetic energy averaged on $[-T,T]$ is $O(\log^2(2+T))$ throughout $1\le T\le U/2$ and $n\le (U^2/6)\log(U/\log U)$. This finite regime substantially exceeds the range available by uncentered Dirichlet polynomial orthogonality. The constants in the bound are absolute and unevaluated.
