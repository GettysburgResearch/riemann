# Compact tests isolating a single off-line zero in the prime discrepancy

**Status.** Proposed analytic lemma, unreviewed. The arithmetic inputs are Ingham's zero-density theorem, the classical local partial fraction estimate for $\zeta'/\zeta$, and the classical prime-counting bound under RH. The functional-analytic input is the $L^2$ Paley–Wiener theorem for entire functions of exponential type. This lemma supplies a necessary local consequence of an off-line zero. It gives no unconditional square-root bound for the actual discrepancy.

Let $E(y)=\pi(y)-\int_2^y du/\log u$. Fix $w>0$, $a>1/2$, and an unbounded sequence of real centers $t_j\to\infty$. Write $d_j\ge0$ for integral degrees. Suppose there are polynomials $P_j$ of those degrees or less such that
$$
\| E(e^{t_j+u})-P_j(u)\|_{L^2(-w,w)}\le \exp((a+o(1))t_j).
$$
If $\lambda=\liminf_j d_j\log(d_j+2)/t_j<\infty$, then $\zeta$ has no zero with real part greater than $a+\lambda$. In particular for $\lambda=0$ the hypothesis along these centers, for each $a>1/2$, is equivalent to RH. The centers may be arbitrarily sparse. The width is fixed in this first statement. A shrinking-window version appears below. The approximation is on a fixed logarithmic interval and is compatible with arbitrary additive levels per interval.

**1. Construct a local zero-isolating test.** Suppose a zero $\rho=\beta+i\gamma$ satisfies $\beta>a+\lambda$. Choose $1/2<\sigma_0<a$ with $\sigma_0<1$. Ingham's bound
$$
N(\sigma_0,T)\ll T^{3(1-\sigma_0)/(2-\sigma_0)}(\log T)^5
$$
gives $N(\sigma_0,T)=O(T^k)$ for some $k<1$. By conjugation this applies at negative ordinates as well. Choose $k<q<1$ so close to 1 that $\lambda/q<\beta-a$.

Select a line $\alpha\in(\sigma_0,\min(a,1))$ at positive distance $\gg(1+|\Im z|)^{-3}$ in real part from every nontrivial zero $z$. More explicitly, take a closed interval strictly inside this open interval. The total lengths excluded around real parts by intervals of radii $c(1+|\Im z|)^{-3}$ are less than its length for sufficiently small $c$, since the full zero count is $O(T\log T)$. This provides a fixed $\alpha$.

Let $Z$ be the distinct zeros of real part greater than $\alpha$ other than $\rho$. Their counting function is $O((1+r)^k)$. Form the entire product
$$
P(s)=\prod_{z\in Z}(1-s/z).
$$
It converges normally and is nonzero at $\rho$. Integrating $\log(1+r/|z|)$ against the counting function bounds $\log|P(s)|\le C(1+|s|)^k$ (one can enlarge $k$ within $(k,q)$ if needed). Multiple zeta zeros only require one product zero because the logarithmic derivative has simple poles.

Take $b_m=B m^{-1/q}$ with $B>0$ chosen so $\sum b_m<w$, and form
$$
J(s)=\prod_{m\ge1}\frac{\sinh(b_m s)}{b_m s}.
$$
The value at zero of each factor is 1. Normal convergence follows from $\sum b_m^2<\infty$. All factor zeros lie on the imaginary axis and $J(\rho)\ne0$. Each factor is bounded by $e^{b_m|\Re s|}\min(1,1/(b_m|s|))$ by its interval-average representation and the elementary bound on $|\sinh|$. When $m\le(B|s|/2)^q$, the minimum is at most $1/2$. Thus $W=PJ$ is entire of exponential type strictly less than $w$, and on every fixed bounded vertical strip
$$
|W(s)|\le C\exp(-c|\Im s|^q).
$$
Paley–Wiener applied on the imaginary axis yields $W(s)=\int K(u)e^{-s u}du$ with $K$ supported in $[-w,w]$. Fourier inversion gives $K\in C_c^\infty$, possibly complex. In particular on every bounded vertical strip, for fixed $M$ and integers $n\ge0$,
$$
\int_{-\infty}^\infty (1+|s|)^{M+n}|W(s)|\,d\Im s
\le \exp\big((n/q)\log(n+2)+O(n+1)\big).
\tag{1}
$$
This follows by a gamma integral and Stirling's formula. The bound with $M=1$ controls both $K^{(n)}$ and $K^{(n+1)}$ in sup norm by Fourier inversion.

**2. Recover the observable.** On $v\ge\log2$ put $\nu(dv)=v\,dE(e^v)$, extending the prime counting step from the left by zero with its atom at $\log2$. Its Laplace transform, initially on $\Re s>1$, is
$$
V(s)=-\frac{\zeta'}{\zeta}(s)-
\sum_{p}\sum_{m\ge2}(\log p)p^{-ms}-\frac{2^{1-s}}{s-1}.
$$
This follows directly from the atoms $\log p$ and continuous density $-e^v$. The pole at 1 cancels, the prime-power series converges locally absolutely for $\Re s>1/2$, and the pole at $\rho$ has residue $-m_\rho$.

For any $t$ and $n\ge0$ the inverse transform on $\Re s=2$ of $s^nW(s)V(s)$ is $(K^{(n)}*\nu)(t)$. Fourier inversion and absolute convergence justify interchange there. Move the contour to $\alpha$. All poles crossed except $\rho$ are removable in this product. The classical local expansion $\zeta'/\zeta(s)=\sum_{|\Im z-\Im s|\le1}(s-z)^{-1}+O(\log(2+|\Im s|))$ at large height, uniformly on the bounded strip used here, gives polynomial growth on the chosen line by its separation from zero real parts. For horizontal contours take heights tending to positive and negative infinity at distance $\gg(1+|\Im s|)^{-3}$ from zero ordinates (choose an available height in successive unit intervals using the full counting estimate). The same polynomial growth holds there and $W$ decays faster than any reciprocal power. The shift for each $n$ followed by (1) thus gives
$$
(K^{(n)}*\nu)(t)=-m_\rho\rho^n W(\rho)e^{\rho t}
+O\!\left(\exp\left(\alpha t+(n/q)\log(n+2)+O(n+1)\right)\right)
\quad(t>0).
\tag{2}
$$
The constants in the error depend on the zero, the line, the strip and the test, independently of $n,t$.

**3. Compare with the polynomial fits.** Restrict to a subsequence attaining $\lambda$, and take $n=d_j+1$, $t=t_j$. Since $vP'_j(v-t)$ has degree at most $d_j$, its integral against $K^{(n)}(t-v)$ is zero by integration by parts. Subtract $P_j$ inside the distributional derivative defining $\nu$ on the support of the test. Integration by parts and Cauchy–Schwarz yield
$$
|(K^{(n)}*\nu)(t)|\le
\|E(e^{t+u})-P_j(u)\|_2\,
\big\|\tfrac{d}{dv}[vK^{(n)}(t-v)]\big\|_{L^2(t-w,t+w)}
\le \exp((a+\lambda/q+o(1))t).
$$
Indeed $n=o(t)$ along this subsequence and (1) controls the second factor. In (2) the error has exponential rate at most $\alpha+\lambda/q<\beta$. The residue term has absolute value $\exp((\beta+o(1))t)$ since $W(\rho)\ne0$. This contradicts $a+\lambda/q<\beta$. The converse for $\lambda=0$ under RH follows by taking $P_j=0$ and using $E(y)=O(\sqrt y\log y)$.

The [single-pair model](causal-polynomial-nov18.md) reaches the additive loss $\lambda$ at exponential scale. It illustrates the sharpness of arguments based only on isolated Mellin poles. It makes no assertion about whether the actual prime source attains a positive loss.

## Shrinking logarithmic windows

Let $0<w_j\le1$ with $\log(1/w_j)/\log t_j\to r\ge0$. Replace the approximation interval above by $(-w_j,w_j)$ and keep its ordinary unnormalized $L^2$ norm. With the same $a,\lambda$ this implies
$$
\Re\rho\le \max\!\left(a,\frac{1+3r}{2+3r}\right)+(1+r)\lambda
\quad\text{for every nontrivial zero }\rho .
\tag{3}
$$
In particular full RH detection survives on any chosen unbounded sequence of shrinking windows with $w_j=t_j^{-o(1)}$ and $d_j\log(d_j+2)=o(t_j)$, when the fitted estimates hold for every $a>1/2$. The conditional converse remains immediate. Dividing the norm by $\sqrt{2w_j}$ has no effect on any exponential rate here.

Indeed let $b=\max(a,(1+3r)/(2+3r))$ and assume $\beta>b+(1+r)\lambda$. Choose $\sigma_0,\alpha$ slightly above $b$ and below $\beta$, with $\sigma_0<\alpha<1$. Then $3(1-\sigma_0)/(2-\sigma_0)<1/(1+r)$. One can choose $k$ strictly between these two numbers and $q<1$ sufficiently close to one that
$$
r<1/k-1/q,\qquad \alpha+(r+1/q)\lambda<\beta .
$$
Keep the zero-canceling $P$ fixed and use $W_j(s)=P(s)J(w_js)$ with the base $J$ constructed using $\sum b_m<1$. Paley–Wiener gives support in $[-w_j,w_j]$ and $|W_j(\rho)|$ is bounded below: $J(v\rho)$ is continuous and nonzero for $0\le v\le1$. The smoothed formula now uses a different test for each $j$ but the same line and the same isolated pole. On any bounded vertical strip, optimizing $Cz^k-(c/2)w_j^qz^q$ for $z\ge0$ gives
$$
|W_j(s)|\le C\exp\left(C w_j^{-qk/(q-k)}-c'|w_j\Im s|^q\right).
$$
Consequently the logarithm of the moment integral in (1) is at most
$$
Cw_j^{-qk/(q-k)}+(M+n+1)\log(1/w_j)
 +(n/q)\log(n+2)+O_M(n+1).
$$
The first term is $o(t_j)$ by the strict bound on $r$. Along the subsequence attaining $\lambda$ the second term divided by $t_j$ tends to $r\lambda$: for $\lambda>0$, $n\sim\lambda t_j/\log t_j$, and for $\lambda=0$, $n=o(t_j/\log t_j)$ (including bounded $n$). Thus the derivative and shifted-contour costs have exponential rate at most $(r+1/q)\lambda$. Substitution into steps 2 and 3 contradicts the assumed $\beta$, proving (3). A subinterval of an actual first octave may be centered this way as long as it stays inside the octave in logarithmic coordinates.

This is a bound for the variation of the cumulative prime error throughout each selected interval. The existence of many intervals having one accurate endpoint difference $\pi(x+h)-\pi(x)-\int_x^{x+h}du/\log u$ does not control that $L^2$ quantity. Nor does relative error $o(h/\log x)$ reach the exponent in the hypothesis when $h=x/(\log x)^{r+o(1)}$.
