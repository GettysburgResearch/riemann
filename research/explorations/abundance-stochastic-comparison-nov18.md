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
