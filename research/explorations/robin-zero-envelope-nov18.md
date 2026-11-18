# The zero-free envelope seen by counts of Robin violations

Let \(V(N)\) count the integers \(5040<n\le N\) failing Robin's strict inequality. Let \(F(u)=\min(u/2,\inf_{\rho:\gamma>0}[(1-\beta)u+\log\gamma])\). If RH fails then
\[
 \liminf_{N\to\infty}\frac{\log(\log N/\log(2+V(N)))}{F(\tfrac12\log\log N)}=1. \tag{1}
\]
Thus, even if the supremum of the real parts is one, the best subsequential order of the count detects more than that abscissa. In this case the denominator is sublinear in \(\log\log N\). When \(1/2<\Theta<1\), the [earlier counting law](robin-violation-count-nov18.md) yields a limit in (1), since \(F(v)/v\to1-\Theta\).

## Uniform upper count when the supremum is one

Assume henceforth \(\Theta=1\). Put \(W(v)=2F(v/2)\), and write \(K(x)=\int_x^\infty(\vartheta(t)-t)t^{-2}(1/\log t+1/\log^2t)dt\). The [integrated explicit formula](robin-finite-horizon-nov18.md) gives, for large \(x=e^v\),
\[
 |K(x)|\ll x^{-1/2}+\sum_\rho e^{-(1-\beta)v}/(|\rho|\,|1-\rho|).
\]
Indeed changing \(\vartheta\) to \(\psi\) costs \(O(x^{-1/2})\). The zero integral in that formula is at most \(O(e^{-(1-\beta)v}/(v|1-\rho|))\) before the factor \(1/|\rho|\), by integration by parts or its positive Laplace-parameter representation. Ingham's density bound in a fixed strip near 1 and absolute convergence in its complement consequently give \(|K(x)|\ll_\epsilon e^{-(1-\epsilon)W(v)}\). The corresponding one-power formula gives \(|\vartheta(x)-x|\ll_\epsilon x\exp(-(1-\epsilon)F(v))\) as in the [Mertens mean proof](zhao-third-mertens-nov18.md).

For a violating \(n\), set \(y=\log n\), \(u=\log y\), \(f=F(u/2)\), \(z=y(1-e^{-(1-2\epsilon)f})\). The tangent identity bounds the total missing-prime cost below \(z\) by \(|K(y)|\). For \(P(z)=\prod_{p\le z}p\) and \(B=P(z)/\gcd(n,P(z))\), the elementary local-cost bound in the counting proof gives
\[
 \log B\le \frac{y\log y\,|K(y)|}{y/z-1}
 \ll_\epsilon y(\log y)e^{-f}.
\]
Also \(A=n/\gcd(n,P(z))\) satisfies \(\log A=y-\vartheta(z)+\log B\ll_\epsilon y\exp(-(1-3\epsilon)f)\). Here \(F(\log z)\ge F(u/2)\), \(f\gg\sqrt u\), and the factor \(\log y=u\) can be absorbed. There are at most \(1+\log N\) distinct primorials as \(n\le N\) varies. Since \(n=P(z)A/B\), counting pairs proves
\[
 \log(2+V(N))\ll_\epsilon (\log N)\exp(-(1-3\epsilon)F(\tfrac12\log\log N)).
\]
The upper envelope in \(y\) increases for large \(y\), since the slopes of \(F\) tend to zero. This proves that the limiting inferior in (1) is at least one.

## Lower count along a sequence

We first show that for every \(\epsilon>0\) there are arbitrarily large \(x=e^v\) with
\[
            -K(x)\ge \exp(-(1+\epsilon)W(v)). \tag{2}
\]
Here is the transfer of the [signed zero-isolation argument](zhao-shrinking-windows-nov18.md) to this particular kernel. Write \(G(v)=K(e^v)\), \(S(x)=\vartheta(x)-x\) and \(a(v)=v^2/(v+1)\). Since \(S(e^v)=-e^v a(v)G'(v)\) almost everywhere, every test supported in \(v>0\) satisfies
\[
 \int k(v)e^{-v}dS(e^v)=-\int [a(v)(k'(v)-k(v))]'G(v)dv.
\]
On the compact adaptive Gaussian window the source is interchangeable with the corresponding \(\psi(e^v)-e^v\) source at error \(e^{-u/2+b}u^{O(1)}\), by partial integration and the prime-power bound. The differential operator costs at most \(u^{O(1)}(1+\gamma)^2\) times the Gaussian, exactly as in the companion argument.

The nonmodulated *fixed-width-parameter* signed mean is exponentially small. To see this, apply the [LCM note's explicit formula](robin-lcm-nov18.md) to \(G(v)\), without its factor \(e^v\). Restrict the Gaussian centered at \(t\asymp u\), of variance \(2q_0t\), to \(|v-t|\le\delta t\), with fixed \(\delta>0\) and sufficiently small \(q_0>0\). For the \(\psi\) version its zero terms are Laplace-parameter integrals of \(e^{(\rho-1-s)v}(1+s)/[\rho(1-\rho+s)]\), \(s\ge0\). For \(s\ge1\) the integral is exponentially small after summing the reciprocal-square weights. For \(0\le s\le1\) restoring the Gaussian on the whole line costs exponentially little, since the real exponent lies in \([-2,0]\) and the displaced center differs by at most \(4q_0t\). The full Gaussian transform has magnitude \(\exp(t[-a+q_0 a^2-q_0\gamma^2])\) with \(0\le a\le2\), hence decays exponentially since all \(|\gamma|\) are bounded away from zero. The prime powers and the archimedean terms on the restricted support are exponentially small as well. This verifies the signed-mean step.

For fixed small \(\eta>0\), take the target minimizing \(W((1+2\eta)u)\) and the compact oscillation window strictly inside \([u,(1+\eta)u]\), as in the [sharp-envelope argument](zhao-sharp-envelope-nov18.md). The previous identity and the signed-mean estimate give the two signed \(G\) excursions at cost at most \(W((1+2\eta)u)\). Here \(du\gg u^{1/4}\) by the Vinogradov–Korobov region, and the fixed-proportion power-sum loss is \(o_\eta(du)\). Monotonicity and concavity of \(W\) give (2) on taking \(2\eta<\epsilon\). This derivation does not require a zero attaining \(\Theta\).

At such an \(x\) the least common multiple \(m_x\) has logarithmic Robin ratio at least \(-K(x)-O(1/(\sqrt x\log x))\), by the exact LCM identity and concavity. Let \(h=x\exp(-(1+2\epsilon)F(v/2))\). Independently insert primes from \((x,x+h]\) if \(\psi(x)\ge x\), or delete primes from \((x-h,x]\) otherwise. The change of the log ratio for any subset costs at most \(O((1+h)^2/x^2)\), as in the counting proof. This is negligible against (2). Since \(h=x^{1-o(1)}\), the short-interval prime number theorem gives \(\gg h/\log x\) eligible primes. All resulting integers have logarithms \(\le2x\): for example the same short-interval theorem bounds the added log mass by \(O(h)\). Taking \(N=\lceil e^{2x}\rceil\) yields
\[
 \log(2+V(N))\gg x\exp(-(1+2\epsilon)F(v/2))/\log x .
\]
Since \(\log\log N=v+O(1)\), the claimed reverse limiting inferior follows on letting \(\epsilon\downarrow0\).

## Exact constants without a hypothesis on the zeros

For any \(\alpha>0\) and real \(k\), set \(\lambda=1/(1+\alpha)\),
\[
 C_{\alpha,k}=\liminf_{\rho,\ \gamma\to+\infty}(1-\beta)(\log\gamma)^\alpha(\log\log\gamma)^k,
 \quad U(u)=u^\lambda(\log u)^{-k\lambda}.
\]
Then, **unconditionally**, with values allowed in \([0,\infty]\),
\[
 \liminf_{N\to\infty}
 \frac{\log(\log N/\log(2+V(N)))}{U(\log\log N)}
 =(1+\alpha)\alpha^{-\alpha\lambda}
       \left(\frac{(1+\alpha)^k}{2}C_{\alpha,k}\right)^\lambda. \tag{3}
\]
For example a conjectural improvement of the power of the Vinogradov–Korobov zero-free region is equivalent to a specific improvement in counting integers violating Robin's inequality. Formula (3) distinguishes different zero-free regions even when they all permit \(\Theta=1\).

First the left side equals \(\liminf F(u/2)/U(u)\) if \(\Theta=1\). The lower inequality follows from the uniform counting upper bound. For the reverse, start the oscillation proof (2) at a sequence of arbitrary \(u\) attaining the latter lower limit, and locate the witnesses in \([u,(1+\eta)u]\). Their costs are at most \(2F((1+2\eta)u/2)\le 2(1+2\eta)F(u/2)\). The construction of integer violations then gives a sequence of \(N\) with \(\log\log N\in[u+O(1),(1+\eta)u+O(1)]\). The function \(U\) is eventually increasing, and \(\log u=o(U(u))\). Taking \(\epsilon,\eta\) arbitrarily small gives the reverse inequality, also when the limit is zero. If \(\Theta<1\), all real parts are bounded away from one, so \(C_{\alpha,k}=\infty\). The left side is infinite by the earlier counting law when RH fails, and directly from Robin's theorem on RH.

It remains to minimize \(du/2+b\) over zero lines. For \(0<c<C_{\alpha,k}\), all sufficiently large heights satisfy \(d\ge c b^{-\alpha}(\log b)^{-k}\). Lines from the finite omitted set and the dummy line grow linearly and are harmless. Writing \(b=sU(u)\), on compact subintervals of \(0<s<\infty\) the normalized lower cost tends uniformly to
\[
 s+\frac{c(1+\alpha)^k}{2s^\alpha}.
\]
The lower bound extends to the infimum: for \(s>M\) the first term is at least \(M\), and for \(s<1/M\) the second is bounded below by its value at \(1/M\), using eventual monotonicity of \(b^\alpha(\log b)^k\). Letting \(M\to\infty\) gives the algebraic minimum in (3) with \(c\) in place of \(C_{\alpha,k}\). For any fixed \(c>C_{\alpha,k}\) there are arbitrarily large ordinates with \(d\le c b^{-\alpha}(\log b)^{-k}\). At such a zero choose \(u=2b^{1+\alpha}(\log b)^k/(\alpha c)\); this attains the same asymptotic minimum as an upper bound. Take limits in \(c\), using nonnegativity and the trivial infinite upper bound in the two endpoint cases.

The explicit region of Mossinghoff, Trudgian and Yang has \(C_{2/3,1/3}\ge1/55.241\). Thus the left side of (3) with \(U(u)=u^{3/5}/(\log u)^{1/5}\) is at least
\[
 \frac53(2/3)^{-2/5}
 \left(\frac{(5/3)^{1/3}}{2\cdot55.241}\right)^{3/5}.
\]
This is a limiting constant. No explicit starting integer for the corresponding counting bound is asserted. [Mossinghoff, Trudgian and Yang, Explicit zero-free regions for the Riemann zeta-function](https://arxiv.org/abs/2212.06867).
