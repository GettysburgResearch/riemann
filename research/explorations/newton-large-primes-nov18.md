# The large ordinary-prime part retains the native Möbius growth exponent

**Proposed analytic theorem.** Write $\Theta=\sup_\rho\Re\rho$ over nontrivial zeta zeros. This paper does not determine $\Theta$. It identifies the exponent of a family of signed prime discrepancies, uniformly over a moving lower prime cutoff, with the actual Möbius history retained. The proof uses the [exact native evolution](newton-prime-feedback-nov18.md) and adapts the [compact sparse-zero isolator](causal-isolated-zero-nov18.md) to the additional pole of a product involving $1/\zeta$.

For $m(x)=\sum_{n\le x}\mu(n)/n$ let $f(t)=e^{t/2}m(e^t)$ on $[0,\infty)$, zero before zero. Fix $U\ge2$ for each observation and put

$$
 D_{>U}=\sum_{p>U}\frac{\log p}{\sqrt p}\delta_{\log p}
          -1_{u>\log U}e^{u/2}\,du,\qquad A_U=D_{>U}*f .
$$

In ordinary arithmetic coordinates $A_U(t)=e^{t/2}\int_{U<v\le e^t}m(e^t/v)(d\vartheta(v)-dv)/v$. Thus only cofactors $\le e^t/U$ enter. The cutoff is held fixed inside each measured window.

### Results

1. For fixed $w>0$, $0<\kappa<1$ and **every** choice $2\le U_t\le e^{\kappa t}$,

$$
 \lim_{t\to\infty}\frac1t\log\left(1+
 \|A_{U_t}(v)/v\|_{L^2(t-w,t+w)}\right)=\Theta-\tfrac12 .       \tag{1}
$$

The upper and lower estimates are uniform over all indicated cutoffs at each $t$. Taking $U_t=e^{\kappa t}$ allows any fixed positive cofactor exponent $1-\kappa$.

2. On the full Newton annulus there is a broader uniform statement. Put $L=\log b$ for integers $b\to\infty$. For **every** choice $2\le U_b\le b^2/2$,

$$
 \lim_{b\to\infty}\frac1{2L}\log\left(1+
 \|A_{U_b}(v)/v\|_{L^2(L,2L)}\right)=\Theta-\tfrac12 .          \tag{2}
$$

In particular subpower bounds along any unbounded sequence of these cutoffs and stages would imply RH. The assertions concern the exponential growth class; they do not furnish a uniformly bounded inverse for arbitrary inputs after enlarging the prime bank. The [general-input inverse threshold](newton-prime-feedback-nov18.md) concerns a different quantifier and norm.

### Uniform upper estimate

With $s=\sigma+i\tau$, use the Laplace variable $z=s-1/2$. The transforms of $f$, all higher powers, and the full ordinary-prime discrepancy are initially

$$
 F(z)=\frac1{(s-1)\zeta(s)},\qquad
 Q(z)=\sum_{p,\,k\ge2}(\log p)p^{-ks},\qquad
 D(z)=-\frac{\zeta'}{\zeta}(s)-Q(z)-\frac1{s-1}.
$$

The pole at one cancels in $D$ and in $(s-1)\zeta(s)$. The power series $Q$ is absolutely convergent on $\sigma>1/2$. Write $D_{\le U}(z)=\sum_{p\le U}(\log p)p^{-s}-\int_1^U v^{-s}dv$.

For each fixed $\Theta<\sigma<1$, uniformly in $U$ and real $\tau$,

$$
 |D_{\le U}(\sigma-1/2+i\tau)|\ll_\sigma \log(3+|\tau|).        \tag{3}
$$

Here and below constants may depend on the chosen distance from $\Theta$. We detail why no factor $|\tau|$ is needed. Fix $\Theta<\lambda<\sigma$. In $\Re s\ge\lambda$, up to real part two, the pole-canceled function $-\zeta'/\zeta(s)-1/(s-1)$ is $O_\lambda(\log(3+|\Im s|))$ by the classical local partial fraction estimate and the positive distance from every zero. The bounded central portion follows by continuity. For $x\ge3$, use Perron on the line $d=1+1/\log x$ at height $V=x^2$ for the cumulative signed measure
$\sum_n\Lambda(n)n^{-i\tau}\delta_n-1_{v\ge1}v^{-i\tau}dv$, first with $x$ a half-integer. Its transform in the Perron variable $w$ is the preceding pole-canceled function at $s=w+i\tau$. The ordinary truncated Perron error is $O(\log^2(2x))$ uniformly in $\tau$. Indeed its modulus is bounded by integrating
$C(x/v)^d\min(1,(V|\log(x/v)|)^{-1})$ against $\sum_n\Lambda(n)\delta_n+dv$. Off $[x/2,2x]$ this is $O(x^d\log^2(2x)/V)$ by summing the majorant $\log(2n)n^{-d}$. Inside the interval, the atom sums use the half-integer separation and the harmonic sum, costing $O(x\log^2(2x)/V)$. The integral costs $O(x(1+\log V)/V)$ by splitting at $|v-x|=x/V$. These estimates follow directly from the truncated Perron kernel, independently of the phases. For other $x$ use $\lfloor x\rfloor+1/2$, altering the continuous integral by at most one.

Shifting the Perron rectangle to $\Re w=\lambda$ crosses no pole. The vertical integral costs $O_\lambda(x^\lambda\log(2x)\log(3+|\tau|+x))$ and the horizontal segments cost $O_\lambda(x^d\log(3+|\tau|+x)/V)$. Deleting higher prime powers costs $O(\sqrt x\log^2(2x))$ in absolute value. Consequently the cumulative twisted discrepancy of ordinary primes is
$O_\lambda(x^\lambda[\log^2(2x)+\log(2x)\log(3+|\tau|)])$. Partial summation now uses the real weight $v^{-\sigma}$, since the phase was included before the Perron shift. The positive gap $\sigma-\lambda$ proves (3).

On the same vertical line $D(z)$ is $O_\sigma(\log(3+|\tau|))$. The classical generalized Littlewood bound gives $1/\zeta(s)\ll_{\sigma,\epsilon}(3+|\tau|)^\epsilon$ for every $\epsilon>0$ when $\sigma>\Theta$. For its application in this normalization see [XCC26, §1.2](https://github.com/GettysburgResearch/riemann/blob/7de75c02417d5d8db7eafb1ceba364380e72d16a/standalone/2026-09-12-astra-crossing-cofinal/PROOF.md). Hence the products $F(z)[D(z)-D_{\le U}(z)]$ have uniformly bounded squared vertical integrals. Laplace Plancherel applies to the physical functions: for each fixed $U$, the native identity $A_U=-tf-Q*f-D_{\le U}*f$ (with $Q$ here acting as its causal measure) and $f(t)\ll_\epsilon e^{(\Theta-1/2+\epsilon)t}$ give convergence on this line. The latter physical bound follows by generalized Littlewood for $M(x)$ and partial summation using $\sum\mu(n)/n=0$. Thus

$$
 \sup_{U\ge2}\int_0^\infty e^{-2(\sigma-1/2)v}|A_U(v)|^2\,dv<\infty .
$$

For $\Theta=1$ use any $\sigma>1$ and absolute convergence instead. The local and annular upper exponents in (1)–(2) follow. When $\Theta=1/2$ nonnegativity of the logarithms already finishes both assertions.

### A cutoff-independent residue on a compact window

Suppose now $\Theta>1/2$. Fix a zero $\rho$ with $\beta=\Re\rho>1/2$, of order $m\ge1$. The transform $F(z)(D(z)-D_{\le U}(z))$ has a pole of order $m+1$ at $s=\rho$. Its top Laurent coefficient is

$$
 -\frac{m\,m!}{(\rho-1)\zeta^{(m)}(\rho)}\ne0,                \tag{4}
$$

independent of $U$. The small finite prime sum, the continuum and the convergent higher powers only multiply poles of order at most $m$. This extra pole order is the arithmetic reason that the residue can survive deleting a growing prime range.

We recall the test construction to specify the orders and the uniformity. Choose $1/2<\sigma_0<\alpha<\beta$, taking $\alpha$ at distance at least $c(1+|\Im\lambda|)^{-3}$ from each zero real part $\Re\lambda$; exclusion of sufficiently small intervals leaves such choices in any prescribed open subinterval. Ingham's density theorem gives $O(R^k)$ zeros with $\Re\lambda>\alpha$, $|\Im\lambda|\le R$, counted with multiplicities, for some $k<1$ (one may enlarge $k$ slightly to absorb logarithms). Form the genus-zero product over those zeros other than $\rho$ with multiplicities $m_\lambda+1$, and multiply by $(s-\rho)^m$. Doubling the counting bound suffices for these extra multiplicities. The resulting entire function has growth bounded by $\exp(C(1+|s|)^k)$ after a possible enlargement of $k<1$.

Choose $k<q<1$ and multiply by $\prod_{j\ge1}\sinh(b_j z)/(b_j z)$, where $b_j=Bj^{-1/q}$ with $\sum b_j<w$. This second factor is nonzero at $z=\rho-1/2$, and decays as $\exp(-c|\Im z|^q)$ on fixed vertical strips by using $b_j|z|\ge2$ in the first $\asymp |z|^q$ factors. The resulting $W(z)$, with $s=z+1/2$, is the bilateral Laplace transform of a smooth kernel supported in $(-w,w)$ by Paley–Wiener. It has a zero of exact order $m$ at the selected point and enough zeros to cancel every other pole on $\Re s>\alpha$. This is the same compact-test construction as [the prime-side isolation proof](causal-isolated-zero-nov18.md), with the increased multiplicities above.

After multiplying by $W$, move the inversion contour from $\Re s=2$ to $\alpha$. For clarity, a polynomial lower bound on the distance to all zeros on the chosen line gives $|1/\zeta(s)|\le\exp(C\log^2(3+|\Im s|))$ there. To see this, center a disk of radius between four and five at $2+i\Im s$, avoiding zeros on its boundary. Jensen's formula on a radius-six disk counts $O(\log(3+|\Im s|))$ zeros inside. Divide by their disk Blaschke factors, and apply Harnack to a constant multiple of $\log(3+|\Im s|)$ minus the log modulus of the zero-free quotient, using polynomial strip growth and $|\zeta(2+i\Im s)|\ge1/\zeta(2)$. In the interior disk of radius three each removed factor is bounded below by a constant times its capped distance from its root, as in [the contour construction](weil-contour-nov18.md). The polynomial-distance lower bound gives the asserted reciprocal estimate. The bounded central portion of the chosen line uses compactness. Horizontal contours tending to both infinities can likewise be chosen polynomially separated in ordinate from all zeros. The standard logarithmic derivative bound on these lines and the superpolynomial decay of $W$ justify the shift for each fixed $U$.

For the $U$ dependence on the left line, use $\vartheta(v)-v\ll_\epsilon v^{\Theta+\epsilon}$, from the same shifted Perron argument at $\tau=0$ with a line strictly to the right of $\Theta$ (or $\vartheta(v)\ll v$ if $\Theta=1$). Ordinary partial summation with $v^{-s}$ now gives $|D_{\le U}|\ll_\epsilon(1+|\Im s|)(1+U)^{\Theta+\epsilon-\alpha}$. The constants on the new line are integrable after multiplication by $W$. Thus the compact convolution satisfies, for a fixed nonzero $C_\rho$ independent of $U$,

$$
 (K*A_U)(t)=C_\rho e^{(\rho-1/2)t}
 +O_{\rho,K,\epsilon}\!\left(e^{(\alpha-1/2)t}
                  [1+(1+U)^{\Theta+\epsilon-\alpha}]\right).
                                                                    \tag{5}
$$

For $\kappa<1$, first choose an open interval of possible $\alpha$ strictly between $1/2$ and $\Theta$. Every $\beta$ sufficiently close to $\Theta$ then admits an $\alpha$ in that interval and an $\epsilon>0$ such that $\alpha+\kappa(\Theta+\epsilon-\alpha)<\beta$. Equation (5) and Cauchy–Schwarz on the support of $K$ give a local lower norm bound $\gg_\rho e^{(\beta-1/2)t}$ for $A_U$, uniform over $U\le e^{\kappa t}$. Division by $t+w$ only costs a polynomial factor. Taking the supremum over such $\beta$ proves (1).

### The interval at the moving cutoff

For (2) fix $0<\delta<1/2$. If $U\le b^{2(1-\delta)}$, use (1) on a fixed window just inside the upper end, with any $\kappa$ strictly between $1-\delta$ and one. If $b^{2(1-\delta)}<U\le b^2/2$, use the interval $(\log U,\log(2U))$ instead. There $m(e^t/v)=1$ for every $U<v\le e^t$, so in distributions on this open interval

$$
 (\partial_t-1/2)A_U(t)=D(t).
$$

Here $D$ is the ordinary centered prime measure, since the argument remains above $U$. For any fixed off-line zero, apply the same compact contour construction to $D(z)$ alone, keeping the selected point and placing simple zeros at every other off-line pole to the right of $\alpha<\beta$. The selected residue is $-m$ times a nonzero test value, the left contour is $O(e^{(\alpha-1/2)t})$, and the kernel can have support in $(-(\log2)/4,(\log2)/4)$. Pair the last distributional identity at the midpoint of the interval with this kernel, transferring the derivative to the test. Cauchy–Schwarz gives the annular norm of $A_U(v)/v$ at least $c_\rho U^{\beta-1/2}/\log(2U)$, uniformly in $U$. For large $b$ the entire test lies in $[L,2L]$. Taking the supremum over $\beta$ and then letting $\delta\downarrow0$ proves the uniform lower exponent in (2).

**Verification scope.** These are analytic implications for the signed native source and include the matching continuous term. The difficult estimate is still an unconditional subpower upper bound. No numerical data or zero-location assumptions beyond the named classical unconditional inputs enter the exponent identities.
