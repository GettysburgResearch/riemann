# What the two actual abundance tails control unconditionally

Let \(A_\phi(t)\) and \(A_\sigma(t)\) be the respective limiting densities of \(n/\phi(n)\ge t\) and \(\sigma(n)/n\ge t\), and \(y=\exp(te^{-\gamma_E})\). Then, unconditionally,
\[
 \log\frac{A_\phi(t)}{A_\sigma(t)}\sim 2\sqrt2\,\sqrt y .
\]
Indeed, at \(u=\log t\) let \(s_\phi,s_\sigma\) be the true tilted saddles. Both satisfy \(s_j\sim y\log y\) by the unconditional derivative calibration. The difference of the two Legendre minima lies between \((W_\phi-W_\sigma)(s_\phi)\) and \((W_\phi-W_\sigma)(s_\sigma)\), by using each minimizer as a trial point for the other function. Both endpoints are asymptotic to \(2\sqrt2\sqrt y\) by [the prime-square calculation](abundance-curvature-sigma-nov18.md). The [exact saddle formula](abundance-exact-saddle-nov18.md) converts the two minima to log tails; their common logarithmic prefactor cancels up to \(o(1)\). In Weingartner's original notation these are \(B(t)\) and \(A(t)\), respectively. [Weingartner, Theorems 1–3](https://arxiv.org/abs/1011.4262)

For the common deterministic centering in [the curvature criterion](abundance-curvature-nov18.md), this implies
\[
 \max(\mathcal E_\phi(t),-\mathcal E_\sigma(t))
 \ge (\sqrt2+o(1))\sqrt y
\]
at *every* large threshold. The ordering fixes the difference of the residuals and leaves their common displacement free. This statement has no fixed choice of the sign that attains the bound.

## The continuous prime comparator is not a probability cumulant

The proposed continuous function
\[
 W_0(z)=\int_2^\infty \log g(v,z)\frac{dv}{\log v},\qquad
 g(v,z)=\frac{v-1+e^{zb(v)}}v,\qquad b(v)=-\log(1-1/v)
\]
is real analytic and finite at every real \(z\). Nevertheless \(\exp(W_0(z)+cz)\) cannot be the moment-generating function of a real random variable, for any real translation \(c\). Thus a stochastic sandwich placing such a variable between the two actual log abundances is unavailable.

To see this, take \(z_0=i\pi/\log2\). On \(\Re z<0\) all factors have positive real part for \(v\ge2\), so choose the branch continuous from the real axis. At \((2,z_0)\), \(g=0\), while
\[
 a=g_v(2,z_0)=(1+z_0/2)/2,\qquad b_0=g_z(2,z_0)=-\log2/2 .
\]
Approach along \(z=z_0-r\) with \(r>0\). For \(t=v-2\) near zero, \(g=a t-b_0r+O((t+r)^2)\); the linear part has modulus comparable to \(t+r\), since \(\Re a>0\) and \(-b_0>0\). All factors \(v\ge2+\delta\) stay away from zero locally and the differentiated integral there is holomorphic, by the \(O(v^{-2})\) bound on compact \(z\)-sets at infinity. On the initial segment the derivative integrand is
\[
 \frac{b_0}{\log2}\frac1{a t-b_0r}+O(1).
\]
Consequently \(W_0'(z_0-r)=-(b_0/(a\log2))\log r+O(1)\), which diverges in modulus. The undifferentiated logarithm is integrably dominated by \(C+|\log t|\), so \(\exp(W_0(z_0-r)+c(z_0-r))\) tends to a finite nonzero value. Its derivative therefore diverges too. This rules out a holomorphic extension through \(z_0\).

Any law with finite exponential moments at every real argument has an entire moment-generating function by compact domination. In fact equality merely on one open real interval of finite moments would force all real moments here: separate the positive and negative tails of the law. At a finite endpoint of the interval of convergence the opposite tail is holomorphic, while the nonnegative tail reaching its abscissa must have a real singularity by Landau's theorem. The proposed expression continues holomorphically locally along the whole real line, precluding such an endpoint. Equality on the negative half-plane by analytic continuation would then contradict the endpoint calculation. This obstruction concerns stochastic interpretation; it does not by itself give an inequality for the real log moments.

There is a real-derivative witness at every fixed nonzero real rate \(s\): infinitely many **even** derivatives of \(M_*(s)=\exp(W_0(s)+cs)\) are negative. All even derivatives of a genuine moment-generating function at an interior rate would be nonnegative. Indeed the defining integrand continues on the entire horizontal strip \(|\Im z|<\pi/\log2\), since a zero requires \(|\Im z|b(v)\ge\pi\); the local logarithms patch from the real line. On either boundary line the only obstructing endpoint is \(\pm z_0\) with real part zero. At any other point on the line the local factors have no zero for real \(v\ge2\), and the integrals are locally holomorphic. Hence the even Taylor part \((M_*(s+z)+M_*(s-z))/2\) has a finite complex singularity at \(z=z_0-s\): the reflected argument \(2s-z_0\) is regular for \(s\ne0\), so it cannot cancel the singularity. The Taylor germ is nevertheless regular by continuation at every real argument. Pringsheim's theorem precludes eventually nonnegative coefficients, after removing finitely many terms. The odd coefficients vanish identically; the offending coefficients are therefore even derivatives.

## A genuine quantile-prime law with the same asymptotic comparator

Despite the exact obstruction, an explicit probability law matches the comparator to every inverse-power order up to a fixed additive constant in its logarithm. Let
\[
 a(v)=\int_2^v\frac{dt}{\log t},\quad v(y)=a^{-1}(y),\quad
 q_j=v(j+1/2),\quad j=0,1,\ldots .
\]
Use independent Bernoulli variables \(J_j\) of probabilities \(1/q_j\), and for a function \(g\) define its composite midpoint error
\[
 Q(g)=\sum_{j\ge0}\left[g(q_j)-\int_j^{j+1}g(v(y))dy\right]
\]
whenever the cell errors converge. Set \(d=c-Q(b)\), \(C_q=-Q(\log)\), and \(X_q=d+\sum b(q_j)J_j\). Both constants are finite: \(b\) has finite variation and \((\log v(y))''=(1-\log v)\log v/v^2\) is integrable in \(y\), giving summable midpoint errors. Also \(\sum b(q_j)/q_j<\infty\), so the random series converges almost surely and its moment generating function exists at every real order. Then, for every \(A>0\),
\[
 W_q(s):=\log\mathbb E e^{sX_q}
     =W_*(s)+C_q+O_A(s^{-A})\quad(s\to\infty).                 \tag{1}
\]

For proof write \(f_s(v)=\log(1+(e^{sb(v)}-1)/v)\) and \(g_s(v)=sb(v)-f_s(v)\). The difference after linear centering is exactly \(-Q(g_s)\). The saturation remainder
\[
 j_s(v)=g_s(v)-\log v=-\log(1+(v-1)e^{-sb(v)})
\]
has \(Q(j_s)=O_A(s^{-A})\). Here are details allowing arbitrary fixed order. In the coordinate \(y\), differentiation is \(D=(\log v)\partial_v\). For \(z=\log(v-1)-sb(v)\) and \(k\ge1\),
\[
 |D^k z|\ll_k (1+s/v)((1+\log v)/v)^k\qquad(v\ge2).
\]
This follows by differentiating \(\log(v-1)\) and \(b(v)\) and expanding \(D^k\). All positive-order real derivatives of the softplus function \(\log(1+e^z)\) are bounded, and are \(O_k(e^z)\) when \(z\le0\). The chain rule therefore gives, for fixed \(r\ge2\),
\[
 |D^r j_s(v)|\ll_r \min(1,ve^{-s/v})(1+s/v)^r
                         ((1+\log v)/v)^r.
\]
Split its \(dy\)-integral at \(V=s/(B\log s)\). Below \(V\) it is \(O_r(s^{r+2-B})\), and above \(V\) it is \(O_{r,B}(s^{1-r}(\log s)^{3r-2})\). Choose \(r>A+2\) and then \(B>A+r+3\). The derivatives at \(y=0\) of positive orders up to \(r\) are \(O_r((1+s)^r2^{-s})\); at infinity every such derivative tends to zero. Apply midpoint Euler–Maclaurin to the first \(N\) cells and let \(N\to\infty\). Its order-zero endpoint term vanishes because \(B_1(1/2)=0\); the remaining boundary derivatives and the periodic-Bernoulli remainder bounded by \(O_r(\int |D^rj_s|dy)\) give the claim. Thus \(-Q(g_s)=-Q(\log)+O_A(s^{-A})\), proving (1).

This law gives a genuine eventual stochastic comparison criterion. Write \(A_q(t)=\Pr(e^{X_q}\ge t)\). Then
\[
 \log A_q(t)=I_*(\log t)+C_q-\tfrac12\log(2\pi y)+o(1).
\]
To check the tilted saddle argument anew, \(\#\{j:q_j\le v\}=a(v)+O(1)\). Consequently each bounded-variation prime-to-integral replacement in the [totient tilted saddle](abundance-exact-saddle-nov18.md) has error at most its total variation plus an endpoint term. The variance shell and its characteristic factor estimates therefore apply to these independent Bernoulli variables with the same leading constants. For the derivative anchor the sum of \(b(q_j)\) up to \(x\) differs from its integral plus \(Q(b)\) by \(O(1/x)\): the incomplete cell costs \(O(1/x)\), and the subsequent cell errors are bounded by the remaining variation of \(b\). The translation \(d\) puts the anchor at \(\gamma_E+\log\log x+o((\log x)^{-2})\). Thus the true proxy saddle has \(x/y\to1\), while the established small-frequency and compact-frequency bounds and uniform unit-interval argument give the same prefactor \((2\pi y)^{-1/2}\). Comparing Legendre minima at their two minimizers, both tending to infinity, then transfers (1) with its constant unchanged.

It follows that each of the assertions \(A_\phi(t)\ge A_q(t)\) eventually and \(A_\sigma(t)\le A_q(t)\) eventually is equivalent to RH. On RH the critical profiles have the required strict signs of size \(\gg\sqrt y\). Off RH each opposite excursion of the Weingartner residual has upper exponent \(\Theta>1/2\), and the proxy changes its centering by only \(O(\log y)\). This criterion uses three actual probability laws. It concerns sufficiently large thresholds, without claiming global stochastic domination down to their lower endpoints.

A componentwise coupling of the primes cannot supply this sandwich. The momentary counting difference between the true primes and the midpoint quantiles is \(\pi(v)-a(v)+O(1)\), unbounded in both directions by Littlewood's oscillation theorem for \(\pi-\operatorname{li}\). This rules out any injection matching each actual prime to a smaller quantile, and also any injection matching each quantile to a smaller actual prime, even after finitely many exceptions. Such an order is necessary for coordinatewise stochastic comparison of the occupied totient scores: their success probabilities and their largest scores both decrease strictly with the prime parameter. It is also necessary when asking that each divisor-sum local score be bounded stochastically by its assigned quantile score, already by comparison of their essential suprema. This rules out a coordinatewise route; it leaves open the comparison of the full sums required by the criterion.

## A finite sandwich of the three probability laws

Throughout \(1100\le\ell=t e^{-\gamma_E}\le4{,}369{,}179\) one has the strict genuine-tail comparison
\[
 A_\sigma(t)<A_q(t)<A_\phi(t).
\]
For all \(1000\le L\le4{,}369{,}185\), the [height filter and zero-free bound](abundance-wrong-sign-nov18.md) exclude every right zero satisfying its displayed necessary threshold. The same proof bounds the normalized absolute right-zero sum by \(0.616\) plus the negligible connector. Together with the small archimedean term, the non-right-zero bound \(0.081\), and the prime-square margins, it gives
\[
 W_\phi-W_*>1.25\sqrt x,\qquad W_\sigma-W_*<-0.08\sqrt x .
\]
These deliberately reduced margins apply at the last endpoint as well.

For the proxy the elementary estimate \(|W_q(s)-W_*(s)|\le2\log(2s)\) holds at \(s\ge2\). Indeed \(|Q(g_s)|\) is at most the total variation of \(g_s\), and this nonnegative function first increases and then decreases, or only decreases on the truncated range. In \(u=\log v\) its derivative has the sign of \(1-(s+1)(1-e^{-u})^s\). At its possible maximum \(v=(1-e^{-\log(s+1)/s})^{-1}\le1+s/\log(s+1)\le2s\), and \(g_s(v)\le\log v\). At the left endpoint the same bound holds. Also \(|W_q'(xL)-W_*'(xL)|<6/x\). Apply the variation estimate to \(\partial_s g_s(v)=b(v)r(v)\), where \(r=(v-1)e^{-sb}/(1+(v-1)e^{-sb})\) increases in \(v\). Up to \(x/2\), \(r\le1/(2x)\), so the product variation is at most \((\log2)/x\). Beyond \(x/2\), \(b(x/2)<2.01/x\) and the cost is at most twice this. The [effective deterministic derivative bound](abundance-weingartner-model-nov18.md) and its explicit endpoint margins put the unique proxy saddle \(s_q=x_q\log x_q\) in \(J_y\), like \(s_*\). In particular \(|\log x_q-\ell|,|\log x_*-\ell|\le2/\ell\).

The Berry–Esseen argument from the [finite actual saddle](abundance-finite-horizon-nov18.md) applies to the proxy with the following constants at \(s=xL\), \(L\ge1000\):
\[
 0.01/(xL^2)<V_q<13/x,\qquad
 \sum_j\mathbb E_s|X_j-\mathbb E_s X_j|^3<40/x^2 .
\]
Here \(X_j=b(q_j)J_j\); the deterministic translation does not change centered moments. The shell \([x,x(1+1/(10L))]\) contains at least \(0.09x/L^2\) quantiles by its integral length and counting error at most two. Its Bernoulli variance factor exceeds 0.2 and \(b(q_j)>0.99/x\). For the upper bounds, the quantile spacing is at least \(\log2\). Below \(x/2\) use the variance factor \(\le q_j/x^2\), and above use \(b(q_j)\le2/q_j\). In the first range the variance costs at most \(4x^{-2}\sum_{q_j\le x/2}q_j^{-1}<1/x\) by the spacing, and the third-moment cost is below \(8x^{-2}\sum q_j^{-2}<8/x^2\). Above the cutoff use \(\sum_{q_j\ge z}q_j^{-k}\le z^{-k}+z^{1-k}/((k-1)\log2)\), \(k=2,3\). These prove the constants. In particular the Kolmogorov error is below \(4\cdot10^6 L^3/\sqrt x\), even allowing a universal Berry–Esseen constant 100. At its true tilted mean the normal interval \([0,0.01/L]\) has mass above \(0.0039/L\), so the tilted interval has mass above \(0.003/L\).

Consequently the true proxy log tail is at least
\[
 I_*(\log t)-2\log(2s_q)-0.037\sqrt{x_q}-\log(334\log x_q)
 >I_*(\log t)-0.04\sqrt{x_*}.
\]
Exponential Markov at the model saddle gives the upper bound \(I_*(\log t)+2\log(2s_*)\). For the actual divisor sum, Markov at that same saddle gives a strict upper bound below \(I_*(\log t)-0.08\sqrt{x_*}\). For the actual totient law the explicit lower tilt in the finite sign theorem gives at least \(I_*(\log t)+(1.25-0.34)\sqrt{x_\phi}-\log(50\log x_\phi)\), which exceeds the proxy upper bound because \(|\log x_\phi-\ell|<6\). This proves the comparison without using a limiting asymptotic to certify a finite interval.

## Full stochastic domination fails near the lower endpoint

For this same explicitly centered midpoint proxy, \(d<-0.003\), so \(\Pr(X_q<0)>0\). Indeed set all the first finitely many Bernoulli components to zero, an event of positive probability, and choose that cutoff so the expectation of the remaining positive sum is less than \(-d/4\). Independence and Markov give a positive probability of a total below \(-d/2\). The actual divisor-sum log ratio is strictly positive almost surely: the probability of no occupied prime is \(\prod_p(1-1/p)=0\). It follows that \(A_\sigma(t)>A_q(t)\) for all \(t>1\) sufficiently close to 1. In particular an unrestricted stochastic coupling of the complete variables cannot prove the eventual sandwich, even under RH.

For the drift estimate, \(b(v(y))\) is convex, with first derivative \(-\log v/[v(v-1)]\) increasing to zero. The midpoint Peano kernel on a unit cell is bounded by \(1/8\); this follows by integrating the first-order Taylor remainder about the midpoint on each half. Beyond the first cell the total absolute quadrature error is at most \(\log v(1)/(8v(1)(v(1)-1))\). In the integral defining \(c\), expand \(b(v)-1/v\) and integrate the positive terms to obtain \(\sum_{m\ge1} E_1(m\log2)/(m+1)\). The [128-bit drift replay](check_abundance_quantile_drift_nov18.py) retains the first twelve positive terms, brackets the needed first-cell quantiles by real logarithmic integrals, and uses a 2048-cell upper Darboux sum for that single integral. The resulting upper bound for \(d\) is \(-0.00359041750589989141092479373337778\) with printed radius \(6.36\cdot10^{-36}\).
