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

## A lower bound on short-interval prime variance at every large center

Suppose $\rho=\beta+i\gamma$ is any zero with $\beta>1/2$. Fix $w>0$. For all sufficiently large real $X$, uniformly for every real $0<\delta\le1$,
$$
\left(\int_{Xe^{-w}}^{Xe^w}
\left|\vartheta(e^\delta y)-\vartheta(y)-(e^\delta-1)y\right|^2\frac{dy}{y}\right)^{1/2}
\gg_{\rho,w} \delta X^\beta .
\tag{4}
$$
Here $\vartheta(y)=\sum_{p\le y}\log p$, with no prime powers. This is a conditional lower bound on the actual source at each center, in a range that includes arbitrarily small multiplicative steps.

Indeed put $B(v)=\vartheta(e^v)-e^v$ and take the isolating test of steps 1–2 with $1/2<\sigma_0<\alpha<\beta$. On our large-center windows $dB=\nu$. The convolution of $K'$ with $[B(\cdot+\delta)-B]/\delta$ at $t=\log X$ is the difference quotient of $(K*\nu)(t)$. Its integral on the line $\Re s=2$ uses the additional factor $U_\delta(s)=(e^{\delta s}-1)/\delta$. On the contour strip, $|U_\delta(s)|\le e^2 |s|$ by the integral representation $s\int_0^1e^{\delta s v}dv$. At $\rho$ one has $|U_\delta(\rho)|\ge (e^{\beta\delta}-1)/\delta\ge\beta$. The same shift therefore gives a main term of absolute size at least $m_\rho|W(\rho)|\beta X^\beta$ and a remainder $O_{\rho,w}(X^\alpha)$ uniformly in $\delta$. Cauchy–Schwarz against $K'$ proves (4).

For example, let $X_j\to\infty$ be arbitrary and let $\delta_j=X_j^{-\eta+o(1)}$ with $0\le\eta\le1$ and $0<\delta_j\le1$. If the left side of (4) along the sequence has the root-interval-length bound $(X_j\delta_j)^{1/2}X_j^{o(1)}$, every zero satisfies $\beta\le(1+\eta)/2$. This is a sufficient arithmetic input. A classical almost-all prime asymptotic with relative $o(1)$ error in the interval length has a different error scale.

## Positive tests and both signs on every sufficiently wide window

If $\zeta$ has any zero of real part $\beta>1/2$, there are constants $C>1$, $c>0$, and $X_0$ such that for every $X\ge X_0$ the function $\vartheta(y)-y$ takes values $\ge cX^\beta$ and $\le-cX^\beta$ in $[X,CX]$. For every $0<\delta\le1$, the function
$$
D_\delta(y)=\vartheta(e^\delta y)-\vartheta(y)-(e^\delta-1)y
$$
takes values of both signs there at respective amplitudes at least $c\delta X^\beta$. The constants are uniform in $\delta$. Both positive and negative parts also have logarithmic integral $\gg\delta X^\beta$ on this interval. This signed statement uses a wider test whose support can depend on the actual zero set.

Keep among zeros on the vertical line $\Re s=\beta$ one $\rho=\beta+i\gamma$ of smallest positive ordinate (there are no nontrivial real zeros). Choose $1/2<\alpha<\beta$ with the separation of step 1 and consider all distinct zeros $z=\beta_z+i\gamma_z$ with $\Re z>\alpha$, $\gamma_z>0$, other than $\rho$. For each set $\ell_z=\pi/\gamma_z$ and take the probability measure
$$
\mu_z=\frac{\delta_0+e^{\beta_z\ell_z}\delta_{\ell_z}}
 {1+e^{\beta_z\ell_z}}.
$$
Its Laplace transform vanishes at $z$ and $\bar z$. It does not vanish at $\rho$: a vanishing would require $\beta_z=\beta$ and $\gamma/\gamma_z$ to be a positive odd integer, whereas each remaining zero on this same line has $\gamma_z>\gamma$. The density bound gives $\sum_z\ell_z<\infty$ by partial summation. The distribution of the sum of independent random variables with respective laws $\mu_z$ is therefore supported in $[0,\sum_z\ell_z]$. Its transform is the corresponding product and is nonzero at $\rho$, since on compact sets its factors differ from 1 by $O(\ell_z)$ apart from finitely many.

Convolve this probability measure with a nonnegative smooth probability density supported in a sufficiently short interval $[0,\epsilon]$ so its transform is nonzero at $\rho$ (take $\gamma\epsilon<\pi/2$). The resulting real $K\ge0$ lies in $C_c^\infty([0,S])$ for some finite $S$. Its transform $W$ has every zero required in step 2 except the retained conjugate pair. It decays faster than any power on the contour strip by integration by parts.

Extend $B(v)=\vartheta(e^v)-e^v+2$ by zero below $\log2$. Its distributional derivative is $\nu$, so its transform is $V(s)/s$. The compact smoothed $B$ and $[B(\cdot+\delta)-B]/\delta$ have contour shifts as in step 2, respectively with extra multipliers $1/s$ and $U_\delta(s)/s$. The main terms are the real conjugate-pair sums
$$
2\Re(A e^{\rho t}),\qquad
2\Re(A U_\delta(\rho)e^{\rho t}),\qquad
A=-m_\rho W(\rho)/\rho\ne0.
$$
The errors are $O(X^\alpha)$ when $t=\log X+O(1)$, uniformly in $0<\delta\le1$ by the preceding multiplier estimate. Since $|U_\delta(\rho)|\ge\beta$, both phases can separately be made to attain each extremal sign as $t$ runs through $[\log X+S,\log X+S+2\pi/\gamma]$. Each signed smoothed value has magnitude $\gg X^\beta$ there. Positivity and unit integral of the kernel yield sample points of each sign in $[X,CX]$, for $C=\exp(S+2\pi/\gamma)$. The fixed additive constant 2 in $B$ is negligible for large $X$. Boundedness of $K$ also bounds each signed average by $\|K\|_\infty$ times the logarithmic integral of the corresponding one-sided part, giving the integral assertion.

## An unconditional bounded-gap consequence at fixed amplitude

For every fixed $H>0$ there exist $C_H>1$ and $X_H$ such that every interval $[X,C_H X]$, $X\ge X_H$, contains points $y_+,y_-$ for which
$$
\vartheta(y_+)-y_+>H\sqrt{y_+},\qquad
\vartheta(y_-)-y_-<-H\sqrt{y_-}.
\tag{5}
$$
The constants are qualitative. The argument imports Littlewood's classical unbounded oscillation theorem $\psi(y)-y=\Omega_\pm(\sqrt y\log\log\log y)$ as well as the von Mangoldt explicit formula. Equation (5) concerns bounded logarithmic gaps at each fixed amplitude and gives no uniform growth rate for $H$ as a function of $X$.

If RH fails, the preceding signed theorem gives (5), since $X^\beta/\sqrt{C X}\to\infty$. Suppose now that RH holds. In the distributional form of the classical explicit formula on $t>0$,
$$
F(t)=e^{-t/2}(\psi(e^t)-e^t)
=-\sum_\rho e^{i\gamma t}/\rho +r(t),\qquad
r(t)=-e^{-t/2}\left(\log(2\pi)+\tfrac12\log(1-e^{-2t})\right).
$$
The convention at isolated prime-power discontinuities is immaterial. For every fixed nonnegative smooth compactly supported kernel $K$ of integral 1, the smoothed zero sum converges uniformly and absolutely on the whole real line: integration by parts gives rapid decay of its Fourier multiplier and the zero count is $O(T\log T)$. Hence this smoothed sum is a uniformly almost periodic function of $t$. Also $K*r(t)\to0$ as $t\to\infty$, and if $K$ has support in $[-1,1]$ its absolute value for $t\ge2$ is at most $\sup_{u\ge t-1}|r(u)|$.

By Littlewood choose large continuity points at which $F$ exceeds $H+5$ and falls below $-H-5$ respectively, with $|r|<1$ on their unit neighborhoods. Such continuity points can be chosen because a strict one-sided inequality at a prime power persists on a neighboring one-sided open interval. Choose a smooth nonnegative kernel supported sufficiently close to 0 that the two smoothed values still exceed $H+4$ and fall below $-H-4$. The almost periodic function contributed by the zeros has values exceeding $H+3$ and below $-H-3$ at those two points. Its 1-almost periods are relatively dense, so each inequality with margin $H+2$ occurs in every sufficiently long real interval. At all sufficiently large times the vanishing remainder transfers the claims to the convolution of $F$ with thresholds $\pm(H+1)$, and positivity of $K$ transfers them to values of $F$ in an interval longer by at most 2. One may start the argument with $H+2$ in place of $H$ to absorb the prime powers, since $(\psi(y)-\vartheta(y))/\sqrt y=1+o(1)$ by the prime number theorem and the elementary bound for powers of order at least three. Exponentiating the resulting fixed length gives (5).

This argument establishes no effective numerical value of $C_H$ or $X_H$, and makes no claim of historical priority.
