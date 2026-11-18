# Fixed multiplicative windows for Robin oscillations on least common multiples

Write $m_x=\operatorname{lcm}(1,\ldots,\lfloor x\rfloor)$ and $B(x)=\log(\sigma(m_x)/(e^{\gamma_E}m_x\log\log m_x))$. Suppose $1/2<c<\Theta=\sup_\rho\Re\rho$. Then there exists a finite $C_c>1$ such that **every** sufficiently large interval $[Y/C_c,Y]$ contains an $x_+$ with $\psi(x_+)=x_+$ and $B(x_+)>x_+^{c-1}$, and an $x_-$ with $B(x_-)<-x_-^{c-1}$. If the supremum $\Theta$ is unattained then **every prescribed** $C_c>1$ works. In particular the latter conclusion always applies when $\Theta=1$.

We use the [LCM arithmetic identity](robin-lcm-nov18.md), the [extremum and fixed-point argument](robin-lcm-short-nov18.md), and a compact output test as in [the single-column trace calculation](trace-single-column-nov18.md). The new ingredient is a positive measure on a compact interval whose action on the exact integrated zero terms vanishes for every zero in a specified sparse family.

### Uniform absolute mass in each translate

Use log coordinates, with $R(v)=\psi(e^v)-e^v$, $Z(v)=-e^v J(e^v)$ and $d(v)=1/v+1/v^2$, so $Z'(v)=Z(v)+d(v)R(v)$ almost everywhere. Choose $c<c'<b<\beta_0=\Re\rho_0$ with $b>1/2$. By Ingham the zeros with $\Re\rho>b$ have count $O(T^k)$ for a fixed $k<1$. For every fixed open interval $I$ of positive length there exists a smooth complex $h$ compactly supported in $I$ such that
$$
 H(z)=\int h(y)e^{zy}dy,\qquad H(\rho_0)\ne0,\qquad
 H(\rho)=0\quad(\rho\ne\rho_0,\ \Re\rho>b).
$$
Indeed multiply the genus-zero product $\prod_{\rho\ne\rho_0,\ \Re\rho>b}(1-z/\rho)$ by a compact Gevrey transform centered at $\rho_0$ with vertical decay $O(e^{-c_1|\Im z|^r})$ for $k<r<1$ and arbitrarily short supporting interval, then translate into $I$. The growth bound on the product is $\exp(O((1+|z|)^k))$ by partial integration of the counting bound. The full Paley–Wiener construction is given in (5) of the single-column note. The conjugate of the target is eliminated as well. The target's multiplicity merely multiplies its coefficient.

The distributional von Mangoldt formula on $v>0$ gives $R'=-\sum_\rho e^{\rho v}+O(e^{-2v})$, with the last expression a smooth density on $v\ge1$. Testing with $h(v-t)$ leaves the target $-m_{\rho_0} e^{\rho_0t}H(\rho_0)$ and an error $O_h(e^{bt})$. Indeed $H$ has uniformly rapid ordinate decay on the closed strip $0\le\Re z\le1$ and the full zero count is $O(T\log T)$. Also
$$
 \int h(v-t)\,dR(v)
 =\int \big[(h'(v-t)/d(v))'+h'(v-t)/d(v)\big]Z(v)\,dv .
$$
The sup norm of the kernel in brackets is $O_h(1+t)$. Consequently for all sufficiently large $t$,
$$
 \int_{t+I}|Z(v)|dv\gg_{b,I,\rho_0}e^{\beta_0t}/(1+t).
\tag{1}
$$

### A compact positive measure that kills the exact integrated zero terms

Let $\mathcal E$ contain one representative of each distinct zero with $\Re\rho>b$, $\Im\rho>0$. Define
$$
 S_b=\sum_{\rho\in\mathcal E}\pi/\Im\rho<\infty .
$$
Convergence follows by partial integration from the same density theorem. For each representative put $s_\rho=\pi/\Im\rho$ and form a probability measure on $\{0,s_\rho\}$ with masses proportional to $1,e^{(1-\Re\rho)s_\rho}$. Let $\mu$ be the convolution of all these measures. It exists as the law of the absolutely convergent sum of independent two-valued random variables and is supported in $[0,S_b]$. For either member of each conjugate pair,
$$
 \int e^{(\rho-1)s}\,\mu(ds)=0.
\tag{2}
$$
Indeed its factor for the specified representative vanishes. Infinite product convergence also follows by dominated convergence for the bounded support.

For $w\ge0$ define $L(w)=\int e^{ws}\mu(ds)$ and $g(y)=\int_0^\infty(1+w)e^{-wy}/L(w)\,dw$ for $y>0$. Since $L(w)\ge1$, $g$ is positive decreasing and at most $d(y)$. For $v>S_b$ Tonelli gives
$$
 \int g(v-s)\mu(ds)=d(v).
\tag{3}
$$
Fix $t>2S_b+1$ and set $F_t(v)=0$ for $v<t$. For $v\ge t$ put
$$
 F_t(v)=\frac{1}{d(v)}\int_{s\le v-t}g(v-s)\mu(ds).
$$
This is a right-continuous cumulative distribution function supported in transition on $[t,t+S_b]$. To see monotonicity let $W_v$ have probability density $(1+w)e^{-vw}/d(v)$ on $w\ge0$. Define $\mu_w(ds)=e^{ws}\mu(ds)/L(w)$. Then
$$
 F_t(v)=\mathbb E\,\mu_{W_v}([0,v-t]).
$$
At each fixed threshold $r$, the tilted cumulative probability $\mu_w([0,r])$ is nonincreasing in $w$ by monotone likelihood ratio. The law of $W_v$ decreases stochastically as $v$ increases, by the same likelihood ratio criterion. Thus $\mathbb E\,\mu_{W_v}([0,r])$ increases in $v$ for fixed $r$. Increasing $r=v-t$ adds a second nonnegative increment. Right continuity follows from dominated convergence and right continuity of a cumulative distribution function. Equation (3) gives $F_t(v)=1$ for $v\ge t+S_b$.

The compact measure $d\nu_t(x)=e^{t-x}\,dF_t(x)$ is positive of mass at most one. By the integrated explicit formula,
$$
 Z(x)=\sum_\rho Z_\rho(x)+O(1/x),\qquad
 Z_\rho(x)=\frac{e^x}{\rho}\int_x^\infty d(v)e^{(\rho-1)v}\,dv .
$$
An integration by parts, using positive decreasing $d$, bounds the last integral by $2d(x)e^{(\Re\rho-1)x}/|1-\rho|$. Thus the series converges absolutely uniformly locally, since $\sum_\rho1/(|\rho||1-\rho|)<\infty$. For each individual zero, Fubini followed by translation $v=y+s$ gives the exact separation
$$
 \int Z_\rho(x)d\nu_t(x)
 =\frac{e^t}{\rho}\int_t^\infty d(v)e^{(\rho-1)v}F_t(v)dv
 =\frac{e^t}{\rho}\left(\int e^{(\rho-1)s}\mu(ds)\right)
                  \int_t^\infty g(y)e^{(\rho-1)y}dy .
\tag{4}
$$
The individual interchanges converge absolutely because $\Re\rho<1$. Every term to the right of $b$ vanishes by (2), regardless of multiplicity. For the other zeros, integration by parts bounds the rightmost integral in (4) by $2g(t)e^{(\Re\rho-1)t}/|1-\rho|$. Hence
$$
 \left|\int Z(x)d\nu_t(x)\right|\ll d(t)e^{bt}+1/t.
\tag{5}
$$

### Padding and the two arithmetic witnesses

Fix any $\delta>0$. Integrate the measures $\nu_t$ over $u\le t\le u+S_b+\delta$ with Lebesgue weight. Their total mass is at most $S_b+\delta$, their support lies in $[u,u+2S_b+\delta]$, and (5) bounds the signed average by $O_{b,\delta}(e^{bu})$. The integrated measure dominates $e^{-S_b}dx$ on $u+S_b<x<u+S_b+\delta$.

For this last assertion put $A(v,r)=d(v)^{-1}\int_{s\le r}g(v-s)\mu(ds)$. At fixed $r$ its $v$ derivative is nonnegative by the stochastic monotonicity above. All such differentiations are bounded on compact $v$ ranges strictly right of $S_b$. The distributional derivative of $F_t(v)=A(v,v-t)$ therefore dominates the positive pushforward of $g(t)\mu(ds)/d(t+s)$ by $s\mapsto t+s$. This identity can equally be obtained by directly differentiating $\int \mathbf1_{v\ge t+s} g(v-s)/d(v)\,\mu(ds)$ under a compact test. On the specified interior interval, every $s\in[0,S_b]$ has $t=x-s$ in the padding range, and the resulting density is at least $e^{-S_b}\int g(x-s)\mu(ds)/d(x)=e^{-S_b}$ by (3).

Apply (1) on the interior interval, translating by $u$, with e.g. $I=(S_b,S_b+\delta)$. The average of $|Z|$ is $\gg e^{\beta_0u}/(1+u)$, exponentially larger than the signed bound. Each sign of $Z$ therefore occurs at amplitude greater than $2e^{c'x}$ on the full supporting interval in log coordinates. Applying this conclusion on four disjoint consecutive intervals of length $2S_b+\delta$ yields alternating signs. As in the [fixed-point argument](robin-lcm-short-nov18.md), an interior minimum and maximum of $J$ between those alternating peaks satisfy $-J(x_+)>2x_+^{c-1}$, $J(x_-)>2x_-^{c-1}$. The minimum has $\psi(x_+)=x_+$, and the maximum has $|\psi(x_-)-x_-|\le\log x_-$. The exact arithmetic identity then yields the asserted Robin signs. Any fixed log width greater than $8S_b$ suffices by taking $\delta$ small. Finally if no zero attains $\Theta$, the sets in the sum defining $S_b$ decrease to the empty set as $b\uparrow\Theta$. Dominated convergence using any fixed $b_0>1/2$ proves $S_b\to0$, so every prescribed positive window width is available.

In particular the number of distinct positive-violation fixed-point indices $N\le X$ from the theorem has positive lower growth rate after division by $\log X$. When $\Theta$ is unattained this quotient tends to infinity. Indeed for every allowed window width one may use disjoint logarithmic windows with gaps of the same width, guaranteeing distinct integer indices at sufficiently large scales. Let the width tend to zero in the unattained case. The same conclusion holds for the count of opposite-sign LCM values, since $\psi(x)\sim x$ separates LCM values on these geometrically separated windows.

### Numerical window factors high in the strip

The [directed density calculation](check_robin_density_nov18.py) also certifies $S_{13/16}<0.152$, $S_{7/8}<0.001282$, and $S_{31/32}<0.000000263$, even counting multiplicity. Indeed the verified height $H=3\cdot10^{12}$ gives $N(b,H)=0$, and partial summation gives $S_b\le\pi\int_H^\infty N(b,t)t^{-2}dt$. Each density majorant $A t^p(\log t)^k$ contributes at most $\pi A H^{p-1}(\log H)^k/(1-p-k/\log H)$ when the denominator is positive. The script uses the smaller of the two explicit Chourasiya–Simonič estimates recorded there. Thus if $\Theta>13/16$, every fixed $1/2<c<\Theta$ has both arithmetic witnesses in every sufficiently large $[Y/4,Y]$: raise $b$ above $c$ if needed, which decreases $S_b$. With $\Theta>7/8$ the ratio $4$ can be replaced by $1.011$, and with $\Theta>31/32$ by $1.0000022$. These factors concern the width only; the starting threshold for $Y$ is qualitative.
