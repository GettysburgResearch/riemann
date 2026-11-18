# Subpower windows for Robin violations on least common multiples

**Proposed strengthening, unreviewed.** Suppose RH fails and $1/2<c<\Theta=\sup\Re\rho$. Fix $b$ with $c<b<\Theta$ and a density exponent $\kappa<1$ such that $N(b,T)\ll_b T^\kappa$. For any
$$
\frac{\kappa}{1+\kappa}<\theta<1
$$
and every sufficiently large $Y$, there is an $x$ with
$$
Ye^{-(\log Y)^\theta}\le x\le Y,\qquad
\log\frac{\sigma(m_x)}{e^{\gamma_E}m_x\log\log m_x}>x^{c-1},
\qquad m_x=\operatorname{lcm}(1,\ldots,\lfloor x\rfloor).
$$
In particular one can always take $\theta=1/2$, since Ingham gives some $\kappa<1$ for every fixed $b>1/2$. The proof needs no rightmost zero, separation of ordinates or independence of their phases. No effective starting point or historical priority is claimed.

Write $J$ for the integrated $\psi(t)-t$ error from the [finite Robin note](robin-finite-horizon-nov18.md) and $Z(u)=-e^uJ(e^u)$. The [LCM arithmetic comparison](robin-lcm-nov18.md) shows that $Z(u)>2e^{cu}$ suffices at large $u$. We prove both signs of this amplitude for $Z$ itself. The positive conclusion gives the stated LCM result.

### Parameters and a local absolute lower bound

Choose $0<p<1$ and $q$ with $\max(1-p,p\kappa)<q<\theta$. Fix a zero $\rho_0$ with $\Re\rho_0>b$. For a large real center $t$ hold $\epsilon=t^{-2p}$ fixed throughout its neighboring centers. Write
$$
\lambda(z)=z+\epsilon z^2,\quad
g_x(v)=\frac{e^{-(v-x)^2/(4\epsilon x)}}{\sqrt{4\pi\epsilon x}},
\quad D=C_0t^{1-p}.
$$
Here $C_0$ is a sufficiently large absolute constant, and all centers below satisfy $x=t+O(t^q)$. Define the finite multiset $\mathcal Z=\{\rho:\Re\rho>b,\ |\Im\rho|\le Kt^p\}$ with both signs and multiplicities, with a sufficiently large fixed absolute $K$. Its size $N\ll t^{p\kappa}$ by the assumed density bound. Set $A=\max_{\rho\in\mathcal Z}\Re\lambda(\rho)$. Then $\Re\rho_0+o(1)\le A\le1+\epsilon$.

Let $R(v)=\psi(e^v)-e^v$ for $v>0$. The distributional von Mangoldt formula gives $dR=-\sum_\rho e^{\rho v}dv+r'(v)dv$ there, where $r(v)=-\log(2\pi)-\tfrac12\log(1-e^{-2v})$. Pair it with $g_x(v)\chi_x(v)$, where $0\le\chi_x\le1$ is smooth, equal to 1 for $|v-x|\le D$, supported in $|v-x|\le D+1$, and with first and second derivatives uniformly bounded. Such cutoffs are obtained by translating fixed smooth steps at either endpoint. The full Gaussian transform at $\rho$ is $e^{\lambda(\rho)x}$. Extending each transform to the full line creates an error $O(e^{-2t}/(1+|\Im\rho|^2))$ uniformly. Indeed for $0\le\beta\le1$ the $L^1$ norms of $e^{\beta v}g_x(v)(1-\chi_x(v))$ and its first two derivatives are $O(e^{-2t})$: completing the square shifts the Gaussian center by $2\beta\epsilon x=o(D)$, and its tail outside $D$ costs $e^{-C_0^2t/(4+o(1))}$ against $e^{x+\epsilon x}$ and polynomial factors in $t$. Integration by parts twice supplies the ordinate denominator. Summing these errors is legitimate. The trivial-zero derivative is exponentially small. The total full Gaussian sum with $|\Im\rho|>Kt^p$ is $O(e^{-2t})$ by the factor $e^{-\epsilon x(\Im\rho)^2}$ and $N(T)=O(T\log T)$, increasing $K$ if necessary. Zeros in the remaining finite range with $\Re\rho\le b$ cost $e^{bt+o(t)}$. Consequently
$$
\int g_x\chi_x\,dR=-\sum_{\rho\in\mathcal Z}e^{\lambda(\rho)x}+O(e^{bt+o(t)}).
\tag{1}
$$

Take $M=\lceil t^2\rceil$, $h=t/M$, and $z_j=e^{h\lambda(\rho_j)}$ for the retained multiset. The Kolesnik–Straus power-sum theorem provides a $k\in[M+1,M+N]$ such that
$$
\left|\sum_j z_j^k\right|
\ge 1.007\left(\frac{N}{4e(M+N)}\right)^N \max_j |z_j|^k .
$$
This theorem allows coincident $z_j$. In particular unit coefficients and counting repeated zeros cause no difficulty. Since $Nh=o(1)$, the center $x=kh$ belongs to $[t,t+1]$, and (1) has absolute value at least $\exp(At-Ct^{p\kappa}\log t)$ there after increasing fixed $C$. [Kolesnik–Straus as stated in Thorner–Zaman, Theorem 5.2](https://arxiv.org/abs/1604.01750)

To read this as a lower bound on the integrated error, put $d(v)=1/v+1/v^2$. Direct differentiation gives $Z'(v)=Z(v)+d(v)R(v)$ almost everywhere. In particular for a smooth compact test $f$ in this interval,
$$
\int f\,dR=\int\left[(f'/d)' + f'/d\right] Z(v)\,dv .
$$
The coefficient for $f=g_x\chi_x$ is polynomially bounded in $t$ in sup norm, since the inverse Gaussian width and the derivatives of $1/d$ have polynomial bounds. Thus for $I=[t-D-2,t+D+2]$,
$$
\int_I|Z(v)|dv\ge\exp(At-C' t^{p\kappa}\log t).
\tag{2}
$$

### A positive average with smaller signed value

With $x=t+O(t^q)$ put $G(x)=\int_{|v-x|\le D}g_x(v)Z(v)dv$, using the unnormalized positive truncation. The integrated explicit formula of the [LCM note](robin-lcm-nov18.md) gives, uniformly at these centers,
$$
G(x)=\sum_{\rho\in\mathcal Z}\int_0^1
 \frac{1+w}{\rho(1-\rho+w)} e^{\lambda(\rho-w)x}\,dw
 +O(e^{bt+o(t)}).
\tag{3}
$$
Indeed $w>1$ in that formula costs $O(1/t)$ since $v\ge t-o(t)$, $|1-\rho+w|\ge|1-\rho|$, and the sum of $1/(|\rho||1-\rho|)$ is finite. For $0\le w\le1$ the real shift is bounded by one in absolute value and the same Gaussian tail estimate applies, now directly with the summable denominators (no differentiability of the cutoff is needed). The full Gaussian generates exactly the exponent in (3). The two complementary zero groups are bounded as in (1), using $\Re\lambda(\rho-w)\le\beta+\epsilon-\epsilon(\Im\rho)^2$.

For each distinct retained positive ordinate and real part, put $\lambda_j=\lambda(\rho_j)$ and $\ell_j=\pi/\Im\lambda_j$. Form the positive probability measure proportional to $\delta_0+e^{-\ell_j\Re\lambda_j}\delta_{\ell_j}$. Its exponential transform vanishes at $\lambda_j$ and its conjugate. Let $m=\lceil t^q\rceil$ and take the convolution $\mu$ of $m$ copies of each such measure. Its support lies in $[0,S]$ with $S=O_b(m)$: $\Im\lambda_j=(1+2\epsilon\Re\rho_j)\Im\rho_j$ and $\sum_{\beta>b,\gamma>0}1/\gamma<\infty$ by $N(b,T)\ll T^\kappa$. For $0\le w\le1$ uniformly in the retained set, $|\lambda(\rho_j-w)-\lambda_j|\le Cw$, since $\epsilon|\rho_j|=O(1)$. The $j$-th two-atom transform at this perturbed argument has modulus at most $C'w$ by the mean-value integral for the exponential. Here $\ell_j$ and $|\Re\lambda_j|$ are uniformly bounded, regardless of $t$. Bounding the other factors by their support gives
$$
\left|\int e^{\lambda(\rho_j-w)s}\,d\mu(s)\right|
 \le (C'w)^m e^{2S}.
\tag{4}
$$
The same holds for negative ordinates by conjugation.

Put $P=2S+4D+10$. Draw $r$ uniformly on $[-P,P]$ and independently $s$ according to $\mu$. Average (3) at $x=t+r+s$. Because $\beta>b>1/2$, $\Re\lambda(\rho-w)\le A-w$ on $[0,1]$. The retained terms in the average therefore have total absolute bound
$$
\ll e^{At+O(m)} (C')^m\int_0^1 w^m e^{-tw}dw
 \ll \exp(At-(1-q+o(1))m\log t),
$$
using the summable reciprocal-square coefficients, $D=o(m)$, $|\Re\lambda(\rho-w)|=O(1)$ for retained zeros, and $m!/t^{m+1}$ for the last integral. The omitted terms cost $e^{bt+o(t)}$. We have proved a bound on the absolute value of the **signed** average:
$$
|\mathbb E G(t+r+s)|\ll
\exp(At-(1-q+o(1))m\log t)+e^{bt+o(t)} .
\tag{5}
$$

The same average is integration of $Z(v)$ against a positive measure of mass at most one supported in $|v-t|\le P+S+D=O(t^q)$. Its density on $I$ is $\gg1/P$. In fact the center $t+r+s$ has density exactly $1/(2P)$ on $[t-P+S,t+P]$ by the uniform padding. For each $v\in I$ the centers $|x-v|\le\sqrt{\epsilon t}$ lie in that plateau and obey $|v-x|\le D$. There $g_x(v)\gg1/\sqrt{\epsilon t}$, proving the density lower bound by integration in $x$. Equation (2) now makes the average of $|Z|$ at least $\exp(At-O(t^{p\kappa}\log t))$ after adjusting a constant. Because $p\kappa<q$ and $A>b$ with fixed slack, (5) is smaller by a factor tending to zero. Both the positive and negative parts consequently have average at least a fixed fraction of that absolute average. Since $A>c$ with fixed slack and $m=o(t)$, some $v$ in the support satisfies $Z(v)>2e^{cv}$, and another satisfies $Z(v)<-2e^{cv}$.

Finally take $t=\log Y-\tfrac12(\log Y)^\theta$. The entire support is inside $[\log Y-(\log Y)^\theta,\log Y]$ for all sufficiently large $Y$ because $q<\theta$. The arithmetic comparison completes the proof.

### Boundary cases for the horizontal zero supremum

If $\Theta=1$, the same short-window conclusion holds for **every** fixed $\theta>0$: choose $b<1$ sufficiently close to 1 so the uniform density exponent $(8/3)(1-b)$ (with a little slack for logarithms) is small enough. If $1/2<\Theta<1$ is attained by a zero, there is a different improvement. In this case the full LCM log ratio $B(x)$ from the companion note has the asymptotic profile
$$
x^{1-\Theta}\log x\,B(x)=
\sum_{\Re\rho=\Theta}\frac{e^{i\Im(\rho)\log x}}{\rho(1-\rho)}+o(1).
$$
Indeed $|\psi(x)-x|\ll x^\Theta\log^2x$ follows from the classical truncated explicit formula (or its usual $x^{\Theta+\delta}$ version for any $\delta>0$ is enough). The nonnegative tangent error in that note is therefore negligible on this scale by Taylor's formula and $\Theta<1$. All prime-power and exponent terms are negligible since $\Theta>1/2$. In the integrated explicit formula the scaled zero terms are bounded by a fixed multiple of $1/(|\rho||1-\rho|)$, and each zero left of $\Theta$ tends to zero after scaling. For a zero on the boundary the coefficient differs from $e^{i\Im(\rho)\log x}/[\rho(1-\rho)]$ by $o(1)$, by the Laplace-integral formula for $F_\rho$. Dominated convergence proves the profile. The remaining uniformly almost periodic sum is real, nonzero and has mean zero. Its positive and negative strict values therefore recur at bounded logarithmic gaps. Consequently every sufficiently large $[X,CX]$ contains both signs of $B$ at absolute amplitudes $\gg X^{\Theta-1}/\log X$, for constants depending on the actual boundary zeros.

### Violations at exact Chebyshev fixed points and LCM values on both sides

The positive LCM witness can be chosen with $\psi(x)=x$. Equivalently, for $N=\lfloor x\rfloor$ the integer $m=\operatorname{lcm}(1,\dots,N)$ satisfies $N=\lfloor\log m\rfloor$. There is also an LCM with $B(x)<-x^{c-1}$ in every window of the theorem, including when $\Theta=1$.

For details, choose $c<c'<b$. In the proof the actual positive and negative averages dominate $2e^{c'v}$, since $A\ge\Re\rho_0+o(1)>b$. Therefore there are both signs of $J(e^v)$ at amplitudes $2e^{(c'-1)v}$ in $|v-t|\le C t^q$. Take four successive disjoint windows of this form within the larger log interval $[\log Y-(\log Y)^\theta,\log Y]$ (possible since $q<\theta$), and choose points with alternating signs of $J$. The two middle points each lie between two points of opposite sign to their own. A minimum and maximum of $J$ on the respective bracket intervals thus lie in their interiors and are at least as extreme as those middle values. At either extremum $x$, the available magnitude is $>2x^{c-1}$ for large $Y$: all logarithms involved equal $\log Y+o(\log Y)$ and the slack $c'-c$ is fixed.

The one-sided derivatives of $J$ are $-(\psi(x^-)-x)w(x)$ and $-(\psi(x)-x)w(x)$ with $w(x)>0$. At a minimum these force $\psi(x^-)\ge x\ge\psi(x)$, hence equality by monotonicity of $\psi$. At a maximum they force $\psi(x^-)\le x\le\psi(x)$, so $|\psi(x)-x|\le\log x$ because the jump at a prime power is at most $\log x$. In the exact arithmetic identity of the companion note this makes the nonnegative logarithmic Taylor remainder $Q$ zero at the minimum and $O((\log x)/x^2)$ at the maximum. Its other terms differ from $-J(x)$ by $O(1/(\sqrt x\log x))$. Thus the minimum yields $B(x)>x^{c-1}$ and the maximum yields $B(x)<-x^{c-1}$. Finally $\log m_x=\psi(x)$ gives the stated integer fixed-point condition. In particular RH is equivalent to strict Robin on all sufficiently large LCMs from this fixed-point subsequence.

These fixed-point indices have an independently known frequency lower bound. On $[N,N+1)$ the function $\psi$ equals $\log m_N$, which is not a positive integer (otherwise $e^k$ would be integral for an integer $k>0$). Thus $N=\lfloor\log m_N\rfloor$ if and only if the decreasing line $\psi(x)-x$ crosses zero downwards in that unit interval. Upward crossings can only occur at prime-power jumps and crossing directions alternate. Apart from an endpoint error the index count is half the sign-change count of $\psi(x)-x$. Consequently its lower logarithmic rate is at least $\gamma_1/(2\pi)+0.9335\cdot10^{-30}$ by the existing unconditional theorem on sign changes, with $\gamma_1$ the first positive zeta ordinate. This counts all such indices regardless of Robin sign. [Morrill–Platt–Trudgian, Theorem 1](https://arxiv.org/abs/1910.14203)

### Local frequency projection gives logarithmic-square windows

A second positive heat transform in the **absolute-value** step, after modulating by a maximizing frequency, improves the window. Under the same hypotheses there is a finite constant $C_c>0$ such that every sufficiently large interval
$$
 [Y\exp(-C_c(\log\log Y)^2),Y]
\tag{6}
$$
contains the positive violation of exponent $c$ at an exact fixed point, and an opposite-sign LCM witness, as above. The constant can depend on the actual zero set and the slack $c<\Theta$. The second transform is used to estimate absolute mass; positivity for the sign conclusion still comes from (3)–(5).

Here take $\epsilon=t^{-2}$, retain $|\gamma|\le Kt$, and truncate the first Gaussian at $D=C_0$, a sufficiently large fixed constant. The first-Gaussian estimates (1) and (3) go through directly with these choices: its variance $2\epsilon x\asymp1/t$ makes the discarded tails $O(e^{-2t})$ against the exponential arithmetic factors, and beyond $Kt$ one has $e^{-\epsilon x\gamma^2}\le e^{-(K^2+o(1))t}$. The derivative bounds for the cutoff remain polynomial in $t$. The estimate $N\ll t^\kappa$ holds, but this many modes need no longer enter the loss of the absolute-value test. All the estimates below are uniform for the centers considered, which differ from $t$ by $O((\log t)^2)$.

Choose a retained $\lambda_*=\lambda(\rho_*)$ with real part $A$, set $\nu_j=\lambda(\rho_j)-\lambda_*$, and put $F(v)=\sum_{j\in\mathcal Z} e^{\nu_j v}$. These shifts are counted with multiplicities and obey $-C_K\le\Re\nu_j\le0$. For a fixed constant $J_0>0$ to be chosen, put $l=\log t$ and $\eta=J_0 l^2/t$. Average $F$ under a normal law of mean $x$ and variance $2\eta x$, where $t\le x\le t+1$. The result is exactly
$$
\sum_{j\in\mathcal Z} e^{(\nu_j+\eta\nu_j^2)x}.
$$
For all sufficiently large $t$, $\Re\nu_j+\eta(\Re\nu_j)^2\le0$. Terms with $|\Im\nu_j|>1$ have total absolute value at most $N e^{-\eta x}$. In the unit frequency interval $|\Im\nu_j|\le1$ there are at most $C_1 l$ terms: $\Im\lambda(\rho)=\gamma+O_K(1/t)$ in the retained range, and the classical full zero count on each unit height interval is $O(\log(2+|\gamma|))$. This uses multiplicities and requires no lower gap bound. The local multiset includes $\nu_j=0$.

Apply Kolesnik–Straus to just this local multiset, using $M=\lceil t^2\rceil$, $h=t/M$ and $z_j=\exp(h(\nu_j+\eta\nu_j^2))$. The maximal modulus is 1, and the number of terms is at most $C_1l$. Thus some $x=kh\in[t,t+1]$ gives absolute local sum at least $\exp(-C_2 l^2)$. Here $C_2$ can be fixed independently of $J_0$, since only the count, the maximum modulus and $M$ entered the bound. Select $J_0>2C_2+10$. Then $N e^{-\eta x}=o(e^{-C_2l^2})$. Truncate this second Gaussian to $|v-x|\le W=C_3 l^2$ with $C_3$ sufficiently large in terms of $J_0,C_2$. For $v\ge0$, $|F(v)|\le N$, and the omitted Gaussian mass costs at most $2N\exp[-W^2/(4\eta x)]$. For $v<0$ we have $|F(v)|\le N e^{C_K|v|}$, whose entire negative-half-line integral against this Gaussian costs $O(e^{-t})$ by completing the square. The truncated integral therefore still has magnitude $\gg e^{-C_2l^2}$. Since the averaging mass is at most one, there exists $v_1$ with $|v_1-t|\le W+1$ and $|F(v_1)|\gg e^{-C_2 l^2}$.

Undo modulation: the full retained sum at $v_1$ has absolute value at least $\exp(A v_1-C_4 l^2)$ for some $C_4$. Equation (1) and the differential identity following it imply
$$
 \int_{v_1-D-2}^{v_1+D+2}|Z(v)|dv\ge\exp(A v_1-C_5 l^2).
$$
The polynomial loss from the derivatives is absorbed into $C_5$, and $A\ge\Re\rho_0+o(1)>b$ has fixed slack.

Recenter the signed averaging step (3)–(5) at $v_1$, keeping $\epsilon$, the retained multiset and $A$ fixed. Now take $m=\lceil C_6 l\rceil$ with $C_6>C_5+2$. Its convolution support is $S=O_b(m)$, the uniform padding $P=2S+4D+10=O(m)$ covers the last fixed-length mass interval, and the tilted centers still have $x=t+O(l^2)$. The main error estimate in (5) is now
$$
\exp(A v_1+O(m))(C')^m m!/v_1^{m+1}
\le \exp(A v_1-(C_6-o(1))l^2).
$$
The remaining source error is $e^{bt+o(t)}$. The positive measure after padding has density $\gg1/P$ on that same mass interval (its final Gaussian has width comparable to $1/\sqrt t$). Its signed average is consequently negligible compared with its absolute average. Thus both signs at amplitudes $2e^{c'v}$, for any fixed $c<c'<b$, occur within $O(l)$ of $v_1$, hence within $O(l^2)$ of $t$. The constants here are uniform as $t\to\infty$. Placing four disjoint such ranges inside a sufficiently wide interval of length $C_c(\log\log Y)^2$ and using the previous extremum argument proves (6) with the fixed-point and opposite-sign assertions.

## Contiguous runs and distinct LCM values

Suppose RH fails. For each $1/2<c<\Theta$ and $0<\delta<1$, every sufficiently large window $[X,CX]$, for a suitable constant $C>1$, contains two intervals of length $X^{1-\delta}$. Throughout the first, $B(x)>x^{c-1}$. Throughout the second, $B(x)<-x^{c-1}$. If $\Theta$ is unattained, any prescribed $C>1$ works. In particular each such window contains $X^{1-o(1)}$ distinct LCM integers of each sign (for the attained case one may take a single $C$ independent of $\delta$ by the almost-periodic profile above).

For the proof shrink the window by a fixed relative amount on either side. The [positive-kernel proof](robin-lcm-positive-kernel-nov18.md) supplies signed extrema of $J$ there of magnitude $\gg X^{c_1-1}$ for any $c<c_1<\Theta$. At its positive maximum $x_0$, $|\psi(x_0)-x_0|\le\log x_0$. Throughout comparable arguments, $\psi(x)-x=O_\eta(X^{\Theta+\eta})$ for every $\eta>0$, by the classical truncated explicit formula (and trivially for $\Theta=1$). Integrating $J'$ changes $J$ by $O_\eta(X^{\Theta-1-\delta+\eta})$ within $X^{1-\delta}$ of either extremum. Choose $c_1>\Theta-\delta$ and $\eta$ sufficiently small. The comparison $B=-J+Q+O(1/(\sqrt x\log x))$ with $Q\ge0$ gives the positive run. For the negative run, if $\Theta<1$ also choose $c_1>2\Theta-1$ and bound $Q\ll X^{2\Theta-2+2\eta}$. If $\Theta=1$, counting all integer arguments of $\Lambda$ gives $|\psi(x)-x|\ll (1+X^{1-\delta})\log X$ near the positive maximum and hence $Q\ll X^{-2\delta}\log X$. These errors are $o(X^{c_1-1})$ with the indicated choices. At every prime in either interval the LCM strictly increases. The classical prime number theorem in short intervals for each fixed exponent $h>7/12$ gives $\gg X^h/\log X$ such distinct values on a run of length $X^h$. Taking $h$ arbitrarily close to one proves the count. For attained $\Theta$, the nonzero mean-zero almost-periodic profile has sign intervals of fixed positive log length recurring with bounded gaps, so fixed $C$ even yields $\gg X/\log X$ distinct values of each sign.
