# The zero abscissa after cancellation of the first abundance mode

Let $D=W_\sigma-W_\phi$ be the difference of the two arithmetic log moments and $D_0=M_\sigma-M_\phi$ the difference of the two matching continuous-prime models, as in the [prime-square analysis](abundance-curvature-sigma-nov18.md). Set $U_2=D-D_0$, and let $\Theta=\sup_\rho\Re\rho$. Then the proposed exact exponents are
$$
 \limsup_{s\to\infty}\frac{\log(1+s^2|U_2''(s)|)}{\log s}
 =\limsup_{s\to\infty}\frac{\log(1+|U_2(s)|)}{\log s}=\Theta/2 .
 \tag{1}
$$
In particular, each of the corresponding families of quarter-power upper bounds is equivalent to RH.

## Differentiated control of the discarded modes

Let $d\Delta(v)=d\pi(v)-dv/\log v$ on $[2,\infty)$, and write $D_v=v\partial_v$ at fixed $s$. For the local tilted variances of the geometric-prime scores use the notation $V_A(s,v), V_B(s,v)$ from the linked note. Put $K(u)=e^u/(1+e^u)^2$ and $q_s(v)=v^{-4}K(s/v^2-\log v)$. We claim
$$
 U_2''(s)=\int_{[2,\infty)}q_s(v)\,d\Delta(v)
 + O_\epsilon(s^{-2+\Theta/3+\epsilon}).
 \tag{2}
$$
This uses cancellation against the prime discrepancy, whereas the absolute error after retaining this shell is only $O_\epsilon(s^{-5/3+\epsilon})$. Fix $\alpha>\Theta$ arbitrarily close to $\Theta$ with $\alpha<1.1$, so that $|\Delta(v)|\ll_\alpha v^\alpha$. We bound the Stieltjes remainder by integrating $v^{\alpha-1}|D_v(V_A-V_B-q_s)|$. Splits below are subdivisions of the resulting derivative integral, so no artificial boundary terms arise.

**Low range.** Put $P=s^{1/3+\eta}$ with fixed small $\eta>0$. For $2\le v\le P$, write
$$
 E_k=-s\log(1-v^{-k-1}),\qquad
 V_A=s^{-2}\operatorname{Var}(E_k)
$$
under weights proportional to $v^{-k}e^{-E_k}$, $k\ge0$. Their normalizer is $\gg1/s$ from $k=\lfloor\log s/\log v\rfloor$. One has $|D_v E_k|\le C(k+1)E_k$, from $v^{-k-1}\le1/2$. All fixed mixed moments $\mathbb E[(1+k)^a(1+E_k)^b]$ are $O_{a,b}((\log s)^{a+b})$ (enlarging the constant in the exponent of the log has no effect here). To see this, cut $k$ at $C_{a,b}\log s$ and $E_k$ at $C_{a,b}\log s$; on their complements geometric decay $2^{-k}$ or exponential decay $e^{-E_k}$ dominates the factor $O(s)$ from normalization, using $\sup_{t\ge0}e^{-t/2}(1+t)^b<\infty$. The differentiation identity
$$
 D_v\mathbb E F=\mathbb E D_v F+\operatorname{Cov}(F,-k-D_v E_k)
$$
therefore gives $|D_v V_A|\ll s^{-2}(\log s)^C$. For the binary $B$ the same argument applies with $E=sb(v)$ when absent and zero otherwise, and with normalizer $\gg1/v$: alternatively differentiate the explicit $b(v)^2K(sb(v)-\log(v-1))$ directly, exponentially small here. The shell $q_s$ and its log derivative are exponentially small throughout $v\le P$. This range contributes $O_\alpha(s^{-2}P^\alpha(\log s)^C)$.

**Intermediate range.** For $P<v\le P_1=s/(\log s)^2$ absence under both tilts costs $O(v\exp[-s\log(1+1/v)])$; its derivatives produce only polynomial factors in $s$, and the total remains negligible. Conditional on occupancy let $p_2$ denote the probability of $k\ge2$, let $\Delta_2$ be the difference of the conditional mean there from $A_1=\log(1+1/v)$, and $V_2$ the conditional variance there. Write $u=s/v^2-\log v$ and $e=s/v^3+1/v=o(1)$. The log odds are $u+E$, and
$$
 |E|+|D_v E|\ll e,\quad
 \Delta_2=v^{-2}+O(v^{-3}),\quad D_v\Delta_2=-2v^{-2}+O(v^{-3}),
 \quad |V_2|+|D_v V_2|\ll v^{-6}.
 \tag{3}
$$
For details divide all terms above two by the $k=2$ term. Their ratios equal $v^{2-k}\exp(s[A_k-A_2])$ with $0\le A_k-A_2\ll v^{-3}$ and $|D_v(A_k-A_2)|\ll(k+1)v^{-3}$. Thus the sum of these ratios and its log derivative are $O(1/v)$ by the geometric tail. The conditional distribution of $k\ge2$ has bounded moments of $k$ of every fixed order, and its normalized-weight log derivatives are $O(k+1)$ after common cancellation of the $k=2$ term. The same covariance differentiation as before proves the variance bound and its derivative using the centered scores $A_k-A_2$. Expanding $A_2-A_1=\log(1+1/(v+v^2))$ gives the first two bounds for $\Delta_2$, and adding $s(A_2-A_1)-\log v$ to the logarithm of the conditional normalizer gives both odds estimates.

The total variance under occupancy is $p_2 V_2+K(u+E)\Delta_2^2$. Here $|K'|+|K''|\ll K$, $|D_v u|\ll1+s/v^2$, and $D_v p_2=K(u+E)D_v(u+E)$. Thus
$$
 |D_v(V_A-V_B-q_s)|
 \ll v^{-6}+K(u)(1+s/v^2)\big(v^{-4}e+v^{-6}\big)
$$
up to the negligible absence terms. The first term contributes $O(P^{\alpha-6})$. Below $v=s^{12/25}$ the logistic factor in the other terms beats every power of $s$, and above it $(1+s/v^2)e\ll s^{-2/5}$. The remaining weighted integral is $O(s^{-2/5+(12/25)(\alpha-4)})$; this is smaller than $s^{-2+\alpha/3}$ for the indicated $\alpha$. The $K(u)v^{-6}(1+s/v^2)$ term satisfies the same bound there since $v^{-2}\le e$.

**High range.** For $v>P_1$, retain the two tilted valuation laws on the same state space and rescale scores by $v$, writing $A^*=vA_k,\ B^*=vB_k$. Both are bounded, $|A^*-B^*|\ll1/v$, $|D_v(A^*-B^*)|\ll(k+1)/v$ and $|D_v A^*|+|D_v B^*|\ll k+1$. The likelihood ratio of the two tilted laws is $1+O(s/v^2)$ uniformly. Their log derivatives before normalization are $-k+sD_v A_k$ and $-k+sD_v B_k$, of magnitude $O((k+1)(1+s/v))$ and difference $O((k+1)s/v^2)$. All fixed tilted moments of $1+k$ are bounded, since, conditional on occupancy, the weights relative to $k=1$ are at most $v^{1-k}e^{Cs/v^2}$. Comparing the formulas for $\mathbb E F,\mathbb E D_v F$ and $\operatorname{Cov}(F,D_v\log\mathrm{weight})$, for $F$ the first and second rescaled scores, gives
$$
 |D_v(V_A-V_B)|\ll(\log s)^C(v^{-3}+s v^{-4}).
$$
The factor $v^{-2}$ from returning to the unscaled variances has the same size on differentiation. The derivative of $q_s$ is $\ll v^{-4}(1+s/v^2)$ there. Integration contributes $O(s^{\alpha-3}(\log s)^C)$.

The boundary at infinity vanishes by the high-range undifferentiated bound; equivalently use the cumulative discrepancy starting at $2-$ to include its lower atom. Taking $\eta$ small and $\alpha$ sufficiently close to $\Theta$ proves (2).

## Mellin obstruction at half of a zero

The shell in (2) is $O_\epsilon(s^{-2+\Theta/2+\epsilon})$ by the same discrepancy integration applied just to $q_s$. Below $s^{1/2-\eta}$ its derivative is exponentially small, and above it one may use $|D_v q_s|\ll v^{-4}(1+s/v^2)$ and then take $\eta$ small. Since $U_2(s)=o(s)$ by the slope normalization of the two models and this curvature bound is integrable, $U_2'(s)=-\int_s^\infty U_2''(v)dv$. Ordinary integration gives the upper bound of (1) for the value as well.

Set $\mathcal M(z)=\int_0^\infty s^{1-z} U_2''(s)ds$, initially in $1<\Re z<2$. By (2) its difference from the shell transform is holomorphic in $\Theta/3<\Re z<2$. The shell transform is
$$
 \int_{[2,\infty)} v^{-2z} I_z(\log v)d\Delta(v),
 \qquad I_z(l)=\int_0^\infty u^{1-z}K(u-l)\,du .
$$
Using the [primary curvature note](abundance-curvature-nov18.md), equation (2) there with $T=3/4$, yields
$$
 \Gamma(z)\mathcal M(z)=
 -\int_0^{3/4} t^{z-1}\{A(t)P'(2z+t)+A'(t)P(2z+t)\}\,dt+E(z),
$$
where $A(t)=\pi t/\sin(\pi t)$, $P(w)=\int v^{-w}d\Delta(v)$, and $E$ is holomorphic for $\max(\Theta/3,1/8)<\Re z<2$. The shell-expansion error converges absolutely since $2\Re z+3/4>1$ there. For any rightmost-at-its-ordinate zero $\rho=\beta+i\gamma$ of multiplicity $m$, with $\beta\ge1/2$ and $\beta>2\Theta/3$, the analytic continuation from the right has
$$
 \mathcal M(\rho/2+r)=-m\Gamma(1-\rho/2)(2r)^{\rho/2-1}(1+o(1)),
 \qquad r\downarrow0 .
 \tag{4}
$$
Indeed the singular derivative term is $-m\int_0^\eta t^{z-1}/(2r+t)\,dt$ before division by $\Gamma(z)$. All other local terms remain bounded for the same reasons as in the primary note. Such zeros approach the supremum $\Theta$, including the case $\Theta=1/2$. A putative smaller power bound on curvature makes its Mellin transform holomorphic at one of these points. For a smaller value bound integrate by parts twice first on $[1,\infty)$ in the initial strip; the value transform has the factor $z(z-1)$ and all boundary terms are holomorphic near $\rho/2$. This proves (1).

## Cofinal secondary profile on RH

Assume RH. Put $Q^2\log Q=s$ and $\ell=\log Q$. Then
$$
 \frac{U_2(s)}{\sqrt Q}
 =\frac43+\sum_\rho \frac{2e^{i\gamma\log Q}}{\rho(2-\rho)}+o(1).
 \tag{5}
$$
The sum over all nontrivial zeros with multiplicity converges absolutely and uniformly. Its absolute value is at most $2\sum_\rho|\rho|^{-2}=2(2+\gamma_E-\log(4\pi))<0.093$, so the centered secondary difference is eventually strictly positive, with positive lower margin on this scale.

Indeed set
$$
 g_s(v)=\log\frac{v^{-1}+e^{-s/v^2}}{1+v^{-1}} .
$$
This has second $s$-derivative $q_s(v)$ and is bounded in absolute value by $\min(\log(v+1),s/v^2)$. Thus its integral against $d\Delta$ is absolutely convergent for each fixed $s$. Its first derivative tends to zero in that integral as $s\to\infty$ by absolute domination by $v^{-2}$. Two integrations of (2), using the zero slope of $U_2$ at infinity, give
$$
 U_2(s)=\int g_s(v)\,d\Delta(v)+O_\epsilon(s^{\Theta/3+\epsilon}).
 \tag{6}
$$
On RH this error is $o(\sqrt Q)$. Introduce a smooth $\eta(v)$ vanishing for $v\le2$ and equal to one for $v\ge3$, at cost $O(1)$. The classical explicit formula for $\psi$ gives, with $f_s(v)=\eta(v)g_s(v)/\log v$,
$$
 \int f_s(v)(d\psi(v)-dv)
 =-\sum_\rho\int_2^\infty f_s(v)v^{\rho-1}dv+O(1).
$$
The trivial-zero contribution is uniformly bounded since $|f_s|\ll1$ and its elementary density on $[2,\infty)$ is integrable. The formula follows first for compact cutoff and then by convergence. In particular the following uniform two-derivative estimate supplies an absolute majorant for the zero sum:
$$
 \int_\mathbb R \big|\partial_y^2 f_s(e^y)\big|e^{y/2}dy\ll\sqrt Q.
 \tag{7}
$$
To see this write $m=s e^{-2y}$, $u=m-y$. Then $g_s(e^y)=-m+\log(1+e^u)-\log(1+e^{-y})$. For $y\le\ell-1$ and above the fixed cutoff, $u\ge (1-e^{-2})m$ and the derivatives through order two of $g_s(e^y)+y$ are bounded, with the $m$-dependent terms exponentially small. Thus the integral there is $O(\sqrt Q)$. On $|y-\ell|\le1$, $m\asymp y\asymp\ell$, $|u'|\asymp\ell$. The second derivative of $g_s$ is a sum of $O(m)$ and $O((1+m)^2 K(u))$ terms, plus $O(e^{-y})$; its first derivative is $O(m+1)$. After division by $y$ the integral on this interval is bounded by $C\sqrt Q(1+\ell\int K(u)dy)=O(\sqrt Q)$. On $y\ge\ell+1$, $m/y\le e^{-2}$, so all logistic terms and their derivatives are $O((1+y)^2e^{-(1-e^{-2})y})$. The $-m/y$ term and its derivatives cost $O(\int_{\ell+1}^\infty e^{y/2}m/y\,dy)=O(\sqrt Q)$. This proves (7). It also works with fixed-$s$ upper cutoffs tending to infinity, with vanishing contributions from cutoff derivatives. Two integrations by parts bound the individual zero integrals by $C\sqrt Q/|\rho|^2$.

For each fixed $\rho$, changing variable $v=Qw$ gives
$$
 -Q^{-\rho}\int_2^\infty f_s(v)v^{\rho-1}dv
 \ \longrightarrow\ \int_0^1 w^{\rho-1}dw+\int_1^\infty w^{\rho-3}dw
 =\frac{2}{\rho(2-\rho)}.
$$
Indeed $-g_s(Qw)/\log(Qw)$ tends to 1 for $0<w<1$ and to $w^{-2}$ for $w>1$. The bound on $g_s$ supplies integrable majorants. The uniform bound (7) passes this limit through the sum including the phases $e^{i\gamma\log Q}$.

To convert from $\psi$ to $\pi$ subtract $\sum_{k\ge2}k^{-1}\sum_p\eta(p^k)g_s(p^k)$. For $k=2$ its negative divided by $\sqrt Q$ tends to $\int_0^1dw+\int_1^\infty w^{-4}dw=4/3$: apply PNT on fixed compact ranges of $p/\sqrt Q$, using the uniform convergence on compact sets away from 1 of the preceding rescaled soft minimum (a narrow interval around 1 has negligible mass after shrinking). Below $a\sqrt Q$ Chebyshev bounds the contribution by $O(a\sqrt Q)$, and above $A\sqrt Q$ partial summation gives $O(\sqrt Q/A^3)$ for fixed $A\ge2$. Higher powers with $p^k\le Q$ cost $O(Q^{1/3}\log Q)$ by Chebyshev. Above $Q$ the cumulative count of powers of exponent at least three is $O(v^{1/3}\log v)$ and $|g_s(v)|\le s/v^2$, giving $O(Q^{1/3}(\log Q)^2)$ there. This proves (5).

## The two limiting tails at a common threshold

For $Z\in\{\sigma,\phi\}$ let $I_{Z,0}(u)=\min_{v\ge1}(M_Z(v)+cv-vu)$ with the common linear anchor $c$ in the primary note, and abbreviate $A_\sigma(t)=\Pr(\sigma(n)/n\ge t)$, $A_\phi(t)=\Pr(n/\varphi(n)\ge t)$ in limiting natural density. Set
$$
 V(t)=\log\frac{A_\sigma(t)}{A_\phi(t)}
       -\big(I_{\sigma,0}(\log t)-I_{\phi,0}(\log t)\big).
$$
Let $s_{\rm m}$ be the minimizer for $I_{\phi,0}(\log t)$, $y=\exp(te^{-\gamma_E})$ and $Q^2\log Q=s_{\rm m}$. If $\Theta<1$ then
$$
 V(t)=U_2(s_{\rm m})+O_\epsilon(y^{\Theta-1/2+\epsilon}).
 \tag{8}
$$
In particular, under RH, (5) holds with $U_2(s)$ replaced by $V(t)$, giving an eventual positive residual in the ratio of two *observed tails at the same threshold*, with both continuous models fixed. If $1/2<\Theta<1$, (8) gives exact upper exponent $\Theta/2$ for $V$ measured against $y$, and transfers the value lower exponent as well, since $\Theta-1/2<\Theta/2$.

Here are the interpolation details. Let $W_\lambda=W_\phi+\lambda D$, $M_\lambda=M_\phi+\lambda D_0+c\,\mathrm{id}$ for $0\le\lambda\le1$, and let $s_\lambda,\tilde s_\lambda$ be their respective saddles at $u=\log t$. All functions are strictly convex, being convex combinations of the corresponding true or continuous log moments, plus a linear term if needed. At $v=x\log x$ their curvatures are $\asymp1/(x\log^2x)$ uniformly in $\lambda$, by the ordinary logistic variance computation and the prime-square variance difference, which also holds with continuous prime measure. Their derivatives equal $\gamma_E+\log\log x+o((\log x)^{-2})$ uniformly, by the [exact saddle analysis](abundance-exact-saddle-nov18.md) and its continuous counterpart. Consequently $x\sim y$ uniformly at all these saddles and between any of them. In particular each saddle is $y^{1+o(1)}$ and $s_{\rm m}=\tilde s_0$.

The primary derivative discrepancy and (2) imply, uniformly in $\lambda$,
$$
 |s_\lambda-\tilde s_\lambda|\ll_\epsilon y^{\Theta+\epsilon}.
$$
Indeed the discrepancy at a saddle is $O_\epsilon(y^{\Theta-1+\epsilon})$ and the inverse curvature costs $O(y\log^2y)$. Also $|\tilde s_\lambda-s_{\rm m}|\ll_\epsilon y^{1/2+\epsilon}$ since $D_0'(v)=O((v\log v)^{-1/2})$. This last bound follows by the continuous prime-square calculation, or by combining $D'$ from the [prime-square note](abundance-curvature-sigma-nov18.md) with $U_2'=O_\epsilon(v^{-1+\Theta/2+\epsilon})$ for $\Theta<1$. The same $O_\epsilon(y^{-1/2+\epsilon})$ bound applies to $D'$ throughout the saddle interval.

By differentiation of a strictly convex Legendre minimum with respect to $\lambda$, the difference between the arithmetic and continuous log-minimum *ratios* is
$$
 \int_0^1 (D(s_\lambda)-D_0(\tilde s_\lambda))\,d\lambda .
$$
Replace $s_\lambda$ by $\tilde s_\lambda$ inside $D$ at cost $O_\epsilon(y^{\Theta-1/2+\epsilon})$. Replace $U_2(\tilde s_\lambda)$ by $U_2(s_{\rm m})$ at cost $O_\epsilon(y^{(\Theta-1)/2+\epsilon})$ by the secondary derivative bound. The prefactor $-\tfrac12\log(2\pi y)$ in the exact saddle formula is common to the two true tails and cancels up to $o(1)$. These estimates prove (8). This same-threshold argument makes no lower-exponent assertion when $\Theta=1$; (1) itself has no such restriction.
