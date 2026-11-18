# The zero abscissa in the limiting distribution of Euler's totient ratio

**Proposed theorem.** Let $X=\log(n/\varphi(n))$ have its limiting distribution in natural density, $W(s)=\log\mathbb E e^{sX}$, and $b(v)=-\log(1-1/v)$. Define the continuous prime comparison
$$
 W_0(s)=\int_2^\infty\log(1+(e^{s b(v)}-1)/v)\frac{dv}{\log v},\qquad
 W_*(s)=W_0(s)+cs,
$$
$$
 c=\gamma_E+\log\log2-\int_2^\infty(b(v)-1/v)\frac{dv}{\log v}.
$$
Write $\Theta=\sup_\rho\Re\rho$. Both real statistics satisfy
$$
 \limsup_{s\to\infty}\frac{\log(1+s^2|W''(s)-W_0''(s)|)}{\log s}
 =\limsup_{s\to\infty}\frac{\log(1+|W(s)-W_*(s)|)}{\log s}=\Theta.
 \tag{1}
$$
The observable $W$ may be defined entirely from the abundance distribution; the comparison involves no primes or zeros. We use Weingartner's classical independent-prime Euler product for its moment. The new direction of interest is the converse from smooth comparison error to zero location. [Weingartner, §1](https://arxiv.org/abs/1011.4262)

## A real-variable upper bound

Let $K(u)=e^{-u}/(1+e^{-u})^2$, and $\ell(v)=\log(v-1)$. The Euler product gives
$$
 W''(s)=\sum_p b(p)^2 K(s b(p)-\ell(p)).
$$
The model $W_0''$ is exactly its continuous integral against $dv/\log v$. Differentiation is justified by absolute convergence locally in real $s$. Put $x\log x=s$, and take any $\alpha>\Theta$ with $\alpha<2$. Classical prime counting gives $|\pi(v)-\int_2^v dt/\log t|\ll_\alpha v^\alpha$, also for $\Theta=1$. The derivative of the weight with respect to $v$ is bounded by $C v^{-3}(1+s/v)\exp(-|s b(v)-\ell(v)|)$ for $v\ge2$. For $v\le x/2$ the absolute value in the exponential is at least $s/(2v)$; for $v\ge x/2$ just discard the exponential. Partial integration (including the lower endpoint atom) then gives
$$
 |W''(s)-W_0''(s)|\ll_\alpha x^{\alpha-2}(1+\log x).
$$
Also $W'(s)-W_0'(s)\to c$. Indeed the differentiated summand is $b(v)/(1+(v-1)e^{-s b(v)})$. Replacing the logistic by $\mathbf1_{v\le x}$ costs $o(1)$ in both sum and integral: on $[x/2,2x]$ use the $O(1/\log x)$ total weight, below it use $1-(1+(v-1)e^{-sb(v)})^{-1}\le v e^{-s/v}$, and above it use $(1+(v-1)e^{-sb(v)})^{-1}\ll x^{0.51}/v$. Mertens' product theorem gives the stated limit. Integrating the curvature bound from infinity for $\Theta<1$, then integrating the first derivative from a fixed positive point, gives $W(s)-W_*(s)=O_\epsilon(s^{\Theta+\epsilon})$. The elementary bound $o(s)$ suffices when $\Theta=1$.

## A singularity that the limiting probability law retains

Let $R=W''-W_0''$. On $1<\Re z<2$, Mellin transformation and absolute integration give
$$
 \mathcal M(z)=\int_0^\infty s^{1-z}R(s)\,ds
 =\int_{[2,\infty)} b(v)^z I_z(\ell(v))\left(d\pi(v)-\frac{dv}{\log v}\right),
 \quad I_z(l)=\int_0^\infty u^{1-z}K(u-l)du .
$$
The powers of positive real variables use their real logarithms. Here are details for continuation, since a formal asymptotic expansion in inverse logs need not identify individual zero singularities. Choose $T=3/4$ and $A(t)=\int_{\mathbb R}K(w)e^{-tw}dw=\pi t/\sin(\pi t)$ for $|t|<1$. On compact subsets of $0<\Re z<2$ one has
$$
 \Gamma(z)I_z(l)=
 \int_0^T t^{z-1}e^{-tl}\{lA(t)-A'(t)\}dt
 +O((1+l)^C e^{-T l}),\quad l\ge0.
 \tag{2}
$$
To prove this, insert $\Gamma(z)u^{1-z}=u\int_0^\infty t^{z-1}e^{-tu}dt$. For $0<t<T$ extend $w=u-l$ to the whole line. The missing $w<-l$ has absolute integral $O(e^{-l}/(1-T)^2)$ after the exterior factor $e^{-tl}$. For $t>T$, the part $u<1$ costs $O(e^{-l})$ by the original integrability at zero (uniformly on compact $z$ sets). At $u\ge1$ the incomplete gamma integral is $O((1+u)^C e^{-Tu})$ and its convolution against $K(u-l)$ is $O((1+l)^C e^{-Tl})$. The error is holomorphic by normal domination. Replacing $b(v)^z$ by $v^{-z}$ and $\ell(v)$ by $\log v$ makes an analytic error on $\Re z>0$ locally inside this strip: both $I_z$ and its first $l$ derivative are at most polynomial in $1+l$, while the elementary relative and additive changes are $O(1/v)$.

With $P(w)=\sum_p p^{-w}-\int_2^\infty v^{-w}dv/\log v$, equation (2) becomes
$$
 \Gamma(z)\mathcal M(z)=
 -\int_0^T t^{z-1}\{A(t)P'(z+t)+A'(t)P(z+t)\}dt+E(z),
 \tag{3}
$$
where $E$ is holomorphic for $1/4<\Re z<2$. The prime-square and higher terms in the Euler logarithm imply $P(w)=\log((w-1)\zeta(w))+$ a locally holomorphic function on $\Re w>1/2$ away from zeros, with branches continued along the path. Indeed differentiation of the continuous integral gives $-2^{1-w}/(w-1)$, and the prime-power terms of order $\ge2$ converge normally there. This description also continues locally near any $w=1/2+i\gamma$ for $\gamma\ne0$, away from the logarithmic singularity of $\zeta(w)$ itself: the order-two term continues through $\log\zeta(2w)$ since $\zeta(1+2i\gamma)\ne0$, and orders at least three converge normally.

Fix a nontrivial zero $\rho=\beta+i\gamma$ which is rightmost among the zeros at its *own ordinate*, of multiplicity $m$. Continue (3) horizontally from the right down to $z=\rho+r$, $r>0$. At this ordinate there is no intervening singularity, and the segment $z+[0,T]$ admits compatible branches locally. Near the endpoint $P(w)=m\log(w-\rho)+$ a holomorphic function. Since $A(0)=1$ and $A'(t)=O(t)$, the singular part of (3) is $-m\int_0^{\delta}t^{z-1}/(r+t)dt$ up to bounded error for small fixed $\delta>0$. Substitution $t=rv$ and the beta integral give
$$
 \mathcal M(\rho+r)=-m\Gamma(1-\rho)r^{\rho-1}(1+o(1)).
 \tag{4}
$$
This diverges in modulus since $\beta<1$. Choosing rightmost zeros at individual ordinates preserves the global supremum. A hypothetical curvature upper exponent below such a $\beta$ would make the original Mellin integral holomorphic there by absolute convergence. A corresponding moment-value bound also contradicts (4): integrate twice by parts on $[1,\infty)$ for $1<\Re z<2$ to express $\mathcal M(z)$ as $z(z-1)\int_1^\infty s^{-z-1}(W(s)-W_*(s))ds$ plus a function holomorphic locally on $\Re z<2$ near $\rho$. The lower endpoint gives only entire boundary terms, and the original integral over $(0,1)$ is regular there. This proves (1), including its critical-line lower exponent.

## Converse to the distribution-tail estimate

For either $Z=n/\varphi(n)$ or $Z=\sigma(n)/n$, write $A_Z(t)$ for the limiting natural density of $Z\ge t$. Put $y=\exp(t e^{-\gamma_E})$ and use **exactly** the integral $I(y,s)$ and interval $J_y=[y\log y-y,y\log y+y]$ of Weingartner's Theorem 2. Then
$$
 \limsup_{t\to\infty}
 \frac{\log\big(1+|\log A_Z(t)+y-\min_{s\in J_y}I(y,s)|\big)}
      {\log y}=\Theta .
 \tag{5}
$$
In particular the $O(\sqrt y\log^2y)$ bound in that published theorem is equivalent to RH, and so is the weaker family of bounds $O_\epsilon(y^{1/2+\epsilon})$ for each $\epsilon>0$. For sufficiency of RH for the sharper logarithmic bound we use Weingartner's theorem as stated. We prove the converse here. Weingartner denotes the two limiting tails by $A(t)$ and $B(t)$. [Original statement, equation (3) and Theorem 2](https://arxiv.org/abs/1011.4262)

First the moment assertion (1) holds for $\sigma(n)/n$ with the same $W_*$, including the lower exponent on RH. The [prime-square comparison](abundance-curvature-sigma-nov18.md) gives $W_\sigma-W_\phi=O(\sqrt{s/\log s})$ and identifies the curvature difference up to $O_\epsilon(s^{-5/3+\epsilon})$ as $\sum_p p^{-4}K(s/p^2-\log p)$. The latter shell's transform for $1<\Re z<2$ is $\sum_p p^{-2z}I_z(\log p)$. By (2) its continuation is holomorphic locally at each $z=1/2+i\gamma$, $\gamma\ne0$, approached from the right: the only prime-zeta arguments on the integration path are $2z+t$, $0\le t\le T$, whose real parts are at least one at that point and whose imaginary parts are nonzero. The normally convergent residual of (2) and the curvature error are regular there. Thus the shell cannot cancel (4). For $\beta>1/2$ regularity already follows from the absolute decay of the curvature difference.

Write $u=\log t$ and $I_*(u)=\min_{s\ge1}(W_*(s)-su)$. The [continuous-model comparison](abundance-weingartner-model-nov18.md) gives, without a prime-number estimate,
$$
 I_*(u)=-y+\min_{s\in J_y}I(y,s)+O(1).
 \tag{6}
$$
It remains to relate the actual limiting tail to $I_*$ on a power scale. Let $W$ now denote the relevant actual log moment and $I_A(u)=\min_{s\ge1}(W(s)-su)$. The actual and model minimizers have sizes $y^{1+o(1)}$. Indeed their first derivatives are $\gamma_E+\log\log x+o(1)$ at $s=x\log x$, by the upper-bound argument and the prime-square comparison. Both derivatives are strictly increasing and unbounded (their second derivatives are positive). Evaluating $W-W_*$ at the two minimizers therefore bounds $|I_A-I_*|$ by $O_\epsilon(y^{\Theta+\epsilon})$.

The exponential Markov bound gives $\log A_Z(e^u)\le I_A(u)$. Conversely fix any small $\epsilon>0$, put $\delta=y^{-1/2+\epsilon}$, and choose $s_+$ with $W'(s_+)=u+\delta$. Again $s_+=y^{1+o(1)}$ since $\delta\log y=o(1)$. Under the probability measure tilted by $e^{s_+X-W(s_+)}$, the log ratio $X=\log Z$ has this mean and variance $W''(s_+)\ll s_+^{-1+o(1)}$. For $\varphi$ the variance bound follows by summing $O(v^{-2})$ above $x/2$ and $O(e^{-s/v}/v)$ below. For $\sigma$ use the curvature comparison. Chebyshev's inequality now gives tilted probability at least $1/2$ on $[u,u+2\delta]$ for large $u$. Undo the tilt to obtain $\log A_Z(e^u)\ge I_A(u)-2s_+\delta-\log2$. This proves the upper exponent in (5).

For the lower exponent, suppose $|\log A_Z(e^u)-I_*(u)|\ll y^d$ for some $0<d<\Theta$. We show $|W(s)-W_*(s)|\ll_\eta s^{d(1+\eta)}+O(\log s)$ for every small fixed $\eta>0$. This would contradict (1). Use
$$
 e^{W(s)}=1+s\int_0^\infty e^{su}A_Z(e^u)du .
$$
The limiting distributions are continuous; endpoint conventions have no effect on the integral. The model saddle $u_*=W_*'(s)$ has $y(u_*)=s^{1+o(1)}$, where $y(u)=\exp(e^{u-\gamma_E})$. Also $W_*(s)/s=\gamma_E+\log\log s+o(1)$ by integrating its derivative, or by the model formula. Below $y(u)<s^{1-\eta}$ the trivial tail bound one gives an exponentially negligible contribution compared with $e^{W_*(s)}$, since $u\le\gamma_E+\log\log s+\log(1-\eta)$. Above $y(u)>s^{1+\eta}$ use $-\log A_Z(e^u)\sim y(u)$, already Weingartner's unconditional Theorem 1. There $su=o(y(u))$ uniformly, and the integrated contribution is negligible (change variables from $u$ to $y$). In the remaining middle range use $I_*(u)+su\le W_*(s)$ and the hypothesized tail error. Its integration length is bounded in terms of $\eta$, giving the desired upper bound. For the reverse bound integrate just over $[u_*-s^{-2},u_*]$. Here $I_*(u)\ge I_*(u_*)$ by monotonicity, $su\ge su_*-1/s$, and $y(u)\le s^{1+\eta}$ for large $s$. This gives the asserted lower bound with an $O(\log s)$ cost. Choosing $\eta$ so $d(1+\eta)<\Theta$ completes (5).

The criterion concerns the error in an infinite limiting distribution, not a bound for a finite sample of integers. Its smallest missing step toward RH is an unconditional $O_\epsilon(y^{1/2+\epsilon})$ estimate for that error, or equivalently the same power bound for the centered log moment in (1).

## The oscillatory residual on RH

Under RH the two remainders in (5) have explicit, opposite signs at all sufficiently large arguments. If $\mathcal E_Z(t)=\log A_Z(t)+y-\min_{s\in J_y}I(y,s)$, then
$$
 \frac{\mathcal E_{n/\varphi(n)}(t)}{\sqrt y}
 =2+F(\log y)+o(1),\qquad
 \frac{\mathcal E_{\sigma(n)/n}(t)}{\sqrt y}
 =2-2\sqrt2+F(\log y)+o(1),\qquad
 F(v)=\sum_\rho \frac{e^{i\gamma v}}{|\rho|^2}.
 \tag{7}
$$
The sum includes both signs and multiplicities. Its uniform absolute bound is $2+\gamma_E-\log(4\pi)<0.047$ by the classical xi product. The order-$\sqrt y$ term retains every critical-line zero frequency.

Here is a direct reduction of the moment to the integrated prime formula. Fix $s=xL$, $L=\log x$. For $v\le x$ split the local log moment integrand as $s b(v)-\log v+\log(1+(v-1)e^{-s b(v)})$. The contribution of the first two terms to $W-W_*$, including the model's linear centering, is $-sK(x)+O(1)$ by the [exact Mertens-product tangent identity](robin-tangent-nov18.md). In detail the $\vartheta(x)-x$ term cancels, the remainder $sR(x)$ costs $O(1)$ using the PNT and $\sum_{p>x}p^{-2}\ll1/(xL)$, and $s\int_x^\infty(b(v)-1/v)dv/\log v=O(1)$.

The remaining arithmetic-minus-integral difference equals, to $o(\sqrt x)$,
$$
 \int g_x(v)(d\pi(v)-dv/\log v),\quad
 g_x(v)=\chi(v/x)\log(1+\exp(-|s/v-\log v|)),
$$
where $0\le\chi\le1$ is smooth, one on $[1/2,2]$ and supported in $(1/3,3)$. On $[x/2,2x]$ the elementary argument changes $s(b(v)-1/v)$ and $\log(v/(v-1))$ give $O(L/x)$ pointwise in the soft logarithm; above $x$ the omitted additional term $\log(1-1/v)$ is $O(1/x)$. Even summing over all integers this is $O(L)$. Below $x/2$ both true and smoothed transition weights cost $O(1)$ in total, by $v e^{-s/v}$. Above $2x$ and below $s$ the sum and integral are bounded using $C e^{s/v}/v$, with integral $O(\sqrt x/L+\log x)$ by the substitution $w=s/v$; the same bound follows for the integer sum by monotonicity. Above $s$ the original weight is $O(s/v^2)$.

Use the von Mangoldt explicit formula against $g_x(v)/\log v$. Converting the prime sum to this prime-power sum costs $O(\sqrt x/L+x^{1/3}\log x)$ by the PNT and boundedness of $g_x$. For $w=\log(v/x)$ put $H_x(w)=g_x(xe^w)/(L+w)$. Uniformly in $0\le\beta\le1$,
$$
 \|e^{\beta w}H_x\|_1\ll L^{-2},\qquad
 \|(e^{\beta w}H_x)''\|_{\rm TV}\ll1.
$$
Indeed $s/(xe^w)-\log(xe^w)=L(e^{-w}-1)-w$ vanishes only at zero and has derivative comparable in magnitude to $L$ on the support. The soft logarithm and its first two ordinary derivatives away from its cusp are $O(e^{-|L(e^{-w}-1)-w|})$ in their own argument; its first derivative has one bounded jump. The chain rule, the $1/(L+w)$ weight, and integration give the two bounds including the atom in the second derivative. Thus the absolute zero contribution is
$$
 \ll x^{\Theta}\sum_\rho\min(L^{-2},|\gamma|^{-2})
 \ll x^\Theta\log L/L
$$
by the Riemann–von Mangoldt count. The explicit formula extends to this continuous piecewise smooth test by mollification, with the two norm bounds giving summable domination; the trivial-zero contribution is negligible on its support. On RH this is $o(\sqrt x)$. The [integrated formula](robin-lcm-nov18.md) gives $-sK(x)/\sqrt x=2+F(\log x)+o(1)$. This proves the first profile at the moment level. The [prime-square comparison](abundance-curvature-sigma-nov18.md) shifts the constant by $-2\sqrt2$ for the divisor sum.

For passage to the tail, set $s_*$ at the model minimum and $s_A$ at the actual minimum. On RH the curvature bound and derivative anchor give $|W'-W_*'|\ll_\epsilon s^{-1/2+\epsilon}$. On $[s_*/2,2s_*]$ one has $W_*''(s)\asymp1/(s\log s)$ by integrating the positive logistic kernel on the $v$ scale $x/\log x$ about $x$ (its exponentially decaying tails have the same upper bound). Thus $s_A$ lies there and $|s_A-s_*|\ll_\epsilon s_*^{1/2+\epsilon}\log s_*$. By convexity the difference between $I_A-I_*$ and $(W-W_*)(s_*)$ is bounded by the product of this distance and the supremum of $|W'-W_*'|$ there. It is $o(\sqrt y)$. The model bracket implies $x_*/y\to1$, $x_*\log x_*=s_*$, so uniform continuity of $F$ permits replacing $x_*$ by $y$ in the profile. Finally the [tilted saddle estimate](abundance-exact-saddle-nov18.md) gives $\log A_Z(e^u)-I_A(u)=o(\sqrt y)$; only this weak form is needed. Together with (6) this proves (7).

## A sign test with no assumed size for the opposite excursions

If RH fails, each sign of $\mathcal E_Z(t)$ in (7) separately has upper growth exponent $\Theta$ in the sense of (5) with positive or negative part in place of absolute value. Hence eventual nonnegativity of the totient remainder, or eventual nonpositivity of the divisor-sum remainder, is alone equivalent to RH.

To see this first consider $D(s)=W(s)-W_*(s)$. Its Mellin integral on $[1,\infty)$ continues regularly along the real axis $z>1/2$ by (3) and twice integrating by parts. The apparent singularity at $z=1$ is removable: the numerator is regular and $D=o(s)$ gives $o(1/(z-1))$ from the right. The divisor-sum comparison has the same continuation here. If either $D(s)$ or $-D(s)$ were eventually bounded above by $C s^d$ for $1/2<d<\Theta$, subtract it from $Cs^d$ to obtain an eventually nonnegative function. The abscissa of convergence of its Mellin integral is at least some $\beta>d$ by (4), and is at most one by the growth bound. Landau's singularity theorem for a positive Laplace transform then forces a real singularity at that abscissa, contradicting regular continuation there. This proves the two signed assertions for $D$. In the tail-to-moment integral proof of (5), the upper bound on $W-W_*$ used only the upper hypothesized bound on the tail error, and the lower bound used only its lower bound. They therefore transfer each obstruction separately.

As one discrete version, it suffices to have $W_\sigma(k^4)\le W_*(k^4)$ at every sufficiently large integer $k$. On RH it follows from the negative moment profile above. Conversely $W_\sigma$ is convex, and the maximum excess of the chord of $W_*$ on $[k^4,(k+1)^4]$ above $W_*$ is $O((k+1)^6/(k^4\log k))$ by its curvature estimate. This is $o(\sqrt{s/\log s})$ on those intervals. The one-sided moment obstruction then implies RH. The integer powers here index moments of the limiting divisor-sum distribution.
