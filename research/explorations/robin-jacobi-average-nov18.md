# A positive Jacobi-theta average for the integrated prime error

Put $R(v)=\psi(e^v)-e^v$, $d(v)=v^{-1}+v^{-2}$ and $J(e^x)=\int_x^\infty d(v)e^{-v}R(v)\,dv$. Write $A(e^x)$ for the same integral with $R(v)$ replaced by the archimedean term $-\log(2\pi)-\tfrac12\log(1-e^{-2v})$. For every fixed $D>0$ and every sufficiently large $X=e^t$ there is an explicit positive probability law $P_t$ supported in
$$
 [\log X-\tfrac12\log(C_D\log X),\ \log X+\tfrac12\log(C_D\log X)]
$$
such that
$$
 \left|\int (J(e^v)-A(e^v))\,dP_t(v)\right|\ll_D X^{-D}.
 \tag{1}
$$
The construction uses the integer theta series and $D$. It requires no zero enclosures. In particular some $x$ in $[X/\sqrt{C_D\log X},X\sqrt{C_D\log X}]$ satisfies $|J(x)-A(x)|\ll_D X^{-D}$ by continuity. Also $\int J(e^v)dP_t(v)\sim-\log(2\pi)/(X\log X)$.

## The positive kernel

Set $h(u)=\sum_{n\ge1}\exp(-\pi n^2e^{2u})$ and $K=h''+h'$. For $u\ge0$ this is the sum of $(4a^2-6a)e^{-a}$ with $a=\pi n^2e^{2u}\ge\pi$. It is strictly positive. The Jacobi relation $h(-u)=e^uh(u)+(e^u-1)/2$ implies $K(-u)=e^uK(u)$. Integration by parts twice, first at $\Re s>1$, yields the entire identity
$$
 \int_{\mathbb R}e^{su}K(u)du=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)=\xi(s).
$$
Take $\mu(du)=e^uK(u)du/\xi(1)$. This probability law has moments $\int e^{zu}\mu(du)=\xi(1+z)/\xi(1)$. In particular every nontrivial zero $\rho$ gives a vanishing moment at $z=\rho-1$. Uniformly for $-1\le\Re z\le0$ the two tails outside $[-S,S]$ cost $O(\exp(-\tfrac\pi2e^{2S}))$ when $S$ is large. This follows from the explicit series on the positive side and Jacobi reflection on the negative side.

Let $S=\frac12\log(C_Dt)$ and take $C_D$ large enough that the tail is $O(e^{-(D+2)t})$. Restrict $\mu$ to $[-S,S]$ and renormalize to get $\mu_t$. Its mass on $[0,1]$ stays bounded below. Thus for $w\ge0$,
$$
 L_t(w)=\int e^{ws}\mu_t(ds)\gg1,\qquad
 g_t(y)=\int_0^\infty(1+w)e^{-wy}/L_t(w)\,dw\ll d(y).
$$
Define $F_t(v)=0$ below $t-S$, and above it put
$$
 F_t(v)=d(v)^{-1}\int_{s\le v-t}g_t(v-s)\mu_t(ds).
$$
This is the distribution function of $P_t$. Indeed $F_t(v)$ averages the tilted probability $\int_{s\le v-t}e^{ws}\mu_t(ds)/L_t(w)$ against density $(1+w)e^{-vw}/d(v)$. The tilted probability decreases in $w$ and increases with the threshold. The distribution of $w$ decreases stochastically as $v$ increases. For $v\ge t+S$ every tilted probability is one.

For an individual zero the integrated explicit formula gives a summand $-\rho^{-1}\int_x^\infty d(v)e^{(\rho-1)v}dv$ in $J(e^x)-A(e^x)$. Its $P_t$-average equals
$$
 -\rho^{-1}\left(\int e^{(\rho-1)s}\mu_t(ds)\right)
                 \int_t^\infty g_t(y)e^{(\rho-1)y}dy
$$
by Fubini and translation. Since $g_t$ is positive decreasing, integration by parts bounds the last integral by $2g_t(t)e^{(\Re\rho-1)t}/|1-\rho|$. The first moment is $O(e^{-(D+2)t})$. Summing $1/(|\rho||1-\rho|)$ proves (1). The explicit formula and the absolute summability argument are given in the [finite Robin note](robin-finite-horizon-nov18.md); the positive lifting identity is from the [compact-kernel note](robin-lcm-positive-kernel-nov18.md).

For the main archimedean contribution substitute $\rho-1=-1$ in the separated integral without the factor $-1/\rho$. The first moment tends to $\xi(0)/\xi(1)=1$. Also $t g_t(t+r)\to1$ for fixed $r\ge0$ by scaling $w=a/t$, since $L_t(a/t)\to1$, its reciprocal stays bounded, and $S=o(t)$. Dominated convergence therefore gives $\int_t^\infty g_t(y)e^{-y}dy\sim e^{-t}/t$. The contribution from the remaining logarithmic term is $O(e^{-3(t-S)})$.

## A chosen zero and positive averages of opposite signs

For any nontrivial zero $\rho_0$ of multiplicity $m$, replace the transform $\xi(s)$ by $\xi(s)/(s-\rho_0)^m$. Its complex kernel $K_m$ obeys $|K_m(u)|\ll_{\rho_0}K(u)$. To verify this iterate $K_0=K$ and
$$
 K_{j+1}(u)=e^{-\rho_0u}\int_u^\infty e^{\rho_0v}K_j(v)dv
           =-e^{-\rho_0u}\int_{-\infty}^u e^{\rho_0v}K_j(v)dv
 \quad(0\le j<m).
$$
The equality uses the remaining zero of the transform at $\rho_0$. Integration by parts gives the required transform at each stage. On the positive tail $K(u)\asymp e^{4u}\exp(-\pi e^{2u})$, and on the negative tail use reflection. The corresponding one-sided integral bounds give $|K_{j+1}(u)|\ll e^{-2|u|}K(u)$ on the tails if $|K_j|\ll K$; on compact sets use strict positivity of $K$.

Use the strictly positive kernel $K+\epsilon\Re(e^{i\phi}K_m)$ with fixed sufficiently small $\epsilon>0$, normalize after multiplication by $e^u$, and truncate as above. All moments at nontrivial zeros vanish up to the same exponentially small tail, except at $\rho_0$ and $\bar\rho_0$. The target moment at $\rho_0$ equals a positive real normalization times $\epsilon e^{i\phi}\xi^{(m)}(\rho_0)/(2m!)$ up to that tail. The conjugate summand is its complex conjugate. Uniformly in $\phi$ the remaining integral at $\rho_0$ is
$$
 \int_t^\infty g_t(y)e^{(\rho_0-1)y}dy
 = \frac{e^{(\rho_0-1)t}}{t}\left(\frac1{1-\rho_0}+o(1)\right)
$$
by the same scaling and dominated convergence, since $\Re\rho_0<1$. Choosing the phase as a function of $t$ makes the leading real sum have either prescribed sign. This proves that in every window above $J$ takes both signs with magnitude $\gg_{\rho_0}X^{\Re\rho_0-1}/\log X$. In particular the first critical zero yields an unconditional two-sign estimate on every such window. The fixed-ratio result for off-line zeros in the compact-kernel note gives shorter windows, while the theta construction provides a positive arithmetic average isolating any chosen zero to inverse-power accuracy.
