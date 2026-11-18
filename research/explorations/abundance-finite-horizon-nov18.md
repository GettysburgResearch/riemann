# A finite sign sandwich for the two limiting abundance moments

**Proposed unconditional finite theorem.** Let $s=x\log x$ and $1000\le L=\log x\le300000$. For the limiting log moments and prime-free continuous comparison in the [abundance-distribution theorem](abundance-curvature-nov18.md),
$$
 W_\sigma(s)< W_*(s)< W_\phi(s).
 \tag{1}
$$
All moment orders in that continuous range are included. The only zero-census input is the published critical-line verification to $H=3\cdot10^{12}$. The width in $\log x$ is much larger than in a sharp primorial cutoff because this moment has an analytic transition. In (1) $W_*$ is a deterministic integral and a linear term. The finite result is for log moments; the separate distribution-tail statements use an asymptotic saddle estimate.

## Exact centering and the explicit formula

For $u>0$ put
$$
 z(u)=u+(s+1)\log(1-e^{-u}),\qquad h(u)=1-\log(1+e^{z(u)})/u ,
$$
and extend $h(u)=1$ for $u\le0$. On $v=e^u>1$, $h=(s b(v)-f_s(v))/\log v$, where $f_s(v)=\log(1+(e^{s b(v)}-1)/v)$. Thus $0\le h\le1$ on the real line and its upper tail is $O(s e^{-u}/u)$. The centering constant $c$ is the limiting integral of $b$ against $d\pi-dv/\log v$ from 2. Consequently
$$
 W_\phi(s)-W_*(s)=
 -\int_{[2,\infty)}h(\log v)(d\psi(v)-dv)
 +P_s,\qquad P_s=\sum_{k\ge2,p}\log p\ h(k\log p).
 \tag{2}
$$
All improper differences converge by the prime number theorem. Extending the displayed signed integral down from 2 to 1 changes it by at most 1 in absolute value. Integrate by parts against $\psi(v)-v$ and use the von Mangoldt formula for $\psi$. The resulting nontrivial-zero term, with the minus sign from (2) included, is
$$
 \sum_\rho\frac{-1}{\rho}\int_0^\infty e^{\rho u}h'(u)du
 =\sum_\rho\frac1{\rho(1-\rho)}
             \int_{\mathbb R}e^{\rho u}k_s(u)du ,
 \qquad k_s=-h''-h'.                                      \tag{3}
$$
The extension gives $h'=0$ on the negative half-line and no derivative atom at zero. The identity follows by two integrations by parts on the full line. The resulting series converges absolutely by the estimates below. Equivalently one obtains (3) first for compact smooth cutoffs in the distributional explicit formula and takes limits; on the upper tail the $e^u$-weighted derivatives $h''+h'$ are integrable and cutoff errors vanish for each zero, with a uniform bound per reciprocal-square coefficient (choose cutoff widths comparable to their locations).

The remaining terms cost less than 5 in absolute value. The lower integration boundary contributes $-1$, the constant $-\log(2\pi)$ contributes $\log(2\pi)$, and the trivial zeros cost at most $\tfrac12(2/s-\log(1-e^{-2}))$. For this last bound integrate $\log(1-e^{-2u})h'(u)$ by parts using $h-1$; for $0<u<1$ we have $|h-1|\le2u^s$ and $2/(e^{2u}-1)\le1/u$, while above one use $|h-1|\le1$. Include the change from 1 to 2 already noted.

On the verified critical ordinates the [real-kernel estimate](abundance-low-zero-kernel-nov18.md) gives $\int e^{u/2}|k_s(u)|du<1.70\sqrt x$. The sum of the corresponding reciprocal weights is below $0.047$ even under finite verification. Indeed $\sum_\rho\Re(1/\rho)=1+\gamma_E/2-\log(4\pi)/2$, each verified $1/|\rho|^2=2\Re(1/\rho)$, and all omitted real parts are positive. Thus the required sum is at most $2+\gamma_E-\log(4\pi)<0.047$. Their absolute total in (3) is below $0.080\sqrt x$.

## An explicit contour estimate above the census

For $0<\beta<1$ and $|\gamma|>H$ we show
$$
 \left|\int_{\mathbb R} k_s(u)e^{(\beta+i\gamma)u}du\right|
 \le 10^4 L^3+e^{3L-|\gamma|/(8L)} .
 \tag{4}
$$
On $0<u<1$ write $r=(e^u-1)(1-e^{-u})^s$. With $a=1-e^{-1}<0.633$, the elementary product rule bounds $|r|,|r'|,|r''|\le 20(s+1)^2u^3a^{s-5}$. Indeed two differentiations lower the power at most two, and $(1-e^{-u})^{s-2}\le u^3 a^{s-5}$. Differentiation of $h=1-\log(1+r)/u$ then gives $|k_s|<1$ in this interval for $L\ge1000$.

On $\Re w=u\ge0.9$, $|\Im w|\le1/(4L)$, use the principal logarithm for $\log(1-e^{-w})$. When $u\le L-1$,
$$
 \log|1-e^{-w}|\le-0.75e^{-u},\qquad \Re z\le -L .
$$
The first follows by squaring and using $2\cos(1/(4L))-e^{-0.9}>1.5$; the second is worst at $L-1$. In $[L-1,L+1]$ one has $|\Im z|\le |\Im w|(1+2(s+1)e^{-u})<1.4<\pi/2$, using the derivative of the analytic log along the vertical segment. For $u\ge L+1$, $\Re z\ge u-2(s+1)e^{-u}>L/4$. These inequalities give a holomorphic determination of $\log(1+e^z)$ agreeing with the real one: use its small exponential on the left, the principal log in the middle, and $z+\log(1+e^{-z})$ on the right. They also give $|h(w)|<6L$ for $0.9\le u\le2L+1$, by direct application in the three ranges. Cauchy's estimate at radius $1/(16L)$ now yields $|k_s(w)|<4000L^3$ on $1\le u\le2L$, $|\Im w|\le1/(8L)$.

For $u\ge2L$ on that smaller strip, use the right-hand representation. On a complex disk of radius $1/4$ about each such point,
$$
 h(w)=s e^{-w}/w+O(20(s+1)^2 e^{-2\Re w}/|w|).
$$
Indeed $|e^{-w}|<2e^{-2L}$ on the disk, $|(s+1)e^{-w}|<1/10$, and expansion of $-(s+1)\log(1-e^{-w})-\log(1+e^{-w}(1-e^{-w})^{-(s+1)})$ has first term $s e^{-w}$ and an error bounded by $20(s+1)^2|e^{-w}|^2$ using the geometric and exponential series. Cauchy differentiation of the error therefore bounds
$$
 |k_s(w)|\le s e^{-u}(u^{-2}+2u^{-3})+2000(s+1)^2e^{-2u}.
$$
Its integral against $e^{\beta u}$ on $u\ge2L$ is at most $s(1/(2L)+1/(4L^2))+2000(s+1)^2e^{-2L}$. Combining with the previous strip bound yields $\int_1^\infty e^{\beta u}|k_s(u+i\theta)|du<e^{3L}$ on $|\theta|\le1/(8L)$.

Move the ray starting at 1 by $i\operatorname{sgn}(\gamma)/(8L)$. Its vertical connector costs at most $e\cdot4000L^3/(8L)$ since the phase decays on that side, and the end at infinity vanishes by the tail bound. Adding back $[0,1]$ proves (4). For the entire stated range $3L-H/(8L)<0$. The signed-ordinate tail bound $\sum_{|\gamma|>H}1/(|\rho||1-\rho|)<3.1\cdot10^{-12}$ from the [finite Robin calculation](robin-smoothed-nov18.md) gives a total smaller than $0.001\sqrt x$ in (3), even using $L\le300000$ in the polynomial and $x\ge e^{1000}$ in the comparison.

Finally the [square-prime and local exponent estimates](abundance-curvature-sigma-nov18.md) give $1.97\sqrt x<P_s<2.001\sqrt x$ and $W_\phi-W_\sigma>2.80\sqrt x$ throughout the range. Equations (2)–(4) and the archimedean bound put $W_\phi-W_*$ strictly between $1.88\sqrt x$ and $2.09\sqrt x$. This proves (1).

## Wider analytic strip and a finite comparison for the actual tails

The [sharper contour estimate](abundance-low-zero-kernel-nov18.md) uses a shift of $3.10/L$ and bounds the shifted norm by a polynomial in $L$ times $e^L$. It extends (1), with the same bounds $1.88\sqrt x<W_\phi-W_*<2.09\sqrt x$, to
$$
 1000\le\log x\le4,300,000 .
 \tag{5}
$$
The exponent relative to $\sqrt x$ is now $L/2-3.10H/L$, below $-12000$ even at the final endpoint. The polynomial and vertical-connector losses are accounted for in the linked estimate.

Throughout the finite threshold interval
$$
 1100\le \ell=t e^{-\gamma_E}\le4,299,900
 \tag{6}
$$
the actual Weingartner errors satisfy
$$
 \log A_{\sigma(n)/n}(t)<-y+\min_{s\in J_y}I(y,s)
 <\log A_{n/\varphi(n)}(t),\qquad y=e^\ell .
 \tag{7}
$$
We prove the lower spending estimate for the totient tail explicitly; a sign comparison for the two moments alone does not give (7).

At $s=xL$ in (5), $|W_\phi'(s)-\gamma_E-\log L|<5/L$. Indeed the [Mertens tangent identity](robin-tangent-nov18.md) and $|\vartheta(v)-v|\le0.0244v/(\log v)^3$ give $|\sum_{p\le x} b(p)-\gamma_E-\log L|<0.01/L^3$ by absolute integration and the elementary bound on the omitted prime-power tail. The transition in $[x/2,2x]$ costs at most $4.1/L$ using $b(p)\le 1/(p-1)$ and the same upper bound for $\vartheta(2x)$. Below $x/2$ the loss costs $O(1/x)$, explicitly at most $2/x$, from $1-(1+(p-1)e^{-sb})^{-1}\le p e^{-s/p}$. Above $2x$ the sum is at most $4 x^{0.51}\sum_{n>2x}n^{-2}<3x^{-0.49}$. These inequalities and monotonicity place the actual totient saddle $s$, where $W_\phi'(s)=\log t$, strictly inside (5) for (6). The [effective continuous-model calculation](abundance-weingartner-model-nov18.md) places the model saddle $s_*$ in $J_y$, hence likewise inside (5) when written $s_*=x_*\log x_*$. It gives $|I_*(\log t)-(-y+\min_{J_y}I)|<10$.

Under the totient distribution tilted by $e^{sX-W_\phi(s)}$, $X$ is a sum of independent Bernoulli scores $b(p)$. Write $V=W_\phi''(s)$ for its variance. The following deliberately loose bounds suffice:
$$
 0.01/(xL^2)\le V\le11/x,\qquad
 \sum_p\mathbb E_s|X_p-\mathbb E_s X_p|^3\le30/x^2 .
$$
For $p\le x/2$, the Bernoulli variance factor $q(1-q)$ is at most $p/x^2$, and $b(p)\le2/p$. The centered third moment in absolute value is at most $b(p)^3 q(1-q)$. Above $x/2$ use the convergent tails of $4/n^2$ and $8/n^3$ over integers. For the lower bound the theta estimate just cited gives at least $0.09x/L^2$ primes between $x$ and $x(1+1/(10L))$ (the endpoint theta error is below $0.06x/L^3$). On this interval $-0.12<s b(p)-\log(p-1)<0.01$, so $q(1-q)>0.2$ and $b(p)>0.99/x$.

The independent-summand Berry–Esseen inequality now bounds the Kolmogorov error by $3\cdot10^6 L^3/\sqrt x$ (even the universal constant 100 suffices). Apply it first to finite prime sums and pass to the convergent variance and mean limits. The standard normal probability of $[0,0.1/L]$ exceeds $0.03/L$. Therefore the tilted probability of
$$
 0\le X-\log t\le 0.1\sqrt V/L
$$
exceeds $0.02/L$ on (5). Undoing the tilt shows
$$
 \log A_{n/\varphi(n)}(t)\ge W_\phi(s)-s\log t
     -0.34\sqrt x-\log(50L)>I_*(\log t)+10 .
$$
Here $0.1s\sqrt V/L<0.34\sqrt x$, and the moment gap is greater than $1.88\sqrt x$. For the divisor sum no inversion estimate is needed: the exponential Markov inequality at $s_*$ gives $\log A_{\sigma(n)/n}(t)\le W_\sigma(s_*)-s_*\log t<I_*(\log t)-10$ by the uniform gaps in (5). This proves (7). The limiting natural densities and the comparison function are those in Weingartner's Theorem 2; (7) is unconditional on this finite real interval.
