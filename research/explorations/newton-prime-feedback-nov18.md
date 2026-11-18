# Absorbing prime powers and a growing prime range in the Möbius evolution

**Status.** Proposed unconditional component bounds for the native all-integer energy on Newton stages. The discrepancy over the remaining ordinary primes is unbounded by this argument. RH and a subquadratic energy recurrence remain open.

## Native source and logarithmic evolution

Use $m(x)=\sum_{n\le x}\mu(n)/n$, with $m(x)=0$ for $x<1$. Write $M(x)=\sum_{n\le x}\mu(n)$. For integer $N\ge1$,

$$
 u_N=m(N)-M(N)/(N+1),\quad E_N=\sum_{k\le N}M(k)^2/[k(k+1)],
 \quad A_N=E_N+2(N+1)u_N^2.
$$

The ordinary innovation identity gives $F_N=\sum_{k\le N}m(k)^2=E_N+(N+1)u_N^2$, hence $F_N\le A_N\le2F_N$. This follows also by differencing in $N$, using $u_N-u_{N-1}=M(N)/[N(N+1)]$, $N\ge2$, and checking $N=1$. With $f(t)=e^{t/2}m(e^t)$ for $t\ge0$, extended by zero on $t<0$, change of variable gives $\int_0^{\log(N+1)}|f|^2=F_N$. At $Y=b-1$, $B=b^2-1$, and $L=\log b$ the known prefix is the interval $[0,L)$ and the new portion is $[L,2L)$. This is the ordinary Möbius energy of [BNR26 and its innovation continuation](https://github.com/GettysburgResearch/riemann/tree/7de75c02417d5d8db7eafb1ceba364380e72d16a/standalone/2026-09-10-astra-balanced-newton).

For causal convolution on the real line let

$$
 D=\sum_p(\log p)p^{-1/2}\delta_{\log p}-1_{u\ge0}e^{u/2}\,du,
 \qquad Q=\sum_p\sum_{k\ge2}(\log p)p^{-k/2}\delta_{k\log p}.
$$

For $t>0$ the exact equation is

$$
 t f(t)=-[(D+Q)*f](t).                                      \tag{1}
$$

Indeed $\mu(n)\log n=-(\Lambda*\mu)(n)$ follows by differentiating $1/\zeta(s)$ for real $s>1$ and comparing coefficients. Also $\sum_{n\le x}\mu(n)\log(x/n)/n=\int_1^x m(v)\,dv/v$. Their sum gives $\log x\,m(x)=\int_1^x m(x/v)\,dv/v-\sum_{n\le x}\Lambda(n)m(x/n)/n$. Multiplication by $\sqrt x$ gives (1). All terms before transformation are finite on every bounded horizon.

## The sharp norm of higher-prime-power feedback

Let $T_L h=1_{[L,2L]}(t)(Q*(h1_{[L,2L]}))(t)/t$ with ordinary Lebesgue $L^2$ norm. As $L\to\infty$,

$$
 \|T_L\|=\sigma_*+O(L^{-1}),\qquad
 \sigma_*=\frac1{2\sqrt{1/4+\omega^2}},\qquad
 \tfrac12\sin(\omega\log2)+\omega\cos(\omega\log2)=0,           \tag{2}
$$

where $\pi/2<\omega\log2<\pi$. In particular $\sigma_*<\log2/\pi$. Numerically the displayed scalar formula gives approximately $0.19270913$.

Under unitary rescaling $t=Lx$, $1\le x\le2$, the operator is $T_\nu h(x)=x^{-1}\int_{[0,x-1]}h(x-z)\,d\nu_L(z)$, with $\nu_L$ the pushforward of $Q|_{[0,L]}/L$ by $u\mapsto u/L$. Uniformly for $0\le z\le1$,

$$
 \nu_L([0,z])=z/2+O(1/L).
$$

The square terms give this by Mertens' estimate $\sum_{p\le w}(\log p)/p=\log w+O(1)$ for $w\ge2$, treating smaller $w$ directly. The total mass of $k\ge3$ is bounded by $\sum_p(\log p)p^{-3/2}/(1-p^{-1/2})<\infty$. For every fixed $C^1$ function $h$ on $[1,2]$, partial summation therefore gives uniform error $O_h(1/L)$ in replacing $T_\nu h$ by

$$
 Vh(x)=\frac1{2x}\int_1^x h(y)\,dy .
$$

The same is true of the adjoints on $C^1$ functions because $T_\nu^*h(x)=\int_{[0,2-x]}h(x+z)/(x+z)\,d\nu_L(z)$ almost everywhere. These statements concern smooth vectors. Convergence of the measures in total variation would be false.

For completeness, the variational quotient for $V$ is $\int_1^2 G^2/(4x^2)\,dx\,/\,\int_1^2 (G')^2\,dx$ for absolutely continuous real $G$ with $G(1)=0$. Its maximum exists by compactness of $V$. The maximizing eigenfunction solves $G''+\lambda G/x^2=0$, $G(1)=0$, $G'(2)=0$, with least eigenvalue $\lambda=1/(4\|V\|^2)$. For $\lambda\le1/4$ the solutions vanishing at one are multiples of $\sqrt x\log x$ or of $\sqrt x\sinh(\sqrt{1/4-\lambda}\log x)$, which have no stationary point in $(1,2]$. For $\lambda>1/4$ the solution is $G=\sqrt x\sin(\omega\log x)$ with $\omega^2=\lambda-1/4$. The first root of the terminal boundary condition is the root in (2), unique on that interval since $\tan(\omega\log2)+2\omega$ is strictly increasing. This proves $\|V\|=\sigma_*$. Its positive right and left singular functions can be taken as $h=G'$ and $g=G/(2x\sigma_*)$. They obey $Vh=\sigma_*g$, $V^*g=\sigma_*h$. The only zeros are $g(1)=0$ and $h(2)=0$, both simple. In particular $V1\le Cg$ and $V^*1\le Ch$.

Uniform convergence on these fixed smooth functions yields, for $\epsilon=M/L$ and an absolute sufficiently large $M$,

$$
 T_\nu(h+\epsilon)\le(\sigma_*+C\epsilon)(g+\epsilon),
 \qquad T_\nu^*(g+\epsilon)\le(\sigma_*+C\epsilon)(h+\epsilon).
$$

Indeed $T_\nu h=\sigma_*g+O(1/L)$, $T_\nu1\le Cg+O(1/L)$, and the adjoint satisfies the analogous estimates. The strictly positive weights allow the two-weight Schur test for the positive translation kernel, giving $\|T_\nu\|\le \sigma_*+O(1/L)$. The lower estimate follows by testing $h$ and using uniform convergence. This proves (2) without asserting operator-norm convergence to $V$.

## A growing cutoff for ordinary primes

For a fixed $c>0$ let $U=cL^2$. Write $D_{\le U}$ for the ordinary prime atoms $p\le U$ together with the *negative* continuum on $0\le u\le\log U$, and $D_{>U}=D-D_{\le U}$. All asymptotics here take $L\to\infty$. Convolution by the finite signed measure $D_{\le U}$ on the full line has norm

$$
 \|D_{\le U}*\|_{2\to2}=(2+o(1))\sqrt U.                     \tag{3}
$$

By Plancherel its norm is the supremum of the multiplier
$\sum_{p\le U}(\log p)p^{-1/2-i\tau}-(U^{1/2-i\tau}-1)/(1/2-i\tau)$.
For $|\tau|\le R$ fixed, partial summation of $\sum_{p\le x}\log p=x+o(x)$ shows the difference is $o_R(\sqrt U)$ uniformly. For $|\tau|>R$ its absolute value is at most $(2+o(1))\sqrt U+(\sqrt U+1)/R$, since the unsigned prime sum is asymptotic to $2\sqrt U$. Take the upper limit then $R\to\infty$. For the reverse inequality, for each fixed finite prime set there are arbitrarily large real $\tau$ with all $e^{-i\tau\log p}$ arbitrarily close to one, by simultaneous Dirichlet approximation (periodicity gives the assertion also if a bounded return time recurs exactly). The continuum multiplier tends to zero at infinity. This gives (3).

Combining (2) and (3), the compression of $h\mapsto (Q+D_{\le U})*h/t$ to $[L,2L]$ has norm at most $\sigma_*+2\sqrt c+o(1)$. In particular $c=1/8$ is admissible. If $2\sqrt c+\sigma_*<1$, (1) gives the uniform equivalence

$$
 \sqrt{F_B}\ \asymp_c\ \sqrt{F_Y}+
 \left\|t^{-1}(D_{>U}*f)(t)\right\|_{L^2([L,2L])}.             \tag{4}
$$

For the proof, write $f=f_0+f_1$ through the horizon using the two adjacent intervals. The forcing of $f_0$ by $Q$ costs at most $L^{-1}Q([0,2L])\|f_0\|=(1+O(1/L))\|f_0\|$ by Young's inequality. The forcing by $D_{\le U}$ costs at most $(2\sqrt c+o(1))\|f_0\|$ by (3). In the equation for $f_1$ absorb the same-interval operator by its strict norm bound. Conversely the triangle inequality in (1) directly bounds the discrepancy norm by $C_c(\|f_0\|+\|f_1\|)$. Finally $\sqrt{F_B}=(\|f_0\|^2+\|f_1\|^2)^{1/2}$. Thus (4) retains the full balancing price to within the known factor two in squared norms and applies to the subquadratic target with arbitrary fixed multiplicative constants. The surviving discrepancy in (4) still uses the actual $f$; ordinary primes between $U$ and $b$ can act on the new interval.

There is a concrete limit on such a source-independent contraction. If $c>1/4$ the same compression has lower limiting norm at least $2\sqrt c>1$. To see this, modulate any fixed nonnegative smooth unit vector on the rescaled interval by $e^{i\tau Lx}$. For each fixed $L$ take arbitrarily large $\tau$ simultaneously aligning *every* prime with an atom in either truncated atomic measure. After undoing the modulation the atomic operators converge on this vector to their unsigned versions; the modulated continuum vanishes by oscillatory integration (dominated convergence in $x$ suffices at each fixed $L$). Discarding the positive $Q$ preserves a lower bound. The ordinary atom translations have rescaled length at most $\log U/L\to0$ and mass divided by $L$ tending to $2\sqrt c$. They therefore converge on each such compactly supported vector to multiplication by $2\sqrt c/x$. Tests supported in $[1+\eta,1+2\eta]$ and then $\eta\downarrow0$ give the lower limit. This is an operator obstruction on arbitrary inputs and does not assign such phases to the actual Möbius source.

**Verification.** The identities and estimates above are analytic. A floating-point scalar root solve gave the displayed approximation in (2); only the defining equation and inequalities enter the proof. The remaining arithmetic task is to estimate the high ordinary-prime discrepancy in (4).

## Sharp threshold for a uniformly bounded inverse

The sign in (1) permits a stronger conclusion than the unweighted norm comparison. Denote the compressed signed feedback on $[L,2L]$ by $J_L h=t^{-1}[(Q+D_{\le U})*(h1_{[L,2L]})](t)$. Then

$$
 \begin{array}{ll}
 0<c<1/4: & \displaystyle\limsup_{L\to\infty}\|(I+J_L)^{-1}\|<\infty,\\[4pt]
 c\ge1/4: & \displaystyle\lim_{L\to\infty}\ \inf_{\|h\|=1}\|(I+J_L)h\|=0 .
 \end{array}                                                        \tag{5}
$$

Accordingly (4) holds for **every fixed $c<1/4$**. The second conclusion of (5) concerns arbitrary input vectors; strong lower bounds for the signed inverse on the specific native vector could survive beyond that cutoff.

For the first assertion, conjugate by multiplication by $e^{-\alpha t/L}$ on the annulus. This costs only an $e^\alpha$ norm-equivalence constant for $\alpha>0$ fixed. In the conjugated kernel every delay $u$ receives the damping $e^{-\alpha u/L}$. The higher powers have norm bounded by their damped total mass divided by $L$, hence by

$$
 \int_0^1 e^{-\alpha z}\,d\nu_L(z)
  =(1-e^{-\alpha})/(2\alpha)+O_\alpha(1/L).
$$

The change to the ordinary signed kernel divided by $L$ has total variation $o(1)$, since its shifts are $\le\log U$, its unsigned mass is $O(\sqrt U)$ and $1-e^{-\alpha\log U/L}=o(1)$. Its conjugated compression thus still has norm at most $2\sqrt c+o(1)$ by (3). For $2\sqrt c<1$ choose $\alpha$ large enough that their sum is strictly below one. The Neumann series in this equivalent norm proves the upper line of (5). The previous bound on the forcing by the old interval then proves (4).

For the lower line, work on the rescaled interval $[1,2]$. Fix $\eta>0$ and a nonnegative smooth unit vector $h$ supported in $(1,1+\eta)$, extended smoothly by zero. For each large $L$ assign signs $\epsilon_p=\pm1$ to $p\le U$ such that
$L^{-1}\sum_{p\le U}\epsilon_p(\log p)/\sqrt p=-1+o(1)$. This is possible because the unsigned normalized sum tends to $2\sqrt c\ge1$ and the largest individual normalized weight tends to zero. Starting with all negative signs and flipping successive signs achieves the desired accuracy, using all negative if the unsigned normalized sum is just below one.

The numbers $\log p$ for the finitely many $p\le U$ are rationally independent by unique factorization. The continuous Kronecker theorem gives arbitrarily large $\tau$ with $e^{-i\tau\log p}$ arbitrarily close to all the specified signs. Modulate $h$ by $e^{i\tau Lx}$ and undo the modulation after applying $I+J_L$. For each fixed $L$ the modulated continuum contribution tends to zero in norm as $\tau\to\infty$, by pointwise oscillatory integration and dominated convergence. The ordinary prime contribution can be made arbitrarily close to the operator using the specified signs. On this fixed smooth $h$ it equals $-h(x)/x+o_h(1)$ as $L\to\infty$, because all rescaled shifts are $\le\log U/L\to0$ and their total absolute normalized mass is bounded.

The remaining modulated prime-power term has pointwise absolute value at most $T_\nu h$. The uniform smooth-vector limit already proved gives $\|T_\nu h\|\to\|Vh\|\le\|h\|_1/2\le\sqrt\eta/2$, regardless of the prime-power phases. Thus the upper limit of the minimum output norm on unit inputs is at most $\eta+\sqrt\eta/2$, using $|1-1/x|\le\eta$ on the support of $h$. Sending $\eta$ to zero proves (5). The construction uses complex unit inputs, which give the same minimum norm as real inputs for a real operator by separating their real and imaginary parts.

## Where a threatening frequency must lie on the actual input

For any fixed $\alpha\ge0$ put $g(t)=e^{-\alpha t/L}f(t)1_{[L,2L)}$. Use the Fourier convention $\widehat g(\tau)=\int g(t)e^{-i\tau t}\,dt$. With $T=b\log b$,

$$
 \frac1{2\pi}\int_{|\tau|>T}|\widehat g(\tau)|^2\,d\tau
 \ll_\alpha \frac{1+b^{-1/3}F_B^{2/3}}{\log b}
 =o(F_B).                                                        \tag{6}
$$

Indeed $(d/dt-1/2+\alpha/L)g$ consists of jumps $\mu(n)e^{-\alpha\log n/L}/\sqrt n$ at $b<n<b^2$ and two endpoint atoms of absolute values $\le\sqrt b\,|m(b)|$, $b|m(B)|$. For every $N\ge2$ we have

$$
 N|m(N)|^2\ll N^{1/3}F_N^{2/3}+N^{-1}.
$$

To see it, the identity $\sum_{n\le N}\mu(n)\lfloor N/n\rfloor=1$ gives $|m(N)|\le1+1/N$. Write $d=|m(N)|$. If $Nd<16$ the $N^{-1}$ term suffices. Otherwise the last $\lfloor Nd/8\rfloor$ integers $k\le N$ satisfy $|m(k)-m(N)|\le 2(N-k)/N\le d/4$, giving $F_N\gg Nd^3$. This controls both endpoint atoms.

For the interior Dirichlet polynomial $P(\tau)=\sum_{b<n<b^2}a_ne^{-i\tau\log n}$, one has $\sum|a_n|^2\le L+O(1)$ and, for $V\ge1$,

$$
 \int_{-V}^{V}|P(\tau)|^2\,d\tau\ll (V+B)\sum_n|a_n|^2.
$$

Indeed majorize the frequency interval by $e\exp(-\tau^2/V^2)$ and take its Fourier transform. The resulting Gaussian matrix has row sums $O(1+B/V)$ before the prefactor $O(V)$, since $|\log(n/m)|\ge |n-m|/B$ throughout the support. Dividing the transformed derivative identity by $i\tau-1/2+\alpha/L$ and summing dyadic frequency ranges above $T$ now bounds the interior contribution by $O(L/T+BL/T^2)$. The endpoint contribution is $O((B^{1/3}F_B^{2/3}+1)/T)$. These prove (6), using $F_B\ge m(1)^2=1$.

Here is the consequence for (4), which addresses a finite frequency interval of the prime sum. For any fixed $c>0$, suppose there is $\eta>0$ such that for all sufficiently large stages under consideration,

$$
 \inf_{|\tau|\le b\log b}\Re\left[
 \sum_{p\le cL^2}\frac{\log p}{p^{1/2+i\tau}}-
 \frac{(cL^2)^{1/2-i\tau}-1}{1/2-i\tau}
 \right]\ge -(1-\eta)L.                                      \tag{7}
$$

Then (4) holds on those stages, including for $c\ge1/4$. To prove this, fix $\alpha$ with $(1-e^{-\alpha})/(2\alpha)<\eta/4$ and apply the damping in (5). In the equation for $g$ before division by $t$, take the real $L^2$ inner product with $g$. Its $tg$ term is at least $L\|g\|^2$. By Plancherel, (3), (6) and (7), the damped small-prime term is bounded below by $-(1-\eta+o(1))L\|g\|^2-o(LF_B)$. Here the damping alters the multiplier uniformly by $o(L)$. The higher-power contribution is bounded in absolute value by $(\eta/4+o(1))L\|g\|^2$. The absolute inner product with the old-interval forcing and the surviving discrepancy is at most $C_{c,\alpha}L(\sqrt{F_Y}+\|t^{-1}D_{>U}*f\|_{[L,2L]})\|g\|$, with the norm interpreted as in (4). Since $F_B=F_Y+\|f_1\|^2\le F_Y+e^{4\alpha}\|g\|^2$, the $o(LF_B)$ error is absorbed, up to $o(LF_Y)$. The resulting quadratic inequality gives the forward estimate in (4); the reverse estimate still follows from (3) and Young's inequality.

Condition (7) is a sufficient arithmetic test, not an established bound for every $c$. Bounded frequencies already contribute $o_c(L)$ by the prime number theorem. The counterinputs proving the lower line of (5) do not demonstrate a violation of (7).
