# The number of integers violating Robin's inequality determines the zero abscissa

**Proposed theorem.** Let $V(N)$ count integers $5040<n\le N$ for which $\sigma(n)\ge e^{\gamma_E}n\log\log n$, and put $\Theta=\sup_\rho\Re\rho$. If RH fails, then
$$
 \lim_{N\to\infty}\frac{\log\log V(N)}{\log\log N} = \frac{1+\Theta}{2}.
 \tag{1}
$$
On RH, $V(N)=0$ by Robin's theorem. The lower bound in (1) counts strict violations and holds on every sufficiently large terminal scale. The upper bound even includes equality. In particular a bound $V(N)\le\exp((\log N)^{3/4+o(1)})$ would imply RH. The lower bound uses only the proposed [power-window LCM oscillation theorem](robin-lcm-nov18.md), proved there by Gaussian smoothing. It does not estimate $V(N)$ by numerical sampling.

## Upper bound by comparison with a primorial

Suppose first $\Theta<1$. Fix $\Theta<\alpha<1$. Write $y=\log n$, $s=(y\log y)^{-1}$, $z=y-y^{(1+\alpha)/2}$ and $P(z)=\prod_{p\le z}p$. The classical explicit formula gives $\vartheta(t)-t=O_\alpha(t^\alpha)$. Thus the signed integrated discrepancy in the [tangent identity](robin-tangent-nov18.md) obeys $|K(y)|\ll_\alpha y^{\alpha-1}/\log y$ by absolute integration. In the proof of that identity retain the actual per-prime differences between the baseline and the contribution. All are nonnegative. A missing prime $p\le z$ contributes
$$
 -\log(1-1/p)-s\log p
 \ge (y/z-1)s\log p.
$$
Indeed $p\log p\le z\log y$. For a violating $n$ the sum of the differences is at most $-K(y)-R(y)\le |K(y)|$. Consequently, for $B=P(z)/\gcd(n,P(z))$,
$$
 \log B\ll_\alpha y^{(1+\alpha)/2}.
$$
Writing $A=n/\gcd(n,P(z))$ gives $n=P(z)A/B$ and $\log A=y-\vartheta(z)+\log B\ll_\alpha y^{(1+\alpha)/2}$. There are at most $1+\log N$ choices for $P(z)$ as $n$ varies through the sufficiently large integers up to $N$. Counting both positive integers $A,B$ now gives $\log(1+V(N))\ll_\alpha (\log N)^{(1+\alpha)/2}$. Let $\alpha\downarrow\Theta$. For $\Theta=1$ the trivial count gives the desired upper exponent.

## Lower bound by independent prime insertions

Fix $1/2<c<\Theta$, $0<\eta<1$, and set $r=(1+c)/2$. The power-window theorem gives, for every sufficiently large $Y$, an $x\in[Y^{1-\eta},Y]$ with
$$
 \log\frac{\sigma(m)}{e^{\gamma_E}m\log\log m}>x^{c-1},
 \qquad m=\operatorname{lcm}(1,\ldots,\lfloor x\rfloor).
$$
Write $y=\log m=\psi(x)\sim x$ and $h=x^r/(\log x)^2$. If $y\ge x$, multiply $m$ by any subset of the primes $x<p\le x+h$. They are coprime to $m$. If $y<x$, divide $m$ by any subset of the primes $x-h<p\le x$. Each divides $m$ to exponent one for large $x$. Set $s_u=1/(u\log u)$, decreasing for $u>1$. Concavity of $u\mapsto\log\log u$ bounds its change from $y$ to $\log n$ by $s_y(\log n-y)$ for either modification. In the multiplication case the resulting per-prime change of the log Robin ratio is bounded below in the sum by $\log(1+1/p)-s_x\log p$, since $s_y\le s_x$. In the division case the lower bound is $s_x\log p-\log(1+1/p)$, since $s_y>s_x$.

On both intervals $|\log(1+1/p)-s_x\log p|\ll (1+h)/x^2$ by the mean value theorem and $\log(1+1/x)=1/x+O(x^{-2})$. Even counting every integer in the interval gives total loss $O((1+h)^2/x^2)=o(x^{c-1})$. All subsets therefore give distinct strict violations. The prime number theorem in short intervals of any fixed exponent greater than $7/12$ yields at least $x^{r-o(1)}$ primes on either side (apply it at each fixed exponent strictly between $7/12$ and $r$). This use lies entirely above exponent $3/4$ in the limit. [Huxley, On the difference between consecutive primes](https://doi.org/10.1007/BF01418933)

Choose $Y=(\log N)/2$. Since $\log n\le y+O((1+h)\log x)=x+o(x)$, all the integers just constructed lie below $N$. It follows that $\log V(N)\ge (\log N)^{(1-\eta)r-o(1)}$ for every sufficiently large $N$. Taking $\eta\downarrow0$ and $c\uparrow\Theta$ proves (1). The stronger [fixed-window theorem](robin-lcm-positive-kernel-nov18.md) puts each family at $\log n\asymp\log N$ and allows prime insertions alone at the selected fixed point.

## Unconditional upper bound and the published exceptional-set estimate

Put $W(u)=(\log u)^{3/5}(\log\log u)^{-1/5}$ for large $u$. For some absolute $b>0$, irrespective of the value of $\Theta$, the same factorization yields
$$
 \log(1+V(N)) \ll (\log N)\exp[-bW(\log N)].
 \tag{2}
$$
Indeed the Vinogradov–Korobov prime number theorem gives $|\vartheta(u)-u|\ll u e^{-aW(u)}$ for an absolute $a>0$. Fix $0<b<a/2$. Integrating the tail defining $K(y)$ and shrinking the exponent gives $|K(y)|\ll e^{-2bW(y)}/\log y$. To see this split off the factor $e^{-2bW(y)}$ by monotonicity. The remaining integral after $v=\log t$ has an exponentially decaying tail in $v^{1/2}$, which absorbs the displayed logarithm. Set $z=y(1-e^{-bW(y)})$. The preceding deficit bound gives $\log B\ll y e^{-bW(y)}$, and $y-\vartheta(z)\ll y e^{-bW(y)}$ by the same prime number theorem since $W(z)/W(y)\to1$. The function $y e^{-bW(y)}$ is eventually increasing, so counting pairs proves (2) at every sufficiently large $N$.

Luca, Pomerance and Solé prove $V(N)\le N^{O(1/\log\log N)}$ in their 2025 correction. Formula (2) improves that published upper estimate asymptotically. The conditional-on-failure exponent in (1) further uses LCM oscillation. [Corrigendum, Theorem 1](https://math.colgate.edu/~integers/z8/z8.errata.pdf)

## Counting near equality gives an abscissa even when RH holds

For $1/2\le a<1$ count $5040<n\le N$ satisfying
$$
 \log\frac{\sigma(n)}{e^{\gamma_E}n\log\log n}\ge -(\log n)^{a-1}.
$$
Denote the count by $V_a(N)$. Then, without a hypothesis on the zeros,
$$
 \lim_{N\to\infty}\frac{\log\log V_a(N)}{\log\log N}
 =\frac{1+\max(a,\Theta)}2.
 \tag{3}
$$
In particular RH is equivalent to the limit $3/4$ for the positive, unbounded counting function $V_{1/2}$. This counts integers that approach Robin's inequality from either side.

For the upper bound the tangent budget increases by $y^{a-1}$. Choose $\alpha>\max(a,\Theta)$ and absorb the extra logarithm into this strict exponent gap in the proof above (use an intermediate exponent for the prime number theorem). The trivial bound suffices if $\Theta=1$. If RH fails and $a\le\Theta$, the strict-violation lower bound already suffices. For $a>\Theta$, take $x=(\log N)/2$ and $m$ as above. The [LCM identity](robin-lcm-nov18.md) gives $B(x)\ge -J(x)-O(1/(\sqrt x\log x))$. For $\Theta<\alpha<a$ the explicit formula gives $|J(x)|\ll_\alpha x^{\alpha-1}/\log x$. Thus $B(x)\ge-o(x^{a-1})$. In the residual case $a=\Theta=1/2$, that same LCM note gives $|B(x)|\ll 1/(\sqrt x\log x)$ under RH using the absolutely summable zero coefficients. In either case spend a budget $o(x^{a-1})$ on the independent prime modifications above, with $r=(1+a)/2$. The perturbed $n$ have $\log n\sim x$ uniformly, so they satisfy the defining near equality, and there are $\exp(x^{r-o(1)})$ of them.
